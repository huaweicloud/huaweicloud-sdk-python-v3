# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCustomerselfResourceRecordDetailsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'monthly_records': 'list[MonthlyBillRes]',
        'total_count': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'monthly_records': 'monthly_records',
        'total_count': 'total_count',
        'currency': 'currency'
    }

    def __init__(self, monthly_records=None, total_count=None, currency=None):
        """ListCustomerselfResourceRecordDetailsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._monthly_records = None
        self._total_count = None
        self._currency = None
        self.discriminator = None

        if monthly_records is not None:
            self.monthly_records = monthly_records
        if total_count is not None:
            self.total_count = total_count
        if currency is not None:
            self.currency = currency

    @property
    def monthly_records(self):
        """Gets the monthly_records of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：资源费用记录数据| |参数的约束及描述：该参数非必填|

        :return: The monthly_records of this ListCustomerselfResourceRecordDetailsResponse.
        :rtype: list[MonthlyBillRes]
        """
        return self._monthly_records

    @monthly_records.setter
    def monthly_records(self, monthly_records):
        """Sets the monthly_records of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：资源费用记录数据| |参数的约束及描述：该参数非必填|

        :param monthly_records: The monthly_records of this ListCustomerselfResourceRecordDetailsResponse.
        :type: list[MonthlyBillRes]
        """
        self._monthly_records = monthly_records

    @property
    def total_count(self):
        """Gets the total_count of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：结果集数量| |参数的约束及描述：该参数非必填，且只允许数字，只有成功才返回这个参数。|

        :return: The total_count of this ListCustomerselfResourceRecordDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：结果集数量| |参数的约束及描述：该参数非必填，且只允许数字，只有成功才返回这个参数。|

        :param total_count: The total_count of this ListCustomerselfResourceRecordDetailsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def currency(self):
        """Gets the currency of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：货币单位代码| |参数的约束及描述：该参数非必填，最大长度3，CNY：人民币；USD：美元|

        :return: The currency of this ListCustomerselfResourceRecordDetailsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListCustomerselfResourceRecordDetailsResponse.

        |参数名称：货币单位代码| |参数的约束及描述：该参数非必填，最大长度3，CNY：人民币；USD：美元|

        :param currency: The currency of this ListCustomerselfResourceRecordDetailsResponse.
        :type: str
        """
        self._currency = currency

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
        if not isinstance(other, ListCustomerselfResourceRecordDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
