# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MqttBriefConnectionInfo:


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
        'user_name': 'str',
        'qos': 'int'
    }

    attribute_map = {
        'server_address': 'server_address',
        'client_id': 'client_id',
        'auth_type': 'auth_type',
        'user_name': 'user_name',
        'qos': 'qos'
    }

    def __init__(self, server_address=None, client_id=None, auth_type=None, user_name=None, qos=None):
        """MqttBriefConnectionInfo - a model defined in huaweicloud sdk"""
        
        

        self._server_address = None
        self._client_id = None
        self._auth_type = None
        self._user_name = None
        self._qos = None
        self.discriminator = None

        if server_address is not None:
            self.server_address = server_address
        if client_id is not None:
            self.client_id = client_id
        if auth_type is not None:
            self.auth_type = auth_type
        if user_name is not None:
            self.user_name = user_name
        if qos is not None:
            self.qos = qos

    @property
    def server_address(self):
        """Gets the server_address of this MqttBriefConnectionInfo.

        采用cleint方式连接时，mqtt服务器地址

        :return: The server_address of this MqttBriefConnectionInfo.
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """Sets the server_address of this MqttBriefConnectionInfo.

        采用cleint方式连接时，mqtt服务器地址

        :param server_address: The server_address of this MqttBriefConnectionInfo.
        :type: str
        """
        self._server_address = server_address

    @property
    def client_id(self):
        """Gets the client_id of this MqttBriefConnectionInfo.

        mqtt连接时，client_id

        :return: The client_id of this MqttBriefConnectionInfo.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this MqttBriefConnectionInfo.

        mqtt连接时，client_id

        :param client_id: The client_id of this MqttBriefConnectionInfo.
        :type: str
        """
        self._client_id = client_id

    @property
    def auth_type(self):
        """Gets the auth_type of this MqttBriefConnectionInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写user_name和user_name字段，使用证书认证接入方式(CERTIFICATES)填写privateKey和certificate字段

        :return: The auth_type of this MqttBriefConnectionInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this MqttBriefConnectionInfo.

        鉴权类型。支持密钥认证接入(SECRET)和证书认证接入(CERTIFICATES)两种方式。使用密钥认证接入方式(SECRET)填写user_name和user_name字段，使用证书认证接入方式(CERTIFICATES)填写privateKey和certificate字段

        :param auth_type: The auth_type of this MqttBriefConnectionInfo.
        :type: str
        """
        self._auth_type = auth_type

    @property
    def user_name(self):
        """Gets the user_name of this MqttBriefConnectionInfo.

        用户名

        :return: The user_name of this MqttBriefConnectionInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this MqttBriefConnectionInfo.

        用户名

        :param user_name: The user_name of this MqttBriefConnectionInfo.
        :type: str
        """
        self._user_name = user_name

    @property
    def qos(self):
        """Gets the qos of this MqttBriefConnectionInfo.

        服务质量,默认为0,表示最多一次的传输,1表示至少一次,2表示仅一次.

        :return: The qos of this MqttBriefConnectionInfo.
        :rtype: int
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """Sets the qos of this MqttBriefConnectionInfo.

        服务质量,默认为0,表示最多一次的传输,1表示至少一次,2表示仅一次.

        :param qos: The qos of this MqttBriefConnectionInfo.
        :type: int
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
        if not isinstance(other, MqttBriefConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
