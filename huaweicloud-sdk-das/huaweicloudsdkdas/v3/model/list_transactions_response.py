# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionsResponse(SdkResponse):

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
        'transaction_info_list': 'list[GetTransactionListRespTransactionInfoList]'
    }

    attribute_map = {
        'total': 'total',
        'transaction_info_list': 'transaction_info_list'
    }

    def __init__(self, total=None, transaction_info_list=None):
        r"""ListTransactionsResponse

        The model defined in huaweicloud sdk

        :param total: 历史事务总数
        :type total: int
        :param transaction_info_list: 历史事务信息列表
        :type transaction_info_list: list[:class:`huaweicloudsdkdas.v3.GetTransactionListRespTransactionInfoList`]
        """
        
        super(ListTransactionsResponse, self).__init__()

        self._total = None
        self._transaction_info_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if transaction_info_list is not None:
            self.transaction_info_list = transaction_info_list

    @property
    def total(self):
        r"""Gets the total of this ListTransactionsResponse.

        历史事务总数

        :return: The total of this ListTransactionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTransactionsResponse.

        历史事务总数

        :param total: The total of this ListTransactionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def transaction_info_list(self):
        r"""Gets the transaction_info_list of this ListTransactionsResponse.

        历史事务信息列表

        :return: The transaction_info_list of this ListTransactionsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.GetTransactionListRespTransactionInfoList`]
        """
        return self._transaction_info_list

    @transaction_info_list.setter
    def transaction_info_list(self, transaction_info_list):
        r"""Sets the transaction_info_list of this ListTransactionsResponse.

        历史事务信息列表

        :param transaction_info_list: The transaction_info_list of this ListTransactionsResponse.
        :type transaction_info_list: list[:class:`huaweicloudsdkdas.v3.GetTransactionListRespTransactionInfoList`]
        """
        self._transaction_info_list = transaction_info_list

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
        if not isinstance(other, ListTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
