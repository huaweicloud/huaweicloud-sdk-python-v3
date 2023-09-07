# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter_conditions': 'list[DataFilteringCondition]',
        'is_batch_process': 'bool',
        'add_columns': 'list[AddColumnInfo]',
        'ddl_operation': 'dict(str, str)',
        'dml_operation': 'str',
        'db_object_column_info': 'DbObjectColumnInfo',
        'db_or_table_rename_rule': 'DbOrTableRenameRule',
        'db_object': 'DbObject',
        'is_synchronized': 'bool'
    }

    attribute_map = {
        'filter_conditions': 'filter_conditions',
        'is_batch_process': 'is_batch_process',
        'add_columns': 'add_columns',
        'ddl_operation': 'ddl_operation',
        'dml_operation': 'dml_operation',
        'db_object_column_info': 'db_object_column_info',
        'db_or_table_rename_rule': 'db_or_table_rename_rule',
        'db_object': 'db_object',
        'is_synchronized': 'is_synchronized'
    }

    def __init__(self, filter_conditions=None, is_batch_process=None, add_columns=None, ddl_operation=None, dml_operation=None, db_object_column_info=None, db_or_table_rename_rule=None, db_object=None, is_synchronized=None):
        """DataProcessInfo

        The model defined in huaweicloud sdk

        :param filter_conditions: 指定任务数据加工规则请求体
        :type filter_conditions: list[:class:`huaweicloudsdkdrs.v5.DataFilteringCondition`]
        :param is_batch_process: 库级、批量表级处理为true，单表操作为false
        :type is_batch_process: bool
        :param add_columns: 附加列 当选择附加列时必须填写 约束：使用多对一操作时，需要使用数据加工的附加列操作来避免数据冲突。
        :type add_columns: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        :param ddl_operation: 支持DDL的语法 选择增量迁移或同步的DDL操作。取值及意思如下： \&quot;table\&quot;: \&quot;CREATE TABLE, ALTER TABLE,DROP TABLE,RENAME TABLE\&quot; 如该值为空，不迁移或同步DDL操作
        :type ddl_operation: dict(str, str)
        :param dml_operation: 支持DML的语法 选择DML操作时，取值如下： i：INSERT。 u：UPDATE。 d：DELETE。 如该值为空，不增量迁移或同步DML操作。
        :type dml_operation: str
        :param db_object_column_info: 
        :type db_object_column_info: :class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`
        :param db_or_table_rename_rule: 
        :type db_or_table_rename_rule: :class:`huaweicloudsdkdrs.v5.DbOrTableRenameRule`
        :param db_object: 
        :type db_object: :class:`huaweicloudsdkdrs.v5.DbObject`
        :param is_synchronized: 表示该规则是否已同步至目标库
        :type is_synchronized: bool
        """
        
        

        self._filter_conditions = None
        self._is_batch_process = None
        self._add_columns = None
        self._ddl_operation = None
        self._dml_operation = None
        self._db_object_column_info = None
        self._db_or_table_rename_rule = None
        self._db_object = None
        self._is_synchronized = None
        self.discriminator = None

        if filter_conditions is not None:
            self.filter_conditions = filter_conditions
        if is_batch_process is not None:
            self.is_batch_process = is_batch_process
        if add_columns is not None:
            self.add_columns = add_columns
        if ddl_operation is not None:
            self.ddl_operation = ddl_operation
        if dml_operation is not None:
            self.dml_operation = dml_operation
        if db_object_column_info is not None:
            self.db_object_column_info = db_object_column_info
        if db_or_table_rename_rule is not None:
            self.db_or_table_rename_rule = db_or_table_rename_rule
        if db_object is not None:
            self.db_object = db_object
        if is_synchronized is not None:
            self.is_synchronized = is_synchronized

    @property
    def filter_conditions(self):
        """Gets the filter_conditions of this DataProcessInfo.

        指定任务数据加工规则请求体

        :return: The filter_conditions of this DataProcessInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataFilteringCondition`]
        """
        return self._filter_conditions

    @filter_conditions.setter
    def filter_conditions(self, filter_conditions):
        """Sets the filter_conditions of this DataProcessInfo.

        指定任务数据加工规则请求体

        :param filter_conditions: The filter_conditions of this DataProcessInfo.
        :type filter_conditions: list[:class:`huaweicloudsdkdrs.v5.DataFilteringCondition`]
        """
        self._filter_conditions = filter_conditions

    @property
    def is_batch_process(self):
        """Gets the is_batch_process of this DataProcessInfo.

        库级、批量表级处理为true，单表操作为false

        :return: The is_batch_process of this DataProcessInfo.
        :rtype: bool
        """
        return self._is_batch_process

    @is_batch_process.setter
    def is_batch_process(self, is_batch_process):
        """Sets the is_batch_process of this DataProcessInfo.

        库级、批量表级处理为true，单表操作为false

        :param is_batch_process: The is_batch_process of this DataProcessInfo.
        :type is_batch_process: bool
        """
        self._is_batch_process = is_batch_process

    @property
    def add_columns(self):
        """Gets the add_columns of this DataProcessInfo.

        附加列 当选择附加列时必须填写 约束：使用多对一操作时，需要使用数据加工的附加列操作来避免数据冲突。

        :return: The add_columns of this DataProcessInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        """
        return self._add_columns

    @add_columns.setter
    def add_columns(self, add_columns):
        """Sets the add_columns of this DataProcessInfo.

        附加列 当选择附加列时必须填写 约束：使用多对一操作时，需要使用数据加工的附加列操作来避免数据冲突。

        :param add_columns: The add_columns of this DataProcessInfo.
        :type add_columns: list[:class:`huaweicloudsdkdrs.v5.AddColumnInfo`]
        """
        self._add_columns = add_columns

    @property
    def ddl_operation(self):
        """Gets the ddl_operation of this DataProcessInfo.

        支持DDL的语法 选择增量迁移或同步的DDL操作。取值及意思如下： \"table\": \"CREATE TABLE, ALTER TABLE,DROP TABLE,RENAME TABLE\" 如该值为空，不迁移或同步DDL操作

        :return: The ddl_operation of this DataProcessInfo.
        :rtype: dict(str, str)
        """
        return self._ddl_operation

    @ddl_operation.setter
    def ddl_operation(self, ddl_operation):
        """Sets the ddl_operation of this DataProcessInfo.

        支持DDL的语法 选择增量迁移或同步的DDL操作。取值及意思如下： \"table\": \"CREATE TABLE, ALTER TABLE,DROP TABLE,RENAME TABLE\" 如该值为空，不迁移或同步DDL操作

        :param ddl_operation: The ddl_operation of this DataProcessInfo.
        :type ddl_operation: dict(str, str)
        """
        self._ddl_operation = ddl_operation

    @property
    def dml_operation(self):
        """Gets the dml_operation of this DataProcessInfo.

        支持DML的语法 选择DML操作时，取值如下： i：INSERT。 u：UPDATE。 d：DELETE。 如该值为空，不增量迁移或同步DML操作。

        :return: The dml_operation of this DataProcessInfo.
        :rtype: str
        """
        return self._dml_operation

    @dml_operation.setter
    def dml_operation(self, dml_operation):
        """Sets the dml_operation of this DataProcessInfo.

        支持DML的语法 选择DML操作时，取值如下： i：INSERT。 u：UPDATE。 d：DELETE。 如该值为空，不增量迁移或同步DML操作。

        :param dml_operation: The dml_operation of this DataProcessInfo.
        :type dml_operation: str
        """
        self._dml_operation = dml_operation

    @property
    def db_object_column_info(self):
        """Gets the db_object_column_info of this DataProcessInfo.

        :return: The db_object_column_info of this DataProcessInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`
        """
        return self._db_object_column_info

    @db_object_column_info.setter
    def db_object_column_info(self, db_object_column_info):
        """Sets the db_object_column_info of this DataProcessInfo.

        :param db_object_column_info: The db_object_column_info of this DataProcessInfo.
        :type db_object_column_info: :class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`
        """
        self._db_object_column_info = db_object_column_info

    @property
    def db_or_table_rename_rule(self):
        """Gets the db_or_table_rename_rule of this DataProcessInfo.

        :return: The db_or_table_rename_rule of this DataProcessInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbOrTableRenameRule`
        """
        return self._db_or_table_rename_rule

    @db_or_table_rename_rule.setter
    def db_or_table_rename_rule(self, db_or_table_rename_rule):
        """Sets the db_or_table_rename_rule of this DataProcessInfo.

        :param db_or_table_rename_rule: The db_or_table_rename_rule of this DataProcessInfo.
        :type db_or_table_rename_rule: :class:`huaweicloudsdkdrs.v5.DbOrTableRenameRule`
        """
        self._db_or_table_rename_rule = db_or_table_rename_rule

    @property
    def db_object(self):
        """Gets the db_object of this DataProcessInfo.

        :return: The db_object of this DataProcessInfo.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        return self._db_object

    @db_object.setter
    def db_object(self, db_object):
        """Sets the db_object of this DataProcessInfo.

        :param db_object: The db_object of this DataProcessInfo.
        :type db_object: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        self._db_object = db_object

    @property
    def is_synchronized(self):
        """Gets the is_synchronized of this DataProcessInfo.

        表示该规则是否已同步至目标库

        :return: The is_synchronized of this DataProcessInfo.
        :rtype: bool
        """
        return self._is_synchronized

    @is_synchronized.setter
    def is_synchronized(self, is_synchronized):
        """Sets the is_synchronized of this DataProcessInfo.

        表示该规则是否已同步至目标库

        :param is_synchronized: The is_synchronized of this DataProcessInfo.
        :type is_synchronized: bool
        """
        self._is_synchronized = is_synchronized

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
        if not isinstance(other, DataProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
