import textwrap
from 未完成.数据综合获取.datas_hrefs_combine import combine_hrefs
from 未完成.数据综合获取.build_client_pool import useful_client_ips
import requests
import random
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from loguru import logger

all_hrefs_doc_content = []

def further_tidy_up_datas(tidy_mode):
    def inner_further_tidy_up_datas_without_client():
        logger.info('inner_further_tidy_up_datas_without_client running...')
        try:
            async def get_all_hrefs_data(async_url_here):
                logger.info(f'访问链接为{async_url_here}....')
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{async_url_here}') as response:
                        logger.info('当前访问的网址为:{}'.format(response.url))
                        if response.status == 200:
                            try:
                                load = BeautifulSoup(str(await response.text()), 'lxml')
                                load_text = textwrap.wrap(str(load.text))
                                all_hrefs_doc_content.append(load_text)

                                logger.info(load_text)
                                return all_hrefs_doc_content

                            except Exception as y:
                                logger.error(y)

            async def transmit_url(transmit_url___):
                logger.info('transmit_url running...')

                await get_all_hrefs_data(async_url_here=transmit_url___)

            loop_without_client = asyncio.get_event_loop()
            tasks_without_client = []
            for single_task in combine_hrefs:
                logger.info('single_task creating...')
                tasks_without_client.append(asyncio.ensure_future(transmit_url(single_task)))

            loop_without_client.run_until_complete(asyncio.wait(tasks_without_client))
        except Exception as e:
            logger.error(e)

    def inner_further_tidy_up_datas_with_client():
        logger.info('inner_further_tidy_up_datas_with_client running...')
        async def with_client(async_url_here):
            async with aiohttp.ClientSession() as session:
                try:
                    random_client = random.choice(useful_client_ips)
                    client_dic = {
                        'http': 'http://{}'.format(random_client),
                        'https': 'http://{}'.format(random_client)
                    }
                    async with session.get(async_url_here, proxy=client_dic) as response:
                        load_doc = BeautifulSoup(await response.text(), 'lxml')
                        load_doc_text = textwrap.wrap(str(load_doc.text))

                        logger.info(load_doc_text)
                        return load_doc_text
                except Exception as e:
                    logger.error(e)


        async def transmit_url_with_client(transmit_url___):
            await with_client(async_url_here=transmit_url___)

        loop_with_client = asyncio.get_event_loop()
        tasks_with_client = []
        for single_task in combine_hrefs:
            logger.info('single_task creating...')
            tasks_with_client.append(asyncio.ensure_future(transmit_url_with_client(single_task)))

        logger.info('all tasks created successfully...')
        loop_with_client.run_until_complete(asyncio.wait(tasks_with_client))

    if tidy_mode == 'without_client':
        inner_further_tidy_up_datas_without_client()
    elif tidy_mode == 'with_client':
        inner_further_tidy_up_datas_with_client()
    else:
        pass




