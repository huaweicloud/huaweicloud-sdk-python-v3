# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScheduleOneTimeOccurrenceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_start_date': 'str',
        'active_start_time': 'str'
    }

    attribute_map = {
        'active_start_date': 'active_start_date',
        'active_start_time': 'active_start_time'
    }

    def __init__(self, active_start_date=None, active_start_time=None):
        r"""JobScheduleOneTimeOccurrenceInfo

        The model defined in huaweicloud sdk

        :param active_start_date: 执行日期 yyyy-MM-dd。取值范围1990-01-01至2099-12-31
        :type active_start_date: str
        :param active_start_time: 执行时间。HH:mm:ss
        :type active_start_time: str
        """
        
        

        self._active_start_date = None
        self._active_start_time = None
        self.discriminator = None

        if active_start_date is not None:
            self.active_start_date = active_start_date
        if active_start_time is not None:
            self.active_start_time = active_start_time

    @property
    def active_start_date(self):
        r"""Gets the active_start_date of this JobScheduleOneTimeOccurrenceInfo.

        执行日期 yyyy-MM-dd。取值范围1990-01-01至2099-12-31

        :return: The active_start_date of this JobScheduleOneTimeOccurrenceInfo.
        :rtype: str
        """
        return self._active_start_date

    @active_start_date.setter
    def active_start_date(self, active_start_date):
        r"""Sets the active_start_date of this JobScheduleOneTimeOccurrenceInfo.

        执行日期 yyyy-MM-dd。取值范围1990-01-01至2099-12-31

        :param active_start_date: The active_start_date of this JobScheduleOneTimeOccurrenceInfo.
        :type active_start_date: str
        """
        self._active_start_date = active_start_date

    @property
    def active_start_time(self):
        r"""Gets the active_start_time of this JobScheduleOneTimeOccurrenceInfo.

        执行时间。HH:mm:ss

        :return: The active_start_time of this JobScheduleOneTimeOccurrenceInfo.
        :rtype: str
        """
        return self._active_start_time

    @active_start_time.setter
    def active_start_time(self, active_start_time):
        r"""Sets the active_start_time of this JobScheduleOneTimeOccurrenceInfo.

        执行时间。HH:mm:ss

        :param active_start_time: The active_start_time of this JobScheduleOneTimeOccurrenceInfo.
        :type active_start_time: str
        """
        self._active_start_time = active_start_time

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
        if not isinstance(other, JobScheduleOneTimeOccurrenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
