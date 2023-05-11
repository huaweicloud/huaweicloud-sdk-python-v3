# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlterPartitionEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition': 'PartitionInput',
        'partition_values': 'list[str]'
    }

    attribute_map = {
        'partition': 'partition',
        'partition_values': 'partition_values'
    }

    def __init__(self, partition=None, partition_values=None):
        """AlterPartitionEntry

        The model defined in huaweicloud sdk

        :param partition: 
        :type partition: :class:`huaweicloudsdklakeformation.v1.PartitionInput`
        :param partition_values: 原分区值数组
        :type partition_values: list[str]
        """
        
        

        self._partition = None
        self._partition_values = None
        self.discriminator = None

        self.partition = partition
        self.partition_values = partition_values

    @property
    def partition(self):
        """Gets the partition of this AlterPartitionEntry.

        :return: The partition of this AlterPartitionEntry.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PartitionInput`
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this AlterPartitionEntry.

        :param partition: The partition of this AlterPartitionEntry.
        :type partition: :class:`huaweicloudsdklakeformation.v1.PartitionInput`
        """
        self._partition = partition

    @property
    def partition_values(self):
        """Gets the partition_values of this AlterPartitionEntry.

        原分区值数组

        :return: The partition_values of this AlterPartitionEntry.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        """Sets the partition_values of this AlterPartitionEntry.

        原分区值数组

        :param partition_values: The partition_values of this AlterPartitionEntry.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

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
        if not isinstance(other, AlterPartitionEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
