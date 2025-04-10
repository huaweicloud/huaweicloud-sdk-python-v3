# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleUpExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_num': 'int',
        'period_type': 'str',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'period_num': 'periodNum',
        'period_type': 'periodType',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, period_num=None, period_type=None, is_auto_renew=None, is_auto_pay=None):
        r"""ScaleUpExtendParam

        The model defined in huaweicloud sdk

        :param period_num: 包周期时长, 包月1-9, 包年1-3
        :type period_num: int
        :param period_type: 包周期类型, year(包年), month(包月)
        :type period_type: str
        :param is_auto_renew: 是否自动续费，可选参数，如果不填写，以节点池isAutoRenew属性为准。
        :type is_auto_renew: bool
        :param is_auto_pay: 是否自动付费，可选参数，如果不填写，以节点池isAutoPay属性为准。
        :type is_auto_pay: bool
        """
        
        

        self._period_num = None
        self._period_type = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self.discriminator = None

        self.period_num = period_num
        self.period_type = period_type
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def period_num(self):
        r"""Gets the period_num of this ScaleUpExtendParam.

        包周期时长, 包月1-9, 包年1-3

        :return: The period_num of this ScaleUpExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ScaleUpExtendParam.

        包周期时长, 包月1-9, 包年1-3

        :param period_num: The period_num of this ScaleUpExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this ScaleUpExtendParam.

        包周期类型, year(包年), month(包月)

        :return: The period_type of this ScaleUpExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ScaleUpExtendParam.

        包周期类型, year(包年), month(包月)

        :param period_type: The period_type of this ScaleUpExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ScaleUpExtendParam.

        是否自动续费，可选参数，如果不填写，以节点池isAutoRenew属性为准。

        :return: The is_auto_renew of this ScaleUpExtendParam.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ScaleUpExtendParam.

        是否自动续费，可选参数，如果不填写，以节点池isAutoRenew属性为准。

        :param is_auto_renew: The is_auto_renew of this ScaleUpExtendParam.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ScaleUpExtendParam.

        是否自动付费，可选参数，如果不填写，以节点池isAutoPay属性为准。

        :return: The is_auto_pay of this ScaleUpExtendParam.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ScaleUpExtendParam.

        是否自动付费，可选参数，如果不填写，以节点池isAutoPay属性为准。

        :param is_auto_pay: The is_auto_pay of this ScaleUpExtendParam.
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
        if not isinstance(other, ScaleUpExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
