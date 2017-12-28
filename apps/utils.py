import hashlib

def md5(strs):
    m2=hashlib.md5()
    m2.update(strs.encode('utf8'))
    return m2.hexdigest()

def verifyMd5(strs,hash_strs):
    if md5(strs)==hash_strs:
        return True
    else:
        return False


import logging


#日志打印模板
def getLogger():
    logger = logging.getLogger("Debuger")
    logger.setLevel(logging.DEBUG)
    dh=logging.FileHandler("F:/pypro")
    ## '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dh.setFormatter(formatter)

    logger.addHandler(dh)
    return  logger


print(md5("xidosfod"))