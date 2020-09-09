# coding: utf-8

import pprint
import re

import six





class ListProductsRespHourly:


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
        'version': 'str',
        'values': 'list[ListProductsRespValues]'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'values': 'values'
    }

    def __init__(self, name=None, version=None, values=None):
        """ListProductsRespHourly - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._version = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this ListProductsRespHourly.

        消息引擎的名称，该字段显示为rabbitmq。

        :return: The name of this ListProductsRespHourly.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProductsRespHourly.

        消息引擎的名称，该字段显示为rabbitmq。

        :param name: The name of this ListProductsRespHourly.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this ListProductsRespHourly.

        消息引擎的版本，当前仅支持3.7.17。

        :return: The version of this ListProductsRespHourly.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListProductsRespHourly.

        消息引擎的版本，当前仅支持3.7.17。

        :param version: The version of this ListProductsRespHourly.
        :type: str
        """
        self._version = version

    @property
    def values(self):
        """Gets the values of this ListProductsRespHourly.

        产品规格列表。

        :return: The values of this ListProductsRespHourly.
        :rtype: list[ListProductsRespValues]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ListProductsRespHourly.

        产品规格列表。

        :param values: The values of this ListProductsRespHourly.
        :type: list[ListProductsRespValues]
        """
        self._values = values

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
        if not isinstance(other, ListProductsRespHourly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
