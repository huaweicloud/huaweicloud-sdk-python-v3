# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskusageEntity:

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
        'topic_list': 'list[DiskusageTopicEntity]'
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
        r"""DiskusageEntity

        The model defined in huaweicloud sdk

        :param broker_name: Broker名称。
        :type broker_name: str
        :param data_disk_size: 磁盘容量。
        :type data_disk_size: str
        :param data_disk_use: 已使用的磁盘容量。
        :type data_disk_use: str
        :param data_disk_free: 剩余可用的磁盘容量。
        :type data_disk_free: str
        :param data_disk_use_percentage: 消息标签。
        :type data_disk_use_percentage: str
        :param status: 消息标签。
        :type status: str
        :param topic_list: Topic磁盘容量使用列表。
        :type topic_list: list[:class:`huaweicloudsdkkafka.v2.DiskusageTopicEntity`]
        """
        
        

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
        r"""Gets the broker_name of this DiskusageEntity.

        Broker名称。

        :return: The broker_name of this DiskusageEntity.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        r"""Sets the broker_name of this DiskusageEntity.

        Broker名称。

        :param broker_name: The broker_name of this DiskusageEntity.
        :type broker_name: str
        """
        self._broker_name = broker_name

    @property
    def data_disk_size(self):
        r"""Gets the data_disk_size of this DiskusageEntity.

        磁盘容量。

        :return: The data_disk_size of this DiskusageEntity.
        :rtype: str
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        r"""Sets the data_disk_size of this DiskusageEntity.

        磁盘容量。

        :param data_disk_size: The data_disk_size of this DiskusageEntity.
        :type data_disk_size: str
        """
        self._data_disk_size = data_disk_size

    @property
    def data_disk_use(self):
        r"""Gets the data_disk_use of this DiskusageEntity.

        已使用的磁盘容量。

        :return: The data_disk_use of this DiskusageEntity.
        :rtype: str
        """
        return self._data_disk_use

    @data_disk_use.setter
    def data_disk_use(self, data_disk_use):
        r"""Sets the data_disk_use of this DiskusageEntity.

        已使用的磁盘容量。

        :param data_disk_use: The data_disk_use of this DiskusageEntity.
        :type data_disk_use: str
        """
        self._data_disk_use = data_disk_use

    @property
    def data_disk_free(self):
        r"""Gets the data_disk_free of this DiskusageEntity.

        剩余可用的磁盘容量。

        :return: The data_disk_free of this DiskusageEntity.
        :rtype: str
        """
        return self._data_disk_free

    @data_disk_free.setter
    def data_disk_free(self, data_disk_free):
        r"""Sets the data_disk_free of this DiskusageEntity.

        剩余可用的磁盘容量。

        :param data_disk_free: The data_disk_free of this DiskusageEntity.
        :type data_disk_free: str
        """
        self._data_disk_free = data_disk_free

    @property
    def data_disk_use_percentage(self):
        r"""Gets the data_disk_use_percentage of this DiskusageEntity.

        消息标签。

        :return: The data_disk_use_percentage of this DiskusageEntity.
        :rtype: str
        """
        return self._data_disk_use_percentage

    @data_disk_use_percentage.setter
    def data_disk_use_percentage(self, data_disk_use_percentage):
        r"""Sets the data_disk_use_percentage of this DiskusageEntity.

        消息标签。

        :param data_disk_use_percentage: The data_disk_use_percentage of this DiskusageEntity.
        :type data_disk_use_percentage: str
        """
        self._data_disk_use_percentage = data_disk_use_percentage

    @property
    def status(self):
        r"""Gets the status of this DiskusageEntity.

        消息标签。

        :return: The status of this DiskusageEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DiskusageEntity.

        消息标签。

        :param status: The status of this DiskusageEntity.
        :type status: str
        """
        self._status = status

    @property
    def topic_list(self):
        r"""Gets the topic_list of this DiskusageEntity.

        Topic磁盘容量使用列表。

        :return: The topic_list of this DiskusageEntity.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.DiskusageTopicEntity`]
        """
        return self._topic_list

    @topic_list.setter
    def topic_list(self, topic_list):
        r"""Sets the topic_list of this DiskusageEntity.

        Topic磁盘容量使用列表。

        :param topic_list: The topic_list of this DiskusageEntity.
        :type topic_list: list[:class:`huaweicloudsdkkafka.v2.DiskusageTopicEntity`]
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
        if not isinstance(other, DiskusageEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
