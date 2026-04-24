# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodObject:

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
        'period_time': 'str'
    }

    attribute_map = {
        'period_num': 'period_num',
        'period_time': 'period_time'
    }

    def __init__(self, period_num=None, period_time=None):
        r"""PeriodObject

        The model defined in huaweicloud sdk

        :param period_num: 周期，取值为1到24。
        :type period_num: int
        :param period_time: 小时:分钟，样例：00:59
        :type period_time: str
        """
        
        

        self._period_num = None
        self._period_time = None
        self.discriminator = None

        self.period_num = period_num
        self.period_time = period_time

    @property
    def period_num(self):
        r"""Gets the period_num of this PeriodObject.

        周期，取值为1到24。

        :return: The period_num of this PeriodObject.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PeriodObject.

        周期，取值为1到24。

        :param period_num: The period_num of this PeriodObject.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_time(self):
        r"""Gets the period_time of this PeriodObject.

        小时:分钟，样例：00:59

        :return: The period_time of this PeriodObject.
        :rtype: str
        """
        return self._period_time

    @period_time.setter
    def period_time(self, period_time):
        r"""Sets the period_time of this PeriodObject.

        小时:分钟，样例：00:59

        :param period_time: The period_time of this PeriodObject.
        :type period_time: str
        """
        self._period_time = period_time

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
        if not isinstance(other, PeriodObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
