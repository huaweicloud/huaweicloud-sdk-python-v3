# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOperationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'histories': 'list[ListHistoryOperationsResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'histories': 'histories',
        'total_count': 'total_count'
    }

    def __init__(self, histories=None, total_count=None):
        """ListHistoryOperationsResponse

        The model defined in huaweicloud sdk

        :param histories: 参数修改历史的列表记录。
        :type histories: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListHistoryOperationsResult`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListHistoryOperationsResponse, self).__init__()

        self._histories = None
        self._total_count = None
        self.discriminator = None

        if histories is not None:
            self.histories = histories
        if total_count is not None:
            self.total_count = total_count

    @property
    def histories(self):
        """Gets the histories of this ListHistoryOperationsResponse.

        参数修改历史的列表记录。

        :return: The histories of this ListHistoryOperationsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListHistoryOperationsResult`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ListHistoryOperationsResponse.

        参数修改历史的列表记录。

        :param histories: The histories of this ListHistoryOperationsResponse.
        :type histories: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListHistoryOperationsResult`]
        """
        self._histories = histories

    @property
    def total_count(self):
        """Gets the total_count of this ListHistoryOperationsResponse.

        总记录数。

        :return: The total_count of this ListHistoryOperationsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListHistoryOperationsResponse.

        总记录数。

        :param total_count: The total_count of this ListHistoryOperationsResponse.
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
        if not isinstance(other, ListHistoryOperationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
