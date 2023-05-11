# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueRecordV4Details:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_property': 'str',
        'old_value': 'str',
        'new_value': 'str',
        'operation': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        '_property': 'property',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'operation': 'operation',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, _property=None, old_value=None, new_value=None, operation=None, id=None, name=None):
        """IssueRecordV4Details

        The model defined in huaweicloud sdk

        :param _property: 操作属性
        :type _property: str
        :param old_value: 上次的记录
        :type old_value: str
        :param new_value: 当前值
        :type new_value: str
        :param operation: 操作
        :type operation: str
        :param id: 操作记录的id
        :type id: int
        :param name: 操作的字段
        :type name: str
        """
        
        

        self.__property = None
        self._old_value = None
        self._new_value = None
        self._operation = None
        self._id = None
        self._name = None
        self.discriminator = None

        if _property is not None:
            self._property = _property
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
        if operation is not None:
            self.operation = operation
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def _property(self):
        """Gets the _property of this IssueRecordV4Details.

        操作属性

        :return: The _property of this IssueRecordV4Details.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this IssueRecordV4Details.

        操作属性

        :param _property: The _property of this IssueRecordV4Details.
        :type _property: str
        """
        self.__property = _property

    @property
    def old_value(self):
        """Gets the old_value of this IssueRecordV4Details.

        上次的记录

        :return: The old_value of this IssueRecordV4Details.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this IssueRecordV4Details.

        上次的记录

        :param old_value: The old_value of this IssueRecordV4Details.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """Gets the new_value of this IssueRecordV4Details.

        当前值

        :return: The new_value of this IssueRecordV4Details.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this IssueRecordV4Details.

        当前值

        :param new_value: The new_value of this IssueRecordV4Details.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def operation(self):
        """Gets the operation of this IssueRecordV4Details.

        操作

        :return: The operation of this IssueRecordV4Details.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IssueRecordV4Details.

        操作

        :param operation: The operation of this IssueRecordV4Details.
        :type operation: str
        """
        self._operation = operation

    @property
    def id(self):
        """Gets the id of this IssueRecordV4Details.

        操作记录的id

        :return: The id of this IssueRecordV4Details.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueRecordV4Details.

        操作记录的id

        :param id: The id of this IssueRecordV4Details.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this IssueRecordV4Details.

        操作的字段

        :return: The name of this IssueRecordV4Details.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueRecordV4Details.

        操作的字段

        :param name: The name of this IssueRecordV4Details.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, IssueRecordV4Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
