# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRpoStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_rpo_statistics': 'list[RpoStattisticsParams]',
        'count': 'int'
    }

    attribute_map = {
        'resource_rpo_statistics': 'resource_rpo_statistics',
        'count': 'count'
    }

    def __init__(self, resource_rpo_statistics=None, count=None):
        """ListRpoStatisticsResponse

        The model defined in huaweicloud sdk

        :param resource_rpo_statistics: 资源的RPO超标趋势记录列表。
        :type resource_rpo_statistics: list[:class:`huaweicloudsdksdrs.v1.RpoStattisticsParams`]
        :param count: 列表中包含的资源的RPO超标趋势记录个数。
        :type count: int
        """
        
        super(ListRpoStatisticsResponse, self).__init__()

        self._resource_rpo_statistics = None
        self._count = None
        self.discriminator = None

        if resource_rpo_statistics is not None:
            self.resource_rpo_statistics = resource_rpo_statistics
        if count is not None:
            self.count = count

    @property
    def resource_rpo_statistics(self):
        """Gets the resource_rpo_statistics of this ListRpoStatisticsResponse.

        资源的RPO超标趋势记录列表。

        :return: The resource_rpo_statistics of this ListRpoStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.RpoStattisticsParams`]
        """
        return self._resource_rpo_statistics

    @resource_rpo_statistics.setter
    def resource_rpo_statistics(self, resource_rpo_statistics):
        """Sets the resource_rpo_statistics of this ListRpoStatisticsResponse.

        资源的RPO超标趋势记录列表。

        :param resource_rpo_statistics: The resource_rpo_statistics of this ListRpoStatisticsResponse.
        :type resource_rpo_statistics: list[:class:`huaweicloudsdksdrs.v1.RpoStattisticsParams`]
        """
        self._resource_rpo_statistics = resource_rpo_statistics

    @property
    def count(self):
        """Gets the count of this ListRpoStatisticsResponse.

        列表中包含的资源的RPO超标趋势记录个数。

        :return: The count of this ListRpoStatisticsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRpoStatisticsResponse.

        列表中包含的资源的RPO超标趋势记录个数。

        :param count: The count of this ListRpoStatisticsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListRpoStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
