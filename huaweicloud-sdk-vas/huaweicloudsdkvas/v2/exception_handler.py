import json


class VasError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    vas_error = VasError()

    vas_error_dict = json.loads(response_body)
    for key in vas_error_dict:
        if type(vas_error_dict[key]) == dict and "error_code" in vas_error_dict[key] and "error_msg" in \
                vas_error_dict[key]:
            vas_error = VasError("0b672da40e00d4ca2f2cc0149613f58d", vas_error_dict[key]["error_code"],
                                 vas_error_dict[key]["error_msg"])
    return vas_error
