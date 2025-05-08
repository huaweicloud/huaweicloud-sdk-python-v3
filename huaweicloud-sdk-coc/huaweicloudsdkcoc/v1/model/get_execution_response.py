# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetExecutionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'data': 'object',
        'x_request_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'data': 'data',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, error_code=None, error_msg=None, data=None, x_request_id=None):
        r"""GetExecutionResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param data: 返回数据
        :type data: :class:`huaweicloudsdkcoc.v1.object`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(GetExecutionResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def error_code(self):
        r"""Gets the error_code of this GetExecutionResponse.

        错误码

        :return: The error_code of this GetExecutionResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this GetExecutionResponse.

        错误码

        :param error_code: The error_code of this GetExecutionResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this GetExecutionResponse.

        错误信息

        :return: The error_msg of this GetExecutionResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this GetExecutionResponse.

        错误信息

        :param error_msg: The error_msg of this GetExecutionResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def data(self):
        r"""Gets the data of this GetExecutionResponse.

        返回数据

        :return: The data of this GetExecutionResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.object`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this GetExecutionResponse.

        返回数据

        :param data: The data of this GetExecutionResponse.
        :type data: :class:`huaweicloudsdkcoc.v1.object`
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this GetExecutionResponse.

        :return: The x_request_id of this GetExecutionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this GetExecutionResponse.

        :param x_request_id: The x_request_id of this GetExecutionResponse.
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
        if not isinstance(other, GetExecutionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
