from conf import configure, load_action, load_email
import sys
import logging.handlers
import logging
import platform
import os


log_format = ("[%(levelname)s]:%(name)s:%(asctime)s "
              "(%(filename)s:%(lineno)d %(funcName)s) "
              "%(message)s")
logger = logging.getLogger("HelloEmail")
logger.setLevel(logging.INFO)

if platform.system().lower() == 'windows':
    os.makedirs("./log", exist_ok=True)
    handle = logging.handlers.TimedRotatingFileHandler("./log/info.log",
                                                       when="d", backupCount=30, encoding='utf-8')
else:
    os.makedirs("/var/log/helloemail", exist_ok=True)
    handle = logging.handlers.TimedRotatingFileHandler("/var/log/helloemail/info.log",
                                                       when="d", backupCount=30, encoding='utf-8')

handle.setFormatter(logging.Formatter(log_format))
logger.addHandler(handle)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Tell me the conf file.")
        exit(1)

    conf = configure(sys.argv[1], logger)
    actions = load_action(conf, logger)
    emails = load_email(conf, actions, logger)
    for i in emails:
        i.send()
