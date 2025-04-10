# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerBudgetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'measure_id': 'int',
        'currency': 'str',
        'budget_infos': 'list[BudgetInfo]'
    }

    attribute_map = {
        'measure_id': 'measure_id',
        'currency': 'currency',
        'budget_infos': 'budget_infos'
    }

    def __init__(self, measure_id=None, currency=None, budget_infos=None):
        r"""ListSubCustomerBudgetResponse

        The model defined in huaweicloud sdk

        :param measure_id: |参数名称：金额单位。||参数的约束及描述：非必填参数|
        :type measure_id: int
        :param currency: |参数名称：货币，CNY：人民币，USD：美元||参数的约束及描述：非必填参数|
        :type currency: str
        :param budget_infos: |参数名称：客户预算信息||参数的约束及描述：必填参数|
        :type budget_infos: list[:class:`huaweicloudsdkbssintl.v2.BudgetInfo`]
        """
        
        super(ListSubCustomerBudgetResponse, self).__init__()

        self._measure_id = None
        self._currency = None
        self._budget_infos = None
        self.discriminator = None

        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if budget_infos is not None:
            self.budget_infos = budget_infos

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ListSubCustomerBudgetResponse.

        |参数名称：金额单位。||参数的约束及描述：非必填参数|

        :return: The measure_id of this ListSubCustomerBudgetResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ListSubCustomerBudgetResponse.

        |参数名称：金额单位。||参数的约束及描述：非必填参数|

        :param measure_id: The measure_id of this ListSubCustomerBudgetResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ListSubCustomerBudgetResponse.

        |参数名称：货币，CNY：人民币，USD：美元||参数的约束及描述：非必填参数|

        :return: The currency of this ListSubCustomerBudgetResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ListSubCustomerBudgetResponse.

        |参数名称：货币，CNY：人民币，USD：美元||参数的约束及描述：非必填参数|

        :param currency: The currency of this ListSubCustomerBudgetResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def budget_infos(self):
        r"""Gets the budget_infos of this ListSubCustomerBudgetResponse.

        |参数名称：客户预算信息||参数的约束及描述：必填参数|

        :return: The budget_infos of this ListSubCustomerBudgetResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.BudgetInfo`]
        """
        return self._budget_infos

    @budget_infos.setter
    def budget_infos(self, budget_infos):
        r"""Sets the budget_infos of this ListSubCustomerBudgetResponse.

        |参数名称：客户预算信息||参数的约束及描述：必填参数|

        :param budget_infos: The budget_infos of this ListSubCustomerBudgetResponse.
        :type budget_infos: list[:class:`huaweicloudsdkbssintl.v2.BudgetInfo`]
        """
        self._budget_infos = budget_infos

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
        if not isinstance(other, ListSubCustomerBudgetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
