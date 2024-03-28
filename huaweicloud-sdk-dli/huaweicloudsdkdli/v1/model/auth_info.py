# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthInfo:

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
        'certificate_location': 'str',
        'datasource_type': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'krb5_conf': 'str',
        'keytab': 'str',
        'truststore_location': 'str',
        'keystore_location': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'auth_info_name': 'auth_info_name',
        'user_name': 'user_name',
        'certificate_location': 'certificate_location',
        'datasource_type': 'datasource_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'krb5_conf': 'krb5_conf',
        'keytab': 'keytab',
        'truststore_location': 'truststore_location',
        'keystore_location': 'keystore_location',
        'owner': 'owner'
    }

    def __init__(self, auth_info_name=None, user_name=None, certificate_location=None, datasource_type=None, create_time=None, update_time=None, krb5_conf=None, keytab=None, truststore_location=None, keystore_location=None, owner=None):
        """AuthInfo

        The model defined in huaweicloud sdk

        :param auth_info_name: 用户安全集群的登录用户名
        :type auth_info_name: str
        :param user_name: 用户安全集群的登录密码
        :type user_name: str
        :param certificate_location: 用户安全集群的证书路径，目前只支持OBS路径，cer类型文件
        :type certificate_location: str
        :param datasource_type: 数据源类型，目前支持CSS,KRB,passwd,Kafka_SSL
        :type datasource_type: str
        :param create_time: 创建时间戳
        :type create_time: int
        :param update_time: 更新时间戳
        :type update_time: int
        :param krb5_conf: krb5配置文件obs路径
        :type krb5_conf: str
        :param keytab: keytab配置文件obs路径
        :type keytab: str
        :param truststore_location: truststore配置文件obs路径
        :type truststore_location: str
        :param keystore_location: keystore配置文件obs路径
        :type keystore_location: str
        :param owner: 所属用户名
        :type owner: str
        """
        
        

        self._auth_info_name = None
        self._user_name = None
        self._certificate_location = None
        self._datasource_type = None
        self._create_time = None
        self._update_time = None
        self._krb5_conf = None
        self._keytab = None
        self._truststore_location = None
        self._keystore_location = None
        self._owner = None
        self.discriminator = None

        if auth_info_name is not None:
            self.auth_info_name = auth_info_name
        if user_name is not None:
            self.user_name = user_name
        if certificate_location is not None:
            self.certificate_location = certificate_location
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if krb5_conf is not None:
            self.krb5_conf = krb5_conf
        if keytab is not None:
            self.keytab = keytab
        if truststore_location is not None:
            self.truststore_location = truststore_location
        if keystore_location is not None:
            self.keystore_location = keystore_location
        if owner is not None:
            self.owner = owner

    @property
    def auth_info_name(self):
        """Gets the auth_info_name of this AuthInfo.

        用户安全集群的登录用户名

        :return: The auth_info_name of this AuthInfo.
        :rtype: str
        """
        return self._auth_info_name

    @auth_info_name.setter
    def auth_info_name(self, auth_info_name):
        """Sets the auth_info_name of this AuthInfo.

        用户安全集群的登录用户名

        :param auth_info_name: The auth_info_name of this AuthInfo.
        :type auth_info_name: str
        """
        self._auth_info_name = auth_info_name

    @property
    def user_name(self):
        """Gets the user_name of this AuthInfo.

        用户安全集群的登录密码

        :return: The user_name of this AuthInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuthInfo.

        用户安全集群的登录密码

        :param user_name: The user_name of this AuthInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def certificate_location(self):
        """Gets the certificate_location of this AuthInfo.

        用户安全集群的证书路径，目前只支持OBS路径，cer类型文件

        :return: The certificate_location of this AuthInfo.
        :rtype: str
        """
        return self._certificate_location

    @certificate_location.setter
    def certificate_location(self, certificate_location):
        """Sets the certificate_location of this AuthInfo.

        用户安全集群的证书路径，目前只支持OBS路径，cer类型文件

        :param certificate_location: The certificate_location of this AuthInfo.
        :type certificate_location: str
        """
        self._certificate_location = certificate_location

    @property
    def datasource_type(self):
        """Gets the datasource_type of this AuthInfo.

        数据源类型，目前支持CSS,KRB,passwd,Kafka_SSL

        :return: The datasource_type of this AuthInfo.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this AuthInfo.

        数据源类型，目前支持CSS,KRB,passwd,Kafka_SSL

        :param datasource_type: The datasource_type of this AuthInfo.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def create_time(self):
        """Gets the create_time of this AuthInfo.

        创建时间戳

        :return: The create_time of this AuthInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AuthInfo.

        创建时间戳

        :param create_time: The create_time of this AuthInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AuthInfo.

        更新时间戳

        :return: The update_time of this AuthInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AuthInfo.

        更新时间戳

        :param update_time: The update_time of this AuthInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def krb5_conf(self):
        """Gets the krb5_conf of this AuthInfo.

        krb5配置文件obs路径

        :return: The krb5_conf of this AuthInfo.
        :rtype: str
        """
        return self._krb5_conf

    @krb5_conf.setter
    def krb5_conf(self, krb5_conf):
        """Sets the krb5_conf of this AuthInfo.

        krb5配置文件obs路径

        :param krb5_conf: The krb5_conf of this AuthInfo.
        :type krb5_conf: str
        """
        self._krb5_conf = krb5_conf

    @property
    def keytab(self):
        """Gets the keytab of this AuthInfo.

        keytab配置文件obs路径

        :return: The keytab of this AuthInfo.
        :rtype: str
        """
        return self._keytab

    @keytab.setter
    def keytab(self, keytab):
        """Sets the keytab of this AuthInfo.

        keytab配置文件obs路径

        :param keytab: The keytab of this AuthInfo.
        :type keytab: str
        """
        self._keytab = keytab

    @property
    def truststore_location(self):
        """Gets the truststore_location of this AuthInfo.

        truststore配置文件obs路径

        :return: The truststore_location of this AuthInfo.
        :rtype: str
        """
        return self._truststore_location

    @truststore_location.setter
    def truststore_location(self, truststore_location):
        """Sets the truststore_location of this AuthInfo.

        truststore配置文件obs路径

        :param truststore_location: The truststore_location of this AuthInfo.
        :type truststore_location: str
        """
        self._truststore_location = truststore_location

    @property
    def keystore_location(self):
        """Gets the keystore_location of this AuthInfo.

        keystore配置文件obs路径

        :return: The keystore_location of this AuthInfo.
        :rtype: str
        """
        return self._keystore_location

    @keystore_location.setter
    def keystore_location(self, keystore_location):
        """Sets the keystore_location of this AuthInfo.

        keystore配置文件obs路径

        :param keystore_location: The keystore_location of this AuthInfo.
        :type keystore_location: str
        """
        self._keystore_location = keystore_location

    @property
    def owner(self):
        """Gets the owner of this AuthInfo.

        所属用户名

        :return: The owner of this AuthInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AuthInfo.

        所属用户名

        :param owner: The owner of this AuthInfo.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, AuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
