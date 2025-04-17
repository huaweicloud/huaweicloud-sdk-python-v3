# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WidgetInfoWithId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'widget_id': 'str',
        'group_id': 'str',
        'metrics': 'list[WidgetMetric]',
        'title': 'str',
        'threshold': 'float',
        'threshold_enabled': 'bool',
        'view': 'str',
        'metric_display_mode': 'str',
        'properties': 'BaseWidgetInfoProperties',
        'location': 'UpdateWidgetInfoLocation',
        'unit': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'widget_id': 'widget_id',
        'group_id': 'group_id',
        'metrics': 'metrics',
        'title': 'title',
        'threshold': 'threshold',
        'threshold_enabled': 'threshold_enabled',
        'view': 'view',
        'metric_display_mode': 'metric_display_mode',
        'properties': 'properties',
        'location': 'location',
        'unit': 'unit',
        'create_time': 'create_time'
    }

    def __init__(self, widget_id=None, group_id=None, metrics=None, title=None, threshold=None, threshold_enabled=None, view=None, metric_display_mode=None, properties=None, location=None, unit=None, create_time=None):
        r"""WidgetInfoWithId

        The model defined in huaweicloud sdk

        :param widget_id: 视图id
        :type widget_id: str
        :param group_id: 视图分区id
        :type group_id: str
        :param metrics: 指标列表
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        :param title: 监控视图标题
        :type title: str
        :param threshold: 监控视图指标的阈值
        :type threshold: float
        :param threshold_enabled: 阈值是否展示，true:展示，false:不展示
        :type threshold_enabled: bool
        :param view: 监控视图图表类型, bar条形图，line折线图，bar_chart柱状图，table表格，circular_bar环形柱状图，area_chart面积图
        :type view: str
        :param metric_display_mode: 指标展示类型，single 单指标展示，multiple 多指标展示
        :type metric_display_mode: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkces.v2.BaseWidgetInfoProperties`
        :param location: 
        :type location: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        :param unit: 单位
        :type unit: str
        :param create_time: 监控看板创建时间
        :type create_time: int
        """
        
        

        self._widget_id = None
        self._group_id = None
        self._metrics = None
        self._title = None
        self._threshold = None
        self._threshold_enabled = None
        self._view = None
        self._metric_display_mode = None
        self._properties = None
        self._location = None
        self._unit = None
        self._create_time = None
        self.discriminator = None

        if widget_id is not None:
            self.widget_id = widget_id
        if group_id is not None:
            self.group_id = group_id
        self.metrics = metrics
        self.title = title
        if threshold is not None:
            self.threshold = threshold
        self.threshold_enabled = threshold_enabled
        self.view = view
        self.metric_display_mode = metric_display_mode
        if properties is not None:
            self.properties = properties
        self.location = location
        if unit is not None:
            self.unit = unit
        if create_time is not None:
            self.create_time = create_time

    @property
    def widget_id(self):
        r"""Gets the widget_id of this WidgetInfoWithId.

        视图id

        :return: The widget_id of this WidgetInfoWithId.
        :rtype: str
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        r"""Sets the widget_id of this WidgetInfoWithId.

        视图id

        :param widget_id: The widget_id of this WidgetInfoWithId.
        :type widget_id: str
        """
        self._widget_id = widget_id

    @property
    def group_id(self):
        r"""Gets the group_id of this WidgetInfoWithId.

        视图分区id

        :return: The group_id of this WidgetInfoWithId.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this WidgetInfoWithId.

        视图分区id

        :param group_id: The group_id of this WidgetInfoWithId.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def metrics(self):
        r"""Gets the metrics of this WidgetInfoWithId.

        指标列表

        :return: The metrics of this WidgetInfoWithId.
        :rtype: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this WidgetInfoWithId.

        指标列表

        :param metrics: The metrics of this WidgetInfoWithId.
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        """
        self._metrics = metrics

    @property
    def title(self):
        r"""Gets the title of this WidgetInfoWithId.

        监控视图标题

        :return: The title of this WidgetInfoWithId.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WidgetInfoWithId.

        监控视图标题

        :param title: The title of this WidgetInfoWithId.
        :type title: str
        """
        self._title = title

    @property
    def threshold(self):
        r"""Gets the threshold of this WidgetInfoWithId.

        监控视图指标的阈值

        :return: The threshold of this WidgetInfoWithId.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this WidgetInfoWithId.

        监控视图指标的阈值

        :param threshold: The threshold of this WidgetInfoWithId.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def threshold_enabled(self):
        r"""Gets the threshold_enabled of this WidgetInfoWithId.

        阈值是否展示，true:展示，false:不展示

        :return: The threshold_enabled of this WidgetInfoWithId.
        :rtype: bool
        """
        return self._threshold_enabled

    @threshold_enabled.setter
    def threshold_enabled(self, threshold_enabled):
        r"""Sets the threshold_enabled of this WidgetInfoWithId.

        阈值是否展示，true:展示，false:不展示

        :param threshold_enabled: The threshold_enabled of this WidgetInfoWithId.
        :type threshold_enabled: bool
        """
        self._threshold_enabled = threshold_enabled

    @property
    def view(self):
        r"""Gets the view of this WidgetInfoWithId.

        监控视图图表类型, bar条形图，line折线图，bar_chart柱状图，table表格，circular_bar环形柱状图，area_chart面积图

        :return: The view of this WidgetInfoWithId.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this WidgetInfoWithId.

        监控视图图表类型, bar条形图，line折线图，bar_chart柱状图，table表格，circular_bar环形柱状图，area_chart面积图

        :param view: The view of this WidgetInfoWithId.
        :type view: str
        """
        self._view = view

    @property
    def metric_display_mode(self):
        r"""Gets the metric_display_mode of this WidgetInfoWithId.

        指标展示类型，single 单指标展示，multiple 多指标展示

        :return: The metric_display_mode of this WidgetInfoWithId.
        :rtype: str
        """
        return self._metric_display_mode

    @metric_display_mode.setter
    def metric_display_mode(self, metric_display_mode):
        r"""Sets the metric_display_mode of this WidgetInfoWithId.

        指标展示类型，single 单指标展示，multiple 多指标展示

        :param metric_display_mode: The metric_display_mode of this WidgetInfoWithId.
        :type metric_display_mode: str
        """
        self._metric_display_mode = metric_display_mode

    @property
    def properties(self):
        r"""Gets the properties of this WidgetInfoWithId.

        :return: The properties of this WidgetInfoWithId.
        :rtype: :class:`huaweicloudsdkces.v2.BaseWidgetInfoProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this WidgetInfoWithId.

        :param properties: The properties of this WidgetInfoWithId.
        :type properties: :class:`huaweicloudsdkces.v2.BaseWidgetInfoProperties`
        """
        self._properties = properties

    @property
    def location(self):
        r"""Gets the location of this WidgetInfoWithId.

        :return: The location of this WidgetInfoWithId.
        :rtype: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this WidgetInfoWithId.

        :param location: The location of this WidgetInfoWithId.
        :type location: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        """
        self._location = location

    @property
    def unit(self):
        r"""Gets the unit of this WidgetInfoWithId.

        单位

        :return: The unit of this WidgetInfoWithId.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this WidgetInfoWithId.

        单位

        :param unit: The unit of this WidgetInfoWithId.
        :type unit: str
        """
        self._unit = unit

    @property
    def create_time(self):
        r"""Gets the create_time of this WidgetInfoWithId.

        监控看板创建时间

        :return: The create_time of this WidgetInfoWithId.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WidgetInfoWithId.

        监控看板创建时间

        :param create_time: The create_time of this WidgetInfoWithId.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, WidgetInfoWithId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
