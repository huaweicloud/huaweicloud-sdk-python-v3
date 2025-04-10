# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartTimeInfo:

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
        'frequency': 'str',
        'mode': 'str',
        'day_time_frame': 'list[TimeFrame]',
        'single_time_frame': 'list[TimeFrame]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'frequency': 'frequency',
        'mode': 'mode',
        'day_time_frame': 'day_time_frame',
        'single_time_frame': 'single_time_frame'
    }

    def __init__(self, start_time=None, frequency=None, mode=None, day_time_frame=None, single_time_frame=None):
        r"""StartTimeInfo

        The model defined in huaweicloud sdk

        :param start_time: 任务启动时间
        :type start_time: str
        :param frequency: 任务运行频率（定时任务频率，每天运行还是单次运行）
        :type frequency: str
        :param mode: 任务运行模式（按时间段运行还是按频率运行）
        :type mode: str
        :param day_time_frame: 每天运行时间段
        :type day_time_frame: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        :param single_time_frame: 每次运行时间段
        :type single_time_frame: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        """
        
        

        self._start_time = None
        self._frequency = None
        self._mode = None
        self._day_time_frame = None
        self._single_time_frame = None
        self.discriminator = None

        self.start_time = start_time
        if frequency is not None:
            self.frequency = frequency
        if mode is not None:
            self.mode = mode
        if day_time_frame is not None:
            self.day_time_frame = day_time_frame
        if single_time_frame is not None:
            self.single_time_frame = single_time_frame

    @property
    def start_time(self):
        r"""Gets the start_time of this StartTimeInfo.

        任务启动时间

        :return: The start_time of this StartTimeInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StartTimeInfo.

        任务启动时间

        :param start_time: The start_time of this StartTimeInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def frequency(self):
        r"""Gets the frequency of this StartTimeInfo.

        任务运行频率（定时任务频率，每天运行还是单次运行）

        :return: The frequency of this StartTimeInfo.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this StartTimeInfo.

        任务运行频率（定时任务频率，每天运行还是单次运行）

        :param frequency: The frequency of this StartTimeInfo.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def mode(self):
        r"""Gets the mode of this StartTimeInfo.

        任务运行模式（按时间段运行还是按频率运行）

        :return: The mode of this StartTimeInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this StartTimeInfo.

        任务运行模式（按时间段运行还是按频率运行）

        :param mode: The mode of this StartTimeInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def day_time_frame(self):
        r"""Gets the day_time_frame of this StartTimeInfo.

        每天运行时间段

        :return: The day_time_frame of this StartTimeInfo.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        """
        return self._day_time_frame

    @day_time_frame.setter
    def day_time_frame(self, day_time_frame):
        r"""Sets the day_time_frame of this StartTimeInfo.

        每天运行时间段

        :param day_time_frame: The day_time_frame of this StartTimeInfo.
        :type day_time_frame: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        """
        self._day_time_frame = day_time_frame

    @property
    def single_time_frame(self):
        r"""Gets the single_time_frame of this StartTimeInfo.

        每次运行时间段

        :return: The single_time_frame of this StartTimeInfo.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        """
        return self._single_time_frame

    @single_time_frame.setter
    def single_time_frame(self, single_time_frame):
        r"""Sets the single_time_frame of this StartTimeInfo.

        每次运行时间段

        :param single_time_frame: The single_time_frame of this StartTimeInfo.
        :type single_time_frame: list[:class:`huaweicloudsdkhilens.v3.TimeFrame`]
        """
        self._single_time_frame = single_time_frame

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
        if not isinstance(other, StartTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
