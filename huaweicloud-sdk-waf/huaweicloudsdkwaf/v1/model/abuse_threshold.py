# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbuseThreshold:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_window_seconds': 'int',
        'conditions': 'list[AbuseCondition]'
    }

    attribute_map = {
        'time_window_seconds': 'time_window_seconds',
        'conditions': 'conditions'
    }

    def __init__(self, time_window_seconds=None, conditions=None):
        r"""AbuseThreshold

        The model defined in huaweicloud sdk

        :param time_window_seconds: 统计时间窗口（秒），最大86400（1天）
        :type time_window_seconds: int
        :param conditions: 阈值条件列表，当前仅支持1个条件
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AbuseCondition`]
        """
        
        

        self._time_window_seconds = None
        self._conditions = None
        self.discriminator = None

        if time_window_seconds is not None:
            self.time_window_seconds = time_window_seconds
        if conditions is not None:
            self.conditions = conditions

    @property
    def time_window_seconds(self):
        r"""Gets the time_window_seconds of this AbuseThreshold.

        统计时间窗口（秒），最大86400（1天）

        :return: The time_window_seconds of this AbuseThreshold.
        :rtype: int
        """
        return self._time_window_seconds

    @time_window_seconds.setter
    def time_window_seconds(self, time_window_seconds):
        r"""Sets the time_window_seconds of this AbuseThreshold.

        统计时间窗口（秒），最大86400（1天）

        :param time_window_seconds: The time_window_seconds of this AbuseThreshold.
        :type time_window_seconds: int
        """
        self._time_window_seconds = time_window_seconds

    @property
    def conditions(self):
        r"""Gets the conditions of this AbuseThreshold.

        阈值条件列表，当前仅支持1个条件

        :return: The conditions of this AbuseThreshold.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AbuseCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this AbuseThreshold.

        阈值条件列表，当前仅支持1个条件

        :param conditions: The conditions of this AbuseThreshold.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AbuseCondition`]
        """
        self._conditions = conditions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AbuseThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
