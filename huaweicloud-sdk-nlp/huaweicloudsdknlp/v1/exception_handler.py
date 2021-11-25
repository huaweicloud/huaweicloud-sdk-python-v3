# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class NlpError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    nlp_error = NlpError()

    nlp_error_dict = json.loads(response_body)
    for key in nlp_error_dict:
        if type(nlp_error_dict[key]) == dict and "error_code" in nlp_error_dict[key] and "error_msg" in \
                nlp_error_dict[key]:
            nlp_error = NlpError("087740ab9580d20c1fe5c002c64e11af", nlp_error_dict[key]["error_code"], nlp_error_dict[key]["error_msg"])
    return nlp_error