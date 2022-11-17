# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMqsInstanceMessagesRequest:

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
        'asc': 'bool',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'str',
        'offset': 'str',
        'download': 'bool',
        'message_offset': 'str',
        'partition': 'str',
        'key': 'str',
        'message_id': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'asc': 'asc',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'download': 'download',
        'message_offset': 'message_offset',
        'partition': 'partition',
        'key': 'key',
        'message_id': 'message_id',
        'tag': 'tag'
    }

    def __init__(self, instance_id=None, topic=None, asc=None, start_time=None, end_time=None, limit=None, offset=None, download=None, message_offset=None, partition=None, key=None, message_id=None, tag=None):
        """ShowMqsInstanceMessagesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: topic名称。
        :type topic: str
        :param asc: 是否按照时间排序。
        :type asc: bool
        :param start_time: 开始时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。
        :type start_time: str
        :param end_time: 结束时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。
        :type end_time: str
        :param limit: 查询消息的数量。
        :type limit: str
        :param offset: 查询的偏移量。
        :type offset: str
        :param download: 是否下载。
        :type download: bool
        :param message_offset: 消息偏移量。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。
        :type message_offset: str
        :param partition: 分区。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。
        :type partition: str
        :param key: 消息key。
        :type key: str
        :param message_id: 消息ID。
        :type message_id: str
        :param tag: 消息标签。
        :type tag: str
        """
        
        

        self._instance_id = None
        self._topic = None
        self._asc = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._download = None
        self._message_offset = None
        self._partition = None
        self._key = None
        self._message_id = None
        self._tag = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if asc is not None:
            self.asc = asc
        self.start_time = start_time
        self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if download is not None:
            self.download = download
        if message_offset is not None:
            self.message_offset = message_offset
        if partition is not None:
            self.partition = partition
        if key is not None:
            self.key = key
        if message_id is not None:
            self.message_id = message_id
        if tag is not None:
            self.tag = tag

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowMqsInstanceMessagesRequest.

        实例ID。

        :return: The instance_id of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowMqsInstanceMessagesRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowMqsInstanceMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this ShowMqsInstanceMessagesRequest.

        topic名称。

        :return: The topic of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowMqsInstanceMessagesRequest.

        topic名称。

        :param topic: The topic of this ShowMqsInstanceMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def asc(self):
        """Gets the asc of this ShowMqsInstanceMessagesRequest.

        是否按照时间排序。

        :return: The asc of this ShowMqsInstanceMessagesRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this ShowMqsInstanceMessagesRequest.

        是否按照时间排序。

        :param asc: The asc of this ShowMqsInstanceMessagesRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def start_time(self):
        """Gets the start_time of this ShowMqsInstanceMessagesRequest.

        开始时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。

        :return: The start_time of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowMqsInstanceMessagesRequest.

        开始时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。

        :param start_time: The start_time of this ShowMqsInstanceMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowMqsInstanceMessagesRequest.

        结束时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。

        :return: The end_time of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowMqsInstanceMessagesRequest.

        结束时间。Unix毫秒时间戳。 查询消息偏移量时，为必选参数。

        :param end_time: The end_time of this ShowMqsInstanceMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ShowMqsInstanceMessagesRequest.

        查询消息的数量。

        :return: The limit of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMqsInstanceMessagesRequest.

        查询消息的数量。

        :param limit: The limit of this ShowMqsInstanceMessagesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowMqsInstanceMessagesRequest.

        查询的偏移量。

        :return: The offset of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMqsInstanceMessagesRequest.

        查询的偏移量。

        :param offset: The offset of this ShowMqsInstanceMessagesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def download(self):
        """Gets the download of this ShowMqsInstanceMessagesRequest.

        是否下载。

        :return: The download of this ShowMqsInstanceMessagesRequest.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this ShowMqsInstanceMessagesRequest.

        是否下载。

        :param download: The download of this ShowMqsInstanceMessagesRequest.
        :type download: bool
        """
        self._download = download

    @property
    def message_offset(self):
        """Gets the message_offset of this ShowMqsInstanceMessagesRequest.

        消息偏移量。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。

        :return: The message_offset of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        """Sets the message_offset of this ShowMqsInstanceMessagesRequest.

        消息偏移量。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。

        :param message_offset: The message_offset of this ShowMqsInstanceMessagesRequest.
        :type message_offset: str
        """
        self._message_offset = message_offset

    @property
    def partition(self):
        """Gets the partition of this ShowMqsInstanceMessagesRequest.

        分区。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。

        :return: The partition of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowMqsInstanceMessagesRequest.

        分区。 查询消息内容时，为必选参数。 若start_time、end_time参数不为空，该参数无效。

        :param partition: The partition of this ShowMqsInstanceMessagesRequest.
        :type partition: str
        """
        self._partition = partition

    @property
    def key(self):
        """Gets the key of this ShowMqsInstanceMessagesRequest.

        消息key。

        :return: The key of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ShowMqsInstanceMessagesRequest.

        消息key。

        :param key: The key of this ShowMqsInstanceMessagesRequest.
        :type key: str
        """
        self._key = key

    @property
    def message_id(self):
        """Gets the message_id of this ShowMqsInstanceMessagesRequest.

        消息ID。

        :return: The message_id of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ShowMqsInstanceMessagesRequest.

        消息ID。

        :param message_id: The message_id of this ShowMqsInstanceMessagesRequest.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def tag(self):
        """Gets the tag of this ShowMqsInstanceMessagesRequest.

        消息标签。

        :return: The tag of this ShowMqsInstanceMessagesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ShowMqsInstanceMessagesRequest.

        消息标签。

        :param tag: The tag of this ShowMqsInstanceMessagesRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ShowMqsInstanceMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
