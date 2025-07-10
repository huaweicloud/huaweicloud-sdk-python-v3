# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdapConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'port': 'int',
        'base_dn': 'str',
        'administrator_dn': 'str',
        'administrator_password': 'str',
        'user_dn': 'str',
        'use_ssl': 'bool',
        'cert_content': 'str',
        'username_attribute': 'str',
        'object_class': 'str',
        'security_type': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'base_dn': 'base_dn',
        'administrator_dn': 'administrator_dn',
        'administrator_password': 'administrator_password',
        'user_dn': 'user_dn',
        'use_ssl': 'use_ssl',
        'cert_content': 'cert_content',
        'username_attribute': 'username_attribute',
        'object_class': 'object_class',
        'security_type': 'security_type'
    }

    def __init__(self, host=None, port=None, base_dn=None, administrator_dn=None, administrator_password=None, user_dn=None, use_ssl=None, cert_content=None, username_attribute=None, object_class=None, security_type=None):
        r"""LdapConfig

        The model defined in huaweicloud sdk

        :param host: host。
        :type host: str
        :param port: 端口,取值范围1-65535,默认389。
        :type port: int
        :param base_dn: base_dn。
        :type base_dn: str
        :param administrator_dn: 管理员dn。
        :type administrator_dn: str
        :param administrator_password: 管理员密码。
        :type administrator_password: str
        :param user_dn: 用户dn。
        :type user_dn: str
        :param use_ssl: 是否启用ssl。
        :type use_ssl: bool
        :param cert_content: 证书。
        :type cert_content: str
        :param username_attribute: 用户名属性。
        :type username_attribute: str
        :param object_class: 用户ObjectClass。
        :type object_class: str
        :param security_type: 安全类型。
        :type security_type: str
        """
        
        

        self._host = None
        self._port = None
        self._base_dn = None
        self._administrator_dn = None
        self._administrator_password = None
        self._user_dn = None
        self._use_ssl = None
        self._cert_content = None
        self._username_attribute = None
        self._object_class = None
        self._security_type = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if base_dn is not None:
            self.base_dn = base_dn
        if administrator_dn is not None:
            self.administrator_dn = administrator_dn
        if administrator_password is not None:
            self.administrator_password = administrator_password
        if user_dn is not None:
            self.user_dn = user_dn
        if use_ssl is not None:
            self.use_ssl = use_ssl
        if cert_content is not None:
            self.cert_content = cert_content
        if username_attribute is not None:
            self.username_attribute = username_attribute
        if object_class is not None:
            self.object_class = object_class
        if security_type is not None:
            self.security_type = security_type

    @property
    def host(self):
        r"""Gets the host of this LdapConfig.

        host。

        :return: The host of this LdapConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this LdapConfig.

        host。

        :param host: The host of this LdapConfig.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        r"""Gets the port of this LdapConfig.

        端口,取值范围1-65535,默认389。

        :return: The port of this LdapConfig.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this LdapConfig.

        端口,取值范围1-65535,默认389。

        :param port: The port of this LdapConfig.
        :type port: int
        """
        self._port = port

    @property
    def base_dn(self):
        r"""Gets the base_dn of this LdapConfig.

        base_dn。

        :return: The base_dn of this LdapConfig.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        r"""Sets the base_dn of this LdapConfig.

        base_dn。

        :param base_dn: The base_dn of this LdapConfig.
        :type base_dn: str
        """
        self._base_dn = base_dn

    @property
    def administrator_dn(self):
        r"""Gets the administrator_dn of this LdapConfig.

        管理员dn。

        :return: The administrator_dn of this LdapConfig.
        :rtype: str
        """
        return self._administrator_dn

    @administrator_dn.setter
    def administrator_dn(self, administrator_dn):
        r"""Sets the administrator_dn of this LdapConfig.

        管理员dn。

        :param administrator_dn: The administrator_dn of this LdapConfig.
        :type administrator_dn: str
        """
        self._administrator_dn = administrator_dn

    @property
    def administrator_password(self):
        r"""Gets the administrator_password of this LdapConfig.

        管理员密码。

        :return: The administrator_password of this LdapConfig.
        :rtype: str
        """
        return self._administrator_password

    @administrator_password.setter
    def administrator_password(self, administrator_password):
        r"""Sets the administrator_password of this LdapConfig.

        管理员密码。

        :param administrator_password: The administrator_password of this LdapConfig.
        :type administrator_password: str
        """
        self._administrator_password = administrator_password

    @property
    def user_dn(self):
        r"""Gets the user_dn of this LdapConfig.

        用户dn。

        :return: The user_dn of this LdapConfig.
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn):
        r"""Sets the user_dn of this LdapConfig.

        用户dn。

        :param user_dn: The user_dn of this LdapConfig.
        :type user_dn: str
        """
        self._user_dn = user_dn

    @property
    def use_ssl(self):
        r"""Gets the use_ssl of this LdapConfig.

        是否启用ssl。

        :return: The use_ssl of this LdapConfig.
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        r"""Sets the use_ssl of this LdapConfig.

        是否启用ssl。

        :param use_ssl: The use_ssl of this LdapConfig.
        :type use_ssl: bool
        """
        self._use_ssl = use_ssl

    @property
    def cert_content(self):
        r"""Gets the cert_content of this LdapConfig.

        证书。

        :return: The cert_content of this LdapConfig.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        r"""Sets the cert_content of this LdapConfig.

        证书。

        :param cert_content: The cert_content of this LdapConfig.
        :type cert_content: str
        """
        self._cert_content = cert_content

    @property
    def username_attribute(self):
        r"""Gets the username_attribute of this LdapConfig.

        用户名属性。

        :return: The username_attribute of this LdapConfig.
        :rtype: str
        """
        return self._username_attribute

    @username_attribute.setter
    def username_attribute(self, username_attribute):
        r"""Sets the username_attribute of this LdapConfig.

        用户名属性。

        :param username_attribute: The username_attribute of this LdapConfig.
        :type username_attribute: str
        """
        self._username_attribute = username_attribute

    @property
    def object_class(self):
        r"""Gets the object_class of this LdapConfig.

        用户ObjectClass。

        :return: The object_class of this LdapConfig.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        r"""Sets the object_class of this LdapConfig.

        用户ObjectClass。

        :param object_class: The object_class of this LdapConfig.
        :type object_class: str
        """
        self._object_class = object_class

    @property
    def security_type(self):
        r"""Gets the security_type of this LdapConfig.

        安全类型。

        :return: The security_type of this LdapConfig.
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        r"""Sets the security_type of this LdapConfig.

        安全类型。

        :param security_type: The security_type of this LdapConfig.
        :type security_type: str
        """
        self._security_type = security_type

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
        if not isinstance(other, LdapConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
