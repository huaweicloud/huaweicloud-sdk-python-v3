# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, request_id=None, error_msg=None, error_code=None):
        r"""DeleteImageResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求id
        :type request_id: str
        :param error_msg: 任务错误码说明。
        :type error_msg: str
        :param error_code: 任务错误码。
        :type error_code: str
        """
        
        super(DeleteImageResponse, self).__init__()

        self._request_id = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def request_id(self):
        r"""Gets the request_id of this DeleteImageResponse.

        请求id

        :return: The request_id of this DeleteImageResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this DeleteImageResponse.

        请求id

        :param request_id: The request_id of this DeleteImageResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def error_msg(self):
        r"""Gets the error_msg of this DeleteImageResponse.

        任务错误码说明。

        :return: The error_msg of this DeleteImageResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this DeleteImageResponse.

        任务错误码说明。

        :param error_msg: The error_msg of this DeleteImageResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this DeleteImageResponse.

        任务错误码。

        :return: The error_code of this DeleteImageResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DeleteImageResponse.

        任务错误码。

        :param error_code: The error_code of this DeleteImageResponse.
        :type error_code: str
        """
        self._error_code = error_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
