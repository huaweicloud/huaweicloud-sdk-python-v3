# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_total': 'int',
        'clusters': 'list[Cluster]'
    }

    attribute_map = {
        'cluster_total': 'clusterTotal',
        'clusters': 'clusters'
    }

    def __init__(self, cluster_total=None, clusters=None):
        """ListClustersResponse

        The model defined in huaweicloud sdk

        :param cluster_total: 集群列表总数。
        :type cluster_total: int
        :param clusters: 集群参数。
        :type clusters: list[:class:`huaweicloudsdkmrs.v1.Cluster`]
        """
        
        super(ListClustersResponse, self).__init__()

        self._cluster_total = None
        self._clusters = None
        self.discriminator = None

        if cluster_total is not None:
            self.cluster_total = cluster_total
        if clusters is not None:
            self.clusters = clusters

    @property
    def cluster_total(self):
        """Gets the cluster_total of this ListClustersResponse.

        集群列表总数。

        :return: The cluster_total of this ListClustersResponse.
        :rtype: int
        """
        return self._cluster_total

    @cluster_total.setter
    def cluster_total(self, cluster_total):
        """Sets the cluster_total of this ListClustersResponse.

        集群列表总数。

        :param cluster_total: The cluster_total of this ListClustersResponse.
        :type cluster_total: int
        """
        self._cluster_total = cluster_total

    @property
    def clusters(self):
        """Gets the clusters of this ListClustersResponse.

        集群参数。

        :return: The clusters of this ListClustersResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.Cluster`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ListClustersResponse.

        集群参数。

        :param clusters: The clusters of this ListClustersResponse.
        :type clusters: list[:class:`huaweicloudsdkmrs.v1.Cluster`]
        """
        self._clusters = clusters

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
        if not isinstance(other, ListClustersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
