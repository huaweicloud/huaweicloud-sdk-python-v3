# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdPartyAuthConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_type': 'str',
        'enable': 'bool',
        'update_object': 'str',
        'auth_type': 'str',
        'client_interface_config': 'InterfacesConfig',
        'server_interface_config': 'InterfacesConfig',
        'third_password_update_type': 'str',
        'custom_definition': 'str',
        'oauth_configs': 'str',
        'ldap_configs': 'list[LdapConfig]',
        'third_password_name': 'str'
    }

    attribute_map = {
        'update_type': 'update_type',
        'enable': 'enable',
        'update_object': 'update_object',
        'auth_type': 'auth_type',
        'client_interface_config': 'client_interface_config',
        'server_interface_config': 'server_interface_config',
        'third_password_update_type': 'third_password_update_type',
        'custom_definition': 'custom_definition',
        'oauth_configs': 'oauth_configs',
        'ldap_configs': 'ldap_configs',
        'third_password_name': 'third_password_name'
    }

    def __init__(self, update_type=None, enable=None, update_object=None, auth_type=None, client_interface_config=None, server_interface_config=None, third_password_update_type=None, custom_definition=None, oauth_configs=None, ldap_configs=None, third_password_name=None):
        r"""ThirdPartyAuthConfig

        The model defined in huaweicloud sdk

        :param update_type: 更新认证配置类型，认证类型为第三方单点登录时使用。
        :type update_type: str
        :param enable: 是否启用。
        :type enable: bool
        :param update_object: 更新认证配置对象，认证类型为第三方单点登录时使用。
        :type update_object: str
        :param auth_type: 认证类型。
        :type auth_type: str
        :param client_interface_config: 
        :type client_interface_config: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        :param server_interface_config: 
        :type server_interface_config: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        :param third_password_update_type: 更新认证配置类型，认证类型为第三方密码时使用。ADD代表新增，UPDATE代表修改，DELETE代表删除。
        :type third_password_update_type: str
        :param custom_definition: 自定义接口配置。
        :type custom_definition: str
        :param oauth_configs: oauth2配置。
        :type oauth_configs: str
        :param ldap_configs: 单点登录配置信息列表。
        :type ldap_configs: list[:class:`huaweicloudsdkworkspace.v2.LdapConfig`]
        :param third_password_name: 更新认证配置对象，认证类型为第三方密码时使用。
        :type third_password_name: str
        """
        
        

        self._update_type = None
        self._enable = None
        self._update_object = None
        self._auth_type = None
        self._client_interface_config = None
        self._server_interface_config = None
        self._third_password_update_type = None
        self._custom_definition = None
        self._oauth_configs = None
        self._ldap_configs = None
        self._third_password_name = None
        self.discriminator = None

        if update_type is not None:
            self.update_type = update_type
        if enable is not None:
            self.enable = enable
        if update_object is not None:
            self.update_object = update_object
        if auth_type is not None:
            self.auth_type = auth_type
        if client_interface_config is not None:
            self.client_interface_config = client_interface_config
        if server_interface_config is not None:
            self.server_interface_config = server_interface_config
        if third_password_update_type is not None:
            self.third_password_update_type = third_password_update_type
        if custom_definition is not None:
            self.custom_definition = custom_definition
        if oauth_configs is not None:
            self.oauth_configs = oauth_configs
        if ldap_configs is not None:
            self.ldap_configs = ldap_configs
        if third_password_name is not None:
            self.third_password_name = third_password_name

    @property
    def update_type(self):
        r"""Gets the update_type of this ThirdPartyAuthConfig.

        更新认证配置类型，认证类型为第三方单点登录时使用。

        :return: The update_type of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this ThirdPartyAuthConfig.

        更新认证配置类型，认证类型为第三方单点登录时使用。

        :param update_type: The update_type of this ThirdPartyAuthConfig.
        :type update_type: str
        """
        self._update_type = update_type

    @property
    def enable(self):
        r"""Gets the enable of this ThirdPartyAuthConfig.

        是否启用。

        :return: The enable of this ThirdPartyAuthConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ThirdPartyAuthConfig.

        是否启用。

        :param enable: The enable of this ThirdPartyAuthConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def update_object(self):
        r"""Gets the update_object of this ThirdPartyAuthConfig.

        更新认证配置对象，认证类型为第三方单点登录时使用。

        :return: The update_object of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._update_object

    @update_object.setter
    def update_object(self, update_object):
        r"""Sets the update_object of this ThirdPartyAuthConfig.

        更新认证配置对象，认证类型为第三方单点登录时使用。

        :param update_object: The update_object of this ThirdPartyAuthConfig.
        :type update_object: str
        """
        self._update_object = update_object

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ThirdPartyAuthConfig.

        认证类型。

        :return: The auth_type of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ThirdPartyAuthConfig.

        认证类型。

        :param auth_type: The auth_type of this ThirdPartyAuthConfig.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def client_interface_config(self):
        r"""Gets the client_interface_config of this ThirdPartyAuthConfig.

        :return: The client_interface_config of this ThirdPartyAuthConfig.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        """
        return self._client_interface_config

    @client_interface_config.setter
    def client_interface_config(self, client_interface_config):
        r"""Sets the client_interface_config of this ThirdPartyAuthConfig.

        :param client_interface_config: The client_interface_config of this ThirdPartyAuthConfig.
        :type client_interface_config: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        """
        self._client_interface_config = client_interface_config

    @property
    def server_interface_config(self):
        r"""Gets the server_interface_config of this ThirdPartyAuthConfig.

        :return: The server_interface_config of this ThirdPartyAuthConfig.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        """
        return self._server_interface_config

    @server_interface_config.setter
    def server_interface_config(self, server_interface_config):
        r"""Sets the server_interface_config of this ThirdPartyAuthConfig.

        :param server_interface_config: The server_interface_config of this ThirdPartyAuthConfig.
        :type server_interface_config: :class:`huaweicloudsdkworkspace.v2.InterfacesConfig`
        """
        self._server_interface_config = server_interface_config

    @property
    def third_password_update_type(self):
        r"""Gets the third_password_update_type of this ThirdPartyAuthConfig.

        更新认证配置类型，认证类型为第三方密码时使用。ADD代表新增，UPDATE代表修改，DELETE代表删除。

        :return: The third_password_update_type of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._third_password_update_type

    @third_password_update_type.setter
    def third_password_update_type(self, third_password_update_type):
        r"""Sets the third_password_update_type of this ThirdPartyAuthConfig.

        更新认证配置类型，认证类型为第三方密码时使用。ADD代表新增，UPDATE代表修改，DELETE代表删除。

        :param third_password_update_type: The third_password_update_type of this ThirdPartyAuthConfig.
        :type third_password_update_type: str
        """
        self._third_password_update_type = third_password_update_type

    @property
    def custom_definition(self):
        r"""Gets the custom_definition of this ThirdPartyAuthConfig.

        自定义接口配置。

        :return: The custom_definition of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._custom_definition

    @custom_definition.setter
    def custom_definition(self, custom_definition):
        r"""Sets the custom_definition of this ThirdPartyAuthConfig.

        自定义接口配置。

        :param custom_definition: The custom_definition of this ThirdPartyAuthConfig.
        :type custom_definition: str
        """
        self._custom_definition = custom_definition

    @property
    def oauth_configs(self):
        r"""Gets the oauth_configs of this ThirdPartyAuthConfig.

        oauth2配置。

        :return: The oauth_configs of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._oauth_configs

    @oauth_configs.setter
    def oauth_configs(self, oauth_configs):
        r"""Sets the oauth_configs of this ThirdPartyAuthConfig.

        oauth2配置。

        :param oauth_configs: The oauth_configs of this ThirdPartyAuthConfig.
        :type oauth_configs: str
        """
        self._oauth_configs = oauth_configs

    @property
    def ldap_configs(self):
        r"""Gets the ldap_configs of this ThirdPartyAuthConfig.

        单点登录配置信息列表。

        :return: The ldap_configs of this ThirdPartyAuthConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.LdapConfig`]
        """
        return self._ldap_configs

    @ldap_configs.setter
    def ldap_configs(self, ldap_configs):
        r"""Sets the ldap_configs of this ThirdPartyAuthConfig.

        单点登录配置信息列表。

        :param ldap_configs: The ldap_configs of this ThirdPartyAuthConfig.
        :type ldap_configs: list[:class:`huaweicloudsdkworkspace.v2.LdapConfig`]
        """
        self._ldap_configs = ldap_configs

    @property
    def third_password_name(self):
        r"""Gets the third_password_name of this ThirdPartyAuthConfig.

        更新认证配置对象，认证类型为第三方密码时使用。

        :return: The third_password_name of this ThirdPartyAuthConfig.
        :rtype: str
        """
        return self._third_password_name

    @third_password_name.setter
    def third_password_name(self, third_password_name):
        r"""Sets the third_password_name of this ThirdPartyAuthConfig.

        更新认证配置对象，认证类型为第三方密码时使用。

        :param third_password_name: The third_password_name of this ThirdPartyAuthConfig.
        :type third_password_name: str
        """
        self._third_password_name = third_password_name

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
        if not isinstance(other, ThirdPartyAuthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
