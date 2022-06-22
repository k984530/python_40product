import psutil

#CPU의 속도
cpu = psutil.cpu_freq()
print(f'cpu \n {cpu}')

#CPU의 물리코어 수
cpu_core = psutil.cpu_count(logical=False)
print(f'cpu_core \n {cpu_core}')

#메모리 정보
memory = psutil.virtual_memory()
print(f'memory \n {memory}')

#디스크 정보
disk = psutil.disk_partitions()
print(f"disk \n {disk}")

#네트워크를 통해 보내고 받은 데이터량
net = psutil.net_io_counters()
print(f"net \n {net}")