# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMessagesRequest:

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
        'partition': 'str'
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
        'partition': 'partition'
    }

    def __init__(self, instance_id=None, topic=None, asc=None, start_time=None, end_time=None, limit=None, offset=None, download=None, message_offset=None, partition=None):
        """ShowInstanceMessagesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param topic: Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。
        :type topic: str
        :param asc: 是否按照时间排序。
        :type asc: bool
        :param start_time: 开始时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。
        :type start_time: str
        :param end_time: 结束时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。
        :type end_time: str
        :param limit: 分页大小。取值范围为0~50。
        :type limit: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: str
        :param download: 是否下载。
        :type download: bool
        :param message_offset: 消息偏移量。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。
        :type message_offset: str
        :param partition: 分区。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。
        :type partition: str
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
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if asc is not None:
            self.asc = asc
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
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

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceMessagesRequest.

        实例ID。

        :return: The instance_id of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceMessagesRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceMessagesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this ShowInstanceMessagesRequest.

        Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :return: The topic of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowInstanceMessagesRequest.

        Topic名称。  Topic名称必现以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :param topic: The topic of this ShowInstanceMessagesRequest.
        :type topic: str
        """
        self._topic = topic

    @property
    def asc(self):
        """Gets the asc of this ShowInstanceMessagesRequest.

        是否按照时间排序。

        :return: The asc of this ShowInstanceMessagesRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this ShowInstanceMessagesRequest.

        是否按照时间排序。

        :param asc: The asc of this ShowInstanceMessagesRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def start_time(self):
        """Gets the start_time of this ShowInstanceMessagesRequest.

        开始时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。

        :return: The start_time of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowInstanceMessagesRequest.

        开始时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。

        :param start_time: The start_time of this ShowInstanceMessagesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowInstanceMessagesRequest.

        结束时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。

        :return: The end_time of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowInstanceMessagesRequest.

        结束时间。  Unix毫秒时间戳。  查询消息偏移量时，为必选参数。

        :param end_time: The end_time of this ShowInstanceMessagesRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ShowInstanceMessagesRequest.

        分页大小。取值范围为0~50。

        :return: The limit of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowInstanceMessagesRequest.

        分页大小。取值范围为0~50。

        :param limit: The limit of this ShowInstanceMessagesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowInstanceMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowInstanceMessagesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ShowInstanceMessagesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def download(self):
        """Gets the download of this ShowInstanceMessagesRequest.

        是否下载。

        :return: The download of this ShowInstanceMessagesRequest.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this ShowInstanceMessagesRequest.

        是否下载。

        :param download: The download of this ShowInstanceMessagesRequest.
        :type download: bool
        """
        self._download = download

    @property
    def message_offset(self):
        """Gets the message_offset of this ShowInstanceMessagesRequest.

        消息偏移量。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。

        :return: The message_offset of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        """Sets the message_offset of this ShowInstanceMessagesRequest.

        消息偏移量。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。

        :param message_offset: The message_offset of this ShowInstanceMessagesRequest.
        :type message_offset: str
        """
        self._message_offset = message_offset

    @property
    def partition(self):
        """Gets the partition of this ShowInstanceMessagesRequest.

        分区。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。

        :return: The partition of this ShowInstanceMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowInstanceMessagesRequest.

        分区。  **查询消息内容时，为必选参数。**  若start_time、end_time参数不为空，该参数无效。

        :param partition: The partition of this ShowInstanceMessagesRequest.
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
        if not isinstance(other, ShowInstanceMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
