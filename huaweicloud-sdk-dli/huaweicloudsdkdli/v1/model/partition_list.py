# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'partition_infos': 'list[Partition]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'partition_infos': 'partition_infos'
    }

    def __init__(self, total_count=None, partition_infos=None):
        r"""PartitionList

        The model defined in huaweicloud sdk

        :param total_count: 总个数
        :type total_count: int
        :param partition_infos: 分区信息列表
        :type partition_infos: list[:class:`huaweicloudsdkdli.v1.Partition`]
        """
        
        

        self._total_count = None
        self._partition_infos = None
        self.discriminator = None

        self.total_count = total_count
        self.partition_infos = partition_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this PartitionList.

        总个数

        :return: The total_count of this PartitionList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this PartitionList.

        总个数

        :param total_count: The total_count of this PartitionList.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def partition_infos(self):
        r"""Gets the partition_infos of this PartitionList.

        分区信息列表

        :return: The partition_infos of this PartitionList.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Partition`]
        """
        return self._partition_infos

    @partition_infos.setter
    def partition_infos(self, partition_infos):
        r"""Sets the partition_infos of this PartitionList.

        分区信息列表

        :param partition_infos: The partition_infos of this PartitionList.
        :type partition_infos: list[:class:`huaweicloudsdkdli.v1.Partition`]
        """
        self._partition_infos = partition_infos

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
        if not isinstance(other, PartitionList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
