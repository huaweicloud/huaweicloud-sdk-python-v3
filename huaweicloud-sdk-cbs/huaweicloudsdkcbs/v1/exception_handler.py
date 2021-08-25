# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class CbsError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    cbs_error = CbsError()

    cbs_error_dict = json.loads(response_body)
    for key in cbs_error_dict:
        if type(cbs_error_dict[key]) == dict and "error_code" in cbs_error_dict[key] and "error_msg" in \
                cbs_error_dict[key]:
            cbs_error = CbsError("2f9f4f57d2bc444cb4140c2d58a17508", cbs_error_dict[key]["error_code"], cbs_error_dict[key]["error_msg"])
    return cbs_error