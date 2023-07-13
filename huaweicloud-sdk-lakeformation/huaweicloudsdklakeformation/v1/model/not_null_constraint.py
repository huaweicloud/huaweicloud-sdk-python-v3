# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotNullConstraint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'constraint_name': 'str',
        'enable_constraint': 'bool',
        'rely_constraint': 'bool',
        'validate_constraint': 'bool'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'constraint_name': 'constraint_name',
        'enable_constraint': 'enable_constraint',
        'rely_constraint': 'rely_constraint',
        'validate_constraint': 'validate_constraint'
    }

    def __init__(self, catalog_name=None, database_name=None, table_name=None, column_name=None, constraint_name=None, enable_constraint=None, rely_constraint=None, validate_constraint=None):
        """NotNullConstraint

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param column_name: 列名
        :type column_name: str
        :param constraint_name: constraint Name
        :type constraint_name: str
        :param enable_constraint: enable constraint
        :type enable_constraint: bool
        :param rely_constraint: constraint is rely when Query
        :type rely_constraint: bool
        :param validate_constraint: constraint is validated
        :type validate_constraint: bool
        """
        
        

        self._catalog_name = None
        self._database_name = None
        self._table_name = None
        self._column_name = None
        self._constraint_name = None
        self._enable_constraint = None
        self._rely_constraint = None
        self._validate_constraint = None
        self.discriminator = None

        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name
        self.column_name = column_name
        self.constraint_name = constraint_name
        self.enable_constraint = enable_constraint
        self.rely_constraint = rely_constraint
        self.validate_constraint = validate_constraint

    @property
    def catalog_name(self):
        """Gets the catalog_name of this NotNullConstraint.

        catalog名字

        :return: The catalog_name of this NotNullConstraint.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this NotNullConstraint.

        catalog名字

        :param catalog_name: The catalog_name of this NotNullConstraint.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this NotNullConstraint.

        数据库名字

        :return: The database_name of this NotNullConstraint.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this NotNullConstraint.

        数据库名字

        :param database_name: The database_name of this NotNullConstraint.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this NotNullConstraint.

        表名称

        :return: The table_name of this NotNullConstraint.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this NotNullConstraint.

        表名称

        :param table_name: The table_name of this NotNullConstraint.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this NotNullConstraint.

        列名

        :return: The column_name of this NotNullConstraint.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this NotNullConstraint.

        列名

        :param column_name: The column_name of this NotNullConstraint.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def constraint_name(self):
        """Gets the constraint_name of this NotNullConstraint.

        constraint Name

        :return: The constraint_name of this NotNullConstraint.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """Sets the constraint_name of this NotNullConstraint.

        constraint Name

        :param constraint_name: The constraint_name of this NotNullConstraint.
        :type constraint_name: str
        """
        self._constraint_name = constraint_name

    @property
    def enable_constraint(self):
        """Gets the enable_constraint of this NotNullConstraint.

        enable constraint

        :return: The enable_constraint of this NotNullConstraint.
        :rtype: bool
        """
        return self._enable_constraint

    @enable_constraint.setter
    def enable_constraint(self, enable_constraint):
        """Sets the enable_constraint of this NotNullConstraint.

        enable constraint

        :param enable_constraint: The enable_constraint of this NotNullConstraint.
        :type enable_constraint: bool
        """
        self._enable_constraint = enable_constraint

    @property
    def rely_constraint(self):
        """Gets the rely_constraint of this NotNullConstraint.

        constraint is rely when Query

        :return: The rely_constraint of this NotNullConstraint.
        :rtype: bool
        """
        return self._rely_constraint

    @rely_constraint.setter
    def rely_constraint(self, rely_constraint):
        """Sets the rely_constraint of this NotNullConstraint.

        constraint is rely when Query

        :param rely_constraint: The rely_constraint of this NotNullConstraint.
        :type rely_constraint: bool
        """
        self._rely_constraint = rely_constraint

    @property
    def validate_constraint(self):
        """Gets the validate_constraint of this NotNullConstraint.

        constraint is validated

        :return: The validate_constraint of this NotNullConstraint.
        :rtype: bool
        """
        return self._validate_constraint

    @validate_constraint.setter
    def validate_constraint(self, validate_constraint):
        """Sets the validate_constraint of this NotNullConstraint.

        constraint is validated

        :param validate_constraint: The validate_constraint of this NotNullConstraint.
        :type validate_constraint: bool
        """
        self._validate_constraint = validate_constraint

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
        if not isinstance(other, NotNullConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
