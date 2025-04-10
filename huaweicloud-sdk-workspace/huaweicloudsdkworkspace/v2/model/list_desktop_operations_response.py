# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopOperationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operations': 'list[OperationForList]',
        'total_count': 'int'
    }

    attribute_map = {
        'operations': 'operations',
        'total_count': 'total_count'
    }

    def __init__(self, operations=None, total_count=None):
        r"""ListDesktopOperationsResponse

        The model defined in huaweicloud sdk

        :param operations: 操作记录。
        :type operations: list[:class:`huaweicloudsdkworkspace.v2.OperationForList`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ListDesktopOperationsResponse, self).__init__()

        self._operations = None
        self._total_count = None
        self.discriminator = None

        if operations is not None:
            self.operations = operations
        if total_count is not None:
            self.total_count = total_count

    @property
    def operations(self):
        r"""Gets the operations of this ListDesktopOperationsResponse.

        操作记录。

        :return: The operations of this ListDesktopOperationsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.OperationForList`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this ListDesktopOperationsResponse.

        操作记录。

        :param operations: The operations of this ListDesktopOperationsResponse.
        :type operations: list[:class:`huaweicloudsdkworkspace.v2.OperationForList`]
        """
        self._operations = operations

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDesktopOperationsResponse.

        总数。

        :return: The total_count of this ListDesktopOperationsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDesktopOperationsResponse.

        总数。

        :param total_count: The total_count of this ListDesktopOperationsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListDesktopOperationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
