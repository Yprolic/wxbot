from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response


@app.route('/send/msg', methods=['POST'])
def send_msg():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    print("params")
    # return {
    #   "ToUserName": "用户OPENID",
    #   "FromUserName": "公众号/小程序原始ID",
    #   "CreateTime": "发送时间", // 整型，例如：1648014186
    #   "MsgType": "text",
    #   "Content": "文本消息"
    # }
    return
