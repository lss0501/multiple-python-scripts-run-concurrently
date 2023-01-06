import time
import logging
import os
import datetime

print(os.path.dirname(os.path.realpath(__file__)))


# OutPutPath = os.path.dirname(os.path.realpath(__file__))
OutPutPath = os.getcwd()
jobname = 'job3'
count = 0


logger = logging.getLogger('%s'%jobname)
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('%s/logs/%s.log'%(OutPutPath,jobname))
fh.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)



while  True:
    print(count)
    current_time = datetime.datetime.now()
    logger.info('%s %s'%(count, current_time))
    count += 1
    time.sleep(2)
    if count == 50:
        break
