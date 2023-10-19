# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyCentralNetworkPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'central_network_policy': 'CentralNetworkPolicy',
        'central_network_policy_change_set': 'list[CentralNetworkElementChange]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'central_network_policy': 'central_network_policy',
        'central_network_policy_change_set': 'central_network_policy_change_set'
    }

    def __init__(self, request_id=None, central_network_policy=None, central_network_policy_change_set=None):
        """ApplyCentralNetworkPolicyResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param central_network_policy: 
        :type central_network_policy: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicy`
        :param central_network_policy_change_set: 网络策略变化列表。
        :type central_network_policy_change_set: list[:class:`huaweicloudsdkcc.v3.CentralNetworkElementChange`]
        """
        
        super(ApplyCentralNetworkPolicyResponse, self).__init__()

        self._request_id = None
        self._central_network_policy = None
        self._central_network_policy_change_set = None
        self.discriminator = None

        self.request_id = request_id
        self.central_network_policy = central_network_policy
        self.central_network_policy_change_set = central_network_policy_change_set

    @property
    def request_id(self):
        """Gets the request_id of this ApplyCentralNetworkPolicyResponse.

        资源ID标识符。

        :return: The request_id of this ApplyCentralNetworkPolicyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ApplyCentralNetworkPolicyResponse.

        资源ID标识符。

        :param request_id: The request_id of this ApplyCentralNetworkPolicyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def central_network_policy(self):
        """Gets the central_network_policy of this ApplyCentralNetworkPolicyResponse.

        :return: The central_network_policy of this ApplyCentralNetworkPolicyResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicy`
        """
        return self._central_network_policy

    @central_network_policy.setter
    def central_network_policy(self, central_network_policy):
        """Sets the central_network_policy of this ApplyCentralNetworkPolicyResponse.

        :param central_network_policy: The central_network_policy of this ApplyCentralNetworkPolicyResponse.
        :type central_network_policy: :class:`huaweicloudsdkcc.v3.CentralNetworkPolicy`
        """
        self._central_network_policy = central_network_policy

    @property
    def central_network_policy_change_set(self):
        """Gets the central_network_policy_change_set of this ApplyCentralNetworkPolicyResponse.

        网络策略变化列表。

        :return: The central_network_policy_change_set of this ApplyCentralNetworkPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkElementChange`]
        """
        return self._central_network_policy_change_set

    @central_network_policy_change_set.setter
    def central_network_policy_change_set(self, central_network_policy_change_set):
        """Sets the central_network_policy_change_set of this ApplyCentralNetworkPolicyResponse.

        网络策略变化列表。

        :param central_network_policy_change_set: The central_network_policy_change_set of this ApplyCentralNetworkPolicyResponse.
        :type central_network_policy_change_set: list[:class:`huaweicloudsdkcc.v3.CentralNetworkElementChange`]
        """
        self._central_network_policy_change_set = central_network_policy_change_set

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
        if not isinstance(other, ApplyCentralNetworkPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
