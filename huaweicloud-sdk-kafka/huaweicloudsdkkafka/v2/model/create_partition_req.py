# coding: utf-8

import pprint
import re

import six





class CreatePartitionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'partition': 'int'
    }

    attribute_map = {
        'partition': 'partition'
    }

    def __init__(self, partition=None):
        """CreatePartitionReq - a model defined in huaweicloud sdk"""
        
        

        self._partition = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition

    @property
    def partition(self):
        """Gets the partition of this CreatePartitionReq.

        期望调整分区后的数量，必须大于当前分区数量，小于等于20。

        :return: The partition of this CreatePartitionReq.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this CreatePartitionReq.

        期望调整分区后的数量，必须大于当前分区数量，小于等于20。

        :param partition: The partition of this CreatePartitionReq.
        :type: int
        """
        self._partition = partition

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
        if not isinstance(other, CreatePartitionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
