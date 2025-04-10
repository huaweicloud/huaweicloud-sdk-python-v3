# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopSqlTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'sql_sample_string': 'str',
        'sql_type': 'str',
        'db_name': 'str',
        'execute_num': 'int',
        'total_cost': 'float',
        'avg_cost': 'float',
        'avg_rows_sent': 'float',
        'avg_rows_affected': 'float',
        'avg_lock_time': 'float',
        'total_rows_examined': 'float',
        'avg_rows_examined': 'float',
        'total_cost_ratio': 'str',
        'total_examined_ratio': 'str',
        'execute_num_ratio': 'str'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'sql_sample_string': 'sql_sample_string',
        'sql_type': 'sql_type',
        'db_name': 'db_name',
        'execute_num': 'execute_num',
        'total_cost': 'total_cost',
        'avg_cost': 'avg_cost',
        'avg_rows_sent': 'avg_rows_sent',
        'avg_rows_affected': 'avg_rows_affected',
        'avg_lock_time': 'avg_lock_time',
        'total_rows_examined': 'total_rows_examined',
        'avg_rows_examined': 'avg_rows_examined',
        'total_cost_ratio': 'total_cost_ratio',
        'total_examined_ratio': 'total_examined_ratio',
        'execute_num_ratio': 'execute_num_ratio'
    }

    def __init__(self, sql_template=None, sql_sample_string=None, sql_type=None, db_name=None, execute_num=None, total_cost=None, avg_cost=None, avg_rows_sent=None, avg_rows_affected=None, avg_lock_time=None, total_rows_examined=None, avg_rows_examined=None, total_cost_ratio=None, total_examined_ratio=None, execute_num_ratio=None):
        r"""TopSqlTemplate

        The model defined in huaweicloud sdk

        :param sql_template: SQL模板。
        :type sql_template: str
        :param sql_sample_string: SQL样本。
        :type sql_sample_string: str
        :param sql_type: SQL操作类型。
        :type sql_type: str
        :param db_name: 数据库名称。
        :type db_name: str
        :param execute_num: 总执行次数。
        :type execute_num: int
        :param total_cost: 总耗时(ms)。
        :type total_cost: float
        :param avg_cost: 平均耗时(ms)。
        :type avg_cost: float
        :param avg_rows_sent: 平均返回行数。
        :type avg_rows_sent: float
        :param avg_rows_affected: 平均影响行数。
        :type avg_rows_affected: float
        :param avg_lock_time: 平均锁等待耗时(ms)。
        :type avg_lock_time: float
        :param total_rows_examined: 总扫描行数。
        :type total_rows_examined: float
        :param avg_rows_examined: 平均扫描行数。
        :type avg_rows_examined: float
        :param total_cost_ratio: 总耗时占比。
        :type total_cost_ratio: str
        :param total_examined_ratio: 扫描行数占比。
        :type total_examined_ratio: str
        :param execute_num_ratio: 执行次数占比。
        :type execute_num_ratio: str
        """
        
        

        self._sql_template = None
        self._sql_sample_string = None
        self._sql_type = None
        self._db_name = None
        self._execute_num = None
        self._total_cost = None
        self._avg_cost = None
        self._avg_rows_sent = None
        self._avg_rows_affected = None
        self._avg_lock_time = None
        self._total_rows_examined = None
        self._avg_rows_examined = None
        self._total_cost_ratio = None
        self._total_examined_ratio = None
        self._execute_num_ratio = None
        self.discriminator = None

        self.sql_template = sql_template
        self.sql_sample_string = sql_sample_string
        self.sql_type = sql_type
        self.db_name = db_name
        self.execute_num = execute_num
        self.total_cost = total_cost
        self.avg_cost = avg_cost
        self.avg_rows_sent = avg_rows_sent
        self.avg_rows_affected = avg_rows_affected
        self.avg_lock_time = avg_lock_time
        self.total_rows_examined = total_rows_examined
        self.avg_rows_examined = avg_rows_examined
        self.total_cost_ratio = total_cost_ratio
        self.total_examined_ratio = total_examined_ratio
        self.execute_num_ratio = execute_num_ratio

    @property
    def sql_template(self):
        r"""Gets the sql_template of this TopSqlTemplate.

        SQL模板。

        :return: The sql_template of this TopSqlTemplate.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this TopSqlTemplate.

        SQL模板。

        :param sql_template: The sql_template of this TopSqlTemplate.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def sql_sample_string(self):
        r"""Gets the sql_sample_string of this TopSqlTemplate.

        SQL样本。

        :return: The sql_sample_string of this TopSqlTemplate.
        :rtype: str
        """
        return self._sql_sample_string

    @sql_sample_string.setter
    def sql_sample_string(self, sql_sample_string):
        r"""Sets the sql_sample_string of this TopSqlTemplate.

        SQL样本。

        :param sql_sample_string: The sql_sample_string of this TopSqlTemplate.
        :type sql_sample_string: str
        """
        self._sql_sample_string = sql_sample_string

    @property
    def sql_type(self):
        r"""Gets the sql_type of this TopSqlTemplate.

        SQL操作类型。

        :return: The sql_type of this TopSqlTemplate.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this TopSqlTemplate.

        SQL操作类型。

        :param sql_type: The sql_type of this TopSqlTemplate.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def db_name(self):
        r"""Gets the db_name of this TopSqlTemplate.

        数据库名称。

        :return: The db_name of this TopSqlTemplate.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TopSqlTemplate.

        数据库名称。

        :param db_name: The db_name of this TopSqlTemplate.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def execute_num(self):
        r"""Gets the execute_num of this TopSqlTemplate.

        总执行次数。

        :return: The execute_num of this TopSqlTemplate.
        :rtype: int
        """
        return self._execute_num

    @execute_num.setter
    def execute_num(self, execute_num):
        r"""Sets the execute_num of this TopSqlTemplate.

        总执行次数。

        :param execute_num: The execute_num of this TopSqlTemplate.
        :type execute_num: int
        """
        self._execute_num = execute_num

    @property
    def total_cost(self):
        r"""Gets the total_cost of this TopSqlTemplate.

        总耗时(ms)。

        :return: The total_cost of this TopSqlTemplate.
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        r"""Sets the total_cost of this TopSqlTemplate.

        总耗时(ms)。

        :param total_cost: The total_cost of this TopSqlTemplate.
        :type total_cost: float
        """
        self._total_cost = total_cost

    @property
    def avg_cost(self):
        r"""Gets the avg_cost of this TopSqlTemplate.

        平均耗时(ms)。

        :return: The avg_cost of this TopSqlTemplate.
        :rtype: float
        """
        return self._avg_cost

    @avg_cost.setter
    def avg_cost(self, avg_cost):
        r"""Sets the avg_cost of this TopSqlTemplate.

        平均耗时(ms)。

        :param avg_cost: The avg_cost of this TopSqlTemplate.
        :type avg_cost: float
        """
        self._avg_cost = avg_cost

    @property
    def avg_rows_sent(self):
        r"""Gets the avg_rows_sent of this TopSqlTemplate.

        平均返回行数。

        :return: The avg_rows_sent of this TopSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_sent

    @avg_rows_sent.setter
    def avg_rows_sent(self, avg_rows_sent):
        r"""Sets the avg_rows_sent of this TopSqlTemplate.

        平均返回行数。

        :param avg_rows_sent: The avg_rows_sent of this TopSqlTemplate.
        :type avg_rows_sent: float
        """
        self._avg_rows_sent = avg_rows_sent

    @property
    def avg_rows_affected(self):
        r"""Gets the avg_rows_affected of this TopSqlTemplate.

        平均影响行数。

        :return: The avg_rows_affected of this TopSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_affected

    @avg_rows_affected.setter
    def avg_rows_affected(self, avg_rows_affected):
        r"""Sets the avg_rows_affected of this TopSqlTemplate.

        平均影响行数。

        :param avg_rows_affected: The avg_rows_affected of this TopSqlTemplate.
        :type avg_rows_affected: float
        """
        self._avg_rows_affected = avg_rows_affected

    @property
    def avg_lock_time(self):
        r"""Gets the avg_lock_time of this TopSqlTemplate.

        平均锁等待耗时(ms)。

        :return: The avg_lock_time of this TopSqlTemplate.
        :rtype: float
        """
        return self._avg_lock_time

    @avg_lock_time.setter
    def avg_lock_time(self, avg_lock_time):
        r"""Sets the avg_lock_time of this TopSqlTemplate.

        平均锁等待耗时(ms)。

        :param avg_lock_time: The avg_lock_time of this TopSqlTemplate.
        :type avg_lock_time: float
        """
        self._avg_lock_time = avg_lock_time

    @property
    def total_rows_examined(self):
        r"""Gets the total_rows_examined of this TopSqlTemplate.

        总扫描行数。

        :return: The total_rows_examined of this TopSqlTemplate.
        :rtype: float
        """
        return self._total_rows_examined

    @total_rows_examined.setter
    def total_rows_examined(self, total_rows_examined):
        r"""Sets the total_rows_examined of this TopSqlTemplate.

        总扫描行数。

        :param total_rows_examined: The total_rows_examined of this TopSqlTemplate.
        :type total_rows_examined: float
        """
        self._total_rows_examined = total_rows_examined

    @property
    def avg_rows_examined(self):
        r"""Gets the avg_rows_examined of this TopSqlTemplate.

        平均扫描行数。

        :return: The avg_rows_examined of this TopSqlTemplate.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        r"""Sets the avg_rows_examined of this TopSqlTemplate.

        平均扫描行数。

        :param avg_rows_examined: The avg_rows_examined of this TopSqlTemplate.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def total_cost_ratio(self):
        r"""Gets the total_cost_ratio of this TopSqlTemplate.

        总耗时占比。

        :return: The total_cost_ratio of this TopSqlTemplate.
        :rtype: str
        """
        return self._total_cost_ratio

    @total_cost_ratio.setter
    def total_cost_ratio(self, total_cost_ratio):
        r"""Sets the total_cost_ratio of this TopSqlTemplate.

        总耗时占比。

        :param total_cost_ratio: The total_cost_ratio of this TopSqlTemplate.
        :type total_cost_ratio: str
        """
        self._total_cost_ratio = total_cost_ratio

    @property
    def total_examined_ratio(self):
        r"""Gets the total_examined_ratio of this TopSqlTemplate.

        扫描行数占比。

        :return: The total_examined_ratio of this TopSqlTemplate.
        :rtype: str
        """
        return self._total_examined_ratio

    @total_examined_ratio.setter
    def total_examined_ratio(self, total_examined_ratio):
        r"""Sets the total_examined_ratio of this TopSqlTemplate.

        扫描行数占比。

        :param total_examined_ratio: The total_examined_ratio of this TopSqlTemplate.
        :type total_examined_ratio: str
        """
        self._total_examined_ratio = total_examined_ratio

    @property
    def execute_num_ratio(self):
        r"""Gets the execute_num_ratio of this TopSqlTemplate.

        执行次数占比。

        :return: The execute_num_ratio of this TopSqlTemplate.
        :rtype: str
        """
        return self._execute_num_ratio

    @execute_num_ratio.setter
    def execute_num_ratio(self, execute_num_ratio):
        r"""Sets the execute_num_ratio of this TopSqlTemplate.

        执行次数占比。

        :param execute_num_ratio: The execute_num_ratio of this TopSqlTemplate.
        :type execute_num_ratio: str
        """
        self._execute_num_ratio = execute_num_ratio

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
        if not isinstance(other, TopSqlTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
