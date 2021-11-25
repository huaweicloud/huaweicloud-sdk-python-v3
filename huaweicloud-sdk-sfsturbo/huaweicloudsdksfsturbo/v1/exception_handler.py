# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions


class SfsturboError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    sfsturbo_error = SfsturboError()

    sfsturbo_error_dict = json.loads(response_body)
    for key in sfsturbo_error_dict:
        if type(sfsturbo_error_dict[key]) == dict and "error_code" in sfsturbo_error_dict[key] and "error_msg" in \
                sfsturbo_error_dict[key]:
            sfsturbo_error = SfsturboError("c7861e32-1154-4ee0-a16e-ab2323d4b030", sfsturbo_error_dict[key]["error_code"],
                                           sfsturbo_error_dict[key]["error_msg"])
    return sfsturbo_error