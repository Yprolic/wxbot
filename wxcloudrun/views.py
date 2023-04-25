import logging
import time
from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response

# 初始化日志
logger = logging.getLogger('log')


@app.route('/send/msg', methods=['POST'])
def send_msg():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()
    logger.info("GetMsg {0}, {1}".format(params, params.get('Content')))
    return make_succ_response({
        "ToUserName": params.get('FromUserName'),
        "FromUserName": params.get('ToUserName'),
        "CreateTime": time.time(),
        "MsgType": "text",
        "Content": "hello world"
    })
