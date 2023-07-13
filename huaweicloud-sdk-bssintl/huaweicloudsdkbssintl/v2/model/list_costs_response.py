# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCostsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'currency': 'str',
        'total_count': 'int',
        'cost_data': 'list[CostDataByDimension]'
    }

    attribute_map = {
        'currency': 'currency',
        'total_count': 'total_count',
        'cost_data': 'cost_data'
    }

    def __init__(self, currency=None, total_count=None, cost_data=None):
        """ListCostsResponse

        The model defined in huaweicloud sdk

        :param currency: 货币。 USD：美元
        :type currency: str
        :param total_count: 总条数。
        :type total_count: int
        :param cost_data: 按天或按月的明细金额。
        :type cost_data: list[:class:`huaweicloudsdkbssintl.v2.CostDataByDimension`]
        """
        
        super(ListCostsResponse, self).__init__()

        self._currency = None
        self._total_count = None
        self._cost_data = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if total_count is not None:
            self.total_count = total_count
        if cost_data is not None:
            self.cost_data = cost_data

    @property
    def currency(self):
        """Gets the currency of this ListCostsResponse.

        货币。 USD：美元

        :return: The currency of this ListCostsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListCostsResponse.

        货币。 USD：美元

        :param currency: The currency of this ListCostsResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def total_count(self):
        """Gets the total_count of this ListCostsResponse.

        总条数。

        :return: The total_count of this ListCostsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCostsResponse.

        总条数。

        :param total_count: The total_count of this ListCostsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def cost_data(self):
        """Gets the cost_data of this ListCostsResponse.

        按天或按月的明细金额。

        :return: The cost_data of this ListCostsResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.CostDataByDimension`]
        """
        return self._cost_data

    @cost_data.setter
    def cost_data(self, cost_data):
        """Sets the cost_data of this ListCostsResponse.

        按天或按月的明细金额。

        :param cost_data: The cost_data of this ListCostsResponse.
        :type cost_data: list[:class:`huaweicloudsdkbssintl.v2.CostDataByDimension`]
        """
        self._cost_data = cost_data

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
        if not isinstance(other, ListCostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
