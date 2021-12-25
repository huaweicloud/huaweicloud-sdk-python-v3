# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class SaError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    sa_error = SaError()

    sa_error_dict = json.loads(response_body)
    for key in sa_error_dict:
        if type(sa_error_dict[key]) == dict and "error_code" in sa_error_dict[key] and "error_msg" in \
                sa_error_dict[key]:
            sa_error = SaError("39d29606d49b483a9914c581ce190d54", sa_error_dict[key]["error_code"], sa_error_dict[key]["error_msg"])
    return sa_error