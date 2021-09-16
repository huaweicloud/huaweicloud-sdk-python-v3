import json


class DasError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    das_error = DasError()

    das_error_dict = json.loads(response_body)
    for key in das_error_dict:
        if type(das_error_dict[key]) == dict and "error_code" in das_error_dict[key] and "error_msg" in \
                das_error_dict[key]:
            das_error = DasError(das_error_dict[key]["request_id"], das_error_dict[key]["error_code"],
                                 das_error_dict[key]["error_msg"])
    return das_error