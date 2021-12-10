# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class ResError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    res_error = ResError()

    res_error_dict = json.loads(response_body)
    for key in res_error_dict:
        if type(res_error_dict[key]) == dict and "error_code" in res_error_dict[key] and "error_msg" in \
                res_error_dict[key]:
            res_error = ResError("0a04ffbcb5db120ce371f27e078e8980", res_error_dict[key]["error_code"], res_error_dict[key]["error_msg"])
    return res_error