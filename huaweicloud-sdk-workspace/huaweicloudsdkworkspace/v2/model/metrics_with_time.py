# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricsWithTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'metrics': 'list[Metric]'
    }

    attribute_map = {
        'time': 'time',
        'metrics': 'metrics'
    }

    def __init__(self, time=None, metrics=None):
        """MetricsWithTime

        The model defined in huaweicloud sdk

        :param time: 时间
        :type time: str
        :param metrics: 指标值
        :type metrics: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        
        

        self._time = None
        self._metrics = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if metrics is not None:
            self.metrics = metrics

    @property
    def time(self):
        """Gets the time of this MetricsWithTime.

        时间

        :return: The time of this MetricsWithTime.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MetricsWithTime.

        时间

        :param time: The time of this MetricsWithTime.
        :type time: str
        """
        self._time = time

    @property
    def metrics(self):
        """Gets the metrics of this MetricsWithTime.

        指标值

        :return: The metrics of this MetricsWithTime.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this MetricsWithTime.

        指标值

        :param metrics: The metrics of this MetricsWithTime.
        :type metrics: list[:class:`huaweicloudsdkworkspace.v2.Metric`]
        """
        self._metrics = metrics

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
        if not isinstance(other, MetricsWithTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
