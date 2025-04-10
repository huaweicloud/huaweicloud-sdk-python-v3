# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerMetricData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'datapoints': 'list[ServerDataPoints]',
        'dimension_value': 'str'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'datapoints': 'datapoints',
        'dimension_value': 'dimension_value'
    }

    def __init__(self, metric_name=None, datapoints=None, dimension_value=None):
        r"""ServerMetricData

        The model defined in huaweicloud sdk

        :param metric_name: 监控指标名称。
        :type metric_name: str
        :param datapoints: 指标数据列表。
        :type datapoints: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerDataPoints`]
        :param dimension_value: 维度值，仅查询GPU监控信息时有值。
        :type dimension_value: str
        """
        
        

        self._metric_name = None
        self._datapoints = None
        self._dimension_value = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if datapoints is not None:
            self.datapoints = datapoints
        if dimension_value is not None:
            self.dimension_value = dimension_value

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ServerMetricData.

        监控指标名称。

        :return: The metric_name of this ServerMetricData.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ServerMetricData.

        监控指标名称。

        :param metric_name: The metric_name of this ServerMetricData.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def datapoints(self):
        r"""Gets the datapoints of this ServerMetricData.

        指标数据列表。

        :return: The datapoints of this ServerMetricData.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerDataPoints`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this ServerMetricData.

        指标数据列表。

        :param datapoints: The datapoints of this ServerMetricData.
        :type datapoints: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerDataPoints`]
        """
        self._datapoints = datapoints

    @property
    def dimension_value(self):
        r"""Gets the dimension_value of this ServerMetricData.

        维度值，仅查询GPU监控信息时有值。

        :return: The dimension_value of this ServerMetricData.
        :rtype: str
        """
        return self._dimension_value

    @dimension_value.setter
    def dimension_value(self, dimension_value):
        r"""Sets the dimension_value of this ServerMetricData.

        维度值，仅查询GPU监控信息时有值。

        :param dimension_value: The dimension_value of this ServerMetricData.
        :type dimension_value: str
        """
        self._dimension_value = dimension_value

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
        if not isinstance(other, ServerMetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
