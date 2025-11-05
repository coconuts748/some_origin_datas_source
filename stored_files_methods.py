import json
from loguru import logger
import hashlib


def creat_json_file(writing_file_name,writing_content,whether_been_seen):
    try:
        with open(f'{writing_file_name}.json', 'wb') as f:
            f.write(json.dumps(writing_content, ensure_ascii=whether_been_seen).encode('utf-8'))
        logger.info('json file created successfully')

    except Exception as e:
        logger.error(e)

def creat_txt_file(writing_file_name,writing_content,whether_been_seen):
    if whether_been_seen == 'False':
        encrypt_writing_content = hashlib.md5(writing_content.encode('utf-8')).hexdigest()
        with open(f'{writing_file_name}.txt', 'w',encoding='utf-8') as f:
            f.write(encrypt_writing_content)
        logger.info('encrypted txt file created successfully')
    elif whether_been_seen == 'True':
        with open(f'{writing_file_name}.txt', 'w',encoding='utf-8') as f:
            f.write(writing_content)
        logger.info('unencrypted txt file created successfully')
    else:
        logger.error('输入参数无效！')