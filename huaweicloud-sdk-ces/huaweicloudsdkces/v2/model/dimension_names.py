# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionNames:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'list[str]',
        'event': 'list[str]'
    }

    attribute_map = {
        'metric': 'metric',
        'event': 'event'
    }

    def __init__(self, metric=None, event=None):
        r"""DimensionNames

        The model defined in huaweicloud sdk

        :param metric: 启用一键告警关联指标告警规则的维度列表，未指定的维度默认不开启
        :type metric: list[str]
        :param event: 启用一键告警关联事件告警规则的维度列表，未指定的维度默认不开启，其中\&quot;\&quot;代表全部资源
        :type event: list[str]
        """
        
        

        self._metric = None
        self._event = None
        self.discriminator = None

        self.metric = metric
        self.event = event

    @property
    def metric(self):
        r"""Gets the metric of this DimensionNames.

        启用一键告警关联指标告警规则的维度列表，未指定的维度默认不开启

        :return: The metric of this DimensionNames.
        :rtype: list[str]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this DimensionNames.

        启用一键告警关联指标告警规则的维度列表，未指定的维度默认不开启

        :param metric: The metric of this DimensionNames.
        :type metric: list[str]
        """
        self._metric = metric

    @property
    def event(self):
        r"""Gets the event of this DimensionNames.

        启用一键告警关联事件告警规则的维度列表，未指定的维度默认不开启，其中\"\"代表全部资源

        :return: The event of this DimensionNames.
        :rtype: list[str]
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this DimensionNames.

        启用一键告警关联事件告警规则的维度列表，未指定的维度默认不开启，其中\"\"代表全部资源

        :param event: The event of this DimensionNames.
        :type event: list[str]
        """
        self._event = event

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
        if not isinstance(other, DimensionNames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
