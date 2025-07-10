# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddMetricNotifyRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'metric_name': 'str',
        'threshold': 'int',
        'comparison_operator': 'str',
        'interval': 'int',
        'enable': 'bool',
        'notify_object': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'metric_name': 'metric_name',
        'threshold': 'threshold',
        'comparison_operator': 'comparison_operator',
        'interval': 'interval',
        'enable': 'enable',
        'notify_object': 'notify_object'
    }

    def __init__(self, rule_id=None, metric_name=None, threshold=None, comparison_operator=None, interval=None, enable=None, notify_object=None):
        r"""AddMetricNotifyRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 规则ID。
        :type rule_id: str
        :param metric_name: 统计指标名称，目前仅支持固定值：desktop_idle_duration * &#x60;desktop_idle_duration&#x60; -  桌面空闲时长
        :type metric_name: str
        :param threshold: 统计持续周期(天)。
        :type threshold: int
        :param comparison_operator: 统计指标对应的统计值和threshold进行比较的条件 * &#x60;&gt;&#x3D;&#x60; -  统计指标大于等于threshold时触发 * &#x60;&gt;&#x60; -   统计指标大于threshold时触发 * &#x60;&#x3D;&#x60; -  统计指标等于threshold时触发 * &#x60;&lt;&#x3D;&#x60; -  统计指标小于等于threshold时触发 * &#x60;&lt;&#x60; -  统计指标小于threshold时触发
        :type comparison_operator: str
        :param interval: 触发通知后；下次通知的间隔时间;默认每天一次
        :type interval: int
        :param enable: 启禁用规则 true:启用 false:禁用。
        :type enable: bool
        :param notify_object: 通知对象;smn的主题urn。
        :type notify_object: str
        """
        
        super(AddMetricNotifyRuleResponse, self).__init__()

        self._rule_id = None
        self._metric_name = None
        self._threshold = None
        self._comparison_operator = None
        self._interval = None
        self._enable = None
        self._notify_object = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if metric_name is not None:
            self.metric_name = metric_name
        if threshold is not None:
            self.threshold = threshold
        if comparison_operator is not None:
            self.comparison_operator = comparison_operator
        if interval is not None:
            self.interval = interval
        if enable is not None:
            self.enable = enable
        if notify_object is not None:
            self.notify_object = notify_object

    @property
    def rule_id(self):
        r"""Gets the rule_id of this AddMetricNotifyRuleResponse.

        规则ID。

        :return: The rule_id of this AddMetricNotifyRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this AddMetricNotifyRuleResponse.

        规则ID。

        :param rule_id: The rule_id of this AddMetricNotifyRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AddMetricNotifyRuleResponse.

        统计指标名称，目前仅支持固定值：desktop_idle_duration * `desktop_idle_duration` -  桌面空闲时长

        :return: The metric_name of this AddMetricNotifyRuleResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AddMetricNotifyRuleResponse.

        统计指标名称，目前仅支持固定值：desktop_idle_duration * `desktop_idle_duration` -  桌面空闲时长

        :param metric_name: The metric_name of this AddMetricNotifyRuleResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def threshold(self):
        r"""Gets the threshold of this AddMetricNotifyRuleResponse.

        统计持续周期(天)。

        :return: The threshold of this AddMetricNotifyRuleResponse.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this AddMetricNotifyRuleResponse.

        统计持续周期(天)。

        :param threshold: The threshold of this AddMetricNotifyRuleResponse.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this AddMetricNotifyRuleResponse.

        统计指标对应的统计值和threshold进行比较的条件 * `>=` -  统计指标大于等于threshold时触发 * `>` -   统计指标大于threshold时触发 * `=` -  统计指标等于threshold时触发 * `<=` -  统计指标小于等于threshold时触发 * `<` -  统计指标小于threshold时触发

        :return: The comparison_operator of this AddMetricNotifyRuleResponse.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this AddMetricNotifyRuleResponse.

        统计指标对应的统计值和threshold进行比较的条件 * `>=` -  统计指标大于等于threshold时触发 * `>` -   统计指标大于threshold时触发 * `=` -  统计指标等于threshold时触发 * `<=` -  统计指标小于等于threshold时触发 * `<` -  统计指标小于threshold时触发

        :param comparison_operator: The comparison_operator of this AddMetricNotifyRuleResponse.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def interval(self):
        r"""Gets the interval of this AddMetricNotifyRuleResponse.

        触发通知后；下次通知的间隔时间;默认每天一次

        :return: The interval of this AddMetricNotifyRuleResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this AddMetricNotifyRuleResponse.

        触发通知后；下次通知的间隔时间;默认每天一次

        :param interval: The interval of this AddMetricNotifyRuleResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def enable(self):
        r"""Gets the enable of this AddMetricNotifyRuleResponse.

        启禁用规则 true:启用 false:禁用。

        :return: The enable of this AddMetricNotifyRuleResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AddMetricNotifyRuleResponse.

        启禁用规则 true:启用 false:禁用。

        :param enable: The enable of this AddMetricNotifyRuleResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def notify_object(self):
        r"""Gets the notify_object of this AddMetricNotifyRuleResponse.

        通知对象;smn的主题urn。

        :return: The notify_object of this AddMetricNotifyRuleResponse.
        :rtype: str
        """
        return self._notify_object

    @notify_object.setter
    def notify_object(self, notify_object):
        r"""Sets the notify_object of this AddMetricNotifyRuleResponse.

        通知对象;smn的主题urn。

        :param notify_object: The notify_object of this AddMetricNotifyRuleResponse.
        :type notify_object: str
        """
        self._notify_object = notify_object

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
        if not isinstance(other, AddMetricNotifyRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
