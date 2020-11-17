# coding: utf-8

import pprint
import re

import six





class BatchCreateDnatRulesRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dnat_rules': 'list[CreateNatGatewayDnatOption]'
    }

    attribute_map = {
        'dnat_rules': 'dnat_rules'
    }

    def __init__(self, dnat_rules=None):
        """BatchCreateDnatRulesRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._dnat_rules = None
        self.discriminator = None

        self.dnat_rules = dnat_rules

    @property
    def dnat_rules(self):
        """Gets the dnat_rules of this BatchCreateDnatRulesRequestBody.

        DNAT规则批量创建对象的请求体。

        :return: The dnat_rules of this BatchCreateDnatRulesRequestBody.
        :rtype: list[CreateNatGatewayDnatOption]
        """
        return self._dnat_rules

    @dnat_rules.setter
    def dnat_rules(self, dnat_rules):
        """Sets the dnat_rules of this BatchCreateDnatRulesRequestBody.

        DNAT规则批量创建对象的请求体。

        :param dnat_rules: The dnat_rules of this BatchCreateDnatRulesRequestBody.
        :type: list[CreateNatGatewayDnatOption]
        """
        self._dnat_rules = dnat_rules

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
        if not isinstance(other, BatchCreateDnatRulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
