# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryItemV2Metric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'metric_name': 'str',
        'dimensions': 'list[AlarmHistoryItemV2MetricDimensions]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None):
        r"""AlarmHistoryItemV2Metric

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 3 到 32 之间。 
        :type namespace: str
        :param metric_name: **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 1 到 64 之间。 
        :type metric_name: str
        :param dimensions: **参数解释**： 指标维度。 **取值范围**： 不涉及。 
        :type dimensions: list[:class:`huaweicloudsdkces.v2.AlarmHistoryItemV2MetricDimensions`]
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if metric_name is not None:
            self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def namespace(self):
        r"""Gets the namespace of this AlarmHistoryItemV2Metric.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 3 到 32 之间。 

        :return: The namespace of this AlarmHistoryItemV2Metric.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AlarmHistoryItemV2Metric.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 3 到 32 之间。 

        :param namespace: The namespace of this AlarmHistoryItemV2Metric.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AlarmHistoryItemV2Metric.

        **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 1 到 64 之间。 

        :return: The metric_name of this AlarmHistoryItemV2Metric.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AlarmHistoryItemV2Metric.

        **参数解释**： 资源的监控指标名称。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **取值范围**： 字符串长度在 1 到 64 之间。 

        :param metric_name: The metric_name of this AlarmHistoryItemV2Metric.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        r"""Gets the dimensions of this AlarmHistoryItemV2Metric.

        **参数解释**： 指标维度。 **取值范围**： 不涉及。 

        :return: The dimensions of this AlarmHistoryItemV2Metric.
        :rtype: list[:class:`huaweicloudsdkces.v2.AlarmHistoryItemV2MetricDimensions`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this AlarmHistoryItemV2Metric.

        **参数解释**： 指标维度。 **取值范围**： 不涉及。 

        :param dimensions: The dimensions of this AlarmHistoryItemV2Metric.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.AlarmHistoryItemV2MetricDimensions`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, AlarmHistoryItemV2Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
