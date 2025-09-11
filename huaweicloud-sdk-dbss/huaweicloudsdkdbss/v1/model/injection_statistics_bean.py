# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InjectionStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'injection_num': 'int',
        'period': 'str'
    }

    attribute_map = {
        'injection_num': 'injection_num',
        'period': 'period'
    }

    def __init__(self, injection_num=None, period=None):
        r"""InjectionStatisticsBean

        The model defined in huaweicloud sdk

        :param injection_num: 注入数量
        :type injection_num: int
        :param period: 周期
        :type period: str
        """
        
        

        self._injection_num = None
        self._period = None
        self.discriminator = None

        if injection_num is not None:
            self.injection_num = injection_num
        if period is not None:
            self.period = period

    @property
    def injection_num(self):
        r"""Gets the injection_num of this InjectionStatisticsBean.

        注入数量

        :return: The injection_num of this InjectionStatisticsBean.
        :rtype: int
        """
        return self._injection_num

    @injection_num.setter
    def injection_num(self, injection_num):
        r"""Sets the injection_num of this InjectionStatisticsBean.

        注入数量

        :param injection_num: The injection_num of this InjectionStatisticsBean.
        :type injection_num: int
        """
        self._injection_num = injection_num

    @property
    def period(self):
        r"""Gets the period of this InjectionStatisticsBean.

        周期

        :return: The period of this InjectionStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this InjectionStatisticsBean.

        周期

        :param period: The period of this InjectionStatisticsBean.
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
        if not isinstance(other, InjectionStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
