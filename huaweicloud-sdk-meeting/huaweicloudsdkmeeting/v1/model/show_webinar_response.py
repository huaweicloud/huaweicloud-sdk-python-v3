# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebinarResponse(SdkResponse):

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
        'notify_setting': 'OpenNotifySetting',
        'attendees': 'list[str]'
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
        'notify_setting': 'notifySetting',
        'attendees': 'attendees'
    }

    def __init__(self, conference_id=None, corp_id=None, subject=None, description=None, start_time=None, duration=None, time_zone_id=None, state=None, scheduser_id=None, dept_name=None, scheduser_name=None, vmr_pkg_name=None, call_restriction=None, scope=None, audience_scope=None, chair_join_uri=None, chair_passwd=None, guest_join_uri=None, guest_passwd=None, audience_join_uri=None, audience_passwd=None, notify_setting=None, attendees=None):
        """ShowWebinarResponse

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
        :param notify_setting: 
        :type notify_setting: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        :param attendees: 与会嘉宾名称列表。
        :type attendees: list[str]
        """
        
        super(ShowWebinarResponse, self).__init__()

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
        self._notify_setting = None
        self._attendees = None
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
        if notify_setting is not None:
            self.notify_setting = notify_setting
        if attendees is not None:
            self.attendees = attendees

    @property
    def conference_id(self):
        """Gets the conference_id of this ShowWebinarResponse.

        网络研讨会ID。

        :return: The conference_id of this ShowWebinarResponse.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this ShowWebinarResponse.

        网络研讨会ID。

        :param conference_id: The conference_id of this ShowWebinarResponse.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def corp_id(self):
        """Gets the corp_id of this ShowWebinarResponse.

        企业ID。

        :return: The corp_id of this ShowWebinarResponse.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this ShowWebinarResponse.

        企业ID。

        :param corp_id: The corp_id of this ShowWebinarResponse.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def subject(self):
        """Gets the subject of this ShowWebinarResponse.

        网络研讨会主题。

        :return: The subject of this ShowWebinarResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ShowWebinarResponse.

        网络研讨会主题。

        :param subject: The subject of this ShowWebinarResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def description(self):
        """Gets the description of this ShowWebinarResponse.

        网络研讨会描述。

        :return: The description of this ShowWebinarResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowWebinarResponse.

        网络研讨会描述。

        :param description: The description of this ShowWebinarResponse.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this ShowWebinarResponse.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :return: The start_time of this ShowWebinarResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowWebinarResponse.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :param start_time: The start_time of this ShowWebinarResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this ShowWebinarResponse.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :return: The duration of this ShowWebinarResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ShowWebinarResponse.

        网络研讨会持续时长，单位分钟，取值范围[15,1440]。

        :param duration: The duration of this ShowWebinarResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this ShowWebinarResponse.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :return: The time_zone_id of this ShowWebinarResponse.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this ShowWebinarResponse.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :param time_zone_id: The time_zone_id of this ShowWebinarResponse.
        :type time_zone_id: int
        """
        self._time_zone_id = time_zone_id

    @property
    def state(self):
        """Gets the state of this ShowWebinarResponse.


        :return: The state of this ShowWebinarResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MeetingStatus`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowWebinarResponse.


        :param state: The state of this ShowWebinarResponse.
        :type state: :class:`huaweicloudsdkmeeting.v1.MeetingStatus`
        """
        self._state = state

    @property
    def scheduser_id(self):
        """Gets the scheduser_id of this ShowWebinarResponse.

        网络研讨会预订者的用户UUID。

        :return: The scheduser_id of this ShowWebinarResponse.
        :rtype: str
        """
        return self._scheduser_id

    @scheduser_id.setter
    def scheduser_id(self, scheduser_id):
        """Sets the scheduser_id of this ShowWebinarResponse.

        网络研讨会预订者的用户UUID。

        :param scheduser_id: The scheduser_id of this ShowWebinarResponse.
        :type scheduser_id: str
        """
        self._scheduser_id = scheduser_id

    @property
    def dept_name(self):
        """Gets the dept_name of this ShowWebinarResponse.

        预订者部门命名。

        :return: The dept_name of this ShowWebinarResponse.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ShowWebinarResponse.

        预订者部门命名。

        :param dept_name: The dept_name of this ShowWebinarResponse.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this ShowWebinarResponse.

        预订者名称。

        :return: The scheduser_name of this ShowWebinarResponse.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this ShowWebinarResponse.

        预订者名称。

        :param scheduser_name: The scheduser_name of this ShowWebinarResponse.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this ShowWebinarResponse.

        网络研讨会VMR名称。

        :return: The vmr_pkg_name of this ShowWebinarResponse.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this ShowWebinarResponse.

        网络研讨会VMR名称。

        :param vmr_pkg_name: The vmr_pkg_name of this ShowWebinarResponse.
        :type vmr_pkg_name: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def call_restriction(self):
        """Gets the call_restriction of this ShowWebinarResponse.

        入会范围开关。

        :return: The call_restriction of this ShowWebinarResponse.
        :rtype: bool
        """
        return self._call_restriction

    @call_restriction.setter
    def call_restriction(self, call_restriction):
        """Sets the call_restriction of this ShowWebinarResponse.

        入会范围开关。

        :param call_restriction: The call_restriction of this ShowWebinarResponse.
        :type call_restriction: bool
        """
        self._call_restriction = call_restriction

    @property
    def scope(self):
        """Gets the scope of this ShowWebinarResponse.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :return: The scope of this ShowWebinarResponse.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ShowWebinarResponse.

        主持人、嘉宾入会范围。 * 0: 所有用户 * 2: 企业内用户 * 3: 被邀请用户 

        :param scope: The scope of this ShowWebinarResponse.
        :type scope: int
        """
        self._scope = scope

    @property
    def audience_scope(self):
        """Gets the audience_scope of this ShowWebinarResponse.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户 

        :return: The audience_scope of this ShowWebinarResponse.
        :rtype: int
        """
        return self._audience_scope

    @audience_scope.setter
    def audience_scope(self, audience_scope):
        """Sets the audience_scope of this ShowWebinarResponse.

        观众入会范围。 * 0: 所有用户 * 2: 企业内用户 

        :param audience_scope: The audience_scope of this ShowWebinarResponse.
        :type audience_scope: int
        """
        self._audience_scope = audience_scope

    @property
    def chair_join_uri(self):
        """Gets the chair_join_uri of this ShowWebinarResponse.

        主持人入会地址。

        :return: The chair_join_uri of this ShowWebinarResponse.
        :rtype: str
        """
        return self._chair_join_uri

    @chair_join_uri.setter
    def chair_join_uri(self, chair_join_uri):
        """Sets the chair_join_uri of this ShowWebinarResponse.

        主持人入会地址。

        :param chair_join_uri: The chair_join_uri of this ShowWebinarResponse.
        :type chair_join_uri: str
        """
        self._chair_join_uri = chair_join_uri

    @property
    def chair_passwd(self):
        """Gets the chair_passwd of this ShowWebinarResponse.

        主持人入会密码。

        :return: The chair_passwd of this ShowWebinarResponse.
        :rtype: str
        """
        return self._chair_passwd

    @chair_passwd.setter
    def chair_passwd(self, chair_passwd):
        """Sets the chair_passwd of this ShowWebinarResponse.

        主持人入会密码。

        :param chair_passwd: The chair_passwd of this ShowWebinarResponse.
        :type chair_passwd: str
        """
        self._chair_passwd = chair_passwd

    @property
    def guest_join_uri(self):
        """Gets the guest_join_uri of this ShowWebinarResponse.

        嘉宾入会地址。

        :return: The guest_join_uri of this ShowWebinarResponse.
        :rtype: str
        """
        return self._guest_join_uri

    @guest_join_uri.setter
    def guest_join_uri(self, guest_join_uri):
        """Sets the guest_join_uri of this ShowWebinarResponse.

        嘉宾入会地址。

        :param guest_join_uri: The guest_join_uri of this ShowWebinarResponse.
        :type guest_join_uri: str
        """
        self._guest_join_uri = guest_join_uri

    @property
    def guest_passwd(self):
        """Gets the guest_passwd of this ShowWebinarResponse.

        嘉宾入会密码。

        :return: The guest_passwd of this ShowWebinarResponse.
        :rtype: str
        """
        return self._guest_passwd

    @guest_passwd.setter
    def guest_passwd(self, guest_passwd):
        """Sets the guest_passwd of this ShowWebinarResponse.

        嘉宾入会密码。

        :param guest_passwd: The guest_passwd of this ShowWebinarResponse.
        :type guest_passwd: str
        """
        self._guest_passwd = guest_passwd

    @property
    def audience_join_uri(self):
        """Gets the audience_join_uri of this ShowWebinarResponse.

        观众入会地址。

        :return: The audience_join_uri of this ShowWebinarResponse.
        :rtype: str
        """
        return self._audience_join_uri

    @audience_join_uri.setter
    def audience_join_uri(self, audience_join_uri):
        """Sets the audience_join_uri of this ShowWebinarResponse.

        观众入会地址。

        :param audience_join_uri: The audience_join_uri of this ShowWebinarResponse.
        :type audience_join_uri: str
        """
        self._audience_join_uri = audience_join_uri

    @property
    def audience_passwd(self):
        """Gets the audience_passwd of this ShowWebinarResponse.

        观众入会密码。

        :return: The audience_passwd of this ShowWebinarResponse.
        :rtype: str
        """
        return self._audience_passwd

    @audience_passwd.setter
    def audience_passwd(self, audience_passwd):
        """Sets the audience_passwd of this ShowWebinarResponse.

        观众入会密码。

        :param audience_passwd: The audience_passwd of this ShowWebinarResponse.
        :type audience_passwd: str
        """
        self._audience_passwd = audience_passwd

    @property
    def notify_setting(self):
        """Gets the notify_setting of this ShowWebinarResponse.


        :return: The notify_setting of this ShowWebinarResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        """
        return self._notify_setting

    @notify_setting.setter
    def notify_setting(self, notify_setting):
        """Sets the notify_setting of this ShowWebinarResponse.


        :param notify_setting: The notify_setting of this ShowWebinarResponse.
        :type notify_setting: :class:`huaweicloudsdkmeeting.v1.OpenNotifySetting`
        """
        self._notify_setting = notify_setting

    @property
    def attendees(self):
        """Gets the attendees of this ShowWebinarResponse.

        与会嘉宾名称列表。

        :return: The attendees of this ShowWebinarResponse.
        :rtype: list[str]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this ShowWebinarResponse.

        与会嘉宾名称列表。

        :param attendees: The attendees of this ShowWebinarResponse.
        :type attendees: list[str]
        """
        self._attendees = attendees

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
        if not isinstance(other, ShowWebinarResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
