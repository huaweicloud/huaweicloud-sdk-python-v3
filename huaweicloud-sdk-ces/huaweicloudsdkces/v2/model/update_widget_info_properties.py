# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWidgetInfoProperties:

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
        'top_n': 'int',
        'order': 'str',
        'description': 'str',
        'last_week_compare_enable': 'bool',
        'yesterday_compare_enable': 'bool',
        'legend_location': 'str',
        'legend_values': 'list[str]',
        'thresholds': 'list[ThresholdInfo]',
        'is_all_compare_enable': 'bool'
    }

    attribute_map = {
        'filter': 'filter',
        'top_n': 'topN',
        'order': 'order',
        'description': 'description',
        'last_week_compare_enable': 'last_week_compare_enable',
        'yesterday_compare_enable': 'yesterday_compare_enable',
        'legend_location': 'legend_location',
        'legend_values': 'legend_values',
        'thresholds': 'thresholds',
        'is_all_compare_enable': 'is_all_compare_enable'
    }

    def __init__(self, filter=None, top_n=None, order=None, description=None, last_week_compare_enable=None, yesterday_compare_enable=None, legend_location=None, legend_values=None, thresholds=None, is_all_compare_enable=None):
        r"""UpdateWidgetInfoProperties

        The model defined in huaweicloud sdk

        :param filter: 聚合类型，目前只有TopN这一种类型，折线图不支持该参数
        :type filter: str
        :param top_n: Top值前N个;折线图时表示随机展示的时序数据条数
        :type top_n: int
        :param order: 排序字段，asc正序，desc倒序，折线图不支持该参数
        :type order: str
        :param description: 监控视图的描述信息
        :type description: str
        :param last_week_compare_enable: 是否展示同比（上周同一时间）数据，true:展示，false:不展示
        :type last_week_compare_enable: bool
        :param yesterday_compare_enable: 是否展示环比（昨天同一时间）数据，true:展示，false:不展示
        :type yesterday_compare_enable: bool
        :param legend_location: 图例位置标记，hide表示隐藏图例，right表示图例放在监控视图右侧，bottom表示图例放在监控视图底部，表格不支持该参数
        :type legend_location: str
        :param legend_values: 当前时序数据需要在图例中展示的统计值名称列表，表格不支持该参数，条形图和柱状图仅支持选择当前值
        :type legend_values: list[str]
        :param thresholds: 监控视图的阈值辅助线配置
        :type thresholds: list[:class:`huaweicloudsdkces.v2.ThresholdInfo`]
        :param is_all_compare_enable: 同比环比总开关是否生效;true:生效；false:不生效
        :type is_all_compare_enable: bool
        """
        
        

        self._filter = None
        self._top_n = None
        self._order = None
        self._description = None
        self._last_week_compare_enable = None
        self._yesterday_compare_enable = None
        self._legend_location = None
        self._legend_values = None
        self._thresholds = None
        self._is_all_compare_enable = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if top_n is not None:
            self.top_n = top_n
        if order is not None:
            self.order = order
        if description is not None:
            self.description = description
        if last_week_compare_enable is not None:
            self.last_week_compare_enable = last_week_compare_enable
        if yesterday_compare_enable is not None:
            self.yesterday_compare_enable = yesterday_compare_enable
        if legend_location is not None:
            self.legend_location = legend_location
        if legend_values is not None:
            self.legend_values = legend_values
        if thresholds is not None:
            self.thresholds = thresholds
        if is_all_compare_enable is not None:
            self.is_all_compare_enable = is_all_compare_enable

    @property
    def filter(self):
        r"""Gets the filter of this UpdateWidgetInfoProperties.

        聚合类型，目前只有TopN这一种类型，折线图不支持该参数

        :return: The filter of this UpdateWidgetInfoProperties.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this UpdateWidgetInfoProperties.

        聚合类型，目前只有TopN这一种类型，折线图不支持该参数

        :param filter: The filter of this UpdateWidgetInfoProperties.
        :type filter: str
        """
        self._filter = filter

    @property
    def top_n(self):
        r"""Gets the top_n of this UpdateWidgetInfoProperties.

        Top值前N个;折线图时表示随机展示的时序数据条数

        :return: The top_n of this UpdateWidgetInfoProperties.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        r"""Sets the top_n of this UpdateWidgetInfoProperties.

        Top值前N个;折线图时表示随机展示的时序数据条数

        :param top_n: The top_n of this UpdateWidgetInfoProperties.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def order(self):
        r"""Gets the order of this UpdateWidgetInfoProperties.

        排序字段，asc正序，desc倒序，折线图不支持该参数

        :return: The order of this UpdateWidgetInfoProperties.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this UpdateWidgetInfoProperties.

        排序字段，asc正序，desc倒序，折线图不支持该参数

        :param order: The order of this UpdateWidgetInfoProperties.
        :type order: str
        """
        self._order = order

    @property
    def description(self):
        r"""Gets the description of this UpdateWidgetInfoProperties.

        监控视图的描述信息

        :return: The description of this UpdateWidgetInfoProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWidgetInfoProperties.

        监控视图的描述信息

        :param description: The description of this UpdateWidgetInfoProperties.
        :type description: str
        """
        self._description = description

    @property
    def last_week_compare_enable(self):
        r"""Gets the last_week_compare_enable of this UpdateWidgetInfoProperties.

        是否展示同比（上周同一时间）数据，true:展示，false:不展示

        :return: The last_week_compare_enable of this UpdateWidgetInfoProperties.
        :rtype: bool
        """
        return self._last_week_compare_enable

    @last_week_compare_enable.setter
    def last_week_compare_enable(self, last_week_compare_enable):
        r"""Sets the last_week_compare_enable of this UpdateWidgetInfoProperties.

        是否展示同比（上周同一时间）数据，true:展示，false:不展示

        :param last_week_compare_enable: The last_week_compare_enable of this UpdateWidgetInfoProperties.
        :type last_week_compare_enable: bool
        """
        self._last_week_compare_enable = last_week_compare_enable

    @property
    def yesterday_compare_enable(self):
        r"""Gets the yesterday_compare_enable of this UpdateWidgetInfoProperties.

        是否展示环比（昨天同一时间）数据，true:展示，false:不展示

        :return: The yesterday_compare_enable of this UpdateWidgetInfoProperties.
        :rtype: bool
        """
        return self._yesterday_compare_enable

    @yesterday_compare_enable.setter
    def yesterday_compare_enable(self, yesterday_compare_enable):
        r"""Sets the yesterday_compare_enable of this UpdateWidgetInfoProperties.

        是否展示环比（昨天同一时间）数据，true:展示，false:不展示

        :param yesterday_compare_enable: The yesterday_compare_enable of this UpdateWidgetInfoProperties.
        :type yesterday_compare_enable: bool
        """
        self._yesterday_compare_enable = yesterday_compare_enable

    @property
    def legend_location(self):
        r"""Gets the legend_location of this UpdateWidgetInfoProperties.

        图例位置标记，hide表示隐藏图例，right表示图例放在监控视图右侧，bottom表示图例放在监控视图底部，表格不支持该参数

        :return: The legend_location of this UpdateWidgetInfoProperties.
        :rtype: str
        """
        return self._legend_location

    @legend_location.setter
    def legend_location(self, legend_location):
        r"""Sets the legend_location of this UpdateWidgetInfoProperties.

        图例位置标记，hide表示隐藏图例，right表示图例放在监控视图右侧，bottom表示图例放在监控视图底部，表格不支持该参数

        :param legend_location: The legend_location of this UpdateWidgetInfoProperties.
        :type legend_location: str
        """
        self._legend_location = legend_location

    @property
    def legend_values(self):
        r"""Gets the legend_values of this UpdateWidgetInfoProperties.

        当前时序数据需要在图例中展示的统计值名称列表，表格不支持该参数，条形图和柱状图仅支持选择当前值

        :return: The legend_values of this UpdateWidgetInfoProperties.
        :rtype: list[str]
        """
        return self._legend_values

    @legend_values.setter
    def legend_values(self, legend_values):
        r"""Sets the legend_values of this UpdateWidgetInfoProperties.

        当前时序数据需要在图例中展示的统计值名称列表，表格不支持该参数，条形图和柱状图仅支持选择当前值

        :param legend_values: The legend_values of this UpdateWidgetInfoProperties.
        :type legend_values: list[str]
        """
        self._legend_values = legend_values

    @property
    def thresholds(self):
        r"""Gets the thresholds of this UpdateWidgetInfoProperties.

        监控视图的阈值辅助线配置

        :return: The thresholds of this UpdateWidgetInfoProperties.
        :rtype: list[:class:`huaweicloudsdkces.v2.ThresholdInfo`]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        r"""Sets the thresholds of this UpdateWidgetInfoProperties.

        监控视图的阈值辅助线配置

        :param thresholds: The thresholds of this UpdateWidgetInfoProperties.
        :type thresholds: list[:class:`huaweicloudsdkces.v2.ThresholdInfo`]
        """
        self._thresholds = thresholds

    @property
    def is_all_compare_enable(self):
        r"""Gets the is_all_compare_enable of this UpdateWidgetInfoProperties.

        同比环比总开关是否生效;true:生效；false:不生效

        :return: The is_all_compare_enable of this UpdateWidgetInfoProperties.
        :rtype: bool
        """
        return self._is_all_compare_enable

    @is_all_compare_enable.setter
    def is_all_compare_enable(self, is_all_compare_enable):
        r"""Sets the is_all_compare_enable of this UpdateWidgetInfoProperties.

        同比环比总开关是否生效;true:生效；false:不生效

        :param is_all_compare_enable: The is_all_compare_enable of this UpdateWidgetInfoProperties.
        :type is_all_compare_enable: bool
        """
        self._is_all_compare_enable = is_all_compare_enable

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
        if not isinstance(other, UpdateWidgetInfoProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
