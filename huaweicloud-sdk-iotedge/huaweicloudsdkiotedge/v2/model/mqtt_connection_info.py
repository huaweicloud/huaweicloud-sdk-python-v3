# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MqttConnectionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_address': 'str',
        'client_id': 'str',
        'auth_type': 'str',
        'private_key': 'str',
        'certificate': 'str',
        'user_name': 'str',
        'password': 'str',
        'qos': 'int'
    }

    attribute_map = {
        'server_address': 'server_address',
        'client_id': 'client_id',
        'auth_type': 'auth_type',
        'private_key': 'private_key',
        'certificate': 'certificate',
        'user_name': 'user_name',
        'password': 'password',
        'qos': 'qos'
    }

    def __init__(self, server_address=None, client_id=None, auth_type=None, private_key=None, certificate=None, user_name=None, password=None, qos=None):
        r"""MqttConnectionInfo

        The model defined in huaweicloud sdk

        :param server_address: 采用cleint方式连接时，mqtt服务器地址
        :type server_address: str
        :param client_id: mqtt连接时，client_id
        :type client_id: str
        :param auth_type: 鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写user_name和user_name字段，使用证书认证接入方式(CERTIFICATES)填写privateKey和certificate字段
        :type auth_type: str
        :param private_key: 证书秘钥
        :type private_key: str
        :param certificate: 证书
        :type certificate: str
        :param user_name: 用户名
        :type user_name: str
        :param password: 密码
        :type password: str
        :param qos: 服务质量,默认为0,表示最多一次的传输,1表示至少一次,2表示仅一次.
        :type qos: int
        """
        
        

        self._server_address = None
        self._client_id = None
        self._auth_type = None
        self._private_key = None
        self._certificate = None
        self._user_name = None
        self._password = None
        self._qos = None
        self.discriminator = None

        if server_address is not None:
            self.server_address = server_address
        if client_id is not None:
            self.client_id = client_id
        if auth_type is not None:
            self.auth_type = auth_type
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if qos is not None:
            self.qos = qos

    @property
    def server_address(self):
        r"""Gets the server_address of this MqttConnectionInfo.

        采用cleint方式连接时，mqtt服务器地址

        :return: The server_address of this MqttConnectionInfo.
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        r"""Sets the server_address of this MqttConnectionInfo.

        采用cleint方式连接时，mqtt服务器地址

        :param server_address: The server_address of this MqttConnectionInfo.
        :type server_address: str
        """
        self._server_address = server_address

    @property
    def client_id(self):
        r"""Gets the client_id of this MqttConnectionInfo.

        mqtt连接时，client_id

        :return: The client_id of this MqttConnectionInfo.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this MqttConnectionInfo.

        mqtt连接时，client_id

        :param client_id: The client_id of this MqttConnectionInfo.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def auth_type(self):
        r"""Gets the auth_type of this MqttConnectionInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写user_name和user_name字段，使用证书认证接入方式(CERTIFICATES)填写privateKey和certificate字段

        :return: The auth_type of this MqttConnectionInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this MqttConnectionInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写user_name和user_name字段，使用证书认证接入方式(CERTIFICATES)填写privateKey和certificate字段

        :param auth_type: The auth_type of this MqttConnectionInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def private_key(self):
        r"""Gets the private_key of this MqttConnectionInfo.

        证书秘钥

        :return: The private_key of this MqttConnectionInfo.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this MqttConnectionInfo.

        证书秘钥

        :param private_key: The private_key of this MqttConnectionInfo.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        r"""Gets the certificate of this MqttConnectionInfo.

        证书

        :return: The certificate of this MqttConnectionInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this MqttConnectionInfo.

        证书

        :param certificate: The certificate of this MqttConnectionInfo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def user_name(self):
        r"""Gets the user_name of this MqttConnectionInfo.

        用户名

        :return: The user_name of this MqttConnectionInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this MqttConnectionInfo.

        用户名

        :param user_name: The user_name of this MqttConnectionInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this MqttConnectionInfo.

        密码

        :return: The password of this MqttConnectionInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this MqttConnectionInfo.

        密码

        :param password: The password of this MqttConnectionInfo.
        :type password: str
        """
        self._password = password

    @property
    def qos(self):
        r"""Gets the qos of this MqttConnectionInfo.

        服务质量,默认为0,表示最多一次的传输,1表示至少一次,2表示仅一次.

        :return: The qos of this MqttConnectionInfo.
        :rtype: int
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        r"""Sets the qos of this MqttConnectionInfo.

        服务质量,默认为0,表示最多一次的传输,1表示至少一次,2表示仅一次.

        :param qos: The qos of this MqttConnectionInfo.
        :type qos: int
        """
        self._qos = qos

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
        if not isinstance(other, MqttConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
