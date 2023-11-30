# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Record:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_key': 'str',
        'sequence_number': 'str',
        'data': 'str',
        'timestamp': 'int',
        'timestamp_type': 'str'
    }

    attribute_map = {
        'partition_key': 'partition_key',
        'sequence_number': 'sequence_number',
        'data': 'data',
        'timestamp': 'timestamp',
        'timestamp_type': 'timestamp_type'
    }

    def __init__(self, partition_key=None, sequence_number=None, data=None, timestamp=None, timestamp_type=None):
        """Record

        The model defined in huaweicloud sdk

        :param partition_key: 用户上传数据时设置的partition_key。  说明：  上传数据时，如果传了partition_key参数，则下载数据时可返回此参数。如果上传数据时，未传partition_key参数，而是传入partition_id，则不返回partition_key。
        :type partition_key: str
        :param sequence_number: 该条数据的序列号。
        :type sequence_number: str
        :param data: 下载的数据。  下载的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如下载数据接口返回的数据是“ZGF0YQ&#x3D;&#x3D;”，“ZGF0YQ&#x3D;&#x3D;”经过Base64解码之后是“data”。
        :type data: str
        :param timestamp: 记录写入DIS的时间戳。
        :type timestamp: int
        :param timestamp_type: 时间戳类型。  - CreateTime：创建时间。
        :type timestamp_type: str
        """
        
        

        self._partition_key = None
        self._sequence_number = None
        self._data = None
        self._timestamp = None
        self._timestamp_type = None
        self.discriminator = None

        if partition_key is not None:
            self.partition_key = partition_key
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if data is not None:
            self.data = data
        if timestamp is not None:
            self.timestamp = timestamp
        if timestamp_type is not None:
            self.timestamp_type = timestamp_type

    @property
    def partition_key(self):
        """Gets the partition_key of this Record.

        用户上传数据时设置的partition_key。  说明：  上传数据时，如果传了partition_key参数，则下载数据时可返回此参数。如果上传数据时，未传partition_key参数，而是传入partition_id，则不返回partition_key。

        :return: The partition_key of this Record.
        :rtype: str
        """
        return self._partition_key

    @partition_key.setter
    def partition_key(self, partition_key):
        """Sets the partition_key of this Record.

        用户上传数据时设置的partition_key。  说明：  上传数据时，如果传了partition_key参数，则下载数据时可返回此参数。如果上传数据时，未传partition_key参数，而是传入partition_id，则不返回partition_key。

        :param partition_key: The partition_key of this Record.
        :type partition_key: str
        """
        self._partition_key = partition_key

    @property
    def sequence_number(self):
        """Gets the sequence_number of this Record.

        该条数据的序列号。

        :return: The sequence_number of this Record.
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this Record.

        该条数据的序列号。

        :param sequence_number: The sequence_number of this Record.
        :type sequence_number: str
        """
        self._sequence_number = sequence_number

    @property
    def data(self):
        """Gets the data of this Record.

        下载的数据。  下载的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如下载数据接口返回的数据是“ZGF0YQ==”，“ZGF0YQ==”经过Base64解码之后是“data”。

        :return: The data of this Record.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Record.

        下载的数据。  下载的数据为序列化之后的二进制数据（Base64编码后的字符串）。  比如下载数据接口返回的数据是“ZGF0YQ==”，“ZGF0YQ==”经过Base64解码之后是“data”。

        :param data: The data of this Record.
        :type data: str
        """
        self._data = data

    @property
    def timestamp(self):
        """Gets the timestamp of this Record.

        记录写入DIS的时间戳。

        :return: The timestamp of this Record.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Record.

        记录写入DIS的时间戳。

        :param timestamp: The timestamp of this Record.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def timestamp_type(self):
        """Gets the timestamp_type of this Record.

        时间戳类型。  - CreateTime：创建时间。

        :return: The timestamp_type of this Record.
        :rtype: str
        """
        return self._timestamp_type

    @timestamp_type.setter
    def timestamp_type(self, timestamp_type):
        """Sets the timestamp_type of this Record.

        时间戳类型。  - CreateTime：创建时间。

        :param timestamp_type: The timestamp_type of this Record.
        :type timestamp_type: str
        """
        self._timestamp_type = timestamp_type

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
        if not isinstance(other, Record):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
