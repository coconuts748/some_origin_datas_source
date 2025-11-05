import requests
from loguru import logger
import random

origin_client_ips = []
useful_client_ips = []

def build_client_pool(api_source):
    logger.info('build_client_pool running...')

    def get_total_ip_port():
        logger.info('get_total_ip_port running...')
        try:
            r = requests.get(api_source)
            if r.status_code == 200:
                r_json = r.json()
                r_data = r_json['data']
                r_proxy = r_data['proxy_list']
                for single_client_proxy in r_proxy:
                    ip_source = single_client_proxy['ip']
                    ip_port = single_client_proxy['port']
                    full_client_ip = f'{ip_source}:{ip_port}'
                    origin_client_ips.append(full_client_ip)
                    logger.info(f'代理{full_client_ip}已成功添加!')
                logger.info('所有原始代理添加成功!')
                return origin_client_ips

            else:
                logger.error('代理链接失效')

        except Exception as e:
            logger.error(e)

    def versify_whether_could_be_used():
        logger.info('versify_whether_could_be_used running...')
        versify_url_list = []
        versify_url_list.append('https://baidu.com/')
        versify_url_list.append('https://cn.bing.com/')
        versify_url_list.append('https://zhihu.sogou.com/')
        try:
            logger.info('验证代理可用性中.....')
            for i in origin_client_ips:
                versify_proxy_dic = {
                    'https': f'http://{i}',
                    'http': f'http://{i}',
                }
                test_url = random.choice(versify_url_list)
                r = requests.get(test_url, proxies=versify_proxy_dic)

                if r.status_code == 200:
                    logger.info(f'代理:{i}可用!')
                    useful_client_ips.append(i)
                else:
                    continue
            return useful_client_ips

        except Exception as e:
            logger.error(e)

    def build_client_pool_running_sequence():   #可调试
        get_total_ip_port()
        versify_whether_could_be_used()

    build_client_pool_running_sequence()

if __name__ == '__main__':
    #####'http://www.zdopen.com/ShortProxy/GetIP/?api=202510311958171072&akey=e435d5dde45154ec&count={??????}}&fitter=1&timespan=5&type=3'################
    build_client_pool(api_source='http://www.zdopen.com/ShortProxy/GetIP/?api=202510311958171072&akey=e435d5dde45154ec&count=10}&fitter=1&timespan=5&type=3')
