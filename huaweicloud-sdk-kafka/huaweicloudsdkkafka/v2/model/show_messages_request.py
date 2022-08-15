# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessagesRequest:

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
        'topic': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'partition': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'partition': 'partition'
    }

    def __init__(self, instance_id=None, topic=None, start_time=None, end_time=None, limit=None, offset=None, partition=None):
        """ShowMessagesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。
        :type topic: str
        :param start_time: 查询起始时间，为unix时间戳格式，默认值为0。
        :type start_time: str
        :param end_time: 查询结束时间，为unix时间戳格式，默认值为系统当前时间。
        :type end_time: str
        :param limit: 单页返回消息数，默认值为10。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        :param partition: 分区编号，默认值为-1，若传入值为-1，则查询所有分区。
        :type partition: str
        """
        
        

        self._instance_id = None
        self._topic = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._partition = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if partition is not None:
            self.partition = partition

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowMessagesRequest.

        实例ID。

        :return: The instance_id of this ShowMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowMessagesRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this ShowMessagesRequest.

        Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :return: The topic of this ShowMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowMessagesRequest.

        Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :param topic: The topic of this ShowMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def start_time(self):
        """Gets the start_time of this ShowMessagesRequest.

        查询起始时间，为unix时间戳格式，默认值为0。

        :return: The start_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowMessagesRequest.

        查询起始时间，为unix时间戳格式，默认值为0。

        :param start_time: The start_time of this ShowMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowMessagesRequest.

        查询结束时间，为unix时间戳格式，默认值为系统当前时间。

        :return: The end_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowMessagesRequest.

        查询结束时间，为unix时间戳格式，默认值为系统当前时间。

        :param end_time: The end_time of this ShowMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ShowMessagesRequest.

        单页返回消息数，默认值为10。

        :return: The limit of this ShowMessagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMessagesRequest.

        单页返回消息数，默认值为10。

        :param limit: The limit of this ShowMessagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ShowMessagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ShowMessagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def partition(self):
        """Gets the partition of this ShowMessagesRequest.

        分区编号，默认值为-1，若传入值为-1，则查询所有分区。

        :return: The partition of this ShowMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowMessagesRequest.

        分区编号，默认值为-1，若传入值为-1，则查询所有分区。

        :param partition: The partition of this ShowMessagesRequest.
        :type partition: str
        """
        self._partition = partition

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
        if not isinstance(other, ShowMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
