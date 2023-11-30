# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_record_count': 'int',
        'records': 'list[PutRecordsResultEntry]'
    }

    attribute_map = {
        'failed_record_count': 'failed_record_count',
        'records': 'records'
    }

    def __init__(self, failed_record_count=None, records=None):
        """SendRecordsResponse

        The model defined in huaweicloud sdk

        :param failed_record_count: 上传失败的数据数量。
        :type failed_record_count: int
        :param records: 上传结果列表。
        :type records: list[:class:`huaweicloudsdkdis.v2.PutRecordsResultEntry`]
        """
        
        super(SendRecordsResponse, self).__init__()

        self._failed_record_count = None
        self._records = None
        self.discriminator = None

        if failed_record_count is not None:
            self.failed_record_count = failed_record_count
        if records is not None:
            self.records = records

    @property
    def failed_record_count(self):
        """Gets the failed_record_count of this SendRecordsResponse.

        上传失败的数据数量。

        :return: The failed_record_count of this SendRecordsResponse.
        :rtype: int
        """
        return self._failed_record_count

    @failed_record_count.setter
    def failed_record_count(self, failed_record_count):
        """Sets the failed_record_count of this SendRecordsResponse.

        上传失败的数据数量。

        :param failed_record_count: The failed_record_count of this SendRecordsResponse.
        :type failed_record_count: int
        """
        self._failed_record_count = failed_record_count

    @property
    def records(self):
        """Gets the records of this SendRecordsResponse.

        上传结果列表。

        :return: The records of this SendRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PutRecordsResultEntry`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this SendRecordsResponse.

        上传结果列表。

        :param records: The records of this SendRecordsResponse.
        :type records: list[:class:`huaweicloudsdkdis.v2.PutRecordsResultEntry`]
        """
        self._records = records

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
        if not isinstance(other, SendRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
