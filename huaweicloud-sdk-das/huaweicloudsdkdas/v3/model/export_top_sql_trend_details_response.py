# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTopSqlTrendDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval_millis': 'int',
        'top_sql_trend_items': 'list[TopSqlTrendItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'interval_millis': 'interval_millis',
        'top_sql_trend_items': 'top_sql_trend_items',
        'total_count': 'total_count'
    }

    def __init__(self, interval_millis=None, top_sql_trend_items=None, total_count=None):
        """ExportTopSqlTrendDetailsResponse

        The model defined in huaweicloud sdk

        :param interval_millis: 返回列表两个时间点之间的时间间隔。总查询时长一小时之内间隔10s，一小时到六小时范围内间隔60s，六小时以上间隔300s。单位为毫秒。
        :type interval_millis: int
        :param top_sql_trend_items: SQL执行耗时区间数据。
        :type top_sql_trend_items: list[:class:`huaweicloudsdkdas.v3.TopSqlTrendItem`]
        :param total_count: 耗时区间数据总数。
        :type total_count: int
        """
        
        super(ExportTopSqlTrendDetailsResponse, self).__init__()

        self._interval_millis = None
        self._top_sql_trend_items = None
        self._total_count = None
        self.discriminator = None

        if interval_millis is not None:
            self.interval_millis = interval_millis
        if top_sql_trend_items is not None:
            self.top_sql_trend_items = top_sql_trend_items
        if total_count is not None:
            self.total_count = total_count

    @property
    def interval_millis(self):
        """Gets the interval_millis of this ExportTopSqlTrendDetailsResponse.

        返回列表两个时间点之间的时间间隔。总查询时长一小时之内间隔10s，一小时到六小时范围内间隔60s，六小时以上间隔300s。单位为毫秒。

        :return: The interval_millis of this ExportTopSqlTrendDetailsResponse.
        :rtype: int
        """
        return self._interval_millis

    @interval_millis.setter
    def interval_millis(self, interval_millis):
        """Sets the interval_millis of this ExportTopSqlTrendDetailsResponse.

        返回列表两个时间点之间的时间间隔。总查询时长一小时之内间隔10s，一小时到六小时范围内间隔60s，六小时以上间隔300s。单位为毫秒。

        :param interval_millis: The interval_millis of this ExportTopSqlTrendDetailsResponse.
        :type interval_millis: int
        """
        self._interval_millis = interval_millis

    @property
    def top_sql_trend_items(self):
        """Gets the top_sql_trend_items of this ExportTopSqlTrendDetailsResponse.

        SQL执行耗时区间数据。

        :return: The top_sql_trend_items of this ExportTopSqlTrendDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopSqlTrendItem`]
        """
        return self._top_sql_trend_items

    @top_sql_trend_items.setter
    def top_sql_trend_items(self, top_sql_trend_items):
        """Sets the top_sql_trend_items of this ExportTopSqlTrendDetailsResponse.

        SQL执行耗时区间数据。

        :param top_sql_trend_items: The top_sql_trend_items of this ExportTopSqlTrendDetailsResponse.
        :type top_sql_trend_items: list[:class:`huaweicloudsdkdas.v3.TopSqlTrendItem`]
        """
        self._top_sql_trend_items = top_sql_trend_items

    @property
    def total_count(self):
        """Gets the total_count of this ExportTopSqlTrendDetailsResponse.

        耗时区间数据总数。

        :return: The total_count of this ExportTopSqlTrendDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ExportTopSqlTrendDetailsResponse.

        耗时区间数据总数。

        :param total_count: The total_count of this ExportTopSqlTrendDetailsResponse.
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
        if not isinstance(other, ExportTopSqlTrendDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
