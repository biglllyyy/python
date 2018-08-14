#!/bin/bash
#crontab_sql.sh
#date 2017-09-15
#version 1.0

source /home/config.cnf
echo -e "执行时间：`date`\n" > /tmp/DCE_CHECK.txt

#ORIG数据库大小和条数
ORIG_MYSQL_STATISTICS() {
echo "统计ORIG数据库大小和条数：" >> /tmp/DCE_CHECK.txt
date=`date +%Y_%m`
table_name=t_raw_$date
let day=(`date +%d`/7+1)
if [ ${day} -gt 4 ]
then
   day=4
fi
table_name=${table_name}_w0${day}
sql[0]="select concat(round(sum((data_length+index_length)/1024/1024/1024),2),'GB') as database_size from tables where table_schema='raw_data_storage' \G;"
sql[1]="select concat(round((data_length+index_length)/1024/1024/1024,2),'GB') as ${table_name}_size from tables where table_schema='raw_data_storage' and table_name = '${table_name}' \G;"
sql[2]="SELECT count(*) as ${table_name}_count from raw_data_storage.${table_name} \G;"
sql[3]="select concat(round((data_length+index_length)/1024/1024,2),'MB') as nev_forward_check from tables where table_schema = 'nev_forward_check' and table_name = 't_forward_local_record' \G;"
sql[4]="SELECT count(*) as nev_forward_check_count from  nev_forward_check.t_forward_local_record \G;"
sql[5]="select concat(round((data_length+index_length)/1024/1024,2),'MB') as nev_local_check from tables where table_schema = 'nev_local_check' and table_name = 't_forward_local_record' \G;"
sql[6]="SELECT count(*) as nev_local_check_count from  nev_local_check.t_forward_local_record \G;"
for i in {0..6};
do
	/usr/bin/mysql -u${MYSQL_USER} -p${MYSQL_PW} -h10.99.6.41 -P${ORIG_MYSQL_MASTER_PORT}  -e "use information_schema;${sql[$i]}" >> /tmp/DCE_CHECK.txt
echo "" >> /tmp/DCE_CHECK.txt
done
echo "" >> /tmp/DCE_CHECK.txt
}

#MGMT数据大小和条数
MGMT_MYSQL_STATISTICS() {
echo "统计MGMT数据库大小和条数：" >> /tmp/DCE_CHECK.txt
arr=$1
for i in ${arr[*]};
do
        if [ "$i" = "database_car" ];then
		sql3="select count(*) as 车辆总数 from vehicle_info\G"
	elif [ "$i" = "nev_alarm_data" ];then
		sql3="select count(*) as 报警总次数 from t_alarm_data\G"
        else
           echo "database name error!"
	fi
        /usr/bin/mysql -u${MYSQL_USER} -p${MYSQL_PW} -h${HOST} -P${2}  -e "use '$i';${sql3}" >> /tmp/DCE_CHECK.txt
done
echo "" >> /tmp/DCE_CHECK.txt
}

#检查slave集群状态
MYSQL_SLAVE_STATUS() {
echo "MYSQL SLAVE STATUS:" >> /tmp/DCE_CHECK.txt
    string[0]='Slave_SQL_Running:'
    string[1]='Slave_IO_Running:'
    string[2]='Seconds_Behind_Master:'
    echo -e "mysql_host:${HOST} \n mysql_port:${1}" >> /tmp/DCE_CHECK.txt
    for i in {0..2};
    do
	/usr/bin/mysql -u${MYSQL_USER} -p${MYSQL_PW} -h${HOST} -P${1}  -e "show slave status\G"|grep "${string[$i]}" >> /tmp/DCE_CHECK.txt
    done
echo "" >> /tmp/DCE_CHECK.txt
}

#检查slave集群状态
ORGI_MYSQL_SLAVE_STATUS() {
    string[0]='Slave_SQL_Running:'
    string[1]='Slave_IO_Running:'
    string[2]='Seconds_Behind_Master:'
    echo -e "mysql_host:${1} \n mysql_port:${2}" >> /tmp/DCE_CHECK.txt
    for i in {0..2};
    do
        /usr/bin/mysql -u${MYSQL_USER} -p${MYSQL_PW} -h${1} -P${2}  -e "show slave status\G"|grep "${string[$i]}" >> /tmp/DCE_CHECK.txt
    done
echo "" >> /tmp/DCE_CHECK.txt
}

#mongodb状态统计
MONGODB_STATUS() {
echo  "${1}状态统计：" >> /tmp/DCE_CHECK.txt
mongostat -h ${HOST} --port ${2} -n 2 1 >> /tmp/DCE_CHECK.txt
echo "" >> /tmp/DCE_CHECK.txt
}

