# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnAccessPolicyRequest:

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
        'policy_id': 'str',
        'body': 'UpdateVpnAccessPolicyRequestBody'
    }

    attribute_map = {
        'vpn_server_id': 'vpn_server_id',
        'policy_id': 'policy_id',
        'body': 'body'
    }

    def __init__(self, vpn_server_id=None, policy_id=None, body=None):
        """UpdateVpnAccessPolicyRequest

        The model defined in huaweicloud sdk

        :param vpn_server_id: VPN服务端 ID
        :type vpn_server_id: str
        :param policy_id: VPN访问策略ID
        :type policy_id: str
        :param body: Body of the UpdateVpnAccessPolicyRequest
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnAccessPolicyRequestBody`
        """
        
        

        self._vpn_server_id = None
        self._policy_id = None
        self._body = None
        self.discriminator = None

        self.vpn_server_id = vpn_server_id
        self.policy_id = policy_id
        if body is not None:
            self.body = body

    @property
    def vpn_server_id(self):
        """Gets the vpn_server_id of this UpdateVpnAccessPolicyRequest.

        VPN服务端 ID

        :return: The vpn_server_id of this UpdateVpnAccessPolicyRequest.
        :rtype: str
        """
        return self._vpn_server_id

    @vpn_server_id.setter
    def vpn_server_id(self, vpn_server_id):
        """Sets the vpn_server_id of this UpdateVpnAccessPolicyRequest.

        VPN服务端 ID

        :param vpn_server_id: The vpn_server_id of this UpdateVpnAccessPolicyRequest.
        :type vpn_server_id: str
        """
        self._vpn_server_id = vpn_server_id

    @property
    def policy_id(self):
        """Gets the policy_id of this UpdateVpnAccessPolicyRequest.

        VPN访问策略ID

        :return: The policy_id of this UpdateVpnAccessPolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this UpdateVpnAccessPolicyRequest.

        VPN访问策略ID

        :param policy_id: The policy_id of this UpdateVpnAccessPolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def body(self):
        """Gets the body of this UpdateVpnAccessPolicyRequest.

        :return: The body of this UpdateVpnAccessPolicyRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnAccessPolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateVpnAccessPolicyRequest.

        :param body: The body of this UpdateVpnAccessPolicyRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnAccessPolicyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateVpnAccessPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
