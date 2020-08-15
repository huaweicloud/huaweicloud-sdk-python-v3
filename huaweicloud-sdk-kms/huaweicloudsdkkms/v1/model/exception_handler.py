import json

from huaweicloudsdkcore.exceptions import exceptions

class KmsError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    kms_error = KmsError()

    kms_error_dict = json.loads(response_body)
    for key in kms_error_dict:
        if type(kms_error_dict[key]) == dict and "error_code" in kms_error_dict[key] and "error_msg" in \
                kms_error_dict[key]:
            kms_error = KmsError("0a04ffbcb5db120ce371f27e078e8980", kms_error_dict[key]["error_code"], kms_error_dict[key]["error_msg"])
    return kms_error