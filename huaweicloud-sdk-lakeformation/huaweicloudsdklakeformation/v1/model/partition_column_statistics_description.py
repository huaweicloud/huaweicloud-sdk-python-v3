# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionColumnStatisticsDescription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_values': 'list[str]',
        'last_analyzed_time': 'datetime'
    }

    attribute_map = {
        'partition_values': 'partition_values',
        'last_analyzed_time': 'last_analyzed_time'
    }

    def __init__(self, partition_values=None, last_analyzed_time=None):
        """PartitionColumnStatisticsDescription

        The model defined in huaweicloud sdk

        :param partition_values: 分区值的列表
        :type partition_values: list[str]
        :param last_analyzed_time: 最后统计时间
        :type last_analyzed_time: datetime
        """
        
        

        self._partition_values = None
        self._last_analyzed_time = None
        self.discriminator = None

        if partition_values is not None:
            self.partition_values = partition_values
        self.last_analyzed_time = last_analyzed_time

    @property
    def partition_values(self):
        """Gets the partition_values of this PartitionColumnStatisticsDescription.

        分区值的列表

        :return: The partition_values of this PartitionColumnStatisticsDescription.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        """Sets the partition_values of this PartitionColumnStatisticsDescription.

        分区值的列表

        :param partition_values: The partition_values of this PartitionColumnStatisticsDescription.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

    @property
    def last_analyzed_time(self):
        """Gets the last_analyzed_time of this PartitionColumnStatisticsDescription.

        最后统计时间

        :return: The last_analyzed_time of this PartitionColumnStatisticsDescription.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        """Sets the last_analyzed_time of this PartitionColumnStatisticsDescription.

        最后统计时间

        :param last_analyzed_time: The last_analyzed_time of this PartitionColumnStatisticsDescription.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

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
        if not isinstance(other, PartitionColumnStatisticsDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
