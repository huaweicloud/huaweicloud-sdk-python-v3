# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ESDBSlowSqlTemplateItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_sample': 'str',
        'database': 'str',
        'execute_times': 'float',
        'avg_rows_examined': 'float',
        'max_time': 'float',
        'avg_time': 'float',
        'max_rows_examined': 'float',
        'rows_examined_sum': 'float',
        'cost_time_sum': 'float'
    }

    attribute_map = {
        'query_sample': 'query_sample',
        'database': 'database',
        'execute_times': 'execute_times',
        'avg_rows_examined': 'avg_rows_examined',
        'max_time': 'max_time',
        'avg_time': 'avg_time',
        'max_rows_examined': 'max_rows_examined',
        'rows_examined_sum': 'rows_examined_sum',
        'cost_time_sum': 'cost_time_sum'
    }

    def __init__(self, query_sample=None, database=None, execute_times=None, avg_rows_examined=None, max_time=None, avg_time=None, max_rows_examined=None, rows_examined_sum=None, cost_time_sum=None):
        r"""ESDBSlowSqlTemplateItem

        The model defined in huaweicloud sdk

        :param query_sample: **参数解释**：  示例。  **参数范围**：  不涉及。
        :type query_sample: str
        :param database: **参数解释**：  数据库。  **参数范围**：  不涉及。
        :type database: str
        :param execute_times: **参数解释**：  执行时间。  **参数范围**：  不涉及。
        :type execute_times: float
        :param avg_rows_examined: **参数解释**：  平均检查行数。  **参数范围**：  不涉及。
        :type avg_rows_examined: float
        :param max_time: **参数解释**：  最大时间。  **参数范围**：  不涉及。
        :type max_time: float
        :param avg_time: **参数解释**：  平均时间。  **参数范围**：  不涉及。
        :type avg_time: float
        :param max_rows_examined: **参数解释**：  最大检查行数。  **参数范围**：  不涉及。
        :type max_rows_examined: float
        :param rows_examined_sum: **参数解释**：  总检查行数。  **参数范围**：  不涉及。
        :type rows_examined_sum: float
        :param cost_time_sum: **参数解释**：  总耗时。  **参数范围**：  不涉及。
        :type cost_time_sum: float
        """
        
        

        self._query_sample = None
        self._database = None
        self._execute_times = None
        self._avg_rows_examined = None
        self._max_time = None
        self._avg_time = None
        self._max_rows_examined = None
        self._rows_examined_sum = None
        self._cost_time_sum = None
        self.discriminator = None

        if query_sample is not None:
            self.query_sample = query_sample
        if database is not None:
            self.database = database
        if execute_times is not None:
            self.execute_times = execute_times
        if avg_rows_examined is not None:
            self.avg_rows_examined = avg_rows_examined
        if max_time is not None:
            self.max_time = max_time
        if avg_time is not None:
            self.avg_time = avg_time
        if max_rows_examined is not None:
            self.max_rows_examined = max_rows_examined
        if rows_examined_sum is not None:
            self.rows_examined_sum = rows_examined_sum
        if cost_time_sum is not None:
            self.cost_time_sum = cost_time_sum

    @property
    def query_sample(self):
        r"""Gets the query_sample of this ESDBSlowSqlTemplateItem.

        **参数解释**：  示例。  **参数范围**：  不涉及。

        :return: The query_sample of this ESDBSlowSqlTemplateItem.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        r"""Sets the query_sample of this ESDBSlowSqlTemplateItem.

        **参数解释**：  示例。  **参数范围**：  不涉及。

        :param query_sample: The query_sample of this ESDBSlowSqlTemplateItem.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def database(self):
        r"""Gets the database of this ESDBSlowSqlTemplateItem.

        **参数解释**：  数据库。  **参数范围**：  不涉及。

        :return: The database of this ESDBSlowSqlTemplateItem.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ESDBSlowSqlTemplateItem.

        **参数解释**：  数据库。  **参数范围**：  不涉及。

        :param database: The database of this ESDBSlowSqlTemplateItem.
        :type database: str
        """
        self._database = database

    @property
    def execute_times(self):
        r"""Gets the execute_times of this ESDBSlowSqlTemplateItem.

        **参数解释**：  执行时间。  **参数范围**：  不涉及。

        :return: The execute_times of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        r"""Sets the execute_times of this ESDBSlowSqlTemplateItem.

        **参数解释**：  执行时间。  **参数范围**：  不涉及。

        :param execute_times: The execute_times of this ESDBSlowSqlTemplateItem.
        :type execute_times: float
        """
        self._execute_times = execute_times

    @property
    def avg_rows_examined(self):
        r"""Gets the avg_rows_examined of this ESDBSlowSqlTemplateItem.

        **参数解释**：  平均检查行数。  **参数范围**：  不涉及。

        :return: The avg_rows_examined of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        r"""Sets the avg_rows_examined of this ESDBSlowSqlTemplateItem.

        **参数解释**：  平均检查行数。  **参数范围**：  不涉及。

        :param avg_rows_examined: The avg_rows_examined of this ESDBSlowSqlTemplateItem.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def max_time(self):
        r"""Gets the max_time of this ESDBSlowSqlTemplateItem.

        **参数解释**：  最大时间。  **参数范围**：  不涉及。

        :return: The max_time of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        r"""Sets the max_time of this ESDBSlowSqlTemplateItem.

        **参数解释**：  最大时间。  **参数范围**：  不涉及。

        :param max_time: The max_time of this ESDBSlowSqlTemplateItem.
        :type max_time: float
        """
        self._max_time = max_time

    @property
    def avg_time(self):
        r"""Gets the avg_time of this ESDBSlowSqlTemplateItem.

        **参数解释**：  平均时间。  **参数范围**：  不涉及。

        :return: The avg_time of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._avg_time

    @avg_time.setter
    def avg_time(self, avg_time):
        r"""Sets the avg_time of this ESDBSlowSqlTemplateItem.

        **参数解释**：  平均时间。  **参数范围**：  不涉及。

        :param avg_time: The avg_time of this ESDBSlowSqlTemplateItem.
        :type avg_time: float
        """
        self._avg_time = avg_time

    @property
    def max_rows_examined(self):
        r"""Gets the max_rows_examined of this ESDBSlowSqlTemplateItem.

        **参数解释**：  最大检查行数。  **参数范围**：  不涉及。

        :return: The max_rows_examined of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._max_rows_examined

    @max_rows_examined.setter
    def max_rows_examined(self, max_rows_examined):
        r"""Sets the max_rows_examined of this ESDBSlowSqlTemplateItem.

        **参数解释**：  最大检查行数。  **参数范围**：  不涉及。

        :param max_rows_examined: The max_rows_examined of this ESDBSlowSqlTemplateItem.
        :type max_rows_examined: float
        """
        self._max_rows_examined = max_rows_examined

    @property
    def rows_examined_sum(self):
        r"""Gets the rows_examined_sum of this ESDBSlowSqlTemplateItem.

        **参数解释**：  总检查行数。  **参数范围**：  不涉及。

        :return: The rows_examined_sum of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._rows_examined_sum

    @rows_examined_sum.setter
    def rows_examined_sum(self, rows_examined_sum):
        r"""Sets the rows_examined_sum of this ESDBSlowSqlTemplateItem.

        **参数解释**：  总检查行数。  **参数范围**：  不涉及。

        :param rows_examined_sum: The rows_examined_sum of this ESDBSlowSqlTemplateItem.
        :type rows_examined_sum: float
        """
        self._rows_examined_sum = rows_examined_sum

    @property
    def cost_time_sum(self):
        r"""Gets the cost_time_sum of this ESDBSlowSqlTemplateItem.

        **参数解释**：  总耗时。  **参数范围**：  不涉及。

        :return: The cost_time_sum of this ESDBSlowSqlTemplateItem.
        :rtype: float
        """
        return self._cost_time_sum

    @cost_time_sum.setter
    def cost_time_sum(self, cost_time_sum):
        r"""Sets the cost_time_sum of this ESDBSlowSqlTemplateItem.

        **参数解释**：  总耗时。  **参数范围**：  不涉及。

        :param cost_time_sum: The cost_time_sum of this ESDBSlowSqlTemplateItem.
        :type cost_time_sum: float
        """
        self._cost_time_sum = cost_time_sum

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
        if not isinstance(other, ESDBSlowSqlTemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
