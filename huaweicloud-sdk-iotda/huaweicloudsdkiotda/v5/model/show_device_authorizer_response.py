# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceAuthorizerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizer_id': 'str',
        'authorizer_name': 'str',
        'func_name': 'str',
        'func_urn': 'str',
        'signing_enable': 'bool',
        'signing_token': 'str',
        'signing_public_key': 'str',
        'default_authorizer': 'bool',
        'status': 'str',
        'cache_enable': 'bool',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'authorizer_id': 'authorizer_id',
        'authorizer_name': 'authorizer_name',
        'func_name': 'func_name',
        'func_urn': 'func_urn',
        'signing_enable': 'signing_enable',
        'signing_token': 'signing_token',
        'signing_public_key': 'signing_public_key',
        'default_authorizer': 'default_authorizer',
        'status': 'status',
        'cache_enable': 'cache_enable',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, authorizer_id=None, authorizer_name=None, func_name=None, func_urn=None, signing_enable=None, signing_token=None, signing_public_key=None, default_authorizer=None, status=None, cache_enable=None, create_time=None, update_time=None):
        """ShowDeviceAuthorizerResponse

        The model defined in huaweicloud sdk

        :param authorizer_id: **参数说明**：自定义鉴权ID。
        :type authorizer_id: str
        :param authorizer_name: **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type authorizer_name: str
        :param func_name: **参数说明**：函数名称。
        :type func_name: str
        :param func_urn: **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。
        :type func_urn: str
        :param signing_enable: **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启。
        :type signing_enable: bool
        :param signing_token: **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type signing_token: str
        :param signing_public_key: **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。
        :type signing_public_key: str
        :param default_authorizer: **参数说明**：是否为默认的鉴权方式，默认为false。
        :type default_authorizer: bool
        :param status: **参数说明**：是否激活该鉴权方式 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。
        :type status: str
        :param cache_enable: **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。
        :type cache_enable: bool
        :param create_time: 在物联网平台进行自定义鉴权相关操作的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type create_time: str
        :param update_time: 在物联网平台更新自定义鉴权相关操作的时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如：20151212T121212Z。
        :type update_time: str
        """
        
        super(ShowDeviceAuthorizerResponse, self).__init__()

        self._authorizer_id = None
        self._authorizer_name = None
        self._func_name = None
        self._func_urn = None
        self._signing_enable = None
        self._signing_token = None
        self._signing_public_key = None
        self._default_authorizer = None
        self._status = None
        self._cache_enable = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if authorizer_name is not None:
            self.authorizer_name = authorizer_name
        if func_name is not None:
            self.func_name = func_name
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ShowDeviceAuthorizerResponse.

        **参数说明**：自定义鉴权ID。

        :return: The authorizer_id of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ShowDeviceAuthorizerResponse.

        **参数说明**：自定义鉴权ID。

        :param authorizer_id: The authorizer_id of this ShowDeviceAuthorizerResponse.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def authorizer_name(self):
        """Gets the authorizer_name of this ShowDeviceAuthorizerResponse.

        **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The authorizer_name of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._authorizer_name

    @authorizer_name.setter
    def authorizer_name(self, authorizer_name):
        """Sets the authorizer_name of this ShowDeviceAuthorizerResponse.

        **参数说明**：自定义鉴权器名称，同一租户下的自定义鉴权器名称不能重复。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param authorizer_name: The authorizer_name of this ShowDeviceAuthorizerResponse.
        :type authorizer_name: str
        """
        self._authorizer_name = authorizer_name

    @property
    def func_name(self):
        """Gets the func_name of this ShowDeviceAuthorizerResponse.

        **参数说明**：函数名称。

        :return: The func_name of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this ShowDeviceAuthorizerResponse.

        **参数说明**：函数名称。

        :param func_name: The func_name of this ShowDeviceAuthorizerResponse.
        :type func_name: str
        """
        self._func_name = func_name

    @property
    def func_urn(self):
        """Gets the func_urn of this ShowDeviceAuthorizerResponse.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。

        :return: The func_urn of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this ShowDeviceAuthorizerResponse.

        **参数说明**：函数的URN（Uniform Resource Name），唯一标识函数，即自定义鉴权器对应的处理函数地址。

        :param func_urn: The func_urn of this ShowDeviceAuthorizerResponse.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def signing_enable(self):
        """Gets the signing_enable of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启。

        :return: The signing_enable of this ShowDeviceAuthorizerResponse.
        :rtype: bool
        """
        return self._signing_enable

    @signing_enable.setter
    def signing_enable(self, signing_enable):
        """Sets the signing_enable of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否启动签名校验，启动签名校验后不满足签名要求的鉴权信息将被拒绝，以减少无效的函数调用。推荐用户进行安全的签名校验，默认开启。

        :param signing_enable: The signing_enable of this ShowDeviceAuthorizerResponse.
        :type signing_enable: bool
        """
        self._signing_enable = signing_enable

    @property
    def signing_token(self):
        """Gets the signing_token of this ShowDeviceAuthorizerResponse.

        **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The signing_token of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._signing_token

    @signing_token.setter
    def signing_token(self, signing_token):
        """Sets the signing_token of this ShowDeviceAuthorizerResponse.

        **参数说明**：签名校验的Key值，开启签名校验时使用。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param signing_token: The signing_token of this ShowDeviceAuthorizerResponse.
        :type signing_token: str
        """
        self._signing_token = signing_token

    @property
    def signing_public_key(self):
        """Gets the signing_public_key of this ShowDeviceAuthorizerResponse.

        **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。

        :return: The signing_public_key of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._signing_public_key

    @signing_public_key.setter
    def signing_public_key(self, signing_public_key):
        """Sets the signing_public_key of this ShowDeviceAuthorizerResponse.

        **参数说明**：签名校验的公钥，开启签名校验时使用。用于认证设备携带的签名信息是否正确。

        :param signing_public_key: The signing_public_key of this ShowDeviceAuthorizerResponse.
        :type signing_public_key: str
        """
        self._signing_public_key = signing_public_key

    @property
    def default_authorizer(self):
        """Gets the default_authorizer of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否为默认的鉴权方式，默认为false。

        :return: The default_authorizer of this ShowDeviceAuthorizerResponse.
        :rtype: bool
        """
        return self._default_authorizer

    @default_authorizer.setter
    def default_authorizer(self, default_authorizer):
        """Sets the default_authorizer of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否为默认的鉴权方式，默认为false。

        :param default_authorizer: The default_authorizer of this ShowDeviceAuthorizerResponse.
        :type default_authorizer: bool
        """
        self._default_authorizer = default_authorizer

    @property
    def status(self):
        """Gets the status of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否激活该鉴权方式 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。

        :return: The status of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否激活该鉴权方式 - ACTIVE：该鉴权为激活状态。 - INACTIVE：该鉴权为停用状态。

        :param status: The status of this ShowDeviceAuthorizerResponse.
        :type status: str
        """
        self._status = status

    @property
    def cache_enable(self):
        """Gets the cache_enable of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。

        :return: The cache_enable of this ShowDeviceAuthorizerResponse.
        :rtype: bool
        """
        return self._cache_enable

    @cache_enable.setter
    def cache_enable(self, cache_enable):
        """Sets the cache_enable of this ShowDeviceAuthorizerResponse.

        **参数说明**：是否开启缓存，默认为false，设备为true时，当设备入参（username，clientId，password，以及证书信息，函数urn）不变时，当缓存结果存在时，将直接使用缓存结果，建议在调试时设置为false，生产时设置为true，避免频繁调用函数。

        :param cache_enable: The cache_enable of this ShowDeviceAuthorizerResponse.
        :type cache_enable: bool
        """
        self._cache_enable = cache_enable

    @property
    def create_time(self):
        """Gets the create_time of this ShowDeviceAuthorizerResponse.

        在物联网平台进行自定义鉴权相关操作的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The create_time of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDeviceAuthorizerResponse.

        在物联网平台进行自定义鉴权相关操作的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param create_time: The create_time of this ShowDeviceAuthorizerResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowDeviceAuthorizerResponse.

        在物联网平台更新自定义鉴权相关操作的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :return: The update_time of this ShowDeviceAuthorizerResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowDeviceAuthorizerResponse.

        在物联网平台更新自定义鉴权相关操作的时间。格式：yyyyMMdd'T'HHmmss'Z'，如：20151212T121212Z。

        :param update_time: The update_time of this ShowDeviceAuthorizerResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowDeviceAuthorizerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
