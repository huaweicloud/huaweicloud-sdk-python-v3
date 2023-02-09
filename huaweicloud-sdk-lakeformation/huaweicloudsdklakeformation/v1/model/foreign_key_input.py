# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForeignKeyInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_key_database_name': 'str',
        'parent_key_table_name': 'str',
        'parent_key_column_name': 'str',
        'parent_key_name': 'str',
        'foreign_key_column_name': 'str',
        'foreign_key_name': 'str',
        'delete_rule': 'int',
        'enable_constraint': 'bool',
        'key_sequence': 'int',
        'rely_constraint': 'bool',
        'update_rule': 'int',
        'validate_constraint': 'bool'
    }

    attribute_map = {
        'parent_key_database_name': 'parent_key_database_name',
        'parent_key_table_name': 'parent_key_table_name',
        'parent_key_column_name': 'parent_key_column_name',
        'parent_key_name': 'parent_key_name',
        'foreign_key_column_name': 'foreign_key_column_name',
        'foreign_key_name': 'foreign_key_name',
        'delete_rule': 'delete_rule',
        'enable_constraint': 'enable_constraint',
        'key_sequence': 'key_sequence',
        'rely_constraint': 'rely_constraint',
        'update_rule': 'update_rule',
        'validate_constraint': 'validate_constraint'
    }

    def __init__(self, parent_key_database_name=None, parent_key_table_name=None, parent_key_column_name=None, parent_key_name=None, foreign_key_column_name=None, foreign_key_name=None, delete_rule=None, enable_constraint=None, key_sequence=None, rely_constraint=None, update_rule=None, validate_constraint=None):
        """ForeignKeyInput

        The model defined in huaweicloud sdk

        :param parent_key_database_name: 被引用表的数据库名
        :type parent_key_database_name: str
        :param parent_key_table_name: 被引用表的表名
        :type parent_key_table_name: str
        :param parent_key_column_name: 被引用列名
        :type parent_key_column_name: str
        :param parent_key_name: 被引用键名称
        :type parent_key_name: str
        :param foreign_key_column_name: 引用列名
        :type foreign_key_column_name: str
        :param foreign_key_name: 外键名称
        :type foreign_key_name: str
        :param delete_rule: 当被引用表中被引用的记录被删除，本表中对应记录的删除规则
        :type delete_rule: int
        :param enable_constraint: 外键是否启用
        :type enable_constraint: bool
        :param key_sequence: 外键排列规则
        :type key_sequence: int
        :param rely_constraint: is foreign Key rely
        :type rely_constraint: bool
        :param update_rule: 当被引用表中被引用的记录被修改，本表中对应记录的更新规则
        :type update_rule: int
        :param validate_constraint: 外键是否可用
        :type validate_constraint: bool
        """
        
        

        self._parent_key_database_name = None
        self._parent_key_table_name = None
        self._parent_key_column_name = None
        self._parent_key_name = None
        self._foreign_key_column_name = None
        self._foreign_key_name = None
        self._delete_rule = None
        self._enable_constraint = None
        self._key_sequence = None
        self._rely_constraint = None
        self._update_rule = None
        self._validate_constraint = None
        self.discriminator = None

        self.parent_key_database_name = parent_key_database_name
        self.parent_key_table_name = parent_key_table_name
        self.parent_key_column_name = parent_key_column_name
        self.parent_key_name = parent_key_name
        self.foreign_key_column_name = foreign_key_column_name
        self.foreign_key_name = foreign_key_name
        self.delete_rule = delete_rule
        self.enable_constraint = enable_constraint
        self.key_sequence = key_sequence
        self.rely_constraint = rely_constraint
        self.update_rule = update_rule
        self.validate_constraint = validate_constraint

    @property
    def parent_key_database_name(self):
        """Gets the parent_key_database_name of this ForeignKeyInput.

        被引用表的数据库名

        :return: The parent_key_database_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._parent_key_database_name

    @parent_key_database_name.setter
    def parent_key_database_name(self, parent_key_database_name):
        """Sets the parent_key_database_name of this ForeignKeyInput.

        被引用表的数据库名

        :param parent_key_database_name: The parent_key_database_name of this ForeignKeyInput.
        :type parent_key_database_name: str
        """
        self._parent_key_database_name = parent_key_database_name

    @property
    def parent_key_table_name(self):
        """Gets the parent_key_table_name of this ForeignKeyInput.

        被引用表的表名

        :return: The parent_key_table_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._parent_key_table_name

    @parent_key_table_name.setter
    def parent_key_table_name(self, parent_key_table_name):
        """Sets the parent_key_table_name of this ForeignKeyInput.

        被引用表的表名

        :param parent_key_table_name: The parent_key_table_name of this ForeignKeyInput.
        :type parent_key_table_name: str
        """
        self._parent_key_table_name = parent_key_table_name

    @property
    def parent_key_column_name(self):
        """Gets the parent_key_column_name of this ForeignKeyInput.

        被引用列名

        :return: The parent_key_column_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._parent_key_column_name

    @parent_key_column_name.setter
    def parent_key_column_name(self, parent_key_column_name):
        """Sets the parent_key_column_name of this ForeignKeyInput.

        被引用列名

        :param parent_key_column_name: The parent_key_column_name of this ForeignKeyInput.
        :type parent_key_column_name: str
        """
        self._parent_key_column_name = parent_key_column_name

    @property
    def parent_key_name(self):
        """Gets the parent_key_name of this ForeignKeyInput.

        被引用键名称

        :return: The parent_key_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._parent_key_name

    @parent_key_name.setter
    def parent_key_name(self, parent_key_name):
        """Sets the parent_key_name of this ForeignKeyInput.

        被引用键名称

        :param parent_key_name: The parent_key_name of this ForeignKeyInput.
        :type parent_key_name: str
        """
        self._parent_key_name = parent_key_name

    @property
    def foreign_key_column_name(self):
        """Gets the foreign_key_column_name of this ForeignKeyInput.

        引用列名

        :return: The foreign_key_column_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._foreign_key_column_name

    @foreign_key_column_name.setter
    def foreign_key_column_name(self, foreign_key_column_name):
        """Sets the foreign_key_column_name of this ForeignKeyInput.

        引用列名

        :param foreign_key_column_name: The foreign_key_column_name of this ForeignKeyInput.
        :type foreign_key_column_name: str
        """
        self._foreign_key_column_name = foreign_key_column_name

    @property
    def foreign_key_name(self):
        """Gets the foreign_key_name of this ForeignKeyInput.

        外键名称

        :return: The foreign_key_name of this ForeignKeyInput.
        :rtype: str
        """
        return self._foreign_key_name

    @foreign_key_name.setter
    def foreign_key_name(self, foreign_key_name):
        """Sets the foreign_key_name of this ForeignKeyInput.

        外键名称

        :param foreign_key_name: The foreign_key_name of this ForeignKeyInput.
        :type foreign_key_name: str
        """
        self._foreign_key_name = foreign_key_name

    @property
    def delete_rule(self):
        """Gets the delete_rule of this ForeignKeyInput.

        当被引用表中被引用的记录被删除，本表中对应记录的删除规则

        :return: The delete_rule of this ForeignKeyInput.
        :rtype: int
        """
        return self._delete_rule

    @delete_rule.setter
    def delete_rule(self, delete_rule):
        """Sets the delete_rule of this ForeignKeyInput.

        当被引用表中被引用的记录被删除，本表中对应记录的删除规则

        :param delete_rule: The delete_rule of this ForeignKeyInput.
        :type delete_rule: int
        """
        self._delete_rule = delete_rule

    @property
    def enable_constraint(self):
        """Gets the enable_constraint of this ForeignKeyInput.

        外键是否启用

        :return: The enable_constraint of this ForeignKeyInput.
        :rtype: bool
        """
        return self._enable_constraint

    @enable_constraint.setter
    def enable_constraint(self, enable_constraint):
        """Sets the enable_constraint of this ForeignKeyInput.

        外键是否启用

        :param enable_constraint: The enable_constraint of this ForeignKeyInput.
        :type enable_constraint: bool
        """
        self._enable_constraint = enable_constraint

    @property
    def key_sequence(self):
        """Gets the key_sequence of this ForeignKeyInput.

        外键排列规则

        :return: The key_sequence of this ForeignKeyInput.
        :rtype: int
        """
        return self._key_sequence

    @key_sequence.setter
    def key_sequence(self, key_sequence):
        """Sets the key_sequence of this ForeignKeyInput.

        外键排列规则

        :param key_sequence: The key_sequence of this ForeignKeyInput.
        :type key_sequence: int
        """
        self._key_sequence = key_sequence

    @property
    def rely_constraint(self):
        """Gets the rely_constraint of this ForeignKeyInput.

        is foreign Key rely

        :return: The rely_constraint of this ForeignKeyInput.
        :rtype: bool
        """
        return self._rely_constraint

    @rely_constraint.setter
    def rely_constraint(self, rely_constraint):
        """Sets the rely_constraint of this ForeignKeyInput.

        is foreign Key rely

        :param rely_constraint: The rely_constraint of this ForeignKeyInput.
        :type rely_constraint: bool
        """
        self._rely_constraint = rely_constraint

    @property
    def update_rule(self):
        """Gets the update_rule of this ForeignKeyInput.

        当被引用表中被引用的记录被修改，本表中对应记录的更新规则

        :return: The update_rule of this ForeignKeyInput.
        :rtype: int
        """
        return self._update_rule

    @update_rule.setter
    def update_rule(self, update_rule):
        """Sets the update_rule of this ForeignKeyInput.

        当被引用表中被引用的记录被修改，本表中对应记录的更新规则

        :param update_rule: The update_rule of this ForeignKeyInput.
        :type update_rule: int
        """
        self._update_rule = update_rule

    @property
    def validate_constraint(self):
        """Gets the validate_constraint of this ForeignKeyInput.

        外键是否可用

        :return: The validate_constraint of this ForeignKeyInput.
        :rtype: bool
        """
        return self._validate_constraint

    @validate_constraint.setter
    def validate_constraint(self, validate_constraint):
        """Sets the validate_constraint of this ForeignKeyInput.

        外键是否可用

        :param validate_constraint: The validate_constraint of this ForeignKeyInput.
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
        if not isinstance(other, ForeignKeyInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
