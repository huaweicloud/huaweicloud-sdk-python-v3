# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendedKeyUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_auth': 'bool',
        'client_auth': 'bool',
        'code_signing': 'bool',
        'email_protection': 'bool',
        'time_stamping': 'bool'
    }

    attribute_map = {
        'server_auth': 'server_auth',
        'client_auth': 'client_auth',
        'code_signing': 'code_signing',
        'email_protection': 'email_protection',
        'time_stamping': 'time_stamping'
    }

    def __init__(self, server_auth=None, client_auth=None, code_signing=None, email_protection=None, time_stamping=None):
        """ExtendedKeyUsage

        The model defined in huaweicloud sdk

        :param server_auth: 服务器身份验证，OID为：1.3.6.1.5.5.7.3.1。 - **true** - **false** &gt; 服务器证书请启用本增强型密钥用法，默认为false。
        :type server_auth: bool
        :param client_auth: 客户端身份验证，OID为：1.3.6.1.5.5.7.3.2。 - **true** - **false** &gt; 客户端证书请启用本增强型密钥用法，默认为false。
        :type client_auth: bool
        :param code_signing: 代码签名，OID为：1.3.6.1.5.5.7.3.3。 - **true** - **false** &gt; 签署可下载的可执行代码客户端认证，默认为false。
        :type code_signing: bool
        :param email_protection: 安全电子邮件，OID为：1.3.6.1.5.5.7.3.4。 - **true** - **false** &gt; 电子邮件保护，默认为false。
        :type email_protection: bool
        :param time_stamping: 时间戳，OID为：1.3.6.1.5.5.7.3.8。 - **true** - **false** &gt; 将一个对象的哈希绑定到一个时间，默认为false。
        :type time_stamping: bool
        """
        
        

        self._server_auth = None
        self._client_auth = None
        self._code_signing = None
        self._email_protection = None
        self._time_stamping = None
        self.discriminator = None

        if server_auth is not None:
            self.server_auth = server_auth
        if client_auth is not None:
            self.client_auth = client_auth
        if code_signing is not None:
            self.code_signing = code_signing
        if email_protection is not None:
            self.email_protection = email_protection
        if time_stamping is not None:
            self.time_stamping = time_stamping

    @property
    def server_auth(self):
        """Gets the server_auth of this ExtendedKeyUsage.

        服务器身份验证，OID为：1.3.6.1.5.5.7.3.1。 - **true** - **false** > 服务器证书请启用本增强型密钥用法，默认为false。

        :return: The server_auth of this ExtendedKeyUsage.
        :rtype: bool
        """
        return self._server_auth

    @server_auth.setter
    def server_auth(self, server_auth):
        """Sets the server_auth of this ExtendedKeyUsage.

        服务器身份验证，OID为：1.3.6.1.5.5.7.3.1。 - **true** - **false** > 服务器证书请启用本增强型密钥用法，默认为false。

        :param server_auth: The server_auth of this ExtendedKeyUsage.
        :type server_auth: bool
        """
        self._server_auth = server_auth

    @property
    def client_auth(self):
        """Gets the client_auth of this ExtendedKeyUsage.

        客户端身份验证，OID为：1.3.6.1.5.5.7.3.2。 - **true** - **false** > 客户端证书请启用本增强型密钥用法，默认为false。

        :return: The client_auth of this ExtendedKeyUsage.
        :rtype: bool
        """
        return self._client_auth

    @client_auth.setter
    def client_auth(self, client_auth):
        """Sets the client_auth of this ExtendedKeyUsage.

        客户端身份验证，OID为：1.3.6.1.5.5.7.3.2。 - **true** - **false** > 客户端证书请启用本增强型密钥用法，默认为false。

        :param client_auth: The client_auth of this ExtendedKeyUsage.
        :type client_auth: bool
        """
        self._client_auth = client_auth

    @property
    def code_signing(self):
        """Gets the code_signing of this ExtendedKeyUsage.

        代码签名，OID为：1.3.6.1.5.5.7.3.3。 - **true** - **false** > 签署可下载的可执行代码客户端认证，默认为false。

        :return: The code_signing of this ExtendedKeyUsage.
        :rtype: bool
        """
        return self._code_signing

    @code_signing.setter
    def code_signing(self, code_signing):
        """Sets the code_signing of this ExtendedKeyUsage.

        代码签名，OID为：1.3.6.1.5.5.7.3.3。 - **true** - **false** > 签署可下载的可执行代码客户端认证，默认为false。

        :param code_signing: The code_signing of this ExtendedKeyUsage.
        :type code_signing: bool
        """
        self._code_signing = code_signing

    @property
    def email_protection(self):
        """Gets the email_protection of this ExtendedKeyUsage.

        安全电子邮件，OID为：1.3.6.1.5.5.7.3.4。 - **true** - **false** > 电子邮件保护，默认为false。

        :return: The email_protection of this ExtendedKeyUsage.
        :rtype: bool
        """
        return self._email_protection

    @email_protection.setter
    def email_protection(self, email_protection):
        """Sets the email_protection of this ExtendedKeyUsage.

        安全电子邮件，OID为：1.3.6.1.5.5.7.3.4。 - **true** - **false** > 电子邮件保护，默认为false。

        :param email_protection: The email_protection of this ExtendedKeyUsage.
        :type email_protection: bool
        """
        self._email_protection = email_protection

    @property
    def time_stamping(self):
        """Gets the time_stamping of this ExtendedKeyUsage.

        时间戳，OID为：1.3.6.1.5.5.7.3.8。 - **true** - **false** > 将一个对象的哈希绑定到一个时间，默认为false。

        :return: The time_stamping of this ExtendedKeyUsage.
        :rtype: bool
        """
        return self._time_stamping

    @time_stamping.setter
    def time_stamping(self, time_stamping):
        """Sets the time_stamping of this ExtendedKeyUsage.

        时间戳，OID为：1.3.6.1.5.5.7.3.8。 - **true** - **false** > 将一个对象的哈希绑定到一个时间，默认为false。

        :param time_stamping: The time_stamping of this ExtendedKeyUsage.
        :type time_stamping: bool
        """
        self._time_stamping = time_stamping

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
        if not isinstance(other, ExtendedKeyUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
