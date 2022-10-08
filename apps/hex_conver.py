"""
python 10进制转16进制
负数的进制转换
正数的进制转换
"""
from loguru import logger


# 包含正负数的十进制转为16进制
def change_10_to_16():
    a = 15623
    if a > 0:
        c = hex(a)
        logger.info(f"正数进制转换...{c}")
    else:
        c = hex(-761755957 & 0xFFFFFFFF)
        logger.info(f"负数进制转换...{c}")


if __name__ == '__main__':
    change_10_to_16()


