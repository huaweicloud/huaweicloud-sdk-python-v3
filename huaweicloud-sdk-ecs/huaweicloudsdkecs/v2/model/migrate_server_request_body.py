# coding: utf-8

import pprint
import re

import six


class MigrateServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'migrate': 'MigrateServerOption'
    }

    attribute_map = {
        'migrate': 'migrate'
    }

    def __init__(self, migrate=None):  # noqa: E501
        """MigrateServerRequestBody - a model defined in huaweicloud sdk"""

        self._migrate = None
        self.discriminator = None

        self.migrate = migrate

    @property
    def migrate(self):
        """Gets the migrate of this MigrateServerRequestBody.


        :return: The migrate of this MigrateServerRequestBody.
        :rtype: MigrateServerOption
        """
        return self._migrate

    @migrate.setter
    def migrate(self, migrate):
        """Sets the migrate of this MigrateServerRequestBody.


        :param migrate: The migrate of this MigrateServerRequestBody.
        :type: MigrateServerOption
        """
        self._migrate = migrate

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
        if not isinstance(other, MigrateServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
