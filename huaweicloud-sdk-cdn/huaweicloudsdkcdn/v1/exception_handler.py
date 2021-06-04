import json


class CdnError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id


def handle_exception(response_body):
    cdn_error = CdnError()

    cdn_error_dict = json.loads(response_body)
    for key in cdn_error_dict:
        if type(cdn_error_dict[key]) == dict and "error_code" in cdn_error_dict[key] and "error_msg" in \
                cdn_error_dict[key]:
            cdn_error = CdnError("0b672da40e00d4ca2f2cc0149613f58d", cdn_error_dict[key]["error_code"],
                                 cdn_error_dict[key]["error_msg"])
    return cdn_error
