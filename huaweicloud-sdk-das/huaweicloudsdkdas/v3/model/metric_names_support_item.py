# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricNamesSupportItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_types': 'list[str]',
        'metric_name': 'str',
        'unit': 'str',
        'metric_name_des': 'str'
    }

    attribute_map = {
        'engine_types': 'engine_types',
        'metric_name': 'metric_name',
        'unit': 'unit',
        'metric_name_des': 'metric_name_des'
    }

    def __init__(self, engine_types=None, metric_name=None, unit=None, metric_name_des=None):
        r"""MetricNamesSupportItem

        The model defined in huaweicloud sdk

        :param engine_types: 数据库类型
        :type engine_types: list[str]
        :param metric_name: 指标名称
        :type metric_name: str
        :param unit: 单位
        :type unit: str
        :param metric_name_des: 描述
        :type metric_name_des: str
        """
        
        

        self._engine_types = None
        self._metric_name = None
        self._unit = None
        self._metric_name_des = None
        self.discriminator = None

        if engine_types is not None:
            self.engine_types = engine_types
        if metric_name is not None:
            self.metric_name = metric_name
        if unit is not None:
            self.unit = unit
        if metric_name_des is not None:
            self.metric_name_des = metric_name_des

    @property
    def engine_types(self):
        r"""Gets the engine_types of this MetricNamesSupportItem.

        数据库类型

        :return: The engine_types of this MetricNamesSupportItem.
        :rtype: list[str]
        """
        return self._engine_types

    @engine_types.setter
    def engine_types(self, engine_types):
        r"""Sets the engine_types of this MetricNamesSupportItem.

        数据库类型

        :param engine_types: The engine_types of this MetricNamesSupportItem.
        :type engine_types: list[str]
        """
        self._engine_types = engine_types

    @property
    def metric_name(self):
        r"""Gets the metric_name of this MetricNamesSupportItem.

        指标名称

        :return: The metric_name of this MetricNamesSupportItem.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this MetricNamesSupportItem.

        指标名称

        :param metric_name: The metric_name of this MetricNamesSupportItem.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def unit(self):
        r"""Gets the unit of this MetricNamesSupportItem.

        单位

        :return: The unit of this MetricNamesSupportItem.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this MetricNamesSupportItem.

        单位

        :param unit: The unit of this MetricNamesSupportItem.
        :type unit: str
        """
        self._unit = unit

    @property
    def metric_name_des(self):
        r"""Gets the metric_name_des of this MetricNamesSupportItem.

        描述

        :return: The metric_name_des of this MetricNamesSupportItem.
        :rtype: str
        """
        return self._metric_name_des

    @metric_name_des.setter
    def metric_name_des(self, metric_name_des):
        r"""Sets the metric_name_des of this MetricNamesSupportItem.

        描述

        :param metric_name_des: The metric_name_des of this MetricNamesSupportItem.
        :type metric_name_des: str
        """
        self._metric_name_des = metric_name_des

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
        if not isinstance(other, MetricNamesSupportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
