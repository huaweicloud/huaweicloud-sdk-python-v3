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
        'auto_pay_policy': 'str',
        'auto_renew_policy': 'str'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'auto_pay_policy': 'auto_pay_policy',
        'auto_renew_policy': 'auto_renew_policy'
    }

    def __init__(self, period_type=None, period_num=None, auto_pay_policy=None, auto_renew_policy=None):
        r"""ToPeriodReq

        The model defined in huaweicloud sdk

        :param period_type: 周期类型。MONTH：月；YEAR：年
        :type period_type: str
        :param period_num: 周期数。
        :type period_num: int
        :param auto_pay_policy: 是否自动支付。YES：自动扣费；NO：手动支付（默认）
        :type auto_pay_policy: str
        :param auto_renew_policy: 是否到期自动续期。YES：自动续费；NO：不自动续费（默认）
        :type auto_renew_policy: str
        """
        
        

        self._period_type = None
        self._period_num = None
        self._auto_pay_policy = None
        self._auto_renew_policy = None
        self.discriminator = None

        self.period_type = period_type
        self.period_num = period_num
        if auto_pay_policy is not None:
            self.auto_pay_policy = auto_pay_policy
        if auto_renew_policy is not None:
            self.auto_renew_policy = auto_renew_policy

    @property
    def period_type(self):
        r"""Gets the period_type of this ToPeriodReq.

        周期类型。MONTH：月；YEAR：年

        :return: The period_type of this ToPeriodReq.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ToPeriodReq.

        周期类型。MONTH：月；YEAR：年

        :param period_type: The period_type of this ToPeriodReq.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ToPeriodReq.

        周期数。

        :return: The period_num of this ToPeriodReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ToPeriodReq.

        周期数。

        :param period_num: The period_num of this ToPeriodReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def auto_pay_policy(self):
        r"""Gets the auto_pay_policy of this ToPeriodReq.

        是否自动支付。YES：自动扣费；NO：手动支付（默认）

        :return: The auto_pay_policy of this ToPeriodReq.
        :rtype: str
        """
        return self._auto_pay_policy

    @auto_pay_policy.setter
    def auto_pay_policy(self, auto_pay_policy):
        r"""Sets the auto_pay_policy of this ToPeriodReq.

        是否自动支付。YES：自动扣费；NO：手动支付（默认）

        :param auto_pay_policy: The auto_pay_policy of this ToPeriodReq.
        :type auto_pay_policy: str
        """
        self._auto_pay_policy = auto_pay_policy

    @property
    def auto_renew_policy(self):
        r"""Gets the auto_renew_policy of this ToPeriodReq.

        是否到期自动续期。YES：自动续费；NO：不自动续费（默认）

        :return: The auto_renew_policy of this ToPeriodReq.
        :rtype: str
        """
        return self._auto_renew_policy

    @auto_renew_policy.setter
    def auto_renew_policy(self, auto_renew_policy):
        r"""Sets the auto_renew_policy of this ToPeriodReq.

        是否到期自动续期。YES：自动续费；NO：不自动续费（默认）

        :param auto_renew_policy: The auto_renew_policy of this ToPeriodReq.
        :type auto_renew_policy: str
        """
        self._auto_renew_policy = auto_renew_policy

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
