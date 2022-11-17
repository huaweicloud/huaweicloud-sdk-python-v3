# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFirewallRuleResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'egress_firewall_policy': 'FirewallPolicy',
        'ingress_firewall_policy': 'FirewallPolicy'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'egress_firewall_policy': 'egress_firewall_policy',
        'ingress_firewall_policy': 'ingress_firewall_policy'
    }

    def __init__(self, id=None, status=None, egress_firewall_policy=None, ingress_firewall_policy=None):
        """UpdateFirewallRuleResp

        The model defined in huaweicloud sdk

        :param id: 网络ACL ID
        :type id: str
        :param status: 网络ACL状态。
        :type status: str
        :param egress_firewall_policy: 
        :type egress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        :param ingress_firewall_policy: 
        :type ingress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        
        

        self._id = None
        self._status = None
        self._egress_firewall_policy = None
        self._ingress_firewall_policy = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.egress_firewall_policy = egress_firewall_policy
        self.ingress_firewall_policy = ingress_firewall_policy

    @property
    def id(self):
        """Gets the id of this UpdateFirewallRuleResp.

        网络ACL ID

        :return: The id of this UpdateFirewallRuleResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateFirewallRuleResp.

        网络ACL ID

        :param id: The id of this UpdateFirewallRuleResp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this UpdateFirewallRuleResp.

        网络ACL状态。

        :return: The status of this UpdateFirewallRuleResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateFirewallRuleResp.

        网络ACL状态。

        :param status: The status of this UpdateFirewallRuleResp.
        :type status: str
        """
        self._status = status

    @property
    def egress_firewall_policy(self):
        """Gets the egress_firewall_policy of this UpdateFirewallRuleResp.

        :return: The egress_firewall_policy of this UpdateFirewallRuleResp.
        :rtype: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        return self._egress_firewall_policy

    @egress_firewall_policy.setter
    def egress_firewall_policy(self, egress_firewall_policy):
        """Sets the egress_firewall_policy of this UpdateFirewallRuleResp.

        :param egress_firewall_policy: The egress_firewall_policy of this UpdateFirewallRuleResp.
        :type egress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        self._egress_firewall_policy = egress_firewall_policy

    @property
    def ingress_firewall_policy(self):
        """Gets the ingress_firewall_policy of this UpdateFirewallRuleResp.

        :return: The ingress_firewall_policy of this UpdateFirewallRuleResp.
        :rtype: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        return self._ingress_firewall_policy

    @ingress_firewall_policy.setter
    def ingress_firewall_policy(self, ingress_firewall_policy):
        """Sets the ingress_firewall_policy of this UpdateFirewallRuleResp.

        :param ingress_firewall_policy: The ingress_firewall_policy of this UpdateFirewallRuleResp.
        :type ingress_firewall_policy: :class:`huaweicloudsdkiec.v1.FirewallPolicy`
        """
        self._ingress_firewall_policy = ingress_firewall_policy

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
        if not isinstance(other, UpdateFirewallRuleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
