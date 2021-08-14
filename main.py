#!/usr/bin/env python3
"""
pip install -r requirements.txt
"""
import requests
from bs4 import BeautifulSoup as bs
import os
from random import uniform
from time import sleep
from send_mail import send_email


def save(data):
    with open('/home/vlad405/public/acma/lst_sites.txt', 'w'):
        for i in data:
            with open('/home/vlad405/public/acma/lst_sites.txt', 'a', encoding='utf-8', newline='') as file:
                file.write('{}\n'.format(i))


def lst_old():
    with open('./lst_sites.txt', encoding='utf-8') as file:
        return [i.strip() for i in file.readlines()]


def get_html(url):
    cnt = 1
    while True:
        headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        response = requests.get(url, headers=headers)
        if response.ok:
            return response.text
        else:
            sec = uniform(50, 60)
            print('Ошибка сайта:', str(response.status_code) + ',', 'переподключение', str(int(sec)), 'секунд..', 'попытка', str(cnt))
            if cnt > 5:
                break
            cnt += 1
            sleep(sec)


def get_data(html):
    all_lst = []
    soup = bs(html, 'lxml')
    items = soup.find_all('div', class_='card-body')
    for item in items:
        lst = item.text.strip().split('\n')
        for i in lst:
            all_lst.append(i)
    
    return all_lst


def verify_news(url):
    ref_lst = lst_old()
    new_lst = get_data(get_html(url))

    freshs_lst = []
    for new in new_lst:
        if new not in ref_lst:
            freshs_lst.append(new)
    if freshs_lst:
        save(new_lst)
        send_email(freshs_lst)
    else:
        send_email(['Нет добавленного контента'])


def run(url):
    try:
        if os.path.exists('./lst_sites.txt'):
            verify_news(url)
        else:
            save(get_data(get_html(url)))
    except Exception as ex:
        print(ex)


def main():
    url = r'https://www.acma.gov.au/blocked-gambling-websites'  
    run(url)


if __name__ == "__main__":
    main()