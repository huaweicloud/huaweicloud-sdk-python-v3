# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBlackWhiteListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'result': 'str',
        'data': 'object',
        'x_request_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'result': 'result',
        'data': 'data',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, code=None, result=None, data=None, x_request_id=None):
        r"""UpdateBlackWhiteListResponse

        The model defined in huaweicloud sdk

        :param code: 响应码，200：成功，400，失败。
        :type code: str
        :param result: 响应结果。
        :type result: str
        :param data: 响应体返回内容。
        :type data: object
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateBlackWhiteListResponse, self).__init__()

        self._code = None
        self._result = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if result is not None:
            self.result = result
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def code(self):
        r"""Gets the code of this UpdateBlackWhiteListResponse.

        响应码，200：成功，400，失败。

        :return: The code of this UpdateBlackWhiteListResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this UpdateBlackWhiteListResponse.

        响应码，200：成功，400，失败。

        :param code: The code of this UpdateBlackWhiteListResponse.
        :type code: str
        """
        self._code = code

    @property
    def result(self):
        r"""Gets the result of this UpdateBlackWhiteListResponse.

        响应结果。

        :return: The result of this UpdateBlackWhiteListResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UpdateBlackWhiteListResponse.

        响应结果。

        :param result: The result of this UpdateBlackWhiteListResponse.
        :type result: str
        """
        self._result = result

    @property
    def data(self):
        r"""Gets the data of this UpdateBlackWhiteListResponse.

        响应体返回内容。

        :return: The data of this UpdateBlackWhiteListResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this UpdateBlackWhiteListResponse.

        响应体返回内容。

        :param data: The data of this UpdateBlackWhiteListResponse.
        :type data: object
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateBlackWhiteListResponse.

        :return: The x_request_id of this UpdateBlackWhiteListResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateBlackWhiteListResponse.

        :param x_request_id: The x_request_id of this UpdateBlackWhiteListResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateBlackWhiteListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
