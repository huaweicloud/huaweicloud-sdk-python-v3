# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoint:
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
        'weight': 'int'
    }

    attribute_map = {
        'name': 'name',
        'weight': 'weight'
    }

    def __init__(self, name=None, weight=None):
        """Endpoint

        The model defined in huaweicloud sdk

        :param name: endpoint name。
        :type name: str
        :param weight: endpoint weight。
        :type weight: int
        """

        self._name = None
        self._weight = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight

    @property
    def name(self):
        """Gets the name of this Endpoint.

         name of endpoint.

        :return: The name of this Endpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Endpoint.

        name of endpoint.

        :param name: The name of this Endpoint.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this Endpoint.

        weight of endpoint.

        :return: The weight of this Endpoint.
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Endpoint.

         weight of endpoint.

        :param weight: The weight of this Endpoint.
        :type weight: int
        """
        self._weight = weight

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
