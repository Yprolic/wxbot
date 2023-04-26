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


hot_names = None


def get_hot100_card_names():
    global hot_names
    if hot_names:
        return hot_names
    hot_names = []
    for card in Jhscard.select().order_by(Jhscard.init_price.desc()).limit(200):
        hot_names.append([card.name, card.card_version_id])
    return hot_names
