# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaurusDbTxnProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transactions': 'list[TxnItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'transactions': 'transactions',
        'total_count': 'total_count'
    }

    def __init__(self, transactions=None, total_count=None):
        r"""ShowTaurusDbTxnProgressResponse

        The model defined in huaweicloud sdk

        :param transactions: **参数解释**：  处于活跃状态（回滚中）的事务进度列表。如果输入的ID已结束或不存在，则不在此列表中返回。
        :type transactions: list[:class:`huaweicloudsdkgaussdb.v3.TxnItem`]
        :param total_count: **参数解释**： 满足查询条件的事务记录总数。 **取值范围**： 0~100。 
        :type total_count: int
        """
        
        super().__init__()

        self._transactions = None
        self._total_count = None
        self.discriminator = None

        if transactions is not None:
            self.transactions = transactions
        if total_count is not None:
            self.total_count = total_count

    @property
    def transactions(self):
        r"""Gets the transactions of this ShowTaurusDbTxnProgressResponse.

        **参数解释**：  处于活跃状态（回滚中）的事务进度列表。如果输入的ID已结束或不存在，则不在此列表中返回。

        :return: The transactions of this ShowTaurusDbTxnProgressResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TxnItem`]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        r"""Sets the transactions of this ShowTaurusDbTxnProgressResponse.

        **参数解释**：  处于活跃状态（回滚中）的事务进度列表。如果输入的ID已结束或不存在，则不在此列表中返回。

        :param transactions: The transactions of this ShowTaurusDbTxnProgressResponse.
        :type transactions: list[:class:`huaweicloudsdkgaussdb.v3.TxnItem`]
        """
        self._transactions = transactions

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowTaurusDbTxnProgressResponse.

        **参数解释**： 满足查询条件的事务记录总数。 **取值范围**： 0~100。 

        :return: The total_count of this ShowTaurusDbTxnProgressResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowTaurusDbTxnProgressResponse.

        **参数解释**： 满足查询条件的事务记录总数。 **取值范围**： 0~100。 

        :param total_count: The total_count of this ShowTaurusDbTxnProgressResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaurusDbTxnProgressResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaurusDbTxnProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
