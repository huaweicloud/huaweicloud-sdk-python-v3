# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateDiscoveredResourceCountsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregator_id': 'str',
        'filter': 'ResourceCountsFilters',
        'group_by_key': 'str'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'filter': 'filter',
        'group_by_key': 'group_by_key'
    }

    def __init__(self, aggregator_id=None, filter=None, group_by_key=None):
        r"""AggregateDiscoveredResourceCountsRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkrms.v1.ResourceCountsFilters`
        :param group_by_key: 用于对资源计数进行分组的键（RESOURCE_TYPE | ACCOUNT_ID）。
        :type group_by_key: str
        """
        
        

        self._aggregator_id = None
        self._filter = None
        self._group_by_key = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        if filter is not None:
            self.filter = filter
        self.group_by_key = group_by_key

    @property
    def aggregator_id(self):
        r"""Gets the aggregator_id of this AggregateDiscoveredResourceCountsRequest.

        资源聚合器ID。

        :return: The aggregator_id of this AggregateDiscoveredResourceCountsRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        r"""Sets the aggregator_id of this AggregateDiscoveredResourceCountsRequest.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this AggregateDiscoveredResourceCountsRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def filter(self):
        r"""Gets the filter of this AggregateDiscoveredResourceCountsRequest.

        :return: The filter of this AggregateDiscoveredResourceCountsRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.ResourceCountsFilters`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this AggregateDiscoveredResourceCountsRequest.

        :param filter: The filter of this AggregateDiscoveredResourceCountsRequest.
        :type filter: :class:`huaweicloudsdkrms.v1.ResourceCountsFilters`
        """
        self._filter = filter

    @property
    def group_by_key(self):
        r"""Gets the group_by_key of this AggregateDiscoveredResourceCountsRequest.

        用于对资源计数进行分组的键（RESOURCE_TYPE | ACCOUNT_ID）。

        :return: The group_by_key of this AggregateDiscoveredResourceCountsRequest.
        :rtype: str
        """
        return self._group_by_key

    @group_by_key.setter
    def group_by_key(self, group_by_key):
        r"""Sets the group_by_key of this AggregateDiscoveredResourceCountsRequest.

        用于对资源计数进行分组的键（RESOURCE_TYPE | ACCOUNT_ID）。

        :param group_by_key: The group_by_key of this AggregateDiscoveredResourceCountsRequest.
        :type group_by_key: str
        """
        self._group_by_key = group_by_key

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
        if not isinstance(other, AggregateDiscoveredResourceCountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
