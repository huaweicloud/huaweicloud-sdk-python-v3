# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitCheckpointReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'checkpoint_type': 'str',
        'stream_name': 'str',
        'partition_id': 'str',
        'sequence_number': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'checkpoint_type': 'checkpoint_type',
        'stream_name': 'stream_name',
        'partition_id': 'partition_id',
        'sequence_number': 'sequence_number',
        'metadata': 'metadata'
    }

    def __init__(self, app_name=None, checkpoint_type=None, stream_name=None, partition_id=None, sequence_number=None, metadata=None):
        r"""CommitCheckpointReq

        The model defined in huaweicloud sdk

        :param app_name: APP的名称，用户数据消费程序的唯一标识符，需要先通过创建App接口创建。
        :type app_name: str
        :param checkpoint_type: Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。
        :type checkpoint_type: str
        :param stream_name: 已创建的通道名称。
        :type stream_name: str
        :param partition_id: 通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002
        :type partition_id: str
        :param sequence_number: 需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。
        :type sequence_number: str
        :param metadata: 用户消费程序端的元数据信息。  元数据信息的最大长度为1000个字符。
        :type metadata: str
        """
        
        

        self._app_name = None
        self._checkpoint_type = None
        self._stream_name = None
        self._partition_id = None
        self._sequence_number = None
        self._metadata = None
        self.discriminator = None

        self.app_name = app_name
        self.checkpoint_type = checkpoint_type
        self.stream_name = stream_name
        self.partition_id = partition_id
        self.sequence_number = sequence_number
        if metadata is not None:
            self.metadata = metadata

    @property
    def app_name(self):
        r"""Gets the app_name of this CommitCheckpointReq.

        APP的名称，用户数据消费程序的唯一标识符，需要先通过创建App接口创建。

        :return: The app_name of this CommitCheckpointReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this CommitCheckpointReq.

        APP的名称，用户数据消费程序的唯一标识符，需要先通过创建App接口创建。

        :param app_name: The app_name of this CommitCheckpointReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def checkpoint_type(self):
        r"""Gets the checkpoint_type of this CommitCheckpointReq.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :return: The checkpoint_type of this CommitCheckpointReq.
        :rtype: str
        """
        return self._checkpoint_type

    @checkpoint_type.setter
    def checkpoint_type(self, checkpoint_type):
        r"""Sets the checkpoint_type of this CommitCheckpointReq.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :param checkpoint_type: The checkpoint_type of this CommitCheckpointReq.
        :type checkpoint_type: str
        """
        self._checkpoint_type = checkpoint_type

    @property
    def stream_name(self):
        r"""Gets the stream_name of this CommitCheckpointReq.

        已创建的通道名称。

        :return: The stream_name of this CommitCheckpointReq.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this CommitCheckpointReq.

        已创建的通道名称。

        :param stream_name: The stream_name of this CommitCheckpointReq.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def partition_id(self):
        r"""Gets the partition_id of this CommitCheckpointReq.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :return: The partition_id of this CommitCheckpointReq.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        r"""Sets the partition_id of this CommitCheckpointReq.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0 比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :param partition_id: The partition_id of this CommitCheckpointReq.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def sequence_number(self):
        r"""Gets the sequence_number of this CommitCheckpointReq.

        需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。

        :return: The sequence_number of this CommitCheckpointReq.
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        r"""Sets the sequence_number of this CommitCheckpointReq.

        需要提交的序列号，用来记录该通道的消费检查点，需要保证该序列号处于有效范围内。

        :param sequence_number: The sequence_number of this CommitCheckpointReq.
        :type sequence_number: str
        """
        self._sequence_number = sequence_number

    @property
    def metadata(self):
        r"""Gets the metadata of this CommitCheckpointReq.

        用户消费程序端的元数据信息。  元数据信息的最大长度为1000个字符。

        :return: The metadata of this CommitCheckpointReq.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CommitCheckpointReq.

        用户消费程序端的元数据信息。  元数据信息的最大长度为1000个字符。

        :param metadata: The metadata of this CommitCheckpointReq.
        :type metadata: str
        """
        self._metadata = metadata

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
        if not isinstance(other, CommitCheckpointReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
