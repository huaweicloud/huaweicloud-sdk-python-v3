# coding: utf-8

import pprint
import re

import six





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
        'operation': 'str'
    }

    attribute_map = {
        '_property': 'property',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'operation': 'operation'
    }

    def __init__(self, _property=None, old_value=None, new_value=None, operation=None):
        """IssueRecordV4Details - a model defined in huaweicloud sdk"""
        
        

        self.__property = None
        self._old_value = None
        self._new_value = None
        self._operation = None
        self.discriminator = None

        if _property is not None:
            self._property = _property
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
        if operation is not None:
            self.operation = operation

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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._operation = operation

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueRecordV4Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
