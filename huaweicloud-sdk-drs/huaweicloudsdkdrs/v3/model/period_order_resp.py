# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodOrderResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'order_id': 'str',
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'eff_time': 'str',
        'exp_time': 'str'
    }

    attribute_map = {
        'status': 'status',
        'order_id': 'order_id',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'eff_time': 'eff_time',
        'exp_time': 'exp_time'
    }

    def __init__(self, status=None, order_id=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, eff_time=None, exp_time=None):
        r"""PeriodOrderResp

        The model defined in huaweicloud sdk

        :param status: 订单状态
        :type status: str
        :param order_id: 订单ID
        :type order_id: str
        :param charging_mode: 计费模式
        :type charging_mode: int
        :param period_type: 订购包周期类型
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param is_auto_renew: 是否自动续费
        :type is_auto_renew: int
        :param eff_time: 资源生效时间（即资源创建时间）
        :type eff_time: str
        :param exp_time: 到期时间
        :type exp_time: str
        """
        
        

        self._status = None
        self._order_id = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._eff_time = None
        self._exp_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if order_id is not None:
            self.order_id = order_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if eff_time is not None:
            self.eff_time = eff_time
        if exp_time is not None:
            self.exp_time = exp_time

    @property
    def status(self):
        r"""Gets the status of this PeriodOrderResp.

        订单状态

        :return: The status of this PeriodOrderResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PeriodOrderResp.

        订单状态

        :param status: The status of this PeriodOrderResp.
        :type status: str
        """
        self._status = status

    @property
    def order_id(self):
        r"""Gets the order_id of this PeriodOrderResp.

        订单ID

        :return: The order_id of this PeriodOrderResp.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this PeriodOrderResp.

        订单ID

        :param order_id: The order_id of this PeriodOrderResp.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this PeriodOrderResp.

        计费模式

        :return: The charging_mode of this PeriodOrderResp.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this PeriodOrderResp.

        计费模式

        :param charging_mode: The charging_mode of this PeriodOrderResp.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this PeriodOrderResp.

        订购包周期类型

        :return: The period_type of this PeriodOrderResp.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PeriodOrderResp.

        订购包周期类型

        :param period_type: The period_type of this PeriodOrderResp.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this PeriodOrderResp.

        订购周期数

        :return: The period_num of this PeriodOrderResp.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PeriodOrderResp.

        订购周期数

        :param period_num: The period_num of this PeriodOrderResp.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this PeriodOrderResp.

        是否自动续费

        :return: The is_auto_renew of this PeriodOrderResp.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this PeriodOrderResp.

        是否自动续费

        :param is_auto_renew: The is_auto_renew of this PeriodOrderResp.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def eff_time(self):
        r"""Gets the eff_time of this PeriodOrderResp.

        资源生效时间（即资源创建时间）

        :return: The eff_time of this PeriodOrderResp.
        :rtype: str
        """
        return self._eff_time

    @eff_time.setter
    def eff_time(self, eff_time):
        r"""Sets the eff_time of this PeriodOrderResp.

        资源生效时间（即资源创建时间）

        :param eff_time: The eff_time of this PeriodOrderResp.
        :type eff_time: str
        """
        self._eff_time = eff_time

    @property
    def exp_time(self):
        r"""Gets the exp_time of this PeriodOrderResp.

        到期时间

        :return: The exp_time of this PeriodOrderResp.
        :rtype: str
        """
        return self._exp_time

    @exp_time.setter
    def exp_time(self, exp_time):
        r"""Sets the exp_time of this PeriodOrderResp.

        到期时间

        :param exp_time: The exp_time of this PeriodOrderResp.
        :type exp_time: str
        """
        self._exp_time = exp_time

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
        if not isinstance(other, PeriodOrderResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
