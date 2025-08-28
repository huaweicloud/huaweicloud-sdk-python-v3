# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerExpenditureQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'granting_amount': 'decimal.Decimal',
        'granting_amount_used': 'decimal.Decimal',
        'percentage_granting_amount_used': 'decimal.Decimal',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'granting_amount': 'granting_amount',
        'granting_amount_used': 'granting_amount_used',
        'percentage_granting_amount_used': 'percentage_granting_amount_used',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, granting_amount=None, granting_amount_used=None, percentage_granting_amount_used=None, measure_id=None, currency=None):
        r"""ShowCustomerExpenditureQuotaResponse

        The model defined in huaweicloud sdk

        :param granting_amount: |参数名称：消费配额| |参数约束及描述：当前授予额度，消费配额。|
        :type granting_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param granting_amount_used: |参数名称：已使用消费配额| |参数约束及描述：已使用消费配额。|
        :type granting_amount_used: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param percentage_granting_amount_used: |参数名称：已使用消费配额占比| |参数约束及描述：已使用消费配额占比。|
        :type percentage_granting_amount_used: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param measure_id: |参数名称：金额的度量单位。| |参数约束及描述：1：元|
        :type measure_id: int
        :param currency: |参数名称：币种。| |参数约束及描述：货币单位，USD：美元。|
        :type currency: str
        """
        
        super(ShowCustomerExpenditureQuotaResponse, self).__init__()

        self._granting_amount = None
        self._granting_amount_used = None
        self._percentage_granting_amount_used = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if granting_amount is not None:
            self.granting_amount = granting_amount
        if granting_amount_used is not None:
            self.granting_amount_used = granting_amount_used
        if percentage_granting_amount_used is not None:
            self.percentage_granting_amount_used = percentage_granting_amount_used
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def granting_amount(self):
        r"""Gets the granting_amount of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：消费配额| |参数约束及描述：当前授予额度，消费配额。|

        :return: The granting_amount of this ShowCustomerExpenditureQuotaResponse.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._granting_amount

    @granting_amount.setter
    def granting_amount(self, granting_amount):
        r"""Sets the granting_amount of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：消费配额| |参数约束及描述：当前授予额度，消费配额。|

        :param granting_amount: The granting_amount of this ShowCustomerExpenditureQuotaResponse.
        :type granting_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._granting_amount = granting_amount

    @property
    def granting_amount_used(self):
        r"""Gets the granting_amount_used of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：已使用消费配额| |参数约束及描述：已使用消费配额。|

        :return: The granting_amount_used of this ShowCustomerExpenditureQuotaResponse.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._granting_amount_used

    @granting_amount_used.setter
    def granting_amount_used(self, granting_amount_used):
        r"""Sets the granting_amount_used of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：已使用消费配额| |参数约束及描述：已使用消费配额。|

        :param granting_amount_used: The granting_amount_used of this ShowCustomerExpenditureQuotaResponse.
        :type granting_amount_used: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._granting_amount_used = granting_amount_used

    @property
    def percentage_granting_amount_used(self):
        r"""Gets the percentage_granting_amount_used of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：已使用消费配额占比| |参数约束及描述：已使用消费配额占比。|

        :return: The percentage_granting_amount_used of this ShowCustomerExpenditureQuotaResponse.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._percentage_granting_amount_used

    @percentage_granting_amount_used.setter
    def percentage_granting_amount_used(self, percentage_granting_amount_used):
        r"""Sets the percentage_granting_amount_used of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：已使用消费配额占比| |参数约束及描述：已使用消费配额占比。|

        :param percentage_granting_amount_used: The percentage_granting_amount_used of this ShowCustomerExpenditureQuotaResponse.
        :type percentage_granting_amount_used: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._percentage_granting_amount_used = percentage_granting_amount_used

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：金额的度量单位。| |参数约束及描述：1：元|

        :return: The measure_id of this ShowCustomerExpenditureQuotaResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：金额的度量单位。| |参数约束及描述：1：元|

        :param measure_id: The measure_id of this ShowCustomerExpenditureQuotaResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：币种。| |参数约束及描述：货币单位，USD：美元。|

        :return: The currency of this ShowCustomerExpenditureQuotaResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ShowCustomerExpenditureQuotaResponse.

        |参数名称：币种。| |参数约束及描述：货币单位，USD：美元。|

        :param currency: The currency of this ShowCustomerExpenditureQuotaResponse.
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
        if not isinstance(other, ShowCustomerExpenditureQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
