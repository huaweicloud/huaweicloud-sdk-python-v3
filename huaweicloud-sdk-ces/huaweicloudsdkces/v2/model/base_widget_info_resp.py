# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseWidgetInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'metrics': 'list[WidgetMetricResp]',
        'title': 'str',
        'threshold': 'float',
        'threshold_enabled': 'bool',
        'view': 'str',
        'metric_display_mode': 'str',
        'properties': 'BaseWidgetInfoRespProperties',
        'location': 'BaseWidgetInfoRespLocation',
        'unit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'metrics': 'metrics',
        'title': 'title',
        'threshold': 'threshold',
        'threshold_enabled': 'threshold_enabled',
        'view': 'view',
        'metric_display_mode': 'metric_display_mode',
        'properties': 'properties',
        'location': 'location',
        'unit': 'unit'
    }

    def __init__(self, group_id=None, metrics=None, title=None, threshold=None, threshold_enabled=None, view=None, metric_display_mode=None, properties=None, location=None, unit=None):
        r"""BaseWidgetInfoResp

        The model defined in huaweicloud sdk

        :param group_id: **参数解释** 视图分组id **取值范围** 字符串必须以dg开头，包含22个字母和数字，长度为24个字符或者为default，default代表不分组 
        :type group_id: str
        :param metrics: **参数解释** 指标列表 
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetricResp`]
        :param title: **参数解释** 监控视图标题 **取值范围** 长度为[1,128]个字符，允许包括以下内容：1、中文汉字；2、拉丁字母；3、英文大小写字母；4、数字(0-9)；5、符号： ” \&quot; ≤ &lt; &gt; &amp; % _ : / ; “ &#39; ? + , ~ ， （ ） º ( ) [ . - 
        :type title: str
        :param threshold: **参数解释** 监控视图指标的阈值 **取值范围** 最小值为0，最大值为1.7976931348623157e+308 
        :type threshold: float
        :param threshold_enabled: **参数解释** 阈值是否展示 **取值范围** - true:展示 - false:不展示 
        :type threshold_enabled: bool
        :param view: **参数解释** 监控视图图表类型 **取值范围** - bar:条形图 - line:折线图 - bar_chart:柱状图 - table:表格 - circular_bar:环形柱状图 - area_chart:面积图 
        :type view: str
        :param metric_display_mode: **参数解释** 指标展示类型 **取值范围** - single:单指标展示 - multiple:多指标展示 
        :type metric_display_mode: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespProperties`
        :param location: 
        :type location: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespLocation`
        :param unit: **参数解释** 单位 **取值范围** 长度为[0,32]个字符 
        :type unit: str
        """
        
        

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
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if metrics is not None:
            self.metrics = metrics
        if title is not None:
            self.title = title
        if threshold is not None:
            self.threshold = threshold
        if threshold_enabled is not None:
            self.threshold_enabled = threshold_enabled
        if view is not None:
            self.view = view
        if metric_display_mode is not None:
            self.metric_display_mode = metric_display_mode
        if properties is not None:
            self.properties = properties
        if location is not None:
            self.location = location
        if unit is not None:
            self.unit = unit

    @property
    def group_id(self):
        r"""Gets the group_id of this BaseWidgetInfoResp.

        **参数解释** 视图分组id **取值范围** 字符串必须以dg开头，包含22个字母和数字，长度为24个字符或者为default，default代表不分组 

        :return: The group_id of this BaseWidgetInfoResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this BaseWidgetInfoResp.

        **参数解释** 视图分组id **取值范围** 字符串必须以dg开头，包含22个字母和数字，长度为24个字符或者为default，default代表不分组 

        :param group_id: The group_id of this BaseWidgetInfoResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def metrics(self):
        r"""Gets the metrics of this BaseWidgetInfoResp.

        **参数解释** 指标列表 

        :return: The metrics of this BaseWidgetInfoResp.
        :rtype: list[:class:`huaweicloudsdkces.v2.WidgetMetricResp`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this BaseWidgetInfoResp.

        **参数解释** 指标列表 

        :param metrics: The metrics of this BaseWidgetInfoResp.
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetricResp`]
        """
        self._metrics = metrics

    @property
    def title(self):
        r"""Gets the title of this BaseWidgetInfoResp.

        **参数解释** 监控视图标题 **取值范围** 长度为[1,128]个字符，允许包括以下内容：1、中文汉字；2、拉丁字母；3、英文大小写字母；4、数字(0-9)；5、符号： ” \" ≤ < > & % _ : / ; “ ' ? + , ~ ， （ ） º ( ) [ . - 

        :return: The title of this BaseWidgetInfoResp.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this BaseWidgetInfoResp.

        **参数解释** 监控视图标题 **取值范围** 长度为[1,128]个字符，允许包括以下内容：1、中文汉字；2、拉丁字母；3、英文大小写字母；4、数字(0-9)；5、符号： ” \" ≤ < > & % _ : / ; “ ' ? + , ~ ， （ ） º ( ) [ . - 

        :param title: The title of this BaseWidgetInfoResp.
        :type title: str
        """
        self._title = title

    @property
    def threshold(self):
        r"""Gets the threshold of this BaseWidgetInfoResp.

        **参数解释** 监控视图指标的阈值 **取值范围** 最小值为0，最大值为1.7976931348623157e+308 

        :return: The threshold of this BaseWidgetInfoResp.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this BaseWidgetInfoResp.

        **参数解释** 监控视图指标的阈值 **取值范围** 最小值为0，最大值为1.7976931348623157e+308 

        :param threshold: The threshold of this BaseWidgetInfoResp.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def threshold_enabled(self):
        r"""Gets the threshold_enabled of this BaseWidgetInfoResp.

        **参数解释** 阈值是否展示 **取值范围** - true:展示 - false:不展示 

        :return: The threshold_enabled of this BaseWidgetInfoResp.
        :rtype: bool
        """
        return self._threshold_enabled

    @threshold_enabled.setter
    def threshold_enabled(self, threshold_enabled):
        r"""Sets the threshold_enabled of this BaseWidgetInfoResp.

        **参数解释** 阈值是否展示 **取值范围** - true:展示 - false:不展示 

        :param threshold_enabled: The threshold_enabled of this BaseWidgetInfoResp.
        :type threshold_enabled: bool
        """
        self._threshold_enabled = threshold_enabled

    @property
    def view(self):
        r"""Gets the view of this BaseWidgetInfoResp.

        **参数解释** 监控视图图表类型 **取值范围** - bar:条形图 - line:折线图 - bar_chart:柱状图 - table:表格 - circular_bar:环形柱状图 - area_chart:面积图 

        :return: The view of this BaseWidgetInfoResp.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        r"""Sets the view of this BaseWidgetInfoResp.

        **参数解释** 监控视图图表类型 **取值范围** - bar:条形图 - line:折线图 - bar_chart:柱状图 - table:表格 - circular_bar:环形柱状图 - area_chart:面积图 

        :param view: The view of this BaseWidgetInfoResp.
        :type view: str
        """
        self._view = view

    @property
    def metric_display_mode(self):
        r"""Gets the metric_display_mode of this BaseWidgetInfoResp.

        **参数解释** 指标展示类型 **取值范围** - single:单指标展示 - multiple:多指标展示 

        :return: The metric_display_mode of this BaseWidgetInfoResp.
        :rtype: str
        """
        return self._metric_display_mode

    @metric_display_mode.setter
    def metric_display_mode(self, metric_display_mode):
        r"""Sets the metric_display_mode of this BaseWidgetInfoResp.

        **参数解释** 指标展示类型 **取值范围** - single:单指标展示 - multiple:多指标展示 

        :param metric_display_mode: The metric_display_mode of this BaseWidgetInfoResp.
        :type metric_display_mode: str
        """
        self._metric_display_mode = metric_display_mode

    @property
    def properties(self):
        r"""Gets the properties of this BaseWidgetInfoResp.

        :return: The properties of this BaseWidgetInfoResp.
        :rtype: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this BaseWidgetInfoResp.

        :param properties: The properties of this BaseWidgetInfoResp.
        :type properties: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespProperties`
        """
        self._properties = properties

    @property
    def location(self):
        r"""Gets the location of this BaseWidgetInfoResp.

        :return: The location of this BaseWidgetInfoResp.
        :rtype: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this BaseWidgetInfoResp.

        :param location: The location of this BaseWidgetInfoResp.
        :type location: :class:`huaweicloudsdkces.v2.BaseWidgetInfoRespLocation`
        """
        self._location = location

    @property
    def unit(self):
        r"""Gets the unit of this BaseWidgetInfoResp.

        **参数解释** 单位 **取值范围** 长度为[0,32]个字符 

        :return: The unit of this BaseWidgetInfoResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this BaseWidgetInfoResp.

        **参数解释** 单位 **取值范围** 长度为[0,32]个字符 

        :param unit: The unit of this BaseWidgetInfoResp.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, BaseWidgetInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
