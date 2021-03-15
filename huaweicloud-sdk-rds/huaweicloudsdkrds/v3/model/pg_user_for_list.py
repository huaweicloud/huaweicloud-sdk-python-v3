# coding: utf-8

import pprint
import re

import six





class PgUserForList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'attributes': 'object',
        'memberof': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'attributes': 'attributes',
        'memberof': 'memberof'
    }

    def __init__(self, name=None, attributes=None, memberof=None):
        """PgUserForList - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._attributes = None
        self._memberof = None
        self.discriminator = None

        self.name = name
        if attributes is not None:
            self.attributes = attributes
        if memberof is not None:
            self.memberof = memberof

    @property
    def name(self):
        """Gets the name of this PgUserForList.

        数据库用户名称。

        :return: The name of this PgUserForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PgUserForList.

        数据库用户名称。

        :param name: The name of this PgUserForList.
        :type: str
        """
        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this PgUserForList.

        用户的权限属性。

        :return: The attributes of this PgUserForList.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PgUserForList.

        用户的权限属性。

        :param attributes: The attributes of this PgUserForList.
        :type: object
        """
        self._attributes = attributes

    @property
    def memberof(self):
        """Gets the memberof of this PgUserForList.

        用户的权限属性。

        :return: The memberof of this PgUserForList.
        :rtype: list[str]
        """
        return self._memberof

    @memberof.setter
    def memberof(self, memberof):
        """Sets the memberof of this PgUserForList.

        用户的权限属性。

        :param memberof: The memberof of this PgUserForList.
        :type: list[str]
        """
        self._memberof = memberof

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
        if not isinstance(other, PgUserForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
