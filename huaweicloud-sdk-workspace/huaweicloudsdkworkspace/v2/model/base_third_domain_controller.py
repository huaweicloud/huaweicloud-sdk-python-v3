# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseThirdDomainController:

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
        'openapi_ca_cert': 'str'
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
        'openapi_ca_cert': 'openapi_ca_cert'
    }

    def __init__(self, username=None, user_password=None, main_dc_address=None, open_interface_address=None, open_interface_domain_name=None, internal_service_address=None, app_cert=None, app_cert_key=None, openapi_ca_cert=None):
        r"""BaseThirdDomainController

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

    @property
    def username(self):
        r"""Gets the username of this BaseThirdDomainController.

        域管理员。

        :return: The username of this BaseThirdDomainController.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this BaseThirdDomainController.

        域管理员。

        :param username: The username of this BaseThirdDomainController.
        :type username: str
        """
        self._username = username

    @property
    def user_password(self):
        r"""Gets the user_password of this BaseThirdDomainController.

        域管理员密码。

        :return: The user_password of this BaseThirdDomainController.
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        r"""Sets the user_password of this BaseThirdDomainController.

        域管理员密码。

        :param user_password: The user_password of this BaseThirdDomainController.
        :type user_password: str
        """
        self._user_password = user_password

    @property
    def main_dc_address(self):
        r"""Gets the main_dc_address of this BaseThirdDomainController.

        域管平台地址。

        :return: The main_dc_address of this BaseThirdDomainController.
        :rtype: str
        """
        return self._main_dc_address

    @main_dc_address.setter
    def main_dc_address(self, main_dc_address):
        r"""Sets the main_dc_address of this BaseThirdDomainController.

        域管平台地址。

        :param main_dc_address: The main_dc_address of this BaseThirdDomainController.
        :type main_dc_address: str
        """
        self._main_dc_address = main_dc_address

    @property
    def open_interface_address(self):
        r"""Gets the open_interface_address of this BaseThirdDomainController.

        域管开放接口地址。

        :return: The open_interface_address of this BaseThirdDomainController.
        :rtype: str
        """
        return self._open_interface_address

    @open_interface_address.setter
    def open_interface_address(self, open_interface_address):
        r"""Sets the open_interface_address of this BaseThirdDomainController.

        域管开放接口地址。

        :param open_interface_address: The open_interface_address of this BaseThirdDomainController.
        :type open_interface_address: str
        """
        self._open_interface_address = open_interface_address

    @property
    def open_interface_domain_name(self):
        r"""Gets the open_interface_domain_name of this BaseThirdDomainController.

        域管开放接口域名。

        :return: The open_interface_domain_name of this BaseThirdDomainController.
        :rtype: str
        """
        return self._open_interface_domain_name

    @open_interface_domain_name.setter
    def open_interface_domain_name(self, open_interface_domain_name):
        r"""Sets the open_interface_domain_name of this BaseThirdDomainController.

        域管开放接口域名。

        :param open_interface_domain_name: The open_interface_domain_name of this BaseThirdDomainController.
        :type open_interface_domain_name: str
        """
        self._open_interface_domain_name = open_interface_domain_name

    @property
    def internal_service_address(self):
        r"""Gets the internal_service_address of this BaseThirdDomainController.

        域管内部服务地址。

        :return: The internal_service_address of this BaseThirdDomainController.
        :rtype: str
        """
        return self._internal_service_address

    @internal_service_address.setter
    def internal_service_address(self, internal_service_address):
        r"""Sets the internal_service_address of this BaseThirdDomainController.

        域管内部服务地址。

        :param internal_service_address: The internal_service_address of this BaseThirdDomainController.
        :type internal_service_address: str
        """
        self._internal_service_address = internal_service_address

    @property
    def app_cert(self):
        r"""Gets the app_cert of this BaseThirdDomainController.

        客户端证书公钥。

        :return: The app_cert of this BaseThirdDomainController.
        :rtype: str
        """
        return self._app_cert

    @app_cert.setter
    def app_cert(self, app_cert):
        r"""Sets the app_cert of this BaseThirdDomainController.

        客户端证书公钥。

        :param app_cert: The app_cert of this BaseThirdDomainController.
        :type app_cert: str
        """
        self._app_cert = app_cert

    @property
    def app_cert_key(self):
        r"""Gets the app_cert_key of this BaseThirdDomainController.

        客户端证书私钥。

        :return: The app_cert_key of this BaseThirdDomainController.
        :rtype: str
        """
        return self._app_cert_key

    @app_cert_key.setter
    def app_cert_key(self, app_cert_key):
        r"""Sets the app_cert_key of this BaseThirdDomainController.

        客户端证书私钥。

        :param app_cert_key: The app_cert_key of this BaseThirdDomainController.
        :type app_cert_key: str
        """
        self._app_cert_key = app_cert_key

    @property
    def openapi_ca_cert(self):
        r"""Gets the openapi_ca_cert of this BaseThirdDomainController.

        服务端CA。

        :return: The openapi_ca_cert of this BaseThirdDomainController.
        :rtype: str
        """
        return self._openapi_ca_cert

    @openapi_ca_cert.setter
    def openapi_ca_cert(self, openapi_ca_cert):
        r"""Sets the openapi_ca_cert of this BaseThirdDomainController.

        服务端CA。

        :param openapi_ca_cert: The openapi_ca_cert of this BaseThirdDomainController.
        :type openapi_ca_cert: str
        """
        self._openapi_ca_cert = openapi_ca_cert

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
        if not isinstance(other, BaseThirdDomainController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
