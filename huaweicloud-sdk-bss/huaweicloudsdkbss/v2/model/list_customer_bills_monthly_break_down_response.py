# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCustomerBillsMonthlyBreakDownResponse(SdkResponse):


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
        'details': 'list[NvlCostAnalysedBillDetail]'
    }

    attribute_map = {
        'currency': 'currency',
        'total_count': 'total_count',
        'details': 'details'
    }

    def __init__(self, currency=None, total_count=None, details=None):
        """ListCustomerBillsMonthlyBreakDownResponse - a model defined in huaweicloud sdk"""
        
        super(ListCustomerBillsMonthlyBreakDownResponse, self).__init__()

        self._currency = None
        self._total_count = None
        self._details = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if total_count is not None:
            self.total_count = total_count
        if details is not None:
            self.details = details

    @property
    def currency(self):
        """Gets the currency of this ListCustomerBillsMonthlyBreakDownResponse.

        货币单位代码： CNY：人民币

        :return: The currency of this ListCustomerBillsMonthlyBreakDownResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListCustomerBillsMonthlyBreakDownResponse.

        货币单位代码： CNY：人民币

        :param currency: The currency of this ListCustomerBillsMonthlyBreakDownResponse.
        :type: str
        """
        self._currency = currency

    @property
    def total_count(self):
        """Gets the total_count of this ListCustomerBillsMonthlyBreakDownResponse.

        结果集数量，只有成功才返回这个参数。

        :return: The total_count of this ListCustomerBillsMonthlyBreakDownResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCustomerBillsMonthlyBreakDownResponse.

        结果集数量，只有成功才返回这个参数。

        :param total_count: The total_count of this ListCustomerBillsMonthlyBreakDownResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def details(self):
        """Gets the details of this ListCustomerBillsMonthlyBreakDownResponse.

        分摊成本记录数据。 具体请参见表3。

        :return: The details of this ListCustomerBillsMonthlyBreakDownResponse.
        :rtype: list[NvlCostAnalysedBillDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ListCustomerBillsMonthlyBreakDownResponse.

        分摊成本记录数据。 具体请参见表3。

        :param details: The details of this ListCustomerBillsMonthlyBreakDownResponse.
        :type: list[NvlCostAnalysedBillDetail]
        """
        self._details = details

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCustomerBillsMonthlyBreakDownResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
