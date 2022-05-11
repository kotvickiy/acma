from main import *
from time import sleep
from test_ip import get_info_by_ip
import platform
import os


sleep(2)
print(get_info_by_ip())
print(platform.system(), os.name)

for i in range(10):
    with open('./sites.txt', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[1:])


    main()
    print(f'[+] test {i + 1}')

