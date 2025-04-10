# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityTaskRuleDetailForOpenApi:

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
        'ignore_error': 'bool',
        'dimension': 'str',
        'queue': 'str',
        'regular_expression': 'str',
        'template_arguments': 'str',
        'weight': 'int',
        'calculation_range': 'str',
        'calculation_range_sql': 'str',
        'alarm_condition': 'str',
        'export_abnormal_table': 'bool',
        'abnormal_table_database': 'str',
        'abnormal_table_schema': 'str',
        'abnormal_table': 'str',
        'abnormal_table_prefix': 'str',
        'abnormal_table_suffix': 'str',
        'abnormal_table_columns': 'str',
        'abnormal_table_sql': 'str',
        'abnormal_table_out_config': 'bool',
        'abnormal_table_include_null_value': 'bool',
        'abnormal_table_out_data_number': 'int',
        'score_switch': 'bool',
        'score_schema': 'str',
        'score_table': 'str',
        'score_expression': 'str'
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
        'ignore_error': 'ignore_error',
        'dimension': 'dimension',
        'queue': 'queue',
        'regular_expression': 'regular_expression',
        'template_arguments': 'template_arguments',
        'weight': 'weight',
        'calculation_range': 'calculation_range',
        'calculation_range_sql': 'calculation_range_sql',
        'alarm_condition': 'alarm_condition',
        'export_abnormal_table': 'export_abnormal_table',
        'abnormal_table_database': 'abnormal_table_database',
        'abnormal_table_schema': 'abnormal_table_schema',
        'abnormal_table': 'abnormal_table',
        'abnormal_table_prefix': 'abnormal_table_prefix',
        'abnormal_table_suffix': 'abnormal_table_suffix',
        'abnormal_table_columns': 'abnormal_table_columns',
        'abnormal_table_sql': 'abnormal_table_sql',
        'abnormal_table_out_config': 'abnormal_table_out_config',
        'abnormal_table_include_null_value': 'abnormal_table_include_null_value',
        'abnormal_table_out_data_number': 'abnormal_table_out_data_number',
        'score_switch': 'score_switch',
        'score_schema': 'score_schema',
        'score_table': 'score_table',
        'score_expression': 'score_expression'
    }

    def __init__(self, id=None, sub_rule_name=None, type=None, template_id=None, connection=None, connection_type=None, databases=None, sql=None, tables=None, reference_tables=None, columns=None, reference_columns=None, ignore_error=None, dimension=None, queue=None, regular_expression=None, template_arguments=None, weight=None, calculation_range=None, calculation_range_sql=None, alarm_condition=None, export_abnormal_table=None, abnormal_table_database=None, abnormal_table_schema=None, abnormal_table=None, abnormal_table_prefix=None, abnormal_table_suffix=None, abnormal_table_columns=None, abnormal_table_sql=None, abnormal_table_out_config=None, abnormal_table_include_null_value=None, abnormal_table_out_data_number=None, score_switch=None, score_schema=None, score_table=None, score_expression=None):
        r"""QualityTaskRuleDetailForOpenApi

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
        :param sql: 自定义规则中的SQL脚本，系统内置规则时返回
        :type sql: str
        :param tables: 表名，当存在多个值时以逗号分隔
        :type tables: str
        :param reference_tables: 跨字段规则中的参考表名，当存在多个值时以逗号分隔
        :type reference_tables: str
        :param columns: 字段名，当存在多个值时以逗号分隔
        :type columns: str
        :param reference_columns: 跨字段规则中的参考字段名，当存在多个值时以逗号分隔
        :type reference_columns: str
        :param ignore_error: 是否忽视规则错误
        :type ignore_error: bool
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
        :param export_abnormal_table: 是否导出异常数据
        :type export_abnormal_table: bool
        :param abnormal_table_database: 异常表数据库
        :type abnormal_table_database: str
        :param abnormal_table_schema: 异常表Schema
        :type abnormal_table_schema: str
        :param abnormal_table: 异常字段所在的表
        :type abnormal_table: str
        :param abnormal_table_prefix: 异常表前缀
        :type abnormal_table_prefix: str
        :param abnormal_table_suffix: 异常表后缀
        :type abnormal_table_suffix: str
        :param abnormal_table_columns: 异常字段名，当存在多个值时以逗号分隔
        :type abnormal_table_columns: str
        :param abnormal_table_sql: 异常表SQL
        :type abnormal_table_sql: str
        :param abnormal_table_out_config: 异常表是否输出规则配置
        :type abnormal_table_out_config: bool
        :param abnormal_table_include_null_value: 异常表是否包含空值
        :type abnormal_table_include_null_value: bool
        :param abnormal_table_out_data_number: 异常表输出行数, 0代表全量输出
        :type abnormal_table_out_data_number: int
        :param score_switch: 是否开启质量评分
        :type score_switch: bool
        :param score_schema: 质量评分表所在schema
        :type score_schema: str
        :param score_table: 质量评分表名
        :type score_table: str
        :param score_expression: 质量评分表达式
        :type score_expression: str
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
        self._ignore_error = None
        self._dimension = None
        self._queue = None
        self._regular_expression = None
        self._template_arguments = None
        self._weight = None
        self._calculation_range = None
        self._calculation_range_sql = None
        self._alarm_condition = None
        self._export_abnormal_table = None
        self._abnormal_table_database = None
        self._abnormal_table_schema = None
        self._abnormal_table = None
        self._abnormal_table_prefix = None
        self._abnormal_table_suffix = None
        self._abnormal_table_columns = None
        self._abnormal_table_sql = None
        self._abnormal_table_out_config = None
        self._abnormal_table_include_null_value = None
        self._abnormal_table_out_data_number = None
        self._score_switch = None
        self._score_schema = None
        self._score_table = None
        self._score_expression = None
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
        if ignore_error is not None:
            self.ignore_error = ignore_error
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
        if export_abnormal_table is not None:
            self.export_abnormal_table = export_abnormal_table
        if abnormal_table_database is not None:
            self.abnormal_table_database = abnormal_table_database
        if abnormal_table_schema is not None:
            self.abnormal_table_schema = abnormal_table_schema
        if abnormal_table is not None:
            self.abnormal_table = abnormal_table
        if abnormal_table_prefix is not None:
            self.abnormal_table_prefix = abnormal_table_prefix
        if abnormal_table_suffix is not None:
            self.abnormal_table_suffix = abnormal_table_suffix
        if abnormal_table_columns is not None:
            self.abnormal_table_columns = abnormal_table_columns
        if abnormal_table_sql is not None:
            self.abnormal_table_sql = abnormal_table_sql
        if abnormal_table_out_config is not None:
            self.abnormal_table_out_config = abnormal_table_out_config
        if abnormal_table_include_null_value is not None:
            self.abnormal_table_include_null_value = abnormal_table_include_null_value
        if abnormal_table_out_data_number is not None:
            self.abnormal_table_out_data_number = abnormal_table_out_data_number
        if score_switch is not None:
            self.score_switch = score_switch
        if score_schema is not None:
            self.score_schema = score_schema
        if score_table is not None:
            self.score_table = score_table
        if score_expression is not None:
            self.score_expression = score_expression

    @property
    def id(self):
        r"""Gets the id of this QualityTaskRuleDetailForOpenApi.

        子规则ID

        :return: The id of this QualityTaskRuleDetailForOpenApi.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QualityTaskRuleDetailForOpenApi.

        子规则ID

        :param id: The id of this QualityTaskRuleDetailForOpenApi.
        :type id: int
        """
        self._id = id

    @property
    def sub_rule_name(self):
        r"""Gets the sub_rule_name of this QualityTaskRuleDetailForOpenApi.

        子规则名称

        :return: The sub_rule_name of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._sub_rule_name

    @sub_rule_name.setter
    def sub_rule_name(self, sub_rule_name):
        r"""Sets the sub_rule_name of this QualityTaskRuleDetailForOpenApi.

        子规则名称

        :param sub_rule_name: The sub_rule_name of this QualityTaskRuleDetailForOpenApi.
        :type sub_rule_name: str
        """
        self._sub_rule_name = sub_rule_name

    @property
    def type(self):
        r"""Gets the type of this QualityTaskRuleDetailForOpenApi.

        SingleDatabase:库级规则，SingleTable:表级规则,SingleColumn:字段级规则,CrossColumn:跨字段规则,Customize:自定义规则

        :return: The type of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QualityTaskRuleDetailForOpenApi.

        SingleDatabase:库级规则，SingleTable:表级规则,SingleColumn:字段级规则,CrossColumn:跨字段规则,Customize:自定义规则

        :param type: The type of this QualityTaskRuleDetailForOpenApi.
        :type type: str
        """
        self._type = type

    @property
    def template_id(self):
        r"""Gets the template_id of this QualityTaskRuleDetailForOpenApi.

        规则模板ID

        :return: The template_id of this QualityTaskRuleDetailForOpenApi.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this QualityTaskRuleDetailForOpenApi.

        规则模板ID

        :param template_id: The template_id of this QualityTaskRuleDetailForOpenApi.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def connection(self):
        r"""Gets the connection of this QualityTaskRuleDetailForOpenApi.

        数据连接ID

        :return: The connection of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this QualityTaskRuleDetailForOpenApi.

        数据连接ID

        :param connection: The connection of this QualityTaskRuleDetailForOpenApi.
        :type connection: str
        """
        self._connection = connection

    @property
    def connection_type(self):
        r"""Gets the connection_type of this QualityTaskRuleDetailForOpenApi.

        数据连接类型

        :return: The connection_type of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this QualityTaskRuleDetailForOpenApi.

        数据连接类型

        :param connection_type: The connection_type of this QualityTaskRuleDetailForOpenApi.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def databases(self):
        r"""Gets the databases of this QualityTaskRuleDetailForOpenApi.

        数据库名，当存在多个值时以逗号分隔

        :return: The databases of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this QualityTaskRuleDetailForOpenApi.

        数据库名，当存在多个值时以逗号分隔

        :param databases: The databases of this QualityTaskRuleDetailForOpenApi.
        :type databases: str
        """
        self._databases = databases

    @property
    def sql(self):
        r"""Gets the sql of this QualityTaskRuleDetailForOpenApi.

        自定义规则中的SQL脚本，系统内置规则时返回

        :return: The sql of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this QualityTaskRuleDetailForOpenApi.

        自定义规则中的SQL脚本，系统内置规则时返回

        :param sql: The sql of this QualityTaskRuleDetailForOpenApi.
        :type sql: str
        """
        self._sql = sql

    @property
    def tables(self):
        r"""Gets the tables of this QualityTaskRuleDetailForOpenApi.

        表名，当存在多个值时以逗号分隔

        :return: The tables of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this QualityTaskRuleDetailForOpenApi.

        表名，当存在多个值时以逗号分隔

        :param tables: The tables of this QualityTaskRuleDetailForOpenApi.
        :type tables: str
        """
        self._tables = tables

    @property
    def reference_tables(self):
        r"""Gets the reference_tables of this QualityTaskRuleDetailForOpenApi.

        跨字段规则中的参考表名，当存在多个值时以逗号分隔

        :return: The reference_tables of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._reference_tables

    @reference_tables.setter
    def reference_tables(self, reference_tables):
        r"""Sets the reference_tables of this QualityTaskRuleDetailForOpenApi.

        跨字段规则中的参考表名，当存在多个值时以逗号分隔

        :param reference_tables: The reference_tables of this QualityTaskRuleDetailForOpenApi.
        :type reference_tables: str
        """
        self._reference_tables = reference_tables

    @property
    def columns(self):
        r"""Gets the columns of this QualityTaskRuleDetailForOpenApi.

        字段名，当存在多个值时以逗号分隔

        :return: The columns of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this QualityTaskRuleDetailForOpenApi.

        字段名，当存在多个值时以逗号分隔

        :param columns: The columns of this QualityTaskRuleDetailForOpenApi.
        :type columns: str
        """
        self._columns = columns

    @property
    def reference_columns(self):
        r"""Gets the reference_columns of this QualityTaskRuleDetailForOpenApi.

        跨字段规则中的参考字段名，当存在多个值时以逗号分隔

        :return: The reference_columns of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._reference_columns

    @reference_columns.setter
    def reference_columns(self, reference_columns):
        r"""Sets the reference_columns of this QualityTaskRuleDetailForOpenApi.

        跨字段规则中的参考字段名，当存在多个值时以逗号分隔

        :param reference_columns: The reference_columns of this QualityTaskRuleDetailForOpenApi.
        :type reference_columns: str
        """
        self._reference_columns = reference_columns

    @property
    def ignore_error(self):
        r"""Gets the ignore_error of this QualityTaskRuleDetailForOpenApi.

        是否忽视规则错误

        :return: The ignore_error of this QualityTaskRuleDetailForOpenApi.
        :rtype: bool
        """
        return self._ignore_error

    @ignore_error.setter
    def ignore_error(self, ignore_error):
        r"""Sets the ignore_error of this QualityTaskRuleDetailForOpenApi.

        是否忽视规则错误

        :param ignore_error: The ignore_error of this QualityTaskRuleDetailForOpenApi.
        :type ignore_error: bool
        """
        self._ignore_error = ignore_error

    @property
    def dimension(self):
        r"""Gets the dimension of this QualityTaskRuleDetailForOpenApi.

        维度

        :return: The dimension of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this QualityTaskRuleDetailForOpenApi.

        维度

        :param dimension: The dimension of this QualityTaskRuleDetailForOpenApi.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def queue(self):
        r"""Gets the queue of this QualityTaskRuleDetailForOpenApi.

        DLI队列

        :return: The queue of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this QualityTaskRuleDetailForOpenApi.

        DLI队列

        :param queue: The queue of this QualityTaskRuleDetailForOpenApi.
        :type queue: str
        """
        self._queue = queue

    @property
    def regular_expression(self):
        r"""Gets the regular_expression of this QualityTaskRuleDetailForOpenApi.

        当规则模板为正则表达式校验时的正则表达式

        :return: The regular_expression of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        r"""Sets the regular_expression of this QualityTaskRuleDetailForOpenApi.

        当规则模板为正则表达式校验时的正则表达式

        :param regular_expression: The regular_expression of this QualityTaskRuleDetailForOpenApi.
        :type regular_expression: str
        """
        self._regular_expression = regular_expression

    @property
    def template_arguments(self):
        r"""Gets the template_arguments of this QualityTaskRuleDetailForOpenApi.

        模板参数

        :return: The template_arguments of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._template_arguments

    @template_arguments.setter
    def template_arguments(self, template_arguments):
        r"""Sets the template_arguments of this QualityTaskRuleDetailForOpenApi.

        模板参数

        :param template_arguments: The template_arguments of this QualityTaskRuleDetailForOpenApi.
        :type template_arguments: str
        """
        self._template_arguments = template_arguments

    @property
    def weight(self):
        r"""Gets the weight of this QualityTaskRuleDetailForOpenApi.

        规则权重

        :return: The weight of this QualityTaskRuleDetailForOpenApi.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this QualityTaskRuleDetailForOpenApi.

        规则权重

        :param weight: The weight of this QualityTaskRuleDetailForOpenApi.
        :type weight: int
        """
        self._weight = weight

    @property
    def calculation_range(self):
        r"""Gets the calculation_range of this QualityTaskRuleDetailForOpenApi.

        计算范围

        :return: The calculation_range of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._calculation_range

    @calculation_range.setter
    def calculation_range(self, calculation_range):
        r"""Sets the calculation_range of this QualityTaskRuleDetailForOpenApi.

        计算范围

        :param calculation_range: The calculation_range of this QualityTaskRuleDetailForOpenApi.
        :type calculation_range: str
        """
        self._calculation_range = calculation_range

    @property
    def calculation_range_sql(self):
        r"""Gets the calculation_range_sql of this QualityTaskRuleDetailForOpenApi.

        计算范围SQL

        :return: The calculation_range_sql of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._calculation_range_sql

    @calculation_range_sql.setter
    def calculation_range_sql(self, calculation_range_sql):
        r"""Sets the calculation_range_sql of this QualityTaskRuleDetailForOpenApi.

        计算范围SQL

        :param calculation_range_sql: The calculation_range_sql of this QualityTaskRuleDetailForOpenApi.
        :type calculation_range_sql: str
        """
        self._calculation_range_sql = calculation_range_sql

    @property
    def alarm_condition(self):
        r"""Gets the alarm_condition of this QualityTaskRuleDetailForOpenApi.

        告警表达式

        :return: The alarm_condition of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._alarm_condition

    @alarm_condition.setter
    def alarm_condition(self, alarm_condition):
        r"""Sets the alarm_condition of this QualityTaskRuleDetailForOpenApi.

        告警表达式

        :param alarm_condition: The alarm_condition of this QualityTaskRuleDetailForOpenApi.
        :type alarm_condition: str
        """
        self._alarm_condition = alarm_condition

    @property
    def export_abnormal_table(self):
        r"""Gets the export_abnormal_table of this QualityTaskRuleDetailForOpenApi.

        是否导出异常数据

        :return: The export_abnormal_table of this QualityTaskRuleDetailForOpenApi.
        :rtype: bool
        """
        return self._export_abnormal_table

    @export_abnormal_table.setter
    def export_abnormal_table(self, export_abnormal_table):
        r"""Sets the export_abnormal_table of this QualityTaskRuleDetailForOpenApi.

        是否导出异常数据

        :param export_abnormal_table: The export_abnormal_table of this QualityTaskRuleDetailForOpenApi.
        :type export_abnormal_table: bool
        """
        self._export_abnormal_table = export_abnormal_table

    @property
    def abnormal_table_database(self):
        r"""Gets the abnormal_table_database of this QualityTaskRuleDetailForOpenApi.

        异常表数据库

        :return: The abnormal_table_database of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_database

    @abnormal_table_database.setter
    def abnormal_table_database(self, abnormal_table_database):
        r"""Sets the abnormal_table_database of this QualityTaskRuleDetailForOpenApi.

        异常表数据库

        :param abnormal_table_database: The abnormal_table_database of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_database: str
        """
        self._abnormal_table_database = abnormal_table_database

    @property
    def abnormal_table_schema(self):
        r"""Gets the abnormal_table_schema of this QualityTaskRuleDetailForOpenApi.

        异常表Schema

        :return: The abnormal_table_schema of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_schema

    @abnormal_table_schema.setter
    def abnormal_table_schema(self, abnormal_table_schema):
        r"""Sets the abnormal_table_schema of this QualityTaskRuleDetailForOpenApi.

        异常表Schema

        :param abnormal_table_schema: The abnormal_table_schema of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_schema: str
        """
        self._abnormal_table_schema = abnormal_table_schema

    @property
    def abnormal_table(self):
        r"""Gets the abnormal_table of this QualityTaskRuleDetailForOpenApi.

        异常字段所在的表

        :return: The abnormal_table of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table

    @abnormal_table.setter
    def abnormal_table(self, abnormal_table):
        r"""Sets the abnormal_table of this QualityTaskRuleDetailForOpenApi.

        异常字段所在的表

        :param abnormal_table: The abnormal_table of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table: str
        """
        self._abnormal_table = abnormal_table

    @property
    def abnormal_table_prefix(self):
        r"""Gets the abnormal_table_prefix of this QualityTaskRuleDetailForOpenApi.

        异常表前缀

        :return: The abnormal_table_prefix of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_prefix

    @abnormal_table_prefix.setter
    def abnormal_table_prefix(self, abnormal_table_prefix):
        r"""Sets the abnormal_table_prefix of this QualityTaskRuleDetailForOpenApi.

        异常表前缀

        :param abnormal_table_prefix: The abnormal_table_prefix of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_prefix: str
        """
        self._abnormal_table_prefix = abnormal_table_prefix

    @property
    def abnormal_table_suffix(self):
        r"""Gets the abnormal_table_suffix of this QualityTaskRuleDetailForOpenApi.

        异常表后缀

        :return: The abnormal_table_suffix of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_suffix

    @abnormal_table_suffix.setter
    def abnormal_table_suffix(self, abnormal_table_suffix):
        r"""Sets the abnormal_table_suffix of this QualityTaskRuleDetailForOpenApi.

        异常表后缀

        :param abnormal_table_suffix: The abnormal_table_suffix of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_suffix: str
        """
        self._abnormal_table_suffix = abnormal_table_suffix

    @property
    def abnormal_table_columns(self):
        r"""Gets the abnormal_table_columns of this QualityTaskRuleDetailForOpenApi.

        异常字段名，当存在多个值时以逗号分隔

        :return: The abnormal_table_columns of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_columns

    @abnormal_table_columns.setter
    def abnormal_table_columns(self, abnormal_table_columns):
        r"""Sets the abnormal_table_columns of this QualityTaskRuleDetailForOpenApi.

        异常字段名，当存在多个值时以逗号分隔

        :param abnormal_table_columns: The abnormal_table_columns of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_columns: str
        """
        self._abnormal_table_columns = abnormal_table_columns

    @property
    def abnormal_table_sql(self):
        r"""Gets the abnormal_table_sql of this QualityTaskRuleDetailForOpenApi.

        异常表SQL

        :return: The abnormal_table_sql of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._abnormal_table_sql

    @abnormal_table_sql.setter
    def abnormal_table_sql(self, abnormal_table_sql):
        r"""Sets the abnormal_table_sql of this QualityTaskRuleDetailForOpenApi.

        异常表SQL

        :param abnormal_table_sql: The abnormal_table_sql of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_sql: str
        """
        self._abnormal_table_sql = abnormal_table_sql

    @property
    def abnormal_table_out_config(self):
        r"""Gets the abnormal_table_out_config of this QualityTaskRuleDetailForOpenApi.

        异常表是否输出规则配置

        :return: The abnormal_table_out_config of this QualityTaskRuleDetailForOpenApi.
        :rtype: bool
        """
        return self._abnormal_table_out_config

    @abnormal_table_out_config.setter
    def abnormal_table_out_config(self, abnormal_table_out_config):
        r"""Sets the abnormal_table_out_config of this QualityTaskRuleDetailForOpenApi.

        异常表是否输出规则配置

        :param abnormal_table_out_config: The abnormal_table_out_config of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_out_config: bool
        """
        self._abnormal_table_out_config = abnormal_table_out_config

    @property
    def abnormal_table_include_null_value(self):
        r"""Gets the abnormal_table_include_null_value of this QualityTaskRuleDetailForOpenApi.

        异常表是否包含空值

        :return: The abnormal_table_include_null_value of this QualityTaskRuleDetailForOpenApi.
        :rtype: bool
        """
        return self._abnormal_table_include_null_value

    @abnormal_table_include_null_value.setter
    def abnormal_table_include_null_value(self, abnormal_table_include_null_value):
        r"""Sets the abnormal_table_include_null_value of this QualityTaskRuleDetailForOpenApi.

        异常表是否包含空值

        :param abnormal_table_include_null_value: The abnormal_table_include_null_value of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_include_null_value: bool
        """
        self._abnormal_table_include_null_value = abnormal_table_include_null_value

    @property
    def abnormal_table_out_data_number(self):
        r"""Gets the abnormal_table_out_data_number of this QualityTaskRuleDetailForOpenApi.

        异常表输出行数, 0代表全量输出

        :return: The abnormal_table_out_data_number of this QualityTaskRuleDetailForOpenApi.
        :rtype: int
        """
        return self._abnormal_table_out_data_number

    @abnormal_table_out_data_number.setter
    def abnormal_table_out_data_number(self, abnormal_table_out_data_number):
        r"""Sets the abnormal_table_out_data_number of this QualityTaskRuleDetailForOpenApi.

        异常表输出行数, 0代表全量输出

        :param abnormal_table_out_data_number: The abnormal_table_out_data_number of this QualityTaskRuleDetailForOpenApi.
        :type abnormal_table_out_data_number: int
        """
        self._abnormal_table_out_data_number = abnormal_table_out_data_number

    @property
    def score_switch(self):
        r"""Gets the score_switch of this QualityTaskRuleDetailForOpenApi.

        是否开启质量评分

        :return: The score_switch of this QualityTaskRuleDetailForOpenApi.
        :rtype: bool
        """
        return self._score_switch

    @score_switch.setter
    def score_switch(self, score_switch):
        r"""Sets the score_switch of this QualityTaskRuleDetailForOpenApi.

        是否开启质量评分

        :param score_switch: The score_switch of this QualityTaskRuleDetailForOpenApi.
        :type score_switch: bool
        """
        self._score_switch = score_switch

    @property
    def score_schema(self):
        r"""Gets the score_schema of this QualityTaskRuleDetailForOpenApi.

        质量评分表所在schema

        :return: The score_schema of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._score_schema

    @score_schema.setter
    def score_schema(self, score_schema):
        r"""Sets the score_schema of this QualityTaskRuleDetailForOpenApi.

        质量评分表所在schema

        :param score_schema: The score_schema of this QualityTaskRuleDetailForOpenApi.
        :type score_schema: str
        """
        self._score_schema = score_schema

    @property
    def score_table(self):
        r"""Gets the score_table of this QualityTaskRuleDetailForOpenApi.

        质量评分表名

        :return: The score_table of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._score_table

    @score_table.setter
    def score_table(self, score_table):
        r"""Sets the score_table of this QualityTaskRuleDetailForOpenApi.

        质量评分表名

        :param score_table: The score_table of this QualityTaskRuleDetailForOpenApi.
        :type score_table: str
        """
        self._score_table = score_table

    @property
    def score_expression(self):
        r"""Gets the score_expression of this QualityTaskRuleDetailForOpenApi.

        质量评分表达式

        :return: The score_expression of this QualityTaskRuleDetailForOpenApi.
        :rtype: str
        """
        return self._score_expression

    @score_expression.setter
    def score_expression(self, score_expression):
        r"""Sets the score_expression of this QualityTaskRuleDetailForOpenApi.

        质量评分表达式

        :param score_expression: The score_expression of this QualityTaskRuleDetailForOpenApi.
        :type score_expression: str
        """
        self._score_expression = score_expression

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
        if not isinstance(other, QualityTaskRuleDetailForOpenApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
