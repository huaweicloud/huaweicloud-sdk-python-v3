# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogicalClustersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_clusters': 'list[LogicalClusterInfo]',
        'count': 'int',
        'add_enable': 'bool'
    }

    attribute_map = {
        'logical_clusters': 'logical_clusters',
        'count': 'count',
        'add_enable': 'add_enable'
    }

    def __init__(self, logical_clusters=None, count=None, add_enable=None):
        """ListLogicalClustersResponse

        The model defined in huaweicloud sdk

        :param logical_clusters: 逻辑集群列表信息
        :type logical_clusters: list[:class:`huaweicloudsdkdws.v2.LogicalClusterInfo`]
        :param count: 逻辑集群总数量
        :type count: int
        :param add_enable: 作为互斥结果，如果集群内有其他运维操作，该值为false，此时不能添加逻辑集群
        :type add_enable: bool
        """
        
        super(ListLogicalClustersResponse, self).__init__()

        self._logical_clusters = None
        self._count = None
        self._add_enable = None
        self.discriminator = None

        if logical_clusters is not None:
            self.logical_clusters = logical_clusters
        if count is not None:
            self.count = count
        if add_enable is not None:
            self.add_enable = add_enable

    @property
    def logical_clusters(self):
        """Gets the logical_clusters of this ListLogicalClustersResponse.

        逻辑集群列表信息

        :return: The logical_clusters of this ListLogicalClustersResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterInfo`]
        """
        return self._logical_clusters

    @logical_clusters.setter
    def logical_clusters(self, logical_clusters):
        """Sets the logical_clusters of this ListLogicalClustersResponse.

        逻辑集群列表信息

        :param logical_clusters: The logical_clusters of this ListLogicalClustersResponse.
        :type logical_clusters: list[:class:`huaweicloudsdkdws.v2.LogicalClusterInfo`]
        """
        self._logical_clusters = logical_clusters

    @property
    def count(self):
        """Gets the count of this ListLogicalClustersResponse.

        逻辑集群总数量

        :return: The count of this ListLogicalClustersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListLogicalClustersResponse.

        逻辑集群总数量

        :param count: The count of this ListLogicalClustersResponse.
        :type count: int
        """
        self._count = count

    @property
    def add_enable(self):
        """Gets the add_enable of this ListLogicalClustersResponse.

        作为互斥结果，如果集群内有其他运维操作，该值为false，此时不能添加逻辑集群

        :return: The add_enable of this ListLogicalClustersResponse.
        :rtype: bool
        """
        return self._add_enable

    @add_enable.setter
    def add_enable(self, add_enable):
        """Sets the add_enable of this ListLogicalClustersResponse.

        作为互斥结果，如果集群内有其他运维操作，该值为false，此时不能添加逻辑集群

        :param add_enable: The add_enable of this ListLogicalClustersResponse.
        :type add_enable: bool
        """
        self._add_enable = add_enable

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
        if not isinstance(other, ListLogicalClustersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
