# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopSlowLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'x_language': 'str',
        'start_at': 'int',
        'end_at': 'int'
    }

    attribute_map = {
        'num': 'num',
        'x_language': 'X-Language',
        'start_at': 'start_at',
        'end_at': 'end_at'
    }

    def __init__(self, num=None, x_language=None, start_at=None, end_at=None):
        r"""ListTopSlowLogRequest

        The model defined in huaweicloud sdk

        :param num: TOP数量
        :type num: int
        :param x_language: 语言
        :type x_language: str
        :param start_at: 开始时间
        :type start_at: int
        :param end_at: 结束时间
        :type end_at: int
        """
        
        

        self._num = None
        self._x_language = None
        self._start_at = None
        self._end_at = None
        self.discriminator = None

        self.num = num
        if x_language is not None:
            self.x_language = x_language
        self.start_at = start_at
        self.end_at = end_at

    @property
    def num(self):
        r"""Gets the num of this ListTopSlowLogRequest.

        TOP数量

        :return: The num of this ListTopSlowLogRequest.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this ListTopSlowLogRequest.

        TOP数量

        :param num: The num of this ListTopSlowLogRequest.
        :type num: int
        """
        self._num = num

    @property
    def x_language(self):
        r"""Gets the x_language of this ListTopSlowLogRequest.

        语言

        :return: The x_language of this ListTopSlowLogRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListTopSlowLogRequest.

        语言

        :param x_language: The x_language of this ListTopSlowLogRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_at(self):
        r"""Gets the start_at of this ListTopSlowLogRequest.

        开始时间

        :return: The start_at of this ListTopSlowLogRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListTopSlowLogRequest.

        开始时间

        :param start_at: The start_at of this ListTopSlowLogRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListTopSlowLogRequest.

        结束时间

        :return: The end_at of this ListTopSlowLogRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListTopSlowLogRequest.

        结束时间

        :param end_at: The end_at of this ListTopSlowLogRequest.
        :type end_at: int
        """
        self._end_at = end_at

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
        if not isinstance(other, ListTopSlowLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
