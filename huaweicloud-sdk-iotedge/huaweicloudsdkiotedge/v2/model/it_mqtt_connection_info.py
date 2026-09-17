# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItMqttConnectionInfo:

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
        'password': 'str',
        'trust_certs': 'object',
        'verify_hostname': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'trust_certs': 'trust_certs',
        'verify_hostname': 'verify_hostname'
    }

    def __init__(self, username=None, password=None, trust_certs=None, verify_hostname=None):
        r"""ItMqttConnectionInfo

        The model defined in huaweicloud sdk

        :param username: 鉴权用户名
        :type username: str
        :param password: 鉴权密码
        :type password: str
        :param trust_certs: 客户端信任证书列表
        :type trust_certs: object
        :param verify_hostname: 客户端是否开启校验域名
        :type verify_hostname: bool
        """
        
        

        self._username = None
        self._password = None
        self._trust_certs = None
        self._verify_hostname = None
        self.discriminator = None

        self.username = username
        self.password = password
        if trust_certs is not None:
            self.trust_certs = trust_certs
        if verify_hostname is not None:
            self.verify_hostname = verify_hostname

    @property
    def username(self):
        r"""Gets the username of this ItMqttConnectionInfo.

        鉴权用户名

        :return: The username of this ItMqttConnectionInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ItMqttConnectionInfo.

        鉴权用户名

        :param username: The username of this ItMqttConnectionInfo.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this ItMqttConnectionInfo.

        鉴权密码

        :return: The password of this ItMqttConnectionInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ItMqttConnectionInfo.

        鉴权密码

        :param password: The password of this ItMqttConnectionInfo.
        :type password: str
        """
        self._password = password

    @property
    def trust_certs(self):
        r"""Gets the trust_certs of this ItMqttConnectionInfo.

        客户端信任证书列表

        :return: The trust_certs of this ItMqttConnectionInfo.
        :rtype: object
        """
        return self._trust_certs

    @trust_certs.setter
    def trust_certs(self, trust_certs):
        r"""Sets the trust_certs of this ItMqttConnectionInfo.

        客户端信任证书列表

        :param trust_certs: The trust_certs of this ItMqttConnectionInfo.
        :type trust_certs: object
        """
        self._trust_certs = trust_certs

    @property
    def verify_hostname(self):
        r"""Gets the verify_hostname of this ItMqttConnectionInfo.

        客户端是否开启校验域名

        :return: The verify_hostname of this ItMqttConnectionInfo.
        :rtype: bool
        """
        return self._verify_hostname

    @verify_hostname.setter
    def verify_hostname(self, verify_hostname):
        r"""Sets the verify_hostname of this ItMqttConnectionInfo.

        客户端是否开启校验域名

        :param verify_hostname: The verify_hostname of this ItMqttConnectionInfo.
        :type verify_hostname: bool
        """
        self._verify_hostname = verify_hostname

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
        if not isinstance(other, ItMqttConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
