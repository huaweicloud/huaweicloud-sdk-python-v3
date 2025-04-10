# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPropertiesResponse(SdkResponse):

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
        'response': 'object',
        'error_code': 'str',
        'error_msg': 'object'
    }

    attribute_map = {
        'request_id': 'request_id',
        'response': 'response',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, request_id=None, response=None, error_code=None, error_msg=None):
        r"""ListPropertiesResponse

        The model defined in huaweicloud sdk

        :param request_id: 设备属性查询ID，用于唯一标识一条属性查询，在下发查询属性时由物联网平台分配获得。
        :type request_id: str
        :param response: 设备上报的属性执行结果。Json格式，具体格式需要应用和设备约定。
        :type response: object
        :param error_code: 属性查询异常错误码。
        :type error_code: str
        :param error_msg: 属性查询异常错误信息。
        :type error_msg: object
        """
        
        super(ListPropertiesResponse, self).__init__()

        self._request_id = None
        self._response = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if response is not None:
            self.response = response
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPropertiesResponse.

        设备属性查询ID，用于唯一标识一条属性查询，在下发查询属性时由物联网平台分配获得。

        :return: The request_id of this ListPropertiesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPropertiesResponse.

        设备属性查询ID，用于唯一标识一条属性查询，在下发查询属性时由物联网平台分配获得。

        :param request_id: The request_id of this ListPropertiesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def response(self):
        r"""Gets the response of this ListPropertiesResponse.

        设备上报的属性执行结果。Json格式，具体格式需要应用和设备约定。

        :return: The response of this ListPropertiesResponse.
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this ListPropertiesResponse.

        设备上报的属性执行结果。Json格式，具体格式需要应用和设备约定。

        :param response: The response of this ListPropertiesResponse.
        :type response: object
        """
        self._response = response

    @property
    def error_code(self):
        r"""Gets the error_code of this ListPropertiesResponse.

        属性查询异常错误码。

        :return: The error_code of this ListPropertiesResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListPropertiesResponse.

        属性查询异常错误码。

        :param error_code: The error_code of this ListPropertiesResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ListPropertiesResponse.

        属性查询异常错误信息。

        :return: The error_msg of this ListPropertiesResponse.
        :rtype: object
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ListPropertiesResponse.

        属性查询异常错误信息。

        :param error_msg: The error_msg of this ListPropertiesResponse.
        :type error_msg: object
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ListPropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
