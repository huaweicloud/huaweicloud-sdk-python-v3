# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeviceAuthorizer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizer_name': 'str',
        'func_urn': 'str',
        'signing_enable': 'bool',
        'signing_token': 'str',
        'signing_public_key': 'str',
        'default_authorizer': 'bool',
        'status': 'str',
        'cache_enable': 'bool'
    }

    attribute_map = {
        'authorizer_name': 'authorizer_name',
        'func_urn': 'func_urn',
        'signing_enable': 'signing_enable',
        'signing_token': 'signing_token',
        'signing_public_key': 'signing_public_key',
        'default_authorizer': 'default_authorizer',
        'status': 'status',
        'cache_enable': 'cache_enable'
    }

    def __init__(self, authorizer_name=None, func_urn=None, signing_enable=None, signing_token=None, signing_public_key=None, default_authorizer=None, status=None, cache_enable=None):
        r"""UpdateDeviceAuthorizer

        The model defined in huaweicloud sdk

        :param authorizer_name: **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type authorizer_name: str
        :param func_urn: **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。
        :type func_urn: str
        :param signing_enable: **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启，开启时signing_token与signing_public_key必填。
        :type signing_enable: bool
        :param signing_token: **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type signing_token: str
        :param signing_public_key: **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。
        :type signing_public_key: str
        :param default_authorizer: **参数说明**：当前自定义鉴权是否为默认的鉴权方式，默认为false，当设置为true时，用户所有支持SNI的设备，如果在鉴权时不指定使用特定的设备鉴权，将统一使用当前鉴权器策略进行鉴权。
        :type default_authorizer: bool
        :param status: **参数说明**：是否激活该鉴权方式，默认为激活。 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。
        :type status: str
        :param cache_enable: **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。
        :type cache_enable: bool
        """
        
        

        self._authorizer_name = None
        self._func_urn = None
        self._signing_enable = None
        self._signing_token = None
        self._signing_public_key = None
        self._default_authorizer = None
        self._status = None
        self._cache_enable = None
        self.discriminator = None

        if authorizer_name is not None:
            self.authorizer_name = authorizer_name
        if func_urn is not None:
            self.func_urn = func_urn
        if signing_enable is not None:
            self.signing_enable = signing_enable
        if signing_token is not None:
            self.signing_token = signing_token
        if signing_public_key is not None:
            self.signing_public_key = signing_public_key
        if default_authorizer is not None:
            self.default_authorizer = default_authorizer
        if status is not None:
            self.status = status
        if cache_enable is not None:
            self.cache_enable = cache_enable

    @property
    def authorizer_name(self):
        r"""Gets the authorizer_name of this UpdateDeviceAuthorizer.

        **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The authorizer_name of this UpdateDeviceAuthorizer.
        :rtype: str
        """
        return self._authorizer_name

    @authorizer_name.setter
    def authorizer_name(self, authorizer_name):
        r"""Sets the authorizer_name of this UpdateDeviceAuthorizer.

        **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param authorizer_name: The authorizer_name of this UpdateDeviceAuthorizer.
        :type authorizer_name: str
        """
        self._authorizer_name = authorizer_name

    @property
    def func_urn(self):
        r"""Gets the func_urn of this UpdateDeviceAuthorizer.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。

        :return: The func_urn of this UpdateDeviceAuthorizer.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this UpdateDeviceAuthorizer.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。

        :param func_urn: The func_urn of this UpdateDeviceAuthorizer.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def signing_enable(self):
        r"""Gets the signing_enable of this UpdateDeviceAuthorizer.

        **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启，开启时signing_token与signing_public_key必填。

        :return: The signing_enable of this UpdateDeviceAuthorizer.
        :rtype: bool
        """
        return self._signing_enable

    @signing_enable.setter
    def signing_enable(self, signing_enable):
        r"""Sets the signing_enable of this UpdateDeviceAuthorizer.

        **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启，开启时signing_token与signing_public_key必填。

        :param signing_enable: The signing_enable of this UpdateDeviceAuthorizer.
        :type signing_enable: bool
        """
        self._signing_enable = signing_enable

    @property
    def signing_token(self):
        r"""Gets the signing_token of this UpdateDeviceAuthorizer.

        **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The signing_token of this UpdateDeviceAuthorizer.
        :rtype: str
        """
        return self._signing_token

    @signing_token.setter
    def signing_token(self, signing_token):
        r"""Sets the signing_token of this UpdateDeviceAuthorizer.

        **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param signing_token: The signing_token of this UpdateDeviceAuthorizer.
        :type signing_token: str
        """
        self._signing_token = signing_token

    @property
    def signing_public_key(self):
        r"""Gets the signing_public_key of this UpdateDeviceAuthorizer.

        **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。

        :return: The signing_public_key of this UpdateDeviceAuthorizer.
        :rtype: str
        """
        return self._signing_public_key

    @signing_public_key.setter
    def signing_public_key(self, signing_public_key):
        r"""Sets the signing_public_key of this UpdateDeviceAuthorizer.

        **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。

        :param signing_public_key: The signing_public_key of this UpdateDeviceAuthorizer.
        :type signing_public_key: str
        """
        self._signing_public_key = signing_public_key

    @property
    def default_authorizer(self):
        r"""Gets the default_authorizer of this UpdateDeviceAuthorizer.

        **参数说明**：当前自定义鉴权是否为默认的鉴权方式，默认为false，当设置为true时，用户所有支持SNI的设备，如果在鉴权时不指定使用特定的设备鉴权，将统一使用当前鉴权器策略进行鉴权。

        :return: The default_authorizer of this UpdateDeviceAuthorizer.
        :rtype: bool
        """
        return self._default_authorizer

    @default_authorizer.setter
    def default_authorizer(self, default_authorizer):
        r"""Sets the default_authorizer of this UpdateDeviceAuthorizer.

        **参数说明**：当前自定义鉴权是否为默认的鉴权方式，默认为false，当设置为true时，用户所有支持SNI的设备，如果在鉴权时不指定使用特定的设备鉴权，将统一使用当前鉴权器策略进行鉴权。

        :param default_authorizer: The default_authorizer of this UpdateDeviceAuthorizer.
        :type default_authorizer: bool
        """
        self._default_authorizer = default_authorizer

    @property
    def status(self):
        r"""Gets the status of this UpdateDeviceAuthorizer.

        **参数说明**：是否激活该鉴权方式，默认为激活。 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。

        :return: The status of this UpdateDeviceAuthorizer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateDeviceAuthorizer.

        **参数说明**：是否激活该鉴权方式，默认为激活。 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。

        :param status: The status of this UpdateDeviceAuthorizer.
        :type status: str
        """
        self._status = status

    @property
    def cache_enable(self):
        r"""Gets the cache_enable of this UpdateDeviceAuthorizer.

        **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。

        :return: The cache_enable of this UpdateDeviceAuthorizer.
        :rtype: bool
        """
        return self._cache_enable

    @cache_enable.setter
    def cache_enable(self, cache_enable):
        r"""Sets the cache_enable of this UpdateDeviceAuthorizer.

        **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。

        :param cache_enable: The cache_enable of this UpdateDeviceAuthorizer.
        :type cache_enable: bool
        """
        self._cache_enable = cache_enable

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
        if not isinstance(other, UpdateDeviceAuthorizer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
