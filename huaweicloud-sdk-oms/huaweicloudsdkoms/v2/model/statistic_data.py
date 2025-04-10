# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_stamp': 'int',
        'statistic_num': 'int'
    }

    attribute_map = {
        'time_stamp': 'time_stamp',
        'statistic_num': 'statistic_num'
    }

    def __init__(self, time_stamp=None, statistic_num=None):
        r"""StatisticData

        The model defined in huaweicloud sdk

        :param time_stamp: 统计时间戳
        :type time_stamp: int
        :param statistic_num: 统计数量
        :type statistic_num: int
        """
        
        

        self._time_stamp = None
        self._statistic_num = None
        self.discriminator = None

        if time_stamp is not None:
            self.time_stamp = time_stamp
        if statistic_num is not None:
            self.statistic_num = statistic_num

    @property
    def time_stamp(self):
        r"""Gets the time_stamp of this StatisticData.

        统计时间戳

        :return: The time_stamp of this StatisticData.
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        r"""Sets the time_stamp of this StatisticData.

        统计时间戳

        :param time_stamp: The time_stamp of this StatisticData.
        :type time_stamp: int
        """
        self._time_stamp = time_stamp

    @property
    def statistic_num(self):
        r"""Gets the statistic_num of this StatisticData.

        统计数量

        :return: The statistic_num of this StatisticData.
        :rtype: int
        """
        return self._statistic_num

    @statistic_num.setter
    def statistic_num(self, statistic_num):
        r"""Sets the statistic_num of this StatisticData.

        统计数量

        :param statistic_num: The statistic_num of this StatisticData.
        :type statistic_num: int
        """
        self._statistic_num = statistic_num

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
        if not isinstance(other, StatisticData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
