# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterProtectOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_num': 'int',
        'under_protect_num': 'int',
        'policy_num': 'int',
        'event_num': 'int',
        'block_num': 'int'
    }

    attribute_map = {
        'cluster_num': 'cluster_num',
        'under_protect_num': 'under_protect_num',
        'policy_num': 'policy_num',
        'event_num': 'event_num',
        'block_num': 'block_num'
    }

    def __init__(self, cluster_num=None, under_protect_num=None, policy_num=None, event_num=None, block_num=None):
        r"""ListClusterProtectOverviewResponse

        The model defined in huaweicloud sdk

        :param cluster_num: 集群数量
        :type cluster_num: int
        :param under_protect_num: 防护中数量
        :type under_protect_num: int
        :param policy_num: 策略数量
        :type policy_num: int
        :param event_num: 事件数量
        :type event_num: int
        :param block_num: 已阻断事件数量
        :type block_num: int
        """
        
        super(ListClusterProtectOverviewResponse, self).__init__()

        self._cluster_num = None
        self._under_protect_num = None
        self._policy_num = None
        self._event_num = None
        self._block_num = None
        self.discriminator = None

        if cluster_num is not None:
            self.cluster_num = cluster_num
        if under_protect_num is not None:
            self.under_protect_num = under_protect_num
        if policy_num is not None:
            self.policy_num = policy_num
        if event_num is not None:
            self.event_num = event_num
        if block_num is not None:
            self.block_num = block_num

    @property
    def cluster_num(self):
        r"""Gets the cluster_num of this ListClusterProtectOverviewResponse.

        集群数量

        :return: The cluster_num of this ListClusterProtectOverviewResponse.
        :rtype: int
        """
        return self._cluster_num

    @cluster_num.setter
    def cluster_num(self, cluster_num):
        r"""Sets the cluster_num of this ListClusterProtectOverviewResponse.

        集群数量

        :param cluster_num: The cluster_num of this ListClusterProtectOverviewResponse.
        :type cluster_num: int
        """
        self._cluster_num = cluster_num

    @property
    def under_protect_num(self):
        r"""Gets the under_protect_num of this ListClusterProtectOverviewResponse.

        防护中数量

        :return: The under_protect_num of this ListClusterProtectOverviewResponse.
        :rtype: int
        """
        return self._under_protect_num

    @under_protect_num.setter
    def under_protect_num(self, under_protect_num):
        r"""Sets the under_protect_num of this ListClusterProtectOverviewResponse.

        防护中数量

        :param under_protect_num: The under_protect_num of this ListClusterProtectOverviewResponse.
        :type under_protect_num: int
        """
        self._under_protect_num = under_protect_num

    @property
    def policy_num(self):
        r"""Gets the policy_num of this ListClusterProtectOverviewResponse.

        策略数量

        :return: The policy_num of this ListClusterProtectOverviewResponse.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        r"""Sets the policy_num of this ListClusterProtectOverviewResponse.

        策略数量

        :param policy_num: The policy_num of this ListClusterProtectOverviewResponse.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def event_num(self):
        r"""Gets the event_num of this ListClusterProtectOverviewResponse.

        事件数量

        :return: The event_num of this ListClusterProtectOverviewResponse.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this ListClusterProtectOverviewResponse.

        事件数量

        :param event_num: The event_num of this ListClusterProtectOverviewResponse.
        :type event_num: int
        """
        self._event_num = event_num

    @property
    def block_num(self):
        r"""Gets the block_num of this ListClusterProtectOverviewResponse.

        已阻断事件数量

        :return: The block_num of this ListClusterProtectOverviewResponse.
        :rtype: int
        """
        return self._block_num

    @block_num.setter
    def block_num(self, block_num):
        r"""Sets the block_num of this ListClusterProtectOverviewResponse.

        已阻断事件数量

        :param block_num: The block_num of this ListClusterProtectOverviewResponse.
        :type block_num: int
        """
        self._block_num = block_num

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
        if not isinstance(other, ListClusterProtectOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
