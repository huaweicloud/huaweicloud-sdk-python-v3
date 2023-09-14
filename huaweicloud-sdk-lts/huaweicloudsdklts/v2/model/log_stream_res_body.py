# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogStreamResBody:

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
        'filter_count': 'int',
        'is_favorite': 'bool'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'tag': 'tag',
        'filter_count': 'filter_count',
        'is_favorite': 'is_favorite'
    }

    def __init__(self, creation_time=None, log_stream_id=None, log_stream_name=None, tag=None, filter_count=None, is_favorite=None):
        """LogStreamResBody

        The model defined in huaweicloud sdk

        :param creation_time: 创建时间 最小值：1577808000000 最大值：4102416000000
        :type creation_time: int
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param tag: 日志流所属标签
        :type tag: dict(str, str)
        :param filter_count: 过滤器个数
        :type filter_count: int
        :param is_favorite: 是否收藏日志流。
        :type is_favorite: bool
        """
        
        

        self._creation_time = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._tag = None
        self._filter_count = None
        self._is_favorite = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if tag is not None:
            self.tag = tag
        if filter_count is not None:
            self.filter_count = filter_count
        if is_favorite is not None:
            self.is_favorite = is_favorite

    @property
    def creation_time(self):
        """Gets the creation_time of this LogStreamResBody.

        创建时间 最小值：1577808000000 最大值：4102416000000

        :return: The creation_time of this LogStreamResBody.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this LogStreamResBody.

        创建时间 最小值：1577808000000 最大值：4102416000000

        :param creation_time: The creation_time of this LogStreamResBody.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this LogStreamResBody.

        日志流ID

        :return: The log_stream_id of this LogStreamResBody.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this LogStreamResBody.

        日志流ID

        :param log_stream_id: The log_stream_id of this LogStreamResBody.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this LogStreamResBody.

        日志流名称

        :return: The log_stream_name of this LogStreamResBody.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this LogStreamResBody.

        日志流名称

        :param log_stream_name: The log_stream_name of this LogStreamResBody.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def tag(self):
        """Gets the tag of this LogStreamResBody.

        日志流所属标签

        :return: The tag of this LogStreamResBody.
        :rtype: dict(str, str)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this LogStreamResBody.

        日志流所属标签

        :param tag: The tag of this LogStreamResBody.
        :type tag: dict(str, str)
        """
        self._tag = tag

    @property
    def filter_count(self):
        """Gets the filter_count of this LogStreamResBody.

        过滤器个数

        :return: The filter_count of this LogStreamResBody.
        :rtype: int
        """
        return self._filter_count

    @filter_count.setter
    def filter_count(self, filter_count):
        """Sets the filter_count of this LogStreamResBody.

        过滤器个数

        :param filter_count: The filter_count of this LogStreamResBody.
        :type filter_count: int
        """
        self._filter_count = filter_count

    @property
    def is_favorite(self):
        """Gets the is_favorite of this LogStreamResBody.

        是否收藏日志流。

        :return: The is_favorite of this LogStreamResBody.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this LogStreamResBody.

        是否收藏日志流。

        :param is_favorite: The is_favorite of this LogStreamResBody.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

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
        if not isinstance(other, LogStreamResBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
