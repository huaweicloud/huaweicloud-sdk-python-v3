import json

from huaweicloudsdkcpts.exceptions import exceptions

class CssError:
    def __init__(self, request_id=None, error_code=None, error_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id

def handle_exception(response_body):
    css_error = CssError()

    css_error_dict = json.loads(response_body)
    for key in css_error_dict:
        if type(css_error_dict[key]) == dict and "error_code" in css_error_dict[key] and "error_msg" in \
                css_error_dict[key]:
            css_error = CssError(css_error_dict[key]["request_id"], css_error_dict[key]["error_code"], css_error_dict[key]["error_msg"])
    return css_error