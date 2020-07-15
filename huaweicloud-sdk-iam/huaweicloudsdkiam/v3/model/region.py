# coding: utf-8

import pprint
import re

import six





class Region:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'parent_region_id': 'str',
        'links': 'LinksSelf',
        'locales': 'RegionLocales',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'parent_region_id': 'parent_region_id',
        'links': 'links',
        'locales': 'locales',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, description=None, parent_region_id=None, links=None, locales=None, id=None, type=None):
        """Region - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._parent_region_id = None
        self._links = None
        self._locales = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.parent_region_id = parent_region_id
        self.links = links
        self.locales = locales
        self.id = id
        self.type = type

    @property
    def description(self):
        """Gets the description of this Region.

        区域描述信息。

        :return: The description of this Region.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Region.

        区域描述信息。

        :param description: The description of this Region.
        :type: str
        """
        self._description = description

    @property
    def parent_region_id(self):
        """Gets the parent_region_id of this Region.

        null.

        :return: The parent_region_id of this Region.
        :rtype: str
        """
        return self._parent_region_id

    @parent_region_id.setter
    def parent_region_id(self, parent_region_id):
        """Sets the parent_region_id of this Region.

        null.

        :param parent_region_id: The parent_region_id of this Region.
        :type: str
        """
        self._parent_region_id = parent_region_id

    @property
    def links(self):
        """Gets the links of this Region.


        :return: The links of this Region.
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Region.


        :param links: The links of this Region.
        :type: LinksSelf
        """
        self._links = links

    @property
    def locales(self):
        """Gets the locales of this Region.


        :return: The locales of this Region.
        :rtype: RegionLocales
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this Region.


        :param locales: The locales of this Region.
        :type: RegionLocales
        """
        self._locales = locales

    @property
    def id(self):
        """Gets the id of this Region.

        区域ID。

        :return: The id of this Region.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.

        区域ID。

        :param id: The id of this Region.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Region.

        区域类型。

        :return: The type of this Region.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Region.

        区域类型。

        :param type: The type of this Region.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
