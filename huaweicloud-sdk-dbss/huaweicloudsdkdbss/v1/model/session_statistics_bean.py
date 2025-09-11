# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_session_num': 'int',
        'fail_session_num': 'int',
        'new_session_num': 'int',
        'period': 'str'
    }

    attribute_map = {
        'active_session_num': 'active_session_num',
        'fail_session_num': 'fail_session_num',
        'new_session_num': 'new_session_num',
        'period': 'period'
    }

    def __init__(self, active_session_num=None, fail_session_num=None, new_session_num=None, period=None):
        r"""SessionStatisticsBean

        The model defined in huaweicloud sdk

        :param active_session_num: 活跃SESSION数量
        :type active_session_num: int
        :param fail_session_num: 失败SESSION数量
        :type fail_session_num: int
        :param new_session_num: 新增SESSION数量
        :type new_session_num: int
        :param period: 周期
        :type period: str
        """
        
        

        self._active_session_num = None
        self._fail_session_num = None
        self._new_session_num = None
        self._period = None
        self.discriminator = None

        if active_session_num is not None:
            self.active_session_num = active_session_num
        if fail_session_num is not None:
            self.fail_session_num = fail_session_num
        if new_session_num is not None:
            self.new_session_num = new_session_num
        if period is not None:
            self.period = period

    @property
    def active_session_num(self):
        r"""Gets the active_session_num of this SessionStatisticsBean.

        活跃SESSION数量

        :return: The active_session_num of this SessionStatisticsBean.
        :rtype: int
        """
        return self._active_session_num

    @active_session_num.setter
    def active_session_num(self, active_session_num):
        r"""Sets the active_session_num of this SessionStatisticsBean.

        活跃SESSION数量

        :param active_session_num: The active_session_num of this SessionStatisticsBean.
        :type active_session_num: int
        """
        self._active_session_num = active_session_num

    @property
    def fail_session_num(self):
        r"""Gets the fail_session_num of this SessionStatisticsBean.

        失败SESSION数量

        :return: The fail_session_num of this SessionStatisticsBean.
        :rtype: int
        """
        return self._fail_session_num

    @fail_session_num.setter
    def fail_session_num(self, fail_session_num):
        r"""Sets the fail_session_num of this SessionStatisticsBean.

        失败SESSION数量

        :param fail_session_num: The fail_session_num of this SessionStatisticsBean.
        :type fail_session_num: int
        """
        self._fail_session_num = fail_session_num

    @property
    def new_session_num(self):
        r"""Gets the new_session_num of this SessionStatisticsBean.

        新增SESSION数量

        :return: The new_session_num of this SessionStatisticsBean.
        :rtype: int
        """
        return self._new_session_num

    @new_session_num.setter
    def new_session_num(self, new_session_num):
        r"""Sets the new_session_num of this SessionStatisticsBean.

        新增SESSION数量

        :param new_session_num: The new_session_num of this SessionStatisticsBean.
        :type new_session_num: int
        """
        self._new_session_num = new_session_num

    @property
    def period(self):
        r"""Gets the period of this SessionStatisticsBean.

        周期

        :return: The period of this SessionStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SessionStatisticsBean.

        周期

        :param period: The period of this SessionStatisticsBean.
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
        if not isinstance(other, SessionStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
