# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendInfo:

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
        'display_time': 'int',
        'refresh_time': 'int',
        '_from': 'int',
        'to': 'int',
        'screen_color': 'str',
        'enable_screen_auto_play': 'bool',
        'time_interval': 'int',
        'enable_legend': 'bool',
        'full_screen_widget_num': 'int'
    }

    attribute_map = {
        'filter': 'filter',
        'period': 'period',
        'display_time': 'display_time',
        'refresh_time': 'refresh_time',
        '_from': 'from',
        'to': 'to',
        'screen_color': 'screen_color',
        'enable_screen_auto_play': 'enable_screen_auto_play',
        'time_interval': 'time_interval',
        'enable_legend': 'enable_legend',
        'full_screen_widget_num': 'full_screen_widget_num'
    }

    def __init__(self, filter=None, period=None, display_time=None, refresh_time=None, _from=None, to=None, screen_color=None, enable_screen_auto_play=None, time_interval=None, enable_legend=None, full_screen_widget_num=None):
        r"""ExtendInfo

        The model defined in huaweicloud sdk

        :param filter: 表示指标聚合方式，average表示平均值，min表示最小值，max表示最大值，sum表示求合
        :type filter: str
        :param period: &#39;表示指标聚合周期，{1:表示原始值，60:表示一分钟，300:表示5分钟，1200:表示20分钟，3600:表示1小时，14400:表示4小时，86400:表示1天}&#39; 
        :type period: str
        :param display_time: 展示时间，0表示使用自定义时间展示， 5分钟，15分钟，30分钟，1小时，2小时，3小时，12小时，24小时，7天，30天
        :type display_time: int
        :param refresh_time: 刷新时间 0秒表示不刷新,10秒，1分钟，5分钟，20分钟
        :type refresh_time: int
        :param _from: 开始时间
        :type _from: int
        :param to: 结束时间
        :type to: int
        :param screen_color: 监控大屏背景颜色
        :type screen_color: str
        :param enable_screen_auto_play: 监控大屏是否自动切换
        :type enable_screen_auto_play: bool
        :param time_interval: 监控大屏自动切换时间间隔，10000代表10s，30000代表30s，60000代表1min
        :type time_interval: int
        :param enable_legend: 是否开启图例
        :type enable_legend: bool
        :param full_screen_widget_num: 大屏展示视图数量, 可以取得值必须与console页面可选值保持一致
        :type full_screen_widget_num: int
        """
        
        

        self._filter = None
        self._period = None
        self._display_time = None
        self._refresh_time = None
        self.__from = None
        self._to = None
        self._screen_color = None
        self._enable_screen_auto_play = None
        self._time_interval = None
        self._enable_legend = None
        self._full_screen_widget_num = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if period is not None:
            self.period = period
        if display_time is not None:
            self.display_time = display_time
        if refresh_time is not None:
            self.refresh_time = refresh_time
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if screen_color is not None:
            self.screen_color = screen_color
        if enable_screen_auto_play is not None:
            self.enable_screen_auto_play = enable_screen_auto_play
        if time_interval is not None:
            self.time_interval = time_interval
        if enable_legend is not None:
            self.enable_legend = enable_legend
        if full_screen_widget_num is not None:
            self.full_screen_widget_num = full_screen_widget_num

    @property
    def filter(self):
        r"""Gets the filter of this ExtendInfo.

        表示指标聚合方式，average表示平均值，min表示最小值，max表示最大值，sum表示求合

        :return: The filter of this ExtendInfo.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ExtendInfo.

        表示指标聚合方式，average表示平均值，min表示最小值，max表示最大值，sum表示求合

        :param filter: The filter of this ExtendInfo.
        :type filter: str
        """
        self._filter = filter

    @property
    def period(self):
        r"""Gets the period of this ExtendInfo.

        '表示指标聚合周期，{1:表示原始值，60:表示一分钟，300:表示5分钟，1200:表示20分钟，3600:表示1小时，14400:表示4小时，86400:表示1天}' 

        :return: The period of this ExtendInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ExtendInfo.

        '表示指标聚合周期，{1:表示原始值，60:表示一分钟，300:表示5分钟，1200:表示20分钟，3600:表示1小时，14400:表示4小时，86400:表示1天}' 

        :param period: The period of this ExtendInfo.
        :type period: str
        """
        self._period = period

    @property
    def display_time(self):
        r"""Gets the display_time of this ExtendInfo.

        展示时间，0表示使用自定义时间展示， 5分钟，15分钟，30分钟，1小时，2小时，3小时，12小时，24小时，7天，30天

        :return: The display_time of this ExtendInfo.
        :rtype: int
        """
        return self._display_time

    @display_time.setter
    def display_time(self, display_time):
        r"""Sets the display_time of this ExtendInfo.

        展示时间，0表示使用自定义时间展示， 5分钟，15分钟，30分钟，1小时，2小时，3小时，12小时，24小时，7天，30天

        :param display_time: The display_time of this ExtendInfo.
        :type display_time: int
        """
        self._display_time = display_time

    @property
    def refresh_time(self):
        r"""Gets the refresh_time of this ExtendInfo.

        刷新时间 0秒表示不刷新,10秒，1分钟，5分钟，20分钟

        :return: The refresh_time of this ExtendInfo.
        :rtype: int
        """
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, refresh_time):
        r"""Sets the refresh_time of this ExtendInfo.

        刷新时间 0秒表示不刷新,10秒，1分钟，5分钟，20分钟

        :param refresh_time: The refresh_time of this ExtendInfo.
        :type refresh_time: int
        """
        self._refresh_time = refresh_time

    @property
    def _from(self):
        r"""Gets the _from of this ExtendInfo.

        开始时间

        :return: The _from of this ExtendInfo.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ExtendInfo.

        开始时间

        :param _from: The _from of this ExtendInfo.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ExtendInfo.

        结束时间

        :return: The to of this ExtendInfo.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ExtendInfo.

        结束时间

        :param to: The to of this ExtendInfo.
        :type to: int
        """
        self._to = to

    @property
    def screen_color(self):
        r"""Gets the screen_color of this ExtendInfo.

        监控大屏背景颜色

        :return: The screen_color of this ExtendInfo.
        :rtype: str
        """
        return self._screen_color

    @screen_color.setter
    def screen_color(self, screen_color):
        r"""Sets the screen_color of this ExtendInfo.

        监控大屏背景颜色

        :param screen_color: The screen_color of this ExtendInfo.
        :type screen_color: str
        """
        self._screen_color = screen_color

    @property
    def enable_screen_auto_play(self):
        r"""Gets the enable_screen_auto_play of this ExtendInfo.

        监控大屏是否自动切换

        :return: The enable_screen_auto_play of this ExtendInfo.
        :rtype: bool
        """
        return self._enable_screen_auto_play

    @enable_screen_auto_play.setter
    def enable_screen_auto_play(self, enable_screen_auto_play):
        r"""Sets the enable_screen_auto_play of this ExtendInfo.

        监控大屏是否自动切换

        :param enable_screen_auto_play: The enable_screen_auto_play of this ExtendInfo.
        :type enable_screen_auto_play: bool
        """
        self._enable_screen_auto_play = enable_screen_auto_play

    @property
    def time_interval(self):
        r"""Gets the time_interval of this ExtendInfo.

        监控大屏自动切换时间间隔，10000代表10s，30000代表30s，60000代表1min

        :return: The time_interval of this ExtendInfo.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        r"""Sets the time_interval of this ExtendInfo.

        监控大屏自动切换时间间隔，10000代表10s，30000代表30s，60000代表1min

        :param time_interval: The time_interval of this ExtendInfo.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def enable_legend(self):
        r"""Gets the enable_legend of this ExtendInfo.

        是否开启图例

        :return: The enable_legend of this ExtendInfo.
        :rtype: bool
        """
        return self._enable_legend

    @enable_legend.setter
    def enable_legend(self, enable_legend):
        r"""Sets the enable_legend of this ExtendInfo.

        是否开启图例

        :param enable_legend: The enable_legend of this ExtendInfo.
        :type enable_legend: bool
        """
        self._enable_legend = enable_legend

    @property
    def full_screen_widget_num(self):
        r"""Gets the full_screen_widget_num of this ExtendInfo.

        大屏展示视图数量, 可以取得值必须与console页面可选值保持一致

        :return: The full_screen_widget_num of this ExtendInfo.
        :rtype: int
        """
        return self._full_screen_widget_num

    @full_screen_widget_num.setter
    def full_screen_widget_num(self, full_screen_widget_num):
        r"""Sets the full_screen_widget_num of this ExtendInfo.

        大屏展示视图数量, 可以取得值必须与console页面可选值保持一致

        :param full_screen_widget_num: The full_screen_widget_num of this ExtendInfo.
        :type full_screen_widget_num: int
        """
        self._full_screen_widget_num = full_screen_widget_num

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
        if not isinstance(other, ExtendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
