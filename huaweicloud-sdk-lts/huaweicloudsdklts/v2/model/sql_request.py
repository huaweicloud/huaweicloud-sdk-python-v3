# coding: utf-8

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
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'sql': 'str',
        'search_time_range': 'int',
        'search_time_range_unit': 'str',
        'custom_date': 'CustomDate',
        'is_time_range_relative': 'bool'
    }

    attribute_map = {
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'sql': 'sql',
        'search_time_range': 'search_time_range',
        'search_time_range_unit': 'search_time_range_unit',
        'custom_date': 'custom_date',
        'is_time_range_relative': 'is_time_range_relative'
    }

    def __init__(self, log_stream_id=None, log_stream_name=None, log_group_id=None, log_group_name=None, sql=None, search_time_range=None, search_time_range_unit=None, custom_date=None, is_time_range_relative=None):
        r"""SqlRequest

        The model defined in huaweicloud sdk

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
        :param search_time_range: 查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)
        :type search_time_range: int
        :param search_time_range_unit: 查询时间单位
        :type search_time_range_unit: str
        :param custom_date: 
        :type custom_date: :class:`huaweicloudsdklts.v2.CustomDate`
        :param is_time_range_relative: **参数解释：** 告警查询日志的时间区间为相对时间还是整点时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true: 相对时间。 - false: 整点时间。 **默认取值：** true
        :type is_time_range_relative: bool
        """
        
        

        self._log_stream_id = None
        self._log_stream_name = None
        self._log_group_id = None
        self._log_group_name = None
        self._sql = None
        self._search_time_range = None
        self._search_time_range_unit = None
        self._custom_date = None
        self._is_time_range_relative = None
        self.discriminator = None

        self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        self.sql = sql
        if search_time_range is not None:
            self.search_time_range = search_time_range
        if search_time_range_unit is not None:
            self.search_time_range_unit = search_time_range_unit
        if custom_date is not None:
            self.custom_date = custom_date
        if is_time_range_relative is not None:
            self.is_time_range_relative = is_time_range_relative

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this SqlRequest.

        日志流id

        :return: The log_stream_id of this SqlRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this SqlRequest.

        日志流id

        :param log_stream_id: The log_stream_id of this SqlRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this SqlRequest.

        日志流名称

        :return: The log_stream_name of this SqlRequest.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this SqlRequest.

        日志流名称

        :param log_stream_name: The log_stream_name of this SqlRequest.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this SqlRequest.

        日志组id

        :return: The log_group_id of this SqlRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this SqlRequest.

        日志组id

        :param log_group_id: The log_group_id of this SqlRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this SqlRequest.

        日志组名称

        :return: The log_group_name of this SqlRequest.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this SqlRequest.

        日志组名称

        :param log_group_name: The log_group_name of this SqlRequest.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def sql(self):
        r"""Gets the sql of this SqlRequest.

        sql语句

        :return: The sql of this SqlRequest.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SqlRequest.

        sql语句

        :param sql: The sql of this SqlRequest.
        :type sql: str
        """
        self._sql = sql

    @property
    def search_time_range(self):
        r"""Gets the search_time_range of this SqlRequest.

        查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)

        :return: The search_time_range of this SqlRequest.
        :rtype: int
        """
        return self._search_time_range

    @search_time_range.setter
    def search_time_range(self, search_time_range):
        r"""Sets the search_time_range of this SqlRequest.

        查询执行任务时最近数据的时间范围(当search_time_range_unit为minute，则最大值为60;当search_time_range_unit为hour，则最大值为24)

        :param search_time_range: The search_time_range of this SqlRequest.
        :type search_time_range: int
        """
        self._search_time_range = search_time_range

    @property
    def search_time_range_unit(self):
        r"""Gets the search_time_range_unit of this SqlRequest.

        查询时间单位

        :return: The search_time_range_unit of this SqlRequest.
        :rtype: str
        """
        return self._search_time_range_unit

    @search_time_range_unit.setter
    def search_time_range_unit(self, search_time_range_unit):
        r"""Sets the search_time_range_unit of this SqlRequest.

        查询时间单位

        :param search_time_range_unit: The search_time_range_unit of this SqlRequest.
        :type search_time_range_unit: str
        """
        self._search_time_range_unit = search_time_range_unit

    @property
    def custom_date(self):
        r"""Gets the custom_date of this SqlRequest.

        :return: The custom_date of this SqlRequest.
        :rtype: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        return self._custom_date

    @custom_date.setter
    def custom_date(self, custom_date):
        r"""Sets the custom_date of this SqlRequest.

        :param custom_date: The custom_date of this SqlRequest.
        :type custom_date: :class:`huaweicloudsdklts.v2.CustomDate`
        """
        self._custom_date = custom_date

    @property
    def is_time_range_relative(self):
        r"""Gets the is_time_range_relative of this SqlRequest.

        **参数解释：** 告警查询日志的时间区间为相对时间还是整点时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true: 相对时间。 - false: 整点时间。 **默认取值：** true

        :return: The is_time_range_relative of this SqlRequest.
        :rtype: bool
        """
        return self._is_time_range_relative

    @is_time_range_relative.setter
    def is_time_range_relative(self, is_time_range_relative):
        r"""Sets the is_time_range_relative of this SqlRequest.

        **参数解释：** 告警查询日志的时间区间为相对时间还是整点时间。（暂不开放，后续aom上线该功能后一起开放） **约束限制：** 不涉及。 **取值范围：** - true: 相对时间。 - false: 整点时间。 **默认取值：** true

        :param is_time_range_relative: The is_time_range_relative of this SqlRequest.
        :type is_time_range_relative: bool
        """
        self._is_time_range_relative = is_time_range_relative

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
