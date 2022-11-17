# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCdnStatisticsResponse(SdkResponse):

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
        'interval': 'int',
        'values': 'list[int]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'interval': 'interval',
        'values': 'values'
    }

    def __init__(self, start_time=None, interval=None, values=None):
        """ShowCdnStatisticsResponse

        The model defined in huaweicloud sdk

        :param start_time: 统计起始时间。
        :type start_time: str
        :param interval: 统计间隔。
        :type interval: int
        :param values: 采样数据数组。  从start_time开始，每个间隔对应一个采样数据。
        :type values: list[int]
        """
        
        super(ShowCdnStatisticsResponse, self).__init__()

        self._start_time = None
        self._interval = None
        self._values = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if interval is not None:
            self.interval = interval
        if values is not None:
            self.values = values

    @property
    def start_time(self):
        """Gets the start_time of this ShowCdnStatisticsResponse.

        统计起始时间。

        :return: The start_time of this ShowCdnStatisticsResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowCdnStatisticsResponse.

        统计起始时间。

        :param start_time: The start_time of this ShowCdnStatisticsResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def interval(self):
        """Gets the interval of this ShowCdnStatisticsResponse.

        统计间隔。

        :return: The interval of this ShowCdnStatisticsResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowCdnStatisticsResponse.

        统计间隔。

        :param interval: The interval of this ShowCdnStatisticsResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def values(self):
        """Gets the values of this ShowCdnStatisticsResponse.

        采样数据数组。  从start_time开始，每个间隔对应一个采样数据。

        :return: The values of this ShowCdnStatisticsResponse.
        :rtype: list[int]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ShowCdnStatisticsResponse.

        采样数据数组。  从start_time开始，每个间隔对应一个采样数据。

        :param values: The values of this ShowCdnStatisticsResponse.
        :type values: list[int]
        """
        self._values = values

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
        if not isinstance(other, ShowCdnStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
