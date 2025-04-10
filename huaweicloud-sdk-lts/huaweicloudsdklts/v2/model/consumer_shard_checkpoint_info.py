# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumerShardCheckpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shard_id': 'str',
        'checkpoint': 'int'
    }

    attribute_map = {
        'shard_id': 'shard_id',
        'checkpoint': 'checkpoint'
    }

    def __init__(self, shard_id=None, checkpoint=None):
        r"""ConsumerShardCheckpointInfo

        The model defined in huaweicloud sdk

        :param shard_id: 日志Shard ID
        :type shard_id: str
        :param checkpoint: 游标值
        :type checkpoint: int
        """
        
        

        self._shard_id = None
        self._checkpoint = None
        self.discriminator = None

        self.shard_id = shard_id
        self.checkpoint = checkpoint

    @property
    def shard_id(self):
        r"""Gets the shard_id of this ConsumerShardCheckpointInfo.

        日志Shard ID

        :return: The shard_id of this ConsumerShardCheckpointInfo.
        :rtype: str
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        r"""Sets the shard_id of this ConsumerShardCheckpointInfo.

        日志Shard ID

        :param shard_id: The shard_id of this ConsumerShardCheckpointInfo.
        :type shard_id: str
        """
        self._shard_id = shard_id

    @property
    def checkpoint(self):
        r"""Gets the checkpoint of this ConsumerShardCheckpointInfo.

        游标值

        :return: The checkpoint of this ConsumerShardCheckpointInfo.
        :rtype: int
        """
        return self._checkpoint

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        r"""Sets the checkpoint of this ConsumerShardCheckpointInfo.

        游标值

        :param checkpoint: The checkpoint of this ConsumerShardCheckpointInfo.
        :type checkpoint: int
        """
        self._checkpoint = checkpoint

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
        if not isinstance(other, ConsumerShardCheckpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
