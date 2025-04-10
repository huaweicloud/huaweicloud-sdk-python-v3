# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpeedLimitlJson:

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
        'end': 'str',
        'speed': 'int',
        'over_speed_threshold': 'float'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'speed': 'speed',
        'over_speed_threshold': 'over_speed_threshold'
    }

    def __init__(self, start=None, end=None, speed=None, over_speed_threshold=None):
        r"""SpeedLimitlJson

        The model defined in huaweicloud sdk

        :param start: 时间段开始时间，格式：XX:XX。
        :type start: str
        :param end: 时间段结束时间，格式：XX:XX。
        :type end: str
        :param speed: 时间段的速率，0-1000的整数，单位：Mbit/s。
        :type speed: int
        :param over_speed_threshold: 停止迁移的超速阈值。 是一个迁移速率的保护机制，超出该阈值会停止任务。它主要用于控制迁移过程中资源（特别是网络带宽）的消耗，确保系统的整体性能不受单一迁移任务影响 单位是百分比
        :type over_speed_threshold: float
        """
        
        

        self._start = None
        self._end = None
        self._speed = None
        self._over_speed_threshold = None
        self.discriminator = None

        self.start = start
        self.end = end
        self.speed = speed
        if over_speed_threshold is not None:
            self.over_speed_threshold = over_speed_threshold

    @property
    def start(self):
        r"""Gets the start of this SpeedLimitlJson.

        时间段开始时间，格式：XX:XX。

        :return: The start of this SpeedLimitlJson.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this SpeedLimitlJson.

        时间段开始时间，格式：XX:XX。

        :param start: The start of this SpeedLimitlJson.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this SpeedLimitlJson.

        时间段结束时间，格式：XX:XX。

        :return: The end of this SpeedLimitlJson.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this SpeedLimitlJson.

        时间段结束时间，格式：XX:XX。

        :param end: The end of this SpeedLimitlJson.
        :type end: str
        """
        self._end = end

    @property
    def speed(self):
        r"""Gets the speed of this SpeedLimitlJson.

        时间段的速率，0-1000的整数，单位：Mbit/s。

        :return: The speed of this SpeedLimitlJson.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this SpeedLimitlJson.

        时间段的速率，0-1000的整数，单位：Mbit/s。

        :param speed: The speed of this SpeedLimitlJson.
        :type speed: int
        """
        self._speed = speed

    @property
    def over_speed_threshold(self):
        r"""Gets the over_speed_threshold of this SpeedLimitlJson.

        停止迁移的超速阈值。 是一个迁移速率的保护机制，超出该阈值会停止任务。它主要用于控制迁移过程中资源（特别是网络带宽）的消耗，确保系统的整体性能不受单一迁移任务影响 单位是百分比

        :return: The over_speed_threshold of this SpeedLimitlJson.
        :rtype: float
        """
        return self._over_speed_threshold

    @over_speed_threshold.setter
    def over_speed_threshold(self, over_speed_threshold):
        r"""Sets the over_speed_threshold of this SpeedLimitlJson.

        停止迁移的超速阈值。 是一个迁移速率的保护机制，超出该阈值会停止任务。它主要用于控制迁移过程中资源（特别是网络带宽）的消耗，确保系统的整体性能不受单一迁移任务影响 单位是百分比

        :param over_speed_threshold: The over_speed_threshold of this SpeedLimitlJson.
        :type over_speed_threshold: float
        """
        self._over_speed_threshold = over_speed_threshold

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
        if not isinstance(other, SpeedLimitlJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
