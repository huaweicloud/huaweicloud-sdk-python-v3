# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected_cluster_total_num': 'int',
        'cluster_total_num': 'int',
        'namespace_total_num': 'int',
        'network_policy_total_num': 'int'
    }

    attribute_map = {
        'protected_cluster_total_num': 'protected_cluster_total_num',
        'cluster_total_num': 'cluster_total_num',
        'namespace_total_num': 'namespace_total_num',
        'network_policy_total_num': 'network_policy_total_num'
    }

    def __init__(self, protected_cluster_total_num=None, cluster_total_num=None, namespace_total_num=None, network_policy_total_num=None):
        r"""ShowNetworkStatisticsResponse

        The model defined in huaweicloud sdk

        :param protected_cluster_total_num: 未保护集群数
        :type protected_cluster_total_num: int
        :param cluster_total_num: 集群数
        :type cluster_total_num: int
        :param namespace_total_num: 命名空间数
        :type namespace_total_num: int
        :param network_policy_total_num: 策略数
        :type network_policy_total_num: int
        """
        
        super(ShowNetworkStatisticsResponse, self).__init__()

        self._protected_cluster_total_num = None
        self._cluster_total_num = None
        self._namespace_total_num = None
        self._network_policy_total_num = None
        self.discriminator = None

        if protected_cluster_total_num is not None:
            self.protected_cluster_total_num = protected_cluster_total_num
        if cluster_total_num is not None:
            self.cluster_total_num = cluster_total_num
        if namespace_total_num is not None:
            self.namespace_total_num = namespace_total_num
        if network_policy_total_num is not None:
            self.network_policy_total_num = network_policy_total_num

    @property
    def protected_cluster_total_num(self):
        r"""Gets the protected_cluster_total_num of this ShowNetworkStatisticsResponse.

        未保护集群数

        :return: The protected_cluster_total_num of this ShowNetworkStatisticsResponse.
        :rtype: int
        """
        return self._protected_cluster_total_num

    @protected_cluster_total_num.setter
    def protected_cluster_total_num(self, protected_cluster_total_num):
        r"""Sets the protected_cluster_total_num of this ShowNetworkStatisticsResponse.

        未保护集群数

        :param protected_cluster_total_num: The protected_cluster_total_num of this ShowNetworkStatisticsResponse.
        :type protected_cluster_total_num: int
        """
        self._protected_cluster_total_num = protected_cluster_total_num

    @property
    def cluster_total_num(self):
        r"""Gets the cluster_total_num of this ShowNetworkStatisticsResponse.

        集群数

        :return: The cluster_total_num of this ShowNetworkStatisticsResponse.
        :rtype: int
        """
        return self._cluster_total_num

    @cluster_total_num.setter
    def cluster_total_num(self, cluster_total_num):
        r"""Sets the cluster_total_num of this ShowNetworkStatisticsResponse.

        集群数

        :param cluster_total_num: The cluster_total_num of this ShowNetworkStatisticsResponse.
        :type cluster_total_num: int
        """
        self._cluster_total_num = cluster_total_num

    @property
    def namespace_total_num(self):
        r"""Gets the namespace_total_num of this ShowNetworkStatisticsResponse.

        命名空间数

        :return: The namespace_total_num of this ShowNetworkStatisticsResponse.
        :rtype: int
        """
        return self._namespace_total_num

    @namespace_total_num.setter
    def namespace_total_num(self, namespace_total_num):
        r"""Sets the namespace_total_num of this ShowNetworkStatisticsResponse.

        命名空间数

        :param namespace_total_num: The namespace_total_num of this ShowNetworkStatisticsResponse.
        :type namespace_total_num: int
        """
        self._namespace_total_num = namespace_total_num

    @property
    def network_policy_total_num(self):
        r"""Gets the network_policy_total_num of this ShowNetworkStatisticsResponse.

        策略数

        :return: The network_policy_total_num of this ShowNetworkStatisticsResponse.
        :rtype: int
        """
        return self._network_policy_total_num

    @network_policy_total_num.setter
    def network_policy_total_num(self, network_policy_total_num):
        r"""Sets the network_policy_total_num of this ShowNetworkStatisticsResponse.

        策略数

        :param network_policy_total_num: The network_policy_total_num of this ShowNetworkStatisticsResponse.
        :type network_policy_total_num: int
        """
        self._network_policy_total_num = network_policy_total_num

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
        if not isinstance(other, ShowNetworkStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
