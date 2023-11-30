# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutRecordsRequestEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'explicit_hash_key': 'str',
        'partition_id': 'str',
        'partition_key': 'str'
    }

    attribute_map = {
        'data': 'data',
        'explicit_hash_key': 'explicit_hash_key',
        'partition_id': 'partition_id',
        'partition_key': 'partition_key'
    }

    def __init__(self, data=None, explicit_hash_key=None, partition_id=None, partition_key=None):
        """PutRecordsRequestEntry

        The model defined in huaweicloud sdk

        :param data: 需要上传的数据。  上传的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如需要上传字符串“data”，“data”经过Base64编码之后是“ZGF0YQ&#x3D;&#x3D;”。
        :type data: str
        :param explicit_hash_key: 用于明确数据需要写入分区的哈希值，此哈希值将覆盖“partition_key”的哈希值。  取值范围：0~long.max
        :type explicit_hash_key: str
        :param partition_id: 通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002
        :type partition_id: str
        :param partition_key: 数据将写入的分区。  说明：  如果传了partition_id参数，则优先使用partition_id参数。如果partition_id没有传，则使用partition_key。
        :type partition_key: str
        """
        
        

        self._data = None
        self._explicit_hash_key = None
        self._partition_id = None
        self._partition_key = None
        self.discriminator = None

        self.data = data
        if explicit_hash_key is not None:
            self.explicit_hash_key = explicit_hash_key
        if partition_id is not None:
            self.partition_id = partition_id
        if partition_key is not None:
            self.partition_key = partition_key

    @property
    def data(self):
        """Gets the data of this PutRecordsRequestEntry.

        需要上传的数据。  上传的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如需要上传字符串“data”，“data”经过Base64编码之后是“ZGF0YQ==”。

        :return: The data of this PutRecordsRequestEntry.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PutRecordsRequestEntry.

        需要上传的数据。  上传的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如需要上传字符串“data”，“data”经过Base64编码之后是“ZGF0YQ==”。

        :param data: The data of this PutRecordsRequestEntry.
        :type data: str
        """
        self._data = data

    @property
    def explicit_hash_key(self):
        """Gets the explicit_hash_key of this PutRecordsRequestEntry.

        用于明确数据需要写入分区的哈希值，此哈希值将覆盖“partition_key”的哈希值。  取值范围：0~long.max

        :return: The explicit_hash_key of this PutRecordsRequestEntry.
        :rtype: str
        """
        return self._explicit_hash_key

    @explicit_hash_key.setter
    def explicit_hash_key(self, explicit_hash_key):
        """Sets the explicit_hash_key of this PutRecordsRequestEntry.

        用于明确数据需要写入分区的哈希值，此哈希值将覆盖“partition_key”的哈希值。  取值范围：0~long.max

        :param explicit_hash_key: The explicit_hash_key of this PutRecordsRequestEntry.
        :type explicit_hash_key: str
        """
        self._explicit_hash_key = explicit_hash_key

    @property
    def partition_id(self):
        """Gets the partition_id of this PutRecordsRequestEntry.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :return: The partition_id of this PutRecordsRequestEntry.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this PutRecordsRequestEntry.

        通道的分区标识符。 可定义为如下两种样式： - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :param partition_id: The partition_id of this PutRecordsRequestEntry.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def partition_key(self):
        """Gets the partition_key of this PutRecordsRequestEntry.

        数据将写入的分区。  说明：  如果传了partition_id参数，则优先使用partition_id参数。如果partition_id没有传，则使用partition_key。

        :return: The partition_key of this PutRecordsRequestEntry.
        :rtype: str
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        """Sets the partition_key of this PutRecordsRequestEntry.

        数据将写入的分区。  说明：  如果传了partition_id参数，则优先使用partition_id参数。如果partition_id没有传，则使用partition_key。

        :param partition_key: The partition_key of this PutRecordsRequestEntry.
        :type partition_key: str
        """
        self._partition_key = partition_key

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
        if not isinstance(other, PutRecordsRequestEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
