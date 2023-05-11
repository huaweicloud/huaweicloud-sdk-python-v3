# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchTransactionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tx_item_list': 'list[TxItemVo]',
        'latest_time': 'int',
        'total_count': 'int',
        'result_id': 'str'
    }

    attribute_map = {
        'tx_item_list': 'tx_item_list',
        'latest_time': 'latest_time',
        'total_count': 'total_count',
        'result_id': 'result_id'
    }

    def __init__(self, tx_item_list=None, latest_time=None, total_count=None, result_id=None):
        """SearchTransactionResponse

        The model defined in huaweicloud sdk

        :param tx_item_list: URL跟踪视图列表。
        :type tx_item_list: list[:class:`huaweicloudsdkapm.v1.TxItemVo`]
        :param latest_time: 最后响应时间。
        :type latest_time: int
        :param total_count: 总数据条数。
        :type total_count: int
        :param result_id: 请求id。
        :type result_id: str
        """
        
        super(SearchTransactionResponse, self).__init__()

        self._tx_item_list = None
        self._latest_time = None
        self._total_count = None
        self._result_id = None
        self.discriminator = None

        if tx_item_list is not None:
            self.tx_item_list = tx_item_list
        if latest_time is not None:
            self.latest_time = latest_time
        if total_count is not None:
            self.total_count = total_count
        if result_id is not None:
            self.result_id = result_id

    @property
    def tx_item_list(self):
        """Gets the tx_item_list of this SearchTransactionResponse.

        URL跟踪视图列表。

        :return: The tx_item_list of this SearchTransactionResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TxItemVo`]
        """
        return self._tx_item_list

    @tx_item_list.setter
    def tx_item_list(self, tx_item_list):
        """Sets the tx_item_list of this SearchTransactionResponse.

        URL跟踪视图列表。

        :param tx_item_list: The tx_item_list of this SearchTransactionResponse.
        :type tx_item_list: list[:class:`huaweicloudsdkapm.v1.TxItemVo`]
        """
        self._tx_item_list = tx_item_list

    @property
    def latest_time(self):
        """Gets the latest_time of this SearchTransactionResponse.

        最后响应时间。

        :return: The latest_time of this SearchTransactionResponse.
        :rtype: int
        """
        return self._latest_time

    @latest_time.setter
    def latest_time(self, latest_time):
        """Sets the latest_time of this SearchTransactionResponse.

        最后响应时间。

        :param latest_time: The latest_time of this SearchTransactionResponse.
        :type latest_time: int
        """
        self._latest_time = latest_time

    @property
    def total_count(self):
        """Gets the total_count of this SearchTransactionResponse.

        总数据条数。

        :return: The total_count of this SearchTransactionResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SearchTransactionResponse.

        总数据条数。

        :param total_count: The total_count of this SearchTransactionResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def result_id(self):
        """Gets the result_id of this SearchTransactionResponse.

        请求id。

        :return: The result_id of this SearchTransactionResponse.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this SearchTransactionResponse.

        请求id。

        :param result_id: The result_id of this SearchTransactionResponse.
        :type result_id: str
        """
        self._result_id = result_id

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
        if not isinstance(other, SearchTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
