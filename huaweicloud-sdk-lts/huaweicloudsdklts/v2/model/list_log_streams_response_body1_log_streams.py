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
        'log_stream_name_alias': 'str',
        'tag': 'dict(str, str)',
        'filter_count': 'int',
        'whether_log_storage': 'bool',
        'hot_cold_separation': 'bool',
        'auth_web_tracking': 'bool',
        'ttl_in_days': 'int',
        'hot_storage_days': 'int',
        'log_group_id': 'str'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_stream_name_alias': 'log_stream_name_alias',
        'tag': 'tag',
        'filter_count': 'filter_count',
        'whether_log_storage': 'whether_log_storage',
        'hot_cold_separation': 'hot_cold_separation',
        'auth_web_tracking': 'auth_web_tracking',
        'ttl_in_days': 'ttl_in_days',
        'hot_storage_days': 'hot_storage_days',
        'log_group_id': 'log_group_id'
    }

    def __init__(self, creation_time=None, log_stream_id=None, log_stream_name=None, log_stream_name_alias=None, tag=None, filter_count=None, whether_log_storage=None, hot_cold_separation=None, auth_web_tracking=None, ttl_in_days=None, hot_storage_days=None, log_group_id=None):
        r"""ListLogStreamsResponseBody1LogStreams

        The model defined in huaweicloud sdk

        :param creation_time: 日志流创建时间
        :type creation_time: int
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param log_stream_name_alias: 日志流别名
        :type log_stream_name_alias: str
        :param tag: 日志流所属标签
        :type tag: dict(str, str)
        :param filter_count: 过滤器个数
        :type filter_count: int
        :param whether_log_storage: 是否日志存储
        :type whether_log_storage: bool
        :param hot_cold_separation: 是否冷存储
        :type hot_cold_separation: bool
        :param auth_web_tracking: 匿名写入开关
        :type auth_web_tracking: bool
        :param ttl_in_days: 存储时间
        :type ttl_in_days: int
        :param hot_storage_days: 标准存储时间
        :type hot_storage_days: int
        :param log_group_id: 日志组ID
        :type log_group_id: str
        """
        
        

        self._creation_time = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._log_stream_name_alias = None
        self._tag = None
        self._filter_count = None
        self._whether_log_storage = None
        self._hot_cold_separation = None
        self._auth_web_tracking = None
        self._ttl_in_days = None
        self._hot_storage_days = None
        self._log_group_id = None
        self.discriminator = None

        self.creation_time = creation_time
        self.log_stream_id = log_stream_id
        self.log_stream_name = log_stream_name
        if log_stream_name_alias is not None:
            self.log_stream_name_alias = log_stream_name_alias
        self.tag = tag
        self.filter_count = filter_count
        if whether_log_storage is not None:
            self.whether_log_storage = whether_log_storage
        if hot_cold_separation is not None:
            self.hot_cold_separation = hot_cold_separation
        if auth_web_tracking is not None:
            self.auth_web_tracking = auth_web_tracking
        if ttl_in_days is not None:
            self.ttl_in_days = ttl_in_days
        if hot_storage_days is not None:
            self.hot_storage_days = hot_storage_days
        if log_group_id is not None:
            self.log_group_id = log_group_id

    @property
    def creation_time(self):
        r"""Gets the creation_time of this ListLogStreamsResponseBody1LogStreams.

        日志流创建时间

        :return: The creation_time of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this ListLogStreamsResponseBody1LogStreams.

        日志流创建时间

        :param creation_time: The creation_time of this ListLogStreamsResponseBody1LogStreams.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this ListLogStreamsResponseBody1LogStreams.

        日志流ID

        :return: The log_stream_id of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this ListLogStreamsResponseBody1LogStreams.

        日志流ID

        :param log_stream_id: The log_stream_id of this ListLogStreamsResponseBody1LogStreams.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this ListLogStreamsResponseBody1LogStreams.

        日志流名称

        :return: The log_stream_name of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this ListLogStreamsResponseBody1LogStreams.

        日志流名称

        :param log_stream_name: The log_stream_name of this ListLogStreamsResponseBody1LogStreams.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_stream_name_alias(self):
        r"""Gets the log_stream_name_alias of this ListLogStreamsResponseBody1LogStreams.

        日志流别名

        :return: The log_stream_name_alias of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_stream_name_alias

    @log_stream_name_alias.setter
    def log_stream_name_alias(self, log_stream_name_alias):
        r"""Sets the log_stream_name_alias of this ListLogStreamsResponseBody1LogStreams.

        日志流别名

        :param log_stream_name_alias: The log_stream_name_alias of this ListLogStreamsResponseBody1LogStreams.
        :type log_stream_name_alias: str
        """
        self._log_stream_name_alias = log_stream_name_alias

    @property
    def tag(self):
        r"""Gets the tag of this ListLogStreamsResponseBody1LogStreams.

        日志流所属标签

        :return: The tag of this ListLogStreamsResponseBody1LogStreams.
        :rtype: dict(str, str)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListLogStreamsResponseBody1LogStreams.

        日志流所属标签

        :param tag: The tag of this ListLogStreamsResponseBody1LogStreams.
        :type tag: dict(str, str)
        """
        self._tag = tag

    @property
    def filter_count(self):
        r"""Gets the filter_count of this ListLogStreamsResponseBody1LogStreams.

        过滤器个数

        :return: The filter_count of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._filter_count

    @filter_count.setter
    def filter_count(self, filter_count):
        r"""Sets the filter_count of this ListLogStreamsResponseBody1LogStreams.

        过滤器个数

        :param filter_count: The filter_count of this ListLogStreamsResponseBody1LogStreams.
        :type filter_count: int
        """
        self._filter_count = filter_count

    @property
    def whether_log_storage(self):
        r"""Gets the whether_log_storage of this ListLogStreamsResponseBody1LogStreams.

        是否日志存储

        :return: The whether_log_storage of this ListLogStreamsResponseBody1LogStreams.
        :rtype: bool
        """
        return self._whether_log_storage

    @whether_log_storage.setter
    def whether_log_storage(self, whether_log_storage):
        r"""Sets the whether_log_storage of this ListLogStreamsResponseBody1LogStreams.

        是否日志存储

        :param whether_log_storage: The whether_log_storage of this ListLogStreamsResponseBody1LogStreams.
        :type whether_log_storage: bool
        """
        self._whether_log_storage = whether_log_storage

    @property
    def hot_cold_separation(self):
        r"""Gets the hot_cold_separation of this ListLogStreamsResponseBody1LogStreams.

        是否冷存储

        :return: The hot_cold_separation of this ListLogStreamsResponseBody1LogStreams.
        :rtype: bool
        """
        return self._hot_cold_separation

    @hot_cold_separation.setter
    def hot_cold_separation(self, hot_cold_separation):
        r"""Sets the hot_cold_separation of this ListLogStreamsResponseBody1LogStreams.

        是否冷存储

        :param hot_cold_separation: The hot_cold_separation of this ListLogStreamsResponseBody1LogStreams.
        :type hot_cold_separation: bool
        """
        self._hot_cold_separation = hot_cold_separation

    @property
    def auth_web_tracking(self):
        r"""Gets the auth_web_tracking of this ListLogStreamsResponseBody1LogStreams.

        匿名写入开关

        :return: The auth_web_tracking of this ListLogStreamsResponseBody1LogStreams.
        :rtype: bool
        """
        return self._auth_web_tracking

    @auth_web_tracking.setter
    def auth_web_tracking(self, auth_web_tracking):
        r"""Sets the auth_web_tracking of this ListLogStreamsResponseBody1LogStreams.

        匿名写入开关

        :param auth_web_tracking: The auth_web_tracking of this ListLogStreamsResponseBody1LogStreams.
        :type auth_web_tracking: bool
        """
        self._auth_web_tracking = auth_web_tracking

    @property
    def ttl_in_days(self):
        r"""Gets the ttl_in_days of this ListLogStreamsResponseBody1LogStreams.

        存储时间

        :return: The ttl_in_days of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        r"""Sets the ttl_in_days of this ListLogStreamsResponseBody1LogStreams.

        存储时间

        :param ttl_in_days: The ttl_in_days of this ListLogStreamsResponseBody1LogStreams.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def hot_storage_days(self):
        r"""Gets the hot_storage_days of this ListLogStreamsResponseBody1LogStreams.

        标准存储时间

        :return: The hot_storage_days of this ListLogStreamsResponseBody1LogStreams.
        :rtype: int
        """
        return self._hot_storage_days

    @hot_storage_days.setter
    def hot_storage_days(self, hot_storage_days):
        r"""Sets the hot_storage_days of this ListLogStreamsResponseBody1LogStreams.

        标准存储时间

        :param hot_storage_days: The hot_storage_days of this ListLogStreamsResponseBody1LogStreams.
        :type hot_storage_days: int
        """
        self._hot_storage_days = hot_storage_days

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ListLogStreamsResponseBody1LogStreams.

        日志组ID

        :return: The log_group_id of this ListLogStreamsResponseBody1LogStreams.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ListLogStreamsResponseBody1LogStreams.

        日志组ID

        :param log_group_id: The log_group_id of this ListLogStreamsResponseBody1LogStreams.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

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
