# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'sql_num': 'int'
    }

    attribute_map = {
        'period': 'period',
        'sql_num': 'sql_num'
    }

    def __init__(self, period=None, sql_num=None):
        r"""CountStatisticsBean

        The model defined in huaweicloud sdk

        :param period: 周期
        :type period: str
        :param sql_num: SQL数量
        :type sql_num: int
        """
        
        

        self._period = None
        self._sql_num = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if sql_num is not None:
            self.sql_num = sql_num

    @property
    def period(self):
        r"""Gets the period of this CountStatisticsBean.

        周期

        :return: The period of this CountStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this CountStatisticsBean.

        周期

        :param period: The period of this CountStatisticsBean.
        :type period: str
        """
        self._period = period

    @property
    def sql_num(self):
        r"""Gets the sql_num of this CountStatisticsBean.

        SQL数量

        :return: The sql_num of this CountStatisticsBean.
        :rtype: int
        """
        return self._sql_num

    @sql_num.setter
    def sql_num(self, sql_num):
        r"""Sets the sql_num of this CountStatisticsBean.

        SQL数量

        :param sql_num: The sql_num of this CountStatisticsBean.
        :type sql_num: int
        """
        self._sql_num = sql_num

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
        if not isinstance(other, CountStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
