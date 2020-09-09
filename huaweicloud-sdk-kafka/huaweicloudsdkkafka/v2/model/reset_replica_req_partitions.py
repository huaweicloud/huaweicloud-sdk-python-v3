# coding: utf-8

import pprint
import re

import six





class ResetReplicaReqPartitions:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'partition': 'int',
        'replicas': 'list[int]'
    }

    attribute_map = {
        'partition': 'partition',
        'replicas': 'replicas'
    }

    def __init__(self, partition=None, replicas=None):
        """ResetReplicaReqPartitions - a model defined in huaweicloud sdk"""
        
        

        self._partition = None
        self._replicas = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if replicas is not None:
            self.replicas = replicas

    @property
    def partition(self):
        """Gets the partition of this ResetReplicaReqPartitions.

        分区ID。

        :return: The partition of this ResetReplicaReqPartitions.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ResetReplicaReqPartitions.

        分区ID。

        :param partition: The partition of this ResetReplicaReqPartitions.
        :type: int
        """
        self._partition = partition

    @property
    def replicas(self):
        """Gets the replicas of this ResetReplicaReqPartitions.

        副本期望所在的broker ID。其中Array首位为leader副本，所有分区需要有同样数量的副本，副本数不能大于总broker的数量。

        :return: The replicas of this ResetReplicaReqPartitions.
        :rtype: list[int]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ResetReplicaReqPartitions.

        副本期望所在的broker ID。其中Array首位为leader副本，所有分区需要有同样数量的副本，副本数不能大于总broker的数量。

        :param replicas: The replicas of this ResetReplicaReqPartitions.
        :type: list[int]
        """
        self._replicas = replicas

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
        if not isinstance(other, ResetReplicaReqPartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
