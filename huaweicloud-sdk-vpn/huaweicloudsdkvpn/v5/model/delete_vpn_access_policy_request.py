# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVpnAccessPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_server_id': 'str',
        'policy_id': 'str'
    }

    attribute_map = {
        'vpn_server_id': 'vpn_server_id',
        'policy_id': 'policy_id'
    }

    def __init__(self, vpn_server_id=None, policy_id=None):
        """DeleteVpnAccessPolicyRequest

        The model defined in huaweicloud sdk

        :param vpn_server_id: VPN服务端 ID
        :type vpn_server_id: str
        :param policy_id: VPN访问策略ID
        :type policy_id: str
        """
        
        

        self._vpn_server_id = None
        self._policy_id = None
        self.discriminator = None

        self.vpn_server_id = vpn_server_id
        self.policy_id = policy_id

    @property
    def vpn_server_id(self):
        """Gets the vpn_server_id of this DeleteVpnAccessPolicyRequest.

        VPN服务端 ID

        :return: The vpn_server_id of this DeleteVpnAccessPolicyRequest.
        :rtype: str
        """
        return self._vpn_server_id

    @vpn_server_id.setter
    def vpn_server_id(self, vpn_server_id):
        """Sets the vpn_server_id of this DeleteVpnAccessPolicyRequest.

        VPN服务端 ID

        :param vpn_server_id: The vpn_server_id of this DeleteVpnAccessPolicyRequest.
        :type vpn_server_id: str
        """
        self._vpn_server_id = vpn_server_id

    @property
    def policy_id(self):
        """Gets the policy_id of this DeleteVpnAccessPolicyRequest.

        VPN访问策略ID

        :return: The policy_id of this DeleteVpnAccessPolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this DeleteVpnAccessPolicyRequest.

        VPN访问策略ID

        :param policy_id: The policy_id of this DeleteVpnAccessPolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, DeleteVpnAccessPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
