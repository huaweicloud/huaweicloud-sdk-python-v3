# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UosDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_config_id': 'str',
        'id': 'str',
        'type': 'DomainType',
        'domain_name': 'str',
        'username': 'str',
        'main_dc_address': 'str',
        'open_interface_address': 'str',
        'open_interface_domain_name': 'str',
        'internal_service_address': 'str',
        'app_cert_id': 'str',
        'app_cert_start_time': 'str',
        'app_cert_end_time': 'str',
        'openapi_ca_cert_id': 'str',
        'openapi_ca_cert_start_time': 'str',
        'openapi_ca_cert_end_time': 'str'
    }

    attribute_map = {
        'auth_config_id': 'auth_config_id',
        'id': 'id',
        'type': 'type',
        'domain_name': 'domain_name',
        'username': 'username',
        'main_dc_address': 'main_dc_address',
        'open_interface_address': 'open_interface_address',
        'open_interface_domain_name': 'open_interface_domain_name',
        'internal_service_address': 'internal_service_address',
        'app_cert_id': 'app_cert_id',
        'app_cert_start_time': 'app_cert_start_time',
        'app_cert_end_time': 'app_cert_end_time',
        'openapi_ca_cert_id': 'openapi_ca_cert_id',
        'openapi_ca_cert_start_time': 'openapi_ca_cert_start_time',
        'openapi_ca_cert_end_time': 'openapi_ca_cert_end_time'
    }

    def __init__(self, auth_config_id=None, id=None, type=None, domain_name=None, username=None, main_dc_address=None, open_interface_address=None, open_interface_domain_name=None, internal_service_address=None, app_cert_id=None, app_cert_start_time=None, app_cert_end_time=None, openapi_ca_cert_id=None, openapi_ca_cert_start_time=None, openapi_ca_cert_end_time=None):
        r"""UosDomainInfo

        The model defined in huaweicloud sdk

        :param auth_config_id: 认证配置id。
        :type auth_config_id: str
        :param id: 域控id。
        :type id: str
        :param type: 
        :type type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        :param domain_name: 统信域控名称。
        :type domain_name: str
        :param username: 域管理员。
        :type username: str
        :param main_dc_address: 域管平台地址。
        :type main_dc_address: str
        :param open_interface_address: 域管开放接口地址。
        :type open_interface_address: str
        :param open_interface_domain_name: 域管开放接口域名。
        :type open_interface_domain_name: str
        :param internal_service_address: 域管内部服务地址。
        :type internal_service_address: str
        :param app_cert_id: 客户端证书公钥id。
        :type app_cert_id: str
        :param app_cert_start_time: 客户端证书公钥有效期起始时间。
        :type app_cert_start_time: str
        :param app_cert_end_time: 客户端证书公钥有效期结束时间。
        :type app_cert_end_time: str
        :param openapi_ca_cert_id: 服务端CA id。
        :type openapi_ca_cert_id: str
        :param openapi_ca_cert_start_time: 服务端CA有效期起始时间。
        :type openapi_ca_cert_start_time: str
        :param openapi_ca_cert_end_time: 服务端CA有效期结束时间。
        :type openapi_ca_cert_end_time: str
        """
        
        

        self._auth_config_id = None
        self._id = None
        self._type = None
        self._domain_name = None
        self._username = None
        self._main_dc_address = None
        self._open_interface_address = None
        self._open_interface_domain_name = None
        self._internal_service_address = None
        self._app_cert_id = None
        self._app_cert_start_time = None
        self._app_cert_end_time = None
        self._openapi_ca_cert_id = None
        self._openapi_ca_cert_start_time = None
        self._openapi_ca_cert_end_time = None
        self.discriminator = None

        if auth_config_id is not None:
            self.auth_config_id = auth_config_id
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if domain_name is not None:
            self.domain_name = domain_name
        if username is not None:
            self.username = username
        if main_dc_address is not None:
            self.main_dc_address = main_dc_address
        if open_interface_address is not None:
            self.open_interface_address = open_interface_address
        if open_interface_domain_name is not None:
            self.open_interface_domain_name = open_interface_domain_name
        if internal_service_address is not None:
            self.internal_service_address = internal_service_address
        if app_cert_id is not None:
            self.app_cert_id = app_cert_id
        if app_cert_start_time is not None:
            self.app_cert_start_time = app_cert_start_time
        if app_cert_end_time is not None:
            self.app_cert_end_time = app_cert_end_time
        if openapi_ca_cert_id is not None:
            self.openapi_ca_cert_id = openapi_ca_cert_id
        if openapi_ca_cert_start_time is not None:
            self.openapi_ca_cert_start_time = openapi_ca_cert_start_time
        if openapi_ca_cert_end_time is not None:
            self.openapi_ca_cert_end_time = openapi_ca_cert_end_time

    @property
    def auth_config_id(self):
        r"""Gets the auth_config_id of this UosDomainInfo.

        认证配置id。

        :return: The auth_config_id of this UosDomainInfo.
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        r"""Sets the auth_config_id of this UosDomainInfo.

        认证配置id。

        :param auth_config_id: The auth_config_id of this UosDomainInfo.
        :type auth_config_id: str
        """
        self._auth_config_id = auth_config_id

    @property
    def id(self):
        r"""Gets the id of this UosDomainInfo.

        域控id。

        :return: The id of this UosDomainInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UosDomainInfo.

        域控id。

        :param id: The id of this UosDomainInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this UosDomainInfo.

        :return: The type of this UosDomainInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UosDomainInfo.

        :param type: The type of this UosDomainInfo.
        :type type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        self._type = type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UosDomainInfo.

        统信域控名称。

        :return: The domain_name of this UosDomainInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UosDomainInfo.

        统信域控名称。

        :param domain_name: The domain_name of this UosDomainInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def username(self):
        r"""Gets the username of this UosDomainInfo.

        域管理员。

        :return: The username of this UosDomainInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this UosDomainInfo.

        域管理员。

        :param username: The username of this UosDomainInfo.
        :type username: str
        """
        self._username = username

    @property
    def main_dc_address(self):
        r"""Gets the main_dc_address of this UosDomainInfo.

        域管平台地址。

        :return: The main_dc_address of this UosDomainInfo.
        :rtype: str
        """
        return self._main_dc_address

    @main_dc_address.setter
    def main_dc_address(self, main_dc_address):
        r"""Sets the main_dc_address of this UosDomainInfo.

        域管平台地址。

        :param main_dc_address: The main_dc_address of this UosDomainInfo.
        :type main_dc_address: str
        """
        self._main_dc_address = main_dc_address

    @property
    def open_interface_address(self):
        r"""Gets the open_interface_address of this UosDomainInfo.

        域管开放接口地址。

        :return: The open_interface_address of this UosDomainInfo.
        :rtype: str
        """
        return self._open_interface_address

    @open_interface_address.setter
    def open_interface_address(self, open_interface_address):
        r"""Sets the open_interface_address of this UosDomainInfo.

        域管开放接口地址。

        :param open_interface_address: The open_interface_address of this UosDomainInfo.
        :type open_interface_address: str
        """
        self._open_interface_address = open_interface_address

    @property
    def open_interface_domain_name(self):
        r"""Gets the open_interface_domain_name of this UosDomainInfo.

        域管开放接口域名。

        :return: The open_interface_domain_name of this UosDomainInfo.
        :rtype: str
        """
        return self._open_interface_domain_name

    @open_interface_domain_name.setter
    def open_interface_domain_name(self, open_interface_domain_name):
        r"""Sets the open_interface_domain_name of this UosDomainInfo.

        域管开放接口域名。

        :param open_interface_domain_name: The open_interface_domain_name of this UosDomainInfo.
        :type open_interface_domain_name: str
        """
        self._open_interface_domain_name = open_interface_domain_name

    @property
    def internal_service_address(self):
        r"""Gets the internal_service_address of this UosDomainInfo.

        域管内部服务地址。

        :return: The internal_service_address of this UosDomainInfo.
        :rtype: str
        """
        return self._internal_service_address

    @internal_service_address.setter
    def internal_service_address(self, internal_service_address):
        r"""Sets the internal_service_address of this UosDomainInfo.

        域管内部服务地址。

        :param internal_service_address: The internal_service_address of this UosDomainInfo.
        :type internal_service_address: str
        """
        self._internal_service_address = internal_service_address

    @property
    def app_cert_id(self):
        r"""Gets the app_cert_id of this UosDomainInfo.

        客户端证书公钥id。

        :return: The app_cert_id of this UosDomainInfo.
        :rtype: str
        """
        return self._app_cert_id

    @app_cert_id.setter
    def app_cert_id(self, app_cert_id):
        r"""Sets the app_cert_id of this UosDomainInfo.

        客户端证书公钥id。

        :param app_cert_id: The app_cert_id of this UosDomainInfo.
        :type app_cert_id: str
        """
        self._app_cert_id = app_cert_id

    @property
    def app_cert_start_time(self):
        r"""Gets the app_cert_start_time of this UosDomainInfo.

        客户端证书公钥有效期起始时间。

        :return: The app_cert_start_time of this UosDomainInfo.
        :rtype: str
        """
        return self._app_cert_start_time

    @app_cert_start_time.setter
    def app_cert_start_time(self, app_cert_start_time):
        r"""Sets the app_cert_start_time of this UosDomainInfo.

        客户端证书公钥有效期起始时间。

        :param app_cert_start_time: The app_cert_start_time of this UosDomainInfo.
        :type app_cert_start_time: str
        """
        self._app_cert_start_time = app_cert_start_time

    @property
    def app_cert_end_time(self):
        r"""Gets the app_cert_end_time of this UosDomainInfo.

        客户端证书公钥有效期结束时间。

        :return: The app_cert_end_time of this UosDomainInfo.
        :rtype: str
        """
        return self._app_cert_end_time

    @app_cert_end_time.setter
    def app_cert_end_time(self, app_cert_end_time):
        r"""Sets the app_cert_end_time of this UosDomainInfo.

        客户端证书公钥有效期结束时间。

        :param app_cert_end_time: The app_cert_end_time of this UosDomainInfo.
        :type app_cert_end_time: str
        """
        self._app_cert_end_time = app_cert_end_time

    @property
    def openapi_ca_cert_id(self):
        r"""Gets the openapi_ca_cert_id of this UosDomainInfo.

        服务端CA id。

        :return: The openapi_ca_cert_id of this UosDomainInfo.
        :rtype: str
        """
        return self._openapi_ca_cert_id

    @openapi_ca_cert_id.setter
    def openapi_ca_cert_id(self, openapi_ca_cert_id):
        r"""Sets the openapi_ca_cert_id of this UosDomainInfo.

        服务端CA id。

        :param openapi_ca_cert_id: The openapi_ca_cert_id of this UosDomainInfo.
        :type openapi_ca_cert_id: str
        """
        self._openapi_ca_cert_id = openapi_ca_cert_id

    @property
    def openapi_ca_cert_start_time(self):
        r"""Gets the openapi_ca_cert_start_time of this UosDomainInfo.

        服务端CA有效期起始时间。

        :return: The openapi_ca_cert_start_time of this UosDomainInfo.
        :rtype: str
        """
        return self._openapi_ca_cert_start_time

    @openapi_ca_cert_start_time.setter
    def openapi_ca_cert_start_time(self, openapi_ca_cert_start_time):
        r"""Sets the openapi_ca_cert_start_time of this UosDomainInfo.

        服务端CA有效期起始时间。

        :param openapi_ca_cert_start_time: The openapi_ca_cert_start_time of this UosDomainInfo.
        :type openapi_ca_cert_start_time: str
        """
        self._openapi_ca_cert_start_time = openapi_ca_cert_start_time

    @property
    def openapi_ca_cert_end_time(self):
        r"""Gets the openapi_ca_cert_end_time of this UosDomainInfo.

        服务端CA有效期结束时间。

        :return: The openapi_ca_cert_end_time of this UosDomainInfo.
        :rtype: str
        """
        return self._openapi_ca_cert_end_time

    @openapi_ca_cert_end_time.setter
    def openapi_ca_cert_end_time(self, openapi_ca_cert_end_time):
        r"""Sets the openapi_ca_cert_end_time of this UosDomainInfo.

        服务端CA有效期结束时间。

        :param openapi_ca_cert_end_time: The openapi_ca_cert_end_time of this UosDomainInfo.
        :type openapi_ca_cert_end_time: str
        """
        self._openapi_ca_cert_end_time = openapi_ca_cert_end_time

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
        if not isinstance(other, UosDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
