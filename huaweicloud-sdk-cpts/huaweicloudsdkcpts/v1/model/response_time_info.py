# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseTimeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg_response_time': 'float',
        'avg_tp50': 'int',
        'avg_tp90': 'int',
        'max_response_time': 'int',
        'min_response_time': 'int'
    }

    attribute_map = {
        'avg_response_time': 'avg_response_time',
        'avg_tp50': 'avg_tp50',
        'avg_tp90': 'avg_tp90',
        'max_response_time': 'max_response_time',
        'min_response_time': 'min_response_time'
    }

    def __init__(self, avg_response_time=None, avg_tp50=None, avg_tp90=None, max_response_time=None, min_response_time=None):
        r"""ResponseTimeInfo

        The model defined in huaweicloud sdk

        :param avg_response_time: 平均响应时间
        :type avg_response_time: float
        :param avg_tp50: TP50
        :type avg_tp50: int
        :param avg_tp90: TP90
        :type avg_tp90: int
        :param max_response_time: 最大响应时间
        :type max_response_time: int
        :param min_response_time: 最小响应时间
        :type min_response_time: int
        """
        
        

        self._avg_response_time = None
        self._avg_tp50 = None
        self._avg_tp90 = None
        self._max_response_time = None
        self._min_response_time = None
        self.discriminator = None

        if avg_response_time is not None:
            self.avg_response_time = avg_response_time
        if avg_tp50 is not None:
            self.avg_tp50 = avg_tp50
        if avg_tp90 is not None:
            self.avg_tp90 = avg_tp90
        if max_response_time is not None:
            self.max_response_time = max_response_time
        if min_response_time is not None:
            self.min_response_time = min_response_time

    @property
    def avg_response_time(self):
        r"""Gets the avg_response_time of this ResponseTimeInfo.

        平均响应时间

        :return: The avg_response_time of this ResponseTimeInfo.
        :rtype: float
        """
        return self._avg_response_time

    @avg_response_time.setter
    def avg_response_time(self, avg_response_time):
        r"""Sets the avg_response_time of this ResponseTimeInfo.

        平均响应时间

        :param avg_response_time: The avg_response_time of this ResponseTimeInfo.
        :type avg_response_time: float
        """
        self._avg_response_time = avg_response_time

    @property
    def avg_tp50(self):
        r"""Gets the avg_tp50 of this ResponseTimeInfo.

        TP50

        :return: The avg_tp50 of this ResponseTimeInfo.
        :rtype: int
        """
        return self._avg_tp50

    @avg_tp50.setter
    def avg_tp50(self, avg_tp50):
        r"""Sets the avg_tp50 of this ResponseTimeInfo.

        TP50

        :param avg_tp50: The avg_tp50 of this ResponseTimeInfo.
        :type avg_tp50: int
        """
        self._avg_tp50 = avg_tp50

    @property
    def avg_tp90(self):
        r"""Gets the avg_tp90 of this ResponseTimeInfo.

        TP90

        :return: The avg_tp90 of this ResponseTimeInfo.
        :rtype: int
        """
        return self._avg_tp90

    @avg_tp90.setter
    def avg_tp90(self, avg_tp90):
        r"""Sets the avg_tp90 of this ResponseTimeInfo.

        TP90

        :param avg_tp90: The avg_tp90 of this ResponseTimeInfo.
        :type avg_tp90: int
        """
        self._avg_tp90 = avg_tp90

    @property
    def max_response_time(self):
        r"""Gets the max_response_time of this ResponseTimeInfo.

        最大响应时间

        :return: The max_response_time of this ResponseTimeInfo.
        :rtype: int
        """
        return self._max_response_time

    @max_response_time.setter
    def max_response_time(self, max_response_time):
        r"""Sets the max_response_time of this ResponseTimeInfo.

        最大响应时间

        :param max_response_time: The max_response_time of this ResponseTimeInfo.
        :type max_response_time: int
        """
        self._max_response_time = max_response_time

    @property
    def min_response_time(self):
        r"""Gets the min_response_time of this ResponseTimeInfo.

        最小响应时间

        :return: The min_response_time of this ResponseTimeInfo.
        :rtype: int
        """
        return self._min_response_time

    @min_response_time.setter
    def min_response_time(self, min_response_time):
        r"""Sets the min_response_time of this ResponseTimeInfo.

        最小响应时间

        :param min_response_time: The min_response_time of this ResponseTimeInfo.
        :type min_response_time: int
        """
        self._min_response_time = min_response_time

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
        if not isinstance(other, ResponseTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
