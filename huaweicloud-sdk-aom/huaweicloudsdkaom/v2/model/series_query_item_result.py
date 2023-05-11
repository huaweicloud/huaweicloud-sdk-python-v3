# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SeriesQueryItemResult:

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
        'dimensions': 'list[DimensionSeries]',
        'metric_name': 'str',
        'unit': 'str',
        'dimension_value_hash': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'unit': 'unit',
        'dimension_value_hash': 'dimension_value_hash'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None, unit=None, dimension_value_hash=None):
        """SeriesQueryItemResult

        The model defined in huaweicloud sdk

        :param namespace: 命名空间。
        :type namespace: str
        :param dimensions: 维度列表。
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        :param metric_name: 时间序列名称。
        :type metric_name: str
        :param unit: 时间序列单位。
        :type unit: str
        :param dimension_value_hash: 时间序列哈希值。
        :type dimension_value_hash: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self._unit = None
        self._dimension_value_hash = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if metric_name is not None:
            self.metric_name = metric_name
        if unit is not None:
            self.unit = unit
        if dimension_value_hash is not None:
            self.dimension_value_hash = dimension_value_hash

    @property
    def namespace(self):
        """Gets the namespace of this SeriesQueryItemResult.

        命名空间。

        :return: The namespace of this SeriesQueryItemResult.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SeriesQueryItemResult.

        命名空间。

        :param namespace: The namespace of this SeriesQueryItemResult.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this SeriesQueryItemResult.

        维度列表。

        :return: The dimensions of this SeriesQueryItemResult.
        :rtype: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this SeriesQueryItemResult.

        维度列表。

        :param dimensions: The dimensions of this SeriesQueryItemResult.
        :type dimensions: list[:class:`huaweicloudsdkaom.v2.DimensionSeries`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this SeriesQueryItemResult.

        时间序列名称。

        :return: The metric_name of this SeriesQueryItemResult.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this SeriesQueryItemResult.

        时间序列名称。

        :param metric_name: The metric_name of this SeriesQueryItemResult.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def unit(self):
        """Gets the unit of this SeriesQueryItemResult.

        时间序列单位。

        :return: The unit of this SeriesQueryItemResult.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this SeriesQueryItemResult.

        时间序列单位。

        :param unit: The unit of this SeriesQueryItemResult.
        :type unit: str
        """
        self._unit = unit

    @property
    def dimension_value_hash(self):
        """Gets the dimension_value_hash of this SeriesQueryItemResult.

        时间序列哈希值。

        :return: The dimension_value_hash of this SeriesQueryItemResult.
        :rtype: str
        """
        return self._dimension_value_hash

    @dimension_value_hash.setter
    def dimension_value_hash(self, dimension_value_hash):
        """Sets the dimension_value_hash of this SeriesQueryItemResult.

        时间序列哈希值。

        :param dimension_value_hash: The dimension_value_hash of this SeriesQueryItemResult.
        :type dimension_value_hash: str
        """
        self._dimension_value_hash = dimension_value_hash

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
        if not isinstance(other, SeriesQueryItemResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
