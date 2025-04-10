# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsistencyRuleDetailForOpenApi:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'sub_rule_name': 'str',
        'type': 'str',
        'template_id': 'int',
        'connection': 'str',
        'connection_type': 'str',
        'databases': 'str',
        'sql': 'str',
        'tables': 'str',
        'reference_tables': 'str',
        'columns': 'str',
        'reference_columns': 'str',
        'dimension': 'str',
        'queue': 'str',
        'regular_expression': 'str',
        'template_arguments': 'str',
        'weight': 'int',
        'calculation_range': 'str',
        'calculation_range_sql': 'str',
        'alarm_condition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sub_rule_name': 'sub_rule_name',
        'type': 'type',
        'template_id': 'template_id',
        'connection': 'connection',
        'connection_type': 'connection_type',
        'databases': 'databases',
        'sql': 'sql',
        'tables': 'tables',
        'reference_tables': 'reference_tables',
        'columns': 'columns',
        'reference_columns': 'reference_columns',
        'dimension': 'dimension',
        'queue': 'queue',
        'regular_expression': 'regular_expression',
        'template_arguments': 'template_arguments',
        'weight': 'weight',
        'calculation_range': 'calculation_range',
        'calculation_range_sql': 'calculation_range_sql',
        'alarm_condition': 'alarm_condition'
    }

    def __init__(self, id=None, sub_rule_name=None, type=None, template_id=None, connection=None, connection_type=None, databases=None, sql=None, tables=None, reference_tables=None, columns=None, reference_columns=None, dimension=None, queue=None, regular_expression=None, template_arguments=None, weight=None, calculation_range=None, calculation_range_sql=None, alarm_condition=None):
        r"""ConsistencyRuleDetailForOpenApi

        The model defined in huaweicloud sdk

        :param id: 子规则ID
        :type id: int
        :param sub_rule_name: 子规则名称
        :type sub_rule_name: str
        :param type: SingleDatabase:库级规则，SingleTable:表级规则,SingleColumn:字段级规则,CrossColumn:跨字段规则,Customize:自定义规则
        :type type: str
        :param template_id: 规则模板ID
        :type template_id: int
        :param connection: 数据连接ID
        :type connection: str
        :param connection_type: 数据连接类型
        :type connection_type: str
        :param databases: 数据库名，当存在多个值时以逗号分隔
        :type databases: str
        :param sql: 自定义规则中的SQL脚本
        :type sql: str
        :param tables: 表名，当存在多个值时以逗号分隔
        :type tables: str
        :param reference_tables: 对照表名，当存在多个值时以逗号分隔
        :type reference_tables: str
        :param columns: 字段名，当存在多个值时以逗号分隔
        :type columns: str
        :param reference_columns: 对照列名，当存在多个值时以逗号分隔
        :type reference_columns: str
        :param dimension: 维度
        :type dimension: str
        :param queue: DLI队列
        :type queue: str
        :param regular_expression: 当规则模板为正则表达式校验时的正则表达式
        :type regular_expression: str
        :param template_arguments: 模板参数
        :type template_arguments: str
        :param weight: 规则权重
        :type weight: int
        :param calculation_range: 计算范围
        :type calculation_range: str
        :param calculation_range_sql: 计算范围SQL
        :type calculation_range_sql: str
        :param alarm_condition: 告警表达式
        :type alarm_condition: str
        """
        
        

        self._id = None
        self._sub_rule_name = None
        self._type = None
        self._template_id = None
        self._connection = None
        self._connection_type = None
        self._databases = None
        self._sql = None
        self._tables = None
        self._reference_tables = None
        self._columns = None
        self._reference_columns = None
        self._dimension = None
        self._queue = None
        self._regular_expression = None
        self._template_arguments = None
        self._weight = None
        self._calculation_range = None
        self._calculation_range_sql = None
        self._alarm_condition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sub_rule_name is not None:
            self.sub_rule_name = sub_rule_name
        if type is not None:
            self.type = type
        if template_id is not None:
            self.template_id = template_id
        if connection is not None:
            self.connection = connection
        if connection_type is not None:
            self.connection_type = connection_type
        if databases is not None:
            self.databases = databases
        if sql is not None:
            self.sql = sql
        if tables is not None:
            self.tables = tables
        if reference_tables is not None:
            self.reference_tables = reference_tables
        if columns is not None:
            self.columns = columns
        if reference_columns is not None:
            self.reference_columns = reference_columns
        if dimension is not None:
            self.dimension = dimension
        if queue is not None:
            self.queue = queue
        if regular_expression is not None:
            self.regular_expression = regular_expression
        if template_arguments is not None:
            self.template_arguments = template_arguments
        if weight is not None:
            self.weight = weight
        if calculation_range is not None:
            self.calculation_range = calculation_range
        if calculation_range_sql is not None:
            self.calculation_range_sql = calculation_range_sql
        if alarm_condition is not None:
            self.alarm_condition = alarm_condition

    @property
    def id(self):
        r"""Gets the id of this ConsistencyRuleDetailForOpenApi.

        子规则ID

        :return: The id of this ConsistencyRuleDetailForOpenApi.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConsistencyRuleDetailForOpenApi.

        子规则ID

        :param id: The id of this ConsistencyRuleDetailForOpenApi.
        :type id: int
        """
        self._id = id

    @property
    def sub_rule_name(self):
        r"""Gets the sub_rule_name of this ConsistencyRuleDetailForOpenApi.

        子规则名称

        :return: The sub_rule_name of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._sub_rule_name

    @sub_rule_name.setter
    def sub_rule_name(self, sub_rule_name):
        r"""Sets the sub_rule_name of this ConsistencyRuleDetailForOpenApi.

        子规则名称

        :param sub_rule_name: The sub_rule_name of this ConsistencyRuleDetailForOpenApi.
        :type sub_rule_name: str
        """
        self._sub_rule_name = sub_rule_name

    @property
    def type(self):
        r"""Gets the type of this ConsistencyRuleDetailForOpenApi.

        SingleDatabase:库级规则，SingleTable:表级规则,SingleColumn:字段级规则,CrossColumn:跨字段规则,Customize:自定义规则

        :return: The type of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConsistencyRuleDetailForOpenApi.

        SingleDatabase:库级规则，SingleTable:表级规则,SingleColumn:字段级规则,CrossColumn:跨字段规则,Customize:自定义规则

        :param type: The type of this ConsistencyRuleDetailForOpenApi.
        :type type: str
        """
        self._type = type

    @property
    def template_id(self):
        r"""Gets the template_id of this ConsistencyRuleDetailForOpenApi.

        规则模板ID

        :return: The template_id of this ConsistencyRuleDetailForOpenApi.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ConsistencyRuleDetailForOpenApi.

        规则模板ID

        :param template_id: The template_id of this ConsistencyRuleDetailForOpenApi.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def connection(self):
        r"""Gets the connection of this ConsistencyRuleDetailForOpenApi.

        数据连接ID

        :return: The connection of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ConsistencyRuleDetailForOpenApi.

        数据连接ID

        :param connection: The connection of this ConsistencyRuleDetailForOpenApi.
        :type connection: str
        """
        self._connection = connection

    @property
    def connection_type(self):
        r"""Gets the connection_type of this ConsistencyRuleDetailForOpenApi.

        数据连接类型

        :return: The connection_type of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this ConsistencyRuleDetailForOpenApi.

        数据连接类型

        :param connection_type: The connection_type of this ConsistencyRuleDetailForOpenApi.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def databases(self):
        r"""Gets the databases of this ConsistencyRuleDetailForOpenApi.

        数据库名，当存在多个值时以逗号分隔

        :return: The databases of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ConsistencyRuleDetailForOpenApi.

        数据库名，当存在多个值时以逗号分隔

        :param databases: The databases of this ConsistencyRuleDetailForOpenApi.
        :type databases: str
        """
        self._databases = databases

    @property
    def sql(self):
        r"""Gets the sql of this ConsistencyRuleDetailForOpenApi.

        自定义规则中的SQL脚本

        :return: The sql of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ConsistencyRuleDetailForOpenApi.

        自定义规则中的SQL脚本

        :param sql: The sql of this ConsistencyRuleDetailForOpenApi.
        :type sql: str
        """
        self._sql = sql

    @property
    def tables(self):
        r"""Gets the tables of this ConsistencyRuleDetailForOpenApi.

        表名，当存在多个值时以逗号分隔

        :return: The tables of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this ConsistencyRuleDetailForOpenApi.

        表名，当存在多个值时以逗号分隔

        :param tables: The tables of this ConsistencyRuleDetailForOpenApi.
        :type tables: str
        """
        self._tables = tables

    @property
    def reference_tables(self):
        r"""Gets the reference_tables of this ConsistencyRuleDetailForOpenApi.

        对照表名，当存在多个值时以逗号分隔

        :return: The reference_tables of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._reference_tables

    @reference_tables.setter
    def reference_tables(self, reference_tables):
        r"""Sets the reference_tables of this ConsistencyRuleDetailForOpenApi.

        对照表名，当存在多个值时以逗号分隔

        :param reference_tables: The reference_tables of this ConsistencyRuleDetailForOpenApi.
        :type reference_tables: str
        """
        self._reference_tables = reference_tables

    @property
    def columns(self):
        r"""Gets the columns of this ConsistencyRuleDetailForOpenApi.

        字段名，当存在多个值时以逗号分隔

        :return: The columns of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this ConsistencyRuleDetailForOpenApi.

        字段名，当存在多个值时以逗号分隔

        :param columns: The columns of this ConsistencyRuleDetailForOpenApi.
        :type columns: str
        """
        self._columns = columns

    @property
    def reference_columns(self):
        r"""Gets the reference_columns of this ConsistencyRuleDetailForOpenApi.

        对照列名，当存在多个值时以逗号分隔

        :return: The reference_columns of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._reference_columns

    @reference_columns.setter
    def reference_columns(self, reference_columns):
        r"""Sets the reference_columns of this ConsistencyRuleDetailForOpenApi.

        对照列名，当存在多个值时以逗号分隔

        :param reference_columns: The reference_columns of this ConsistencyRuleDetailForOpenApi.
        :type reference_columns: str
        """
        self._reference_columns = reference_columns

    @property
    def dimension(self):
        r"""Gets the dimension of this ConsistencyRuleDetailForOpenApi.

        维度

        :return: The dimension of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this ConsistencyRuleDetailForOpenApi.

        维度

        :param dimension: The dimension of this ConsistencyRuleDetailForOpenApi.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def queue(self):
        r"""Gets the queue of this ConsistencyRuleDetailForOpenApi.

        DLI队列

        :return: The queue of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this ConsistencyRuleDetailForOpenApi.

        DLI队列

        :param queue: The queue of this ConsistencyRuleDetailForOpenApi.
        :type queue: str
        """
        self._queue = queue

    @property
    def regular_expression(self):
        r"""Gets the regular_expression of this ConsistencyRuleDetailForOpenApi.

        当规则模板为正则表达式校验时的正则表达式

        :return: The regular_expression of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        r"""Sets the regular_expression of this ConsistencyRuleDetailForOpenApi.

        当规则模板为正则表达式校验时的正则表达式

        :param regular_expression: The regular_expression of this ConsistencyRuleDetailForOpenApi.
        :type regular_expression: str
        """
        self._regular_expression = regular_expression

    @property
    def template_arguments(self):
        r"""Gets the template_arguments of this ConsistencyRuleDetailForOpenApi.

        模板参数

        :return: The template_arguments of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._template_arguments

    @template_arguments.setter
    def template_arguments(self, template_arguments):
        r"""Sets the template_arguments of this ConsistencyRuleDetailForOpenApi.

        模板参数

        :param template_arguments: The template_arguments of this ConsistencyRuleDetailForOpenApi.
        :type template_arguments: str
        """
        self._template_arguments = template_arguments

    @property
    def weight(self):
        r"""Gets the weight of this ConsistencyRuleDetailForOpenApi.

        规则权重

        :return: The weight of this ConsistencyRuleDetailForOpenApi.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ConsistencyRuleDetailForOpenApi.

        规则权重

        :param weight: The weight of this ConsistencyRuleDetailForOpenApi.
        :type weight: int
        """
        self._weight = weight

    @property
    def calculation_range(self):
        r"""Gets the calculation_range of this ConsistencyRuleDetailForOpenApi.

        计算范围

        :return: The calculation_range of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._calculation_range

    @calculation_range.setter
    def calculation_range(self, calculation_range):
        r"""Sets the calculation_range of this ConsistencyRuleDetailForOpenApi.

        计算范围

        :param calculation_range: The calculation_range of this ConsistencyRuleDetailForOpenApi.
        :type calculation_range: str
        """
        self._calculation_range = calculation_range

    @property
    def calculation_range_sql(self):
        r"""Gets the calculation_range_sql of this ConsistencyRuleDetailForOpenApi.

        计算范围SQL

        :return: The calculation_range_sql of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._calculation_range_sql

    @calculation_range_sql.setter
    def calculation_range_sql(self, calculation_range_sql):
        r"""Sets the calculation_range_sql of this ConsistencyRuleDetailForOpenApi.

        计算范围SQL

        :param calculation_range_sql: The calculation_range_sql of this ConsistencyRuleDetailForOpenApi.
        :type calculation_range_sql: str
        """
        self._calculation_range_sql = calculation_range_sql

    @property
    def alarm_condition(self):
        r"""Gets the alarm_condition of this ConsistencyRuleDetailForOpenApi.

        告警表达式

        :return: The alarm_condition of this ConsistencyRuleDetailForOpenApi.
        :rtype: str
        """
        return self._alarm_condition

    @alarm_condition.setter
    def alarm_condition(self, alarm_condition):
        r"""Sets the alarm_condition of this ConsistencyRuleDetailForOpenApi.

        告警表达式

        :param alarm_condition: The alarm_condition of this ConsistencyRuleDetailForOpenApi.
        :type alarm_condition: str
        """
        self._alarm_condition = alarm_condition

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
        if not isinstance(other, ConsistencyRuleDetailForOpenApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
