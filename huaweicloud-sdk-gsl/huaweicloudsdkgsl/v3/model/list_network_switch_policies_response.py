# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkSwitchPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'count': 'int',
        'network_switch_policy_list': 'list[NetworkSwitchPolicyVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'network_switch_policy_list': 'network_switch_policy_list'
    }

    def __init__(self, limit=None, offset=None, count=None, network_switch_policy_list=None):
        r"""ListNetworkSwitchPoliciesResponse

        The model defined in huaweicloud sdk

        :param limit: 每页的记录数
        :type limit: int
        :param offset: 页码，最小值是1，最大值为1000000。默认值是1.
        :type offset: int
        :param count: 记录总数
        :type count: int
        :param network_switch_policy_list: 网络切换策略实例列表
        :type network_switch_policy_list: list[:class:`huaweicloudsdkgsl.v3.NetworkSwitchPolicyVO`]
        """
        
        super(ListNetworkSwitchPoliciesResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._network_switch_policy_list = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if network_switch_policy_list is not None:
            self.network_switch_policy_list = network_switch_policy_list

    @property
    def limit(self):
        r"""Gets the limit of this ListNetworkSwitchPoliciesResponse.

        每页的记录数

        :return: The limit of this ListNetworkSwitchPoliciesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNetworkSwitchPoliciesResponse.

        每页的记录数

        :param limit: The limit of this ListNetworkSwitchPoliciesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNetworkSwitchPoliciesResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :return: The offset of this ListNetworkSwitchPoliciesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNetworkSwitchPoliciesResponse.

        页码，最小值是1，最大值为1000000。默认值是1.

        :param offset: The offset of this ListNetworkSwitchPoliciesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        r"""Gets the count of this ListNetworkSwitchPoliciesResponse.

        记录总数

        :return: The count of this ListNetworkSwitchPoliciesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListNetworkSwitchPoliciesResponse.

        记录总数

        :param count: The count of this ListNetworkSwitchPoliciesResponse.
        :type count: int
        """
        self._count = count

    @property
    def network_switch_policy_list(self):
        r"""Gets the network_switch_policy_list of this ListNetworkSwitchPoliciesResponse.

        网络切换策略实例列表

        :return: The network_switch_policy_list of this ListNetworkSwitchPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.NetworkSwitchPolicyVO`]
        """
        return self._network_switch_policy_list

    @network_switch_policy_list.setter
    def network_switch_policy_list(self, network_switch_policy_list):
        r"""Sets the network_switch_policy_list of this ListNetworkSwitchPoliciesResponse.

        网络切换策略实例列表

        :param network_switch_policy_list: The network_switch_policy_list of this ListNetworkSwitchPoliciesResponse.
        :type network_switch_policy_list: list[:class:`huaweicloudsdkgsl.v3.NetworkSwitchPolicyVO`]
        """
        self._network_switch_policy_list = network_switch_policy_list

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
        if not isinstance(other, ListNetworkSwitchPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
