# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayShardStaticsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'total': 'int',
        'finish': 'int',
        'abnormal': 'int',
        'slow': 'int'
    }

    attribute_map = {
        'time': 'time',
        'total': 'total',
        'finish': 'finish',
        'abnormal': 'abnormal',
        'slow': 'slow'
    }

    def __init__(self, time=None, total=None, finish=None, abnormal=None, slow=None):
        r"""ReplayShardStaticsResp

        The model defined in huaweicloud sdk

        :param time: 回放时间点
        :type time: str
        :param total: SQL总量
        :type total: int
        :param finish: SQL执行量
        :type finish: int
        :param abnormal: SQL异常量
        :type abnormal: int
        :param slow: 慢SQL数量
        :type slow: int
        """
        
        

        self._time = None
        self._total = None
        self._finish = None
        self._abnormal = None
        self._slow = None
        self.discriminator = None

        self.time = time
        self.total = total
        self.finish = finish
        self.abnormal = abnormal
        self.slow = slow

    @property
    def time(self):
        r"""Gets the time of this ReplayShardStaticsResp.

        回放时间点

        :return: The time of this ReplayShardStaticsResp.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ReplayShardStaticsResp.

        回放时间点

        :param time: The time of this ReplayShardStaticsResp.
        :type time: str
        """
        self._time = time

    @property
    def total(self):
        r"""Gets the total of this ReplayShardStaticsResp.

        SQL总量

        :return: The total of this ReplayShardStaticsResp.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ReplayShardStaticsResp.

        SQL总量

        :param total: The total of this ReplayShardStaticsResp.
        :type total: int
        """
        self._total = total

    @property
    def finish(self):
        r"""Gets the finish of this ReplayShardStaticsResp.

        SQL执行量

        :return: The finish of this ReplayShardStaticsResp.
        :rtype: int
        """
        return self._finish

    @finish.setter
    def finish(self, finish):
        r"""Sets the finish of this ReplayShardStaticsResp.

        SQL执行量

        :param finish: The finish of this ReplayShardStaticsResp.
        :type finish: int
        """
        self._finish = finish

    @property
    def abnormal(self):
        r"""Gets the abnormal of this ReplayShardStaticsResp.

        SQL异常量

        :return: The abnormal of this ReplayShardStaticsResp.
        :rtype: int
        """
        return self._abnormal

    @abnormal.setter
    def abnormal(self, abnormal):
        r"""Sets the abnormal of this ReplayShardStaticsResp.

        SQL异常量

        :param abnormal: The abnormal of this ReplayShardStaticsResp.
        :type abnormal: int
        """
        self._abnormal = abnormal

    @property
    def slow(self):
        r"""Gets the slow of this ReplayShardStaticsResp.

        慢SQL数量

        :return: The slow of this ReplayShardStaticsResp.
        :rtype: int
        """
        return self._slow

    @slow.setter
    def slow(self, slow):
        r"""Sets the slow of this ReplayShardStaticsResp.

        慢SQL数量

        :param slow: The slow of this ReplayShardStaticsResp.
        :type slow: int
        """
        self._slow = slow

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
        if not isinstance(other, ReplayShardStaticsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
