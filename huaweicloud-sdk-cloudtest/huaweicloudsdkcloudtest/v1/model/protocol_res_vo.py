# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtocolResVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'response_code': 'list[int]',
        'response_time': 'str'
    }

    attribute_map = {
        'response_code': 'response_code',
        'response_time': 'response_time'
    }

    def __init__(self, response_code=None, response_time=None):
        r"""ProtocolResVo

        The model defined in huaweicloud sdk

        :param response_code: 期望响应的状态码
        :type response_code: list[int]
        :param response_time: 期望响应时间
        :type response_time: str
        """
        
        

        self._response_code = None
        self._response_time = None
        self.discriminator = None

        if response_code is not None:
            self.response_code = response_code
        if response_time is not None:
            self.response_time = response_time

    @property
    def response_code(self):
        r"""Gets the response_code of this ProtocolResVo.

        期望响应的状态码

        :return: The response_code of this ProtocolResVo.
        :rtype: list[int]
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        r"""Sets the response_code of this ProtocolResVo.

        期望响应的状态码

        :param response_code: The response_code of this ProtocolResVo.
        :type response_code: list[int]
        """
        self._response_code = response_code

    @property
    def response_time(self):
        r"""Gets the response_time of this ProtocolResVo.

        期望响应时间

        :return: The response_time of this ProtocolResVo.
        :rtype: str
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        r"""Sets the response_time of this ProtocolResVo.

        期望响应时间

        :param response_time: The response_time of this ProtocolResVo.
        :type response_time: str
        """
        self._response_time = response_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtocolResVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
