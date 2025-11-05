import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from loguru import logger

net_360_results_hrefs = []

def net_360_task_no_client(search_content):
    logger.info('net_360_task_no_client running.......')
    quote_search_content = quote(search_content)
    build_bai_du_url = f'https://www.so.com/s?ie=utf-8&shb=1&hsid=e6068993204486db&src=hao_360so_b_per_bdtest_sj&eci=&nlpv=&ssid=&cp=1c50000160&q={quote_search_content}'
    try:
        r = requests.get(build_bai_du_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            # print(soup.prettify())
            # with open('net_360.txt', 'w',encoding='utf-8') as f:
            #     f.write(str(soup))
            results = soup.find('ul',class_='result')
            # print(results)
            result_li_s = results.find_all('li',class_='res-list')
            print(len(result_li_s))
            for u in result_li_s:
                # print(u)
                u_soup = BeautifulSoup(str(u), 'lxml')
                try:
                    column_href_cite = u_soup.find('cite')
                    # print(column_href_cite)
                    column_href_cite_1 = column_href_cite.find('a')
                    # print(column_href_cite_1)
                    column_href = column_href_cite_1['href']
                    # print(column_href)
                    net_360_results_hrefs.append(column_href)
                except Exception as e:
                    logger.error(e)
                print('[[]]' *89)
            return net_360_results_hrefs

    except Exception as e:
        logger.error(e)

def net_360_task_client(search_content,client_ip):
    logger.info('net_360_task running.......')
    client_dict = {
        'http' : 'http://' + client_ip,
        'https' : 'https://' + client_ip,
    }
    quote_search_content = quote(search_content)
    build_bai_du_url = f'https://www.so.com/s?ie=utf-8&shb=1&hsid=e6068993204486db&src=hao_360so_b_per_bdtest_sj&eci=&nlpv=&ssid=&cp=1c50000160&q={quote_search_content}'
    try:
        r = requests.get(build_bai_du_url,proxies=client_dict)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            # print(soup.prettify())
            # with open('net_360.txt', 'w',encoding='utf-8') as f:
            #     f.write(str(soup))
            results = soup.find('ul', class_='result')
            # print(results)
            result_li_s = results.find_all('li', class_='res-list')
            print(len(result_li_s))
            for u in result_li_s:
                # print(u)
                u_soup = BeautifulSoup(str(u), 'lxml')
                try:
                    column_href_cite = u_soup.find('cite')
                    # print(column_href_cite)
                    column_href_cite_1 = column_href_cite.find('a')
                    # print(column_href_cite_1)
                    column_href = column_href_cite_1['href']
                    # print(column_href)
                    net_360_results_hrefs.append(column_href)
                except Exception as e:
                    logger.error(e)
                print('[[]]' * 89)
            return net_360_results_hrefs

    except Exception as e:
        logger.error(f'代理出错:{e}')

if __name__ == '__main__':
    net_360_task_no_client(search_content='123456')