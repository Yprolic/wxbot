import json
import logging
import time
import requests
from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid, \
    query_jhs_card_byname
from wxcloudrun.model import Counters
from wxcloudrun.response import json_response

# 初始化日志
logger = logging.getLogger('log')



x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
y = 'vkXupMNUJjiAGbwYnoclCFfQsKxyrETDWdVegPatzmLHhZIOqRBS'

decoder = str.maketrans(y, x)
host = 'dZZmh://xmV.eVdIxthdT.rza'.translate(decoder)


def encode(s):
    return s.translate(encoder)

def get_price(card_version_id):
    url = host + "/api/market/card-versions/products"
    params = {
        "card_version_id": card_version_id,
		"condition":     "1",
		'game_key': 'pkm',
        'game_sub_key': 'sc',
		'page':          1,
    }
    return requests.get(url, params=params).json()

@app.route('/send/msg', methods=['POST', 'GET'])
def send_msg():
    params = request.get_json()
    app.logger.info("GetMsg {0}, {1}".format(params, params.get('Content')))
    query = params.get('Content')
    jhs_card = query_jhs_card_byname(query)
    app.logger.info("Select {0}, {1}".format(jhs_card, query))
    if not jhs_card:
        answer = '对不起，没找到对应的卡'
    else:
        answer = json.dumps(get_price(jhs_card.card_version_id),ensure_ascii=False)
    msg = {
        "ToUserName": params.get('FromUserName'),
        "FromUserName": params.get('ToUserName'),
        "CreateTime": time.time(),
        "MsgType": "text",
        "Content": answer
    }
    return json_response(msg)
