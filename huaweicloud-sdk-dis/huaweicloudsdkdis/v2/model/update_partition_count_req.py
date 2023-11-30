# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePartitionCountReq:

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
        'target_partition_count': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'target_partition_count': 'target_partition_count'
    }

    def __init__(self, stream_name=None, target_partition_count=None):
        """UpdatePartitionCountReq

        The model defined in huaweicloud sdk

        :param stream_name: 需要变更分区数量的通道名称。
        :type stream_name: str
        :param target_partition_count: 变更的目标分区数量。  取值为大于0的整数。  设置的值大于当前分区数量表示扩容，小于当前分区数量表示缩容。  注意：  每个通道在一小时内扩容和缩容总次数最多5次，且一小时内扩容或缩容操作有一次成功则最近一小时内不允许再次进行扩容或缩容操作。
        :type target_partition_count: int
        """
        
        

        self._stream_name = None
        self._target_partition_count = None
        self.discriminator = None

        self.stream_name = stream_name
        self.target_partition_count = target_partition_count

    @property
    def stream_name(self):
        """Gets the stream_name of this UpdatePartitionCountReq.

        需要变更分区数量的通道名称。

        :return: The stream_name of this UpdatePartitionCountReq.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this UpdatePartitionCountReq.

        需要变更分区数量的通道名称。

        :param stream_name: The stream_name of this UpdatePartitionCountReq.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def target_partition_count(self):
        """Gets the target_partition_count of this UpdatePartitionCountReq.

        变更的目标分区数量。  取值为大于0的整数。  设置的值大于当前分区数量表示扩容，小于当前分区数量表示缩容。  注意：  每个通道在一小时内扩容和缩容总次数最多5次，且一小时内扩容或缩容操作有一次成功则最近一小时内不允许再次进行扩容或缩容操作。

        :return: The target_partition_count of this UpdatePartitionCountReq.
        :rtype: int
        """
        return self._target_partition_count

    @target_partition_count.setter
    def target_partition_count(self, target_partition_count):
        """Sets the target_partition_count of this UpdatePartitionCountReq.

        变更的目标分区数量。  取值为大于0的整数。  设置的值大于当前分区数量表示扩容，小于当前分区数量表示缩容。  注意：  每个通道在一小时内扩容和缩容总次数最多5次，且一小时内扩容或缩容操作有一次成功则最近一小时内不允许再次进行扩容或缩容操作。

        :param target_partition_count: The target_partition_count of this UpdatePartitionCountReq.
        :type target_partition_count: int
        """
        self._target_partition_count = target_partition_count

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
        if not isinstance(other, UpdatePartitionCountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
