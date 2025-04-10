# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStreamRequest:

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
        'start_partition_id': 'str',
        'limit_partitions': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'start_partition_id': 'start_partitionId',
        'limit_partitions': 'limit_partitions'
    }

    def __init__(self, stream_name=None, start_partition_id=None, limit_partitions=None):
        r"""ShowStreamRequest

        The model defined in huaweicloud sdk

        :param stream_name: 需要查询的通道名称。
        :type stream_name: str
        :param start_partition_id: 从该分区值开始返回分区列表，返回的分区列表不包括此分区。
        :type start_partition_id: str
        :param limit_partitions: 单次请求返回的最大分区数。
        :type limit_partitions: int
        """
        
        

        self._stream_name = None
        self._start_partition_id = None
        self._limit_partitions = None
        self.discriminator = None

        self.stream_name = stream_name
        if start_partition_id is not None:
            self.start_partition_id = start_partition_id
        if limit_partitions is not None:
            self.limit_partitions = limit_partitions

    @property
    def stream_name(self):
        r"""Gets the stream_name of this ShowStreamRequest.

        需要查询的通道名称。

        :return: The stream_name of this ShowStreamRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this ShowStreamRequest.

        需要查询的通道名称。

        :param stream_name: The stream_name of this ShowStreamRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def start_partition_id(self):
        r"""Gets the start_partition_id of this ShowStreamRequest.

        从该分区值开始返回分区列表，返回的分区列表不包括此分区。

        :return: The start_partition_id of this ShowStreamRequest.
        :rtype: str
        """
        return self._start_partition_id

    @start_partition_id.setter
    def start_partition_id(self, start_partition_id):
        r"""Sets the start_partition_id of this ShowStreamRequest.

        从该分区值开始返回分区列表，返回的分区列表不包括此分区。

        :param start_partition_id: The start_partition_id of this ShowStreamRequest.
        :type start_partition_id: str
        """
        self._start_partition_id = start_partition_id

    @property
    def limit_partitions(self):
        r"""Gets the limit_partitions of this ShowStreamRequest.

        单次请求返回的最大分区数。

        :return: The limit_partitions of this ShowStreamRequest.
        :rtype: int
        """
        return self._limit_partitions

    @limit_partitions.setter
    def limit_partitions(self, limit_partitions):
        r"""Sets the limit_partitions of this ShowStreamRequest.

        单次请求返回的最大分区数。

        :param limit_partitions: The limit_partitions of this ShowStreamRequest.
        :type limit_partitions: int
        """
        self._limit_partitions = limit_partitions

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
        if not isinstance(other, ShowStreamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
