# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKafkaUserClientQuotaTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'client': 'str',
        'user_default': 'bool',
        'client_default': 'bool',
        'producer_byte_rate': 'int',
        'consumer_byte_rate': 'int'
    }

    attribute_map = {
        'user': 'user',
        'client': 'client',
        'user_default': 'user-default',
        'client_default': 'client-default',
        'producer_byte_rate': 'producer-byte-rate',
        'consumer_byte_rate': 'consumer-byte-rate'
    }

    def __init__(self, user=None, client=None, user_default=None, client_default=None, producer_byte_rate=None, consumer_byte_rate=None):
        """CreateKafkaUserClientQuotaTaskReq

        The model defined in huaweicloud sdk

        :param user: 用户名
        :type user: str
        :param client: 客户端ID
        :type client: str
        :param user_default: 是否使用用户默认设置（是则表示对全部用户限流）。
        :type user_default: bool
        :param client_default: 是否使用客户端默认设置（是则表示对全部客户端限流）。
        :type client_default: bool
        :param producer_byte_rate: 生产上限速率（单位为B/s）
        :type producer_byte_rate: int
        :param consumer_byte_rate: 消费上限速率（单位为B/s）
        :type consumer_byte_rate: int
        """
        
        

        self._user = None
        self._client = None
        self._user_default = None
        self._client_default = None
        self._producer_byte_rate = None
        self._consumer_byte_rate = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if client is not None:
            self.client = client
        if user_default is not None:
            self.user_default = user_default
        if client_default is not None:
            self.client_default = client_default
        if producer_byte_rate is not None:
            self.producer_byte_rate = producer_byte_rate
        if consumer_byte_rate is not None:
            self.consumer_byte_rate = consumer_byte_rate

    @property
    def user(self):
        """Gets the user of this CreateKafkaUserClientQuotaTaskReq.

        用户名

        :return: The user of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CreateKafkaUserClientQuotaTaskReq.

        用户名

        :param user: The user of this CreateKafkaUserClientQuotaTaskReq.
        :type user: str
        """
        self._user = user

    @property
    def client(self):
        """Gets the client of this CreateKafkaUserClientQuotaTaskReq.

        客户端ID

        :return: The client of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this CreateKafkaUserClientQuotaTaskReq.

        客户端ID

        :param client: The client of this CreateKafkaUserClientQuotaTaskReq.
        :type client: str
        """
        self._client = client

    @property
    def user_default(self):
        """Gets the user_default of this CreateKafkaUserClientQuotaTaskReq.

        是否使用用户默认设置（是则表示对全部用户限流）。

        :return: The user_default of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: bool
        """
        return self._user_default

    @user_default.setter
    def user_default(self, user_default):
        """Sets the user_default of this CreateKafkaUserClientQuotaTaskReq.

        是否使用用户默认设置（是则表示对全部用户限流）。

        :param user_default: The user_default of this CreateKafkaUserClientQuotaTaskReq.
        :type user_default: bool
        """
        self._user_default = user_default

    @property
    def client_default(self):
        """Gets the client_default of this CreateKafkaUserClientQuotaTaskReq.

        是否使用客户端默认设置（是则表示对全部客户端限流）。

        :return: The client_default of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: bool
        """
        return self._client_default

    @client_default.setter
    def client_default(self, client_default):
        """Sets the client_default of this CreateKafkaUserClientQuotaTaskReq.

        是否使用客户端默认设置（是则表示对全部客户端限流）。

        :param client_default: The client_default of this CreateKafkaUserClientQuotaTaskReq.
        :type client_default: bool
        """
        self._client_default = client_default

    @property
    def producer_byte_rate(self):
        """Gets the producer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.

        生产上限速率（单位为B/s）

        :return: The producer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: int
        """
        return self._producer_byte_rate

    @producer_byte_rate.setter
    def producer_byte_rate(self, producer_byte_rate):
        """Sets the producer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.

        生产上限速率（单位为B/s）

        :param producer_byte_rate: The producer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.
        :type producer_byte_rate: int
        """
        self._producer_byte_rate = producer_byte_rate

    @property
    def consumer_byte_rate(self):
        """Gets the consumer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.

        消费上限速率（单位为B/s）

        :return: The consumer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.
        :rtype: int
        """
        return self._consumer_byte_rate

    @consumer_byte_rate.setter
    def consumer_byte_rate(self, consumer_byte_rate):
        """Sets the consumer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.

        消费上限速率（单位为B/s）

        :param consumer_byte_rate: The consumer_byte_rate of this CreateKafkaUserClientQuotaTaskReq.
        :type consumer_byte_rate: int
        """
        self._consumer_byte_rate = consumer_byte_rate

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
        if not isinstance(other, CreateKafkaUserClientQuotaTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
