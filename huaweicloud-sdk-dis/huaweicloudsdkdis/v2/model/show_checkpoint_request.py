# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckpointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'partition_id': 'str',
        'app_name': 'str',
        'checkpoint_type': 'str'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'partition_id': 'partition_id',
        'app_name': 'app_name',
        'checkpoint_type': 'checkpoint_type'
    }

    def __init__(self, stream_name=None, partition_id=None, app_name=None, checkpoint_type=None):
        """ShowCheckpointRequest

        The model defined in huaweicloud sdk

        :param stream_name: 该Checkpoint所属的通道名称。
        :type stream_name: str
        :param partition_id: 该Checkpoint所属的通道分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002
        :type partition_id: str
        :param app_name: 该Checkpoint关联App名称。
        :type app_name: str
        :param checkpoint_type: Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。
        :type checkpoint_type: str
        """
        
        

        self._stream_name = None
        self._partition_id = None
        self._app_name = None
        self._checkpoint_type = None
        self.discriminator = None

        self.stream_name = stream_name
        self.partition_id = partition_id
        self.app_name = app_name
        self.checkpoint_type = checkpoint_type

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowCheckpointRequest.

        该Checkpoint所属的通道名称。

        :return: The stream_name of this ShowCheckpointRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowCheckpointRequest.

        该Checkpoint所属的通道名称。

        :param stream_name: The stream_name of this ShowCheckpointRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def partition_id(self):
        """Gets the partition_id of this ShowCheckpointRequest.

        该Checkpoint所属的通道分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :return: The partition_id of this ShowCheckpointRequest.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this ShowCheckpointRequest.

        该Checkpoint所属的通道分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :param partition_id: The partition_id of this ShowCheckpointRequest.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def app_name(self):
        """Gets the app_name of this ShowCheckpointRequest.

        该Checkpoint关联App名称。

        :return: The app_name of this ShowCheckpointRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowCheckpointRequest.

        该Checkpoint关联App名称。

        :param app_name: The app_name of this ShowCheckpointRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def checkpoint_type(self):
        """Gets the checkpoint_type of this ShowCheckpointRequest.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :return: The checkpoint_type of this ShowCheckpointRequest.
        :rtype: str
        """
        return self._checkpoint_type

    @checkpoint_type.setter
    def checkpoint_type(self, checkpoint_type):
        """Sets the checkpoint_type of this ShowCheckpointRequest.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :param checkpoint_type: The checkpoint_type of this ShowCheckpointRequest.
        :type checkpoint_type: str
        """
        self._checkpoint_type = checkpoint_type

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
        if not isinstance(other, ShowCheckpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
