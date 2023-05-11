# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubCustomerBudgetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'budget_amount': 'float',
        'used_amount': 'float',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'budget_amount': 'budget_amount',
        'used_amount': 'used_amount',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, budget_amount=None, used_amount=None, measure_id=None, currency=None):
        """ShowSubCustomerBudgetResponse

        The model defined in huaweicloud sdk

        :param budget_amount: 初始预算金额。
        :type budget_amount: float
        :param used_amount: 已经使用的预算。该预算存在一定的时延和误差。
        :type used_amount: float
        :param measure_id: 金额单位。 1：元
        :type measure_id: int
        :param currency: 币种。 USD：美金
        :type currency: str
        """
        
        super(ShowSubCustomerBudgetResponse, self).__init__()

        self._budget_amount = None
        self._used_amount = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if budget_amount is not None:
            self.budget_amount = budget_amount
        if used_amount is not None:
            self.used_amount = used_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def budget_amount(self):
        """Gets the budget_amount of this ShowSubCustomerBudgetResponse.

        初始预算金额。

        :return: The budget_amount of this ShowSubCustomerBudgetResponse.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this ShowSubCustomerBudgetResponse.

        初始预算金额。

        :param budget_amount: The budget_amount of this ShowSubCustomerBudgetResponse.
        :type budget_amount: float
        """
        self._budget_amount = budget_amount

    @property
    def used_amount(self):
        """Gets the used_amount of this ShowSubCustomerBudgetResponse.

        已经使用的预算。该预算存在一定的时延和误差。

        :return: The used_amount of this ShowSubCustomerBudgetResponse.
        :rtype: float
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """Sets the used_amount of this ShowSubCustomerBudgetResponse.

        已经使用的预算。该预算存在一定的时延和误差。

        :param used_amount: The used_amount of this ShowSubCustomerBudgetResponse.
        :type used_amount: float
        """
        self._used_amount = used_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ShowSubCustomerBudgetResponse.

        金额单位。 1：元

        :return: The measure_id of this ShowSubCustomerBudgetResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ShowSubCustomerBudgetResponse.

        金额单位。 1：元

        :param measure_id: The measure_id of this ShowSubCustomerBudgetResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ShowSubCustomerBudgetResponse.

        币种。 USD：美金

        :return: The currency of this ShowSubCustomerBudgetResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShowSubCustomerBudgetResponse.

        币种。 USD：美金

        :param currency: The currency of this ShowSubCustomerBudgetResponse.
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
        if not isinstance(other, ShowSubCustomerBudgetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
