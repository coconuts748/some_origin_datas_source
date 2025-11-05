from urllib.parse import quote
import random
from loguru import logger
from 未完成.数据综合获取.net_bing_task import net_bing_task_no_client,net_bing_task_client
from 未完成.数据综合获取.net_360_task import net_360_task_no_client,net_360_task_client
from 未完成.数据综合获取.build_client_pool import useful_client_ips

def control_all_tasks(search_here,control_mode):
    def without_client():
        net_bing_task_no_client(search_content=search_here)
        net_360_task_no_client(search_content=search_here)

    def with_client():
        try:
            random_client_ip = random.choice(useful_client_ips)
            def inner_with_client():
                net_bing_task_client(search_content=search_here,client_ip=random_client_ip)
                net_360_task_client(search_content=search_here,client_ip=random_client_ip)
            inner_with_client()
        except Exception as e:
            logger.error(e)

    if control_mode == 'without_client':
        without_client()
    elif control_mode == 'with_client':
        with_client()
    else:
        pass
