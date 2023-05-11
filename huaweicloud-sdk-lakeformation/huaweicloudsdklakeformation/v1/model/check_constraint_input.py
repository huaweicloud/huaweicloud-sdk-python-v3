# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckConstraintInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'constraint_name': 'str',
        'check_expression': 'str',
        'enable_constraint': 'bool',
        'rely_constraint': 'bool',
        'validate_constraint': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'constraint_name': 'constraint_name',
        'check_expression': 'check_expression',
        'enable_constraint': 'enable_constraint',
        'rely_constraint': 'rely_constraint',
        'validate_constraint': 'validate_constraint'
    }

    def __init__(self, column_name=None, constraint_name=None, check_expression=None, enable_constraint=None, rely_constraint=None, validate_constraint=None):
        """CheckConstraintInput

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param constraint_name: constraint Name
        :type constraint_name: str
        :param check_expression: 检查条件表达式
        :type check_expression: str
        :param enable_constraint: enable constraint
        :type enable_constraint: bool
        :param rely_constraint: constraint is rely when Query
        :type rely_constraint: bool
        :param validate_constraint: constraint is validated
        :type validate_constraint: bool
        """
        
        

        self._column_name = None
        self._constraint_name = None
        self._check_expression = None
        self._enable_constraint = None
        self._rely_constraint = None
        self._validate_constraint = None
        self.discriminator = None

        self.column_name = column_name
        self.constraint_name = constraint_name
        if check_expression is not None:
            self.check_expression = check_expression
        self.enable_constraint = enable_constraint
        self.rely_constraint = rely_constraint
        self.validate_constraint = validate_constraint

    @property
    def column_name(self):
        """Gets the column_name of this CheckConstraintInput.

        列名

        :return: The column_name of this CheckConstraintInput.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this CheckConstraintInput.

        列名

        :param column_name: The column_name of this CheckConstraintInput.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def constraint_name(self):
        """Gets the constraint_name of this CheckConstraintInput.

        constraint Name

        :return: The constraint_name of this CheckConstraintInput.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """Sets the constraint_name of this CheckConstraintInput.

        constraint Name

        :param constraint_name: The constraint_name of this CheckConstraintInput.
        :type constraint_name: str
        """
        self._constraint_name = constraint_name

    @property
    def check_expression(self):
        """Gets the check_expression of this CheckConstraintInput.

        检查条件表达式

        :return: The check_expression of this CheckConstraintInput.
        :rtype: str
        """
        return self._check_expression

    @check_expression.setter
    def check_expression(self, check_expression):
        """Sets the check_expression of this CheckConstraintInput.

        检查条件表达式

        :param check_expression: The check_expression of this CheckConstraintInput.
        :type check_expression: str
        """
        self._check_expression = check_expression

    @property
    def enable_constraint(self):
        """Gets the enable_constraint of this CheckConstraintInput.

        enable constraint

        :return: The enable_constraint of this CheckConstraintInput.
        :rtype: bool
        """
        return self._enable_constraint

    @enable_constraint.setter
    def enable_constraint(self, enable_constraint):
        """Sets the enable_constraint of this CheckConstraintInput.

        enable constraint

        :param enable_constraint: The enable_constraint of this CheckConstraintInput.
        :type enable_constraint: bool
        """
        self._enable_constraint = enable_constraint

    @property
    def rely_constraint(self):
        """Gets the rely_constraint of this CheckConstraintInput.

        constraint is rely when Query

        :return: The rely_constraint of this CheckConstraintInput.
        :rtype: bool
        """
        return self._rely_constraint

    @rely_constraint.setter
    def rely_constraint(self, rely_constraint):
        """Sets the rely_constraint of this CheckConstraintInput.

        constraint is rely when Query

        :param rely_constraint: The rely_constraint of this CheckConstraintInput.
        :type rely_constraint: bool
        """
        self._rely_constraint = rely_constraint

    @property
    def validate_constraint(self):
        """Gets the validate_constraint of this CheckConstraintInput.

        constraint is validated

        :return: The validate_constraint of this CheckConstraintInput.
        :rtype: bool
        """
        return self._validate_constraint

    @validate_constraint.setter
    def validate_constraint(self, validate_constraint):
        """Sets the validate_constraint of this CheckConstraintInput.

        constraint is validated

        :param validate_constraint: The validate_constraint of this CheckConstraintInput.
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
        if not isinstance(other, CheckConstraintInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
