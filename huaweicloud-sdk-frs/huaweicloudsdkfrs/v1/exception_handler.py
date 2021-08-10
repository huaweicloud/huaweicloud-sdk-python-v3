# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class FrsError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    frs_error = FrsError()

    frs_error_dict = json.loads(response_body)
    for key in frs_error_dict:
        if type(frs_error_dict[key]) == dict and "error_code" in frs_error_dict[key] and "error_msg" in \
                frs_error_dict[key]:
            frs_error = FrsError("057ee94bd280267e2ff7c01342e6d1e6", frs_error_dict[key]["error_code"], frs_error_dict[key]["error_msg"])
    return frs_error