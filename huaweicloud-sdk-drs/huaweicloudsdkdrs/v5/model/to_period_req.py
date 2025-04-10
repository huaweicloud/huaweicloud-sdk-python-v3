# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ToPeriodReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None):
        r"""ToPeriodReq

        The model defined in huaweicloud sdk

        :param period_type: 订单类型，取值： - 2：包月 - 3：包年
        :type period_type: str
        :param period_num: 订单周期数
        :type period_num: int
        :param is_auto_renew: 是否自动续费
        :type is_auto_renew: bool
        :param is_auto_pay: 是否自动支付
        :type is_auto_pay: bool
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

        self.period_type = period_type
        self.period_num = period_num
        self.is_auto_renew = is_auto_renew
        self.is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this ToPeriodReq.

        订单类型，取值： - 2：包月 - 3：包年

        :return: The period_type of this ToPeriodReq.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ToPeriodReq.

        订单类型，取值： - 2：包月 - 3：包年

        :param period_type: The period_type of this ToPeriodReq.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ToPeriodReq.

        订单周期数

        :return: The period_num of this ToPeriodReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ToPeriodReq.

        订单周期数

        :param period_num: The period_num of this ToPeriodReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ToPeriodReq.

        是否自动续费

        :return: The is_auto_renew of this ToPeriodReq.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ToPeriodReq.

        是否自动续费

        :param is_auto_renew: The is_auto_renew of this ToPeriodReq.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ToPeriodReq.

        是否自动支付

        :return: The is_auto_pay of this ToPeriodReq.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ToPeriodReq.

        是否自动支付

        :param is_auto_pay: The is_auto_pay of this ToPeriodReq.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ToPeriodReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
