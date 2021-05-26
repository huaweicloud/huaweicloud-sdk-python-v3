# coding: utf-8

import pprint
import re

import six





class ListLiveSampleLogsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domain=None, start_time=None, end_time=None):
        """ListLiveSampleLogsRequest - a model defined in huaweicloud sdk"""
        
        

        self._play_domain = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domain = play_domain
        self.start_time = start_time
        self.end_time = end_time

    @property
    def play_domain(self):
        """Gets the play_domain of this ListLiveSampleLogsRequest.

        播放域名。

        :return: The play_domain of this ListLiveSampleLogsRequest.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        """Sets the play_domain of this ListLiveSampleLogsRequest.

        播放域名。

        :param play_domain: The play_domain of this ListLiveSampleLogsRequest.
        :type: str
        """
        self._play_domain = play_domain

    @property
    def start_time(self):
        """Gets the start_time of this ListLiveSampleLogsRequest.

        查询开始时间，UTC时间：YYYY-MM-DDTHH:mm:ssZ，如北京时间2020年3月4日16点00分00秒可表示为2020-03-04T08:00:00Z。仅支持查询最近3个月内的数据。

        :return: The start_time of this ListLiveSampleLogsRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListLiveSampleLogsRequest.

        查询开始时间，UTC时间：YYYY-MM-DDTHH:mm:ssZ，如北京时间2020年3月4日16点00分00秒可表示为2020-03-04T08:00:00Z。仅支持查询最近3个月内的数据。

        :param start_time: The start_time of this ListLiveSampleLogsRequest.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListLiveSampleLogsRequest.

        查询结束时间，UTC时间：YYYY-MM-DDTHH:mm:ssZ，如北京时间2020年3月4日16点00分00秒可表示为2020-03-04T08:00:00Z。查询时间跨度不能大于7天。

        :return: The end_time of this ListLiveSampleLogsRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListLiveSampleLogsRequest.

        查询结束时间，UTC时间：YYYY-MM-DDTHH:mm:ssZ，如北京时间2020年3月4日16点00分00秒可表示为2020-03-04T08:00:00Z。查询时间跨度不能大于7天。

        :param end_time: The end_time of this ListLiveSampleLogsRequest.
        :type: datetime
        """
        self._end_time = end_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListLiveSampleLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
