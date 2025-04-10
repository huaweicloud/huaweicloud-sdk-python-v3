# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCursorRequest:

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
        'cursor_type': 'str',
        'starting_sequence_number': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'stream_name': 'stream-name',
        'partition_id': 'partition-id',
        'cursor_type': 'cursor-type',
        'starting_sequence_number': 'starting-sequence-number',
        'timestamp': 'timestamp'
    }

    def __init__(self, stream_name=None, partition_id=None, cursor_type=None, starting_sequence_number=None, timestamp=None):
        r"""ShowCursorRequest

        The model defined in huaweicloud sdk

        :param stream_name: 已创建的通道名称。
        :type stream_name: str
        :param partition_id: 通道的分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002
        :type partition_id: str
        :param cursor_type: 游标类型。  - AT_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）所在的记录开始读取数据。此类型为默认游标类型。  - AFTER_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）后的记录开始读取数据。  - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。例如，某租户使用DIS的通道，分别上传了三条数据A1，A2，A3。N天后（设定A1已过期，A2和A3仍在有效期范围内），该租户需要下载此三条数据，并选择了TRIM_HORIZON这种下载方式。那么用户可下载的数据将从A2开始读取。  - LATEST：从分区中的最新记录开始读取，此设置可以保证你总是读到分区中最新记录。  - AT_TIMESTAMP：从特定时间戳（即timestamp定义的时间戳）开始读取。
        :type cursor_type: str
        :param starting_sequence_number: 序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。  序列号与游标类型AT_SEQUENCE_NUMBER和AFTER_SEQUENCE_NUMBER强相关，二者共同确定读取数据的位置。  取值范围：0~9223372036854775807。
        :type starting_sequence_number: str
        :param timestamp: 开始读取数据记录的时间戳，与游标类型AT_TIMESTAMP强相关，二者共同确定读取数据的位置。  说明：  此时间戳精确到毫秒。
        :type timestamp: int
        """
        
        

        self._stream_name = None
        self._partition_id = None
        self._cursor_type = None
        self._starting_sequence_number = None
        self._timestamp = None
        self.discriminator = None

        self.stream_name = stream_name
        self.partition_id = partition_id
        if cursor_type is not None:
            self.cursor_type = cursor_type
        if starting_sequence_number is not None:
            self.starting_sequence_number = starting_sequence_number
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def stream_name(self):
        r"""Gets the stream_name of this ShowCursorRequest.

        已创建的通道名称。

        :return: The stream_name of this ShowCursorRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this ShowCursorRequest.

        已创建的通道名称。

        :param stream_name: The stream_name of this ShowCursorRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def partition_id(self):
        r"""Gets the partition_id of this ShowCursorRequest.

        通道的分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :return: The partition_id of this ShowCursorRequest.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        r"""Sets the partition_id of this ShowCursorRequest.

        通道的分区标识符。  可定义为如下两种样式：  - shardId-0000000000 - 0  比如一个通道有三个分区，那么分区标识符分别为0, 1, 2，或者shardId-0000000000, shardId-0000000001, shardId-0000000002

        :param partition_id: The partition_id of this ShowCursorRequest.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def cursor_type(self):
        r"""Gets the cursor_type of this ShowCursorRequest.

        游标类型。  - AT_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）所在的记录开始读取数据。此类型为默认游标类型。  - AFTER_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）后的记录开始读取数据。  - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。例如，某租户使用DIS的通道，分别上传了三条数据A1，A2，A3。N天后（设定A1已过期，A2和A3仍在有效期范围内），该租户需要下载此三条数据，并选择了TRIM_HORIZON这种下载方式。那么用户可下载的数据将从A2开始读取。  - LATEST：从分区中的最新记录开始读取，此设置可以保证你总是读到分区中最新记录。  - AT_TIMESTAMP：从特定时间戳（即timestamp定义的时间戳）开始读取。

        :return: The cursor_type of this ShowCursorRequest.
        :rtype: str
        """
        return self._cursor_type

    @cursor_type.setter
    def cursor_type(self, cursor_type):
        r"""Sets the cursor_type of this ShowCursorRequest.

        游标类型。  - AT_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）所在的记录开始读取数据。此类型为默认游标类型。  - AFTER_SEQUENCE_NUMBER：从特定序列号（即starting-sequence-number定义的序列号）后的记录开始读取数据。  - TRIM_HORIZON：从最早被存储至分区的有效记录开始读取。例如，某租户使用DIS的通道，分别上传了三条数据A1，A2，A3。N天后（设定A1已过期，A2和A3仍在有效期范围内），该租户需要下载此三条数据，并选择了TRIM_HORIZON这种下载方式。那么用户可下载的数据将从A2开始读取。  - LATEST：从分区中的最新记录开始读取，此设置可以保证你总是读到分区中最新记录。  - AT_TIMESTAMP：从特定时间戳（即timestamp定义的时间戳）开始读取。

        :param cursor_type: The cursor_type of this ShowCursorRequest.
        :type cursor_type: str
        """
        self._cursor_type = cursor_type

    @property
    def starting_sequence_number(self):
        r"""Gets the starting_sequence_number of this ShowCursorRequest.

        序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。  序列号与游标类型AT_SEQUENCE_NUMBER和AFTER_SEQUENCE_NUMBER强相关，二者共同确定读取数据的位置。  取值范围：0~9223372036854775807。

        :return: The starting_sequence_number of this ShowCursorRequest.
        :rtype: str
        """
        return self._starting_sequence_number

    @starting_sequence_number.setter
    def starting_sequence_number(self, starting_sequence_number):
        r"""Sets the starting_sequence_number of this ShowCursorRequest.

        序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。  序列号与游标类型AT_SEQUENCE_NUMBER和AFTER_SEQUENCE_NUMBER强相关，二者共同确定读取数据的位置。  取值范围：0~9223372036854775807。

        :param starting_sequence_number: The starting_sequence_number of this ShowCursorRequest.
        :type starting_sequence_number: str
        """
        self._starting_sequence_number = starting_sequence_number

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowCursorRequest.

        开始读取数据记录的时间戳，与游标类型AT_TIMESTAMP强相关，二者共同确定读取数据的位置。  说明：  此时间戳精确到毫秒。

        :return: The timestamp of this ShowCursorRequest.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowCursorRequest.

        开始读取数据记录的时间戳，与游标类型AT_TIMESTAMP强相关，二者共同确定读取数据的位置。  说明：  此时间戳精确到毫秒。

        :param timestamp: The timestamp of this ShowCursorRequest.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, ShowCursorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
