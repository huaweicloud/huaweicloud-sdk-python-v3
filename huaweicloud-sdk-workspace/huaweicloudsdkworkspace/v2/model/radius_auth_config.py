# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RadiusAuthConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'radius_configs': 'list[RadiusHost]',
        'radius_secret': 'str',
        'radius_timeout': 'int',
        'radius_attempt_time': 'int',
        'domain_in_user_prefix': 'str',
        'radius_auth_type': 'str',
        'enable': 'bool',
        'auth_protocol': 'str',
        'verification_code_display_enable': 'bool',
        'verification_code_conditions': 'int',
        'obtain_code_attributes': 'object',
        'check_code_attributes': 'object'
    }

    attribute_map = {
        'radius_configs': 'radius_configs',
        'radius_secret': 'radius_secret',
        'radius_timeout': 'radius_timeout',
        'radius_attempt_time': 'radius_attempt_time',
        'domain_in_user_prefix': 'domain_in_user_prefix',
        'radius_auth_type': 'radius_auth_type',
        'enable': 'enable',
        'auth_protocol': 'auth_protocol',
        'verification_code_display_enable': 'verification_code_display_enable',
        'verification_code_conditions': 'verification_code_conditions',
        'obtain_code_attributes': 'obtain_code_attributes',
        'check_code_attributes': 'check_code_attributes'
    }

    def __init__(self, radius_configs=None, radius_secret=None, radius_timeout=None, radius_attempt_time=None, domain_in_user_prefix=None, radius_auth_type=None, enable=None, auth_protocol=None, verification_code_display_enable=None, verification_code_conditions=None, obtain_code_attributes=None, check_code_attributes=None):
        """RadiusAuthConfig

        The model defined in huaweicloud sdk

        :param radius_configs: Radius主机配置列表
        :type radius_configs: list[:class:`huaweicloudsdkworkspace.v2.RadiusHost`]
        :param radius_secret: Radius密码
        :type radius_secret: str
        :param radius_timeout: 超时时间,取值范围1-300s
        :type radius_timeout: int
        :param radius_attempt_time: 尝试次数,取值范围1-10
        :type radius_attempt_time: int
        :param domain_in_user_prefix: 用户前缀中的域。0代表禁用，1代表开启域前缀，2代表开启域后缀，默认值为0。
        :type domain_in_user_prefix: str
        :param radius_auth_type: 认证类型。静态密码: \&quot;STATIC\&quot;，动态口令: \&quot;DYNAMIC\&quot;
        :type radius_auth_type: str
        :param enable: 是否启用
        :type enable: bool
        :param auth_protocol: 身份验证类型: pap或chap，选择短信验证码时才可用
        :type auth_protocol: str
        :param verification_code_display_enable: 验证码开关，默认开启
        :type verification_code_display_enable: bool
        :param verification_code_conditions: 验证码失败次数
        :type verification_code_conditions: int
        :param obtain_code_attributes: 过滤短信拓展字段
        :type obtain_code_attributes: object
        :param check_code_attributes: 过滤短信拓展字段
        :type check_code_attributes: object
        """
        
        

        self._radius_configs = None
        self._radius_secret = None
        self._radius_timeout = None
        self._radius_attempt_time = None
        self._domain_in_user_prefix = None
        self._radius_auth_type = None
        self._enable = None
        self._auth_protocol = None
        self._verification_code_display_enable = None
        self._verification_code_conditions = None
        self._obtain_code_attributes = None
        self._check_code_attributes = None
        self.discriminator = None

        if radius_configs is not None:
            self.radius_configs = radius_configs
        if radius_secret is not None:
            self.radius_secret = radius_secret
        if radius_timeout is not None:
            self.radius_timeout = radius_timeout
        if radius_attempt_time is not None:
            self.radius_attempt_time = radius_attempt_time
        if domain_in_user_prefix is not None:
            self.domain_in_user_prefix = domain_in_user_prefix
        if radius_auth_type is not None:
            self.radius_auth_type = radius_auth_type
        if enable is not None:
            self.enable = enable
        if auth_protocol is not None:
            self.auth_protocol = auth_protocol
        if verification_code_display_enable is not None:
            self.verification_code_display_enable = verification_code_display_enable
        if verification_code_conditions is not None:
            self.verification_code_conditions = verification_code_conditions
        if obtain_code_attributes is not None:
            self.obtain_code_attributes = obtain_code_attributes
        if check_code_attributes is not None:
            self.check_code_attributes = check_code_attributes

    @property
    def radius_configs(self):
        """Gets the radius_configs of this RadiusAuthConfig.

        Radius主机配置列表

        :return: The radius_configs of this RadiusAuthConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.RadiusHost`]
        """
        return self._radius_configs

    @radius_configs.setter
    def radius_configs(self, radius_configs):
        """Sets the radius_configs of this RadiusAuthConfig.

        Radius主机配置列表

        :param radius_configs: The radius_configs of this RadiusAuthConfig.
        :type radius_configs: list[:class:`huaweicloudsdkworkspace.v2.RadiusHost`]
        """
        self._radius_configs = radius_configs

    @property
    def radius_secret(self):
        """Gets the radius_secret of this RadiusAuthConfig.

        Radius密码

        :return: The radius_secret of this RadiusAuthConfig.
        :rtype: str
        """
        return self._radius_secret

    @radius_secret.setter
    def radius_secret(self, radius_secret):
        """Sets the radius_secret of this RadiusAuthConfig.

        Radius密码

        :param radius_secret: The radius_secret of this RadiusAuthConfig.
        :type radius_secret: str
        """
        self._radius_secret = radius_secret

    @property
    def radius_timeout(self):
        """Gets the radius_timeout of this RadiusAuthConfig.

        超时时间,取值范围1-300s

        :return: The radius_timeout of this RadiusAuthConfig.
        :rtype: int
        """
        return self._radius_timeout

    @radius_timeout.setter
    def radius_timeout(self, radius_timeout):
        """Sets the radius_timeout of this RadiusAuthConfig.

        超时时间,取值范围1-300s

        :param radius_timeout: The radius_timeout of this RadiusAuthConfig.
        :type radius_timeout: int
        """
        self._radius_timeout = radius_timeout

    @property
    def radius_attempt_time(self):
        """Gets the radius_attempt_time of this RadiusAuthConfig.

        尝试次数,取值范围1-10

        :return: The radius_attempt_time of this RadiusAuthConfig.
        :rtype: int
        """
        return self._radius_attempt_time

    @radius_attempt_time.setter
    def radius_attempt_time(self, radius_attempt_time):
        """Sets the radius_attempt_time of this RadiusAuthConfig.

        尝试次数,取值范围1-10

        :param radius_attempt_time: The radius_attempt_time of this RadiusAuthConfig.
        :type radius_attempt_time: int
        """
        self._radius_attempt_time = radius_attempt_time

    @property
    def domain_in_user_prefix(self):
        """Gets the domain_in_user_prefix of this RadiusAuthConfig.

        用户前缀中的域。0代表禁用，1代表开启域前缀，2代表开启域后缀，默认值为0。

        :return: The domain_in_user_prefix of this RadiusAuthConfig.
        :rtype: str
        """
        return self._domain_in_user_prefix

    @domain_in_user_prefix.setter
    def domain_in_user_prefix(self, domain_in_user_prefix):
        """Sets the domain_in_user_prefix of this RadiusAuthConfig.

        用户前缀中的域。0代表禁用，1代表开启域前缀，2代表开启域后缀，默认值为0。

        :param domain_in_user_prefix: The domain_in_user_prefix of this RadiusAuthConfig.
        :type domain_in_user_prefix: str
        """
        self._domain_in_user_prefix = domain_in_user_prefix

    @property
    def radius_auth_type(self):
        """Gets the radius_auth_type of this RadiusAuthConfig.

        认证类型。静态密码: \"STATIC\"，动态口令: \"DYNAMIC\"

        :return: The radius_auth_type of this RadiusAuthConfig.
        :rtype: str
        """
        return self._radius_auth_type

    @radius_auth_type.setter
    def radius_auth_type(self, radius_auth_type):
        """Sets the radius_auth_type of this RadiusAuthConfig.

        认证类型。静态密码: \"STATIC\"，动态口令: \"DYNAMIC\"

        :param radius_auth_type: The radius_auth_type of this RadiusAuthConfig.
        :type radius_auth_type: str
        """
        self._radius_auth_type = radius_auth_type

    @property
    def enable(self):
        """Gets the enable of this RadiusAuthConfig.

        是否启用

        :return: The enable of this RadiusAuthConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this RadiusAuthConfig.

        是否启用

        :param enable: The enable of this RadiusAuthConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this RadiusAuthConfig.

        身份验证类型: pap或chap，选择短信验证码时才可用

        :return: The auth_protocol of this RadiusAuthConfig.
        :rtype: str
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this RadiusAuthConfig.

        身份验证类型: pap或chap，选择短信验证码时才可用

        :param auth_protocol: The auth_protocol of this RadiusAuthConfig.
        :type auth_protocol: str
        """
        self._auth_protocol = auth_protocol

    @property
    def verification_code_display_enable(self):
        """Gets the verification_code_display_enable of this RadiusAuthConfig.

        验证码开关，默认开启

        :return: The verification_code_display_enable of this RadiusAuthConfig.
        :rtype: bool
        """
        return self._verification_code_display_enable

    @verification_code_display_enable.setter
    def verification_code_display_enable(self, verification_code_display_enable):
        """Sets the verification_code_display_enable of this RadiusAuthConfig.

        验证码开关，默认开启

        :param verification_code_display_enable: The verification_code_display_enable of this RadiusAuthConfig.
        :type verification_code_display_enable: bool
        """
        self._verification_code_display_enable = verification_code_display_enable

    @property
    def verification_code_conditions(self):
        """Gets the verification_code_conditions of this RadiusAuthConfig.

        验证码失败次数

        :return: The verification_code_conditions of this RadiusAuthConfig.
        :rtype: int
        """
        return self._verification_code_conditions

    @verification_code_conditions.setter
    def verification_code_conditions(self, verification_code_conditions):
        """Sets the verification_code_conditions of this RadiusAuthConfig.

        验证码失败次数

        :param verification_code_conditions: The verification_code_conditions of this RadiusAuthConfig.
        :type verification_code_conditions: int
        """
        self._verification_code_conditions = verification_code_conditions

    @property
    def obtain_code_attributes(self):
        """Gets the obtain_code_attributes of this RadiusAuthConfig.

        过滤短信拓展字段

        :return: The obtain_code_attributes of this RadiusAuthConfig.
        :rtype: object
        """
        return self._obtain_code_attributes

    @obtain_code_attributes.setter
    def obtain_code_attributes(self, obtain_code_attributes):
        """Sets the obtain_code_attributes of this RadiusAuthConfig.

        过滤短信拓展字段

        :param obtain_code_attributes: The obtain_code_attributes of this RadiusAuthConfig.
        :type obtain_code_attributes: object
        """
        self._obtain_code_attributes = obtain_code_attributes

    @property
    def check_code_attributes(self):
        """Gets the check_code_attributes of this RadiusAuthConfig.

        过滤短信拓展字段

        :return: The check_code_attributes of this RadiusAuthConfig.
        :rtype: object
        """
        return self._check_code_attributes

    @check_code_attributes.setter
    def check_code_attributes(self, check_code_attributes):
        """Sets the check_code_attributes of this RadiusAuthConfig.

        过滤短信拓展字段

        :param check_code_attributes: The check_code_attributes of this RadiusAuthConfig.
        :type check_code_attributes: object
        """
        self._check_code_attributes = check_code_attributes

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
        if not isinstance(other, RadiusAuthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
