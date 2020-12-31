import json

from huaweicloudsdkcore.exceptions import exceptions

class DgcError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    dgc_error = DgcError()

    dgc_error_dict = json.loads(response_body)
    for key in dgc_error_dict:
        if type(dgc_error_dict[key]) == dict and "error_code" in dgc_error_dict[key] and "error_msg" in \
                dgc_error_dict[key]:
            dgc_error = DgcError("0a04ffbcb5db120ce371f27e078e8980", dgc_error_dict[key]["error_code"], dgc_error_dict[key]["error_msg"])
    return dgc_error