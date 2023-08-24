import logging
from business.common import get_path

# 名称往往是app或者是对应模块的名称
logger = logging.getLogger("api_auto")
# 记录日志级别
# 设置日志级别为DEBUG，即只有日志级别大于等于DEBUG的日志才会输出，输出：debug/info/warning/error/cirtical
logger.setLevel(logging.DEBUG)

# 依次对应时间 级别 函数名
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')
# 在指定文件输出
fl = logging.FileHandler(filename=get_path()[2], mode='a', encoding='utf-8')
fl.setFormatter(formatter)
logger.addHandler(fl)

# 在命令行运行时输出
sl = logging.StreamHandler()
sl.setFormatter(formatter)
logger.addHandler(sl)
# message = "logger2"
# logger.info(message)

fl.close()
