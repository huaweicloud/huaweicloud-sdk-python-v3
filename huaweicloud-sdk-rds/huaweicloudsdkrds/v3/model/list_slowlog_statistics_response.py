# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSlowlogStatisticsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'page_number': 'int',
        'page_record': 'int',
        'slow_log_list': 'list[SlowLog]',
        'total_record': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'page_record': 'pageRecord',
        'slow_log_list': 'slowLogList',
        'total_record': 'totalRecord',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, page_number=None, page_record=None, slow_log_list=None, total_record=None, start_time=None, end_time=None):
        """ListSlowlogStatisticsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._page_number = None
        self._page_record = None
        self._slow_log_list = None
        self._total_record = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_record is not None:
            self.page_record = page_record
        if slow_log_list is not None:
            self.slow_log_list = slow_log_list
        if total_record is not None:
            self.total_record = total_record
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def page_number(self):
        """Gets the page_number of this ListSlowlogStatisticsResponse.

        当前页码

        :return: The page_number of this ListSlowlogStatisticsResponse.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListSlowlogStatisticsResponse.

        当前页码

        :param page_number: The page_number of this ListSlowlogStatisticsResponse.
        :type: int
        """
        self._page_number = page_number

    @property
    def page_record(self):
        """Gets the page_record of this ListSlowlogStatisticsResponse.

        每页条数

        :return: The page_record of this ListSlowlogStatisticsResponse.
        :rtype: int
        """
        return self._page_record

    @page_record.setter
    def page_record(self, page_record):
        """Sets the page_record of this ListSlowlogStatisticsResponse.

        每页条数

        :param page_record: The page_record of this ListSlowlogStatisticsResponse.
        :type: int
        """
        self._page_record = page_record

    @property
    def slow_log_list(self):
        """Gets the slow_log_list of this ListSlowlogStatisticsResponse.

        慢日志列表

        :return: The slow_log_list of this ListSlowlogStatisticsResponse.
        :rtype: list[SlowLog]
        """
        return self._slow_log_list

    @slow_log_list.setter
    def slow_log_list(self, slow_log_list):
        """Sets the slow_log_list of this ListSlowlogStatisticsResponse.

        慢日志列表

        :param slow_log_list: The slow_log_list of this ListSlowlogStatisticsResponse.
        :type: list[SlowLog]
        """
        self._slow_log_list = slow_log_list

    @property
    def total_record(self):
        """Gets the total_record of this ListSlowlogStatisticsResponse.

        总条数

        :return: The total_record of this ListSlowlogStatisticsResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListSlowlogStatisticsResponse.

        总条数

        :param total_record: The total_record of this ListSlowlogStatisticsResponse.
        :type: int
        """
        self._total_record = total_record

    @property
    def start_time(self):
        """Gets the start_time of this ListSlowlogStatisticsResponse.

        开始时间

        :return: The start_time of this ListSlowlogStatisticsResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListSlowlogStatisticsResponse.

        开始时间

        :param start_time: The start_time of this ListSlowlogStatisticsResponse.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSlowlogStatisticsResponse.

        结束时间

        :return: The end_time of this ListSlowlogStatisticsResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSlowlogStatisticsResponse.

        结束时间

        :param end_time: The end_time of this ListSlowlogStatisticsResponse.
        :type: int
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
        if not isinstance(other, ListSlowlogStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
