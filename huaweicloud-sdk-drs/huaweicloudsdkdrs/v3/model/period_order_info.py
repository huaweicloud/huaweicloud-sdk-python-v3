# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodOrderInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_renew=None):
        """PeriodOrderInfo

        The model defined in huaweicloud sdk

        :param period_type: 订购周期类型。 取值范围： - 2：表示周期类型为月。 - 3：表示周期类型为年。
        :type period_type: int
        :param period_num: 订购周期数。 取值范围： - period_type&#x3D;2（周期类型为月）时，取值为[1，9]。 - period_type&#x3D;3（周期类型为年）时，取值为[1，3]。
        :type period_num: int
        :param is_auto_renew: 是否自动续订。 取值范围： - 0：表示不自动续订。 - 1：表示自动续订。
        :type is_auto_renew: int
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self.discriminator = None

        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew

    @property
    def period_type(self):
        """Gets the period_type of this PeriodOrderInfo.

        订购周期类型。 取值范围： - 2：表示周期类型为月。 - 3：表示周期类型为年。

        :return: The period_type of this PeriodOrderInfo.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PeriodOrderInfo.

        订购周期类型。 取值范围： - 2：表示周期类型为月。 - 3：表示周期类型为年。

        :param period_type: The period_type of this PeriodOrderInfo.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this PeriodOrderInfo.

        订购周期数。 取值范围： - period_type=2（周期类型为月）时，取值为[1，9]。 - period_type=3（周期类型为年）时，取值为[1，3]。

        :return: The period_num of this PeriodOrderInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PeriodOrderInfo.

        订购周期数。 取值范围： - period_type=2（周期类型为月）时，取值为[1，9]。 - period_type=3（周期类型为年）时，取值为[1，3]。

        :param period_num: The period_num of this PeriodOrderInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this PeriodOrderInfo.

        是否自动续订。 取值范围： - 0：表示不自动续订。 - 1：表示自动续订。

        :return: The is_auto_renew of this PeriodOrderInfo.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this PeriodOrderInfo.

        是否自动续订。 取值范围： - 0：表示不自动续订。 - 1：表示自动续订。

        :param is_auto_renew: The is_auto_renew of this PeriodOrderInfo.
        :type is_auto_renew: int
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
        if not isinstance(other, PeriodOrderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
