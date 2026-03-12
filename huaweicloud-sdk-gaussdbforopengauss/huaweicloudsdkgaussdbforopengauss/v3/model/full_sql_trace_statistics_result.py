# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlTraceStatisticsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hit_rate': 'float',
        'db_time': 'int',
        'cpu_time': 'int',
        'io_time': 'int',
        'execution_time': 'int',
        'scan_rows': 'int',
        'update_rows': 'int',
        'insert_rows': 'int',
        'delete_rows': 'int'
    }

    attribute_map = {
        'hit_rate': 'hit_rate',
        'db_time': 'db_time',
        'cpu_time': 'cpu_time',
        'io_time': 'io_time',
        'execution_time': 'execution_time',
        'scan_rows': 'scan_rows',
        'update_rows': 'update_rows',
        'insert_rows': 'insert_rows',
        'delete_rows': 'delete_rows'
    }

    def __init__(self, hit_rate=None, db_time=None, cpu_time=None, io_time=None, execution_time=None, scan_rows=None, update_rows=None, insert_rows=None, delete_rows=None):
        r"""FullSqlTraceStatisticsResult

        The model defined in huaweicloud sdk

        :param hit_rate: **参数解释**: 命中率。 **取值范围**: 不涉及。
        :type hit_rate: float
        :param db_time: **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。
        :type db_time: int
        :param cpu_time: **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。
        :type cpu_time: int
        :param io_time: **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。
        :type io_time: int
        :param execution_time: **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type execution_time: int
        :param scan_rows: **参数解释**: 扫描行数。 **取值范围**: 不涉及。
        :type scan_rows: int
        :param update_rows: **参数解释**: 更新行数。 **取值范围**: 不涉及。
        :type update_rows: int
        :param insert_rows: **参数解释**: 插入行数。 **取值范围**: 不涉及。
        :type insert_rows: int
        :param delete_rows: **参数解释**: 删除行数。 **取值范围**: 不涉及。
        :type delete_rows: int
        """
        
        

        self._hit_rate = None
        self._db_time = None
        self._cpu_time = None
        self._io_time = None
        self._execution_time = None
        self._scan_rows = None
        self._update_rows = None
        self._insert_rows = None
        self._delete_rows = None
        self.discriminator = None

        if hit_rate is not None:
            self.hit_rate = hit_rate
        if db_time is not None:
            self.db_time = db_time
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if io_time is not None:
            self.io_time = io_time
        if execution_time is not None:
            self.execution_time = execution_time
        if scan_rows is not None:
            self.scan_rows = scan_rows
        if update_rows is not None:
            self.update_rows = update_rows
        if insert_rows is not None:
            self.insert_rows = insert_rows
        if delete_rows is not None:
            self.delete_rows = delete_rows

    @property
    def hit_rate(self):
        r"""Gets the hit_rate of this FullSqlTraceStatisticsResult.

        **参数解释**: 命中率。 **取值范围**: 不涉及。

        :return: The hit_rate of this FullSqlTraceStatisticsResult.
        :rtype: float
        """
        return self._hit_rate

    @hit_rate.setter
    def hit_rate(self, hit_rate):
        r"""Sets the hit_rate of this FullSqlTraceStatisticsResult.

        **参数解释**: 命中率。 **取值范围**: 不涉及。

        :param hit_rate: The hit_rate of this FullSqlTraceStatisticsResult.
        :type hit_rate: float
        """
        self._hit_rate = hit_rate

    @property
    def db_time(self):
        r"""Gets the db_time of this FullSqlTraceStatisticsResult.

        **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。

        :return: The db_time of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._db_time

    @db_time.setter
    def db_time(self, db_time):
        r"""Sets the db_time of this FullSqlTraceStatisticsResult.

        **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。

        :param db_time: The db_time of this FullSqlTraceStatisticsResult.
        :type db_time: int
        """
        self._db_time = db_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this FullSqlTraceStatisticsResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The cpu_time of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this FullSqlTraceStatisticsResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this FullSqlTraceStatisticsResult.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def io_time(self):
        r"""Gets the io_time of this FullSqlTraceStatisticsResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The io_time of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._io_time

    @io_time.setter
    def io_time(self, io_time):
        r"""Sets the io_time of this FullSqlTraceStatisticsResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :param io_time: The io_time of this FullSqlTraceStatisticsResult.
        :type io_time: int
        """
        self._io_time = io_time

    @property
    def execution_time(self):
        r"""Gets the execution_time of this FullSqlTraceStatisticsResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The execution_time of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this FullSqlTraceStatisticsResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param execution_time: The execution_time of this FullSqlTraceStatisticsResult.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def scan_rows(self):
        r"""Gets the scan_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 扫描行数。 **取值范围**: 不涉及。

        :return: The scan_rows of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._scan_rows

    @scan_rows.setter
    def scan_rows(self, scan_rows):
        r"""Sets the scan_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 扫描行数。 **取值范围**: 不涉及。

        :param scan_rows: The scan_rows of this FullSqlTraceStatisticsResult.
        :type scan_rows: int
        """
        self._scan_rows = scan_rows

    @property
    def update_rows(self):
        r"""Gets the update_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 更新行数。 **取值范围**: 不涉及。

        :return: The update_rows of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._update_rows

    @update_rows.setter
    def update_rows(self, update_rows):
        r"""Sets the update_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 更新行数。 **取值范围**: 不涉及。

        :param update_rows: The update_rows of this FullSqlTraceStatisticsResult.
        :type update_rows: int
        """
        self._update_rows = update_rows

    @property
    def insert_rows(self):
        r"""Gets the insert_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 插入行数。 **取值范围**: 不涉及。

        :return: The insert_rows of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._insert_rows

    @insert_rows.setter
    def insert_rows(self, insert_rows):
        r"""Sets the insert_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 插入行数。 **取值范围**: 不涉及。

        :param insert_rows: The insert_rows of this FullSqlTraceStatisticsResult.
        :type insert_rows: int
        """
        self._insert_rows = insert_rows

    @property
    def delete_rows(self):
        r"""Gets the delete_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 删除行数。 **取值范围**: 不涉及。

        :return: The delete_rows of this FullSqlTraceStatisticsResult.
        :rtype: int
        """
        return self._delete_rows

    @delete_rows.setter
    def delete_rows(self, delete_rows):
        r"""Sets the delete_rows of this FullSqlTraceStatisticsResult.

        **参数解释**: 删除行数。 **取值范围**: 不涉及。

        :param delete_rows: The delete_rows of this FullSqlTraceStatisticsResult.
        :type delete_rows: int
        """
        self._delete_rows = delete_rows

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
        if not isinstance(other, FullSqlTraceStatisticsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
