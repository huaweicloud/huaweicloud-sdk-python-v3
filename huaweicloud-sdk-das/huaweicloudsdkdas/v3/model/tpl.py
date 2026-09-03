# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tpl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'sql_template': 'str',
        'sql_sample_string': 'str',
        'db_name': 'str',
        'db_names': 'list[str]',
        'sql_type': 'str',
        'execute_num': 'int',
        'total_cost': 'float',
        'avg_cost': 'float',
        'max_cost': 'float',
        'avg_rows_sent': 'float',
        'max_rows_sent': 'float',
        'avg_rows_affected': 'float',
        'max_rows_affected': 'float',
        'avg_lock_time': 'float',
        'max_lock_time': 'float',
        'total_rows_examined': 'float',
        'avg_rows_examined': 'float',
        'max_rows_examined': 'float',
        'tunable': 'bool',
        'total_cost_ratio': 'str',
        'total_examined_ratio': 'str',
        'execute_num_ratio': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'sql_template': 'sql_template',
        'sql_sample_string': 'sql_sample_string',
        'db_name': 'db_name',
        'db_names': 'db_names',
        'sql_type': 'sql_type',
        'execute_num': 'execute_num',
        'total_cost': 'total_cost',
        'avg_cost': 'avg_cost',
        'max_cost': 'max_cost',
        'avg_rows_sent': 'avg_rows_sent',
        'max_rows_sent': 'max_rows_sent',
        'avg_rows_affected': 'avg_rows_affected',
        'max_rows_affected': 'max_rows_affected',
        'avg_lock_time': 'avg_lock_time',
        'max_lock_time': 'max_lock_time',
        'total_rows_examined': 'total_rows_examined',
        'avg_rows_examined': 'avg_rows_examined',
        'max_rows_examined': 'max_rows_examined',
        'tunable': 'tunable',
        'total_cost_ratio': 'total_cost_ratio',
        'total_examined_ratio': 'total_examined_ratio',
        'execute_num_ratio': 'execute_num_ratio'
    }

    def __init__(self, template_id=None, sql_template=None, sql_sample_string=None, db_name=None, db_names=None, sql_type=None, execute_num=None, total_cost=None, avg_cost=None, max_cost=None, avg_rows_sent=None, max_rows_sent=None, avg_rows_affected=None, max_rows_affected=None, avg_lock_time=None, max_lock_time=None, total_rows_examined=None, avg_rows_examined=None, max_rows_examined=None, tunable=None, total_cost_ratio=None, total_examined_ratio=None, execute_num_ratio=None):
        r"""Tpl

        The model defined in huaweicloud sdk

        :param template_id: SQL模板ID
        :type template_id: str
        :param sql_template: SQL模板
        :type sql_template: str
        :param sql_sample_string: SQL样例
        :type sql_sample_string: str
        :param db_name: 数据库名称
        :type db_name: str
        :param db_names: 数据库列表
        :type db_names: list[str]
        :param sql_type: SQL类型
        :type sql_type: str
        :param execute_num: 执行次数
        :type execute_num: int
        :param total_cost: 总执行耗时 ms
        :type total_cost: float
        :param avg_cost: 平均执行耗时 ms
        :type avg_cost: float
        :param max_cost: 最大执行耗时 ms
        :type max_cost: float
        :param avg_rows_sent: 平均返回行数
        :type avg_rows_sent: float
        :param max_rows_sent: 最大返回行数
        :type max_rows_sent: float
        :param avg_rows_affected: 平均影响行数
        :type avg_rows_affected: float
        :param max_rows_affected: 最大影响行数
        :type max_rows_affected: float
        :param avg_lock_time: 平均锁等待时间
        :type avg_lock_time: float
        :param max_lock_time: 最大锁等待时间
        :type max_lock_time: float
        :param total_rows_examined: 总扫描行数
        :type total_rows_examined: float
        :param avg_rows_examined: 平均扫描行数
        :type avg_rows_examined: float
        :param max_rows_examined: 最大扫描行数
        :type max_rows_examined: float
        :param tunable: 是否支持诊断
        :type tunable: bool
        :param total_cost_ratio: 执行耗时占比
        :type total_cost_ratio: str
        :param total_examined_ratio: 扫描行数占比
        :type total_examined_ratio: str
        :param execute_num_ratio: 执行次数占比
        :type execute_num_ratio: str
        """
        
        

        self._template_id = None
        self._sql_template = None
        self._sql_sample_string = None
        self._db_name = None
        self._db_names = None
        self._sql_type = None
        self._execute_num = None
        self._total_cost = None
        self._avg_cost = None
        self._max_cost = None
        self._avg_rows_sent = None
        self._max_rows_sent = None
        self._avg_rows_affected = None
        self._max_rows_affected = None
        self._avg_lock_time = None
        self._max_lock_time = None
        self._total_rows_examined = None
        self._avg_rows_examined = None
        self._max_rows_examined = None
        self._tunable = None
        self._total_cost_ratio = None
        self._total_examined_ratio = None
        self._execute_num_ratio = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if sql_template is not None:
            self.sql_template = sql_template
        if sql_sample_string is not None:
            self.sql_sample_string = sql_sample_string
        if db_name is not None:
            self.db_name = db_name
        if db_names is not None:
            self.db_names = db_names
        if sql_type is not None:
            self.sql_type = sql_type
        if execute_num is not None:
            self.execute_num = execute_num
        if total_cost is not None:
            self.total_cost = total_cost
        if avg_cost is not None:
            self.avg_cost = avg_cost
        if max_cost is not None:
            self.max_cost = max_cost
        if avg_rows_sent is not None:
            self.avg_rows_sent = avg_rows_sent
        if max_rows_sent is not None:
            self.max_rows_sent = max_rows_sent
        if avg_rows_affected is not None:
            self.avg_rows_affected = avg_rows_affected
        if max_rows_affected is not None:
            self.max_rows_affected = max_rows_affected
        if avg_lock_time is not None:
            self.avg_lock_time = avg_lock_time
        if max_lock_time is not None:
            self.max_lock_time = max_lock_time
        if total_rows_examined is not None:
            self.total_rows_examined = total_rows_examined
        if avg_rows_examined is not None:
            self.avg_rows_examined = avg_rows_examined
        if max_rows_examined is not None:
            self.max_rows_examined = max_rows_examined
        if tunable is not None:
            self.tunable = tunable
        if total_cost_ratio is not None:
            self.total_cost_ratio = total_cost_ratio
        if total_examined_ratio is not None:
            self.total_examined_ratio = total_examined_ratio
        if execute_num_ratio is not None:
            self.execute_num_ratio = execute_num_ratio

    @property
    def template_id(self):
        r"""Gets the template_id of this Tpl.

        SQL模板ID

        :return: The template_id of this Tpl.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this Tpl.

        SQL模板ID

        :param template_id: The template_id of this Tpl.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def sql_template(self):
        r"""Gets the sql_template of this Tpl.

        SQL模板

        :return: The sql_template of this Tpl.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this Tpl.

        SQL模板

        :param sql_template: The sql_template of this Tpl.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def sql_sample_string(self):
        r"""Gets the sql_sample_string of this Tpl.

        SQL样例

        :return: The sql_sample_string of this Tpl.
        :rtype: str
        """
        return self._sql_sample_string

    @sql_sample_string.setter
    def sql_sample_string(self, sql_sample_string):
        r"""Sets the sql_sample_string of this Tpl.

        SQL样例

        :param sql_sample_string: The sql_sample_string of this Tpl.
        :type sql_sample_string: str
        """
        self._sql_sample_string = sql_sample_string

    @property
    def db_name(self):
        r"""Gets the db_name of this Tpl.

        数据库名称

        :return: The db_name of this Tpl.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this Tpl.

        数据库名称

        :param db_name: The db_name of this Tpl.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_names(self):
        r"""Gets the db_names of this Tpl.

        数据库列表

        :return: The db_names of this Tpl.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this Tpl.

        数据库列表

        :param db_names: The db_names of this Tpl.
        :type db_names: list[str]
        """
        self._db_names = db_names

    @property
    def sql_type(self):
        r"""Gets the sql_type of this Tpl.

        SQL类型

        :return: The sql_type of this Tpl.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this Tpl.

        SQL类型

        :param sql_type: The sql_type of this Tpl.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def execute_num(self):
        r"""Gets the execute_num of this Tpl.

        执行次数

        :return: The execute_num of this Tpl.
        :rtype: int
        """
        return self._execute_num

    @execute_num.setter
    def execute_num(self, execute_num):
        r"""Sets the execute_num of this Tpl.

        执行次数

        :param execute_num: The execute_num of this Tpl.
        :type execute_num: int
        """
        self._execute_num = execute_num

    @property
    def total_cost(self):
        r"""Gets the total_cost of this Tpl.

        总执行耗时 ms

        :return: The total_cost of this Tpl.
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        r"""Sets the total_cost of this Tpl.

        总执行耗时 ms

        :param total_cost: The total_cost of this Tpl.
        :type total_cost: float
        """
        self._total_cost = total_cost

    @property
    def avg_cost(self):
        r"""Gets the avg_cost of this Tpl.

        平均执行耗时 ms

        :return: The avg_cost of this Tpl.
        :rtype: float
        """
        return self._avg_cost

    @avg_cost.setter
    def avg_cost(self, avg_cost):
        r"""Sets the avg_cost of this Tpl.

        平均执行耗时 ms

        :param avg_cost: The avg_cost of this Tpl.
        :type avg_cost: float
        """
        self._avg_cost = avg_cost

    @property
    def max_cost(self):
        r"""Gets the max_cost of this Tpl.

        最大执行耗时 ms

        :return: The max_cost of this Tpl.
        :rtype: float
        """
        return self._max_cost

    @max_cost.setter
    def max_cost(self, max_cost):
        r"""Sets the max_cost of this Tpl.

        最大执行耗时 ms

        :param max_cost: The max_cost of this Tpl.
        :type max_cost: float
        """
        self._max_cost = max_cost

    @property
    def avg_rows_sent(self):
        r"""Gets the avg_rows_sent of this Tpl.

        平均返回行数

        :return: The avg_rows_sent of this Tpl.
        :rtype: float
        """
        return self._avg_rows_sent

    @avg_rows_sent.setter
    def avg_rows_sent(self, avg_rows_sent):
        r"""Sets the avg_rows_sent of this Tpl.

        平均返回行数

        :param avg_rows_sent: The avg_rows_sent of this Tpl.
        :type avg_rows_sent: float
        """
        self._avg_rows_sent = avg_rows_sent

    @property
    def max_rows_sent(self):
        r"""Gets the max_rows_sent of this Tpl.

        最大返回行数

        :return: The max_rows_sent of this Tpl.
        :rtype: float
        """
        return self._max_rows_sent

    @max_rows_sent.setter
    def max_rows_sent(self, max_rows_sent):
        r"""Sets the max_rows_sent of this Tpl.

        最大返回行数

        :param max_rows_sent: The max_rows_sent of this Tpl.
        :type max_rows_sent: float
        """
        self._max_rows_sent = max_rows_sent

    @property
    def avg_rows_affected(self):
        r"""Gets the avg_rows_affected of this Tpl.

        平均影响行数

        :return: The avg_rows_affected of this Tpl.
        :rtype: float
        """
        return self._avg_rows_affected

    @avg_rows_affected.setter
    def avg_rows_affected(self, avg_rows_affected):
        r"""Sets the avg_rows_affected of this Tpl.

        平均影响行数

        :param avg_rows_affected: The avg_rows_affected of this Tpl.
        :type avg_rows_affected: float
        """
        self._avg_rows_affected = avg_rows_affected

    @property
    def max_rows_affected(self):
        r"""Gets the max_rows_affected of this Tpl.

        最大影响行数

        :return: The max_rows_affected of this Tpl.
        :rtype: float
        """
        return self._max_rows_affected

    @max_rows_affected.setter
    def max_rows_affected(self, max_rows_affected):
        r"""Sets the max_rows_affected of this Tpl.

        最大影响行数

        :param max_rows_affected: The max_rows_affected of this Tpl.
        :type max_rows_affected: float
        """
        self._max_rows_affected = max_rows_affected

    @property
    def avg_lock_time(self):
        r"""Gets the avg_lock_time of this Tpl.

        平均锁等待时间

        :return: The avg_lock_time of this Tpl.
        :rtype: float
        """
        return self._avg_lock_time

    @avg_lock_time.setter
    def avg_lock_time(self, avg_lock_time):
        r"""Sets the avg_lock_time of this Tpl.

        平均锁等待时间

        :param avg_lock_time: The avg_lock_time of this Tpl.
        :type avg_lock_time: float
        """
        self._avg_lock_time = avg_lock_time

    @property
    def max_lock_time(self):
        r"""Gets the max_lock_time of this Tpl.

        最大锁等待时间

        :return: The max_lock_time of this Tpl.
        :rtype: float
        """
        return self._max_lock_time

    @max_lock_time.setter
    def max_lock_time(self, max_lock_time):
        r"""Sets the max_lock_time of this Tpl.

        最大锁等待时间

        :param max_lock_time: The max_lock_time of this Tpl.
        :type max_lock_time: float
        """
        self._max_lock_time = max_lock_time

    @property
    def total_rows_examined(self):
        r"""Gets the total_rows_examined of this Tpl.

        总扫描行数

        :return: The total_rows_examined of this Tpl.
        :rtype: float
        """
        return self._total_rows_examined

    @total_rows_examined.setter
    def total_rows_examined(self, total_rows_examined):
        r"""Sets the total_rows_examined of this Tpl.

        总扫描行数

        :param total_rows_examined: The total_rows_examined of this Tpl.
        :type total_rows_examined: float
        """
        self._total_rows_examined = total_rows_examined

    @property
    def avg_rows_examined(self):
        r"""Gets the avg_rows_examined of this Tpl.

        平均扫描行数

        :return: The avg_rows_examined of this Tpl.
        :rtype: float
        """
        return self._avg_rows_examined

    @avg_rows_examined.setter
    def avg_rows_examined(self, avg_rows_examined):
        r"""Sets the avg_rows_examined of this Tpl.

        平均扫描行数

        :param avg_rows_examined: The avg_rows_examined of this Tpl.
        :type avg_rows_examined: float
        """
        self._avg_rows_examined = avg_rows_examined

    @property
    def max_rows_examined(self):
        r"""Gets the max_rows_examined of this Tpl.

        最大扫描行数

        :return: The max_rows_examined of this Tpl.
        :rtype: float
        """
        return self._max_rows_examined

    @max_rows_examined.setter
    def max_rows_examined(self, max_rows_examined):
        r"""Sets the max_rows_examined of this Tpl.

        最大扫描行数

        :param max_rows_examined: The max_rows_examined of this Tpl.
        :type max_rows_examined: float
        """
        self._max_rows_examined = max_rows_examined

    @property
    def tunable(self):
        r"""Gets the tunable of this Tpl.

        是否支持诊断

        :return: The tunable of this Tpl.
        :rtype: bool
        """
        return self._tunable

    @tunable.setter
    def tunable(self, tunable):
        r"""Sets the tunable of this Tpl.

        是否支持诊断

        :param tunable: The tunable of this Tpl.
        :type tunable: bool
        """
        self._tunable = tunable

    @property
    def total_cost_ratio(self):
        r"""Gets the total_cost_ratio of this Tpl.

        执行耗时占比

        :return: The total_cost_ratio of this Tpl.
        :rtype: str
        """
        return self._total_cost_ratio

    @total_cost_ratio.setter
    def total_cost_ratio(self, total_cost_ratio):
        r"""Sets the total_cost_ratio of this Tpl.

        执行耗时占比

        :param total_cost_ratio: The total_cost_ratio of this Tpl.
        :type total_cost_ratio: str
        """
        self._total_cost_ratio = total_cost_ratio

    @property
    def total_examined_ratio(self):
        r"""Gets the total_examined_ratio of this Tpl.

        扫描行数占比

        :return: The total_examined_ratio of this Tpl.
        :rtype: str
        """
        return self._total_examined_ratio

    @total_examined_ratio.setter
    def total_examined_ratio(self, total_examined_ratio):
        r"""Sets the total_examined_ratio of this Tpl.

        扫描行数占比

        :param total_examined_ratio: The total_examined_ratio of this Tpl.
        :type total_examined_ratio: str
        """
        self._total_examined_ratio = total_examined_ratio

    @property
    def execute_num_ratio(self):
        r"""Gets the execute_num_ratio of this Tpl.

        执行次数占比

        :return: The execute_num_ratio of this Tpl.
        :rtype: str
        """
        return self._execute_num_ratio

    @execute_num_ratio.setter
    def execute_num_ratio(self, execute_num_ratio):
        r"""Sets the execute_num_ratio of this Tpl.

        执行次数占比

        :param execute_num_ratio: The execute_num_ratio of this Tpl.
        :type execute_num_ratio: str
        """
        self._execute_num_ratio = execute_num_ratio

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
        if not isinstance(other, Tpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
