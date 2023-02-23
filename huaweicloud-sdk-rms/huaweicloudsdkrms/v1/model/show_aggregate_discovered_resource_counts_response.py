# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAggregateDiscoveredResourceCountsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_by_key': 'str',
        'grouped_resource_counts': 'list[GroupedResourceCount]',
        'total_discovered_resources': 'int'
    }

    attribute_map = {
        'group_by_key': 'group_by_key',
        'grouped_resource_counts': 'grouped_resource_counts',
        'total_discovered_resources': 'total_discovered_resources'
    }

    def __init__(self, group_by_key=None, grouped_resource_counts=None, total_discovered_resources=None):
        """ShowAggregateDiscoveredResourceCountsResponse

        The model defined in huaweicloud sdk

        :param group_by_key: 资源计数进行分组的键。
        :type group_by_key: str
        :param grouped_resource_counts: 分组资源计数的列表。
        :type grouped_resource_counts: list[:class:`huaweicloudsdkrms.v1.GroupedResourceCount`]
        :param total_discovered_resources: 指定过滤器的资源聚合器中存在的资源总数。
        :type total_discovered_resources: int
        """
        
        super(ShowAggregateDiscoveredResourceCountsResponse, self).__init__()

        self._group_by_key = None
        self._grouped_resource_counts = None
        self._total_discovered_resources = None
        self.discriminator = None

        if group_by_key is not None:
            self.group_by_key = group_by_key
        if grouped_resource_counts is not None:
            self.grouped_resource_counts = grouped_resource_counts
        if total_discovered_resources is not None:
            self.total_discovered_resources = total_discovered_resources

    @property
    def group_by_key(self):
        """Gets the group_by_key of this ShowAggregateDiscoveredResourceCountsResponse.

        资源计数进行分组的键。

        :return: The group_by_key of this ShowAggregateDiscoveredResourceCountsResponse.
        :rtype: str
        """
        return self._group_by_key

    @group_by_key.setter
    def group_by_key(self, group_by_key):
        """Sets the group_by_key of this ShowAggregateDiscoveredResourceCountsResponse.

        资源计数进行分组的键。

        :param group_by_key: The group_by_key of this ShowAggregateDiscoveredResourceCountsResponse.
        :type group_by_key: str
        """
        self._group_by_key = group_by_key

    @property
    def grouped_resource_counts(self):
        """Gets the grouped_resource_counts of this ShowAggregateDiscoveredResourceCountsResponse.

        分组资源计数的列表。

        :return: The grouped_resource_counts of this ShowAggregateDiscoveredResourceCountsResponse.
        :rtype: list[:class:`huaweicloudsdkrms.v1.GroupedResourceCount`]
        """
        return self._grouped_resource_counts

    @grouped_resource_counts.setter
    def grouped_resource_counts(self, grouped_resource_counts):
        """Sets the grouped_resource_counts of this ShowAggregateDiscoveredResourceCountsResponse.

        分组资源计数的列表。

        :param grouped_resource_counts: The grouped_resource_counts of this ShowAggregateDiscoveredResourceCountsResponse.
        :type grouped_resource_counts: list[:class:`huaweicloudsdkrms.v1.GroupedResourceCount`]
        """
        self._grouped_resource_counts = grouped_resource_counts

    @property
    def total_discovered_resources(self):
        """Gets the total_discovered_resources of this ShowAggregateDiscoveredResourceCountsResponse.

        指定过滤器的资源聚合器中存在的资源总数。

        :return: The total_discovered_resources of this ShowAggregateDiscoveredResourceCountsResponse.
        :rtype: int
        """
        return self._total_discovered_resources

    @total_discovered_resources.setter
    def total_discovered_resources(self, total_discovered_resources):
        """Sets the total_discovered_resources of this ShowAggregateDiscoveredResourceCountsResponse.

        指定过滤器的资源聚合器中存在的资源总数。

        :param total_discovered_resources: The total_discovered_resources of this ShowAggregateDiscoveredResourceCountsResponse.
        :type total_discovered_resources: int
        """
        self._total_discovered_resources = total_discovered_resources

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
        if not isinstance(other, ShowAggregateDiscoveredResourceCountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
