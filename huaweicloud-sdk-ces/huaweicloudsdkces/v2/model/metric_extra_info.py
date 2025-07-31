# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_metric_name': 'str',
        'metric_prefix': 'str',
        'custom_proc_name': 'str',
        'metric_type': 'str'
    }

    attribute_map = {
        'origin_metric_name': 'origin_metric_name',
        'metric_prefix': 'metric_prefix',
        'custom_proc_name': 'custom_proc_name',
        'metric_type': 'metric_type'
    }

    def __init__(self, origin_metric_name=None, metric_prefix=None, custom_proc_name=None, metric_type=None):
        r"""MetricExtraInfo

        The model defined in huaweicloud sdk

        :param origin_metric_name: 原始指标名称
        :type origin_metric_name: str
        :param metric_prefix: 指标名称前缀
        :type metric_prefix: str
        :param custom_proc_name: 用户进程名称
        :type custom_proc_name: str
        :param metric_type: 指标类型
        :type metric_type: str
        """
        
        

        self._origin_metric_name = None
        self._metric_prefix = None
        self._custom_proc_name = None
        self._metric_type = None
        self.discriminator = None

        self.origin_metric_name = origin_metric_name
        if metric_prefix is not None:
            self.metric_prefix = metric_prefix
        if custom_proc_name is not None:
            self.custom_proc_name = custom_proc_name
        if metric_type is not None:
            self.metric_type = metric_type

    @property
    def origin_metric_name(self):
        r"""Gets the origin_metric_name of this MetricExtraInfo.

        原始指标名称

        :return: The origin_metric_name of this MetricExtraInfo.
        :rtype: str
        """
        return self._origin_metric_name

    @origin_metric_name.setter
    def origin_metric_name(self, origin_metric_name):
        r"""Sets the origin_metric_name of this MetricExtraInfo.

        原始指标名称

        :param origin_metric_name: The origin_metric_name of this MetricExtraInfo.
        :type origin_metric_name: str
        """
        self._origin_metric_name = origin_metric_name

    @property
    def metric_prefix(self):
        r"""Gets the metric_prefix of this MetricExtraInfo.

        指标名称前缀

        :return: The metric_prefix of this MetricExtraInfo.
        :rtype: str
        """
        return self._metric_prefix

    @metric_prefix.setter
    def metric_prefix(self, metric_prefix):
        r"""Sets the metric_prefix of this MetricExtraInfo.

        指标名称前缀

        :param metric_prefix: The metric_prefix of this MetricExtraInfo.
        :type metric_prefix: str
        """
        self._metric_prefix = metric_prefix

    @property
    def custom_proc_name(self):
        r"""Gets the custom_proc_name of this MetricExtraInfo.

        用户进程名称

        :return: The custom_proc_name of this MetricExtraInfo.
        :rtype: str
        """
        return self._custom_proc_name

    @custom_proc_name.setter
    def custom_proc_name(self, custom_proc_name):
        r"""Sets the custom_proc_name of this MetricExtraInfo.

        用户进程名称

        :param custom_proc_name: The custom_proc_name of this MetricExtraInfo.
        :type custom_proc_name: str
        """
        self._custom_proc_name = custom_proc_name

    @property
    def metric_type(self):
        r"""Gets the metric_type of this MetricExtraInfo.

        指标类型

        :return: The metric_type of this MetricExtraInfo.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        r"""Sets the metric_type of this MetricExtraInfo.

        指标类型

        :param metric_type: The metric_type of this MetricExtraInfo.
        :type metric_type: str
        """
        self._metric_type = metric_type

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
        if not isinstance(other, MetricExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
