# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceKafkaMQParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addr': 'str',
        'group': 'str',
        'instance_name': 'str',
        'security_protocol': 'str',
        'instance_id': 'str',
        'topic': 'str',
        'seek_to': 'str',
        'enable_sasl_ssl': 'bool',
        'sasl_mechanism': 'str',
        'ssl_certificate_url': 'str',
        'ssl_certificate_pwd': 'str',
        'user_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'addr': 'addr',
        'group': 'group',
        'instance_name': 'instance_name',
        'security_protocol': 'security_protocol',
        'instance_id': 'instance_id',
        'topic': 'topic',
        'seek_to': 'seek_to',
        'enable_sasl_ssl': 'enable_sasl_ssl',
        'sasl_mechanism': 'sasl_mechanism',
        'ssl_certificate_url': 'ssl_certificate_url',
        'ssl_certificate_pwd': 'ssl_certificate_pwd',
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, addr=None, group=None, instance_name=None, security_protocol=None, instance_id=None, topic=None, seek_to=None, enable_sasl_ssl=None, sasl_mechanism=None, ssl_certificate_url=None, ssl_certificate_pwd=None, user_name=None, password=None):
        r"""SourceKafkaMQParameters

        The model defined in huaweicloud sdk

        :param addr: kafka连接地址
        :type addr: str
        :param group: kafka消费组
        :type group: str
        :param instance_name: kafka实例名称
        :type instance_name: str
        :param security_protocol: 安全协议
        :type security_protocol: str
        :param instance_id: kafka实例ID
        :type instance_id: str
        :param topic: kafka topic名称
        :type topic: str
        :param seek_to: 消费点位
        :type seek_to: str
        :param enable_sasl_ssl: SASL_SSL是否开启
        :type enable_sasl_ssl: bool
        :param sasl_mechanism: SASL认证机制
        :type sasl_mechanism: str
        :param ssl_certificate_url: SASL证书地址，配置的obs地址
        :type ssl_certificate_url: str
        :param ssl_certificate_pwd: SASL证书密码
        :type ssl_certificate_pwd: str
        :param user_name: 用户名
        :type user_name: str
        :param password: 用户密码
        :type password: str
        """
        
        

        self._addr = None
        self._group = None
        self._instance_name = None
        self._security_protocol = None
        self._instance_id = None
        self._topic = None
        self._seek_to = None
        self._enable_sasl_ssl = None
        self._sasl_mechanism = None
        self._ssl_certificate_url = None
        self._ssl_certificate_pwd = None
        self._user_name = None
        self._password = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        self.group = group
        if instance_name is not None:
            self.instance_name = instance_name
        if security_protocol is not None:
            self.security_protocol = security_protocol
        if instance_id is not None:
            self.instance_id = instance_id
        self.topic = topic
        if seek_to is not None:
            self.seek_to = seek_to
        if enable_sasl_ssl is not None:
            self.enable_sasl_ssl = enable_sasl_ssl
        if sasl_mechanism is not None:
            self.sasl_mechanism = sasl_mechanism
        if ssl_certificate_url is not None:
            self.ssl_certificate_url = ssl_certificate_url
        if ssl_certificate_pwd is not None:
            self.ssl_certificate_pwd = ssl_certificate_pwd
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @property
    def addr(self):
        r"""Gets the addr of this SourceKafkaMQParameters.

        kafka连接地址

        :return: The addr of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this SourceKafkaMQParameters.

        kafka连接地址

        :param addr: The addr of this SourceKafkaMQParameters.
        :type addr: str
        """
        self._addr = addr

    @property
    def group(self):
        r"""Gets the group of this SourceKafkaMQParameters.

        kafka消费组

        :return: The group of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this SourceKafkaMQParameters.

        kafka消费组

        :param group: The group of this SourceKafkaMQParameters.
        :type group: str
        """
        self._group = group

    @property
    def instance_name(self):
        r"""Gets the instance_name of this SourceKafkaMQParameters.

        kafka实例名称

        :return: The instance_name of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this SourceKafkaMQParameters.

        kafka实例名称

        :param instance_name: The instance_name of this SourceKafkaMQParameters.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def security_protocol(self):
        r"""Gets the security_protocol of this SourceKafkaMQParameters.

        安全协议

        :return: The security_protocol of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        r"""Sets the security_protocol of this SourceKafkaMQParameters.

        安全协议

        :param security_protocol: The security_protocol of this SourceKafkaMQParameters.
        :type security_protocol: str
        """
        self._security_protocol = security_protocol

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SourceKafkaMQParameters.

        kafka实例ID

        :return: The instance_id of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SourceKafkaMQParameters.

        kafka实例ID

        :param instance_id: The instance_id of this SourceKafkaMQParameters.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        r"""Gets the topic of this SourceKafkaMQParameters.

        kafka topic名称

        :return: The topic of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SourceKafkaMQParameters.

        kafka topic名称

        :param topic: The topic of this SourceKafkaMQParameters.
        :type topic: str
        """
        self._topic = topic

    @property
    def seek_to(self):
        r"""Gets the seek_to of this SourceKafkaMQParameters.

        消费点位

        :return: The seek_to of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._seek_to

    @seek_to.setter
    def seek_to(self, seek_to):
        r"""Sets the seek_to of this SourceKafkaMQParameters.

        消费点位

        :param seek_to: The seek_to of this SourceKafkaMQParameters.
        :type seek_to: str
        """
        self._seek_to = seek_to

    @property
    def enable_sasl_ssl(self):
        r"""Gets the enable_sasl_ssl of this SourceKafkaMQParameters.

        SASL_SSL是否开启

        :return: The enable_sasl_ssl of this SourceKafkaMQParameters.
        :rtype: bool
        """
        return self._enable_sasl_ssl

    @enable_sasl_ssl.setter
    def enable_sasl_ssl(self, enable_sasl_ssl):
        r"""Sets the enable_sasl_ssl of this SourceKafkaMQParameters.

        SASL_SSL是否开启

        :param enable_sasl_ssl: The enable_sasl_ssl of this SourceKafkaMQParameters.
        :type enable_sasl_ssl: bool
        """
        self._enable_sasl_ssl = enable_sasl_ssl

    @property
    def sasl_mechanism(self):
        r"""Gets the sasl_mechanism of this SourceKafkaMQParameters.

        SASL认证机制

        :return: The sasl_mechanism of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._sasl_mechanism

    @sasl_mechanism.setter
    def sasl_mechanism(self, sasl_mechanism):
        r"""Sets the sasl_mechanism of this SourceKafkaMQParameters.

        SASL认证机制

        :param sasl_mechanism: The sasl_mechanism of this SourceKafkaMQParameters.
        :type sasl_mechanism: str
        """
        self._sasl_mechanism = sasl_mechanism

    @property
    def ssl_certificate_url(self):
        r"""Gets the ssl_certificate_url of this SourceKafkaMQParameters.

        SASL证书地址，配置的obs地址

        :return: The ssl_certificate_url of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._ssl_certificate_url

    @ssl_certificate_url.setter
    def ssl_certificate_url(self, ssl_certificate_url):
        r"""Sets the ssl_certificate_url of this SourceKafkaMQParameters.

        SASL证书地址，配置的obs地址

        :param ssl_certificate_url: The ssl_certificate_url of this SourceKafkaMQParameters.
        :type ssl_certificate_url: str
        """
        self._ssl_certificate_url = ssl_certificate_url

    @property
    def ssl_certificate_pwd(self):
        r"""Gets the ssl_certificate_pwd of this SourceKafkaMQParameters.

        SASL证书密码

        :return: The ssl_certificate_pwd of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._ssl_certificate_pwd

    @ssl_certificate_pwd.setter
    def ssl_certificate_pwd(self, ssl_certificate_pwd):
        r"""Sets the ssl_certificate_pwd of this SourceKafkaMQParameters.

        SASL证书密码

        :param ssl_certificate_pwd: The ssl_certificate_pwd of this SourceKafkaMQParameters.
        :type ssl_certificate_pwd: str
        """
        self._ssl_certificate_pwd = ssl_certificate_pwd

    @property
    def user_name(self):
        r"""Gets the user_name of this SourceKafkaMQParameters.

        用户名

        :return: The user_name of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SourceKafkaMQParameters.

        用户名

        :param user_name: The user_name of this SourceKafkaMQParameters.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this SourceKafkaMQParameters.

        用户密码

        :return: The password of this SourceKafkaMQParameters.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this SourceKafkaMQParameters.

        用户密码

        :param password: The password of this SourceKafkaMQParameters.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, SourceKafkaMQParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
