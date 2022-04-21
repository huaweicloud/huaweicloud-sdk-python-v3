# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronShowFirewallPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_policy_id': 'str'
    }

    attribute_map = {
        'firewall_policy_id': 'firewall_policy_id'
    }

    def __init__(self, firewall_policy_id=None):
        """NeutronShowFirewallPolicyRequest

        The model defined in huaweicloud sdk

        :param firewall_policy_id: 网络ACL防火墙策略ID
        :type firewall_policy_id: str
        """
        
        

        self._firewall_policy_id = None
        self.discriminator = None

        self.firewall_policy_id = firewall_policy_id

    @property
    def firewall_policy_id(self):
        """Gets the firewall_policy_id of this NeutronShowFirewallPolicyRequest.

        网络ACL防火墙策略ID

        :return: The firewall_policy_id of this NeutronShowFirewallPolicyRequest.
        :rtype: str
        """
        return self._firewall_policy_id

    @firewall_policy_id.setter
    def firewall_policy_id(self, firewall_policy_id):
        """Sets the firewall_policy_id of this NeutronShowFirewallPolicyRequest.

        网络ACL防火墙策略ID

        :param firewall_policy_id: The firewall_policy_id of this NeutronShowFirewallPolicyRequest.
        :type firewall_policy_id: str
        """
        self._firewall_policy_id = firewall_policy_id

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
        if not isinstance(other, NeutronShowFirewallPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
