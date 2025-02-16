import json
import logging
import time
import requests
from thefuzz import process

from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import query_jhs_card_byname, get_hot100_card_names
from wxcloudrun.response import json_response

# 初始化日志
logger = logging.getLogger('log')

x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
y = 'vkXupMNUJjiAGbwYnoclCFfQsKxyrETDWdVegPatzmLHhZIOqRBS'

decoder = str.maketrans(y, x)
host = 'dZZmh://xmV.eVdIxthdT.rza'.translate(decoder)


def get_price(card_version_id):
    url = host + "/api/market/card-versions/products"
    params = {
        "card_version_id": card_version_id,
        "condition": "1",
        'game_key': 'pkm',
        'game_sub_key': 'sc',
        'page': 1,
    }
    resp = requests.get(url, params=params)
    app.logger.info("search {0}, {1}".format(card_version_id, resp))
    return resp.json()


def format_price_resp(r):
    top10price = []
    for d in r.get('data'):
        top10price.append(str(int(float(d.get('min_price')))))
    return '总挂单量为:{0}\n前10挂单分别为:{1}'.format(r.get('total'), ','.join(top10price))


@app.route('/send/msg', methods=['POST', 'GET'])
def send_msg():
    params = request.get_json()
    app.logger.info("GetMsg {0}, {1}".format(params, params.get('Content')))
    query = params.get('Content')
    jhs_card = query_jhs_card_byname(query)
    app.logger.info("Select {0}, {1}".format(jhs_card, query))
    if not jhs_card:
        match_card, score = process.extractOne(query, get_hot100_card_names())
        if score < 0.5:
            answer = u'对不起，没找到对应的卡'
        else:
            answer = '您要找的是: {} 么?'.format(match_card[0])
            answer += format_price_resp(get_price(match_card[1]))
    else:
        answer = format_price_resp(get_price(jhs_card.card_version_id))
        app.logger.info("Answer {0}".format(answer))
    msg = {
        "ToUserName": params.get('FromUserName'),
        "FromUserName": params.get('ToUserName'),
        "CreateTime": time.time(),
        "MsgType": "text",
        "Content": answer
    }
    return json_response(msg)
