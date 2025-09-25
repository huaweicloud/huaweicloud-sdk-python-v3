# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'str',
        'type': 'str',
        'unit': 'str',
        'datapoints': 'list[DatapointResult]',
        'timestamps': 'list[str]'
    }

    attribute_map = {
        'metric': 'metric',
        'type': 'type',
        'unit': 'unit',
        'datapoints': 'datapoints',
        'timestamps': 'timestamps'
    }

    def __init__(self, metric=None, type=None, unit=None, datapoints=None, timestamps=None):
        r"""MetricDataResult

        The model defined in huaweicloud sdk

        :param metric: **参数解释**: 指标ID。 **取值范围**: 不涉及。
        :type metric: str
        :param type: **参数解释** 指标类型 **取值范围** - INSTANCE：实例类型。 - NODE：节点类型。 - COMPONENT：组件类型。 
        :type type: str
        :param unit: **参数解释**: 指标单位。 **取值范围**: 不涉及。
        :type unit: str
        :param datapoints: **参数解释**: 指标维度及指标值。
        :type datapoints: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatapointResult`]
        :param timestamps: **参数解释**: 时间戳，例如1699495140000。
        :type timestamps: list[str]
        """
        
        

        self._metric = None
        self._type = None
        self._unit = None
        self._datapoints = None
        self._timestamps = None
        self.discriminator = None

        self.metric = metric
        self.type = type
        self.unit = unit
        self.datapoints = datapoints
        self.timestamps = timestamps

    @property
    def metric(self):
        r"""Gets the metric of this MetricDataResult.

        **参数解释**: 指标ID。 **取值范围**: 不涉及。

        :return: The metric of this MetricDataResult.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this MetricDataResult.

        **参数解释**: 指标ID。 **取值范围**: 不涉及。

        :param metric: The metric of this MetricDataResult.
        :type metric: str
        """
        self._metric = metric

    @property
    def type(self):
        r"""Gets the type of this MetricDataResult.

        **参数解释** 指标类型 **取值范围** - INSTANCE：实例类型。 - NODE：节点类型。 - COMPONENT：组件类型。 

        :return: The type of this MetricDataResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MetricDataResult.

        **参数解释** 指标类型 **取值范围** - INSTANCE：实例类型。 - NODE：节点类型。 - COMPONENT：组件类型。 

        :param type: The type of this MetricDataResult.
        :type type: str
        """
        self._type = type

    @property
    def unit(self):
        r"""Gets the unit of this MetricDataResult.

        **参数解释**: 指标单位。 **取值范围**: 不涉及。

        :return: The unit of this MetricDataResult.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricDataResult.

        **参数解释**: 指标单位。 **取值范围**: 不涉及。

        :param unit: The unit of this MetricDataResult.
        :type unit: str
        """
        self._unit = unit

    @property
    def datapoints(self):
        r"""Gets the datapoints of this MetricDataResult.

        **参数解释**: 指标维度及指标值。

        :return: The datapoints of this MetricDataResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatapointResult`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this MetricDataResult.

        **参数解释**: 指标维度及指标值。

        :param datapoints: The datapoints of this MetricDataResult.
        :type datapoints: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DatapointResult`]
        """
        self._datapoints = datapoints

    @property
    def timestamps(self):
        r"""Gets the timestamps of this MetricDataResult.

        **参数解释**: 时间戳，例如1699495140000。

        :return: The timestamps of this MetricDataResult.
        :rtype: list[str]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        r"""Sets the timestamps of this MetricDataResult.

        **参数解释**: 时间戳，例如1699495140000。

        :param timestamps: The timestamps of this MetricDataResult.
        :type timestamps: list[str]
        """
        self._timestamps = timestamps

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
        if not isinstance(other, MetricDataResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
