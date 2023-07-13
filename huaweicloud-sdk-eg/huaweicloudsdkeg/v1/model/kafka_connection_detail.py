# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaConnectionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'addr': 'str',
        'sasl_ssl': 'bool',
        'username': 'str',
        'password': 'str',
        'acks': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'addr': 'addr',
        'sasl_ssl': 'sasl_ssl',
        'username': 'username',
        'password': 'password',
        'acks': 'acks'
    }

    def __init__(self, instance_id=None, addr=None, sasl_ssl=None, username=None, password=None, acks=None):
        """KafkaConnectionDetail

        The model defined in huaweicloud sdk

        :param instance_id: kafka实例id。
        :type instance_id: str
        :param addr: kafka连接地址。
        :type addr: str
        :param sasl_ssl: kafka实例是否开启了SASL_SSL。
        :type sasl_ssl: bool
        :param username: kafka实例用户名。实例开启了SASL_SSL时必填
        :type username: str
        :param password: kafka实例密码。实例开启了SASL_SSL时必填
        :type password: str
        :param acks: 收到Server端确认信号个数，表示procuder需要收到多少个这样的确认信号，算消息发送成功。acks参数代表了数据备份的可用性。支持选项： acks&#x3D;0：表示producer不需要等待任何确认收到的信息，副本将立即加到socket buffer并认为已经发送。没有任何保障可以保证此种情况下server已经成功接收数据，同时重试配置不会发生作用（因为客户端不知道是否失败）回馈的offset会总是设置为-1。 acks&#x3D;1：这意味着至少要等待leader已经成功将数据写入本地log，但是并没有等待所有follower是否成功写入。如果follower没有成功备份数据，而此时leader又无法提供服务，则消息会丢失。 acks&#x3D;all：这意味着leader需要等待ISR中所有备份都成功写入日志，只有任何一个备份存活，数据都不会丢失。min.insync.replicas指定必须确认写入才能被认为成功的副本的最小数量。
        :type acks: str
        """
        
        

        self._instance_id = None
        self._addr = None
        self._sasl_ssl = None
        self._username = None
        self._password = None
        self._acks = None
        self.discriminator = None

        self.instance_id = instance_id
        self.addr = addr
        self.sasl_ssl = sasl_ssl
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if acks is not None:
            self.acks = acks

    @property
    def instance_id(self):
        """Gets the instance_id of this KafkaConnectionDetail.

        kafka实例id。

        :return: The instance_id of this KafkaConnectionDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this KafkaConnectionDetail.

        kafka实例id。

        :param instance_id: The instance_id of this KafkaConnectionDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def addr(self):
        """Gets the addr of this KafkaConnectionDetail.

        kafka连接地址。

        :return: The addr of this KafkaConnectionDetail.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this KafkaConnectionDetail.

        kafka连接地址。

        :param addr: The addr of this KafkaConnectionDetail.
        :type addr: str
        """
        self._addr = addr

    @property
    def sasl_ssl(self):
        """Gets the sasl_ssl of this KafkaConnectionDetail.

        kafka实例是否开启了SASL_SSL。

        :return: The sasl_ssl of this KafkaConnectionDetail.
        :rtype: bool
        """
        return self._sasl_ssl

    @sasl_ssl.setter
    def sasl_ssl(self, sasl_ssl):
        """Sets the sasl_ssl of this KafkaConnectionDetail.

        kafka实例是否开启了SASL_SSL。

        :param sasl_ssl: The sasl_ssl of this KafkaConnectionDetail.
        :type sasl_ssl: bool
        """
        self._sasl_ssl = sasl_ssl

    @property
    def username(self):
        """Gets the username of this KafkaConnectionDetail.

        kafka实例用户名。实例开启了SASL_SSL时必填

        :return: The username of this KafkaConnectionDetail.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this KafkaConnectionDetail.

        kafka实例用户名。实例开启了SASL_SSL时必填

        :param username: The username of this KafkaConnectionDetail.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this KafkaConnectionDetail.

        kafka实例密码。实例开启了SASL_SSL时必填

        :return: The password of this KafkaConnectionDetail.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this KafkaConnectionDetail.

        kafka实例密码。实例开启了SASL_SSL时必填

        :param password: The password of this KafkaConnectionDetail.
        :type password: str
        """
        self._password = password

    @property
    def acks(self):
        """Gets the acks of this KafkaConnectionDetail.

        收到Server端确认信号个数，表示procuder需要收到多少个这样的确认信号，算消息发送成功。acks参数代表了数据备份的可用性。支持选项： acks=0：表示producer不需要等待任何确认收到的信息，副本将立即加到socket buffer并认为已经发送。没有任何保障可以保证此种情况下server已经成功接收数据，同时重试配置不会发生作用（因为客户端不知道是否失败）回馈的offset会总是设置为-1。 acks=1：这意味着至少要等待leader已经成功将数据写入本地log，但是并没有等待所有follower是否成功写入。如果follower没有成功备份数据，而此时leader又无法提供服务，则消息会丢失。 acks=all：这意味着leader需要等待ISR中所有备份都成功写入日志，只有任何一个备份存活，数据都不会丢失。min.insync.replicas指定必须确认写入才能被认为成功的副本的最小数量。

        :return: The acks of this KafkaConnectionDetail.
        :rtype: str
        """
        return self._acks

    @acks.setter
    def acks(self, acks):
        """Sets the acks of this KafkaConnectionDetail.

        收到Server端确认信号个数，表示procuder需要收到多少个这样的确认信号，算消息发送成功。acks参数代表了数据备份的可用性。支持选项： acks=0：表示producer不需要等待任何确认收到的信息，副本将立即加到socket buffer并认为已经发送。没有任何保障可以保证此种情况下server已经成功接收数据，同时重试配置不会发生作用（因为客户端不知道是否失败）回馈的offset会总是设置为-1。 acks=1：这意味着至少要等待leader已经成功将数据写入本地log，但是并没有等待所有follower是否成功写入。如果follower没有成功备份数据，而此时leader又无法提供服务，则消息会丢失。 acks=all：这意味着leader需要等待ISR中所有备份都成功写入日志，只有任何一个备份存活，数据都不会丢失。min.insync.replicas指定必须确认写入才能被认为成功的副本的最小数量。

        :param acks: The acks of this KafkaConnectionDetail.
        :type acks: str
        """
        self._acks = acks

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
        if not isinstance(other, KafkaConnectionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
