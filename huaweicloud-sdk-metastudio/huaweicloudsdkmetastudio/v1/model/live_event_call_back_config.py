# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveEventCallBackConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_event_type_callback_url': 'str',
        'auth_type': 'str',
        'key': 'str',
        'callback_event_type': 'list[str]'
    }

    attribute_map = {
        'live_event_type_callback_url': 'live_event_type_callback_url',
        'auth_type': 'auth_type',
        'key': 'key',
        'callback_event_type': 'callback_event_type'
    }

    def __init__(self, live_event_type_callback_url=None, auth_type=None, key=None, callback_event_type=None):
        """LiveEventCallBackConfig

        The model defined in huaweicloud sdk

        :param live_event_type_callback_url: 直播事件回调地址。https地址，需自带鉴权串。
        :type live_event_type_callback_url: str
        :param auth_type: 认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret&#x3D;hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&amp;hwTime&#x3D;hex(timestamp)
        :type auth_type: str
        :param key: 密钥Key
        :type key: str
        :param callback_event_type: 回调的直播事件类型列表
        :type callback_event_type: list[str]
        """
        
        

        self._live_event_type_callback_url = None
        self._auth_type = None
        self._key = None
        self._callback_event_type = None
        self.discriminator = None

        if live_event_type_callback_url is not None:
            self.live_event_type_callback_url = live_event_type_callback_url
        if auth_type is not None:
            self.auth_type = auth_type
        if key is not None:
            self.key = key
        if callback_event_type is not None:
            self.callback_event_type = callback_event_type

    @property
    def live_event_type_callback_url(self):
        """Gets the live_event_type_callback_url of this LiveEventCallBackConfig.

        直播事件回调地址。https地址，需自带鉴权串。

        :return: The live_event_type_callback_url of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._live_event_type_callback_url

    @live_event_type_callback_url.setter
    def live_event_type_callback_url(self, live_event_type_callback_url):
        """Sets the live_event_type_callback_url of this LiveEventCallBackConfig.

        直播事件回调地址。https地址，需自带鉴权串。

        :param live_event_type_callback_url: The live_event_type_callback_url of this LiveEventCallBackConfig.
        :type live_event_type_callback_url: str
        """
        self._live_event_type_callback_url = live_event_type_callback_url

    @property
    def auth_type(self):
        """Gets the auth_type of this LiveEventCallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&hwTime=hex(timestamp)

        :return: The auth_type of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this LiveEventCallBackConfig.

        认证类型。 * NONE。URL中自带认证。 * MSS_A。HMACSHA256签名模式，在URL中追加参数:hwSecret,hwTime。取值方式：hwSecret=hmac_sha256(Key, URI（live_event_callback_url）+ hwTime)&hwTime=hex(timestamp)

        :param auth_type: The auth_type of this LiveEventCallBackConfig.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def key(self):
        """Gets the key of this LiveEventCallBackConfig.

        密钥Key

        :return: The key of this LiveEventCallBackConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LiveEventCallBackConfig.

        密钥Key

        :param key: The key of this LiveEventCallBackConfig.
        :type key: str
        """
        self._key = key

    @property
    def callback_event_type(self):
        """Gets the callback_event_type of this LiveEventCallBackConfig.

        回调的直播事件类型列表

        :return: The callback_event_type of this LiveEventCallBackConfig.
        :rtype: list[str]
        """
        return self._callback_event_type

    @callback_event_type.setter
    def callback_event_type(self, callback_event_type):
        """Sets the callback_event_type of this LiveEventCallBackConfig.

        回调的直播事件类型列表

        :param callback_event_type: The callback_event_type of this LiveEventCallBackConfig.
        :type callback_event_type: list[str]
        """
        self._callback_event_type = callback_event_type

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
        if not isinstance(other, LiveEventCallBackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
