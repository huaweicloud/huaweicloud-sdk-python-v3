import json

from huaweicloudsdkcore.exceptions import exceptions

class CcmError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    pca_error = CcmError()

    pca_error_dict = json.loads(response_body)
    for key in pca_error_dict:
        if type(pca_error_dict[key]) == dict and "error_code" in pca_error_dict[key] and "error_msg" in \
                pca_error_dict[key]:
            pca_error = PcaError("0a04ffbcb5db120ce371f27e078e8980", pca_error_dict[key]["error_code"], pca_error_dict[key]["error_msg"])
    return pca_error