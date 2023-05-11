# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpenApiCalledRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'succeed': 'int',
        'failed': 'int',
        'openapi_called_records': 'list[OpenApiCalledRecord]',
        'next_marker': 'str'
    }

    attribute_map = {
        'total': 'total',
        'succeed': 'succeed',
        'failed': 'failed',
        'openapi_called_records': 'openapi_called_records',
        'next_marker': 'next_marker'
    }

    def __init__(self, total=None, succeed=None, failed=None, openapi_called_records=None, next_marker=None):
        """ShowOpenApiCalledRecordsResponse

        The model defined in huaweicloud sdk

        :param total: 调用API总次数
        :type total: int
        :param succeed: 调用API成功次数
        :type succeed: int
        :param failed: 调用API失败次数
        :type failed: int
        :param openapi_called_records: API调用记录列表
        :type openapi_called_records: list[:class:`huaweicloudsdkdsc.v1.OpenApiCalledRecord`]
        :param next_marker: 获取下一页所需的标识符。
        :type next_marker: str
        """
        
        super(ShowOpenApiCalledRecordsResponse, self).__init__()

        self._total = None
        self._succeed = None
        self._failed = None
        self._openapi_called_records = None
        self._next_marker = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if succeed is not None:
            self.succeed = succeed
        if failed is not None:
            self.failed = failed
        if openapi_called_records is not None:
            self.openapi_called_records = openapi_called_records
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def total(self):
        """Gets the total of this ShowOpenApiCalledRecordsResponse.

        调用API总次数

        :return: The total of this ShowOpenApiCalledRecordsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowOpenApiCalledRecordsResponse.

        调用API总次数

        :param total: The total of this ShowOpenApiCalledRecordsResponse.
        :type total: int
        """
        self._total = total

    @property
    def succeed(self):
        """Gets the succeed of this ShowOpenApiCalledRecordsResponse.

        调用API成功次数

        :return: The succeed of this ShowOpenApiCalledRecordsResponse.
        :rtype: int
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        """Sets the succeed of this ShowOpenApiCalledRecordsResponse.

        调用API成功次数

        :param succeed: The succeed of this ShowOpenApiCalledRecordsResponse.
        :type succeed: int
        """
        self._succeed = succeed

    @property
    def failed(self):
        """Gets the failed of this ShowOpenApiCalledRecordsResponse.

        调用API失败次数

        :return: The failed of this ShowOpenApiCalledRecordsResponse.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this ShowOpenApiCalledRecordsResponse.

        调用API失败次数

        :param failed: The failed of this ShowOpenApiCalledRecordsResponse.
        :type failed: int
        """
        self._failed = failed

    @property
    def openapi_called_records(self):
        """Gets the openapi_called_records of this ShowOpenApiCalledRecordsResponse.

        API调用记录列表

        :return: The openapi_called_records of this ShowOpenApiCalledRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.OpenApiCalledRecord`]
        """
        return self._openapi_called_records

    @openapi_called_records.setter
    def openapi_called_records(self, openapi_called_records):
        """Sets the openapi_called_records of this ShowOpenApiCalledRecordsResponse.

        API调用记录列表

        :param openapi_called_records: The openapi_called_records of this ShowOpenApiCalledRecordsResponse.
        :type openapi_called_records: list[:class:`huaweicloudsdkdsc.v1.OpenApiCalledRecord`]
        """
        self._openapi_called_records = openapi_called_records

    @property
    def next_marker(self):
        """Gets the next_marker of this ShowOpenApiCalledRecordsResponse.

        获取下一页所需的标识符。

        :return: The next_marker of this ShowOpenApiCalledRecordsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ShowOpenApiCalledRecordsResponse.

        获取下一页所需的标识符。

        :param next_marker: The next_marker of this ShowOpenApiCalledRecordsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ShowOpenApiCalledRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
