# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestConfConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_send_notify': 'bool',
        'is_send_sms': 'bool',
        'is_send_calendar': 'bool',
        'is_auto_mute': 'bool',
        'is_hard_terminal_auto_mute': 'bool',
        'is_guest_free_pwd': 'bool',
        'call_in_restriction': 'int',
        'allow_guest_start_conf': 'bool',
        'guest_pwd': 'str',
        'vmr_id_type': 'int',
        'prolong_length': 'int',
        'enable_waiting_room': 'bool',
        'is_host_camera_on': 'bool',
        'is_guest_camera_on': 'bool'
    }

    attribute_map = {
        'is_send_notify': 'isSendNotify',
        'is_send_sms': 'isSendSms',
        'is_send_calendar': 'isSendCalendar',
        'is_auto_mute': 'isAutoMute',
        'is_hard_terminal_auto_mute': 'isHardTerminalAutoMute',
        'is_guest_free_pwd': 'isGuestFreePwd',
        'call_in_restriction': 'callInRestriction',
        'allow_guest_start_conf': 'allowGuestStartConf',
        'guest_pwd': 'guestPwd',
        'vmr_id_type': 'vmrIDType',
        'prolong_length': 'prolongLength',
        'enable_waiting_room': 'enableWaitingRoom',
        'is_host_camera_on': 'isHostCameraOn',
        'is_guest_camera_on': 'isGuestCameraOn'
    }

    def __init__(self, is_send_notify=None, is_send_sms=None, is_send_calendar=None, is_auto_mute=None, is_hard_terminal_auto_mute=None, is_guest_free_pwd=None, call_in_restriction=None, allow_guest_start_conf=None, guest_pwd=None, vmr_id_type=None, prolong_length=None, enable_waiting_room=None, is_host_camera_on=None, is_guest_camera_on=None):
        """RestConfConfigDTO

        The model defined in huaweicloud sdk

        :param is_send_notify: 是否需要发送会议邮件通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要
        :type is_send_notify: bool
        :param is_send_sms: 是否需要发送会议短信通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要 &gt; 只有正式商用企业才有发送会议短信通知的权限，免费企业即使isSendSms设置成true也不会发送会议短信通知。
        :type is_send_sms: bool
        :param is_send_calendar: 是否需要发送会议邮件日历通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要
        :type is_send_calendar: bool
        :param is_auto_mute: 来宾入会,软终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音
        :type is_auto_mute: bool
        :param is_hard_terminal_auto_mute: 来宾入会,硬终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音
        :type is_hard_terminal_auto_mute: bool
        :param is_guest_free_pwd: 是否来宾免密。 - true: 免密 - false: 需要密码 &gt; 仅随机会议ID的会议生效。
        :type is_guest_free_pwd: bool
        :param call_in_restriction: 允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户
        :type call_in_restriction: int
        :param allow_guest_start_conf: 是否允许来宾启动会议。 - true: 允许来宾启动会议 - false: 禁止来宾启动会议 &gt; 仅随机会议ID的会议生效。
        :type allow_guest_start_conf: bool
        :param guest_pwd: 来宾密码（4-16位长度的纯数字）。
        :type guest_pwd: str
        :param vmr_id_type: 云会议室的会议ID模式。 * 0：固定会议ID * 1：随机会议ID
        :type vmr_id_type: int
        :param prolong_length: 自动延长会议时长（取值范围0-60）。 * 0：表示会议到点自动结束，不延长会议 * 其他：表示自动延长的时长 &gt; * 自动结束会议是按照会议时长计算。比如预定的会议是9:00开始11:00结束，会议时长2个小时，如果与会者8:00就加入会议了，那会议在10:00就会自动结束 &gt; * 设置成其他值时，只要会中还有与会者，会议自动多次延长
        :type prolong_length: int
        :param enable_waiting_room: 开启或者关闭等候室。 * true：开启 * false：不开启
        :type enable_waiting_room: bool
        :param is_host_camera_on: 主持人入会是否开启摄像头。 * true：开启 * false：不开启
        :type is_host_camera_on: bool
        :param is_guest_camera_on: 来宾入会是否开启摄像头。 * true：开启 * false：不开启
        :type is_guest_camera_on: bool
        """
        
        

        self._is_send_notify = None
        self._is_send_sms = None
        self._is_send_calendar = None
        self._is_auto_mute = None
        self._is_hard_terminal_auto_mute = None
        self._is_guest_free_pwd = None
        self._call_in_restriction = None
        self._allow_guest_start_conf = None
        self._guest_pwd = None
        self._vmr_id_type = None
        self._prolong_length = None
        self._enable_waiting_room = None
        self._is_host_camera_on = None
        self._is_guest_camera_on = None
        self.discriminator = None

        if is_send_notify is not None:
            self.is_send_notify = is_send_notify
        if is_send_sms is not None:
            self.is_send_sms = is_send_sms
        if is_send_calendar is not None:
            self.is_send_calendar = is_send_calendar
        if is_auto_mute is not None:
            self.is_auto_mute = is_auto_mute
        if is_hard_terminal_auto_mute is not None:
            self.is_hard_terminal_auto_mute = is_hard_terminal_auto_mute
        if is_guest_free_pwd is not None:
            self.is_guest_free_pwd = is_guest_free_pwd
        if call_in_restriction is not None:
            self.call_in_restriction = call_in_restriction
        if allow_guest_start_conf is not None:
            self.allow_guest_start_conf = allow_guest_start_conf
        if guest_pwd is not None:
            self.guest_pwd = guest_pwd
        if vmr_id_type is not None:
            self.vmr_id_type = vmr_id_type
        if prolong_length is not None:
            self.prolong_length = prolong_length
        if enable_waiting_room is not None:
            self.enable_waiting_room = enable_waiting_room
        if is_host_camera_on is not None:
            self.is_host_camera_on = is_host_camera_on
        if is_guest_camera_on is not None:
            self.is_guest_camera_on = is_guest_camera_on

    @property
    def is_send_notify(self):
        """Gets the is_send_notify of this RestConfConfigDTO.

        是否需要发送会议邮件通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要

        :return: The is_send_notify of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_send_notify

    @is_send_notify.setter
    def is_send_notify(self, is_send_notify):
        """Sets the is_send_notify of this RestConfConfigDTO.

        是否需要发送会议邮件通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要

        :param is_send_notify: The is_send_notify of this RestConfConfigDTO.
        :type is_send_notify: bool
        """
        self._is_send_notify = is_send_notify

    @property
    def is_send_sms(self):
        """Gets the is_send_sms of this RestConfConfigDTO.

        是否需要发送会议短信通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要 > 只有正式商用企业才有发送会议短信通知的权限，免费企业即使isSendSms设置成true也不会发送会议短信通知。

        :return: The is_send_sms of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_send_sms

    @is_send_sms.setter
    def is_send_sms(self, is_send_sms):
        """Sets the is_send_sms of this RestConfConfigDTO.

        是否需要发送会议短信通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要 > 只有正式商用企业才有发送会议短信通知的权限，免费企业即使isSendSms设置成true也不会发送会议短信通知。

        :param is_send_sms: The is_send_sms of this RestConfConfigDTO.
        :type is_send_sms: bool
        """
        self._is_send_sms = is_send_sms

    @property
    def is_send_calendar(self):
        """Gets the is_send_calendar of this RestConfConfigDTO.

        是否需要发送会议邮件日历通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要

        :return: The is_send_calendar of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_send_calendar

    @is_send_calendar.setter
    def is_send_calendar(self, is_send_calendar):
        """Sets the is_send_calendar of this RestConfConfigDTO.

        是否需要发送会议邮件日历通知。默认值由企业级配置决定。 - true: 需要 - false: 不需要

        :param is_send_calendar: The is_send_calendar of this RestConfConfigDTO.
        :type is_send_calendar: bool
        """
        self._is_send_calendar = is_send_calendar

    @property
    def is_auto_mute(self):
        """Gets the is_auto_mute of this RestConfConfigDTO.

        来宾入会,软终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音

        :return: The is_auto_mute of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_auto_mute

    @is_auto_mute.setter
    def is_auto_mute(self, is_auto_mute):
        """Sets the is_auto_mute of this RestConfConfigDTO.

        来宾入会,软终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音

        :param is_auto_mute: The is_auto_mute of this RestConfConfigDTO.
        :type is_auto_mute: bool
        """
        self._is_auto_mute = is_auto_mute

    @property
    def is_hard_terminal_auto_mute(self):
        """Gets the is_hard_terminal_auto_mute of this RestConfConfigDTO.

        来宾入会,硬终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音

        :return: The is_hard_terminal_auto_mute of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_hard_terminal_auto_mute

    @is_hard_terminal_auto_mute.setter
    def is_hard_terminal_auto_mute(self, is_hard_terminal_auto_mute):
        """Sets the is_hard_terminal_auto_mute of this RestConfConfigDTO.

        来宾入会,硬终端是否自动静音。默认值由企业级配置决定。 - true: 自动静音 - false: 不自动静音

        :param is_hard_terminal_auto_mute: The is_hard_terminal_auto_mute of this RestConfConfigDTO.
        :type is_hard_terminal_auto_mute: bool
        """
        self._is_hard_terminal_auto_mute = is_hard_terminal_auto_mute

    @property
    def is_guest_free_pwd(self):
        """Gets the is_guest_free_pwd of this RestConfConfigDTO.

        是否来宾免密。 - true: 免密 - false: 需要密码 > 仅随机会议ID的会议生效。

        :return: The is_guest_free_pwd of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_guest_free_pwd

    @is_guest_free_pwd.setter
    def is_guest_free_pwd(self, is_guest_free_pwd):
        """Sets the is_guest_free_pwd of this RestConfConfigDTO.

        是否来宾免密。 - true: 免密 - false: 需要密码 > 仅随机会议ID的会议生效。

        :param is_guest_free_pwd: The is_guest_free_pwd of this RestConfConfigDTO.
        :type is_guest_free_pwd: bool
        """
        self._is_guest_free_pwd = is_guest_free_pwd

    @property
    def call_in_restriction(self):
        """Gets the call_in_restriction of this RestConfConfigDTO.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户

        :return: The call_in_restriction of this RestConfConfigDTO.
        :rtype: int
        """
        return self._call_in_restriction

    @call_in_restriction.setter
    def call_in_restriction(self, call_in_restriction):
        """Sets the call_in_restriction of this RestConfConfigDTO.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户

        :param call_in_restriction: The call_in_restriction of this RestConfConfigDTO.
        :type call_in_restriction: int
        """
        self._call_in_restriction = call_in_restriction

    @property
    def allow_guest_start_conf(self):
        """Gets the allow_guest_start_conf of this RestConfConfigDTO.

        是否允许来宾启动会议。 - true: 允许来宾启动会议 - false: 禁止来宾启动会议 > 仅随机会议ID的会议生效。

        :return: The allow_guest_start_conf of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._allow_guest_start_conf

    @allow_guest_start_conf.setter
    def allow_guest_start_conf(self, allow_guest_start_conf):
        """Sets the allow_guest_start_conf of this RestConfConfigDTO.

        是否允许来宾启动会议。 - true: 允许来宾启动会议 - false: 禁止来宾启动会议 > 仅随机会议ID的会议生效。

        :param allow_guest_start_conf: The allow_guest_start_conf of this RestConfConfigDTO.
        :type allow_guest_start_conf: bool
        """
        self._allow_guest_start_conf = allow_guest_start_conf

    @property
    def guest_pwd(self):
        """Gets the guest_pwd of this RestConfConfigDTO.

        来宾密码（4-16位长度的纯数字）。

        :return: The guest_pwd of this RestConfConfigDTO.
        :rtype: str
        """
        return self._guest_pwd

    @guest_pwd.setter
    def guest_pwd(self, guest_pwd):
        """Sets the guest_pwd of this RestConfConfigDTO.

        来宾密码（4-16位长度的纯数字）。

        :param guest_pwd: The guest_pwd of this RestConfConfigDTO.
        :type guest_pwd: str
        """
        self._guest_pwd = guest_pwd

    @property
    def vmr_id_type(self):
        """Gets the vmr_id_type of this RestConfConfigDTO.

        云会议室的会议ID模式。 * 0：固定会议ID * 1：随机会议ID

        :return: The vmr_id_type of this RestConfConfigDTO.
        :rtype: int
        """
        return self._vmr_id_type

    @vmr_id_type.setter
    def vmr_id_type(self, vmr_id_type):
        """Sets the vmr_id_type of this RestConfConfigDTO.

        云会议室的会议ID模式。 * 0：固定会议ID * 1：随机会议ID

        :param vmr_id_type: The vmr_id_type of this RestConfConfigDTO.
        :type vmr_id_type: int
        """
        self._vmr_id_type = vmr_id_type

    @property
    def prolong_length(self):
        """Gets the prolong_length of this RestConfConfigDTO.

        自动延长会议时长（取值范围0-60）。 * 0：表示会议到点自动结束，不延长会议 * 其他：表示自动延长的时长 > * 自动结束会议是按照会议时长计算。比如预定的会议是9:00开始11:00结束，会议时长2个小时，如果与会者8:00就加入会议了，那会议在10:00就会自动结束 > * 设置成其他值时，只要会中还有与会者，会议自动多次延长

        :return: The prolong_length of this RestConfConfigDTO.
        :rtype: int
        """
        return self._prolong_length

    @prolong_length.setter
    def prolong_length(self, prolong_length):
        """Sets the prolong_length of this RestConfConfigDTO.

        自动延长会议时长（取值范围0-60）。 * 0：表示会议到点自动结束，不延长会议 * 其他：表示自动延长的时长 > * 自动结束会议是按照会议时长计算。比如预定的会议是9:00开始11:00结束，会议时长2个小时，如果与会者8:00就加入会议了，那会议在10:00就会自动结束 > * 设置成其他值时，只要会中还有与会者，会议自动多次延长

        :param prolong_length: The prolong_length of this RestConfConfigDTO.
        :type prolong_length: int
        """
        self._prolong_length = prolong_length

    @property
    def enable_waiting_room(self):
        """Gets the enable_waiting_room of this RestConfConfigDTO.

        开启或者关闭等候室。 * true：开启 * false：不开启

        :return: The enable_waiting_room of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._enable_waiting_room

    @enable_waiting_room.setter
    def enable_waiting_room(self, enable_waiting_room):
        """Sets the enable_waiting_room of this RestConfConfigDTO.

        开启或者关闭等候室。 * true：开启 * false：不开启

        :param enable_waiting_room: The enable_waiting_room of this RestConfConfigDTO.
        :type enable_waiting_room: bool
        """
        self._enable_waiting_room = enable_waiting_room

    @property
    def is_host_camera_on(self):
        """Gets the is_host_camera_on of this RestConfConfigDTO.

        主持人入会是否开启摄像头。 * true：开启 * false：不开启

        :return: The is_host_camera_on of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_host_camera_on

    @is_host_camera_on.setter
    def is_host_camera_on(self, is_host_camera_on):
        """Sets the is_host_camera_on of this RestConfConfigDTO.

        主持人入会是否开启摄像头。 * true：开启 * false：不开启

        :param is_host_camera_on: The is_host_camera_on of this RestConfConfigDTO.
        :type is_host_camera_on: bool
        """
        self._is_host_camera_on = is_host_camera_on

    @property
    def is_guest_camera_on(self):
        """Gets the is_guest_camera_on of this RestConfConfigDTO.

        来宾入会是否开启摄像头。 * true：开启 * false：不开启

        :return: The is_guest_camera_on of this RestConfConfigDTO.
        :rtype: bool
        """
        return self._is_guest_camera_on

    @is_guest_camera_on.setter
    def is_guest_camera_on(self, is_guest_camera_on):
        """Sets the is_guest_camera_on of this RestConfConfigDTO.

        来宾入会是否开启摄像头。 * true：开启 * false：不开启

        :param is_guest_camera_on: The is_guest_camera_on of this RestConfConfigDTO.
        :type is_guest_camera_on: bool
        """
        self._is_guest_camera_on = is_guest_camera_on

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
        if not isinstance(other, RestConfConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
