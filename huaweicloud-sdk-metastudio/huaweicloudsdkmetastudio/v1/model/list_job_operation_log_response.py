# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobOperationLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'operations': 'list[OperationLogItem]'
    }

    attribute_map = {
        'count': 'count',
        'operations': 'operations'
    }

    def __init__(self, count=None, operations=None):
        r"""ListJobOperationLogResponse

        The model defined in huaweicloud sdk

        :param count: 满足查询要求的操作日志总数
        :type count: int
        :param operations: 操作日志列表
        :type operations: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogItem`]
        """
        
        super(ListJobOperationLogResponse, self).__init__()

        self._count = None
        self._operations = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if operations is not None:
            self.operations = operations

    @property
    def count(self):
        r"""Gets the count of this ListJobOperationLogResponse.

        满足查询要求的操作日志总数

        :return: The count of this ListJobOperationLogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListJobOperationLogResponse.

        满足查询要求的操作日志总数

        :param count: The count of this ListJobOperationLogResponse.
        :type count: int
        """
        self._count = count

    @property
    def operations(self):
        r"""Gets the operations of this ListJobOperationLogResponse.

        操作日志列表

        :return: The operations of this ListJobOperationLogResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogItem`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this ListJobOperationLogResponse.

        操作日志列表

        :param operations: The operations of this ListJobOperationLogResponse.
        :type operations: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogItem`]
        """
        self._operations = operations

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
        if not isinstance(other, ListJobOperationLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
