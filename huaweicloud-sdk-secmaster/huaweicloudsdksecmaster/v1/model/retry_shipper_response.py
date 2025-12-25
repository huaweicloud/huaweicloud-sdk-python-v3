# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryShipperResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'msg': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'code': 'code',
        'msg': 'msg',
        'data': 'data'
    }

    def __init__(self, code=None, msg=None, data=None):
        r"""RetryShipperResponse

        The model defined in huaweicloud sdk

        :param code: 错误码，0表示成功，其他值表示错误
        :type code: int
        :param msg: 返回的状态信息，用于描述当前请求的结果
        :type msg: str
        :param data: 投递数据
        :type data: list[str]
        """
        
        super().__init__()

        self._code = None
        self._msg = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this RetryShipperResponse.

        错误码，0表示成功，其他值表示错误

        :return: The code of this RetryShipperResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this RetryShipperResponse.

        错误码，0表示成功，其他值表示错误

        :param code: The code of this RetryShipperResponse.
        :type code: int
        """
        self._code = code

    @property
    def msg(self):
        r"""Gets the msg of this RetryShipperResponse.

        返回的状态信息，用于描述当前请求的结果

        :return: The msg of this RetryShipperResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this RetryShipperResponse.

        返回的状态信息，用于描述当前请求的结果

        :param msg: The msg of this RetryShipperResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def data(self):
        r"""Gets the data of this RetryShipperResponse.

        投递数据

        :return: The data of this RetryShipperResponse.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this RetryShipperResponse.

        投递数据

        :param data: The data of this RetryShipperResponse.
        :type data: list[str]
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("RetryShipperResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, RetryShipperResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
