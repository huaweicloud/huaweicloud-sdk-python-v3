# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSubCustomerResFeeRecordsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fee_records': 'list[SubCustomerResFeeRecordV2]',
        'count': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'fee_records': 'fee_records',
        'count': 'count',
        'currency': 'currency'
    }

    def __init__(self, fee_records=None, count=None, currency=None):
        """ListSubCustomerResFeeRecordsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._fee_records = None
        self._count = None
        self._currency = None
        self.discriminator = None

        if fee_records is not None:
            self.fee_records = fee_records
        if count is not None:
            self.count = count
        if currency is not None:
            self.currency = currency

    @property
    def fee_records(self):
        """Gets the fee_records of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：资源费用记录数据。具体请参见表 ResFeeRecordV2。| |参数约束以及描述：资源费用记录数据。具体请参见表 ResFeeRecordV2。|

        :return: The fee_records of this ListSubCustomerResFeeRecordsResponse.
        :rtype: list[SubCustomerResFeeRecordV2]
        """
        return self._fee_records

    @fee_records.setter
    def fee_records(self, fee_records):
        """Sets the fee_records of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：资源费用记录数据。具体请参见表 ResFeeRecordV2。| |参数约束以及描述：资源费用记录数据。具体请参见表 ResFeeRecordV2。|

        :param fee_records: The fee_records of this ListSubCustomerResFeeRecordsResponse.
        :type: list[SubCustomerResFeeRecordV2]
        """
        self._fee_records = fee_records

    @property
    def count(self):
        """Gets the count of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：结果集数量，只有成功才返回这个参数。| |参数的约束及描述：结果集数量，只有成功才返回这个参数。|

        :return: The count of this ListSubCustomerResFeeRecordsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：结果集数量，只有成功才返回这个参数。| |参数的约束及描述：结果集数量，只有成功才返回这个参数。|

        :param count: The count of this ListSubCustomerResFeeRecordsResponse.
        :type: int
        """
        self._count = count

    @property
    def currency(self):
        """Gets the currency of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：货币单位代码：CNY：人民币USD：美元| |参数约束及描述：货币单位代码：CNY：人民币USD：美元|

        :return: The currency of this ListSubCustomerResFeeRecordsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListSubCustomerResFeeRecordsResponse.

        |参数名称：货币单位代码：CNY：人民币USD：美元| |参数约束及描述：货币单位代码：CNY：人民币USD：美元|

        :param currency: The currency of this ListSubCustomerResFeeRecordsResponse.
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
        if not isinstance(other, ListSubCustomerResFeeRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
