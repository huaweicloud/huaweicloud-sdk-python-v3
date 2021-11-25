import json

from huaweicloudsdkcore.exceptions import exceptions

class DbssError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    dbss_error = DbssError()

    dbss_error_dict = json.loads(response_body)
    for key in dbss_error_dict:
        if type(dbss_error_dict[key]) == dict and "error_code" in dbss_error_dict[key] and "error_msg" in \
                dbss_error_dict[key]:
            dbss_error = DbssError("0a04ffbcb5db120ce371f27e078e8980", dbss_error_dict[key]["error_code"], dbss_error_dict[key]["error_msg"])
    return dbss_error