import json

from huaweicloudsdkcore.exceptions import exceptions

class MrsError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    mrs_error = MrsError()

    mrs_error_dict = json.loads(response_body)
    for key in mrs_error_dict:
        if type(mrs_error_dict[key]) == dict and "error_code" in mrs_error_dict[key] and "error_msg" in \
                mrs_error_dict[key]:
            mrs_error = MrsError("0a04ffbcb5db120ce371f27e078e8980", mrs_error_dict[key]["error_code"], mrs_error_dict[key]["error_msg"])
    return mrs_error