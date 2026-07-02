# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[MetricsDimensionResp]',
        'metric_name': 'str',
        'namespace': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'unit': 'unit'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None, unit=None):
        r"""MetricInfoList

        The model defined in huaweicloud sdk

        :param dimensions: **参数解释** 指标维度 
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        :param metric_name: **参数解释** 指标名称 **取值范围** 不涉及 
        :type metric_name: str
        :param namespace: **参数解释** 服务命名空间 **取值范围** 不涉及 
        :type namespace: str
        :param unit: **参数解释** 指标单位 **取值范围** 不涉及 
        :type unit: str
        """
        
        

        self._dimensions = None
        self._metric_name = None
        self._namespace = None
        self._unit = None
        self.discriminator = None

        self.dimensions = dimensions
        self.metric_name = metric_name
        self.namespace = namespace
        self.unit = unit

    @property
    def dimensions(self):
        r"""Gets the dimensions of this MetricInfoList.

        **参数解释** 指标维度 

        :return: The dimensions of this MetricInfoList.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this MetricInfoList.

        **参数解释** 指标维度 

        :param dimensions: The dimensions of this MetricInfoList.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricInfoList.

        **参数解释** 指标名称 **取值范围** 不涉及 

        :return: The metric_name of this MetricInfoList.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricInfoList.

        **参数解释** 指标名称 **取值范围** 不涉及 

        :param metric_name: The metric_name of this MetricInfoList.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        r"""Gets the namespace of this MetricInfoList.

        **参数解释** 服务命名空间 **取值范围** 不涉及 

        :return: The namespace of this MetricInfoList.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this MetricInfoList.

        **参数解释** 服务命名空间 **取值范围** 不涉及 

        :param namespace: The namespace of this MetricInfoList.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def unit(self):
        r"""Gets the unit of this MetricInfoList.

        **参数解释** 指标单位 **取值范围** 不涉及 

        :return: The unit of this MetricInfoList.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricInfoList.

        **参数解释** 指标单位 **取值范围** 不涉及 

        :param unit: The unit of this MetricInfoList.
        :type unit: str
        """
        self._unit = unit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
