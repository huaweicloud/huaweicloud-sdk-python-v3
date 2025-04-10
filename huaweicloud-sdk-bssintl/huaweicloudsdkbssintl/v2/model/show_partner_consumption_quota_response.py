# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPartnerConsumptionQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumption_quota': 'str',
        'amount': 'str',
        'coupon_amount': 'str',
        'due_amount': 'str',
        'unbilled_amount': 'str',
        'used_consumption_quota': 'str',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'consumption_quota': 'consumption_quota',
        'amount': 'amount',
        'coupon_amount': 'coupon_amount',
        'due_amount': 'due_amount',
        'unbilled_amount': 'unbilled_amount',
        'used_consumption_quota': 'used_consumption_quota',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, consumption_quota=None, amount=None, coupon_amount=None, due_amount=None, unbilled_amount=None, used_consumption_quota=None, measure_id=None, currency=None):
        r"""ShowPartnerConsumptionQuotaResponse

        The model defined in huaweicloud sdk

        :param consumption_quota: |参数名称：总消费配额| |参数约束及描述：非必填|
        :type consumption_quota: str
        :param amount: |参数名称：账户余额| |参数约束及描述：非必填|
        :type amount: str
        :param coupon_amount: |参数名称：代金券余额| |参数约束及描述：非必填|
        :type coupon_amount: str
        :param due_amount: |参数名称：应还金额| |参数约束及描述：非必填|
        :type due_amount: str
        :param unbilled_amount: |参数名称：未出账预估金额| |参数约束及描述：非必填|
        :type unbilled_amount: str
        :param used_consumption_quota: |参数名称：已使用消费配额| |参数约束及描述：非必填，used_consumption_quota &#x3D; due_amount + unbilled_amount - amount - coupon_amount|
        :type used_consumption_quota: str
        :param measure_id: |参数名称：金额单位| |参数约束及描述：金额单位，1：元|
        :type measure_id: int
        :param currency: |参数名称：货币单位| |参数约束及描述：货币单位 |
        :type currency: str
        """
        
        super(ShowPartnerConsumptionQuotaResponse, self).__init__()

        self._consumption_quota = None
        self._amount = None
        self._coupon_amount = None
        self._due_amount = None
        self._unbilled_amount = None
        self._used_consumption_quota = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if consumption_quota is not None:
            self.consumption_quota = consumption_quota
        if amount is not None:
            self.amount = amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if due_amount is not None:
            self.due_amount = due_amount
        if unbilled_amount is not None:
            self.unbilled_amount = unbilled_amount
        if used_consumption_quota is not None:
            self.used_consumption_quota = used_consumption_quota
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def consumption_quota(self):
        r"""Gets the consumption_quota of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：总消费配额| |参数约束及描述：非必填|

        :return: The consumption_quota of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._consumption_quota

    @consumption_quota.setter
    def consumption_quota(self, consumption_quota):
        r"""Sets the consumption_quota of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：总消费配额| |参数约束及描述：非必填|

        :param consumption_quota: The consumption_quota of this ShowPartnerConsumptionQuotaResponse.
        :type consumption_quota: str
        """
        self._consumption_quota = consumption_quota

    @property
    def amount(self):
        r"""Gets the amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：账户余额| |参数约束及描述：非必填|

        :return: The amount of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：账户余额| |参数约束及描述：非必填|

        :param amount: The amount of this ShowPartnerConsumptionQuotaResponse.
        :type amount: str
        """
        self._amount = amount

    @property
    def coupon_amount(self):
        r"""Gets the coupon_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：代金券余额| |参数约束及描述：非必填|

        :return: The coupon_amount of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        r"""Sets the coupon_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：代金券余额| |参数约束及描述：非必填|

        :param coupon_amount: The coupon_amount of this ShowPartnerConsumptionQuotaResponse.
        :type coupon_amount: str
        """
        self._coupon_amount = coupon_amount

    @property
    def due_amount(self):
        r"""Gets the due_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：应还金额| |参数约束及描述：非必填|

        :return: The due_amount of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._due_amount

    @due_amount.setter
    def due_amount(self, due_amount):
        r"""Sets the due_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：应还金额| |参数约束及描述：非必填|

        :param due_amount: The due_amount of this ShowPartnerConsumptionQuotaResponse.
        :type due_amount: str
        """
        self._due_amount = due_amount

    @property
    def unbilled_amount(self):
        r"""Gets the unbilled_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：未出账预估金额| |参数约束及描述：非必填|

        :return: The unbilled_amount of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._unbilled_amount

    @unbilled_amount.setter
    def unbilled_amount(self, unbilled_amount):
        r"""Sets the unbilled_amount of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：未出账预估金额| |参数约束及描述：非必填|

        :param unbilled_amount: The unbilled_amount of this ShowPartnerConsumptionQuotaResponse.
        :type unbilled_amount: str
        """
        self._unbilled_amount = unbilled_amount

    @property
    def used_consumption_quota(self):
        r"""Gets the used_consumption_quota of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：已使用消费配额| |参数约束及描述：非必填，used_consumption_quota = due_amount + unbilled_amount - amount - coupon_amount|

        :return: The used_consumption_quota of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._used_consumption_quota

    @used_consumption_quota.setter
    def used_consumption_quota(self, used_consumption_quota):
        r"""Sets the used_consumption_quota of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：已使用消费配额| |参数约束及描述：非必填，used_consumption_quota = due_amount + unbilled_amount - amount - coupon_amount|

        :param used_consumption_quota: The used_consumption_quota of this ShowPartnerConsumptionQuotaResponse.
        :type used_consumption_quota: str
        """
        self._used_consumption_quota = used_consumption_quota

    @property
    def measure_id(self):
        r"""Gets the measure_id of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：金额单位| |参数约束及描述：金额单位，1：元|

        :return: The measure_id of this ShowPartnerConsumptionQuotaResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：金额单位| |参数约束及描述：金额单位，1：元|

        :param measure_id: The measure_id of this ShowPartnerConsumptionQuotaResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        r"""Gets the currency of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：货币单位| |参数约束及描述：货币单位 |

        :return: The currency of this ShowPartnerConsumptionQuotaResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ShowPartnerConsumptionQuotaResponse.

        |参数名称：货币单位| |参数约束及描述：货币单位 |

        :param currency: The currency of this ShowPartnerConsumptionQuotaResponse.
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
        if not isinstance(other, ShowPartnerConsumptionQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
