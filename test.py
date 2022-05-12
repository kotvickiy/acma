from main import *
import http.client
import socket


def get_info_by_ip():
    try:
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        ip = str(conn.getresponse().read())[2:-1]
        res = []
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[City]': response.get('city'),
            '[Org]': response.get('org')         
        }    
        for k, v in data.items():
            res.append(f'{k} : {v}')
        if res:
            print(*res)
        else:
            print(res)
    except Exception as ex:
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, get_info_by_ip: {ex}")
        get_info_by_ip()

try:
    get_info_by_ip()
except socket.gaierror:
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, test: socket.gaierror")
    get_info_by_ip()
except ConnectionError:
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, test: ConnectionError")
    get_info_by_ip()
except Exception as ex:
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, test: {ex}")
    get_info_by_ip()


for i in range(10):
    with open('./sites.txt', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[1:])
    main()
    print(f'[+] test {i + 1}')
