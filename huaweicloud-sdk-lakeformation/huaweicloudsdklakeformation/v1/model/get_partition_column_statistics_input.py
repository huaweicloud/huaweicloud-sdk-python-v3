# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetPartitionColumnStatisticsInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregate_statics': 'bool',
        'column_names': 'list[str]',
        'partition_values_list': 'list[list[str]]'
    }

    attribute_map = {
        'aggregate_statics': 'aggregate_statics',
        'column_names': 'column_names',
        'partition_values_list': 'partition_values_list'
    }

    def __init__(self, aggregate_statics=None, column_names=None, partition_values_list=None):
        """GetPartitionColumnStatisticsInput

        The model defined in huaweicloud sdk

        :param aggregate_statics: 是否聚合返回统计信息
        :type aggregate_statics: bool
        :param column_names: 统计信息的列名
        :type column_names: list[str]
        :param partition_values_list: 需要统计的分区值列表
        :type partition_values_list: list[list[str]]
        """
        
        

        self._aggregate_statics = None
        self._column_names = None
        self._partition_values_list = None
        self.discriminator = None

        self.aggregate_statics = aggregate_statics
        self.column_names = column_names
        self.partition_values_list = partition_values_list

    @property
    def aggregate_statics(self):
        """Gets the aggregate_statics of this GetPartitionColumnStatisticsInput.

        是否聚合返回统计信息

        :return: The aggregate_statics of this GetPartitionColumnStatisticsInput.
        :rtype: bool
        """
        return self._aggregate_statics

    @aggregate_statics.setter
    def aggregate_statics(self, aggregate_statics):
        """Sets the aggregate_statics of this GetPartitionColumnStatisticsInput.

        是否聚合返回统计信息

        :param aggregate_statics: The aggregate_statics of this GetPartitionColumnStatisticsInput.
        :type aggregate_statics: bool
        """
        self._aggregate_statics = aggregate_statics

    @property
    def column_names(self):
        """Gets the column_names of this GetPartitionColumnStatisticsInput.

        统计信息的列名

        :return: The column_names of this GetPartitionColumnStatisticsInput.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this GetPartitionColumnStatisticsInput.

        统计信息的列名

        :param column_names: The column_names of this GetPartitionColumnStatisticsInput.
        :type column_names: list[str]
        """
        self._column_names = column_names

    @property
    def partition_values_list(self):
        """Gets the partition_values_list of this GetPartitionColumnStatisticsInput.

        需要统计的分区值列表

        :return: The partition_values_list of this GetPartitionColumnStatisticsInput.
        :rtype: list[list[str]]
        """
        return self._partition_values_list

    @partition_values_list.setter
    def partition_values_list(self, partition_values_list):
        """Sets the partition_values_list of this GetPartitionColumnStatisticsInput.

        需要统计的分区值列表

        :param partition_values_list: The partition_values_list of this GetPartitionColumnStatisticsInput.
        :type partition_values_list: list[list[str]]
        """
        self._partition_values_list = partition_values_list

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
        if not isinstance(other, GetPartitionColumnStatisticsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
