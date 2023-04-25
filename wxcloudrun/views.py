import json
import logging
import time
from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid, \
    query_jhs_card_byname
from wxcloudrun.model import Counters
from wxcloudrun.response import json_response

# 初始化日志
logger = logging.getLogger('log')


@app.route('/send/msg', methods=['POST', 'GET'])
def send_msg():
    params = request.get_json()
    app.logger.info("GetMsg {0}, {1}".format(params, params.get('Content')))
    query = params.get('Content')
    x = query_jhs_card_byname(query)
    app.logger.info("Select {0}, {1}".format(x, query))
    answer = str(x.card_version_id)
    msg = {
        "ToUserName": params.get('FromUserName'),
        "FromUserName": params.get('ToUserName'),
        "CreateTime": time.time(),
        "MsgType": "text",
        "Content": answer
    }
    return json_response(msg)
