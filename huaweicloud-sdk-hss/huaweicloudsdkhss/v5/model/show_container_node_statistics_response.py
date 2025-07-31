# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowContainerNodeStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unprotected_num': 'int',
        'protected_num': 'int',
        'protected_num_on_demand': 'int',
        'protected_num_packet_cycle': 'int',
        'cluster_node_not_installed_num': 'int',
        'not_cluster_node_not_installed_num': 'int'
    }

    attribute_map = {
        'unprotected_num': 'unprotected_num',
        'protected_num': 'protected_num',
        'protected_num_on_demand': 'protected_num_on_demand',
        'protected_num_packet_cycle': 'protected_num_packet_cycle',
        'cluster_node_not_installed_num': 'cluster_node_not_installed_num',
        'not_cluster_node_not_installed_num': 'not_cluster_node_not_installed_num'
    }

    def __init__(self, unprotected_num=None, protected_num=None, protected_num_on_demand=None, protected_num_packet_cycle=None, cluster_node_not_installed_num=None, not_cluster_node_not_installed_num=None):
        r"""ShowContainerNodeStatisticsResponse

        The model defined in huaweicloud sdk

        :param unprotected_num: 未防护服务器数
        :type unprotected_num: int
        :param protected_num: 开启防护节点
        :type protected_num: int
        :param protected_num_on_demand: 按需开启防护节点
        :type protected_num_on_demand: int
        :param protected_num_packet_cycle: 按配额开启防护节点
        :type protected_num_packet_cycle: int
        :param cluster_node_not_installed_num: 未安装集群节点
        :type cluster_node_not_installed_num: int
        :param not_cluster_node_not_installed_num: 未安装非集群节点
        :type not_cluster_node_not_installed_num: int
        """
        
        super(ShowContainerNodeStatisticsResponse, self).__init__()

        self._unprotected_num = None
        self._protected_num = None
        self._protected_num_on_demand = None
        self._protected_num_packet_cycle = None
        self._cluster_node_not_installed_num = None
        self._not_cluster_node_not_installed_num = None
        self.discriminator = None

        if unprotected_num is not None:
            self.unprotected_num = unprotected_num
        if protected_num is not None:
            self.protected_num = protected_num
        if protected_num_on_demand is not None:
            self.protected_num_on_demand = protected_num_on_demand
        if protected_num_packet_cycle is not None:
            self.protected_num_packet_cycle = protected_num_packet_cycle
        if cluster_node_not_installed_num is not None:
            self.cluster_node_not_installed_num = cluster_node_not_installed_num
        if not_cluster_node_not_installed_num is not None:
            self.not_cluster_node_not_installed_num = not_cluster_node_not_installed_num

    @property
    def unprotected_num(self):
        r"""Gets the unprotected_num of this ShowContainerNodeStatisticsResponse.

        未防护服务器数

        :return: The unprotected_num of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._unprotected_num

    @unprotected_num.setter
    def unprotected_num(self, unprotected_num):
        r"""Sets the unprotected_num of this ShowContainerNodeStatisticsResponse.

        未防护服务器数

        :param unprotected_num: The unprotected_num of this ShowContainerNodeStatisticsResponse.
        :type unprotected_num: int
        """
        self._unprotected_num = unprotected_num

    @property
    def protected_num(self):
        r"""Gets the protected_num of this ShowContainerNodeStatisticsResponse.

        开启防护节点

        :return: The protected_num of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._protected_num

    @protected_num.setter
    def protected_num(self, protected_num):
        r"""Sets the protected_num of this ShowContainerNodeStatisticsResponse.

        开启防护节点

        :param protected_num: The protected_num of this ShowContainerNodeStatisticsResponse.
        :type protected_num: int
        """
        self._protected_num = protected_num

    @property
    def protected_num_on_demand(self):
        r"""Gets the protected_num_on_demand of this ShowContainerNodeStatisticsResponse.

        按需开启防护节点

        :return: The protected_num_on_demand of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._protected_num_on_demand

    @protected_num_on_demand.setter
    def protected_num_on_demand(self, protected_num_on_demand):
        r"""Sets the protected_num_on_demand of this ShowContainerNodeStatisticsResponse.

        按需开启防护节点

        :param protected_num_on_demand: The protected_num_on_demand of this ShowContainerNodeStatisticsResponse.
        :type protected_num_on_demand: int
        """
        self._protected_num_on_demand = protected_num_on_demand

    @property
    def protected_num_packet_cycle(self):
        r"""Gets the protected_num_packet_cycle of this ShowContainerNodeStatisticsResponse.

        按配额开启防护节点

        :return: The protected_num_packet_cycle of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._protected_num_packet_cycle

    @protected_num_packet_cycle.setter
    def protected_num_packet_cycle(self, protected_num_packet_cycle):
        r"""Sets the protected_num_packet_cycle of this ShowContainerNodeStatisticsResponse.

        按配额开启防护节点

        :param protected_num_packet_cycle: The protected_num_packet_cycle of this ShowContainerNodeStatisticsResponse.
        :type protected_num_packet_cycle: int
        """
        self._protected_num_packet_cycle = protected_num_packet_cycle

    @property
    def cluster_node_not_installed_num(self):
        r"""Gets the cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.

        未安装集群节点

        :return: The cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._cluster_node_not_installed_num

    @cluster_node_not_installed_num.setter
    def cluster_node_not_installed_num(self, cluster_node_not_installed_num):
        r"""Sets the cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.

        未安装集群节点

        :param cluster_node_not_installed_num: The cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.
        :type cluster_node_not_installed_num: int
        """
        self._cluster_node_not_installed_num = cluster_node_not_installed_num

    @property
    def not_cluster_node_not_installed_num(self):
        r"""Gets the not_cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.

        未安装非集群节点

        :return: The not_cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.
        :rtype: int
        """
        return self._not_cluster_node_not_installed_num

    @not_cluster_node_not_installed_num.setter
    def not_cluster_node_not_installed_num(self, not_cluster_node_not_installed_num):
        r"""Sets the not_cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.

        未安装非集群节点

        :param not_cluster_node_not_installed_num: The not_cluster_node_not_installed_num of this ShowContainerNodeStatisticsResponse.
        :type not_cluster_node_not_installed_num: int
        """
        self._not_cluster_node_not_installed_num = not_cluster_node_not_installed_num

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
        if not isinstance(other, ShowContainerNodeStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
