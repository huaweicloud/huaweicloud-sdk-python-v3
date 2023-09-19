# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConsumerGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'broadcast': 'bool',
        'brokers': 'list[str]',
        'name': 'str',
        'retry_max_time': 'float',
        'from_beginning': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'broadcast': 'broadcast',
        'brokers': 'brokers',
        'name': 'name',
        'retry_max_time': 'retry_max_time',
        'from_beginning': 'from_beginning'
    }

    def __init__(self, enabled=None, broadcast=None, brokers=None, name=None, retry_max_time=None, from_beginning=None):
        """UpdateConsumerGroup

        The model defined in huaweicloud sdk

        :param enabled: 是否可以消费。
        :type enabled: bool
        :param broadcast: 是否广播。
        :type broadcast: bool
        :param brokers: 关联的代理列表。
        :type brokers: list[str]
        :param name: 消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。
        :type name: str
        :param retry_max_time: 最大重试次数。
        :type retry_max_time: float
        :param from_beginning: 是否重头消费。
        :type from_beginning: bool
        """
        
        

        self._enabled = None
        self._broadcast = None
        self._brokers = None
        self._name = None
        self._retry_max_time = None
        self._from_beginning = None
        self.discriminator = None

        self.enabled = enabled
        self.broadcast = broadcast
        if brokers is not None:
            self.brokers = brokers
        if name is not None:
            self.name = name
        self.retry_max_time = retry_max_time
        if from_beginning is not None:
            self.from_beginning = from_beginning

    @property
    def enabled(self):
        """Gets the enabled of this UpdateConsumerGroup.

        是否可以消费。

        :return: The enabled of this UpdateConsumerGroup.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateConsumerGroup.

        是否可以消费。

        :param enabled: The enabled of this UpdateConsumerGroup.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def broadcast(self):
        """Gets the broadcast of this UpdateConsumerGroup.

        是否广播。

        :return: The broadcast of this UpdateConsumerGroup.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this UpdateConsumerGroup.

        是否广播。

        :param broadcast: The broadcast of this UpdateConsumerGroup.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def brokers(self):
        """Gets the brokers of this UpdateConsumerGroup.

        关联的代理列表。

        :return: The brokers of this UpdateConsumerGroup.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this UpdateConsumerGroup.

        关联的代理列表。

        :param brokers: The brokers of this UpdateConsumerGroup.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def name(self):
        """Gets the name of this UpdateConsumerGroup.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :return: The name of this UpdateConsumerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateConsumerGroup.

        消费组名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :param name: The name of this UpdateConsumerGroup.
        :type name: str
        """
        self._name = name

    @property
    def retry_max_time(self):
        """Gets the retry_max_time of this UpdateConsumerGroup.

        最大重试次数。

        :return: The retry_max_time of this UpdateConsumerGroup.
        :rtype: float
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        """Sets the retry_max_time of this UpdateConsumerGroup.

        最大重试次数。

        :param retry_max_time: The retry_max_time of this UpdateConsumerGroup.
        :type retry_max_time: float
        """
        self._retry_max_time = retry_max_time

    @property
    def from_beginning(self):
        """Gets the from_beginning of this UpdateConsumerGroup.

        是否重头消费。

        :return: The from_beginning of this UpdateConsumerGroup.
        :rtype: bool
        """
        return self._from_beginning

    @from_beginning.setter
    def from_beginning(self, from_beginning):
        """Sets the from_beginning of this UpdateConsumerGroup.

        是否重头消费。

        :param from_beginning: The from_beginning of this UpdateConsumerGroup.
        :type from_beginning: bool
        """
        self._from_beginning = from_beginning

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
        if not isinstance(other, UpdateConsumerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
