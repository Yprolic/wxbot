import json

from flask import Response


def json_response(raw_data):
    data = json.dumps(raw_data, ensure_ascii=False)
    return Response(data, mimetype='application/json')
