# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaleCycleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pay_mode': 'str',
        'period_type': 'str',
        'period_num': 'list[int]'
    }

    attribute_map = {
        'pay_mode': 'pay_mode',
        'period_type': 'period_type',
        'period_num': 'period_num'
    }

    def __init__(self, pay_mode=None, period_type=None, period_num=None):
        r"""SaleCycleOption

        The model defined in huaweicloud sdk

        :param pay_mode: 包周期付款类型 - FULL: 全预付 - HALF：半预付 - PAID_BY_YEAR：按年付费 - ZERO_PAID_BY_YEAR：零预付-按年
        :type pay_mode: str
        :param period_type: 包周期类型 - year：包年
        :type period_type: str
        :param period_num: 销售周期取值
        :type period_num: list[int]
        """
        
        

        self._pay_mode = None
        self._period_type = None
        self._period_num = None
        self.discriminator = None

        if pay_mode is not None:
            self.pay_mode = pay_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this SaleCycleOption.

        包周期付款类型 - FULL: 全预付 - HALF：半预付 - PAID_BY_YEAR：按年付费 - ZERO_PAID_BY_YEAR：零预付-按年

        :return: The pay_mode of this SaleCycleOption.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this SaleCycleOption.

        包周期付款类型 - FULL: 全预付 - HALF：半预付 - PAID_BY_YEAR：按年付费 - ZERO_PAID_BY_YEAR：零预付-按年

        :param pay_mode: The pay_mode of this SaleCycleOption.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this SaleCycleOption.

        包周期类型 - year：包年

        :return: The period_type of this SaleCycleOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this SaleCycleOption.

        包周期类型 - year：包年

        :param period_type: The period_type of this SaleCycleOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this SaleCycleOption.

        销售周期取值

        :return: The period_num of this SaleCycleOption.
        :rtype: list[int]
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this SaleCycleOption.

        销售周期取值

        :param period_num: The period_num of this SaleCycleOption.
        :type period_num: list[int]
        """
        self._period_num = period_num

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SaleCycleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
