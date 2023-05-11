# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuthInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_info_name': 'str',
        'user_name': 'str',
        'password': 'str',
        'krb5_conf': 'str',
        'keytab': 'str',
        'truststore_location': 'str',
        'truststore_password': 'str',
        'keystore_location': 'str',
        'keystore_password': 'str'
    }

    attribute_map = {
        'auth_info_name': 'auth_info_name',
        'user_name': 'user_name',
        'password': 'password',
        'krb5_conf': 'krb5_conf',
        'keytab': 'keytab',
        'truststore_location': 'truststore_location',
        'truststore_password': 'truststore_password',
        'keystore_location': 'keystore_location',
        'keystore_password': 'keystore_password'
    }

    def __init__(self, auth_info_name=None, user_name=None, password=None, krb5_conf=None, keytab=None, truststore_location=None, truststore_password=None, keystore_location=None, keystore_password=None):
        """UpdateAuthInfoRequestBody

        The model defined in huaweicloud sdk

        :param auth_info_name: 证书名
        :type auth_info_name: str
        :param user_name: 用户安全集群的新登录用户名
        :type user_name: str
        :param password: 用户安全集群的新登录密码
        :type password: str
        :param krb5_conf: krb5配置文件obs路径
        :type krb5_conf: str
        :param keytab: keytab配置文件obs路径
        :type keytab: str
        :param truststore_location: truststore配置文件obs路径
        :type truststore_location: str
        :param truststore_password: truststore配置文件密码
        :type truststore_password: str
        :param keystore_location: keystore配置文件obs路径
        :type keystore_location: str
        :param keystore_password: keystore配置文件密码
        :type keystore_password: str
        """
        
        

        self._auth_info_name = None
        self._user_name = None
        self._password = None
        self._krb5_conf = None
        self._keytab = None
        self._truststore_location = None
        self._truststore_password = None
        self._keystore_location = None
        self._keystore_password = None
        self.discriminator = None

        self.auth_info_name = auth_info_name
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if krb5_conf is not None:
            self.krb5_conf = krb5_conf
        if keytab is not None:
            self.keytab = keytab
        if truststore_location is not None:
            self.truststore_location = truststore_location
        if truststore_password is not None:
            self.truststore_password = truststore_password
        if keystore_location is not None:
            self.keystore_location = keystore_location
        if keystore_password is not None:
            self.keystore_password = keystore_password

    @property
    def auth_info_name(self):
        """Gets the auth_info_name of this UpdateAuthInfoRequestBody.

        证书名

        :return: The auth_info_name of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._auth_info_name

    @auth_info_name.setter
    def auth_info_name(self, auth_info_name):
        """Sets the auth_info_name of this UpdateAuthInfoRequestBody.

        证书名

        :param auth_info_name: The auth_info_name of this UpdateAuthInfoRequestBody.
        :type auth_info_name: str
        """
        self._auth_info_name = auth_info_name

    @property
    def user_name(self):
        """Gets the user_name of this UpdateAuthInfoRequestBody.

        用户安全集群的新登录用户名

        :return: The user_name of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateAuthInfoRequestBody.

        用户安全集群的新登录用户名

        :param user_name: The user_name of this UpdateAuthInfoRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this UpdateAuthInfoRequestBody.

        用户安全集群的新登录密码

        :return: The password of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateAuthInfoRequestBody.

        用户安全集群的新登录密码

        :param password: The password of this UpdateAuthInfoRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def krb5_conf(self):
        """Gets the krb5_conf of this UpdateAuthInfoRequestBody.

        krb5配置文件obs路径

        :return: The krb5_conf of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._krb5_conf

    @krb5_conf.setter
    def krb5_conf(self, krb5_conf):
        """Sets the krb5_conf of this UpdateAuthInfoRequestBody.

        krb5配置文件obs路径

        :param krb5_conf: The krb5_conf of this UpdateAuthInfoRequestBody.
        :type krb5_conf: str
        """
        self._krb5_conf = krb5_conf

    @property
    def keytab(self):
        """Gets the keytab of this UpdateAuthInfoRequestBody.

        keytab配置文件obs路径

        :return: The keytab of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._keytab

    @keytab.setter
    def keytab(self, keytab):
        """Sets the keytab of this UpdateAuthInfoRequestBody.

        keytab配置文件obs路径

        :param keytab: The keytab of this UpdateAuthInfoRequestBody.
        :type keytab: str
        """
        self._keytab = keytab

    @property
    def truststore_location(self):
        """Gets the truststore_location of this UpdateAuthInfoRequestBody.

        truststore配置文件obs路径

        :return: The truststore_location of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._truststore_location

    @truststore_location.setter
    def truststore_location(self, truststore_location):
        """Sets the truststore_location of this UpdateAuthInfoRequestBody.

        truststore配置文件obs路径

        :param truststore_location: The truststore_location of this UpdateAuthInfoRequestBody.
        :type truststore_location: str
        """
        self._truststore_location = truststore_location

    @property
    def truststore_password(self):
        """Gets the truststore_password of this UpdateAuthInfoRequestBody.

        truststore配置文件密码

        :return: The truststore_password of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._truststore_password

    @truststore_password.setter
    def truststore_password(self, truststore_password):
        """Sets the truststore_password of this UpdateAuthInfoRequestBody.

        truststore配置文件密码

        :param truststore_password: The truststore_password of this UpdateAuthInfoRequestBody.
        :type truststore_password: str
        """
        self._truststore_password = truststore_password

    @property
    def keystore_location(self):
        """Gets the keystore_location of this UpdateAuthInfoRequestBody.

        keystore配置文件obs路径

        :return: The keystore_location of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._keystore_location

    @keystore_location.setter
    def keystore_location(self, keystore_location):
        """Sets the keystore_location of this UpdateAuthInfoRequestBody.

        keystore配置文件obs路径

        :param keystore_location: The keystore_location of this UpdateAuthInfoRequestBody.
        :type keystore_location: str
        """
        self._keystore_location = keystore_location

    @property
    def keystore_password(self):
        """Gets the keystore_password of this UpdateAuthInfoRequestBody.

        keystore配置文件密码

        :return: The keystore_password of this UpdateAuthInfoRequestBody.
        :rtype: str
        """
        return self._keystore_password

    @keystore_password.setter
    def keystore_password(self, keystore_password):
        """Sets the keystore_password of this UpdateAuthInfoRequestBody.

        keystore配置文件密码

        :param keystore_password: The keystore_password of this UpdateAuthInfoRequestBody.
        :type keystore_password: str
        """
        self._keystore_password = keystore_password

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
        if not isinstance(other, UpdateAuthInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
