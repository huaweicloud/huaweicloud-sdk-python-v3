# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChInstanceInfoPayInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pay_model': 'str',
        'order_id': 'str',
        'period': 'str',
        'period_type': 'str',
        'is_auto_renew': 'str'
    }

    attribute_map = {
        'pay_model': 'pay_model',
        'order_id': 'order_id',
        'period': 'period',
        'period_type': 'period_type',
        'is_auto_renew': 'is_auto_renew'
    }

    def __init__(self, pay_model=None, order_id=None, period=None, period_type=None, is_auto_renew=None):
        r"""CreateChInstanceInfoPayInfo

        The model defined in huaweicloud sdk

        :param pay_model: 计费模式。默认0。 取值范围： - 0：按需计费 - 1：包周期
        :type pay_model: str
        :param order_id: 包周期计费ID。
        :type order_id: str
        :param period: 包周期周期。
        :type period: str
        :param period_type: 包周期周期类型。 取值范围： - 2：包月 - 3：包年
        :type period_type: str
        :param is_auto_renew: 包周期是否自动续费。 取值范围： - 1：自动续费 - 0：不自动续费
        :type is_auto_renew: str
        """
        
        

        self._pay_model = None
        self._order_id = None
        self._period = None
        self._period_type = None
        self._is_auto_renew = None
        self.discriminator = None

        self.pay_model = pay_model
        self.order_id = order_id
        self.period = period
        self.period_type = period_type
        self.is_auto_renew = is_auto_renew

    @property
    def pay_model(self):
        r"""Gets the pay_model of this CreateChInstanceInfoPayInfo.

        计费模式。默认0。 取值范围： - 0：按需计费 - 1：包周期

        :return: The pay_model of this CreateChInstanceInfoPayInfo.
        :rtype: str
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this CreateChInstanceInfoPayInfo.

        计费模式。默认0。 取值范围： - 0：按需计费 - 1：包周期

        :param pay_model: The pay_model of this CreateChInstanceInfoPayInfo.
        :type pay_model: str
        """
        self._pay_model = pay_model

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateChInstanceInfoPayInfo.

        包周期计费ID。

        :return: The order_id of this CreateChInstanceInfoPayInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateChInstanceInfoPayInfo.

        包周期计费ID。

        :param order_id: The order_id of this CreateChInstanceInfoPayInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period(self):
        r"""Gets the period of this CreateChInstanceInfoPayInfo.

        包周期周期。

        :return: The period of this CreateChInstanceInfoPayInfo.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this CreateChInstanceInfoPayInfo.

        包周期周期。

        :param period: The period of this CreateChInstanceInfoPayInfo.
        :type period: str
        """
        self._period = period

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateChInstanceInfoPayInfo.

        包周期周期类型。 取值范围： - 2：包月 - 3：包年

        :return: The period_type of this CreateChInstanceInfoPayInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateChInstanceInfoPayInfo.

        包周期周期类型。 取值范围： - 2：包月 - 3：包年

        :param period_type: The period_type of this CreateChInstanceInfoPayInfo.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this CreateChInstanceInfoPayInfo.

        包周期是否自动续费。 取值范围： - 1：自动续费 - 0：不自动续费

        :return: The is_auto_renew of this CreateChInstanceInfoPayInfo.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this CreateChInstanceInfoPayInfo.

        包周期是否自动续费。 取值范围： - 1：自动续费 - 0：不自动续费

        :param is_auto_renew: The is_auto_renew of this CreateChInstanceInfoPayInfo.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

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
        if not isinstance(other, CreateChInstanceInfoPayInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
