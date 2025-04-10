# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleTimerType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'repeat_interval': 'int',
        'repeat_count': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'repeat_interval': 'repeat_interval',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, start_time=None, repeat_interval=None, repeat_count=None):
        r"""SimpleTimerType

        The model defined in huaweicloud sdk

        :param start_time: **参数说明**：规则触发的开始时间，使用UTC时区，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;。
        :type start_time: str
        :param repeat_interval: **参数说明**：规则触发的重复时间间隔，单位为秒。
        :type repeat_interval: int
        :param repeat_count: **参数说明**：规则触发的重复次数。
        :type repeat_count: int
        """
        
        

        self._start_time = None
        self._repeat_interval = None
        self._repeat_count = None
        self.discriminator = None

        self.start_time = start_time
        self.repeat_interval = repeat_interval
        self.repeat_count = repeat_count

    @property
    def start_time(self):
        r"""Gets the start_time of this SimpleTimerType.

        **参数说明**：规则触发的开始时间，使用UTC时区，格式：yyyyMMdd'T'HHmmss'Z'。

        :return: The start_time of this SimpleTimerType.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SimpleTimerType.

        **参数说明**：规则触发的开始时间，使用UTC时区，格式：yyyyMMdd'T'HHmmss'Z'。

        :param start_time: The start_time of this SimpleTimerType.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def repeat_interval(self):
        r"""Gets the repeat_interval of this SimpleTimerType.

        **参数说明**：规则触发的重复时间间隔，单位为秒。

        :return: The repeat_interval of this SimpleTimerType.
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        r"""Sets the repeat_interval of this SimpleTimerType.

        **参数说明**：规则触发的重复时间间隔，单位为秒。

        :param repeat_interval: The repeat_interval of this SimpleTimerType.
        :type repeat_interval: int
        """
        self._repeat_interval = repeat_interval

    @property
    def repeat_count(self):
        r"""Gets the repeat_count of this SimpleTimerType.

        **参数说明**：规则触发的重复次数。

        :return: The repeat_count of this SimpleTimerType.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        r"""Sets the repeat_count of this SimpleTimerType.

        **参数说明**：规则触发的重复次数。

        :param repeat_count: The repeat_count of this SimpleTimerType.
        :type repeat_count: int
        """
        self._repeat_count = repeat_count

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
        if not isinstance(other, SimpleTimerType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
