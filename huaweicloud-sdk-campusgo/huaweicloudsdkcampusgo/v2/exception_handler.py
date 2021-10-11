import json


class CampusgoError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    Campusgo_error = CampusgoError()

    campusgo_error_dict = json.loads(response_body)
    for key in campusgo_error_dict:
        if type(campusgo_error_dict[key]) == dict and "error_code" in campusgo_error_dict[key] and "error_msg" in \
                campusgo_error_dict[key]:
            campusgo_error = CampusgoError("0b672da40e00d4ca2f2cc0149613f58d", campusgo_error_dict[key]["error_code"],
                                 campusgo_error_dict[key]["error_msg"])
    return campusgo_error
