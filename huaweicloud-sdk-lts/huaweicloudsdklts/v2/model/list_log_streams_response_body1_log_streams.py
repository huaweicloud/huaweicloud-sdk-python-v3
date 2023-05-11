# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogStreamsResponseBody1LogStreams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'int',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'tag': 'dict(str, str)',
        'filter_count': 'int'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'tag': 'tag',
        'filter_count': 'filter_count'
    }

    def __init__(self, creation_time=None, log_stream_id=None, log_stream_name=None, tag=None, filter_count=None):
        """ListLogStreamsResponseBody1LogStreams

        The model defined in huaweicloud sdk

        :param creation_time: 日志流创建时间
        :type creation_time: int
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param tag: 日志流所属标签
        :type tag: dict(str, str)
        :param filter_count: 过滤器个数
        :type filter_count: int
        """
        
        

        self._creation_time = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._tag = None
        self._filter_count = None
        self.discriminator = None

        self.creation_time = creation_time
        self.log_stream_id = log_stream_id
        self.log_stream_name = log_stream_name
        self.tag = tag
        self.filter_count = filter_count

    @property
    def creation_time(self):
        """Gets the creation_time of this ListLogStreamsResponseBody1LogStreams.

        日志流创建时间

        :return: The creation_time of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ListLogStreamsResponseBody1LogStreams.

        日志流创建时间

        :param creation_time: The creation_time of this ListLogStreamsResponseBody1LogStreams.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ListLogStreamsResponseBody1LogStreams.

        日志流ID

        :return: The log_stream_id of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ListLogStreamsResponseBody1LogStreams.

        日志流ID

        :param log_stream_id: The log_stream_id of this ListLogStreamsResponseBody1LogStreams.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this ListLogStreamsResponseBody1LogStreams.

        日志流名称

        :return: The log_stream_name of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this ListLogStreamsResponseBody1LogStreams.

        日志流名称

        :param log_stream_name: The log_stream_name of this ListLogStreamsResponseBody1LogStreams.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def tag(self):
        """Gets the tag of this ListLogStreamsResponseBody1LogStreams.

        日志流所属标签

        :return: The tag of this ListLogStreamsResponseBody1LogStreams.
        :rtype: dict(str, str)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListLogStreamsResponseBody1LogStreams.

        日志流所属标签

        :param tag: The tag of this ListLogStreamsResponseBody1LogStreams.
        :type tag: dict(str, str)
        """
        self._tag = tag

    @property
    def filter_count(self):
        """Gets the filter_count of this ListLogStreamsResponseBody1LogStreams.

        过滤器个数

        :return: The filter_count of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._filter_count

    @filter_count.setter
    def filter_count(self, filter_count):
        """Sets the filter_count of this ListLogStreamsResponseBody1LogStreams.

        过滤器个数

        :param filter_count: The filter_count of this ListLogStreamsResponseBody1LogStreams.
        :type filter_count: int
        """
        self._filter_count = filter_count

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
        if not isinstance(other, ListLogStreamsResponseBody1LogStreams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
