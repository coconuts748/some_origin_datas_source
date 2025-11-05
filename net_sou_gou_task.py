import requests
from bs4 import BeautifulSoup
from loguru import logger
from urllib.parse import quote

def net_sou_gou_task_no_client(search_content):
    logger.info('net_sou_gou_task running...')
    search_content_ = quote(search_content)
    sou_gou_url = f'https://www.sogou.com/sogou?query={search_content_}'
    logger.info(f'sou_gou_url: {sou_gou_url}')
    try:
        add_params = {
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding' : 'gzip, deflate, br, zstd',
            'accept-language' : 'zh-CN,zh;q=0.9',
            'cache-control' : 'no-cache',
            'connection': 'keep-alive',
            ####cookies..
            'host': 'www.sogou.com',
            'pragma':'no-cache',
            'sec-ch-ua' : '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform' : '"Windows"',
            'sec-fetch-dest' : 'document',
            'sec-fetch-mode' : 'navigate',
            'sec-fetch-site' : 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests' : '1',
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'


        }
        r = requests.get(sou_gou_url,params=add_params)
        if r.status_code == 200:
            logger.info(r.url)
            soup = BeautifulSoup(r.content, 'lxml')
            print(soup.prettify())

    except Exception as w:
        logger.error(w)


if __name__ == '__main__':
    net_sou_gou_task_no_client(search_content='aaa')
