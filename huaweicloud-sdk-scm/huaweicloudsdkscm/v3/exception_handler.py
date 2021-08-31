import json

from huaweicloudsdkcore.exceptions import exceptions

class ScmError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    scm_error = ScmError()

    scm_error_dict = json.loads(response_body)
    for key in scm_error_dict:
        if type(scm_error_dict[key]) == dict and "error_code" in scm_error_dict[key] and "error_msg" in \
                scm_error_dict[key]:
            scm_error = ScmError("0a04ffbcb5db120ce371f27e078e8980", scm_error_dict[key]["error_code"], scm_error_dict[key]["error_msg"])
    return scm_error