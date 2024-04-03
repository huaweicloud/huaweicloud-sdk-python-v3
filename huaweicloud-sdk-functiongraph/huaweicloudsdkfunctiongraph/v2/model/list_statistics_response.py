# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'list[MonthUsed]',
        'gbs': 'list[MonthUsed]',
        'gpu_gbs': 'list[MonthUsed]',
        'statistics': 'ListFunctionStatisticsResponseBody'
    }

    attribute_map = {
        'count': 'count',
        'gbs': 'gbs',
        'gpu_gbs': 'gpu_gbs',
        'statistics': 'statistics'
    }

    def __init__(self, count=None, gbs=None, gpu_gbs=None, statistics=None):
        """ListStatisticsResponse

        The model defined in huaweicloud sdk

        :param count: 月度调用次数
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        :param gbs: 月度资源用量
        :type gbs: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        :param gpu_gbs: 月度gpu资源用量
        :type gpu_gbs: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        :param statistics: 
        :type statistics: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsResponseBody`
        """
        
        super(ListStatisticsResponse, self).__init__()

        self._count = None
        self._gbs = None
        self._gpu_gbs = None
        self._statistics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if gbs is not None:
            self.gbs = gbs
        if gpu_gbs is not None:
            self.gpu_gbs = gpu_gbs
        if statistics is not None:
            self.statistics = statistics

    @property
    def count(self):
        """Gets the count of this ListStatisticsResponse.

        月度调用次数

        :return: The count of this ListStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListStatisticsResponse.

        月度调用次数

        :param count: The count of this ListStatisticsResponse.
        :type count: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        self._count = count

    @property
    def gbs(self):
        """Gets the gbs of this ListStatisticsResponse.

        月度资源用量

        :return: The gbs of this ListStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        return self._gbs

    @gbs.setter
    def gbs(self, gbs):
        """Sets the gbs of this ListStatisticsResponse.

        月度资源用量

        :param gbs: The gbs of this ListStatisticsResponse.
        :type gbs: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        self._gbs = gbs

    @property
    def gpu_gbs(self):
        """Gets the gpu_gbs of this ListStatisticsResponse.

        月度gpu资源用量

        :return: The gpu_gbs of this ListStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        return self._gpu_gbs

    @gpu_gbs.setter
    def gpu_gbs(self, gpu_gbs):
        """Sets the gpu_gbs of this ListStatisticsResponse.

        月度gpu资源用量

        :param gpu_gbs: The gpu_gbs of this ListStatisticsResponse.
        :type gpu_gbs: list[:class:`huaweicloudsdkfunctiongraph.v2.MonthUsed`]
        """
        self._gpu_gbs = gpu_gbs

    @property
    def statistics(self):
        """Gets the statistics of this ListStatisticsResponse.

        :return: The statistics of this ListStatisticsResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsResponseBody`
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ListStatisticsResponse.

        :param statistics: The statistics of this ListStatisticsResponse.
        :type statistics: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsResponseBody`
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
        if not isinstance(other, ListStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
