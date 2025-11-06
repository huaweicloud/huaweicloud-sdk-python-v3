# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScheduleDailyFrequencyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'freq_subday_type': 'str',
        'active_start_time': 'str',
        'active_end_time': 'str',
        'freq_subday_interval': 'int',
        'freq_interval_unit': 'str'
    }

    attribute_map = {
        'freq_subday_type': 'freq_subday_type',
        'active_start_time': 'active_start_time',
        'active_end_time': 'active_end_time',
        'freq_subday_interval': 'freq_subday_interval',
        'freq_interval_unit': 'freq_interval_unit'
    }

    def __init__(self, freq_subday_type=None, active_start_time=None, active_end_time=None, freq_subday_interval=None, freq_interval_unit=None):
        r"""JobScheduleDailyFrequencyInfo

        The model defined in huaweicloud sdk

        :param freq_subday_type: 每日频率类型 once:每日一次, multiple:每日多次。
        :type freq_subday_type: str
        :param active_start_time: 每日第一次执行时间。每日频率类型为每日一次时，则只执行这一次。 HH:mm:ss
        :type active_start_time: str
        :param active_end_time: 最后一次执行时间。每日执行多次时该参数必传，每日执行一次时不生效。 HH:mm:ss
        :type active_end_time: str
        :param freq_subday_interval: 执行间隔。每日执行多次时该参数必传，每日执行一次时不生效。取值范围1至99
        :type freq_subday_interval: int
        :param freq_interval_unit: 执行间隔的单位。每日执行多次时该参数必传，每日执行一次时不生效。 second:秒, minute:分, hour:时
        :type freq_interval_unit: str
        """
        
        

        self._freq_subday_type = None
        self._active_start_time = None
        self._active_end_time = None
        self._freq_subday_interval = None
        self._freq_interval_unit = None
        self.discriminator = None

        if freq_subday_type is not None:
            self.freq_subday_type = freq_subday_type
        if active_start_time is not None:
            self.active_start_time = active_start_time
        if active_end_time is not None:
            self.active_end_time = active_end_time
        if freq_subday_interval is not None:
            self.freq_subday_interval = freq_subday_interval
        if freq_interval_unit is not None:
            self.freq_interval_unit = freq_interval_unit

    @property
    def freq_subday_type(self):
        r"""Gets the freq_subday_type of this JobScheduleDailyFrequencyInfo.

        每日频率类型 once:每日一次, multiple:每日多次。

        :return: The freq_subday_type of this JobScheduleDailyFrequencyInfo.
        :rtype: str
        """
        return self._freq_subday_type

    @freq_subday_type.setter
    def freq_subday_type(self, freq_subday_type):
        r"""Sets the freq_subday_type of this JobScheduleDailyFrequencyInfo.

        每日频率类型 once:每日一次, multiple:每日多次。

        :param freq_subday_type: The freq_subday_type of this JobScheduleDailyFrequencyInfo.
        :type freq_subday_type: str
        """
        self._freq_subday_type = freq_subday_type

    @property
    def active_start_time(self):
        r"""Gets the active_start_time of this JobScheduleDailyFrequencyInfo.

        每日第一次执行时间。每日频率类型为每日一次时，则只执行这一次。 HH:mm:ss

        :return: The active_start_time of this JobScheduleDailyFrequencyInfo.
        :rtype: str
        """
        return self._active_start_time

    @active_start_time.setter
    def active_start_time(self, active_start_time):
        r"""Sets the active_start_time of this JobScheduleDailyFrequencyInfo.

        每日第一次执行时间。每日频率类型为每日一次时，则只执行这一次。 HH:mm:ss

        :param active_start_time: The active_start_time of this JobScheduleDailyFrequencyInfo.
        :type active_start_time: str
        """
        self._active_start_time = active_start_time

    @property
    def active_end_time(self):
        r"""Gets the active_end_time of this JobScheduleDailyFrequencyInfo.

        最后一次执行时间。每日执行多次时该参数必传，每日执行一次时不生效。 HH:mm:ss

        :return: The active_end_time of this JobScheduleDailyFrequencyInfo.
        :rtype: str
        """
        return self._active_end_time

    @active_end_time.setter
    def active_end_time(self, active_end_time):
        r"""Sets the active_end_time of this JobScheduleDailyFrequencyInfo.

        最后一次执行时间。每日执行多次时该参数必传，每日执行一次时不生效。 HH:mm:ss

        :param active_end_time: The active_end_time of this JobScheduleDailyFrequencyInfo.
        :type active_end_time: str
        """
        self._active_end_time = active_end_time

    @property
    def freq_subday_interval(self):
        r"""Gets the freq_subday_interval of this JobScheduleDailyFrequencyInfo.

        执行间隔。每日执行多次时该参数必传，每日执行一次时不生效。取值范围1至99

        :return: The freq_subday_interval of this JobScheduleDailyFrequencyInfo.
        :rtype: int
        """
        return self._freq_subday_interval

    @freq_subday_interval.setter
    def freq_subday_interval(self, freq_subday_interval):
        r"""Sets the freq_subday_interval of this JobScheduleDailyFrequencyInfo.

        执行间隔。每日执行多次时该参数必传，每日执行一次时不生效。取值范围1至99

        :param freq_subday_interval: The freq_subday_interval of this JobScheduleDailyFrequencyInfo.
        :type freq_subday_interval: int
        """
        self._freq_subday_interval = freq_subday_interval

    @property
    def freq_interval_unit(self):
        r"""Gets the freq_interval_unit of this JobScheduleDailyFrequencyInfo.

        执行间隔的单位。每日执行多次时该参数必传，每日执行一次时不生效。 second:秒, minute:分, hour:时

        :return: The freq_interval_unit of this JobScheduleDailyFrequencyInfo.
        :rtype: str
        """
        return self._freq_interval_unit

    @freq_interval_unit.setter
    def freq_interval_unit(self, freq_interval_unit):
        r"""Sets the freq_interval_unit of this JobScheduleDailyFrequencyInfo.

        执行间隔的单位。每日执行多次时该参数必传，每日执行一次时不生效。 second:秒, minute:分, hour:时

        :param freq_interval_unit: The freq_interval_unit of this JobScheduleDailyFrequencyInfo.
        :type freq_interval_unit: str
        """
        self._freq_interval_unit = freq_interval_unit

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
        if not isinstance(other, JobScheduleDailyFrequencyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
