# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiNodesSingleMetricMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'series': 'list[float]',
        'timestamps': 'list[int]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'series': 'series',
        'timestamps': 'timestamps'
    }

    def __init__(self, instance_id=None, node_id=None, series=None, timestamps=None):
        r"""MultiNodesSingleMetricMetrics

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param series: 指标
        :type series: list[float]
        :param timestamps: 时间戳
        :type timestamps: list[int]
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._series = None
        self._timestamps = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if series is not None:
            self.series = series
        if timestamps is not None:
            self.timestamps = timestamps

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MultiNodesSingleMetricMetrics.

        实例ID

        :return: The instance_id of this MultiNodesSingleMetricMetrics.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MultiNodesSingleMetricMetrics.

        实例ID

        :param instance_id: The instance_id of this MultiNodesSingleMetricMetrics.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this MultiNodesSingleMetricMetrics.

        节点ID

        :return: The node_id of this MultiNodesSingleMetricMetrics.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this MultiNodesSingleMetricMetrics.

        节点ID

        :param node_id: The node_id of this MultiNodesSingleMetricMetrics.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def series(self):
        r"""Gets the series of this MultiNodesSingleMetricMetrics.

        指标

        :return: The series of this MultiNodesSingleMetricMetrics.
        :rtype: list[float]
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this MultiNodesSingleMetricMetrics.

        指标

        :param series: The series of this MultiNodesSingleMetricMetrics.
        :type series: list[float]
        """
        self._series = series

    @property
    def timestamps(self):
        r"""Gets the timestamps of this MultiNodesSingleMetricMetrics.

        时间戳

        :return: The timestamps of this MultiNodesSingleMetricMetrics.
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        r"""Sets the timestamps of this MultiNodesSingleMetricMetrics.

        时间戳

        :param timestamps: The timestamps of this MultiNodesSingleMetricMetrics.
        :type timestamps: list[int]
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
        if not isinstance(other, MultiNodesSingleMetricMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
