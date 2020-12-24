# -*- coding: utf-8 -*-

import json
from huaweicloudsdkcore.exceptions import exceptions

class OcrError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    ocr_error = OcrError()

    ocr_error_dict = json.loads(response_body)
    for key in ocr_error_dict:
        if type(ocr_error_dict[key]) == dict and "error_code" in ocr_error_dict[key] and "error_msg" in \
                ocr_error_dict[key]:
            ocr_error = OcrError("057ee94bd280267e2ff7c01342e6d1e6", ocr_error_dict[key]["error_code"], ocr_error_dict[key]["error_msg"])
    return ocr_error