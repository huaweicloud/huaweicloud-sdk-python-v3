# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateUsedJobSchedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'job_schedule_type': 'str',
        'one_time_occurrence': 'JobScheduleOneTimeOccurrenceInfo',
        'frequency': 'JobScheduleFrequencyInfo',
        'daily_frequency': 'JobScheduleDailyFrequencyInfo',
        'duration': 'JobScheduleDurationInfo'
    }

    attribute_map = {
        'id': 'id',
        'job_schedule_type': 'job_schedule_type',
        'one_time_occurrence': 'one_time_occurrence',
        'frequency': 'frequency',
        'daily_frequency': 'daily_frequency',
        'duration': 'duration'
    }

    def __init__(self, id=None, job_schedule_type=None, one_time_occurrence=None, frequency=None, daily_frequency=None, duration=None):
        r"""OperateUsedJobSchedule

        The model defined in huaweicloud sdk

        :param id: 策略id。
        :type id: str
        :param job_schedule_type: 计划类型。默认值recurring。  automatically：SQL Server代理启动时自动启动。 cpu_idle：CPU空闲时启动。 recurring：重复执行。 one_time：执行一次。
        :type job_schedule_type: str
        :param one_time_occurrence: 
        :type one_time_occurrence: :class:`huaweicloudsdkrds.v3.JobScheduleOneTimeOccurrenceInfo`
        :param frequency: 
        :type frequency: :class:`huaweicloudsdkrds.v3.JobScheduleFrequencyInfo`
        :param daily_frequency: 
        :type daily_frequency: :class:`huaweicloudsdkrds.v3.JobScheduleDailyFrequencyInfo`
        :param duration: 
        :type duration: :class:`huaweicloudsdkrds.v3.JobScheduleDurationInfo`
        """
        
        

        self._id = None
        self._job_schedule_type = None
        self._one_time_occurrence = None
        self._frequency = None
        self._daily_frequency = None
        self._duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_schedule_type is not None:
            self.job_schedule_type = job_schedule_type
        if one_time_occurrence is not None:
            self.one_time_occurrence = one_time_occurrence
        if frequency is not None:
            self.frequency = frequency
        if daily_frequency is not None:
            self.daily_frequency = daily_frequency
        if duration is not None:
            self.duration = duration

    @property
    def id(self):
        r"""Gets the id of this OperateUsedJobSchedule.

        策略id。

        :return: The id of this OperateUsedJobSchedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OperateUsedJobSchedule.

        策略id。

        :param id: The id of this OperateUsedJobSchedule.
        :type id: str
        """
        self._id = id

    @property
    def job_schedule_type(self):
        r"""Gets the job_schedule_type of this OperateUsedJobSchedule.

        计划类型。默认值recurring。  automatically：SQL Server代理启动时自动启动。 cpu_idle：CPU空闲时启动。 recurring：重复执行。 one_time：执行一次。

        :return: The job_schedule_type of this OperateUsedJobSchedule.
        :rtype: str
        """
        return self._job_schedule_type

    @job_schedule_type.setter
    def job_schedule_type(self, job_schedule_type):
        r"""Sets the job_schedule_type of this OperateUsedJobSchedule.

        计划类型。默认值recurring。  automatically：SQL Server代理启动时自动启动。 cpu_idle：CPU空闲时启动。 recurring：重复执行。 one_time：执行一次。

        :param job_schedule_type: The job_schedule_type of this OperateUsedJobSchedule.
        :type job_schedule_type: str
        """
        self._job_schedule_type = job_schedule_type

    @property
    def one_time_occurrence(self):
        r"""Gets the one_time_occurrence of this OperateUsedJobSchedule.

        :return: The one_time_occurrence of this OperateUsedJobSchedule.
        :rtype: :class:`huaweicloudsdkrds.v3.JobScheduleOneTimeOccurrenceInfo`
        """
        return self._one_time_occurrence

    @one_time_occurrence.setter
    def one_time_occurrence(self, one_time_occurrence):
        r"""Sets the one_time_occurrence of this OperateUsedJobSchedule.

        :param one_time_occurrence: The one_time_occurrence of this OperateUsedJobSchedule.
        :type one_time_occurrence: :class:`huaweicloudsdkrds.v3.JobScheduleOneTimeOccurrenceInfo`
        """
        self._one_time_occurrence = one_time_occurrence

    @property
    def frequency(self):
        r"""Gets the frequency of this OperateUsedJobSchedule.

        :return: The frequency of this OperateUsedJobSchedule.
        :rtype: :class:`huaweicloudsdkrds.v3.JobScheduleFrequencyInfo`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this OperateUsedJobSchedule.

        :param frequency: The frequency of this OperateUsedJobSchedule.
        :type frequency: :class:`huaweicloudsdkrds.v3.JobScheduleFrequencyInfo`
        """
        self._frequency = frequency

    @property
    def daily_frequency(self):
        r"""Gets the daily_frequency of this OperateUsedJobSchedule.

        :return: The daily_frequency of this OperateUsedJobSchedule.
        :rtype: :class:`huaweicloudsdkrds.v3.JobScheduleDailyFrequencyInfo`
        """
        return self._daily_frequency

    @daily_frequency.setter
    def daily_frequency(self, daily_frequency):
        r"""Sets the daily_frequency of this OperateUsedJobSchedule.

        :param daily_frequency: The daily_frequency of this OperateUsedJobSchedule.
        :type daily_frequency: :class:`huaweicloudsdkrds.v3.JobScheduleDailyFrequencyInfo`
        """
        self._daily_frequency = daily_frequency

    @property
    def duration(self):
        r"""Gets the duration of this OperateUsedJobSchedule.

        :return: The duration of this OperateUsedJobSchedule.
        :rtype: :class:`huaweicloudsdkrds.v3.JobScheduleDurationInfo`
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this OperateUsedJobSchedule.

        :param duration: The duration of this OperateUsedJobSchedule.
        :type duration: :class:`huaweicloudsdkrds.v3.JobScheduleDurationInfo`
        """
        self._duration = duration

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
        if not isinstance(other, OperateUsedJobSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
