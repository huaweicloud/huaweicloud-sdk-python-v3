# coding: utf-8

import pprint
import re

import six





class CreateL7ruleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'l7rule': 'CreateL7ruleV2Req'
    }

    attribute_map = {
        'l7rule': 'l7rule'
    }

    def __init__(self, l7rule=None):
        """CreateL7ruleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._l7rule = None
        self.discriminator = None

        self.l7rule = l7rule

    @property
    def l7rule(self):
        """Gets the l7rule of this CreateL7ruleRequestBody.


        :return: The l7rule of this CreateL7ruleRequestBody.
        :rtype: CreateL7ruleV2Req
        """
        return self._l7rule

    @l7rule.setter
    def l7rule(self, l7rule):
        """Sets the l7rule of this CreateL7ruleRequestBody.


        :param l7rule: The l7rule of this CreateL7ruleRequestBody.
        :type: CreateL7ruleV2Req
        """
        self._l7rule = l7rule

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
        if not isinstance(other, CreateL7ruleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
