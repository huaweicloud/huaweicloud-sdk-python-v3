# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerBillsFeeRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'records': 'list[MonthlyBillRecord]',
        'currency': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'records': 'records',
        'currency': 'currency'
    }

    def __init__(self, total_count=None, records=None, currency=None):
        r"""ListCustomerBillsFeeRecordsResponse

        The model defined in huaweicloud sdk

        :param total_count: 结果集数量，只有成功才返回这个参数。
        :type total_count: int
        :param records: 资源费用记录数据。 具体请参见表2。
        :type records: list[:class:`huaweicloudsdkbss.v2.MonthlyBillRecord`]
        :param currency: 币种。 CNY：人民币
        :type currency: str
        """
        
        super(ListCustomerBillsFeeRecordsResponse, self).__init__()

        self._total_count = None
        self._records = None
        self._currency = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if records is not None:
            self.records = records
        if currency is not None:
            self.currency = currency

    @property
    def total_count(self):
        r"""Gets the total_count of this ListCustomerBillsFeeRecordsResponse.

        结果集数量，只有成功才返回这个参数。

        :return: The total_count of this ListCustomerBillsFeeRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListCustomerBillsFeeRecordsResponse.

        结果集数量，只有成功才返回这个参数。

        :param total_count: The total_count of this ListCustomerBillsFeeRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def records(self):
        r"""Gets the records of this ListCustomerBillsFeeRecordsResponse.

        资源费用记录数据。 具体请参见表2。

        :return: The records of this ListCustomerBillsFeeRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.MonthlyBillRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListCustomerBillsFeeRecordsResponse.

        资源费用记录数据。 具体请参见表2。

        :param records: The records of this ListCustomerBillsFeeRecordsResponse.
        :type records: list[:class:`huaweicloudsdkbss.v2.MonthlyBillRecord`]
        """
        self._records = records

    @property
    def currency(self):
        r"""Gets the currency of this ListCustomerBillsFeeRecordsResponse.

        币种。 CNY：人民币

        :return: The currency of this ListCustomerBillsFeeRecordsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ListCustomerBillsFeeRecordsResponse.

        币种。 CNY：人民币

        :param currency: The currency of this ListCustomerBillsFeeRecordsResponse.
        :type currency: str
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
        if not isinstance(other, ListCustomerBillsFeeRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
