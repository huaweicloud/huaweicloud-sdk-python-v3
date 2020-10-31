# coding: utf-8

import pprint
import re

import six





class MappingResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'links': 'LinksSelf',
        'rules': 'list[MappingRules]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'rules': 'rules'
    }

    def __init__(self, id=None, links=None, rules=None):
        """MappingResult - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._links = None
        self._rules = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.rules = rules

    @property
    def id(self):
        """Gets the id of this MappingResult.

        映射ID。

        :return: The id of this MappingResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MappingResult.

        映射ID。

        :param id: The id of this MappingResult.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this MappingResult.


        :return: The links of this MappingResult.
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MappingResult.


        :param links: The links of this MappingResult.
        :type: LinksSelf
        """
        self._links = links

    @property
    def rules(self):
        """Gets the rules of this MappingResult.

        将联邦用户映射为本地用户的规则列表。

        :return: The rules of this MappingResult.
        :rtype: list[MappingRules]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this MappingResult.

        将联邦用户映射为本地用户的规则列表。

        :param rules: The rules of this MappingResult.
        :type: list[MappingRules]
        """
        self._rules = rules

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
        if not isinstance(other, MappingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
