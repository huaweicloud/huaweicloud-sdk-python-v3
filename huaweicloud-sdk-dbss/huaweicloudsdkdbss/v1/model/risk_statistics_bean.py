# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'high_risk_num': 'int',
        'low_risk_num': 'int',
        'middle_risk_num': 'int',
        'no_risk_num': 'int',
        'period': 'str'
    }

    attribute_map = {
        'high_risk_num': 'high_risk_num',
        'low_risk_num': 'low_risk_num',
        'middle_risk_num': 'middle_risk_num',
        'no_risk_num': 'no_risk_num',
        'period': 'period'
    }

    def __init__(self, high_risk_num=None, low_risk_num=None, middle_risk_num=None, no_risk_num=None, period=None):
        r"""RiskStatisticsBean

        The model defined in huaweicloud sdk

        :param high_risk_num: 高风险数量
        :type high_risk_num: int
        :param low_risk_num: 低风险数量
        :type low_risk_num: int
        :param middle_risk_num: 中风险数量
        :type middle_risk_num: int
        :param no_risk_num: 无风险数量
        :type no_risk_num: int
        :param period: 周期
        :type period: str
        """
        
        

        self._high_risk_num = None
        self._low_risk_num = None
        self._middle_risk_num = None
        self._no_risk_num = None
        self._period = None
        self.discriminator = None

        if high_risk_num is not None:
            self.high_risk_num = high_risk_num
        if low_risk_num is not None:
            self.low_risk_num = low_risk_num
        if middle_risk_num is not None:
            self.middle_risk_num = middle_risk_num
        if no_risk_num is not None:
            self.no_risk_num = no_risk_num
        if period is not None:
            self.period = period

    @property
    def high_risk_num(self):
        r"""Gets the high_risk_num of this RiskStatisticsBean.

        高风险数量

        :return: The high_risk_num of this RiskStatisticsBean.
        :rtype: int
        """
        return self._high_risk_num

    @high_risk_num.setter
    def high_risk_num(self, high_risk_num):
        r"""Sets the high_risk_num of this RiskStatisticsBean.

        高风险数量

        :param high_risk_num: The high_risk_num of this RiskStatisticsBean.
        :type high_risk_num: int
        """
        self._high_risk_num = high_risk_num

    @property
    def low_risk_num(self):
        r"""Gets the low_risk_num of this RiskStatisticsBean.

        低风险数量

        :return: The low_risk_num of this RiskStatisticsBean.
        :rtype: int
        """
        return self._low_risk_num

    @low_risk_num.setter
    def low_risk_num(self, low_risk_num):
        r"""Sets the low_risk_num of this RiskStatisticsBean.

        低风险数量

        :param low_risk_num: The low_risk_num of this RiskStatisticsBean.
        :type low_risk_num: int
        """
        self._low_risk_num = low_risk_num

    @property
    def middle_risk_num(self):
        r"""Gets the middle_risk_num of this RiskStatisticsBean.

        中风险数量

        :return: The middle_risk_num of this RiskStatisticsBean.
        :rtype: int
        """
        return self._middle_risk_num

    @middle_risk_num.setter
    def middle_risk_num(self, middle_risk_num):
        r"""Sets the middle_risk_num of this RiskStatisticsBean.

        中风险数量

        :param middle_risk_num: The middle_risk_num of this RiskStatisticsBean.
        :type middle_risk_num: int
        """
        self._middle_risk_num = middle_risk_num

    @property
    def no_risk_num(self):
        r"""Gets the no_risk_num of this RiskStatisticsBean.

        无风险数量

        :return: The no_risk_num of this RiskStatisticsBean.
        :rtype: int
        """
        return self._no_risk_num

    @no_risk_num.setter
    def no_risk_num(self, no_risk_num):
        r"""Sets the no_risk_num of this RiskStatisticsBean.

        无风险数量

        :param no_risk_num: The no_risk_num of this RiskStatisticsBean.
        :type no_risk_num: int
        """
        self._no_risk_num = no_risk_num

    @property
    def period(self):
        r"""Gets the period of this RiskStatisticsBean.

        周期

        :return: The period of this RiskStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this RiskStatisticsBean.

        周期

        :param period: The period of this RiskStatisticsBean.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, RiskStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
