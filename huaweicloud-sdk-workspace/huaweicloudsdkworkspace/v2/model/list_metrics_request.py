# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'dim': 'str',
        'metric_names': 'list[str]',
        'period': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'dim': 'dim',
        'metric_names': 'metric_names',
        'period': 'period'
    }

    def __init__(self, start_time=None, end_time=None, dim=None, metric_names=None, period=None):
        r"""ListMetricsRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间, UTC时间。
        :type start_time: str
        :param end_time: 结束时间,UTC时间。
        :type end_time: str
        :param dim: 指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}&#x3D;key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0&#x3D;instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0&#x3D;key,value&amp;dim.1&#x3D;key,value。
        :type dim: str
        :param metric_names: 指标名称列表。
        :type metric_names: list[str]
        :param period: 数据周期 | DAY - 天级数据 HOUR - 小时级数据。
        :type period: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._dim = None
        self._metric_names = None
        self._period = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if dim is not None:
            self.dim = dim
        self.metric_names = metric_names
        if period is not None:
            self.period = period

    @property
    def start_time(self):
        r"""Gets the start_time of this ListMetricsRequest.

        开始时间, UTC时间。

        :return: The start_time of this ListMetricsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListMetricsRequest.

        开始时间, UTC时间。

        :param start_time: The start_time of this ListMetricsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListMetricsRequest.

        结束时间,UTC时间。

        :return: The end_time of this ListMetricsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListMetricsRequest.

        结束时间,UTC时间。

        :param end_time: The end_time of this ListMetricsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def dim(self):
        r"""Gets the dim of this ListMetricsRequest.

        指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}=key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0=key,value&dim.1=key,value。

        :return: The dim of this ListMetricsRequest.
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        r"""Sets the dim of this ListMetricsRequest.

        指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}=key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0=key,value&dim.1=key,value。

        :param dim: The dim of this ListMetricsRequest.
        :type dim: str
        """
        self._dim = dim

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ListMetricsRequest.

        指标名称列表。

        :return: The metric_names of this ListMetricsRequest.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ListMetricsRequest.

        指标名称列表。

        :param metric_names: The metric_names of this ListMetricsRequest.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def period(self):
        r"""Gets the period of this ListMetricsRequest.

        数据周期 | DAY - 天级数据 HOUR - 小时级数据。

        :return: The period of this ListMetricsRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ListMetricsRequest.

        数据周期 | DAY - 天级数据 HOUR - 小时级数据。

        :param period: The period of this ListMetricsRequest.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, ListMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
