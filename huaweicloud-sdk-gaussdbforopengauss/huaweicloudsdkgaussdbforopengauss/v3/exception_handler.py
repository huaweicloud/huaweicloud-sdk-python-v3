import json

from huaweicloudsdkcore.exceptions import exceptions

class openGaussError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    openGauss_error = openGaussError()

    openGauss_error_dict = json.loads(response_body)
    for key in openGauss_error_dict:
        if type(openGauss_error_dict[key]) == dict and "error_code" in openGauss_error_dict[key] and "error_msg" in \
                openGauss_error_dict[key]:
            openGauss_error = openGaussError("0a04ffbcb5db120ce371f27e078e8980", openGauss_error_dict[key]["error_code"], openGauss_error_dict[key]["error_msg"])
    return openGauss_error