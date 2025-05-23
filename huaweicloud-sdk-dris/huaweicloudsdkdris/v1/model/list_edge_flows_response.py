# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeFlowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'statistics': 'list[OpenV2XStatisticsBody]'
    }

    attribute_map = {
        'count': 'count',
        'statistics': 'statistics'
    }

    def __init__(self, count=None, statistics=None):
        r"""ListEdgeFlowsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：条件查询返回的总条数。
        :type count: int
        :param statistics: **参数说明**：车辆流量，平均速度等统计信息列表
        :type statistics: list[:class:`huaweicloudsdkdris.v1.OpenV2XStatisticsBody`]
        """
        
        super(ListEdgeFlowsResponse, self).__init__()

        self._count = None
        self._statistics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if statistics is not None:
            self.statistics = statistics

    @property
    def count(self):
        r"""Gets the count of this ListEdgeFlowsResponse.

        **参数说明**：条件查询返回的总条数。

        :return: The count of this ListEdgeFlowsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListEdgeFlowsResponse.

        **参数说明**：条件查询返回的总条数。

        :param count: The count of this ListEdgeFlowsResponse.
        :type count: int
        """
        self._count = count

    @property
    def statistics(self):
        r"""Gets the statistics of this ListEdgeFlowsResponse.

        **参数说明**：车辆流量，平均速度等统计信息列表

        :return: The statistics of this ListEdgeFlowsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.OpenV2XStatisticsBody`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ListEdgeFlowsResponse.

        **参数说明**：车辆流量，平均速度等统计信息列表

        :param statistics: The statistics of this ListEdgeFlowsResponse.
        :type statistics: list[:class:`huaweicloudsdkdris.v1.OpenV2XStatisticsBody`]
        """
        self._statistics = statistics

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
        if not isinstance(other, ListEdgeFlowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
