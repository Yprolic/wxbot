import json
import logging
import time
from datetime import datetime
from flask import render_template, request, Response
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response

# 初始化日志
logger = logging.getLogger('log')


@app.route('/send/msg', methods=['POST', 'GET'])
def send_msg():
    """
    :return:计数结果/清除结果
    """
    # 获取请求体参数
    params = request.get_json()
    # {'ToUserName': 'gh_0718258bf74f', 'FromUserName': 'oFZKD6mGVnsvdwpG8xYTMbzqM5uU', 'CreateTime': 1682422800,
    #  'MsgType': 'text', 'Content': '是', 'MsgId': 24086505433696505}
    app.logger.info("GetMsg {0}, {1}".format(params, params.get('Content')))
    msg = {
        "ToUserName": params.get('FromUserName'),
        "FromUserName": params.get('ToUserName'),
        "CreateTime": time.time(),
        "MsgType": "text",
        "Content": "hello world"
    }
    data = json.dumps(msg)
    return Response(data, mimetype='application/json')
    # return make_succ_response({
    #     "ToUserName": params.get('FromUserName'),
    #     "FromUserName": params.get('ToUserName'),
    #     "CreateTime": time.time(),
    #     "MsgType": "text",
    #     "Content": "hello world"
    # })
