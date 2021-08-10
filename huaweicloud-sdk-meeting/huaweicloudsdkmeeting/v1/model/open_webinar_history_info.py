# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenWebinarHistoryInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'conf_uuid': 'str',
        'subject': 'str',
        'scheduser_name': 'str',
        'moderator': 'str',
        'dept_name': 'str',
        'time_zone_id': 'int',
        'start_time': 'str',
        'duration': 'int',
        'actual_start_time': 'str',
        'end_time': 'str',
        'actual_duration': 'int',
        'attendee_count': 'int',
        'chair_count': 'int',
        'guest_count': 'int',
        'audience_count': 'int',
        'vmr_id': 'str',
        'vmr_pkg_audience_parties': 'int',
        'vmr_pkg_name': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceId',
        'conf_uuid': 'confUUID',
        'subject': 'subject',
        'scheduser_name': 'scheduserName',
        'moderator': 'moderator',
        'dept_name': 'deptName',
        'time_zone_id': 'timeZoneId',
        'start_time': 'startTime',
        'duration': 'duration',
        'actual_start_time': 'actualStartTime',
        'end_time': 'endTime',
        'actual_duration': 'actualDuration',
        'attendee_count': 'attendeeCount',
        'chair_count': 'chairCount',
        'guest_count': 'guestCount',
        'audience_count': 'audienceCount',
        'vmr_id': 'vmrId',
        'vmr_pkg_audience_parties': 'vmrPkgAudienceParties',
        'vmr_pkg_name': 'vmrPkgName'
    }

    def __init__(self, conference_id=None, conf_uuid=None, subject=None, scheduser_name=None, moderator=None, dept_name=None, time_zone_id=None, start_time=None, duration=None, actual_start_time=None, end_time=None, actual_duration=None, attendee_count=None, chair_count=None, guest_count=None, audience_count=None, vmr_id=None, vmr_pkg_audience_parties=None, vmr_pkg_name=None):
        """OpenWebinarHistoryInfo - a model defined in huaweicloud sdk"""
        
        

        self._conference_id = None
        self._conf_uuid = None
        self._subject = None
        self._scheduser_name = None
        self._moderator = None
        self._dept_name = None
        self._time_zone_id = None
        self._start_time = None
        self._duration = None
        self._actual_start_time = None
        self._end_time = None
        self._actual_duration = None
        self._attendee_count = None
        self._chair_count = None
        self._guest_count = None
        self._audience_count = None
        self._vmr_id = None
        self._vmr_pkg_audience_parties = None
        self._vmr_pkg_name = None
        self.discriminator = None

        if conference_id is not None:
            self.conference_id = conference_id
        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if subject is not None:
            self.subject = subject
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if moderator is not None:
            self.moderator = moderator
        if dept_name is not None:
            self.dept_name = dept_name
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if actual_start_time is not None:
            self.actual_start_time = actual_start_time
        if end_time is not None:
            self.end_time = end_time
        if actual_duration is not None:
            self.actual_duration = actual_duration
        if attendee_count is not None:
            self.attendee_count = attendee_count
        if chair_count is not None:
            self.chair_count = chair_count
        if guest_count is not None:
            self.guest_count = guest_count
        if audience_count is not None:
            self.audience_count = audience_count
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if vmr_pkg_audience_parties is not None:
            self.vmr_pkg_audience_parties = vmr_pkg_audience_parties
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name

    @property
    def conference_id(self):
        """Gets the conference_id of this OpenWebinarHistoryInfo.

        会议id

        :return: The conference_id of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this OpenWebinarHistoryInfo.

        会议id

        :param conference_id: The conference_id of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this OpenWebinarHistoryInfo.

        会议UUID

        :return: The conf_uuid of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this OpenWebinarHistoryInfo.

        会议UUID

        :param conf_uuid: The conf_uuid of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def subject(self):
        """Gets the subject of this OpenWebinarHistoryInfo.

        主题

        :return: The subject of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this OpenWebinarHistoryInfo.

        主题

        :param subject: The subject of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._subject = subject

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this OpenWebinarHistoryInfo.

        会议订阅者

        :return: The scheduser_name of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this OpenWebinarHistoryInfo.

        会议订阅者

        :param scheduser_name: The scheduser_name of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._scheduser_name = scheduser_name

    @property
    def moderator(self):
        """Gets the moderator of this OpenWebinarHistoryInfo.

        会议主持人

        :return: The moderator of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._moderator

    @moderator.setter
    def moderator(self, moderator):
        """Sets the moderator of this OpenWebinarHistoryInfo.

        会议主持人

        :param moderator: The moderator of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._moderator = moderator

    @property
    def dept_name(self):
        """Gets the dept_name of this OpenWebinarHistoryInfo.

        部门名称

        :return: The dept_name of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this OpenWebinarHistoryInfo.

        部门名称

        :param dept_name: The dept_name of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this OpenWebinarHistoryInfo.

        时区ID

        :return: The time_zone_id of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this OpenWebinarHistoryInfo.

        时区ID

        :param time_zone_id: The time_zone_id of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._time_zone_id = time_zone_id

    @property
    def start_time(self):
        """Gets the start_time of this OpenWebinarHistoryInfo.

        会议预约时间

        :return: The start_time of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OpenWebinarHistoryInfo.

        会议预约时间

        :param start_time: The start_time of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this OpenWebinarHistoryInfo.

        预约会议时长，单位分钟

        :return: The duration of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OpenWebinarHistoryInfo.

        预约会议时长，单位分钟

        :param duration: The duration of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._duration = duration

    @property
    def actual_start_time(self):
        """Gets the actual_start_time of this OpenWebinarHistoryInfo.

        会议开始时间

        :return: The actual_start_time of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._actual_start_time

    @actual_start_time.setter
    def actual_start_time(self, actual_start_time):
        """Sets the actual_start_time of this OpenWebinarHistoryInfo.

        会议开始时间

        :param actual_start_time: The actual_start_time of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._actual_start_time = actual_start_time

    @property
    def end_time(self):
        """Gets the end_time of this OpenWebinarHistoryInfo.

        会议结束时间

        :return: The end_time of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this OpenWebinarHistoryInfo.

        会议结束时间

        :param end_time: The end_time of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._end_time = end_time

    @property
    def actual_duration(self):
        """Gets the actual_duration of this OpenWebinarHistoryInfo.

        实际会议时长，单位分钟

        :return: The actual_duration of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._actual_duration

    @actual_duration.setter
    def actual_duration(self, actual_duration):
        """Sets the actual_duration of this OpenWebinarHistoryInfo.

        实际会议时长，单位分钟

        :param actual_duration: The actual_duration of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._actual_duration = actual_duration

    @property
    def attendee_count(self):
        """Gets the attendee_count of this OpenWebinarHistoryInfo.

        与会人数

        :return: The attendee_count of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._attendee_count

    @attendee_count.setter
    def attendee_count(self, attendee_count):
        """Sets the attendee_count of this OpenWebinarHistoryInfo.

        与会人数

        :param attendee_count: The attendee_count of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._attendee_count = attendee_count

    @property
    def chair_count(self):
        """Gets the chair_count of this OpenWebinarHistoryInfo.

        主持人人数

        :return: The chair_count of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._chair_count

    @chair_count.setter
    def chair_count(self, chair_count):
        """Sets the chair_count of this OpenWebinarHistoryInfo.

        主持人人数

        :param chair_count: The chair_count of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._chair_count = chair_count

    @property
    def guest_count(self):
        """Gets the guest_count of this OpenWebinarHistoryInfo.

        嘉宾人数

        :return: The guest_count of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._guest_count

    @guest_count.setter
    def guest_count(self, guest_count):
        """Sets the guest_count of this OpenWebinarHistoryInfo.

        嘉宾人数

        :param guest_count: The guest_count of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._guest_count = guest_count

    @property
    def audience_count(self):
        """Gets the audience_count of this OpenWebinarHistoryInfo.

        观众人数

        :return: The audience_count of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._audience_count

    @audience_count.setter
    def audience_count(self, audience_count):
        """Sets the audience_count of this OpenWebinarHistoryInfo.

        观众人数

        :param audience_count: The audience_count of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._audience_count = audience_count

    @property
    def vmr_id(self):
        """Gets the vmr_id of this OpenWebinarHistoryInfo.

        VMR ID

        :return: The vmr_id of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this OpenWebinarHistoryInfo.

        VMR ID

        :param vmr_id: The vmr_id of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def vmr_pkg_audience_parties(self):
        """Gets the vmr_pkg_audience_parties of this OpenWebinarHistoryInfo.

        VMR资源规格-最大观众数

        :return: The vmr_pkg_audience_parties of this OpenWebinarHistoryInfo.
        :rtype: int
        """
        return self._vmr_pkg_audience_parties

    @vmr_pkg_audience_parties.setter
    def vmr_pkg_audience_parties(self, vmr_pkg_audience_parties):
        """Sets the vmr_pkg_audience_parties of this OpenWebinarHistoryInfo.

        VMR资源规格-最大观众数

        :param vmr_pkg_audience_parties: The vmr_pkg_audience_parties of this OpenWebinarHistoryInfo.
        :type: int
        """
        self._vmr_pkg_audience_parties = vmr_pkg_audience_parties

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this OpenWebinarHistoryInfo.

        网络研讨会资源名

        :return: The vmr_pkg_name of this OpenWebinarHistoryInfo.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this OpenWebinarHistoryInfo.

        网络研讨会资源名

        :param vmr_pkg_name: The vmr_pkg_name of this OpenWebinarHistoryInfo.
        :type: str
        """
        self._vmr_pkg_name = vmr_pkg_name

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
        if not isinstance(other, OpenWebinarHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
