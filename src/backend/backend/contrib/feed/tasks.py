from celery import shared_task
from feeds.utils import update_feeds

import logging


class Output(object):
    # little class for when we have no outputter
    def write(self, str):
        logging.info(str)



@shared_task
def get_those_feeds():
    # print(2)
    # the number is the max number of feeds to poll in one go
    update_feeds(30, Output())
