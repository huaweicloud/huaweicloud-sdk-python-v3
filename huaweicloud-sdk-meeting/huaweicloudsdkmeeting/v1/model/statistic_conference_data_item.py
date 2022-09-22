# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticConferenceDataItem:

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
        'conf_count': 'str',
        'conf_duration': 'str',
        'attendee_count': 'str',
        'conf_concurrent_used_count': 'str',
        'conf24h_count': 'str',
        'conf24h_attendee_count': 'str'
    }

    attribute_map = {
        'time': 'time',
        'conf_count': 'confCount',
        'conf_duration': 'confDuration',
        'attendee_count': 'attendeeCount',
        'conf_concurrent_used_count': 'confConcurrentUsedCount',
        'conf24h_count': 'conf24hCount',
        'conf24h_attendee_count': 'conf24hAttendeeCount'
    }

    def __init__(self, time=None, conf_count=None, conf_duration=None, attendee_count=None, conf_concurrent_used_count=None, conf24h_count=None, conf24h_attendee_count=None):
        """StatisticConferenceDataItem

        The model defined in huaweicloud sdk

        :param time: 日期/月份，category &#x3D; conference_info时有效。 小时，category &#x3D; conference_hourly_info时有效。
        :type time: str
        :param conf_count: 会议数(含VMR)。 category &#x3D; conference_info时有效。
        :type conf_count: str
        :param conf_duration: 会议时长(秒)(含VMR)。 category &#x3D; conference_info时有效。
        :type conf_duration: str
        :param attendee_count: 与会人次(含VMR)。 category &#x3D; conference_info时有效。
        :type attendee_count: str
        :param conf_concurrent_used_count: 并发会议使用数。 category &#x3D; conference_info时有效。
        :type conf_concurrent_used_count: str
        :param conf24h_count: 小时单位会议数(含VMR)。 category &#x3D; conference_hourly_info时有效。
        :type conf24h_count: str
        :param conf24h_attendee_count: 小时单位与会人次(含VMR)。 category &#x3D; conference_hourly_info时有效。
        :type conf24h_attendee_count: str
        """
        
        

        self._time = None
        self._conf_count = None
        self._conf_duration = None
        self._attendee_count = None
        self._conf_concurrent_used_count = None
        self._conf24h_count = None
        self._conf24h_attendee_count = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if conf_count is not None:
            self.conf_count = conf_count
        if conf_duration is not None:
            self.conf_duration = conf_duration
        if attendee_count is not None:
            self.attendee_count = attendee_count
        if conf_concurrent_used_count is not None:
            self.conf_concurrent_used_count = conf_concurrent_used_count
        if conf24h_count is not None:
            self.conf24h_count = conf24h_count
        if conf24h_attendee_count is not None:
            self.conf24h_attendee_count = conf24h_attendee_count

    @property
    def time(self):
        """Gets the time of this StatisticConferenceDataItem.

        日期/月份，category = conference_info时有效。 小时，category = conference_hourly_info时有效。

        :return: The time of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticConferenceDataItem.

        日期/月份，category = conference_info时有效。 小时，category = conference_hourly_info时有效。

        :param time: The time of this StatisticConferenceDataItem.
        :type time: str
        """
        self._time = time

    @property
    def conf_count(self):
        """Gets the conf_count of this StatisticConferenceDataItem.

        会议数(含VMR)。 category = conference_info时有效。

        :return: The conf_count of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._conf_count

    @conf_count.setter
    def conf_count(self, conf_count):
        """Sets the conf_count of this StatisticConferenceDataItem.

        会议数(含VMR)。 category = conference_info时有效。

        :param conf_count: The conf_count of this StatisticConferenceDataItem.
        :type conf_count: str
        """
        self._conf_count = conf_count

    @property
    def conf_duration(self):
        """Gets the conf_duration of this StatisticConferenceDataItem.

        会议时长(秒)(含VMR)。 category = conference_info时有效。

        :return: The conf_duration of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._conf_duration

    @conf_duration.setter
    def conf_duration(self, conf_duration):
        """Sets the conf_duration of this StatisticConferenceDataItem.

        会议时长(秒)(含VMR)。 category = conference_info时有效。

        :param conf_duration: The conf_duration of this StatisticConferenceDataItem.
        :type conf_duration: str
        """
        self._conf_duration = conf_duration

    @property
    def attendee_count(self):
        """Gets the attendee_count of this StatisticConferenceDataItem.

        与会人次(含VMR)。 category = conference_info时有效。

        :return: The attendee_count of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._attendee_count

    @attendee_count.setter
    def attendee_count(self, attendee_count):
        """Sets the attendee_count of this StatisticConferenceDataItem.

        与会人次(含VMR)。 category = conference_info时有效。

        :param attendee_count: The attendee_count of this StatisticConferenceDataItem.
        :type attendee_count: str
        """
        self._attendee_count = attendee_count

    @property
    def conf_concurrent_used_count(self):
        """Gets the conf_concurrent_used_count of this StatisticConferenceDataItem.

        并发会议使用数。 category = conference_info时有效。

        :return: The conf_concurrent_used_count of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._conf_concurrent_used_count

    @conf_concurrent_used_count.setter
    def conf_concurrent_used_count(self, conf_concurrent_used_count):
        """Sets the conf_concurrent_used_count of this StatisticConferenceDataItem.

        并发会议使用数。 category = conference_info时有效。

        :param conf_concurrent_used_count: The conf_concurrent_used_count of this StatisticConferenceDataItem.
        :type conf_concurrent_used_count: str
        """
        self._conf_concurrent_used_count = conf_concurrent_used_count

    @property
    def conf24h_count(self):
        """Gets the conf24h_count of this StatisticConferenceDataItem.

        小时单位会议数(含VMR)。 category = conference_hourly_info时有效。

        :return: The conf24h_count of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._conf24h_count

    @conf24h_count.setter
    def conf24h_count(self, conf24h_count):
        """Sets the conf24h_count of this StatisticConferenceDataItem.

        小时单位会议数(含VMR)。 category = conference_hourly_info时有效。

        :param conf24h_count: The conf24h_count of this StatisticConferenceDataItem.
        :type conf24h_count: str
        """
        self._conf24h_count = conf24h_count

    @property
    def conf24h_attendee_count(self):
        """Gets the conf24h_attendee_count of this StatisticConferenceDataItem.

        小时单位与会人次(含VMR)。 category = conference_hourly_info时有效。

        :return: The conf24h_attendee_count of this StatisticConferenceDataItem.
        :rtype: str
        """
        return self._conf24h_attendee_count

    @conf24h_attendee_count.setter
    def conf24h_attendee_count(self, conf24h_attendee_count):
        """Sets the conf24h_attendee_count of this StatisticConferenceDataItem.

        小时单位与会人次(含VMR)。 category = conference_hourly_info时有效。

        :param conf24h_attendee_count: The conf24h_attendee_count of this StatisticConferenceDataItem.
        :type conf24h_attendee_count: str
        """
        self._conf24h_attendee_count = conf24h_attendee_count

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
        if not isinstance(other, StatisticConferenceDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
