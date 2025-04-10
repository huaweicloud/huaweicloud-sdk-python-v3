# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BudgetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'budget_amount': 'decimal.Decimal',
        'used_amount': 'decimal.Decimal',
        'budget_type': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'budget_amount': 'budget_amount',
        'used_amount': 'used_amount',
        'budget_type': 'budget_type'
    }

    def __init__(self, customer_id=None, budget_amount=None, used_amount=None, budget_type=None):
        r"""BudgetInfo

        The model defined in huaweicloud sdk

        :param customer_id: |参数名称：客户账号ID||参数的约束及描述：必填参数，范围限制:1-64|
        :type customer_id: str
        :param budget_amount: |参数名称：初始预算金额。| |参数的约束及描述：非必填，初始预算金额。|
        :type budget_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param used_amount: |参数名称：已经使用的预算。| |参数的约束及描述：已经使用的预算。非必填，该预算存在一定的时延和误差。|
        :type used_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param budget_type: |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算|
        :type budget_type: str
        """
        
        

        self._customer_id = None
        self._budget_amount = None
        self._used_amount = None
        self._budget_type = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if budget_amount is not None:
            self.budget_amount = budget_amount
        if used_amount is not None:
            self.used_amount = used_amount
        if budget_type is not None:
            self.budget_type = budget_type

    @property
    def customer_id(self):
        r"""Gets the customer_id of this BudgetInfo.

        |参数名称：客户账号ID||参数的约束及描述：必填参数，范围限制:1-64|

        :return: The customer_id of this BudgetInfo.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this BudgetInfo.

        |参数名称：客户账号ID||参数的约束及描述：必填参数，范围限制:1-64|

        :param customer_id: The customer_id of this BudgetInfo.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def budget_amount(self):
        r"""Gets the budget_amount of this BudgetInfo.

        |参数名称：初始预算金额。| |参数的约束及描述：非必填，初始预算金额。|

        :return: The budget_amount of this BudgetInfo.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        r"""Sets the budget_amount of this BudgetInfo.

        |参数名称：初始预算金额。| |参数的约束及描述：非必填，初始预算金额。|

        :param budget_amount: The budget_amount of this BudgetInfo.
        :type budget_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._budget_amount = budget_amount

    @property
    def used_amount(self):
        r"""Gets the used_amount of this BudgetInfo.

        |参数名称：已经使用的预算。| |参数的约束及描述：已经使用的预算。非必填，该预算存在一定的时延和误差。|

        :return: The used_amount of this BudgetInfo.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        r"""Sets the used_amount of this BudgetInfo.

        |参数名称：已经使用的预算。| |参数的约束及描述：已经使用的预算。非必填，该预算存在一定的时延和误差。|

        :param used_amount: The used_amount of this BudgetInfo.
        :type used_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._used_amount = used_amount

    @property
    def budget_type(self):
        r"""Gets the budget_type of this BudgetInfo.

        |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算|

        :return: The budget_type of this BudgetInfo.
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        r"""Sets the budget_type of this BudgetInfo.

        |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算|

        :param budget_type: The budget_type of this BudgetInfo.
        :type budget_type: str
        """
        self._budget_type = budget_type

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
        if not isinstance(other, BudgetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