#检查磁盘
DISK_CHECK() {
echo "应用磁盘空间统计:" >> /tmp/DCE_CHECK.txt
for i in ${IP_LIST[*]};
 do
    echo "--------------------------------------------${i}--------------------------------------------" >> /tmp/DCE_CHECK.txt
    ssh ${i} 'df -h|grep px|grep -v You' >> /tmp/DCE_CHECK.txt
    echo "" >>  /tmp/DCE_CHECK.txt
 done
echo -e "\n系统磁盘空间统计:" >> /tmp/DCE_CHECK.txt
for i in ${IP_LIST[*]};
 do
    echo "--------------------------------------------${i}--------------------------------------------" >> /tmp/DCE_CHECK.txt
    ssh ${i} 'df -h|grep -v px|grep -v "/var/lib/docker"|grep -v Filesystem' >> /tmp/DCE_CHECK.txt
    echo "" >>  /tmp/DCE_CHECK.txt
 done
}

#检查负载
CPU_MEM_CHECK() {
echo  "每台服务器top统计:" >> /tmp/DCE_CHECK.txt
for i in ${IP_LIST[*]};
do
    echo "--------------------------------------------${i}--------------------------------------------" >> /tmp/DCE_CHECK.txt
    ssh ${i} 'top -bcn 1|head -n 5' >> /tmp/DCE_CHECK.txt
    echo "" >> /tmp/DCE_CHECK.txt
done
echo "" >> /tmp/DCE_CHECK.txt
}

#redis服务状态
REDIS_SERVICE_STATUS() {
echo "redis service check:" >> /tmp/DCE_CHECK.txt
   status=`echo 'ping'|redis-cli -h ${HOST} -p ${2}`
   if [ ${status} = 'PONG' ];then
	echo "${1}服务可用！"  >> /tmp/DCE_CHECK.txt
   else
	echo "${1}服务异常，请检查！" >> /tmp/DCE_CHECK.txt
   fi
echo "" >> /tmp/DCE_CHECK.txt
}

#redis集群状态
REDIS_SENTINEL_STATUS() {
echo "redis sentinel check:" >> /tmp/DCE_CHECK.txt
redis-cli  -h ${HOST} -p ${2} -r 1 -i 1 info |tail -n 1 >> /tmp/DCE_CHECK.txt
echo "" >> /tmp/DCE_CHECK.txt
}

#zookeeper+kakfa状态
KAFKA_TOPIC_LIST() {
count=`kafka-topics.sh --list --zookeeper ${HOST}:${2}|wc -l`
echo "${1} topic list count:" ${count} >>  /tmp/DCE_CHECK.txt
echo "" >> /tmp/DCE_CHECK.txt
}

FORWARD_CHECK() {
id=`ssh ${HOST} "docker ps|grep ${1}"|awk '{print $1}'`
date=`date -d '1 days ago' +%Y-%m-%d`
count=`ssh ${HOST} "docker exec ${id} sh -c 'cat /usr/src/myapp/logs/logFile.${date}.log'|grep ${2} |wc -l"`

echo "${2}：${count}" >> /tmp/DCE_CHECK.txt
echo "" >> /tmp/DCE_CHECK.txt
}

#检查备份
BACKUP_CHECK() {
WEEKNUM=`date +%V`
WEEKDAY=`date +%u`
arr=$1
size=`ssh 10.99.6.40 "du -sh /data/backup/${WEEKNUM}/${WEEKDAY}"`
echo "原始数据库今天备份为:${size}" >> /tmp/DCE_CHECK.txt
echo "车辆信息数据库备份为：" >> /tmp/DCE_CHECK.txt
for i in ${arr[*]};
do
   ssh 10.99.6.38 "ls -r /mysql_backup/mgmt_mysql/${i}/*.tar.gz|head -n 1|xargs du -sh" >> /tmp/DCE_CHECK.txt
done
echo "" >> /tmp/DCE_CHECK.txt
}

#根据服务获得host
RETURN_HOST() {
   HOST=`ssh 10.99.6.5 docker service ps $1|grep Running|awk '{print $4}'`
}

#px_check
PX_CHECK() {
echo "PX卷磁盘检查：" >> /tmp/DCE_CHECK.txt
arr=$1
for i in ${arr[*]};
do
   echo ${i} >> /tmp/DCE_CHECK.txt
   ssh ${i} "df -h|grep px"|awk '{print $1}' > /tmp/disk_check.log
   for line in `cat /tmp/disk_check.log`
   do
   echo ${line} >> /tmp/DCE_CHECK.txt
   ssh ${i} "dumpe2fs ${line}|grep 'Filesystem state'" >> /tmp/DCE_CHECK.txt
   sleep 1
   done
   echo "" >> /tmp/DCE_CHECK.txt
done
}

