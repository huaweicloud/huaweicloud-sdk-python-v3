# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoutePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_session': 'int',
        'cpu_threshold': 'int',
        'mem_threshold': 'int'
    }

    attribute_map = {
        'max_session': 'max_session',
        'cpu_threshold': 'cpu_threshold',
        'mem_threshold': 'mem_threshold'
    }

    def __init__(self, max_session=None, cpu_threshold=None, mem_threshold=None):
        """RoutePolicy

        The model defined in huaweicloud sdk

        :param max_session: 单台服务器最大的链接会话数
        :type max_session: int
        :param cpu_threshold: cpu使用率阈值，单位为%
        :type cpu_threshold: int
        :param mem_threshold: 内存使用率阈值，单位为%
        :type mem_threshold: int
        """
        
        

        self._max_session = None
        self._cpu_threshold = None
        self._mem_threshold = None
        self.discriminator = None

        if max_session is not None:
            self.max_session = max_session
        if cpu_threshold is not None:
            self.cpu_threshold = cpu_threshold
        if mem_threshold is not None:
            self.mem_threshold = mem_threshold

    @property
    def max_session(self):
        """Gets the max_session of this RoutePolicy.

        单台服务器最大的链接会话数

        :return: The max_session of this RoutePolicy.
        :rtype: int
        """
        return self._max_session

    @max_session.setter
    def max_session(self, max_session):
        """Sets the max_session of this RoutePolicy.

        单台服务器最大的链接会话数

        :param max_session: The max_session of this RoutePolicy.
        :type max_session: int
        """
        self._max_session = max_session

    @property
    def cpu_threshold(self):
        """Gets the cpu_threshold of this RoutePolicy.

        cpu使用率阈值，单位为%

        :return: The cpu_threshold of this RoutePolicy.
        :rtype: int
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, cpu_threshold):
        """Sets the cpu_threshold of this RoutePolicy.

        cpu使用率阈值，单位为%

        :param cpu_threshold: The cpu_threshold of this RoutePolicy.
        :type cpu_threshold: int
        """
        self._cpu_threshold = cpu_threshold

    @property
    def mem_threshold(self):
        """Gets the mem_threshold of this RoutePolicy.

        内存使用率阈值，单位为%

        :return: The mem_threshold of this RoutePolicy.
        :rtype: int
        """
        return self._mem_threshold

    @mem_threshold.setter
    def mem_threshold(self, mem_threshold):
        """Sets the mem_threshold of this RoutePolicy.

        内存使用率阈值，单位为%

        :param mem_threshold: The mem_threshold of this RoutePolicy.
        :type mem_threshold: int
        """
        self._mem_threshold = mem_threshold

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
        if not isinstance(other, RoutePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
