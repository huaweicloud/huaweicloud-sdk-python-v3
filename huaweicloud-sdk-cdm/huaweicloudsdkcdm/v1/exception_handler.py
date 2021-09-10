import json

from huaweicloudsdkcore.exceptions import exceptions

class CdmError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    cdm_error = CdmError()

    cdm_error_dict = json.loads(response_body)
    for key in cdm_error_dict:
        if type(cdm_error_dict[key]) == dict and "error_code" in cdm_error_dict[key] and "error_msg" in \
                cdm_error_dict[key]:
            cdm_error = CdmError("0a04ffbcb5db120ce371f27e078e8980", cdm_error_dict[key]["error_code"], cdm_error_dict[key]["error_msg"])
    return cdm_error