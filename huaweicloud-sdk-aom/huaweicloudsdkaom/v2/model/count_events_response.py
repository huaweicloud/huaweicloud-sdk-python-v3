# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step': 'int',
        'timestamps': 'list[int]',
        'series': 'list[EventSeries]'
    }

    attribute_map = {
        'step': 'step',
        'timestamps': 'timestamps',
        'series': 'series'
    }

    def __init__(self, step=None, timestamps=None, series=None):
        """CountEventsResponse

        The model defined in huaweicloud sdk

        :param step: 统计步长。毫秒数，例如一分钟则填写为60000。
        :type step: int
        :param timestamps: 统计结果对应的时间序列。
        :type timestamps: list[int]
        :param series: 事件或者告警不同级别相同时间序列对应的统计结果。
        :type series: list[:class:`huaweicloudsdkaom.v2.EventSeries`]
        """
        
        super(CountEventsResponse, self).__init__()

        self._step = None
        self._timestamps = None
        self._series = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if timestamps is not None:
            self.timestamps = timestamps
        if series is not None:
            self.series = series

    @property
    def step(self):
        """Gets the step of this CountEventsResponse.

        统计步长。毫秒数，例如一分钟则填写为60000。

        :return: The step of this CountEventsResponse.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this CountEventsResponse.

        统计步长。毫秒数，例如一分钟则填写为60000。

        :param step: The step of this CountEventsResponse.
        :type step: int
        """
        self._step = step

    @property
    def timestamps(self):
        """Gets the timestamps of this CountEventsResponse.

        统计结果对应的时间序列。

        :return: The timestamps of this CountEventsResponse.
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this CountEventsResponse.

        统计结果对应的时间序列。

        :param timestamps: The timestamps of this CountEventsResponse.
        :type timestamps: list[int]
        """
        self._timestamps = timestamps

    @property
    def series(self):
        """Gets the series of this CountEventsResponse.

        事件或者告警不同级别相同时间序列对应的统计结果。

        :return: The series of this CountEventsResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.EventSeries`]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this CountEventsResponse.

        事件或者告警不同级别相同时间序列对应的统计结果。

        :param series: The series of this CountEventsResponse.
        :type series: list[:class:`huaweicloudsdkaom.v2.EventSeries`]
        """
        self._series = series

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
        if not isinstance(other, CountEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
