# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayExecuteRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_time': 'int',
        'finished_sql': 'int',
        'abnormal_sql': 'int',
        'slow_sql': 'int',
        'total_sql': 'int'
    }

    attribute_map = {
        'execute_time': 'execute_time',
        'finished_sql': 'finished_sql',
        'abnormal_sql': 'abnormal_sql',
        'slow_sql': 'slow_sql',
        'total_sql': 'total_sql'
    }

    def __init__(self, execute_time=None, finished_sql=None, abnormal_sql=None, slow_sql=None, total_sql=None):
        r"""ReplayExecuteRecords

        The model defined in huaweicloud sdk

        :param execute_time: 执行记录的时间，格式为秒级时间戳。
        :type execute_time: int
        :param finished_sql: 执行完的SQL数量。
        :type finished_sql: int
        :param abnormal_sql: 执行的异常SQL数量。
        :type abnormal_sql: int
        :param slow_sql: 执行的慢SQL数量。
        :type slow_sql: int
        :param total_sql: 执行记录的SQL总数。
        :type total_sql: int
        """
        
        

        self._execute_time = None
        self._finished_sql = None
        self._abnormal_sql = None
        self._slow_sql = None
        self._total_sql = None
        self.discriminator = None

        if execute_time is not None:
            self.execute_time = execute_time
        if finished_sql is not None:
            self.finished_sql = finished_sql
        if abnormal_sql is not None:
            self.abnormal_sql = abnormal_sql
        if slow_sql is not None:
            self.slow_sql = slow_sql
        if total_sql is not None:
            self.total_sql = total_sql

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ReplayExecuteRecords.

        执行记录的时间，格式为秒级时间戳。

        :return: The execute_time of this ReplayExecuteRecords.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ReplayExecuteRecords.

        执行记录的时间，格式为秒级时间戳。

        :param execute_time: The execute_time of this ReplayExecuteRecords.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def finished_sql(self):
        r"""Gets the finished_sql of this ReplayExecuteRecords.

        执行完的SQL数量。

        :return: The finished_sql of this ReplayExecuteRecords.
        :rtype: int
        """
        return self._finished_sql

    @finished_sql.setter
    def finished_sql(self, finished_sql):
        r"""Sets the finished_sql of this ReplayExecuteRecords.

        执行完的SQL数量。

        :param finished_sql: The finished_sql of this ReplayExecuteRecords.
        :type finished_sql: int
        """
        self._finished_sql = finished_sql

    @property
    def abnormal_sql(self):
        r"""Gets the abnormal_sql of this ReplayExecuteRecords.

        执行的异常SQL数量。

        :return: The abnormal_sql of this ReplayExecuteRecords.
        :rtype: int
        """
        return self._abnormal_sql

    @abnormal_sql.setter
    def abnormal_sql(self, abnormal_sql):
        r"""Sets the abnormal_sql of this ReplayExecuteRecords.

        执行的异常SQL数量。

        :param abnormal_sql: The abnormal_sql of this ReplayExecuteRecords.
        :type abnormal_sql: int
        """
        self._abnormal_sql = abnormal_sql

    @property
    def slow_sql(self):
        r"""Gets the slow_sql of this ReplayExecuteRecords.

        执行的慢SQL数量。

        :return: The slow_sql of this ReplayExecuteRecords.
        :rtype: int
        """
        return self._slow_sql

    @slow_sql.setter
    def slow_sql(self, slow_sql):
        r"""Sets the slow_sql of this ReplayExecuteRecords.

        执行的慢SQL数量。

        :param slow_sql: The slow_sql of this ReplayExecuteRecords.
        :type slow_sql: int
        """
        self._slow_sql = slow_sql

    @property
    def total_sql(self):
        r"""Gets the total_sql of this ReplayExecuteRecords.

        执行记录的SQL总数。

        :return: The total_sql of this ReplayExecuteRecords.
        :rtype: int
        """
        return self._total_sql

    @total_sql.setter
    def total_sql(self, total_sql):
        r"""Sets the total_sql of this ReplayExecuteRecords.

        执行记录的SQL总数。

        :param total_sql: The total_sql of this ReplayExecuteRecords.
        :type total_sql: int
        """
        self._total_sql = total_sql

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
        if not isinstance(other, ReplayExecuteRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
