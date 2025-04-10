# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLivePlatformResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform_id': 'str',
        'access_type': 'AccessTypeEnum',
        'name': 'str',
        'authorization_info': 'PlatformAuthorizationInfo',
        'auth_config': 'CustomPlatformAuthConfig',
        'callback_config': 'list[StandardPlatformApiConfig]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'platform_id': 'platform_id',
        'access_type': 'access_type',
        'name': 'name',
        'authorization_info': 'authorization_info',
        'auth_config': 'auth_config',
        'callback_config': 'callback_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, platform_id=None, access_type=None, name=None, authorization_info=None, auth_config=None, callback_config=None, x_request_id=None):
        r"""ShowLivePlatformResponse

        The model defined in huaweicloud sdk

        :param platform_id: 平台ID
        :type platform_id: str
        :param access_type: 
        :type access_type: :class:`huaweicloudsdkmetastudio.v1.AccessTypeEnum`
        :param name: 直播平台名称
        :type name: str
        :param authorization_info: 
        :type authorization_info: :class:`huaweicloudsdkmetastudio.v1.PlatformAuthorizationInfo`
        :param auth_config: 
        :type auth_config: :class:`huaweicloudsdkmetastudio.v1.CustomPlatformAuthConfig`
        :param callback_config: 自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。
        :type callback_config: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowLivePlatformResponse, self).__init__()

        self._platform_id = None
        self._access_type = None
        self._name = None
        self._authorization_info = None
        self._auth_config = None
        self._callback_config = None
        self._x_request_id = None
        self.discriminator = None

        if platform_id is not None:
            self.platform_id = platform_id
        if access_type is not None:
            self.access_type = access_type
        if name is not None:
            self.name = name
        if authorization_info is not None:
            self.authorization_info = authorization_info
        if auth_config is not None:
            self.auth_config = auth_config
        if callback_config is not None:
            self.callback_config = callback_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def platform_id(self):
        r"""Gets the platform_id of this ShowLivePlatformResponse.

        平台ID

        :return: The platform_id of this ShowLivePlatformResponse.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this ShowLivePlatformResponse.

        平台ID

        :param platform_id: The platform_id of this ShowLivePlatformResponse.
        :type platform_id: str
        """
        self._platform_id = platform_id

    @property
    def access_type(self):
        r"""Gets the access_type of this ShowLivePlatformResponse.

        :return: The access_type of this ShowLivePlatformResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AccessTypeEnum`
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this ShowLivePlatformResponse.

        :param access_type: The access_type of this ShowLivePlatformResponse.
        :type access_type: :class:`huaweicloudsdkmetastudio.v1.AccessTypeEnum`
        """
        self._access_type = access_type

    @property
    def name(self):
        r"""Gets the name of this ShowLivePlatformResponse.

        直播平台名称

        :return: The name of this ShowLivePlatformResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowLivePlatformResponse.

        直播平台名称

        :param name: The name of this ShowLivePlatformResponse.
        :type name: str
        """
        self._name = name

    @property
    def authorization_info(self):
        r"""Gets the authorization_info of this ShowLivePlatformResponse.

        :return: The authorization_info of this ShowLivePlatformResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlatformAuthorizationInfo`
        """
        return self._authorization_info

    @authorization_info.setter
    def authorization_info(self, authorization_info):
        r"""Sets the authorization_info of this ShowLivePlatformResponse.

        :param authorization_info: The authorization_info of this ShowLivePlatformResponse.
        :type authorization_info: :class:`huaweicloudsdkmetastudio.v1.PlatformAuthorizationInfo`
        """
        self._authorization_info = authorization_info

    @property
    def auth_config(self):
        r"""Gets the auth_config of this ShowLivePlatformResponse.

        :return: The auth_config of this ShowLivePlatformResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CustomPlatformAuthConfig`
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        r"""Sets the auth_config of this ShowLivePlatformResponse.

        :param auth_config: The auth_config of this ShowLivePlatformResponse.
        :type auth_config: :class:`huaweicloudsdkmetastudio.v1.CustomPlatformAuthConfig`
        """
        self._auth_config = auth_config

    @property
    def callback_config(self):
        r"""Gets the callback_config of this ShowLivePlatformResponse.

        自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。

        :return: The callback_config of this ShowLivePlatformResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this ShowLivePlatformResponse.

        自定义直播平台回调配置。同一种类型仅保留一个配置，如果配置多个会随机保存一个。

        :param callback_config: The callback_config of this ShowLivePlatformResponse.
        :type callback_config: list[:class:`huaweicloudsdkmetastudio.v1.StandardPlatformApiConfig`]
        """
        self._callback_config = callback_config

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowLivePlatformResponse.

        :return: The x_request_id of this ShowLivePlatformResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowLivePlatformResponse.

        :param x_request_id: The x_request_id of this ShowLivePlatformResponse.
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
        if not isinstance(other, ShowLivePlatformResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
