import json

from huaweicloudsdkcore.exceptions import exceptions

class KpsError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    kps_error = KpsError()

    kps_error_dict = json.loads(response_body)
    for key in kps_error_dict:
        if type(kps_error_dict[key]) == dict and "error_code" in kps_error_dict[key] and "error_msg" in \
                kps_error_dict[key]:
            kps_error = KpsError("0a04ffbcb5db120ce371f27e078e8980", kps_error_dict[key]["error_code"], kps_error_dict[key]["error_msg"])
    return kps_error