# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutRecordsResultEntry:

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
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'partition_id': 'partition_id',
        'sequence_number': 'sequence_number',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, partition_id=None, sequence_number=None, error_code=None, error_message=None):
        r"""PutRecordsResultEntry

        The model defined in huaweicloud sdk

        :param partition_id: 数据上传到的分区ID。
        :type partition_id: str
        :param sequence_number: 数据上传到的序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。
        :type sequence_number: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_message: 错误消息。
        :type error_message: str
        """
        
        

        self._partition_id = None
        self._sequence_number = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if partition_id is not None:
            self.partition_id = partition_id
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def partition_id(self):
        r"""Gets the partition_id of this PutRecordsResultEntry.

        数据上传到的分区ID。

        :return: The partition_id of this PutRecordsResultEntry.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        r"""Sets the partition_id of this PutRecordsResultEntry.

        数据上传到的分区ID。

        :param partition_id: The partition_id of this PutRecordsResultEntry.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def sequence_number(self):
        r"""Gets the sequence_number of this PutRecordsResultEntry.

        数据上传到的序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。

        :return: The sequence_number of this PutRecordsResultEntry.
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        r"""Sets the sequence_number of this PutRecordsResultEntry.

        数据上传到的序列号。序列号是每个记录的唯一标识符。序列号由DIS在数据生产者调用PutRecords操作以添加数据到DIS数据通道时DIS服务自动分配的。同一分区键的序列号通常会随时间变化增加。PutRecords请求之间的时间段越长，序列号越大。

        :param sequence_number: The sequence_number of this PutRecordsResultEntry.
        :type sequence_number: str
        """
        self._sequence_number = sequence_number

    @property
    def error_code(self):
        r"""Gets the error_code of this PutRecordsResultEntry.

        错误码。

        :return: The error_code of this PutRecordsResultEntry.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this PutRecordsResultEntry.

        错误码。

        :param error_code: The error_code of this PutRecordsResultEntry.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this PutRecordsResultEntry.

        错误消息。

        :return: The error_message of this PutRecordsResultEntry.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this PutRecordsResultEntry.

        错误消息。

        :param error_message: The error_message of this PutRecordsResultEntry.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, PutRecordsResultEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
