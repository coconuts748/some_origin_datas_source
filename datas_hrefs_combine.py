from 未完成.数据综合获取.net_360_task import net_360_results_hrefs
from 未完成.数据综合获取.net_bing_task import net_bing_results_hrefs
from loguru import logger


combine_hrefs = []

def hrefs_combine():
    logger.info('hrefs_combine running...')
    for i in net_360_results_hrefs:
        combine_hrefs.append(i)
    logger.info('net_360_hrefs_combine add completed.')

    for u in net_bing_results_hrefs:
        combine_hrefs.append(u)
    logger.info('net_bing_hrefs_combine add completed.')

    return combine_hrefs


