# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyCentralNetworkPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'central_network_id': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'central_network_id': 'central_network_id'
    }

    def __init__(self, policy_id=None, central_network_id=None):
        """ApplyCentralNetworkPolicyRequest

        The model defined in huaweicloud sdk

        :param policy_id: 网络策略ID。
        :type policy_id: str
        :param central_network_id: 中心网络的ID。
        :type central_network_id: str
        """
        
        

        self._policy_id = None
        self._central_network_id = None
        self.discriminator = None

        self.policy_id = policy_id
        self.central_network_id = central_network_id

    @property
    def policy_id(self):
        """Gets the policy_id of this ApplyCentralNetworkPolicyRequest.

        网络策略ID。

        :return: The policy_id of this ApplyCentralNetworkPolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ApplyCentralNetworkPolicyRequest.

        网络策略ID。

        :param policy_id: The policy_id of this ApplyCentralNetworkPolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def central_network_id(self):
        """Gets the central_network_id of this ApplyCentralNetworkPolicyRequest.

        中心网络的ID。

        :return: The central_network_id of this ApplyCentralNetworkPolicyRequest.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        """Sets the central_network_id of this ApplyCentralNetworkPolicyRequest.

        中心网络的ID。

        :param central_network_id: The central_network_id of this ApplyCentralNetworkPolicyRequest.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

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
        if not isinstance(other, ApplyCentralNetworkPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
