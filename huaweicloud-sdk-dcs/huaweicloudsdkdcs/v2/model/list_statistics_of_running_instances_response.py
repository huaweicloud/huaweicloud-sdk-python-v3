# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatisticsOfRunningInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistics': 'list[InstanceStatistic]'
    }

    attribute_map = {
        'statistics': 'statistics'
    }

    def __init__(self, statistics=None):
        r"""ListStatisticsOfRunningInstancesResponse

        The model defined in huaweicloud sdk

        :param statistics: 该租户下处于“运行中”状态的实例的统计信息。
        :type statistics: list[:class:`huaweicloudsdkdcs.v2.InstanceStatistic`]
        """
        
        super(ListStatisticsOfRunningInstancesResponse, self).__init__()

        self._statistics = None
        self.discriminator = None

        if statistics is not None:
            self.statistics = statistics

    @property
    def statistics(self):
        r"""Gets the statistics of this ListStatisticsOfRunningInstancesResponse.

        该租户下处于“运行中”状态的实例的统计信息。

        :return: The statistics of this ListStatisticsOfRunningInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstanceStatistic`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ListStatisticsOfRunningInstancesResponse.

        该租户下处于“运行中”状态的实例的统计信息。

        :param statistics: The statistics of this ListStatisticsOfRunningInstancesResponse.
        :type statistics: list[:class:`huaweicloudsdkdcs.v2.InstanceStatistic`]
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
        if not isinstance(other, ListStatisticsOfRunningInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