#px_size
PX_SIZE() {
echo "PX大小检查：" >> /tmp/DCE_CHECK.txt
arr=$1
for i in ${arr[*]};
do
   echo ${i} >> /tmp/DCE_CHECK.txt
   ssh ${i} "btrfs fi show" >> /tmp/DCE_CHECK.txt
done
echo "" >> /tmp/DCE_CHECK.txt
}

#数据库统计
RETURN_HOST ${MGMT_MYSQL_SLAVE_SERVICE}
MGMT_MYSQL_STATISTICS "${MGMT_MYSQL_DATABASE_LIST[*]}" ${MGMT_MYSQL_SLAVE_PORT}
ORIG_MYSQL_STATISTICS

#统计mysql slave状态
RETURN_HOST ${MGMT_MYSQL_SLAVE_SERVICE}
MYSQL_SLAVE_STATUS ${MGMT_MYSQL_SLAVE_PORT}
ORGI_MYSQL_SLAVE_STATUS ${ORIG_MYSQL_SLAVE_SERVICE} ${ORIG_MYSQL_SLAVE_PORT}

#mongodb状态统计
RETURN_HOST ${MONGODB_SERVICE_01}
MONGODB_STATUS ${MONGODB_SERVICE_01} ${MONGODB_PORT_01}
RETURN_HOST ${MONGODB_SERVICE_02}
MONGODB_STATUS ${MONGODB_SERVICE_02} ${MONGODB_PORT_02}
RETURN_HOST ${MONGODB_SERVICE_03}
MONGODB_STATUS ${MONGODB_SERVICE_03} ${MONGODB_PORT_03}

#数据库备份
BACKUP_CHECK "${MGMT_MYSQL_DATABASE_LIST2[*]}"

#redis
RETURN_HOST ${REDIS_SERVICE_HAPROXY_01}
REDIS_SERVICE_STATUS ${REDIS_SERVICE_HAPROXY_01} ${REDIS_PORT_HAPROXY_01}
RETURN_HOST ${REDIS_SERVICE_HAPROXY_02}
REDIS_SERVICE_STATUS ${REDIS_SERVICE_HAPROXY_02} ${REDIS_PORT_HAPROXY_02}

RETURN_HOST ${REDIS_SERVICE_SENTINEL_01}
REDIS_SENTINEL_STATUS ${REDIS_SERVICE_SENTINEL_01} ${REDIS_PORT_SENTINEL_01}
RETURN_HOST ${REDIS_SERVICE_SENTINEL_02}
REDIS_SENTINEL_STATUS ${REDIS_SERVICE_SENTINEL_02} ${REDIS_PORT_SENTINEL_02}

#zookeeper+kakfa状态
RETURN_HOST ${ZOOKEEPER_SERVICE_01}
KAFKA_TOPIC_LIST ${ZOOKEEPER_SERVICE_01} ${ZOOKEEPER_PORT_01}
RETURN_HOST ${ZOOKEEPER_SERVICE_02}
KAFKA_TOPIC_LIST ${ZOOKEEPER_SERVICE_02} ${ZOOKEEPER_PORT_02}
RETURN_HOST ${ZOOKEEPER_SERVICE_03}
KAFKA_TOPIC_LIST ${ZOOKEEPER_SERVICE_03} ${ZOOKEEPER_PORT_03}

#检查重连次数
RETURN_HOST ${NEV_FORWARD_SERVICE}
FORWARD_CHECK ${FORWARD_SERVICE_NAME} "上海地标平台"
FORWARD_CHECK ${FORWARD_SERVICE_NAME} "昆明地标平台"
FORWARD_CHECK ${FORWARD_SERVICE_NAME} "北京地标平台"

RETURN_HOST ${NEV_LOCAL_SERVICE}
FORWARD_CHECK ${LOCAL_SERVICE_NAME} "云汽国网平台"
FORWARD_CHECK ${LOCAL_SERVICE_NAME} "东风国网平台"

#检查负载
CPU_MEM_CHECK

#px检查
PX_CHECK "${IP_LIST_DCE[*]}"

#px size check
PX_SIZE "${IP_LIST_DCE[*]}"

#磁盘统计
DISK_CHECK

sed -i 's/^ *//' /tmp/DCE_CHECK.txt
sed -i '/1. row/d' /tmp/DCE_CHECK.txt