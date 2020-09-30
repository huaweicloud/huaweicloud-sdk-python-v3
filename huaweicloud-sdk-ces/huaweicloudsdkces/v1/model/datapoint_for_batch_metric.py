# coding: utf-8

import pprint
import re

import six





class DatapointForBatchMetric:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'average': 'float',
        'timestamp': 'int'
    }

    attribute_map = {
        'average': 'average',
        'timestamp': 'timestamp'
    }

    def __init__(self, average=None, timestamp=None):
        """DatapointForBatchMetric - a model defined in huaweicloud sdk"""
        
        

        self._average = None
        self._timestamp = None
        self.discriminator = None

        self.average = average
        self.timestamp = timestamp

    @property
    def average(self):
        """Gets the average of this DatapointForBatchMetric.

        指标值，该字段名称与请求参数中filter使用的查询值相同；字段名称可为：max/min/average/sum/variance。

        :return: The average of this DatapointForBatchMetric.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this DatapointForBatchMetric.

        指标值，该字段名称与请求参数中filter使用的查询值相同；字段名称可为：max/min/average/sum/variance。

        :param average: The average of this DatapointForBatchMetric.
        :type: float
        """
        self._average = average

    @property
    def timestamp(self):
        """Gets the timestamp of this DatapointForBatchMetric.

        指标采集时间，UNIX时间戳，单位毫秒。

        :return: The timestamp of this DatapointForBatchMetric.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DatapointForBatchMetric.

        指标采集时间，UNIX时间戳，单位毫秒。

        :param timestamp: The timestamp of this DatapointForBatchMetric.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, DatapointForBatchMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
