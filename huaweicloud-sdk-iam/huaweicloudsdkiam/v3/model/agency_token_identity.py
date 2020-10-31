# coding: utf-8

import pprint
import re

import six





class AgencyTokenIdentity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'methods': 'list[str]',
        'assume_role': 'AgencyTokenAssumerole'
    }

    attribute_map = {
        'methods': 'methods',
        'assume_role': 'assume_role'
    }

    def __init__(self, methods=None, assume_role=None):
        """AgencyTokenIdentity - a model defined in huaweicloud sdk"""
        
        

        self._methods = None
        self._assume_role = None
        self.discriminator = None

        self.methods = methods
        self.assume_role = assume_role

    @property
    def methods(self):
        """Gets the methods of this AgencyTokenIdentity.

        token的获取方式，该字段内容为[\"assume_role\"]。

        :return: The methods of this AgencyTokenIdentity.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this AgencyTokenIdentity.

        token的获取方式，该字段内容为[\"assume_role\"]。

        :param methods: The methods of this AgencyTokenIdentity.
        :type: list[str]
        """
        self._methods = methods

    @property
    def assume_role(self):
        """Gets the assume_role of this AgencyTokenIdentity.


        :return: The assume_role of this AgencyTokenIdentity.
        :rtype: AgencyTokenAssumerole
        """
        return self._assume_role

    @assume_role.setter
    def assume_role(self, assume_role):
        """Sets the assume_role of this AgencyTokenIdentity.


        :param assume_role: The assume_role of this AgencyTokenIdentity.
        :type: AgencyTokenAssumerole
        """
        self._assume_role = assume_role

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
        if not isinstance(other, AgencyTokenIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
