# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenWebinarBaseInfo:

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
        'corp_id': 'str',
        'subject': 'str',
        'description': 'str',
        'start_time': 'str',
        'duration': 'int',
        'time_zone_id': 'int',
        'state': 'MeetingStatus',
        'scheduser_id': 'str',
        'dept_name': 'str',
        'scheduser_name': 'str',
        'vmr_pkg_name': 'str',
        'call_restriction': 'bool',
        'scope': 'int',
        'audience_scope': 'int',
        'chair_join_uri': 'str',
        'chair_passwd': 'str',
        'guest_join_uri': 'str',
        'guest_passwd': 'str',
        'audience_join_uri': 'str',
        'audience_passwd': 'str',
        'enable_recording': 'YesNoEnum',
        'live_address': 'str',
        'aux_address': 'str',
        'live_url': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceId',
        'corp_id': 'corpId',
        'subject': 'subject',
        'description': 'description',
        'start_time': 'startTime',
        'duration': 'duration',
        'time_zone_id': 'timeZoneId',
        'state': 'state',
        'scheduser_id': 'scheduserId',
        'dept_name': 'deptName',
        'scheduser_name': 'scheduserName',
        'vmr_pkg_name': 'vmrPkgName',
        'call_restriction': 'callRestriction',
        'scope': 'scope',
        'audience_scope': 'audienceScope',
        'chair_join_uri': 'chairJoinUri',
        'chair_passwd': 'chairPasswd',
        'guest_join_uri': 'guestJoinUri',
        'guest_passwd': 'guestPasswd',
        'audience_join_uri': 'audienceJoinUri',
        'audience_passwd': 'audiencePasswd',
        'enable_recording': 'enableRecording',
        'live_address': 'liveAddress',
        'aux_address': 'auxAddress',
        'live_url': 'liveUrl'
    }

    def __init__(self, conference_id=None, corp_id=None, subject=None, description=None, start_time=None, duration=None, time_zone_id=None, state=None, scheduser_id=None, dept_name=None, scheduser_name=None, vmr_pkg_name=None, call_restriction=None, scope=None, audience_scope=None, chair_join_uri=None, chair_passwd=None, guest_join_uri=None, guest_passwd=None, audience_join_uri=None, audience_passwd=None, enable_recording=None, live_address=None, aux_address=None, live_url=None):
        r"""OpenWebinarBaseInfo

        The model defined in huaweicloud sdk

        :param conference_id: 网络研讨会ID。
        :type conference_id: str
        :param corp_id: 企业ID。
        :type corp_id: str
        :param subject: 网络研讨会主题。
        :type subject: str
        :param description: 网络研讨会描述。
        :type description: str
        :param start_time: 网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。
        :type start_time: str
        :param duration: 网络研讨会持续时长，单位分钟，取值范围[15,1440]。
        :type duration: int
        :param time_zone_id: 会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 &gt; * 举例：“timeZoneID”:\&quot;26\&quot;，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 
        :type time_zone_id: int
        :param state: 
        :type state: :class:`huaweicloudsdkmeeting.v1.MeetingStatus`
        :param scheduser_id: 网络研讨会预订者的用户UUID。
        :type scheduser_id: str
        :param dept_name: 预订者部门命名。
        :type dept_name: str
        :param scheduser_name: 预订者名称。
        :type scheduser_name: str
        :param vmr_pkg_name: 网络研讨会VMR名称。
        :type vmr_pkg_name: str
        :param call_restriction: 入会范围开关。
        :type call_restriction: bool
        :param scope: 主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 
        :type scope: int
        :param audience_scope: 观众入会范围。 * 0: 所有用户 * 2: 企业内用户 
        :type audience_scope: int
        :param chair_join_uri: 主持人入会地址。
        :type chair_join_uri: str
        :param chair_passwd: 主持人入会密码。
        :type chair_passwd: str
        :param guest_join_uri: 嘉宾入会地址。
        :type guest_join_uri: str
        :param guest_passwd: 嘉宾入会密码。
        :type guest_passwd: str
        :param audience_join_uri: 观众入会地址。
        :type audience_join_uri: str
        :param audience_passwd: 观众入会密码。
        :type audience_passwd: str
        :param enable_recording: 
        :type enable_recording: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        :param live_address: 主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。
        :type live_address: str
        :param aux_address: 辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。
        :type aux_address: str
        :param live_url: 直播房间地址，在录播类型为录播+直播推流时有效。最大不超过255个字符。
        :type live_url: str
        """
        
        

        self._conference_id = None
        self._corp_id = None
        self._subject = None
        self._description = None
        self._start_time = None
        self._duration = None
        self._time_zone_id = None
        self._state = None
        self._scheduser_id = None
        self._dept_name = None
        self._scheduser_name = None
        self._vmr_pkg_name = None
        self._call_restriction = None
        self._scope = None
        self._audience_scope = None
        self._chair_join_uri = None
        self._chair_passwd = None
        self._guest_join_uri = None
        self._guest_passwd = None
        self._audience_join_uri = None
        self._audience_passwd = None
        self._enable_recording = None
        self._live_address = None
        self._aux_address = None
        self._live_url = None
        self.discriminator = None

        if conference_id is not None:
            self.conference_id = conference_id
        if corp_id is not None:
            self.corp_id = corp_id
        if subject is not None:
            self.subject = subject
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if state is not None:
            self.state = state
        if scheduser_id is not None:
            self.scheduser_id = scheduser_id
        if dept_name is not None:
            self.dept_name = dept_name
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
        if call_restriction is not None:
            self.call_restriction = call_restriction
        if scope is not None:
            self.scope = scope
        if audience_scope is not None:
            self.audience_scope = audience_scope
        if chair_join_uri is not None:
            self.chair_join_uri = chair_join_uri
        if chair_passwd is not None:
            self.chair_passwd = chair_passwd
        if guest_join_uri is not None:
            self.guest_join_uri = guest_join_uri
        if guest_passwd is not None:
            self.guest_passwd = guest_passwd
        if audience_join_uri is not None:
            self.audience_join_uri = audience_join_uri
        if audience_passwd is not None:
            self.audience_passwd = audience_passwd
        if enable_recording is not None:
            self.enable_recording = enable_recording
        if live_address is not None:
            self.live_address = live_address
        if aux_address is not None:
            self.aux_address = aux_address
        if live_url is not None:
            self.live_url = live_url

    @property
    def conference_id(self):
        r"""Gets the conference_id of this OpenWebinarBaseInfo.

        网络研讨会ID。

        :return: The conference_id of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        r"""Sets the conference_id of this OpenWebinarBaseInfo.

        网络研讨会ID。

        :param conference_id: The conference_id of this OpenWebinarBaseInfo.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def corp_id(self):
        r"""Gets the corp_id of this OpenWebinarBaseInfo.

        企业ID。

        :return: The corp_id of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        r"""Sets the corp_id of this OpenWebinarBaseInfo.

        企业ID。

        :param corp_id: The corp_id of this OpenWebinarBaseInfo.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def subject(self):
        r"""Gets the subject of this OpenWebinarBaseInfo.

        网络研讨会主题。

        :return: The subject of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this OpenWebinarBaseInfo.

        网络研讨会主题。

        :param subject: The subject of this OpenWebinarBaseInfo.
        :type subject: str
        """
        self._subject = subject

    @property
    def description(self):
        r"""Gets the description of this OpenWebinarBaseInfo.

        网络研讨会描述。

        :return: The description of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpenWebinarBaseInfo.

        网络研讨会描述。

        :param description: The description of this OpenWebinarBaseInfo.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        r"""Gets the start_time of this OpenWebinarBaseInfo.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :return: The start_time of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this OpenWebinarBaseInfo.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :param start_time: The start_time of this OpenWebinarBaseInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this OpenWebinarBaseInfo.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :return: The duration of this OpenWebinarBaseInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this OpenWebinarBaseInfo.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :param duration: The duration of this OpenWebinarBaseInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def time_zone_id(self):
        r"""Gets the time_zone_id of this OpenWebinarBaseInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :return: The time_zone_id of this OpenWebinarBaseInfo.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        r"""Sets the time_zone_id of this OpenWebinarBaseInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :param time_zone_id: The time_zone_id of this OpenWebinarBaseInfo.
        :type time_zone_id: int
        """
        self._time_zone_id = time_zone_id

    @property
    def state(self):
        r"""Gets the state of this OpenWebinarBaseInfo.

        :return: The state of this OpenWebinarBaseInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MeetingStatus`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this OpenWebinarBaseInfo.

        :param state: The state of this OpenWebinarBaseInfo.
        :type state: :class:`huaweicloudsdkmeeting.v1.MeetingStatus`
        """
        self._state = state

    @property
    def scheduser_id(self):
        r"""Gets the scheduser_id of this OpenWebinarBaseInfo.

        网络研讨会预订者的用户UUID。

        :return: The scheduser_id of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._scheduser_id

    @scheduser_id.setter
    def scheduser_id(self, scheduser_id):
        r"""Sets the scheduser_id of this OpenWebinarBaseInfo.

        网络研讨会预订者的用户UUID。

        :param scheduser_id: The scheduser_id of this OpenWebinarBaseInfo.
        :type scheduser_id: str
        """
        self._scheduser_id = scheduser_id

    @property
    def dept_name(self):
        r"""Gets the dept_name of this OpenWebinarBaseInfo.

        预订者部门命名。

        :return: The dept_name of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        r"""Sets the dept_name of this OpenWebinarBaseInfo.

        预订者部门命名。

        :param dept_name: The dept_name of this OpenWebinarBaseInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def scheduser_name(self):
        r"""Gets the scheduser_name of this OpenWebinarBaseInfo.

        预订者名称。

        :return: The scheduser_name of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        r"""Sets the scheduser_name of this OpenWebinarBaseInfo.

        预订者名称。

        :param scheduser_name: The scheduser_name of this OpenWebinarBaseInfo.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def vmr_pkg_name(self):
        r"""Gets the vmr_pkg_name of this OpenWebinarBaseInfo.

        网络研讨会VMR名称。

        :return: The vmr_pkg_name of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        r"""Sets the vmr_pkg_name of this OpenWebinarBaseInfo.

        网络研讨会VMR名称。

        :param vmr_pkg_name: The vmr_pkg_name of this OpenWebinarBaseInfo.
        :type vmr_pkg_name: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def call_restriction(self):
        r"""Gets the call_restriction of this OpenWebinarBaseInfo.

        入会范围开关。

        :return: The call_restriction of this OpenWebinarBaseInfo.
        :rtype: bool
        """
        return self._call_restriction

    @call_restriction.setter
    def call_restriction(self, call_restriction):
        r"""Sets the call_restriction of this OpenWebinarBaseInfo.

        入会范围开关。

        :param call_restriction: The call_restriction of this OpenWebinarBaseInfo.
        :type call_restriction: bool
        """
        self._call_restriction = call_restriction

    @property
    def scope(self):
        r"""Gets the scope of this OpenWebinarBaseInfo.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :return: The scope of this OpenWebinarBaseInfo.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this OpenWebinarBaseInfo.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :param scope: The scope of this OpenWebinarBaseInfo.
        :type scope: int
        """
        self._scope = scope

    @property
    def audience_scope(self):
        r"""Gets the audience_scope of this OpenWebinarBaseInfo.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户 

        :return: The audience_scope of this OpenWebinarBaseInfo.
        :rtype: int
        """
        return self._audience_scope

    @audience_scope.setter
    def audience_scope(self, audience_scope):
        r"""Sets the audience_scope of this OpenWebinarBaseInfo.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户 

        :param audience_scope: The audience_scope of this OpenWebinarBaseInfo.
        :type audience_scope: int
        """
        self._audience_scope = audience_scope

    @property
    def chair_join_uri(self):
        r"""Gets the chair_join_uri of this OpenWebinarBaseInfo.

        主持人入会地址。

        :return: The chair_join_uri of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._chair_join_uri

    @chair_join_uri.setter
    def chair_join_uri(self, chair_join_uri):
        r"""Sets the chair_join_uri of this OpenWebinarBaseInfo.

        主持人入会地址。

        :param chair_join_uri: The chair_join_uri of this OpenWebinarBaseInfo.
        :type chair_join_uri: str
        """
        self._chair_join_uri = chair_join_uri

    @property
    def chair_passwd(self):
        r"""Gets the chair_passwd of this OpenWebinarBaseInfo.

        主持人入会密码。

        :return: The chair_passwd of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._chair_passwd

    @chair_passwd.setter
    def chair_passwd(self, chair_passwd):
        r"""Sets the chair_passwd of this OpenWebinarBaseInfo.

        主持人入会密码。

        :param chair_passwd: The chair_passwd of this OpenWebinarBaseInfo.
        :type chair_passwd: str
        """
        self._chair_passwd = chair_passwd

    @property
    def guest_join_uri(self):
        r"""Gets the guest_join_uri of this OpenWebinarBaseInfo.

        嘉宾入会地址。

        :return: The guest_join_uri of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._guest_join_uri

    @guest_join_uri.setter
    def guest_join_uri(self, guest_join_uri):
        r"""Sets the guest_join_uri of this OpenWebinarBaseInfo.

        嘉宾入会地址。

        :param guest_join_uri: The guest_join_uri of this OpenWebinarBaseInfo.
        :type guest_join_uri: str
        """
        self._guest_join_uri = guest_join_uri

    @property
    def guest_passwd(self):
        r"""Gets the guest_passwd of this OpenWebinarBaseInfo.

        嘉宾入会密码。

        :return: The guest_passwd of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._guest_passwd

    @guest_passwd.setter
    def guest_passwd(self, guest_passwd):
        r"""Sets the guest_passwd of this OpenWebinarBaseInfo.

        嘉宾入会密码。

        :param guest_passwd: The guest_passwd of this OpenWebinarBaseInfo.
        :type guest_passwd: str
        """
        self._guest_passwd = guest_passwd

    @property
    def audience_join_uri(self):
        r"""Gets the audience_join_uri of this OpenWebinarBaseInfo.

        观众入会地址。

        :return: The audience_join_uri of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._audience_join_uri

    @audience_join_uri.setter
    def audience_join_uri(self, audience_join_uri):
        r"""Sets the audience_join_uri of this OpenWebinarBaseInfo.

        观众入会地址。

        :param audience_join_uri: The audience_join_uri of this OpenWebinarBaseInfo.
        :type audience_join_uri: str
        """
        self._audience_join_uri = audience_join_uri

    @property
    def audience_passwd(self):
        r"""Gets the audience_passwd of this OpenWebinarBaseInfo.

        观众入会密码。

        :return: The audience_passwd of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._audience_passwd

    @audience_passwd.setter
    def audience_passwd(self, audience_passwd):
        r"""Sets the audience_passwd of this OpenWebinarBaseInfo.

        观众入会密码。

        :param audience_passwd: The audience_passwd of this OpenWebinarBaseInfo.
        :type audience_passwd: str
        """
        self._audience_passwd = audience_passwd

    @property
    def enable_recording(self):
        r"""Gets the enable_recording of this OpenWebinarBaseInfo.

        :return: The enable_recording of this OpenWebinarBaseInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        """
        return self._enable_recording

    @enable_recording.setter
    def enable_recording(self, enable_recording):
        r"""Sets the enable_recording of this OpenWebinarBaseInfo.

        :param enable_recording: The enable_recording of this OpenWebinarBaseInfo.
        :type enable_recording: :class:`huaweicloudsdkmeeting.v1.YesNoEnum`
        """
        self._enable_recording = enable_recording

    @property
    def live_address(self):
        r"""Gets the live_address of this OpenWebinarBaseInfo.

        主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :return: The live_address of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._live_address

    @live_address.setter
    def live_address(self, live_address):
        r"""Sets the live_address of this OpenWebinarBaseInfo.

        主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :param live_address: The live_address of this OpenWebinarBaseInfo.
        :type live_address: str
        """
        self._live_address = live_address

    @property
    def aux_address(self):
        r"""Gets the aux_address of this OpenWebinarBaseInfo.

        辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :return: The aux_address of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._aux_address

    @aux_address.setter
    def aux_address(self, aux_address):
        r"""Sets the aux_address of this OpenWebinarBaseInfo.

        辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :param aux_address: The aux_address of this OpenWebinarBaseInfo.
        :type aux_address: str
        """
        self._aux_address = aux_address

    @property
    def live_url(self):
        r"""Gets the live_url of this OpenWebinarBaseInfo.

        直播房间地址，在录播类型为录播+直播推流时有效。最大不超过255个字符。

        :return: The live_url of this OpenWebinarBaseInfo.
        :rtype: str
        """
        return self._live_url

    @live_url.setter
    def live_url(self, live_url):
        r"""Sets the live_url of this OpenWebinarBaseInfo.

        直播房间地址，在录播类型为录播+直播推流时有效。最大不超过255个字符。

        :param live_url: The live_url of this OpenWebinarBaseInfo.
        :type live_url: str
        """
        self._live_url = live_url

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
        if not isinstance(other, OpenWebinarBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
