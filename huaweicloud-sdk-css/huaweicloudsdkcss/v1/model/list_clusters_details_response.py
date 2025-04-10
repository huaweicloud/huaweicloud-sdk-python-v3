# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'int',
        'clusters': 'list[ClusterList]'
    }

    attribute_map = {
        'total_size': 'totalSize',
        'clusters': 'clusters'
    }

    def __init__(self, total_size=None, clusters=None):
        r"""ListClustersDetailsResponse

        The model defined in huaweicloud sdk

        :param total_size: 集群个数。
        :type total_size: int
        :param clusters: 集群对象列表。
        :type clusters: list[:class:`huaweicloudsdkcss.v1.ClusterList`]
        """
        
        super(ListClustersDetailsResponse, self).__init__()

        self._total_size = None
        self._clusters = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if clusters is not None:
            self.clusters = clusters

    @property
    def total_size(self):
        r"""Gets the total_size of this ListClustersDetailsResponse.

        集群个数。

        :return: The total_size of this ListClustersDetailsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListClustersDetailsResponse.

        集群个数。

        :param total_size: The total_size of this ListClustersDetailsResponse.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def clusters(self):
        r"""Gets the clusters of this ListClustersDetailsResponse.

        集群对象列表。

        :return: The clusters of this ListClustersDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ClusterList`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this ListClustersDetailsResponse.

        集群对象列表。

        :param clusters: The clusters of this ListClustersDetailsResponse.
        :type clusters: list[:class:`huaweicloudsdkcss.v1.ClusterList`]
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
        if not isinstance(other, ListClustersDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
