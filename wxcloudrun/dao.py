import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Counters, Jhscard

# 初始化日志
logger = logging.getLogger('log')


def query_jhs_card_byname(name):
    try:
        return Jhscard.query.filter(Jhscard.name == name).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def get_hot100_card_names():
    choices = []
    for card in Jhscard.select().order_by(Jhscard.init_price.desc()).limit(200):
        choices.append([card.name, card.card_version_id])
    return choices
