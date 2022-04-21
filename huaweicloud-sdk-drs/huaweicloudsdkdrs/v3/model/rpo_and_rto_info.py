# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RpoAndRtoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'check_point': 'str',
        'delay': 'str',
        'gtid_set': 'str',
        'time': 'str'
    }

    attribute_map = {
        'check_point': 'check_point',
        'delay': 'delay',
        'gtid_set': 'gtid_set',
        'time': 'time'
    }

    def __init__(self, check_point=None, delay=None, gtid_set=None, time=None):
        """RpoAndRtoInfo

        The model defined in huaweicloud sdk

        :param check_point: 检查点
        :type check_point: str
        :param delay: 延迟
        :type delay: str
        :param gtid_set: gtid集合
        :type gtid_set: str
        :param time: 当前时间 ，格式为“yyyy-MM-dd HH:mm:ss”
        :type time: str
        """
        
        

        self._check_point = None
        self._delay = None
        self._gtid_set = None
        self._time = None
        self.discriminator = None

        if check_point is not None:
            self.check_point = check_point
        if delay is not None:
            self.delay = delay
        if gtid_set is not None:
            self.gtid_set = gtid_set
        if time is not None:
            self.time = time

    @property
    def check_point(self):
        """Gets the check_point of this RpoAndRtoInfo.

        检查点

        :return: The check_point of this RpoAndRtoInfo.
        :rtype: str
        """
        return self._check_point

    @check_point.setter
    def check_point(self, check_point):
        """Sets the check_point of this RpoAndRtoInfo.

        检查点

        :param check_point: The check_point of this RpoAndRtoInfo.
        :type check_point: str
        """
        self._check_point = check_point

    @property
    def delay(self):
        """Gets the delay of this RpoAndRtoInfo.

        延迟

        :return: The delay of this RpoAndRtoInfo.
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this RpoAndRtoInfo.

        延迟

        :param delay: The delay of this RpoAndRtoInfo.
        :type delay: str
        """
        self._delay = delay

    @property
    def gtid_set(self):
        """Gets the gtid_set of this RpoAndRtoInfo.

        gtid集合

        :return: The gtid_set of this RpoAndRtoInfo.
        :rtype: str
        """
        return self._gtid_set

    @gtid_set.setter
    def gtid_set(self, gtid_set):
        """Sets the gtid_set of this RpoAndRtoInfo.

        gtid集合

        :param gtid_set: The gtid_set of this RpoAndRtoInfo.
        :type gtid_set: str
        """
        self._gtid_set = gtid_set

    @property
    def time(self):
        """Gets the time of this RpoAndRtoInfo.

        当前时间 ，格式为“yyyy-MM-dd HH:mm:ss”

        :return: The time of this RpoAndRtoInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RpoAndRtoInfo.

        当前时间 ，格式为“yyyy-MM-dd HH:mm:ss”

        :param time: The time of this RpoAndRtoInfo.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, RpoAndRtoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
