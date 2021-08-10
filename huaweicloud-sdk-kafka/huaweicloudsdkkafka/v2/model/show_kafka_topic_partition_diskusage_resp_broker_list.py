# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicPartitionDiskusageRespBrokerList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'broker_name': 'str',
        'data_disk_size': 'str',
        'data_disk_use': 'str',
        'data_disk_free': 'str',
        'data_disk_use_percentage': 'str',
        'status': 'str',
        'topic_list': 'list[ShowKafkaTopicPartitionDiskusageRespTopicList]'
    }

    attribute_map = {
        'broker_name': 'broker_name',
        'data_disk_size': 'data_disk_size',
        'data_disk_use': 'data_disk_use',
        'data_disk_free': 'data_disk_free',
        'data_disk_use_percentage': 'data_disk_use_percentage',
        'status': 'status',
        'topic_list': 'topic_list'
    }

    def __init__(self, broker_name=None, data_disk_size=None, data_disk_use=None, data_disk_free=None, data_disk_use_percentage=None, status=None, topic_list=None):
        """ShowKafkaTopicPartitionDiskusageRespBrokerList - a model defined in huaweicloud sdk"""
        
        

        self._broker_name = None
        self._data_disk_size = None
        self._data_disk_use = None
        self._data_disk_free = None
        self._data_disk_use_percentage = None
        self._status = None
        self._topic_list = None
        self.discriminator = None

        if broker_name is not None:
            self.broker_name = broker_name
        if data_disk_size is not None:
            self.data_disk_size = data_disk_size
        if data_disk_use is not None:
            self.data_disk_use = data_disk_use
        if data_disk_free is not None:
            self.data_disk_free = data_disk_free
        if data_disk_use_percentage is not None:
            self.data_disk_use_percentage = data_disk_use_percentage
        if status is not None:
            self.status = status
        if topic_list is not None:
            self.topic_list = topic_list

    @property
    def broker_name(self):
        """Gets the broker_name of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        Broker名称。

        :return: The broker_name of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        """Sets the broker_name of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        Broker名称。

        :param broker_name: The broker_name of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._broker_name = broker_name

    @property
    def data_disk_size(self):
        """Gets the data_disk_size of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        磁盘容量。

        :return: The data_disk_size of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        """Sets the data_disk_size of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        磁盘容量。

        :param data_disk_size: The data_disk_size of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._data_disk_size = data_disk_size

    @property
    def data_disk_use(self):
        """Gets the data_disk_use of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        已使用的磁盘容量。

        :return: The data_disk_use of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._data_disk_use

    @data_disk_use.setter
    def data_disk_use(self, data_disk_use):
        """Sets the data_disk_use of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        已使用的磁盘容量。

        :param data_disk_use: The data_disk_use of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._data_disk_use = data_disk_use

    @property
    def data_disk_free(self):
        """Gets the data_disk_free of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        剩余可用的磁盘容量。

        :return: The data_disk_free of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._data_disk_free

    @data_disk_free.setter
    def data_disk_free(self, data_disk_free):
        """Sets the data_disk_free of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        剩余可用的磁盘容量。

        :param data_disk_free: The data_disk_free of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._data_disk_free = data_disk_free

    @property
    def data_disk_use_percentage(self):
        """Gets the data_disk_use_percentage of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        消息标签。

        :return: The data_disk_use_percentage of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._data_disk_use_percentage

    @data_disk_use_percentage.setter
    def data_disk_use_percentage(self, data_disk_use_percentage):
        """Sets the data_disk_use_percentage of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        消息标签。

        :param data_disk_use_percentage: The data_disk_use_percentage of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._data_disk_use_percentage = data_disk_use_percentage

    @property
    def status(self):
        """Gets the status of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        消息标签。

        :return: The status of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        消息标签。

        :param status: The status of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: str
        """
        self._status = status

    @property
    def topic_list(self):
        """Gets the topic_list of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        topic磁盘容量使用列表。

        :return: The topic_list of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :rtype: list[ShowKafkaTopicPartitionDiskusageRespTopicList]
        """
        return self._topic_list

    @topic_list.setter
    def topic_list(self, topic_list):
        """Sets the topic_list of this ShowKafkaTopicPartitionDiskusageRespBrokerList.

        topic磁盘容量使用列表。

        :param topic_list: The topic_list of this ShowKafkaTopicPartitionDiskusageRespBrokerList.
        :type: list[ShowKafkaTopicPartitionDiskusageRespTopicList]
        """
        self._topic_list = topic_list

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
        if not isinstance(other, ShowKafkaTopicPartitionDiskusageRespBrokerList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
