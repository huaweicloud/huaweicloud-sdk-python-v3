# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLivePlatformReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'auth_config': 'UpdateCustomPlatformAuthConfig',
        'callback_config': 'list[StandardPlatformApiConfig]'
    }

    attribute_map = {
        'name': 'name',
        'auth_config': 'auth_config',
        'callback_config': 'callback_config'
    }

    def __init__(self, name=None, auth_config=None, callback_config=None):
        r"""UpdateLivePlatformReq

        The model defined in huaweicloud sdk

        :param name: 直播平台名称
        :type name: str
        :param auth_config: 
        :type auth_config: :class:`huaweicloudsdkmetastudio.v1.UpdateCustomPlatformAuthConfig`
        :param callback_config: 自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。
        :type callback_config: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        """
        
        

        self._name = None
        self._auth_config = None
        self._callback_config = None
        self.discriminator = None

        self.name = name
        if auth_config is not None:
            self.auth_config = auth_config
        self.callback_config = callback_config

    @property
    def name(self):
        r"""Gets the name of this UpdateLivePlatformReq.

        直播平台名称

        :return: The name of this UpdateLivePlatformReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateLivePlatformReq.

        直播平台名称

        :param name: The name of this UpdateLivePlatformReq.
        :type name: str
        """
        self._name = name

    @property
    def auth_config(self):
        r"""Gets the auth_config of this UpdateLivePlatformReq.

        :return: The auth_config of this UpdateLivePlatformReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateCustomPlatformAuthConfig`
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        r"""Sets the auth_config of this UpdateLivePlatformReq.

        :param auth_config: The auth_config of this UpdateLivePlatformReq.
        :type auth_config: :class:`huaweicloudsdkmetastudio.v1.UpdateCustomPlatformAuthConfig`
        """
        self._auth_config = auth_config

    @property
    def callback_config(self):
        r"""Gets the callback_config of this UpdateLivePlatformReq.

        自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。

        :return: The callback_config of this UpdateLivePlatformReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this UpdateLivePlatformReq.

        自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。

        :param callback_config: The callback_config of this UpdateLivePlatformReq.
        :type callback_config: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        """
        self._callback_config = callback_config

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
        if not isinstance(other, UpdateLivePlatformReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
