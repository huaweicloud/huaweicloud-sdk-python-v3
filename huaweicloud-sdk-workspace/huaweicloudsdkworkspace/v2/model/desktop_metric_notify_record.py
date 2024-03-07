# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopMetricNotifyRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_count': 'int',
        'metric_name': 'str',
        'threshold': 'int',
        'comparison_operator': 'str'
    }

    attribute_map = {
        'match_count': 'match_count',
        'metric_name': 'metric_name',
        'threshold': 'threshold',
        'comparison_operator': 'comparison_operator'
    }

    def __init__(self, match_count=None, metric_name=None, threshold=None, comparison_operator=None):
        """DesktopMetricNotifyRecord

        The model defined in huaweicloud sdk

        :param match_count: 满足通知规则阈值的桌面数
        :type match_count: int
        :param metric_name: 指标名称
        :type metric_name: str
        :param threshold: 统计持续周期(天)
        :type threshold: int
        :param comparison_operator: 统计指标对应的统计值和threshold进行比较的条件 * &#x60;&gt;&#x3D;&#x60; -  统计指标大于等于threshold时触发 * &#x60;&gt;&#x60; -   统计指标大于threshold时触发 * &#x60;&#x3D;&#x60; -  统计指标等于threshold时触发 * &#x60;&lt;&#x3D;&#x60; -  统计指标小于等于threshold时触发 * &#x60;&lt;&#x60; -  统计指标小于threshold时触发
        :type comparison_operator: str
        """
        
        

        self._match_count = None
        self._metric_name = None
        self._threshold = None
        self._comparison_operator = None
        self.discriminator = None

        if match_count is not None:
            self.match_count = match_count
        if metric_name is not None:
            self.metric_name = metric_name
        if threshold is not None:
            self.threshold = threshold
        if comparison_operator is not None:
            self.comparison_operator = comparison_operator

    @property
    def match_count(self):
        """Gets the match_count of this DesktopMetricNotifyRecord.

        满足通知规则阈值的桌面数

        :return: The match_count of this DesktopMetricNotifyRecord.
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this DesktopMetricNotifyRecord.

        满足通知规则阈值的桌面数

        :param match_count: The match_count of this DesktopMetricNotifyRecord.
        :type match_count: int
        """
        self._match_count = match_count

    @property
    def metric_name(self):
        """Gets the metric_name of this DesktopMetricNotifyRecord.

        指标名称

        :return: The metric_name of this DesktopMetricNotifyRecord.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this DesktopMetricNotifyRecord.

        指标名称

        :param metric_name: The metric_name of this DesktopMetricNotifyRecord.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def threshold(self):
        """Gets the threshold of this DesktopMetricNotifyRecord.

        统计持续周期(天)

        :return: The threshold of this DesktopMetricNotifyRecord.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this DesktopMetricNotifyRecord.

        统计持续周期(天)

        :param threshold: The threshold of this DesktopMetricNotifyRecord.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this DesktopMetricNotifyRecord.

        统计指标对应的统计值和threshold进行比较的条件 * `>=` -  统计指标大于等于threshold时触发 * `>` -   统计指标大于threshold时触发 * `=` -  统计指标等于threshold时触发 * `<=` -  统计指标小于等于threshold时触发 * `<` -  统计指标小于threshold时触发

        :return: The comparison_operator of this DesktopMetricNotifyRecord.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this DesktopMetricNotifyRecord.

        统计指标对应的统计值和threshold进行比较的条件 * `>=` -  统计指标大于等于threshold时触发 * `>` -   统计指标大于threshold时触发 * `=` -  统计指标等于threshold时触发 * `<=` -  统计指标小于等于threshold时触发 * `<` -  统计指标小于threshold时触发

        :param comparison_operator: The comparison_operator of this DesktopMetricNotifyRecord.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

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
        if not isinstance(other, DesktopMetricNotifyRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
