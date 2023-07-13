# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_logs': 'list[OperationLog]',
        'count': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'operation_logs': 'operation_logs',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, operation_logs=None, count=None, limit=None, offset=None):
        """ListOpLogsResponse

        The model defined in huaweicloud sdk

        :param operation_logs: 任务列表
        :type operation_logs: list[:class:`huaweicloudsdkcbr.v1.OperationLog`]
        :param count: 任务个数
        :type count: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        """
        
        super(ListOpLogsResponse, self).__init__()

        self._operation_logs = None
        self._count = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if operation_logs is not None:
            self.operation_logs = operation_logs
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def operation_logs(self):
        """Gets the operation_logs of this ListOpLogsResponse.

        任务列表

        :return: The operation_logs of this ListOpLogsResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.OperationLog`]
        """
        return self._operation_logs

    @operation_logs.setter
    def operation_logs(self, operation_logs):
        """Sets the operation_logs of this ListOpLogsResponse.

        任务列表

        :param operation_logs: The operation_logs of this ListOpLogsResponse.
        :type operation_logs: list[:class:`huaweicloudsdkcbr.v1.OperationLog`]
        """
        self._operation_logs = operation_logs

    @property
    def count(self):
        """Gets the count of this ListOpLogsResponse.

        任务个数

        :return: The count of this ListOpLogsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListOpLogsResponse.

        任务个数

        :param count: The count of this ListOpLogsResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        """Gets the limit of this ListOpLogsResponse.

        每页显示的条目数量

        :return: The limit of this ListOpLogsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOpLogsResponse.

        每页显示的条目数量

        :param limit: The limit of this ListOpLogsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListOpLogsResponse.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListOpLogsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOpLogsResponse.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListOpLogsResponse.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListOpLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
