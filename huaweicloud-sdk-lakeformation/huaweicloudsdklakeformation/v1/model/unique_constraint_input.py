# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UniqueConstraintInput:

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
        'key_sequence': 'int',
        'enable_constraint': 'bool',
        'rely_constraint': 'bool',
        'validate_constraint': 'bool'
    }

    attribute_map = {
        'column_name': 'column_name',
        'constraint_name': 'constraint_name',
        'key_sequence': 'key_sequence',
        'enable_constraint': 'enable_constraint',
        'rely_constraint': 'rely_constraint',
        'validate_constraint': 'validate_constraint'
    }

    def __init__(self, column_name=None, constraint_name=None, key_sequence=None, enable_constraint=None, rely_constraint=None, validate_constraint=None):
        r"""UniqueConstraintInput

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param constraint_name: constraint Name
        :type constraint_name: str
        :param key_sequence: 列序号（限制条件中第几位）
        :type key_sequence: int
        :param enable_constraint: enable constraint
        :type enable_constraint: bool
        :param rely_constraint: constraint is rely when Query
        :type rely_constraint: bool
        :param validate_constraint: constraint is validated
        :type validate_constraint: bool
        """
        
        

        self._column_name = None
        self._constraint_name = None
        self._key_sequence = None
        self._enable_constraint = None
        self._rely_constraint = None
        self._validate_constraint = None
        self.discriminator = None

        self.column_name = column_name
        self.constraint_name = constraint_name
        if key_sequence is not None:
            self.key_sequence = key_sequence
        self.enable_constraint = enable_constraint
        self.rely_constraint = rely_constraint
        self.validate_constraint = validate_constraint

    @property
    def column_name(self):
        r"""Gets the column_name of this UniqueConstraintInput.

        列名

        :return: The column_name of this UniqueConstraintInput.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this UniqueConstraintInput.

        列名

        :param column_name: The column_name of this UniqueConstraintInput.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def constraint_name(self):
        r"""Gets the constraint_name of this UniqueConstraintInput.

        constraint Name

        :return: The constraint_name of this UniqueConstraintInput.
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        r"""Sets the constraint_name of this UniqueConstraintInput.

        constraint Name

        :param constraint_name: The constraint_name of this UniqueConstraintInput.
        :type constraint_name: str
        """
        self._constraint_name = constraint_name

    @property
    def key_sequence(self):
        r"""Gets the key_sequence of this UniqueConstraintInput.

        列序号（限制条件中第几位）

        :return: The key_sequence of this UniqueConstraintInput.
        :rtype: int
        """
        return self._key_sequence

    @key_sequence.setter
    def key_sequence(self, key_sequence):
        r"""Sets the key_sequence of this UniqueConstraintInput.

        列序号（限制条件中第几位）

        :param key_sequence: The key_sequence of this UniqueConstraintInput.
        :type key_sequence: int
        """
        self._key_sequence = key_sequence

    @property
    def enable_constraint(self):
        r"""Gets the enable_constraint of this UniqueConstraintInput.

        enable constraint

        :return: The enable_constraint of this UniqueConstraintInput.
        :rtype: bool
        """
        return self._enable_constraint

    @enable_constraint.setter
    def enable_constraint(self, enable_constraint):
        r"""Sets the enable_constraint of this UniqueConstraintInput.

        enable constraint

        :param enable_constraint: The enable_constraint of this UniqueConstraintInput.
        :type enable_constraint: bool
        """
        self._enable_constraint = enable_constraint

    @property
    def rely_constraint(self):
        r"""Gets the rely_constraint of this UniqueConstraintInput.

        constraint is rely when Query

        :return: The rely_constraint of this UniqueConstraintInput.
        :rtype: bool
        """
        return self._rely_constraint

    @rely_constraint.setter
    def rely_constraint(self, rely_constraint):
        r"""Sets the rely_constraint of this UniqueConstraintInput.

        constraint is rely when Query

        :param rely_constraint: The rely_constraint of this UniqueConstraintInput.
        :type rely_constraint: bool
        """
        self._rely_constraint = rely_constraint

    @property
    def validate_constraint(self):
        r"""Gets the validate_constraint of this UniqueConstraintInput.

        constraint is validated

        :return: The validate_constraint of this UniqueConstraintInput.
        :rtype: bool
        """
        return self._validate_constraint

    @validate_constraint.setter
    def validate_constraint(self, validate_constraint):
        r"""Sets the validate_constraint of this UniqueConstraintInput.

        constraint is validated

        :param validate_constraint: The validate_constraint of this UniqueConstraintInput.
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
        if not isinstance(other, UniqueConstraintInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
