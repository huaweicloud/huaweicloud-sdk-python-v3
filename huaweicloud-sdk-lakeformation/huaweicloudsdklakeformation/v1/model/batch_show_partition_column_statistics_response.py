# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowPartitionColumnStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'found_partition_number': 'int',
        'column_statistics': 'dict(str, list[ColumnStatisticsObj])'
    }

    attribute_map = {
        'found_partition_number': 'found_partition_number',
        'column_statistics': 'column_statistics'
    }

    def __init__(self, found_partition_number=None, column_statistics=None):
        """BatchShowPartitionColumnStatisticsResponse

        The model defined in huaweicloud sdk

        :param found_partition_number: 分区统计信息的数量
        :type found_partition_number: int
        :param column_statistics: 分区统计信息的列表
        :type column_statistics: dict(str, list[ColumnStatisticsObj])
        """
        
        super(BatchShowPartitionColumnStatisticsResponse, self).__init__()

        self._found_partition_number = None
        self._column_statistics = None
        self.discriminator = None

        if found_partition_number is not None:
            self.found_partition_number = found_partition_number
        if column_statistics is not None:
            self.column_statistics = column_statistics

    @property
    def found_partition_number(self):
        """Gets the found_partition_number of this BatchShowPartitionColumnStatisticsResponse.

        分区统计信息的数量

        :return: The found_partition_number of this BatchShowPartitionColumnStatisticsResponse.
        :rtype: int
        """
        return self._found_partition_number

    @found_partition_number.setter
    def found_partition_number(self, found_partition_number):
        """Sets the found_partition_number of this BatchShowPartitionColumnStatisticsResponse.

        分区统计信息的数量

        :param found_partition_number: The found_partition_number of this BatchShowPartitionColumnStatisticsResponse.
        :type found_partition_number: int
        """
        self._found_partition_number = found_partition_number

    @property
    def column_statistics(self):
        """Gets the column_statistics of this BatchShowPartitionColumnStatisticsResponse.

        分区统计信息的列表

        :return: The column_statistics of this BatchShowPartitionColumnStatisticsResponse.
        :rtype: dict(str, list[ColumnStatisticsObj])
        """
        return self._column_statistics

    @column_statistics.setter
    def column_statistics(self, column_statistics):
        """Sets the column_statistics of this BatchShowPartitionColumnStatisticsResponse.

        分区统计信息的列表

        :param column_statistics: The column_statistics of this BatchShowPartitionColumnStatisticsResponse.
        :type column_statistics: dict(str, list[ColumnStatisticsObj])
        """
        self._column_statistics = column_statistics

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
        if not isinstance(other, BatchShowPartitionColumnStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
