# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionResponse(SdkResponse):

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
        'rows_info': 'list[ListTransactionResponseBodyRowsInfo]'
    }

    attribute_map = {
        'total': 'total',
        'rows_info': 'rows_info'
    }

    def __init__(self, total=None, rows_info=None):
        r"""ListTransactionResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 查到的事务数量。 **取值范围**: 不涉及。
        :type total: int
        :param rows_info: **参数解释**: 事务信息列表。
        :type rows_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionResponseBodyRowsInfo`]
        """
        
        super(ListTransactionResponse, self).__init__()

        self._total = None
        self._rows_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if rows_info is not None:
            self.rows_info = rows_info

    @property
    def total(self):
        r"""Gets the total of this ListTransactionResponse.

        **参数解释**: 查到的事务数量。 **取值范围**: 不涉及。

        :return: The total of this ListTransactionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTransactionResponse.

        **参数解释**: 查到的事务数量。 **取值范围**: 不涉及。

        :param total: The total of this ListTransactionResponse.
        :type total: int
        """
        self._total = total

    @property
    def rows_info(self):
        r"""Gets the rows_info of this ListTransactionResponse.

        **参数解释**: 事务信息列表。

        :return: The rows_info of this ListTransactionResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionResponseBodyRowsInfo`]
        """
        return self._rows_info

    @rows_info.setter
    def rows_info(self, rows_info):
        r"""Sets the rows_info of this ListTransactionResponse.

        **参数解释**: 事务信息列表。

        :param rows_info: The rows_info of this ListTransactionResponse.
        :type rows_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListTransactionResponseBodyRowsInfo`]
        """
        self._rows_info = rows_info

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
        if not isinstance(other, ListTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
