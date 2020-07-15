# coding: utf-8

import pprint
import re

import six





class Catalog:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[CatalogEndpoints]',
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, endpoints=None, id=None, name=None, type=None):
        """Catalog - a model defined in huaweicloud sdk"""
        
        

        self._endpoints = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        self.endpoints = endpoints
        self.id = id
        self.name = name
        self.type = type

    @property
    def endpoints(self):
        """Gets the endpoints of this Catalog.

        终端节点信息。

        :return: The endpoints of this Catalog.
        :rtype: list[CatalogEndpoints]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Catalog.

        终端节点信息。

        :param endpoints: The endpoints of this Catalog.
        :type: list[CatalogEndpoints]
        """
        self._endpoints = endpoints

    @property
    def id(self):
        """Gets the id of this Catalog.

        服务ID。

        :return: The id of this Catalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Catalog.

        服务ID。

        :param id: The id of this Catalog.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Catalog.

        服务名。

        :return: The name of this Catalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Catalog.

        服务名。

        :param name: The name of this Catalog.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Catalog.

        服务类型。

        :return: The type of this Catalog.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Catalog.

        服务类型。

        :param type: The type of this Catalog.
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
        if not isinstance(other, Catalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
