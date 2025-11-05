import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from loguru import logger
import textwrap

net_bing_results_hrefs = []
net_bing_results_titles = []   #无需使用

def net_bing_task_no_client(search_content):
    logger.info('net_bing_task_no_client running ....')
    search_content_ = quote(search_content)
    net_bing_url = f'https://cn.bing.com/search?q={search_content_}'
    print(net_bing_url)
    try:
        r = requests.get(net_bing_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            # print(soup.prettify())
            column_results = soup.find_all('li',class_='b_algo')
            print(len(column_results))
            for o in column_results:
                o_soup = BeautifulSoup(str(o), 'lxml')

                title_describe_source = o_soup.find('p').text
                # print(title_describe_source)
                title_describe = textwrap.wrap(str(title_describe_source))
                print(title_describe)
                net_bing_results_titles.append(title_describe)

                result_href_source = o_soup.find('div',class_='b_tpcn')
                result_href_source_1 = result_href_source.find('a')
                result_href = result_href_source_1['href']
                print(result_href)
                net_bing_results_hrefs.append(result_href)
                print('90900909090' *20)

            return net_bing_results_hrefs,net_bing_results_titles

    except Exception as e:
        logger.error(e)

def net_bing_task_client(search_content,client_ip):
    logger.info('net_bing_task_client running ....')
    r_client = {
        'https' :f'http://{client_ip}',
        'http' :f'http://{client_ip}',
    }
    search_content_ = quote(search_content)
    net_bing_url = f'https://cn.bing.com/search?q={search_content_}'
    print(net_bing_url)
    try:
        r = requests.get(net_bing_url,proxies=r_client)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            # print(soup.prettify())
            column_results = soup.find_all('li', class_='b_algo')
            print(len(column_results))
            for o in column_results:
                o_soup = BeautifulSoup(str(o), 'lxml')

                title_describe_source = o_soup.find('p').text
                # print(title_describe_source)
                title_describe = textwrap.wrap(str(title_describe_source))
                print(title_describe)
                net_bing_results_titles.append(title_describe)

                result_href_source = o_soup.find('div', class_='b_tpcn')
                result_href_source_1 = result_href_source.find('a')
                result_href = result_href_source_1['href']
                print(result_href)
                net_bing_results_hrefs.append(result_href)
                print('90900909090' * 20)

            return net_bing_results_hrefs, net_bing_results_titles

    except Exception as e:
        logger.error(f'代理出错:{e}')


if __name__ == '__main__':
    net_bing_task_no_client(search_content='1233')
