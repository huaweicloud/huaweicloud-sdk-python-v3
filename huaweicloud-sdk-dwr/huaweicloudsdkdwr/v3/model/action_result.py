# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match': 'str',
        'retry_interval': 'int',
        'max_retry': 'int',
        'next_state': 'str',
        'is_terminal': 'bool'
    }

    attribute_map = {
        'match': 'match',
        'retry_interval': 'retry_interval',
        'max_retry': 'max_retry',
        'next_state': 'next_state',
        'is_terminal': 'is_terminal'
    }

    def __init__(self, match=None, retry_interval=None, max_retry=None, next_state=None, is_terminal=None):
        """ActionResult

        The model defined in huaweicloud sdk

        :param match: 触发错误处理需符合的条件
        :type match: str
        :param retry_interval: 每次重试间隔时间
        :type retry_interval: int
        :param max_retry: 最多重试次数
        :type max_retry: int
        :param next_state: 下一个状态
        :type next_state: str
        :param is_terminal: 是否为结束状态
        :type is_terminal: bool
        """
        
        

        self._match = None
        self._retry_interval = None
        self._max_retry = None
        self._next_state = None
        self._is_terminal = None
        self.discriminator = None

        self.match = match
        self.retry_interval = retry_interval
        if max_retry is not None:
            self.max_retry = max_retry
        self.next_state = next_state
        if is_terminal is not None:
            self.is_terminal = is_terminal

    @property
    def match(self):
        """Gets the match of this ActionResult.

        触发错误处理需符合的条件

        :return: The match of this ActionResult.
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this ActionResult.

        触发错误处理需符合的条件

        :param match: The match of this ActionResult.
        :type match: str
        """
        self._match = match

    @property
    def retry_interval(self):
        """Gets the retry_interval of this ActionResult.

        每次重试间隔时间

        :return: The retry_interval of this ActionResult.
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this ActionResult.

        每次重试间隔时间

        :param retry_interval: The retry_interval of this ActionResult.
        :type retry_interval: int
        """
        self._retry_interval = retry_interval

    @property
    def max_retry(self):
        """Gets the max_retry of this ActionResult.

        最多重试次数

        :return: The max_retry of this ActionResult.
        :rtype: int
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, max_retry):
        """Sets the max_retry of this ActionResult.

        最多重试次数

        :param max_retry: The max_retry of this ActionResult.
        :type max_retry: int
        """
        self._max_retry = max_retry

    @property
    def next_state(self):
        """Gets the next_state of this ActionResult.

        下一个状态

        :return: The next_state of this ActionResult.
        :rtype: str
        """
        return self._next_state

    @next_state.setter
    def next_state(self, next_state):
        """Sets the next_state of this ActionResult.

        下一个状态

        :param next_state: The next_state of this ActionResult.
        :type next_state: str
        """
        self._next_state = next_state

    @property
    def is_terminal(self):
        """Gets the is_terminal of this ActionResult.

        是否为结束状态

        :return: The is_terminal of this ActionResult.
        :rtype: bool
        """
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(self, is_terminal):
        """Sets the is_terminal of this ActionResult.

        是否为结束状态

        :param is_terminal: The is_terminal of this ActionResult.
        :type is_terminal: bool
        """
        self._is_terminal = is_terminal

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
        if not isinstance(other, ActionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
