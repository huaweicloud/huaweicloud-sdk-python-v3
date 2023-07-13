# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateDiscoveredResourcesRequest:

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
        'filter': 'ResourcesFilters',
        'provider': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'filter': 'filter',
        'provider': 'provider',
        'resource_type': 'resource_type'
    }

    def __init__(self, aggregator_id=None, filter=None, provider=None, resource_type=None):
        """AggregateDiscoveredResourcesRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkrms.v1.ResourcesFilters`
        :param provider: 云服务类型。
        :type provider: str
        :param resource_type: 资源类型。
        :type resource_type: str
        """
        
        

        self._aggregator_id = None
        self._filter = None
        self._provider = None
        self._resource_type = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        if filter is not None:
            self.filter = filter
        if provider is not None:
            self.provider = provider
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def aggregator_id(self):
        """Gets the aggregator_id of this AggregateDiscoveredResourcesRequest.

        资源聚合器ID。

        :return: The aggregator_id of this AggregateDiscoveredResourcesRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        """Sets the aggregator_id of this AggregateDiscoveredResourcesRequest.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this AggregateDiscoveredResourcesRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def filter(self):
        """Gets the filter of this AggregateDiscoveredResourcesRequest.

        :return: The filter of this AggregateDiscoveredResourcesRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.ResourcesFilters`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this AggregateDiscoveredResourcesRequest.

        :param filter: The filter of this AggregateDiscoveredResourcesRequest.
        :type filter: :class:`huaweicloudsdkrms.v1.ResourcesFilters`
        """
        self._filter = filter

    @property
    def provider(self):
        """Gets the provider of this AggregateDiscoveredResourcesRequest.

        云服务类型。

        :return: The provider of this AggregateDiscoveredResourcesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AggregateDiscoveredResourcesRequest.

        云服务类型。

        :param provider: The provider of this AggregateDiscoveredResourcesRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def resource_type(self):
        """Gets the resource_type of this AggregateDiscoveredResourcesRequest.

        资源类型。

        :return: The resource_type of this AggregateDiscoveredResourcesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AggregateDiscoveredResourcesRequest.

        资源类型。

        :param resource_type: The resource_type of this AggregateDiscoveredResourcesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, AggregateDiscoveredResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
