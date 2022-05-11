import requests
import http.client


def get_info_by_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = str(conn.getresponse().read())[2:-1]
    res = []
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        data = {
            '[IP]': response.get('query'),
            '[City]': response.get('city'),
            '[Org]': response.get('org')
            
        }
        
        for k, v in data.items():
            res.append(f'{k} : {v}')
        
        return res
        
    except requests.exceptions.ConnectionError:
        return '[!] Please check your connection!'
        
        
def main():
    print(*get_info_by_ip())
    
if __name__ == '__main__':
    main()
