# coding: utf-8

import pprint
import re

import six


class NovaSimpleFlavor(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'links': 'list[NovaLink]',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name'
    }

    def __init__(self, id=None, links=None, name=None):  # noqa: E501
        """NovaSimpleFlavor - a model defined in huaweicloud sdk"""

        self._id = None
        self._links = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.name = name

    @property
    def id(self):
        """Gets the id of this NovaSimpleFlavor.

        规格ID。

        :return: The id of this NovaSimpleFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaSimpleFlavor.

        规格ID。

        :param id: The id of this NovaSimpleFlavor.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaSimpleFlavor.

        规格相关快捷链接地址。

        :return: The links of this NovaSimpleFlavor.
        :rtype: list[NovaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaSimpleFlavor.

        规格相关快捷链接地址。

        :param links: The links of this NovaSimpleFlavor.
        :type: list[NovaLink]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this NovaSimpleFlavor.

        规格名称。

        :return: The name of this NovaSimpleFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaSimpleFlavor.

        规格名称。

        :param name: The name of this NovaSimpleFlavor.
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
        if not isinstance(other, NovaSimpleFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
