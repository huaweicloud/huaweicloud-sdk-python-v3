# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewayDnatRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dnat_rule': 'CreateNatGatewayDnatOption'
    }

    attribute_map = {
        'dnat_rule': 'dnat_rule'
    }

    def __init__(self, dnat_rule=None):
        """CreateNatGatewayDnatRuleOption

        The model defined in huaweicloud sdk

        :param dnat_rule: 
        :type dnat_rule: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatOption`
        """
        
        

        self._dnat_rule = None
        self.discriminator = None

        self.dnat_rule = dnat_rule

    @property
    def dnat_rule(self):
        """Gets the dnat_rule of this CreateNatGatewayDnatRuleOption.

        :return: The dnat_rule of this CreateNatGatewayDnatRuleOption.
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatOption`
        """
        return self._dnat_rule

    @dnat_rule.setter
    def dnat_rule(self, dnat_rule):
        """Sets the dnat_rule of this CreateNatGatewayDnatRuleOption.

        :param dnat_rule: The dnat_rule of this CreateNatGatewayDnatRuleOption.
        :type dnat_rule: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatOption`
        """
        self._dnat_rule = dnat_rule

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateNatGatewayDnatRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
