# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionOffsetEntity:

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
        'offset': 'int'
    }

    attribute_map = {
        'partition': 'partition',
        'offset': 'offset'
    }

    def __init__(self, partition=None, offset=None):
        r"""PartitionOffsetEntity

        The model defined in huaweicloud sdk

        :param partition: 分区
        :type partition: int
        :param offset: 消费位点
        :type offset: int
        """
        
        

        self._partition = None
        self._offset = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if offset is not None:
            self.offset = offset

    @property
    def partition(self):
        r"""Gets the partition of this PartitionOffsetEntity.

        分区

        :return: The partition of this PartitionOffsetEntity.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this PartitionOffsetEntity.

        分区

        :param partition: The partition of this PartitionOffsetEntity.
        :type partition: int
        """
        self._partition = partition

    @property
    def offset(self):
        r"""Gets the offset of this PartitionOffsetEntity.

        消费位点

        :return: The offset of this PartitionOffsetEntity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this PartitionOffsetEntity.

        消费位点

        :param offset: The offset of this PartitionOffsetEntity.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, PartitionOffsetEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
