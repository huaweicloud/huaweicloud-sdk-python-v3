# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowSqlTrendDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slow_sql_trend_items': 'list[SlowSqlTrendItem]',
        'interval_millis': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'slow_sql_trend_items': 'slow_sql_trend_items',
        'interval_millis': 'interval_millis',
        'total_count': 'total_count'
    }

    def __init__(self, slow_sql_trend_items=None, interval_millis=None, total_count=None):
        r"""ExportSlowSqlTrendDetailsResponse

        The model defined in huaweicloud sdk

        :param slow_sql_trend_items: 慢SQL数量趋势。
        :type slow_sql_trend_items: list[:class:`huaweicloudsdkdas.v3.SlowSqlTrendItem`]
        :param interval_millis: 返回列表两个时间点之间的时间间隔。总查询时长3小时之内间隔1分钟，3小时到6小时范围内间隔5分钟，6小时到12小时范围内间隔30分钟，12小时以上间隔1小时。单位为毫秒。
        :type interval_millis: int
        :param total_count: 趋势数据总数。
        :type total_count: int
        """
        
        super(ExportSlowSqlTrendDetailsResponse, self).__init__()

        self._slow_sql_trend_items = None
        self._interval_millis = None
        self._total_count = None
        self.discriminator = None

        if slow_sql_trend_items is not None:
            self.slow_sql_trend_items = slow_sql_trend_items
        if interval_millis is not None:
            self.interval_millis = interval_millis
        if total_count is not None:
            self.total_count = total_count

    @property
    def slow_sql_trend_items(self):
        r"""Gets the slow_sql_trend_items of this ExportSlowSqlTrendDetailsResponse.

        慢SQL数量趋势。

        :return: The slow_sql_trend_items of this ExportSlowSqlTrendDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowSqlTrendItem`]
        """
        return self._slow_sql_trend_items

    @slow_sql_trend_items.setter
    def slow_sql_trend_items(self, slow_sql_trend_items):
        r"""Sets the slow_sql_trend_items of this ExportSlowSqlTrendDetailsResponse.

        慢SQL数量趋势。

        :param slow_sql_trend_items: The slow_sql_trend_items of this ExportSlowSqlTrendDetailsResponse.
        :type slow_sql_trend_items: list[:class:`huaweicloudsdkdas.v3.SlowSqlTrendItem`]
        """
        self._slow_sql_trend_items = slow_sql_trend_items

    @property
    def interval_millis(self):
        r"""Gets the interval_millis of this ExportSlowSqlTrendDetailsResponse.

        返回列表两个时间点之间的时间间隔。总查询时长3小时之内间隔1分钟，3小时到6小时范围内间隔5分钟，6小时到12小时范围内间隔30分钟，12小时以上间隔1小时。单位为毫秒。

        :return: The interval_millis of this ExportSlowSqlTrendDetailsResponse.
        :rtype: int
        """
        return self._interval_millis

    @interval_millis.setter
    def interval_millis(self, interval_millis):
        r"""Sets the interval_millis of this ExportSlowSqlTrendDetailsResponse.

        返回列表两个时间点之间的时间间隔。总查询时长3小时之内间隔1分钟，3小时到6小时范围内间隔5分钟，6小时到12小时范围内间隔30分钟，12小时以上间隔1小时。单位为毫秒。

        :param interval_millis: The interval_millis of this ExportSlowSqlTrendDetailsResponse.
        :type interval_millis: int
        """
        self._interval_millis = interval_millis

    @property
    def total_count(self):
        r"""Gets the total_count of this ExportSlowSqlTrendDetailsResponse.

        趋势数据总数。

        :return: The total_count of this ExportSlowSqlTrendDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ExportSlowSqlTrendDetailsResponse.

        趋势数据总数。

        :param total_count: The total_count of this ExportSlowSqlTrendDetailsResponse.
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
        if not isinstance(other, ExportSlowSqlTrendDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
