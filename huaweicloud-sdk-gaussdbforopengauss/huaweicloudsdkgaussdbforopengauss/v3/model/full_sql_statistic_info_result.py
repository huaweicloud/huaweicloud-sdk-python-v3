# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlStatisticInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'str',
        'sql_id': 'str',
        'sql_count': 'int',
        'total_sql_time': 'int',
        'avg_sql_time': 'int',
        'total_db_time': 'int',
        'total_cpu_time': 'int',
        'avg_parse_time': 'int',
        'avg_plan_time': 'int',
        'total_data_io_time': 'int',
        'avg_n_returned_rows': 'int',
        'avg_n_tuples_fetched': 'int',
        'avg_db_time': 'int',
        'avg_cpu_time': 'int',
        'avg_data_io_time': 'int',
        'avg_execution_time': 'int',
        'avg_n_blocks_hit': 'int',
        'start_time_stamp': 'int',
        'end_time_stamp': 'int'
    }

    attribute_map = {
        'template': 'template',
        'sql_id': 'sql_id',
        'sql_count': 'sql_count',
        'total_sql_time': 'total_sql_time',
        'avg_sql_time': 'avg_sql_time',
        'total_db_time': 'total_db_time',
        'total_cpu_time': 'total_cpu_time',
        'avg_parse_time': 'avg_parse_time',
        'avg_plan_time': 'avg_plan_time',
        'total_data_io_time': 'total_data_io_time',
        'avg_n_returned_rows': 'avg_n_returned_rows',
        'avg_n_tuples_fetched': 'avg_n_tuples_fetched',
        'avg_db_time': 'avg_db_time',
        'avg_cpu_time': 'avg_cpu_time',
        'avg_data_io_time': 'avg_data_io_time',
        'avg_execution_time': 'avg_execution_time',
        'avg_n_blocks_hit': 'avg_n_blocks_hit',
        'start_time_stamp': 'start_time_stamp',
        'end_time_stamp': 'end_time_stamp'
    }

    def __init__(self, template=None, sql_id=None, sql_count=None, total_sql_time=None, avg_sql_time=None, total_db_time=None, total_cpu_time=None, avg_parse_time=None, avg_plan_time=None, total_data_io_time=None, avg_n_returned_rows=None, avg_n_tuples_fetched=None, avg_db_time=None, avg_cpu_time=None, avg_data_io_time=None, avg_execution_time=None, avg_n_blocks_hit=None, start_time_stamp=None, end_time_stamp=None):
        r"""FullSqlStatisticInfoResult

        The model defined in huaweicloud sdk

        :param template: **参数解释**: SQL模板。未开启实例内核GUC参数（track_stmt_parameter）时，展示的是归一化SQL模板内容；开启该参数后，展示的是随机一条SQL记录中截断参数列表后的内容。 **取值范围**: 不涉及。
        :type template: str
        :param sql_id: **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param sql_count: **参数解释**: 汇总SQL条目数。 **取值范围**: 不涉及。
        :type sql_count: int
        :param total_sql_time: **参数解释**: 总SQL耗时（微秒）。 **取值范围**: 不涉及。
        :type total_sql_time: int
        :param avg_sql_time: **参数解释**: 平均SQL耗时（微秒）。 **取值范围**: 不涉及。
        :type avg_sql_time: int
        :param total_db_time: **参数解释**: 总有效DB耗时（微秒）。 **取值范围**: 不涉及。
        :type total_db_time: int
        :param total_cpu_time: **参数解释**: 总CPU耗时（微秒）。 **取值范围**: 不涉及。
        :type total_cpu_time: int
        :param avg_parse_time: **参数解释**: 平均解释器时间（微秒）。 **取值范围**: 不涉及。
        :type avg_parse_time: int
        :param avg_plan_time: **参数解释**: 平均执行计划时间（微秒）。 **取值范围**: 不涉及。
        :type avg_plan_time: int
        :param total_data_io_time: **参数解释**: 总IO耗时（微秒）。 **取值范围**: 不涉及。
        :type total_data_io_time: int
        :param avg_n_returned_rows: **参数解释**: 平均返回行数。 **取值范围**: 不涉及。
        :type avg_n_returned_rows: int
        :param avg_n_tuples_fetched: **参数解释**: 平均扫描行数。 **取值范围**: 不涉及。
        :type avg_n_tuples_fetched: int
        :param avg_db_time: **参数解释**: 平均有效DB耗时（微秒）。 **取值范围**: 不涉及。
        :type avg_db_time: int
        :param avg_cpu_time: **参数解释**: 平均CPU执行耗时（微秒）。 **取值范围**: 不涉及。
        :type avg_cpu_time: int
        :param avg_data_io_time: **参数解释**: 平均IO耗时（微秒）。 **取值范围**: 不涉及。
        :type avg_data_io_time: int
        :param avg_execution_time: **参数解释**: 平均SQL执行器内执行时间（微秒）。 **取值范围**: 不涉及。
        :type avg_execution_time: int
        :param avg_n_blocks_hit: **参数解释**: 平均Buffer块命中次数。 **取值范围**: 不涉及。
        :type avg_n_blocks_hit: int
        :param start_time_stamp: **参数解释**: 开始时间戳。 **取值范围**: 不涉及。
        :type start_time_stamp: int
        :param end_time_stamp: **参数解释**: 结束时间戳。 **取值范围**: 不涉及。
        :type end_time_stamp: int
        """
        
        

        self._template = None
        self._sql_id = None
        self._sql_count = None
        self._total_sql_time = None
        self._avg_sql_time = None
        self._total_db_time = None
        self._total_cpu_time = None
        self._avg_parse_time = None
        self._avg_plan_time = None
        self._total_data_io_time = None
        self._avg_n_returned_rows = None
        self._avg_n_tuples_fetched = None
        self._avg_db_time = None
        self._avg_cpu_time = None
        self._avg_data_io_time = None
        self._avg_execution_time = None
        self._avg_n_blocks_hit = None
        self._start_time_stamp = None
        self._end_time_stamp = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if sql_id is not None:
            self.sql_id = sql_id
        if sql_count is not None:
            self.sql_count = sql_count
        if total_sql_time is not None:
            self.total_sql_time = total_sql_time
        if avg_sql_time is not None:
            self.avg_sql_time = avg_sql_time
        if total_db_time is not None:
            self.total_db_time = total_db_time
        if total_cpu_time is not None:
            self.total_cpu_time = total_cpu_time
        if avg_parse_time is not None:
            self.avg_parse_time = avg_parse_time
        if avg_plan_time is not None:
            self.avg_plan_time = avg_plan_time
        if total_data_io_time is not None:
            self.total_data_io_time = total_data_io_time
        if avg_n_returned_rows is not None:
            self.avg_n_returned_rows = avg_n_returned_rows
        if avg_n_tuples_fetched is not None:
            self.avg_n_tuples_fetched = avg_n_tuples_fetched
        if avg_db_time is not None:
            self.avg_db_time = avg_db_time
        if avg_cpu_time is not None:
            self.avg_cpu_time = avg_cpu_time
        if avg_data_io_time is not None:
            self.avg_data_io_time = avg_data_io_time
        if avg_execution_time is not None:
            self.avg_execution_time = avg_execution_time
        if avg_n_blocks_hit is not None:
            self.avg_n_blocks_hit = avg_n_blocks_hit
        if start_time_stamp is not None:
            self.start_time_stamp = start_time_stamp
        if end_time_stamp is not None:
            self.end_time_stamp = end_time_stamp

    @property
    def template(self):
        r"""Gets the template of this FullSqlStatisticInfoResult.

        **参数解释**: SQL模板。未开启实例内核GUC参数（track_stmt_parameter）时，展示的是归一化SQL模板内容；开启该参数后，展示的是随机一条SQL记录中截断参数列表后的内容。 **取值范围**: 不涉及。

        :return: The template of this FullSqlStatisticInfoResult.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this FullSqlStatisticInfoResult.

        **参数解释**: SQL模板。未开启实例内核GUC参数（track_stmt_parameter）时，展示的是归一化SQL模板内容；开启该参数后，展示的是随机一条SQL记录中截断参数列表后的内容。 **取值范围**: 不涉及。

        :param template: The template of this FullSqlStatisticInfoResult.
        :type template: str
        """
        self._template = template

    @property
    def sql_id(self):
        r"""Gets the sql_id of this FullSqlStatisticInfoResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this FullSqlStatisticInfoResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this FullSqlStatisticInfoResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this FullSqlStatisticInfoResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_count(self):
        r"""Gets the sql_count of this FullSqlStatisticInfoResult.

        **参数解释**: 汇总SQL条目数。 **取值范围**: 不涉及。

        :return: The sql_count of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._sql_count

    @sql_count.setter
    def sql_count(self, sql_count):
        r"""Sets the sql_count of this FullSqlStatisticInfoResult.

        **参数解释**: 汇总SQL条目数。 **取值范围**: 不涉及。

        :param sql_count: The sql_count of this FullSqlStatisticInfoResult.
        :type sql_count: int
        """
        self._sql_count = sql_count

    @property
    def total_sql_time(self):
        r"""Gets the total_sql_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总SQL耗时（微秒）。 **取值范围**: 不涉及。

        :return: The total_sql_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._total_sql_time

    @total_sql_time.setter
    def total_sql_time(self, total_sql_time):
        r"""Sets the total_sql_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总SQL耗时（微秒）。 **取值范围**: 不涉及。

        :param total_sql_time: The total_sql_time of this FullSqlStatisticInfoResult.
        :type total_sql_time: int
        """
        self._total_sql_time = total_sql_time

    @property
    def avg_sql_time(self):
        r"""Gets the avg_sql_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均SQL耗时（微秒）。 **取值范围**: 不涉及。

        :return: The avg_sql_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_sql_time

    @avg_sql_time.setter
    def avg_sql_time(self, avg_sql_time):
        r"""Sets the avg_sql_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均SQL耗时（微秒）。 **取值范围**: 不涉及。

        :param avg_sql_time: The avg_sql_time of this FullSqlStatisticInfoResult.
        :type avg_sql_time: int
        """
        self._avg_sql_time = avg_sql_time

    @property
    def total_db_time(self):
        r"""Gets the total_db_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总有效DB耗时（微秒）。 **取值范围**: 不涉及。

        :return: The total_db_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._total_db_time

    @total_db_time.setter
    def total_db_time(self, total_db_time):
        r"""Sets the total_db_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总有效DB耗时（微秒）。 **取值范围**: 不涉及。

        :param total_db_time: The total_db_time of this FullSqlStatisticInfoResult.
        :type total_db_time: int
        """
        self._total_db_time = total_db_time

    @property
    def total_cpu_time(self):
        r"""Gets the total_cpu_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总CPU耗时（微秒）。 **取值范围**: 不涉及。

        :return: The total_cpu_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._total_cpu_time

    @total_cpu_time.setter
    def total_cpu_time(self, total_cpu_time):
        r"""Sets the total_cpu_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总CPU耗时（微秒）。 **取值范围**: 不涉及。

        :param total_cpu_time: The total_cpu_time of this FullSqlStatisticInfoResult.
        :type total_cpu_time: int
        """
        self._total_cpu_time = total_cpu_time

    @property
    def avg_parse_time(self):
        r"""Gets the avg_parse_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均解释器时间（微秒）。 **取值范围**: 不涉及。

        :return: The avg_parse_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_parse_time

    @avg_parse_time.setter
    def avg_parse_time(self, avg_parse_time):
        r"""Sets the avg_parse_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均解释器时间（微秒）。 **取值范围**: 不涉及。

        :param avg_parse_time: The avg_parse_time of this FullSqlStatisticInfoResult.
        :type avg_parse_time: int
        """
        self._avg_parse_time = avg_parse_time

    @property
    def avg_plan_time(self):
        r"""Gets the avg_plan_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均执行计划时间（微秒）。 **取值范围**: 不涉及。

        :return: The avg_plan_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_plan_time

    @avg_plan_time.setter
    def avg_plan_time(self, avg_plan_time):
        r"""Sets the avg_plan_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均执行计划时间（微秒）。 **取值范围**: 不涉及。

        :param avg_plan_time: The avg_plan_time of this FullSqlStatisticInfoResult.
        :type avg_plan_time: int
        """
        self._avg_plan_time = avg_plan_time

    @property
    def total_data_io_time(self):
        r"""Gets the total_data_io_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总IO耗时（微秒）。 **取值范围**: 不涉及。

        :return: The total_data_io_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._total_data_io_time

    @total_data_io_time.setter
    def total_data_io_time(self, total_data_io_time):
        r"""Sets the total_data_io_time of this FullSqlStatisticInfoResult.

        **参数解释**: 总IO耗时（微秒）。 **取值范围**: 不涉及。

        :param total_data_io_time: The total_data_io_time of this FullSqlStatisticInfoResult.
        :type total_data_io_time: int
        """
        self._total_data_io_time = total_data_io_time

    @property
    def avg_n_returned_rows(self):
        r"""Gets the avg_n_returned_rows of this FullSqlStatisticInfoResult.

        **参数解释**: 平均返回行数。 **取值范围**: 不涉及。

        :return: The avg_n_returned_rows of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_n_returned_rows

    @avg_n_returned_rows.setter
    def avg_n_returned_rows(self, avg_n_returned_rows):
        r"""Sets the avg_n_returned_rows of this FullSqlStatisticInfoResult.

        **参数解释**: 平均返回行数。 **取值范围**: 不涉及。

        :param avg_n_returned_rows: The avg_n_returned_rows of this FullSqlStatisticInfoResult.
        :type avg_n_returned_rows: int
        """
        self._avg_n_returned_rows = avg_n_returned_rows

    @property
    def avg_n_tuples_fetched(self):
        r"""Gets the avg_n_tuples_fetched of this FullSqlStatisticInfoResult.

        **参数解释**: 平均扫描行数。 **取值范围**: 不涉及。

        :return: The avg_n_tuples_fetched of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_n_tuples_fetched

    @avg_n_tuples_fetched.setter
    def avg_n_tuples_fetched(self, avg_n_tuples_fetched):
        r"""Sets the avg_n_tuples_fetched of this FullSqlStatisticInfoResult.

        **参数解释**: 平均扫描行数。 **取值范围**: 不涉及。

        :param avg_n_tuples_fetched: The avg_n_tuples_fetched of this FullSqlStatisticInfoResult.
        :type avg_n_tuples_fetched: int
        """
        self._avg_n_tuples_fetched = avg_n_tuples_fetched

    @property
    def avg_db_time(self):
        r"""Gets the avg_db_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均有效DB耗时（微秒）。 **取值范围**: 不涉及。

        :return: The avg_db_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_db_time

    @avg_db_time.setter
    def avg_db_time(self, avg_db_time):
        r"""Sets the avg_db_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均有效DB耗时（微秒）。 **取值范围**: 不涉及。

        :param avg_db_time: The avg_db_time of this FullSqlStatisticInfoResult.
        :type avg_db_time: int
        """
        self._avg_db_time = avg_db_time

    @property
    def avg_cpu_time(self):
        r"""Gets the avg_cpu_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均CPU执行耗时（微秒）。 **取值范围**: 不涉及。

        :return: The avg_cpu_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_cpu_time

    @avg_cpu_time.setter
    def avg_cpu_time(self, avg_cpu_time):
        r"""Sets the avg_cpu_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均CPU执行耗时（微秒）。 **取值范围**: 不涉及。

        :param avg_cpu_time: The avg_cpu_time of this FullSqlStatisticInfoResult.
        :type avg_cpu_time: int
        """
        self._avg_cpu_time = avg_cpu_time

    @property
    def avg_data_io_time(self):
        r"""Gets the avg_data_io_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均IO耗时（微秒）。 **取值范围**: 不涉及。

        :return: The avg_data_io_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_data_io_time

    @avg_data_io_time.setter
    def avg_data_io_time(self, avg_data_io_time):
        r"""Sets the avg_data_io_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均IO耗时（微秒）。 **取值范围**: 不涉及。

        :param avg_data_io_time: The avg_data_io_time of this FullSqlStatisticInfoResult.
        :type avg_data_io_time: int
        """
        self._avg_data_io_time = avg_data_io_time

    @property
    def avg_execution_time(self):
        r"""Gets the avg_execution_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均SQL执行器内执行时间（微秒）。 **取值范围**: 不涉及。

        :return: The avg_execution_time of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_execution_time

    @avg_execution_time.setter
    def avg_execution_time(self, avg_execution_time):
        r"""Sets the avg_execution_time of this FullSqlStatisticInfoResult.

        **参数解释**: 平均SQL执行器内执行时间（微秒）。 **取值范围**: 不涉及。

        :param avg_execution_time: The avg_execution_time of this FullSqlStatisticInfoResult.
        :type avg_execution_time: int
        """
        self._avg_execution_time = avg_execution_time

    @property
    def avg_n_blocks_hit(self):
        r"""Gets the avg_n_blocks_hit of this FullSqlStatisticInfoResult.

        **参数解释**: 平均Buffer块命中次数。 **取值范围**: 不涉及。

        :return: The avg_n_blocks_hit of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._avg_n_blocks_hit

    @avg_n_blocks_hit.setter
    def avg_n_blocks_hit(self, avg_n_blocks_hit):
        r"""Sets the avg_n_blocks_hit of this FullSqlStatisticInfoResult.

        **参数解释**: 平均Buffer块命中次数。 **取值范围**: 不涉及。

        :param avg_n_blocks_hit: The avg_n_blocks_hit of this FullSqlStatisticInfoResult.
        :type avg_n_blocks_hit: int
        """
        self._avg_n_blocks_hit = avg_n_blocks_hit

    @property
    def start_time_stamp(self):
        r"""Gets the start_time_stamp of this FullSqlStatisticInfoResult.

        **参数解释**: 开始时间戳。 **取值范围**: 不涉及。

        :return: The start_time_stamp of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._start_time_stamp

    @start_time_stamp.setter
    def start_time_stamp(self, start_time_stamp):
        r"""Sets the start_time_stamp of this FullSqlStatisticInfoResult.

        **参数解释**: 开始时间戳。 **取值范围**: 不涉及。

        :param start_time_stamp: The start_time_stamp of this FullSqlStatisticInfoResult.
        :type start_time_stamp: int
        """
        self._start_time_stamp = start_time_stamp

    @property
    def end_time_stamp(self):
        r"""Gets the end_time_stamp of this FullSqlStatisticInfoResult.

        **参数解释**: 结束时间戳。 **取值范围**: 不涉及。

        :return: The end_time_stamp of this FullSqlStatisticInfoResult.
        :rtype: int
        """
        return self._end_time_stamp

    @end_time_stamp.setter
    def end_time_stamp(self, end_time_stamp):
        r"""Sets the end_time_stamp of this FullSqlStatisticInfoResult.

        **参数解释**: 结束时间戳。 **取值范围**: 不涉及。

        :param end_time_stamp: The end_time_stamp of this FullSqlStatisticInfoResult.
        :type end_time_stamp: int
        """
        self._end_time_stamp = end_time_stamp

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
        if not isinstance(other, FullSqlStatisticInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
