# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionConsumingStates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_id': 'str',
        'sequence_number': 'str',
        'latest_offset': 'int',
        'earliest_offset': 'int',
        'checkpoint_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'partition_id': 'partition_id',
        'sequence_number': 'sequence_number',
        'latest_offset': 'latest_offset',
        'earliest_offset': 'earliest_offset',
        'checkpoint_type': 'checkpoint_type',
        'status': 'status'
    }

    def __init__(self, partition_id=None, sequence_number=None, latest_offset=None, earliest_offset=None, checkpoint_type=None, status=None):
        r"""PartitionConsumingStates

        The model defined in huaweicloud sdk

        :param partition_id: 通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002
        :type partition_id: str
        :param sequence_number: 需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。
        :type sequence_number: str
        :param latest_offset: 索引位置, 最新的一条索引位置。
        :type latest_offset: int
        :param earliest_offset: 索引位置, 最早的一条索引位置。
        :type earliest_offset: int
        :param checkpoint_type: Checkpoint类型。 - LAST_READ：在数据库中只记录序列号。
        :type checkpoint_type: str
        :param status: 分区的当前状态。 - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期
        :type status: str
        """
        
        

        self._partition_id = None
        self._sequence_number = None
        self._latest_offset = None
        self._earliest_offset = None
        self._checkpoint_type = None
        self._status = None
        self.discriminator = None

        if partition_id is not None:
            self.partition_id = partition_id
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if latest_offset is not None:
            self.latest_offset = latest_offset
        if earliest_offset is not None:
            self.earliest_offset = earliest_offset
        if checkpoint_type is not None:
            self.checkpoint_type = checkpoint_type
        if status is not None:
            self.status = status

    @property
    def partition_id(self):
        r"""Gets the partition_id of this PartitionConsumingStates.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :return: The partition_id of this PartitionConsumingStates.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        r"""Sets the partition_id of this PartitionConsumingStates.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :param partition_id: The partition_id of this PartitionConsumingStates.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def sequence_number(self):
        r"""Gets the sequence_number of this PartitionConsumingStates.

        需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。

        :return: The sequence_number of this PartitionConsumingStates.
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        r"""Sets the sequence_number of this PartitionConsumingStates.

        需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。

        :param sequence_number: The sequence_number of this PartitionConsumingStates.
        :type sequence_number: str
        """
        self._sequence_number = sequence_number

    @property
    def latest_offset(self):
        r"""Gets the latest_offset of this PartitionConsumingStates.

        索引位置, 最新的一条索引位置。

        :return: The latest_offset of this PartitionConsumingStates.
        :rtype: int
        """
        return self._latest_offset

    @latest_offset.setter
    def latest_offset(self, latest_offset):
        r"""Sets the latest_offset of this PartitionConsumingStates.

        索引位置, 最新的一条索引位置。

        :param latest_offset: The latest_offset of this PartitionConsumingStates.
        :type latest_offset: int
        """
        self._latest_offset = latest_offset

    @property
    def earliest_offset(self):
        r"""Gets the earliest_offset of this PartitionConsumingStates.

        索引位置, 最早的一条索引位置。

        :return: The earliest_offset of this PartitionConsumingStates.
        :rtype: int
        """
        return self._earliest_offset

    @earliest_offset.setter
    def earliest_offset(self, earliest_offset):
        r"""Sets the earliest_offset of this PartitionConsumingStates.

        索引位置, 最早的一条索引位置。

        :param earliest_offset: The earliest_offset of this PartitionConsumingStates.
        :type earliest_offset: int
        """
        self._earliest_offset = earliest_offset

    @property
    def checkpoint_type(self):
        r"""Gets the checkpoint_type of this PartitionConsumingStates.

        Checkpoint类型。 - LAST_READ：在数据库中只记录序列号。

        :return: The checkpoint_type of this PartitionConsumingStates.
        :rtype: str
        """
        return self._checkpoint_type

    @checkpoint_type.setter
    def checkpoint_type(self, checkpoint_type):
        r"""Sets the checkpoint_type of this PartitionConsumingStates.

        Checkpoint类型。 - LAST_READ：在数据库中只记录序列号。

        :param checkpoint_type: The checkpoint_type of this PartitionConsumingStates.
        :type checkpoint_type: str
        """
        self._checkpoint_type = checkpoint_type

    @property
    def status(self):
        r"""Gets the status of this PartitionConsumingStates.

        分区的当前状态。 - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期

        :return: The status of this PartitionConsumingStates.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PartitionConsumingStates.

        分区的当前状态。 - CREATING：创建中 - ACTIVE：可用 - DELETED：删除中 - EXPIRED：已过期

        :param status: The status of this PartitionConsumingStates.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PartitionConsumingStates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
