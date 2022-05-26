#!/usr/bin/env python3.8
"""
________________________________
pip install -r requirements.txt
telegram: https://t.me/kotvickiy
________________________________
"""
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as bs
import os
from random import uniform
from time import sleep
from datetime import datetime
from send_mail import send_mail
from time import sleep


def save(data):
    with open('./sites.txt', 'w'):
        for i in data:
            with open('./sites.txt', 'a', encoding='utf-8', newline='') as file:
                file.write('{}\n'.format(i))


def lst_old():
    with open('./sites.txt', encoding='utf-8') as file:
        return [i.strip() for i in file.readlines()]


def get_html(url):    
    headers = {
        'authority': 'www.acma.gov.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'ak_bmsc=283CB0108107B534766E908AC6C613D5~000000000000000000000000000000~YAAQBDIQYGZIaIuAAQAAyC/6rQ9yFG7zlvyX5JPhJKpjvLL28TXM3xZVDST9dAscf+I34CXWWH2/30QMhBHWZ0CJ5+nVncWV8KW4/1WyBPPQfUUBYYpelpjI0gRizrawcdgqpzyoTSGbVt5TugBMYbe2h+bxpBPeIMWUolO8uwt71dO6S0xhB/ieDky3/7RaxBioEsaMskMS0KckKL1yD4otNQgwkpQphQ5n+FYjxv8hOykkD83vbFltmTSAifibijbvK/I2SZ9Lh4L8HSkXo3R5+oA9Rl4axMzayJFCIioepWobpYJnSJd2CTJqCfa1lq+bXvPMJytXDU4v90H9T8sHCO7/bF1a+HdtXIFlMMsYwPIMiTbhi61wiDCQlxdfSGErSEBohRpu; monsido=4091652186295277; bm_mi=B37A963BF388CE01C13BB82A0F6EDFC3~YAAQBDIQYFdKaIuAAQAALjoqrg+GHZLEO5L5hwut/1U9LeI0IrqaoNZe+n8WPBYL+KK7dAYKDCSMQG2MtLx8httceSBoIIkHHfcb6f7iGoMCV7yuXfuwc2TUXoAWKOhFJ6CxcanjIv6ZOBnqRsLMQ+jG6sB5+6WlQqg3d8ohFWJ1edk247RNucu+/cDfDgUoIzhCvEwNpbcxub07uxncQEOeiAl4LSni4n03Oi7SkQ7B/7EIcLxa2lGqU1vQJOth7llRUk2yZE1xvyB55xXaYLn7XItdBljBFZS4uF0xg2x8RNzvpO7PhFc5yd2/C1ZK3xra4Cenj8lbKVjIbIpwl1HaL/66Jp8O~1; bm_sv=8D73C7485E44951C88AAF47E4C8B7872~YAAQBDIQYFhKaIuAAQAALjoqrg8TXPmrIsaMHlVftHDqobzCJkFJmIDgkK6eK8+1xSOaG/vfX6FRsctwsMsJMCZNSUYn+AoU9Snn+H0HdakElaTls4lX+1ZEXjxpLdvWOjau8LVFEq13mlmG6A0N/dIJ2ZvyFzADogXVLm7UUR4c487FgK51TBaEEqy/62SZct7EV4RpNyVJNNzwy6TOnE603SwXSPkphnnSwisVs9uGvd4d+n2bbMOjBfPuoBWZRg==~1',
        'pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.text


def get_data(html):
    all_lst = []
    soup = bs(html, 'lxml')
    items = soup.find_all('div', class_='card-body')
    for item in items:
        lst = item.text.strip().split('\n')
        for i in lst:
            if i != ' ' and i != ' ' and i != '':
                all_lst.append(i)
    return all_lst


def save_last_time(data):
    with open('./time_last.txt', 'w') as file:
            file.write(f'{data}')


def last_time():
    with open('./time_last.txt') as file:
        reader = file.readline()
        return datetime.strptime(reader, '%Y-%m-%d %H:%M:%S.%f')


def verify_news(url):
    if not os.path.exists('./time_last.txt'):
        save_last_time(datetime.now())
    else:
        ref_lst = lst_old()
        new_lst = get_data(get_html(url))

        freshs_lst = []
        for new in new_lst:
            if new not in ref_lst:
                freshs_lst.append(new)
        if freshs_lst:
            save(new_lst)
            send_mail(freshs_lst, 'Австралия заблокировала ещё казино:', ['m@wmob.eu', 'zlokovar@gmail.com', 'kotvickiy@inbox.ru'])
            save_last_time(datetime.now())
        elif datetime.today().weekday() == 4 and int(datetime.now().strftime('%H')) == 15 and (datetime.now() - last_time()).days > 7:
            send_mail(['Новых казино в списке нет'], 'Скрипт по Австралии работает', ['m@wmob.eu', 'zlokovar@gmail.com', 'kotvickiy@inbox.ru'])
        else:
            print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, test --> [ok]")


def run(url):
    if os.path.exists('./sites.txt'):
        verify_news(url)
    else:
        save_last_time(datetime.now())
        save(get_data(get_html(url)))


def main():
    for i in range(25):
        try:
            url = r'https://www.acma.gov.au/blocked-gambling-websites'
            run(url)
            break
        except ConnectionError:
            sec = uniform(10, 20)
            print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, ConnectionError, reconnect: {sec} sec..")
            sleep(sec)
        except Exception as ex:
            sec = uniform(10, 20)
            print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}, main: {ex}, reconnect: {sec} sec..")
            sleep(sec)


if __name__ == "__main__":
    main()
