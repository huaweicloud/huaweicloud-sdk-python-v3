import json


class ApmError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    Apm_error = ApmError()

    apm_error_dict = json.loads(response_body)
    for key in apm_error_dict:
        if type(apm_error_dict[key]) == dict and "error_code" in apm_error_dict[key] and "error_msg" in \
                apm_error_dict[key]:
            apm_error = ApmError("0b672da40e00d4ca2f2cc0149613f58d", apm_error_dict[key]["error_code"],
                                 apm_error_dict[key]["error_msg"])
    return apm_error
