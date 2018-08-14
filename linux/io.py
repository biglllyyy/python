import os

#查询容器的PID
a = os.system("docker service ls |grep dce-plugin_zabbix | awk '{print $1}'").__str__()

#根据查询的service PID，找到运行在哪台主机上面
b = os.system("docker service ps %s | awk '{print $5}'"%(a))

if b == 'Running':
    PID = b

#ssh发送指令到对应主机，并获取容器运行在对应主机的PID


# 根据主机返回的PID，查询对应容器的流量



