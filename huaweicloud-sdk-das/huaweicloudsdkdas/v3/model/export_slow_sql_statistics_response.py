# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowSqlStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistics_list': 'list[SlowSqlStatistics]',
        'total_count': 'int'
    }

    attribute_map = {
        'statistics_list': 'statistics_list',
        'total_count': 'total_count'
    }

    def __init__(self, statistics_list=None, total_count=None):
        """ExportSlowSqlStatisticsResponse

        The model defined in huaweicloud sdk

        :param statistics_list: 慢SQL统计列表。
        :type statistics_list: list[:class:`huaweicloudsdkdas.v3.SlowSqlStatistics`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ExportSlowSqlStatisticsResponse, self).__init__()

        self._statistics_list = None
        self._total_count = None
        self.discriminator = None

        if statistics_list is not None:
            self.statistics_list = statistics_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def statistics_list(self):
        """Gets the statistics_list of this ExportSlowSqlStatisticsResponse.

        慢SQL统计列表。

        :return: The statistics_list of this ExportSlowSqlStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowSqlStatistics`]
        """
        return self._statistics_list

    @statistics_list.setter
    def statistics_list(self, statistics_list):
        """Sets the statistics_list of this ExportSlowSqlStatisticsResponse.

        慢SQL统计列表。

        :param statistics_list: The statistics_list of this ExportSlowSqlStatisticsResponse.
        :type statistics_list: list[:class:`huaweicloudsdkdas.v3.SlowSqlStatistics`]
        """
        self._statistics_list = statistics_list

    @property
    def total_count(self):
        """Gets the total_count of this ExportSlowSqlStatisticsResponse.

        总数。

        :return: The total_count of this ExportSlowSqlStatisticsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ExportSlowSqlStatisticsResponse.

        总数。

        :param total_count: The total_count of this ExportSlowSqlStatisticsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ExportSlowSqlStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
