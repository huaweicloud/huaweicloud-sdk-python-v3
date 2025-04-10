# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenWebinarOngoingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'online_attendee_count': 'int',
        'conf_uuid': 'str',
        'dept_name': 'str',
        'conference_id': 'str',
        'corp_id': 'str',
        'subject': 'str',
        'description': 'str',
        'start_time': 'str',
        'time_zone_id': 'int',
        'scheduser_id': 'str',
        'scheduser_name': 'str',
        'vmr_pkg_name': 'str',
        'chair_join_uri': 'str',
        'chair_passwd': 'str',
        'guest_join_uri': 'str',
        'guest_passwd': 'str',
        'audience_join_uri': 'str',
        'audience_passwd': 'str'
    }

    attribute_map = {
        'online_attendee_count': 'onlineAttendeeCount',
        'conf_uuid': 'confUUID',
        'dept_name': 'deptName',
        'conference_id': 'conferenceId',
        'corp_id': 'corpId',
        'subject': 'subject',
        'description': 'description',
        'start_time': 'startTime',
        'time_zone_id': 'timeZoneId',
        'scheduser_id': 'scheduserId',
        'scheduser_name': 'scheduserName',
        'vmr_pkg_name': 'vmrPkgName',
        'chair_join_uri': 'chairJoinUri',
        'chair_passwd': 'chairPasswd',
        'guest_join_uri': 'guestJoinUri',
        'guest_passwd': 'guestPasswd',
        'audience_join_uri': 'audienceJoinUri',
        'audience_passwd': 'audiencePasswd'
    }

    def __init__(self, online_attendee_count=None, conf_uuid=None, dept_name=None, conference_id=None, corp_id=None, subject=None, description=None, start_time=None, time_zone_id=None, scheduser_id=None, scheduser_name=None, vmr_pkg_name=None, chair_join_uri=None, chair_passwd=None, guest_join_uri=None, guest_passwd=None, audience_join_uri=None, audience_passwd=None):
        r"""OpenWebinarOngoingInfo

        The model defined in huaweicloud sdk

        :param online_attendee_count: 实时在线人数。
        :type online_attendee_count: int
        :param conf_uuid: 网络研讨会UUID。
        :type conf_uuid: str
        :param dept_name: 预订人部门名称。
        :type dept_name: str
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
        :param time_zone_id: 会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 &gt; * 举例：“timeZoneID”:\&quot;26\&quot;，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 
        :type time_zone_id: int
        :param scheduser_id: 网络研讨会预订者的用户UUID。
        :type scheduser_id: str
        :param scheduser_name: 预订者名称。
        :type scheduser_name: str
        :param vmr_pkg_name: 网络研讨会VMR名称。
        :type vmr_pkg_name: str
        :param chair_join_uri: 主持人入会地址。
        :type chair_join_uri: str
        :param chair_passwd: 主持人密码。
        :type chair_passwd: str
        :param guest_join_uri: 嘉宾入会地址。
        :type guest_join_uri: str
        :param guest_passwd: 嘉宾密码。
        :type guest_passwd: str
        :param audience_join_uri: 观众入会地址。
        :type audience_join_uri: str
        :param audience_passwd: 观众密码。
        :type audience_passwd: str
        """
        
        

        self._online_attendee_count = None
        self._conf_uuid = None
        self._dept_name = None
        self._conference_id = None
        self._corp_id = None
        self._subject = None
        self._description = None
        self._start_time = None
        self._time_zone_id = None
        self._scheduser_id = None
        self._scheduser_name = None
        self._vmr_pkg_name = None
        self._chair_join_uri = None
        self._chair_passwd = None
        self._guest_join_uri = None
        self._guest_passwd = None
        self._audience_join_uri = None
        self._audience_passwd = None
        self.discriminator = None

        if online_attendee_count is not None:
            self.online_attendee_count = online_attendee_count
        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if dept_name is not None:
            self.dept_name = dept_name
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
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if scheduser_id is not None:
            self.scheduser_id = scheduser_id
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
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

    @property
    def online_attendee_count(self):
        r"""Gets the online_attendee_count of this OpenWebinarOngoingInfo.

        实时在线人数。

        :return: The online_attendee_count of this OpenWebinarOngoingInfo.
        :rtype: int
        """
        return self._online_attendee_count

    @online_attendee_count.setter
    def online_attendee_count(self, online_attendee_count):
        r"""Sets the online_attendee_count of this OpenWebinarOngoingInfo.

        实时在线人数。

        :param online_attendee_count: The online_attendee_count of this OpenWebinarOngoingInfo.
        :type online_attendee_count: int
        """
        self._online_attendee_count = online_attendee_count

    @property
    def conf_uuid(self):
        r"""Gets the conf_uuid of this OpenWebinarOngoingInfo.

        网络研讨会UUID。

        :return: The conf_uuid of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        r"""Sets the conf_uuid of this OpenWebinarOngoingInfo.

        网络研讨会UUID。

        :param conf_uuid: The conf_uuid of this OpenWebinarOngoingInfo.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def dept_name(self):
        r"""Gets the dept_name of this OpenWebinarOngoingInfo.

        预订人部门名称。

        :return: The dept_name of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        r"""Sets the dept_name of this OpenWebinarOngoingInfo.

        预订人部门名称。

        :param dept_name: The dept_name of this OpenWebinarOngoingInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def conference_id(self):
        r"""Gets the conference_id of this OpenWebinarOngoingInfo.

        网络研讨会ID。

        :return: The conference_id of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        r"""Sets the conference_id of this OpenWebinarOngoingInfo.

        网络研讨会ID。

        :param conference_id: The conference_id of this OpenWebinarOngoingInfo.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def corp_id(self):
        r"""Gets the corp_id of this OpenWebinarOngoingInfo.

        企业ID。

        :return: The corp_id of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        r"""Sets the corp_id of this OpenWebinarOngoingInfo.

        企业ID。

        :param corp_id: The corp_id of this OpenWebinarOngoingInfo.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def subject(self):
        r"""Gets the subject of this OpenWebinarOngoingInfo.

        网络研讨会主题。

        :return: The subject of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this OpenWebinarOngoingInfo.

        网络研讨会主题。

        :param subject: The subject of this OpenWebinarOngoingInfo.
        :type subject: str
        """
        self._subject = subject

    @property
    def description(self):
        r"""Gets the description of this OpenWebinarOngoingInfo.

        网络研讨会描述。

        :return: The description of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpenWebinarOngoingInfo.

        网络研讨会描述。

        :param description: The description of this OpenWebinarOngoingInfo.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        r"""Gets the start_time of this OpenWebinarOngoingInfo.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :return: The start_time of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this OpenWebinarOngoingInfo.

        网络研讨会开始时间（UTC时间），格式“yyyy-MM-dd HH:mm”。

        :param start_time: The start_time of this OpenWebinarOngoingInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def time_zone_id(self):
        r"""Gets the time_zone_id of this OpenWebinarOngoingInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :return: The time_zone_id of this OpenWebinarOngoingInfo.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        r"""Sets the time_zone_id of this OpenWebinarOngoingInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :param time_zone_id: The time_zone_id of this OpenWebinarOngoingInfo.
        :type time_zone_id: int
        """
        self._time_zone_id = time_zone_id

    @property
    def scheduser_id(self):
        r"""Gets the scheduser_id of this OpenWebinarOngoingInfo.

        网络研讨会预订者的用户UUID。

        :return: The scheduser_id of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._scheduser_id

    @scheduser_id.setter
    def scheduser_id(self, scheduser_id):
        r"""Sets the scheduser_id of this OpenWebinarOngoingInfo.

        网络研讨会预订者的用户UUID。

        :param scheduser_id: The scheduser_id of this OpenWebinarOngoingInfo.
        :type scheduser_id: str
        """
        self._scheduser_id = scheduser_id

    @property
    def scheduser_name(self):
        r"""Gets the scheduser_name of this OpenWebinarOngoingInfo.

        预订者名称。

        :return: The scheduser_name of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        r"""Sets the scheduser_name of this OpenWebinarOngoingInfo.

        预订者名称。

        :param scheduser_name: The scheduser_name of this OpenWebinarOngoingInfo.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def vmr_pkg_name(self):
        r"""Gets the vmr_pkg_name of this OpenWebinarOngoingInfo.

        网络研讨会VMR名称。

        :return: The vmr_pkg_name of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        r"""Sets the vmr_pkg_name of this OpenWebinarOngoingInfo.

        网络研讨会VMR名称。

        :param vmr_pkg_name: The vmr_pkg_name of this OpenWebinarOngoingInfo.
        :type vmr_pkg_name: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def chair_join_uri(self):
        r"""Gets the chair_join_uri of this OpenWebinarOngoingInfo.

        主持人入会地址。

        :return: The chair_join_uri of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._chair_join_uri

    @chair_join_uri.setter
    def chair_join_uri(self, chair_join_uri):
        r"""Sets the chair_join_uri of this OpenWebinarOngoingInfo.

        主持人入会地址。

        :param chair_join_uri: The chair_join_uri of this OpenWebinarOngoingInfo.
        :type chair_join_uri: str
        """
        self._chair_join_uri = chair_join_uri

    @property
    def chair_passwd(self):
        r"""Gets the chair_passwd of this OpenWebinarOngoingInfo.

        主持人密码。

        :return: The chair_passwd of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._chair_passwd

    @chair_passwd.setter
    def chair_passwd(self, chair_passwd):
        r"""Sets the chair_passwd of this OpenWebinarOngoingInfo.

        主持人密码。

        :param chair_passwd: The chair_passwd of this OpenWebinarOngoingInfo.
        :type chair_passwd: str
        """
        self._chair_passwd = chair_passwd

    @property
    def guest_join_uri(self):
        r"""Gets the guest_join_uri of this OpenWebinarOngoingInfo.

        嘉宾入会地址。

        :return: The guest_join_uri of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._guest_join_uri

    @guest_join_uri.setter
    def guest_join_uri(self, guest_join_uri):
        r"""Sets the guest_join_uri of this OpenWebinarOngoingInfo.

        嘉宾入会地址。

        :param guest_join_uri: The guest_join_uri of this OpenWebinarOngoingInfo.
        :type guest_join_uri: str
        """
        self._guest_join_uri = guest_join_uri

    @property
    def guest_passwd(self):
        r"""Gets the guest_passwd of this OpenWebinarOngoingInfo.

        嘉宾密码。

        :return: The guest_passwd of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._guest_passwd

    @guest_passwd.setter
    def guest_passwd(self, guest_passwd):
        r"""Sets the guest_passwd of this OpenWebinarOngoingInfo.

        嘉宾密码。

        :param guest_passwd: The guest_passwd of this OpenWebinarOngoingInfo.
        :type guest_passwd: str
        """
        self._guest_passwd = guest_passwd

    @property
    def audience_join_uri(self):
        r"""Gets the audience_join_uri of this OpenWebinarOngoingInfo.

        观众入会地址。

        :return: The audience_join_uri of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._audience_join_uri

    @audience_join_uri.setter
    def audience_join_uri(self, audience_join_uri):
        r"""Sets the audience_join_uri of this OpenWebinarOngoingInfo.

        观众入会地址。

        :param audience_join_uri: The audience_join_uri of this OpenWebinarOngoingInfo.
        :type audience_join_uri: str
        """
        self._audience_join_uri = audience_join_uri

    @property
    def audience_passwd(self):
        r"""Gets the audience_passwd of this OpenWebinarOngoingInfo.

        观众密码。

        :return: The audience_passwd of this OpenWebinarOngoingInfo.
        :rtype: str
        """
        return self._audience_passwd

    @audience_passwd.setter
    def audience_passwd(self, audience_passwd):
        r"""Sets the audience_passwd of this OpenWebinarOngoingInfo.

        观众密码。

        :param audience_passwd: The audience_passwd of this OpenWebinarOngoingInfo.
        :type audience_passwd: str
        """
        self._audience_passwd = audience_passwd

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
        if not isinstance(other, OpenWebinarOngoingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
