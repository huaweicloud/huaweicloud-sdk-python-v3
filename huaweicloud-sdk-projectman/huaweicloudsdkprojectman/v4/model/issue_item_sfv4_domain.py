# coding: utf-8

import pprint
import re

import six





class IssueItemSFV4Domain:


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
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, name=None):
        """IssueItemSFV4Domain - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this IssueItemSFV4Domain.

        领域id

        :return: The id of this IssueItemSFV4Domain.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IssueItemSFV4Domain.

        领域id

        :param id: The id of this IssueItemSFV4Domain.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this IssueItemSFV4Domain.

        领域

        :return: The name of this IssueItemSFV4Domain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueItemSFV4Domain.

        领域

        :param name: The name of this IssueItemSFV4Domain.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IssueItemSFV4Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
