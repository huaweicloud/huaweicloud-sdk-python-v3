# coding: utf-8

import pprint
import re

import six





class ListFunctionStatisticsResponseBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'list[SlaReportsValue]',
        'duration': 'list[SlaReportsValue]',
        'fail_count': 'list[SlaReportsValue]',
        'max_duration': 'list[SlaReportsValue]',
        'min_duration': 'list[SlaReportsValue]',
        'reject_count': 'list[SlaReportsValue]'
    }

    attribute_map = {
        'count': 'count',
        'duration': 'duration',
        'fail_count': 'fail_count',
        'max_duration': 'max_duration',
        'min_duration': 'min_duration',
        'reject_count': 'reject_count'
    }

    def __init__(self, count=None, duration=None, fail_count=None, max_duration=None, min_duration=None, reject_count=None):
        """ListFunctionStatisticsResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._count = None
        self._duration = None
        self._fail_count = None
        self._max_duration = None
        self._min_duration = None
        self._reject_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration
        if fail_count is not None:
            self.fail_count = fail_count
        if max_duration is not None:
            self.max_duration = max_duration
        if min_duration is not None:
            self.min_duration = min_duration
        if reject_count is not None:
            self.reject_count = reject_count

    @property
    def count(self):
        """Gets the count of this ListFunctionStatisticsResponseBody.

        调用次数

        :return: The count of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFunctionStatisticsResponseBody.

        调用次数

        :param count: The count of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._count = count

    @property
    def duration(self):
        """Gets the duration of this ListFunctionStatisticsResponseBody.

        平均时延，单位毫秒

        :return: The duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListFunctionStatisticsResponseBody.

        平均时延，单位毫秒

        :param duration: The duration of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._duration = duration

    @property
    def fail_count(self):
        """Gets the fail_count of this ListFunctionStatisticsResponseBody.

        错误次数

        :return: The fail_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        """Sets the fail_count of this ListFunctionStatisticsResponseBody.

        错误次数

        :param fail_count: The fail_count of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._fail_count = fail_count

    @property
    def max_duration(self):
        """Gets the max_duration of this ListFunctionStatisticsResponseBody.

        最大时延，单位毫秒

        :return: The max_duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this ListFunctionStatisticsResponseBody.

        最大时延，单位毫秒

        :param max_duration: The max_duration of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._max_duration = max_duration

    @property
    def min_duration(self):
        """Gets the min_duration of this ListFunctionStatisticsResponseBody.

        最小时延，单位毫秒

        :return: The min_duration of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._min_duration

    @min_duration.setter
    def min_duration(self, min_duration):
        """Sets the min_duration of this ListFunctionStatisticsResponseBody.

        最小时延，单位毫秒

        :param min_duration: The min_duration of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._min_duration = min_duration

    @property
    def reject_count(self):
        """Gets the reject_count of this ListFunctionStatisticsResponseBody.

        被拒绝次数

        :return: The reject_count of this ListFunctionStatisticsResponseBody.
        :rtype: list[SlaReportsValue]
        """
        return self._reject_count

    @reject_count.setter
    def reject_count(self, reject_count):
        """Sets the reject_count of this ListFunctionStatisticsResponseBody.

        被拒绝次数

        :param reject_count: The reject_count of this ListFunctionStatisticsResponseBody.
        :type: list[SlaReportsValue]
        """
        self._reject_count = reject_count

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
        if not isinstance(other, ListFunctionStatisticsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
