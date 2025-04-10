# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'partition_id': 'str',
        'hash_range': 'str',
        'sequence_number_range': 'str',
        'parent_partitions': 'str'
    }

    attribute_map = {
        'status': 'status',
        'partition_id': 'partition_id',
        'hash_range': 'hash_range',
        'sequence_number_range': 'sequence_number_range',
        'parent_partitions': 'parent_partitions'
    }

    def __init__(self, status=None, partition_id=None, hash_range=None, sequence_number_range=None, parent_partitions=None):
        r"""PartitionResult

        The model defined in huaweicloud sdk

        :param status: 分区的当前状态。  - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期
        :type status: str
        :param partition_id: 分区的唯一标识符。
        :type partition_id: str
        :param hash_range: 分区的可能哈希键值范围。
        :type hash_range: str
        :param sequence_number_range: 分区的序列号范围。
        :type sequence_number_range: str
        :param parent_partitions: 父分区。
        :type parent_partitions: str
        """
        
        

        self._status = None
        self._partition_id = None
        self._hash_range = None
        self._sequence_number_range = None
        self._parent_partitions = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if partition_id is not None:
            self.partition_id = partition_id
        if hash_range is not None:
            self.hash_range = hash_range
        if sequence_number_range is not None:
            self.sequence_number_range = sequence_number_range
        if parent_partitions is not None:
            self.parent_partitions = parent_partitions

    @property
    def status(self):
        r"""Gets the status of this PartitionResult.

        分区的当前状态。  - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期

        :return: The status of this PartitionResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PartitionResult.

        分区的当前状态。  - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期

        :param status: The status of this PartitionResult.
        :type status: str
        """
        self._status = status

    @property
    def partition_id(self):
        r"""Gets the partition_id of this PartitionResult.

        分区的唯一标识符。

        :return: The partition_id of this PartitionResult.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        r"""Sets the partition_id of this PartitionResult.

        分区的唯一标识符。

        :param partition_id: The partition_id of this PartitionResult.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def hash_range(self):
        r"""Gets the hash_range of this PartitionResult.

        分区的可能哈希键值范围。

        :return: The hash_range of this PartitionResult.
        :rtype: str
        """
        return self._hash_range

    @hash_range.setter
    def hash_range(self, hash_range):
        r"""Sets the hash_range of this PartitionResult.

        分区的可能哈希键值范围。

        :param hash_range: The hash_range of this PartitionResult.
        :type hash_range: str
        """
        self._hash_range = hash_range

    @property
    def sequence_number_range(self):
        r"""Gets the sequence_number_range of this PartitionResult.

        分区的序列号范围。

        :return: The sequence_number_range of this PartitionResult.
        :rtype: str
        """
        return self._sequence_number_range

    @sequence_number_range.setter
    def sequence_number_range(self, sequence_number_range):
        r"""Sets the sequence_number_range of this PartitionResult.

        分区的序列号范围。

        :param sequence_number_range: The sequence_number_range of this PartitionResult.
        :type sequence_number_range: str
        """
        self._sequence_number_range = sequence_number_range

    @property
    def parent_partitions(self):
        r"""Gets the parent_partitions of this PartitionResult.

        父分区。

        :return: The parent_partitions of this PartitionResult.
        :rtype: str
        """
        return self._parent_partitions

    @parent_partitions.setter
    def parent_partitions(self, parent_partitions):
        r"""Sets the parent_partitions of this PartitionResult.

        父分区。

        :param parent_partitions: The parent_partitions of this PartitionResult.
        :type parent_partitions: str
        """
        self._parent_partitions = parent_partitions

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
        if not isinstance(other, PartitionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
