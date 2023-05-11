# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionStatsIntervals:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'str',
        'session_count': 'int',
        'user_count': 'int',
        'avg_request_count': 'float',
        'avg_session_time': 'float'
    }

    attribute_map = {
        'start': 'start',
        'session_count': 'session_count',
        'user_count': 'user_count',
        'avg_request_count': 'avg_request_count',
        'avg_session_time': 'avg_session_time'
    }

    def __init__(self, start=None, session_count=None, user_count=None, avg_request_count=None, avg_session_time=None):
        """SessionStatsIntervals

        The model defined in huaweicloud sdk

        :param start: 间隔周期开始时间。
        :type start: str
        :param session_count: 间隔周期会话总数。
        :type session_count: int
        :param user_count: 间隔周期独立用户个数。
        :type user_count: int
        :param avg_request_count: 间隔周期平均会话轮数，保留小数点后三位。
        :type avg_request_count: float
        :param avg_session_time: 间隔周期平均会话时长，保留小数点后三位。
        :type avg_session_time: float
        """
        
        

        self._start = None
        self._session_count = None
        self._user_count = None
        self._avg_request_count = None
        self._avg_session_time = None
        self.discriminator = None

        self.start = start
        self.session_count = session_count
        self.user_count = user_count
        self.avg_request_count = avg_request_count
        self.avg_session_time = avg_session_time

    @property
    def start(self):
        """Gets the start of this SessionStatsIntervals.

        间隔周期开始时间。

        :return: The start of this SessionStatsIntervals.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SessionStatsIntervals.

        间隔周期开始时间。

        :param start: The start of this SessionStatsIntervals.
        :type start: str
        """
        self._start = start

    @property
    def session_count(self):
        """Gets the session_count of this SessionStatsIntervals.

        间隔周期会话总数。

        :return: The session_count of this SessionStatsIntervals.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this SessionStatsIntervals.

        间隔周期会话总数。

        :param session_count: The session_count of this SessionStatsIntervals.
        :type session_count: int
        """
        self._session_count = session_count

    @property
    def user_count(self):
        """Gets the user_count of this SessionStatsIntervals.

        间隔周期独立用户个数。

        :return: The user_count of this SessionStatsIntervals.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this SessionStatsIntervals.

        间隔周期独立用户个数。

        :param user_count: The user_count of this SessionStatsIntervals.
        :type user_count: int
        """
        self._user_count = user_count

    @property
    def avg_request_count(self):
        """Gets the avg_request_count of this SessionStatsIntervals.

        间隔周期平均会话轮数，保留小数点后三位。

        :return: The avg_request_count of this SessionStatsIntervals.
        :rtype: float
        """
        return self._avg_request_count

    @avg_request_count.setter
    def avg_request_count(self, avg_request_count):
        """Sets the avg_request_count of this SessionStatsIntervals.

        间隔周期平均会话轮数，保留小数点后三位。

        :param avg_request_count: The avg_request_count of this SessionStatsIntervals.
        :type avg_request_count: float
        """
        self._avg_request_count = avg_request_count

    @property
    def avg_session_time(self):
        """Gets the avg_session_time of this SessionStatsIntervals.

        间隔周期平均会话时长，保留小数点后三位。

        :return: The avg_session_time of this SessionStatsIntervals.
        :rtype: float
        """
        return self._avg_session_time

    @avg_session_time.setter
    def avg_session_time(self, avg_session_time):
        """Sets the avg_session_time of this SessionStatsIntervals.

        间隔周期平均会话时长，保留小数点后三位。

        :param avg_session_time: The avg_session_time of this SessionStatsIntervals.
        :type avg_session_time: float
        """
        self._avg_session_time = avg_session_time

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
        if not isinstance(other, SessionStatsIntervals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
