# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppSecretKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'x_trace_id': 'str'
    }

    attribute_map = {
        'key': 'key',
        'x_trace_id': 'X-Trace-Id'
    }

    def __init__(self, key=None, x_trace_id=None):
        r"""ShowAppSecretKeyResponse

        The model defined in huaweicloud sdk

        :param key: **参数解释**： 应用请求密钥。 **取值范围**： [1-512]字符。
        :type key: str
        :param x_trace_id: 
        :type x_trace_id: str
        """
        
        super().__init__()

        self._key = None
        self._x_trace_id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id

    @property
    def key(self):
        r"""Gets the key of this ShowAppSecretKeyResponse.

        **参数解释**： 应用请求密钥。 **取值范围**： [1-512]字符。

        :return: The key of this ShowAppSecretKeyResponse.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowAppSecretKeyResponse.

        **参数解释**： 应用请求密钥。 **取值范围**： [1-512]字符。

        :param key: The key of this ShowAppSecretKeyResponse.
        :type key: str
        """
        self._key = key

    @property
    def x_trace_id(self):
        r"""Gets the x_trace_id of this ShowAppSecretKeyResponse.

        :return: The x_trace_id of this ShowAppSecretKeyResponse.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        r"""Sets the x_trace_id of this ShowAppSecretKeyResponse.

        :param x_trace_id: The x_trace_id of this ShowAppSecretKeyResponse.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowAppSecretKeyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAppSecretKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
