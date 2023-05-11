# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenEditConfReq:

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
        'subject': 'str',
        'description': 'str',
        'start_time': 'str',
        'duration': 'int',
        'time_zone_id': 'int',
        'attendees': 'list[OpenAttendeeEntity]',
        'notify_setting': 'OpenNotifySetting',
        'guest_passwd': 'str',
        'audience_passwd': 'str',
        'call_restriction': 'bool',
        'scope': 'int',
        'audience_scope': 'int',
        'enable_recording': 'YesNoEnum'
    }

    attribute_map = {
        'conference_id': 'conferenceId',
        'subject': 'subject',
        'description': 'description',
        'start_time': 'startTime',
        'duration': 'duration',
        'time_zone_id': 'timeZoneId',
        'attendees': 'attendees',
        'notify_setting': 'notifySetting',
        'guest_passwd': 'guestPasswd',
        'audience_passwd': 'audiencePasswd',
        'call_restriction': 'callRestriction',
        'scope': 'scope',
        'audience_scope': 'audienceScope',
        'enable_recording': 'enableRecording'
    }

    def __init__(self, conference_id=None, subject=None, description=None, start_time=None, duration=None, time_zone_id=None, attendees=None, notify_setting=None, guest_passwd=None, audience_passwd=None, call_restriction=None, scope=None, audience_scope=None, enable_recording=None):
        """OpenEditConfReq

        The model defined in huaweicloud sdk

        :param conference_id: 网络研讨会ID。
        :type conference_id: str
        :param subject: 网络研讨会主题。长度限制为128个字符。
        :type subject: str
        :param description: 网络研讨会描述，长度限制为1000个字符。
        :type description: str
        :param start_time: 网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。
        :type start_time: str
        :param duration: 网络研讨会持续时长，单位分钟，取值范围[15,1440]。
        :type duration: int
        :param time_zone_id: 会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 &gt; * 举例：“timeZoneID”:\&quot;26\&quot;，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 
        :type time_zone_id: int
        :param attendees: 与会嘉宾列表。 &gt; 观众只能自己通过链接或者会议ID+密码加入，不支持被邀请。 
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.OpenAttendeeEntity`]
        :param notify_setting: 
        :type notify_setting: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        :param guest_passwd: 嘉宾密码（4-16位长度的纯数字)。
        :type guest_passwd: str
        :param audience_passwd: 观众密码（4-16位长度的纯数字)。
        :type audience_passwd: str
        :param call_restriction: 入会范围开关。
        :type call_restriction: bool
        :param scope: 主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 
        :type scope: int
        :param audience_scope: 观众入会范围。 * 0: 所有用户 * 2: 企业内用户和被邀请用户 
        :type audience_scope: int
        :param enable_recording: 
        :type enable_recording: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        """
        
        

        self._conference_id = None
        self._subject = None
        self._description = None
        self._start_time = None
        self._duration = None
        self._time_zone_id = None
        self._attendees = None
        self._notify_setting = None
        self._guest_passwd = None
        self._audience_passwd = None
        self._call_restriction = None
        self._scope = None
        self._audience_scope = None
        self._enable_recording = None
        self.discriminator = None

        self.conference_id = conference_id
        self.subject = subject
        if description is not None:
            self.description = description
        self.start_time = start_time
        self.duration = duration
        self.time_zone_id = time_zone_id
        if attendees is not None:
            self.attendees = attendees
        if notify_setting is not None:
            self.notify_setting = notify_setting
        if guest_passwd is not None:
            self.guest_passwd = guest_passwd
        if audience_passwd is not None:
            self.audience_passwd = audience_passwd
        if call_restriction is not None:
            self.call_restriction = call_restriction
        if scope is not None:
            self.scope = scope
        if audience_scope is not None:
            self.audience_scope = audience_scope
        if enable_recording is not None:
            self.enable_recording = enable_recording

    @property
    def conference_id(self):
        """Gets the conference_id of this OpenEditConfReq.

        网络研讨会ID。

        :return: The conference_id of this OpenEditConfReq.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this OpenEditConfReq.

        网络研讨会ID。

        :param conference_id: The conference_id of this OpenEditConfReq.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def subject(self):
        """Gets the subject of this OpenEditConfReq.

        网络研讨会主题。长度限制为128个字符。

        :return: The subject of this OpenEditConfReq.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this OpenEditConfReq.

        网络研讨会主题。长度限制为128个字符。

        :param subject: The subject of this OpenEditConfReq.
        :type subject: str
        """
        self._subject = subject

    @property
    def description(self):
        """Gets the description of this OpenEditConfReq.

        网络研讨会描述，长度限制为1000个字符。

        :return: The description of this OpenEditConfReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenEditConfReq.

        网络研讨会描述，长度限制为1000个字符。

        :param description: The description of this OpenEditConfReq.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this OpenEditConfReq.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :return: The start_time of this OpenEditConfReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OpenEditConfReq.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :param start_time: The start_time of this OpenEditConfReq.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this OpenEditConfReq.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :return: The duration of this OpenEditConfReq.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OpenEditConfReq.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :param duration: The duration of this OpenEditConfReq.
        :type duration: int
        """
        self._duration = duration

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this OpenEditConfReq.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :return: The time_zone_id of this OpenEditConfReq.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this OpenEditConfReq.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :param time_zone_id: The time_zone_id of this OpenEditConfReq.
        :type time_zone_id: int
        """
        self._time_zone_id = time_zone_id

    @property
    def attendees(self):
        """Gets the attendees of this OpenEditConfReq.

        与会嘉宾列表。 > 观众只能自己通过链接或者会议ID+密码加入，不支持被邀请。 

        :return: The attendees of this OpenEditConfReq.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.OpenAttendeeEntity`]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this OpenEditConfReq.

        与会嘉宾列表。 > 观众只能自己通过链接或者会议ID+密码加入，不支持被邀请。 

        :param attendees: The attendees of this OpenEditConfReq.
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.OpenAttendeeEntity`]
        """
        self._attendees = attendees

    @property
    def notify_setting(self):
        """Gets the notify_setting of this OpenEditConfReq.

        :return: The notify_setting of this OpenEditConfReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        """
        return self._notify_setting

    @notify_setting.setter
    def notify_setting(self, notify_setting):
        """Sets the notify_setting of this OpenEditConfReq.

        :param notify_setting: The notify_setting of this OpenEditConfReq.
        :type notify_setting: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        """
        self._notify_setting = notify_setting

    @property
    def guest_passwd(self):
        """Gets the guest_passwd of this OpenEditConfReq.

        嘉宾密码（4-16位长度的纯数字)。

        :return: The guest_passwd of this OpenEditConfReq.
        :rtype: str
        """
        return self._guest_passwd

    @guest_passwd.setter
    def guest_passwd(self, guest_passwd):
        """Sets the guest_passwd of this OpenEditConfReq.

        嘉宾密码（4-16位长度的纯数字)。

        :param guest_passwd: The guest_passwd of this OpenEditConfReq.
        :type guest_passwd: str
        """
        self._guest_passwd = guest_passwd

    @property
    def audience_passwd(self):
        """Gets the audience_passwd of this OpenEditConfReq.

        观众密码（4-16位长度的纯数字)。

        :return: The audience_passwd of this OpenEditConfReq.
        :rtype: str
        """
        return self._audience_passwd

    @audience_passwd.setter
    def audience_passwd(self, audience_passwd):
        """Sets the audience_passwd of this OpenEditConfReq.

        观众密码（4-16位长度的纯数字)。

        :param audience_passwd: The audience_passwd of this OpenEditConfReq.
        :type audience_passwd: str
        """
        self._audience_passwd = audience_passwd

    @property
    def call_restriction(self):
        """Gets the call_restriction of this OpenEditConfReq.

        入会范围开关。

        :return: The call_restriction of this OpenEditConfReq.
        :rtype: bool
        """
        return self._call_restriction

    @call_restriction.setter
    def call_restriction(self, call_restriction):
        """Sets the call_restriction of this OpenEditConfReq.

        入会范围开关。

        :param call_restriction: The call_restriction of this OpenEditConfReq.
        :type call_restriction: bool
        """
        self._call_restriction = call_restriction

    @property
    def scope(self):
        """Gets the scope of this OpenEditConfReq.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :return: The scope of this OpenEditConfReq.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OpenEditConfReq.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :param scope: The scope of this OpenEditConfReq.
        :type scope: int
        """
        self._scope = scope

    @property
    def audience_scope(self):
        """Gets the audience_scope of this OpenEditConfReq.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户和被邀请用户 

        :return: The audience_scope of this OpenEditConfReq.
        :rtype: int
        """
        return self._audience_scope

    @audience_scope.setter
    def audience_scope(self, audience_scope):
        """Sets the audience_scope of this OpenEditConfReq.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户和被邀请用户 

        :param audience_scope: The audience_scope of this OpenEditConfReq.
        :type audience_scope: int
        """
        self._audience_scope = audience_scope

    @property
    def enable_recording(self):
        """Gets the enable_recording of this OpenEditConfReq.

        :return: The enable_recording of this OpenEditConfReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        """
        return self._enable_recording

    @enable_recording.setter
    def enable_recording(self, enable_recording):
        """Sets the enable_recording of this OpenEditConfReq.

        :param enable_recording: The enable_recording of this OpenEditConfReq.
        :type enable_recording: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        """
        self._enable_recording = enable_recording

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
        if not isinstance(other, OpenEditConfReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
