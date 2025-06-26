# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerBudgetRecordsResponse(SdkResponse):

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
        'measure_id': 'int',
        'currency': 'str',
        'record_list': 'list[BudgetRecordInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'record_list': 'record_list'
    }

    def __init__(self, total_count=None, measure_id=None, currency=None, record_list=None):
        r"""ListSubCustomerBudgetRecordsResponse

        The model defined in huaweicloud sdk

        :param total_count: |参数名称：返回总条数。| |参数的约束及描述：范围限制：0-2147483647|
        :type total_count: int
        :param measure_id: |参数名称：金额单位。||参数的约束及描述：范围限制：0-3。1：元|
        :type measure_id: int
        :param currency: |参数名称：币种。||参数的约束及描述：范围限制：0-10。CNY：人民币，USD：美元|
        :type currency: str
        :param record_list: |参数名称：客户预算设置记录列表。||参数的约束及描述：客户预算设置记录列表|
        :type record_list: list[:class:`huaweicloudsdkbssintl.v2.BudgetRecordInfo`]
        """
        
        super(ListSubCustomerBudgetRecordsResponse, self).__init__()

        self._total_count = None
        self._measure_id = None
        self._currency = None
        self._record_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if record_list is not None:
            self.record_list = record_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：返回总条数。| |参数的约束及描述：范围限制：0-2147483647|

        :return: The total_count of this ListSubCustomerBudgetRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：返回总条数。| |参数的约束及描述：范围限制：0-2147483647|

        :param total_count: The total_count of this ListSubCustomerBudgetRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：金额单位。||参数的约束及描述：范围限制：0-3。1：元|

        :return: The measure_id of this ListSubCustomerBudgetRecordsResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：金额单位。||参数的约束及描述：范围限制：0-3。1：元|

        :param measure_id: The measure_id of this ListSubCustomerBudgetRecordsResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：币种。||参数的约束及描述：范围限制：0-10。CNY：人民币，USD：美元|

        :return: The currency of this ListSubCustomerBudgetRecordsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：币种。||参数的约束及描述：范围限制：0-10。CNY：人民币，USD：美元|

        :param currency: The currency of this ListSubCustomerBudgetRecordsResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def record_list(self):
        r"""Gets the record_list of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：客户预算设置记录列表。||参数的约束及描述：客户预算设置记录列表|

        :return: The record_list of this ListSubCustomerBudgetRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.BudgetRecordInfo`]
        """
        return self._record_list

    @record_list.setter
    def record_list(self, record_list):
        r"""Sets the record_list of this ListSubCustomerBudgetRecordsResponse.

        |参数名称：客户预算设置记录列表。||参数的约束及描述：客户预算设置记录列表|

        :param record_list: The record_list of this ListSubCustomerBudgetRecordsResponse.
        :type record_list: list[:class:`huaweicloudsdkbssintl.v2.BudgetRecordInfo`]
        """
        self._record_list = record_list

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
        if not isinstance(other, ListSubCustomerBudgetRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
