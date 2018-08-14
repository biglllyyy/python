from docker import DockerClient

client = DockerClient(base_url='tcp://10.3.236.237:8080')

client.version()