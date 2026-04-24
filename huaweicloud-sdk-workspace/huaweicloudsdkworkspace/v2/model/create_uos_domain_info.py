# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUosDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'user_password': 'str',
        'main_dc_address': 'str',
        'open_interface_address': 'str',
        'open_interface_domain_name': 'str',
        'internal_service_address': 'str',
        'app_cert': 'str',
        'app_cert_key': 'str',
        'openapi_ca_cert': 'str',
        'domain_name': 'str',
        'type': 'DomainType'
    }

    attribute_map = {
        'username': 'username',
        'user_password': 'user_password',
        'main_dc_address': 'main_dc_address',
        'open_interface_address': 'open_interface_address',
        'open_interface_domain_name': 'open_interface_domain_name',
        'internal_service_address': 'internal_service_address',
        'app_cert': 'app_cert',
        'app_cert_key': 'app_cert_key',
        'openapi_ca_cert': 'openapi_ca_cert',
        'domain_name': 'domain_name',
        'type': 'type'
    }

    def __init__(self, username=None, user_password=None, main_dc_address=None, open_interface_address=None, open_interface_domain_name=None, internal_service_address=None, app_cert=None, app_cert_key=None, openapi_ca_cert=None, domain_name=None, type=None):
        r"""CreateUosDomainInfo

        The model defined in huaweicloud sdk

        :param username: 域管理员。
        :type username: str
        :param user_password: 域管理员密码。
        :type user_password: str
        :param main_dc_address: 域管平台地址。
        :type main_dc_address: str
        :param open_interface_address: 域管开放接口地址。
        :type open_interface_address: str
        :param open_interface_domain_name: 域管开放接口域名。
        :type open_interface_domain_name: str
        :param internal_service_address: 域管内部服务地址。
        :type internal_service_address: str
        :param app_cert: 客户端证书公钥。
        :type app_cert: str
        :param app_cert_key: 客户端证书私钥。
        :type app_cert_key: str
        :param openapi_ca_cert: 服务端CA。
        :type openapi_ca_cert: str
        :param domain_name: 统信域控名称。
        :type domain_name: str
        :param type: 
        :type type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        
        

        self._username = None
        self._user_password = None
        self._main_dc_address = None
        self._open_interface_address = None
        self._open_interface_domain_name = None
        self._internal_service_address = None
        self._app_cert = None
        self._app_cert_key = None
        self._openapi_ca_cert = None
        self._domain_name = None
        self._type = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if user_password is not None:
            self.user_password = user_password
        if main_dc_address is not None:
            self.main_dc_address = main_dc_address
        if open_interface_address is not None:
            self.open_interface_address = open_interface_address
        if open_interface_domain_name is not None:
            self.open_interface_domain_name = open_interface_domain_name
        if internal_service_address is not None:
            self.internal_service_address = internal_service_address
        if app_cert is not None:
            self.app_cert = app_cert
        if app_cert_key is not None:
            self.app_cert_key = app_cert_key
        if openapi_ca_cert is not None:
            self.openapi_ca_cert = openapi_ca_cert
        if domain_name is not None:
            self.domain_name = domain_name
        if type is not None:
            self.type = type

    @property
    def username(self):
        r"""Gets the username of this CreateUosDomainInfo.

        域管理员。

        :return: The username of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this CreateUosDomainInfo.

        域管理员。

        :param username: The username of this CreateUosDomainInfo.
        :type username: str
        """
        self._username = username

    @property
    def user_password(self):
        r"""Gets the user_password of this CreateUosDomainInfo.

        域管理员密码。

        :return: The user_password of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        r"""Sets the user_password of this CreateUosDomainInfo.

        域管理员密码。

        :param user_password: The user_password of this CreateUosDomainInfo.
        :type user_password: str
        """
        self._user_password = user_password

    @property
    def main_dc_address(self):
        r"""Gets the main_dc_address of this CreateUosDomainInfo.

        域管平台地址。

        :return: The main_dc_address of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._main_dc_address

    @main_dc_address.setter
    def main_dc_address(self, main_dc_address):
        r"""Sets the main_dc_address of this CreateUosDomainInfo.

        域管平台地址。

        :param main_dc_address: The main_dc_address of this CreateUosDomainInfo.
        :type main_dc_address: str
        """
        self._main_dc_address = main_dc_address

    @property
    def open_interface_address(self):
        r"""Gets the open_interface_address of this CreateUosDomainInfo.

        域管开放接口地址。

        :return: The open_interface_address of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._open_interface_address

    @open_interface_address.setter
    def open_interface_address(self, open_interface_address):
        r"""Sets the open_interface_address of this CreateUosDomainInfo.

        域管开放接口地址。

        :param open_interface_address: The open_interface_address of this CreateUosDomainInfo.
        :type open_interface_address: str
        """
        self._open_interface_address = open_interface_address

    @property
    def open_interface_domain_name(self):
        r"""Gets the open_interface_domain_name of this CreateUosDomainInfo.

        域管开放接口域名。

        :return: The open_interface_domain_name of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._open_interface_domain_name

    @open_interface_domain_name.setter
    def open_interface_domain_name(self, open_interface_domain_name):
        r"""Sets the open_interface_domain_name of this CreateUosDomainInfo.

        域管开放接口域名。

        :param open_interface_domain_name: The open_interface_domain_name of this CreateUosDomainInfo.
        :type open_interface_domain_name: str
        """
        self._open_interface_domain_name = open_interface_domain_name

    @property
    def internal_service_address(self):
        r"""Gets the internal_service_address of this CreateUosDomainInfo.

        域管内部服务地址。

        :return: The internal_service_address of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._internal_service_address

    @internal_service_address.setter
    def internal_service_address(self, internal_service_address):
        r"""Sets the internal_service_address of this CreateUosDomainInfo.

        域管内部服务地址。

        :param internal_service_address: The internal_service_address of this CreateUosDomainInfo.
        :type internal_service_address: str
        """
        self._internal_service_address = internal_service_address

    @property
    def app_cert(self):
        r"""Gets the app_cert of this CreateUosDomainInfo.

        客户端证书公钥。

        :return: The app_cert of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._app_cert

    @app_cert.setter
    def app_cert(self, app_cert):
        r"""Sets the app_cert of this CreateUosDomainInfo.

        客户端证书公钥。

        :param app_cert: The app_cert of this CreateUosDomainInfo.
        :type app_cert: str
        """
        self._app_cert = app_cert

    @property
    def app_cert_key(self):
        r"""Gets the app_cert_key of this CreateUosDomainInfo.

        客户端证书私钥。

        :return: The app_cert_key of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._app_cert_key

    @app_cert_key.setter
    def app_cert_key(self, app_cert_key):
        r"""Sets the app_cert_key of this CreateUosDomainInfo.

        客户端证书私钥。

        :param app_cert_key: The app_cert_key of this CreateUosDomainInfo.
        :type app_cert_key: str
        """
        self._app_cert_key = app_cert_key

    @property
    def openapi_ca_cert(self):
        r"""Gets the openapi_ca_cert of this CreateUosDomainInfo.

        服务端CA。

        :return: The openapi_ca_cert of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._openapi_ca_cert

    @openapi_ca_cert.setter
    def openapi_ca_cert(self, openapi_ca_cert):
        r"""Sets the openapi_ca_cert of this CreateUosDomainInfo.

        服务端CA。

        :param openapi_ca_cert: The openapi_ca_cert of this CreateUosDomainInfo.
        :type openapi_ca_cert: str
        """
        self._openapi_ca_cert = openapi_ca_cert

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateUosDomainInfo.

        统信域控名称。

        :return: The domain_name of this CreateUosDomainInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateUosDomainInfo.

        统信域控名称。

        :param domain_name: The domain_name of this CreateUosDomainInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def type(self):
        r"""Gets the type of this CreateUosDomainInfo.

        :return: The type of this CreateUosDomainInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateUosDomainInfo.

        :param type: The type of this CreateUosDomainInfo.
        :type type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        self._type = type

    def to_dict(self):
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
        if not isinstance(other, CreateUosDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
