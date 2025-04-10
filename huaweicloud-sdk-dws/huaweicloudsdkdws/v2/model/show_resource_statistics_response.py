# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_statistics': 'StatusStatistics',
        'node_statistics': 'StatusStatistics'
    }

    attribute_map = {
        'cluster_statistics': 'cluster_statistics',
        'node_statistics': 'node_statistics'
    }

    def __init__(self, cluster_statistics=None, node_statistics=None):
        r"""ShowResourceStatisticsResponse

        The model defined in huaweicloud sdk

        :param cluster_statistics: 
        :type cluster_statistics: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        :param node_statistics: 
        :type node_statistics: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        """
        
        super(ShowResourceStatisticsResponse, self).__init__()

        self._cluster_statistics = None
        self._node_statistics = None
        self.discriminator = None

        if cluster_statistics is not None:
            self.cluster_statistics = cluster_statistics
        if node_statistics is not None:
            self.node_statistics = node_statistics

    @property
    def cluster_statistics(self):
        r"""Gets the cluster_statistics of this ShowResourceStatisticsResponse.

        :return: The cluster_statistics of this ShowResourceStatisticsResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        """
        return self._cluster_statistics

    @cluster_statistics.setter
    def cluster_statistics(self, cluster_statistics):
        r"""Sets the cluster_statistics of this ShowResourceStatisticsResponse.

        :param cluster_statistics: The cluster_statistics of this ShowResourceStatisticsResponse.
        :type cluster_statistics: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        """
        self._cluster_statistics = cluster_statistics

    @property
    def node_statistics(self):
        r"""Gets the node_statistics of this ShowResourceStatisticsResponse.

        :return: The node_statistics of this ShowResourceStatisticsResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        """
        return self._node_statistics

    @node_statistics.setter
    def node_statistics(self, node_statistics):
        r"""Sets the node_statistics of this ShowResourceStatisticsResponse.

        :param node_statistics: The node_statistics of this ShowResourceStatisticsResponse.
        :type node_statistics: :class:`huaweicloudsdkdws.v2.StatusStatistics`
        """
        self._node_statistics = node_statistics

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
        if not isinstance(other, ShowResourceStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
