#from pymongo import Connection, ASCENDING, DESCENDING
from sofia.config import (
#  DB_HOST, DB_USERNAME, DB_PASSWORD,
  QUEUE_HOST_PORT
)

import logging
import sys
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

import stomp
import json

## Enable this when we need a DB
#CONNECTION = Connection(DB_HOST)
#DB = CONNECTION.sofia
#DB.authenticate(DB_USERNAME, DB_PASSWORD)

#DB.modules.ensure_index('updated')
#DB.queue.ensure_index([('priority', DESCENDING), ('updated', ASCENDING)])

class Dispatcher(object):
    def on_error(self, headers, message):
        logger.error(message)

    def on_message(self, headers, message):
        obj = json.loads(message)

conn = stomp.Connection([QUEUE_HOST_PORT])
dispatcher = Dispatcher()
conn.set_listener('', dispatcher)
conn.start()
conn.connect(wait=True)
logger.info('Started')
