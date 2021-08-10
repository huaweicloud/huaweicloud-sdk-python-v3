# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenScheduleConfReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subject': 'str',
        'description': 'str',
        'start_time': 'str',
        'duration': 'int',
        'time_zone_id': 'int',
        'attendees': 'list[OpenAttendeeEntity]',
        'notify_setting': 'OpenNotifySetting',
        'vmr_id': 'str',
        'guest_passwd': 'str',
        'audience_passwd': 'str',
        'call_restriction': 'bool',
        'scope': 'int',
        'audience_scope': 'int'
    }

    attribute_map = {
        'subject': 'subject',
        'description': 'description',
        'start_time': 'startTime',
        'duration': 'duration',
        'time_zone_id': 'timeZoneId',
        'attendees': 'attendees',
        'notify_setting': 'notifySetting',
        'vmr_id': 'vmrID',
        'guest_passwd': 'guestPasswd',
        'audience_passwd': 'audiencePasswd',
        'call_restriction': 'callRestriction',
        'scope': 'scope',
        'audience_scope': 'audienceScope'
    }

    def __init__(self, subject=None, description=None, start_time=None, duration=None, time_zone_id=None, attendees=None, notify_setting=None, vmr_id=None, guest_passwd=None, audience_passwd=None, call_restriction=None, scope=None, audience_scope=None):
        """OpenScheduleConfReq - a model defined in huaweicloud sdk"""
        
        

        self._subject = None
        self._description = None
        self._start_time = None
        self._duration = None
        self._time_zone_id = None
        self._attendees = None
        self._notify_setting = None
        self._vmr_id = None
        self._guest_passwd = None
        self._audience_passwd = None
        self._call_restriction = None
        self._scope = None
        self._audience_scope = None
        self.discriminator = None

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
        self.vmr_id = vmr_id
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

    @property
    def subject(self):
        """Gets the subject of this OpenScheduleConfReq.

        主题

        :return: The subject of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this OpenScheduleConfReq.

        主题

        :param subject: The subject of this OpenScheduleConfReq.
        :type: str
        """
        self._subject = subject

    @property
    def description(self):
        """Gets the description of this OpenScheduleConfReq.

        描述

        :return: The description of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenScheduleConfReq.

        描述

        :param description: The description of this OpenScheduleConfReq.
        :type: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this OpenScheduleConfReq.

        会议开始时间（UTC时间）， 格式：yyyy-MM-dd HH:mm。

        :return: The start_time of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OpenScheduleConfReq.

        会议开始时间（UTC时间）， 格式：yyyy-MM-dd HH:mm。

        :param start_time: The start_time of this OpenScheduleConfReq.
        :type: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this OpenScheduleConfReq.

        会议持续时长，单位分钟，取值范围[15,1440]。

        :return: The duration of this OpenScheduleConfReq.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OpenScheduleConfReq.

        会议持续时长，单位分钟，取值范围[15,1440]。

        :param duration: The duration of this OpenScheduleConfReq.
        :type: int
        """
        self._duration = duration

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this OpenScheduleConfReq.

        开始时间的时区信息。时区信息，参考时区映射关系。

        :return: The time_zone_id of this OpenScheduleConfReq.
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this OpenScheduleConfReq.

        开始时间的时区信息。时区信息，参考时区映射关系。

        :param time_zone_id: The time_zone_id of this OpenScheduleConfReq.
        :type: int
        """
        self._time_zone_id = time_zone_id

    @property
    def attendees(self):
        """Gets the attendees of this OpenScheduleConfReq.

        与会者列表。该列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。

        :return: The attendees of this OpenScheduleConfReq.
        :rtype: list[OpenAttendeeEntity]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this OpenScheduleConfReq.

        与会者列表。该列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。

        :param attendees: The attendees of this OpenScheduleConfReq.
        :type: list[OpenAttendeeEntity]
        """
        self._attendees = attendees

    @property
    def notify_setting(self):
        """Gets the notify_setting of this OpenScheduleConfReq.


        :return: The notify_setting of this OpenScheduleConfReq.
        :rtype: OpenNotifySetting
        """
        return self._notify_setting

    @notify_setting.setter
    def notify_setting(self, notify_setting):
        """Sets the notify_setting of this OpenScheduleConfReq.


        :param notify_setting: The notify_setting of this OpenScheduleConfReq.
        :type: OpenNotifySetting
        """
        self._notify_setting = notify_setting

    @property
    def vmr_id(self):
        """Gets the vmr_id of this OpenScheduleConfReq.

        VMR ID, 用于识别用户开会时绑定的云会议室。最大长度不超过128个字符。

        :return: The vmr_id of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this OpenScheduleConfReq.

        VMR ID, 用于识别用户开会时绑定的云会议室。最大长度不超过128个字符。

        :param vmr_id: The vmr_id of this OpenScheduleConfReq.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def guest_passwd(self):
        """Gets the guest_passwd of this OpenScheduleConfReq.

        自定义嘉宾入会密码, 4-16位数字，不能与观众密码相同；不指定则系统自动创建。

        :return: The guest_passwd of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._guest_passwd

    @guest_passwd.setter
    def guest_passwd(self, guest_passwd):
        """Sets the guest_passwd of this OpenScheduleConfReq.

        自定义嘉宾入会密码, 4-16位数字，不能与观众密码相同；不指定则系统自动创建。

        :param guest_passwd: The guest_passwd of this OpenScheduleConfReq.
        :type: str
        """
        self._guest_passwd = guest_passwd

    @property
    def audience_passwd(self):
        """Gets the audience_passwd of this OpenScheduleConfReq.

        自定义观众入会密码, 4-16位数字，不能与嘉宾密码相同；不指定则系统自动创建。

        :return: The audience_passwd of this OpenScheduleConfReq.
        :rtype: str
        """
        return self._audience_passwd

    @audience_passwd.setter
    def audience_passwd(self, audience_passwd):
        """Sets the audience_passwd of this OpenScheduleConfReq.

        自定义观众入会密码, 4-16位数字，不能与嘉宾密码相同；不指定则系统自动创建。

        :param audience_passwd: The audience_passwd of this OpenScheduleConfReq.
        :type: str
        """
        self._audience_passwd = audience_passwd

    @property
    def call_restriction(self):
        """Gets the call_restriction of this OpenScheduleConfReq.

        入会范围开关

        :return: The call_restriction of this OpenScheduleConfReq.
        :rtype: bool
        """
        return self._call_restriction

    @call_restriction.setter
    def call_restriction(self, call_restriction):
        """Sets the call_restriction of this OpenScheduleConfReq.

        入会范围开关

        :param call_restriction: The call_restriction of this OpenScheduleConfReq.
        :type: bool
        """
        self._call_restriction = call_restriction

    @property
    def scope(self):
        """Gets the scope of this OpenScheduleConfReq.

        主持人、嘉宾入会范围  0: 所有用户 1: 非匿名用户（手机pstn入会视为匿名入会） 2: 企业内用户 3: 被邀请用户; 默认值 0。

        :return: The scope of this OpenScheduleConfReq.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OpenScheduleConfReq.

        主持人、嘉宾入会范围  0: 所有用户 1: 非匿名用户（手机pstn入会视为匿名入会） 2: 企业内用户 3: 被邀请用户; 默认值 0。

        :param scope: The scope of this OpenScheduleConfReq.
        :type: int
        """
        self._scope = scope

    @property
    def audience_scope(self):
        """Gets the audience_scope of this OpenScheduleConfReq.

        观众入会范围 0: 所有用户 2: 企业内用户和被邀请用户; 默认值 0。

        :return: The audience_scope of this OpenScheduleConfReq.
        :rtype: int
        """
        return self._audience_scope

    @audience_scope.setter
    def audience_scope(self, audience_scope):
        """Sets the audience_scope of this OpenScheduleConfReq.

        观众入会范围 0: 所有用户 2: 企业内用户和被邀请用户; 默认值 0。

        :param audience_scope: The audience_scope of this OpenScheduleConfReq.
        :type: int
        """
        self._audience_scope = audience_scope

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
        if not isinstance(other, OpenScheduleConfReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
