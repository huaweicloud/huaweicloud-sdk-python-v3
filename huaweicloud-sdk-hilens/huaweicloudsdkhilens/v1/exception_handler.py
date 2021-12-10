import json


class HilensError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    hilens_error = HilensError()

    hilens_error_dict = json.loads(response_body)
    for key in hilens_error_dict:
        if type(hilens_error_dict[key]) == dict and "error_code" in hilens_error_dict[key] and "error_msg" in \
                hilens_error_dict[key]:
            hilens_error = HilensError("0a04ffbcb5db120ce371f27e078e8980",
                                       hilens_error_dict[key]["error_code"], hilens_error_dict[key]["error_msg"])
    return hilens_error
