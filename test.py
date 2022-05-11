from main import *
from time import sleep

sleep(2)

for i in range(10):
    with open('./sites.txt', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[1:])


    main()
    print(f'[+] test {i + 1}')

