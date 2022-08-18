# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'period': 'str',
        'option': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'period': 'period',
        'option': 'option'
    }

    def __init__(self, filter=None, period=None, option=None):
        """ListStatisticsRequest

        The model defined in huaweicloud sdk

        :param filter: 参数过滤器。 monitor_data: 查询统计信息。 monthly_report：查询月度统计信息。
        :type filter: str
        :param period: 时间段单位为分钟，与filter参数metric配合使用。
        :type period: str
        :param option: 月度统计的维度，filter参数取值为monthly_report时才生效。 当取值不在以上范围时，默认取\&quot;0\&quot;。 - \&quot;0\&quot;: 表示统计本月。 - \&quot;1\&quot;: 表示统计上月。 - \&quot;2\&quot;: 表示统计最近三个月。 - \&quot;3\&quot;: 表示统计最近六个月。
        :type option: str
        """
        
        

        self._filter = None
        self._period = None
        self._option = None
        self.discriminator = None

        self.filter = filter
        if period is not None:
            self.period = period
        if option is not None:
            self.option = option

    @property
    def filter(self):
        """Gets the filter of this ListStatisticsRequest.

        参数过滤器。 monitor_data: 查询统计信息。 monthly_report：查询月度统计信息。

        :return: The filter of this ListStatisticsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListStatisticsRequest.

        参数过滤器。 monitor_data: 查询统计信息。 monthly_report：查询月度统计信息。

        :param filter: The filter of this ListStatisticsRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this ListStatisticsRequest.

        时间段单位为分钟，与filter参数metric配合使用。

        :return: The period of this ListStatisticsRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ListStatisticsRequest.

        时间段单位为分钟，与filter参数metric配合使用。

        :param period: The period of this ListStatisticsRequest.
        :type period: str
        """
        self._period = period

    @property
    def option(self):
        """Gets the option of this ListStatisticsRequest.

        月度统计的维度，filter参数取值为monthly_report时才生效。 当取值不在以上范围时，默认取\"0\"。 - \"0\": 表示统计本月。 - \"1\": 表示统计上月。 - \"2\": 表示统计最近三个月。 - \"3\": 表示统计最近六个月。

        :return: The option of this ListStatisticsRequest.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ListStatisticsRequest.

        月度统计的维度，filter参数取值为monthly_report时才生效。 当取值不在以上范围时，默认取\"0\"。 - \"0\": 表示统计本月。 - \"1\": 表示统计上月。 - \"2\": 表示统计最近三个月。 - \"3\": 表示统计最近六个月。

        :param option: The option of this ListStatisticsRequest.
        :type option: str
        """
        self._option = option

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
        if not isinstance(other, ListStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
