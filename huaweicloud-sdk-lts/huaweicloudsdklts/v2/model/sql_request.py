# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_time_range_relative': 'bool',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'sql': 'str',
        'sql_request_title': 'str',
        'search_time_range': 'int',
        'search_time_range_unit': 'str'
    }

    attribute_map = {
        'is_time_range_relative': 'is_time_range_relative',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'sql': 'sql',
        'sql_request_title': 'sql_request_title',
        'search_time_range': 'search_time_range',
        'search_time_range_unit': 'search_time_range_unit'
    }

    def __init__(self, is_time_range_relative=None, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, sql=None, sql_request_title=None, search_time_range=None, search_time_range_unit=None):
        """SqlRequest

        The model defined in huaweicloud sdk

        :param is_time_range_relative: 是时间范围相对
        :type is_time_range_relative: bool
        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param sql: sql语句
        :type sql: str
        :param sql_request_title: 图表名称
        :type sql_request_title: str
        :param search_time_range: 查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)
        :type search_time_range: int
        :param search_time_range_unit: 查询时间单位
        :type search_time_range_unit: str
        """
        
        

        self._is_time_range_relative = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._sql = None
        self._sql_request_title = None
        self._search_time_range = None
        self._search_time_range_unit = None
        self.discriminator = None

        if is_time_range_relative is not None:
            self.is_time_range_relative = is_time_range_relative
        self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        self.sql = sql
        self.sql_request_title = sql_request_title
        self.search_time_range = search_time_range
        self.search_time_range_unit = search_time_range_unit

    @property
    def is_time_range_relative(self):
        """Gets the is_time_range_relative of this SqlRequest.

        是时间范围相对

        :return: The is_time_range_relative of this SqlRequest.
        :rtype: bool
        """
        return self._is_time_range_relative

    @is_time_range_relative.setter
    def is_time_range_relative(self, is_time_range_relative):
        """Sets the is_time_range_relative of this SqlRequest.

        是时间范围相对

        :param is_time_range_relative: The is_time_range_relative of this SqlRequest.
        :type is_time_range_relative: bool
        """
        self._is_time_range_relative = is_time_range_relative

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this SqlRequest.

        日志流id

        :return: The log_stream_id of this SqlRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this SqlRequest.

        日志流id

        :param log_stream_id: The log_stream_id of this SqlRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this SqlRequest.

        日志流名称

        :return: The log_stream_name of this SqlRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this SqlRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this SqlRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        """Gets the log_group_id of this SqlRequest.

        日志组id

        :return: The log_group_id of this SqlRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this SqlRequest.

        日志组id

        :param log_group_id: The log_group_id of this SqlRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this SqlRequest.

        日志组名称

        :return: The log_group_name of this SqlRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this SqlRequest.

        日志组名称

        :param log_group_name: The log_group_name of this SqlRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def sql(self):
        """Gets the sql of this SqlRequest.

        sql语句

        :return: The sql of this SqlRequest.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this SqlRequest.

        sql语句

        :param sql: The sql of this SqlRequest.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_request_title(self):
        """Gets the sql_request_title of this SqlRequest.

        图表名称

        :return: The sql_request_title of this SqlRequest.
        :rtype: str
        """
        return self._sql_request_title

    @sql_request_title.setter
    def sql_request_title(self, sql_request_title):
        """Sets the sql_request_title of this SqlRequest.

        图表名称

        :param sql_request_title: The sql_request_title of this SqlRequest.
        :type sql_request_title: str
        """
        self._sql_request_title = sql_request_title

    @property
    def search_time_range(self):
        """Gets the search_time_range of this SqlRequest.

        查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)

        :return: The search_time_range of this SqlRequest.
        :rtype: int
        """
        return self._search_time_range

    @search_time_range.setter
    def search_time_range(self, search_time_range):
        """Sets the search_time_range of this SqlRequest.

        查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)

        :param search_time_range: The search_time_range of this SqlRequest.
        :type search_time_range: int
        """
        self._search_time_range = search_time_range

    @property
    def search_time_range_unit(self):
        """Gets the search_time_range_unit of this SqlRequest.

        查询时间单位

        :return: The search_time_range_unit of this SqlRequest.
        :rtype: str
        """
        return self._search_time_range_unit

    @search_time_range_unit.setter
    def search_time_range_unit(self, search_time_range_unit):
        """Sets the search_time_range_unit of this SqlRequest.

        查询时间单位

        :param search_time_range_unit: The search_time_range_unit of this SqlRequest.
        :type search_time_range_unit: str
        """
        self._search_time_range_unit = search_time_range_unit

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
        if not isinstance(other, SqlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
