# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransformMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_span': 'TimeSpan',
        'tags': 'dict(str, str)',
        'metrics': 'list[TransformMetric]',
        'limit': 'int'
    }

    attribute_map = {
        'time_span': 'time_span',
        'tags': 'tags',
        'metrics': 'metrics',
        'limit': 'limit'
    }

    def __init__(self, time_span=None, tags=None, metrics=None, limit=None):
        r"""TransformMetrics

        The model defined in huaweicloud sdk

        :param time_span: 
        :type time_span: :class:`huaweicloudsdkiotanalytics.v1.TimeSpan`
        :param tags: 对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\&quot;deviceId\&quot;: \&quot;id0001\&quot;}
        :type tags: dict(str, str)
        :param metrics: 查询的测量指标列表
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.TransformMetric`]
        :param limit: 返回值个数限制
        :type limit: int
        """
        
        

        self._time_span = None
        self._tags = None
        self._metrics = None
        self._limit = None
        self.discriminator = None

        self.time_span = time_span
        self.tags = tags
        self.metrics = metrics
        if limit is not None:
            self.limit = limit

    @property
    def time_span(self):
        r"""Gets the time_span of this TransformMetrics.

        :return: The time_span of this TransformMetrics.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.TimeSpan`
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        r"""Sets the time_span of this TransformMetrics.

        :param time_span: The time_span of this TransformMetrics.
        :type time_span: :class:`huaweicloudsdkiotanalytics.v1.TimeSpan`
        """
        self._time_span = time_span

    @property
    def tags(self):
        r"""Gets the tags of this TransformMetrics.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :return: The tags of this TransformMetrics.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TransformMetrics.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :param tags: The tags of this TransformMetrics.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def metrics(self):
        r"""Gets the metrics of this TransformMetrics.

        查询的测量指标列表

        :return: The metrics of this TransformMetrics.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.TransformMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this TransformMetrics.

        查询的测量指标列表

        :param metrics: The metrics of this TransformMetrics.
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.TransformMetric`]
        """
        self._metrics = metrics

    @property
    def limit(self):
        r"""Gets the limit of this TransformMetrics.

        返回值个数限制

        :return: The limit of this TransformMetrics.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this TransformMetrics.

        返回值个数限制

        :param limit: The limit of this TransformMetrics.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, TransformMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
