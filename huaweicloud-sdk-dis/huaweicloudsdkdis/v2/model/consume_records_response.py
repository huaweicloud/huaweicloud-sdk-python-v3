# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumeRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[Record]',
        'next_partition_cursor': 'str'
    }

    attribute_map = {
        'records': 'records',
        'next_partition_cursor': 'next_partition_cursor'
    }

    def __init__(self, records=None, next_partition_cursor=None):
        """ConsumeRecordsResponse

        The model defined in huaweicloud sdk

        :param records: 下载的记录列表。
        :type records: list[:class:`huaweicloudsdkdis.v2.Record`]
        :param next_partition_cursor: 下一个迭代器。  说明：  数据游标有效期为5分钟。
        :type next_partition_cursor: str
        """
        
        super(ConsumeRecordsResponse, self).__init__()

        self._records = None
        self._next_partition_cursor = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if next_partition_cursor is not None:
            self.next_partition_cursor = next_partition_cursor

    @property
    def records(self):
        """Gets the records of this ConsumeRecordsResponse.

        下载的记录列表。

        :return: The records of this ConsumeRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.Record`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ConsumeRecordsResponse.

        下载的记录列表。

        :param records: The records of this ConsumeRecordsResponse.
        :type records: list[:class:`huaweicloudsdkdis.v2.Record`]
        """
        self._records = records

    @property
    def next_partition_cursor(self):
        """Gets the next_partition_cursor of this ConsumeRecordsResponse.

        下一个迭代器。  说明：  数据游标有效期为5分钟。

        :return: The next_partition_cursor of this ConsumeRecordsResponse.
        :rtype: str
        """
        return self._next_partition_cursor

    @next_partition_cursor.setter
    def next_partition_cursor(self, next_partition_cursor):
        """Sets the next_partition_cursor of this ConsumeRecordsResponse.

        下一个迭代器。  说明：  数据游标有效期为5分钟。

        :param next_partition_cursor: The next_partition_cursor of this ConsumeRecordsResponse.
        :type next_partition_cursor: str
        """
        self._next_partition_cursor = next_partition_cursor

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
        if not isinstance(other, ConsumeRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
