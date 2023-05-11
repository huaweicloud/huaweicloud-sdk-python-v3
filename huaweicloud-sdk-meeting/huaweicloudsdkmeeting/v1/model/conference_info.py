# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConferenceInfo:

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
        'size': 'int',
        'time_zone_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'media_types': 'str',
        'conference_state': 'str',
        'language': 'str',
        'access_number': 'str',
        'password_entry': 'list[PasswordEntry]',
        'user_uuid': 'str',
        'scheduser_name': 'str',
        'conference_type': 'int',
        'conf_type': 'str',
        'cycle_params': 'CycleParams',
        'is_auto_mute': 'int',
        'is_auto_record': 'int',
        'chair_join_uri': 'str',
        'guest_join_uri': 'str',
        'audience_join_uri': 'str',
        'record_type': 'int',
        'aux_address': 'str',
        'live_address': 'str',
        'record_aux_stream': 'int',
        'record_auth_type': 'int',
        'live_url': 'str',
        'conf_config_info': 'RestConfConfigDTO',
        'vmr_flag': 'int',
        'is_has_record_file': 'bool',
        'vmr_conference_id': 'str',
        'conf_uuid': 'str',
        'part_attendee_info': 'list[PartAttendee]',
        'terminl_count': 'int',
        'normal_count': 'int',
        'dept_name': 'str',
        'vmr_id': 'str',
        'role': 'str',
        'webinar': 'bool',
        'online_attendee_amount': 'int',
        'multi_stream_flag': 'int',
        'conf_mode': 'str',
        'schedule_vmr': 'bool',
        'concurrent_participants': 'int',
        'pic_display': 'MultiPicDisplayDO',
        'sub_confs': 'list[CycleSubConf]',
        'cycle_sub_conf_id': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'subject': 'subject',
        'size': 'size',
        'time_zone_id': 'timeZoneID',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'media_types': 'mediaTypes',
        'conference_state': 'conferenceState',
        'language': 'language',
        'access_number': 'accessNumber',
        'password_entry': 'passwordEntry',
        'user_uuid': 'userUUID',
        'scheduser_name': 'scheduserName',
        'conference_type': 'conferenceType',
        'conf_type': 'confType',
        'cycle_params': 'cycleParams',
        'is_auto_mute': 'isAutoMute',
        'is_auto_record': 'isAutoRecord',
        'chair_join_uri': 'chairJoinUri',
        'guest_join_uri': 'guestJoinUri',
        'audience_join_uri': 'audienceJoinUri',
        'record_type': 'recordType',
        'aux_address': 'auxAddress',
        'live_address': 'liveAddress',
        'record_aux_stream': 'recordAuxStream',
        'record_auth_type': 'recordAuthType',
        'live_url': 'liveUrl',
        'conf_config_info': 'confConfigInfo',
        'vmr_flag': 'vmrFlag',
        'is_has_record_file': 'isHasRecordFile',
        'vmr_conference_id': 'vmrConferenceID',
        'conf_uuid': 'confUUID',
        'part_attendee_info': 'partAttendeeInfo',
        'terminl_count': 'terminlCount',
        'normal_count': 'normalCount',
        'dept_name': 'deptName',
        'vmr_id': 'vmrID',
        'role': 'role',
        'webinar': 'webinar',
        'online_attendee_amount': 'onlineAttendeeAmount',
        'multi_stream_flag': 'multiStreamFlag',
        'conf_mode': 'confMode',
        'schedule_vmr': 'scheduleVmr',
        'concurrent_participants': 'concurrentParticipants',
        'pic_display': 'picDisplay',
        'sub_confs': 'subConfs',
        'cycle_sub_conf_id': 'cycleSubConfID'
    }

    def __init__(self, conference_id=None, subject=None, size=None, time_zone_id=None, start_time=None, end_time=None, media_types=None, conference_state=None, language=None, access_number=None, password_entry=None, user_uuid=None, scheduser_name=None, conference_type=None, conf_type=None, cycle_params=None, is_auto_mute=None, is_auto_record=None, chair_join_uri=None, guest_join_uri=None, audience_join_uri=None, record_type=None, aux_address=None, live_address=None, record_aux_stream=None, record_auth_type=None, live_url=None, conf_config_info=None, vmr_flag=None, is_has_record_file=None, vmr_conference_id=None, conf_uuid=None, part_attendee_info=None, terminl_count=None, normal_count=None, dept_name=None, vmr_id=None, role=None, webinar=None, online_attendee_amount=None, multi_stream_flag=None, conf_mode=None, schedule_vmr=None, concurrent_participants=None, pic_display=None, sub_confs=None, cycle_sub_conf_id=None):
        """ConferenceInfo

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。
        :type conference_id: str
        :param subject: 会议主题。
        :type subject: str
        :param size: 会议预约时添加的会议者数量。
        :type size: int
        :param time_zone_id: 会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。
        :type time_zone_id: str
        :param start_time: 会议起始时间 (YYYY-MM-DD HH:MM )。
        :type start_time: str
        :param end_time: 会议结束时间 (YYYY-MM-DD HH:MM )。
        :type end_time: str
        :param media_types: 会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔。 - Voice: 语音 - Video: 标清视频 - HDVideo: 高清视频 - Data: 数据
        :type media_types: str
        :param conference_state: 会议状态。 - Schedule: 预定状态 - Creating: 正在创建状态 - Created: 会议已经被创建，并正在召开 - Destroyed: 会议已经关闭
        :type conference_state: str
        :param language: 会议通知短信或邮件的语言。默认中文。 * zh-CN：中文 * en-US：英文 
        :type language: str
        :param access_number: 会议接入的SIP号码。
        :type access_number: str
        :param password_entry: 会议密码。 &gt; * 创建会议时，返回主持人密码和来宾密码 &gt; * 主持人查询会议时，返回主持人密码和来宾密码来 &gt; * 宾查询会议时，返回来宾密码
        :type password_entry: list[:class:`huaweicloudsdkmeeting.v1.PasswordEntry`]
        :param user_uuid: 会议预订者的用户UUID。
        :type user_uuid: str
        :param scheduser_name: 会议预订者名称。
        :type scheduser_name: str
        :param conference_type: 会议类型。 - 0: 普通会议 - 2: 周期性会议
        :type conference_type: int
        :param conf_type: 会议类型。 - FUTURE：将来开始的会议（创建时） - IMMEDIATELY：立即开始的会议（创建时） - CYCLE：周期会议
        :type conf_type: str
        :param cycle_params: 
        :type cycle_params: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        :param is_auto_mute: 是否入会自动静音。 - 0: 不自动静音 - 1: 自动静音
        :type is_auto_mute: int
        :param is_auto_record: 是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动
        :type is_auto_record: int
        :param chair_join_uri: 主持人会议链接地址。
        :type chair_join_uri: str
        :param guest_join_uri: 普通与会者会议链接地址。
        :type guest_join_uri: str
        :param audience_join_uri: 网络研讨会观众会议链接地址。
        :type audience_join_uri: str
        :param record_type: 录播类型。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播
        :type record_type: int
        :param aux_address: 辅流直播推流地址。
        :type aux_address: str
        :param live_address: 主流直播推流地址。
        :type live_address: str
        :param record_aux_stream: 是否录制辅流。  - 0: 否  - 1: 是
        :type record_aux_stream: int
        :param record_auth_type: 观看/下载录播的鉴权方式。  - 0: 可通过链接观看/下载  - 1: 企业用户可观看/下载  - 2: 与会者可观看/下载
        :type record_auth_type: int
        :param live_url: 直播观看地址。
        :type live_url: str
        :param conf_config_info: 
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        :param vmr_flag: 是否使用云会议室或个人会议ID召开预约会议。 - 0: 不使用云会议室或个人会议ID - 1: 使用云会议室或个人会议ID
        :type vmr_flag: int
        :param is_has_record_file: 是否有会议录制文件。仅历史会议查询时返回。 - true: 有录制文件 - false: 没有录制文件
        :type is_has_record_file: bool
        :param vmr_conference_id: 云会议室会议ID或个人会议ID，如果vmrFlag为\&quot;1\&quot;，则该字段不为空。
        :type vmr_conference_id: str
        :param conf_uuid: 会议的UUID。 &gt; * 只有创建立即开始的会议才返回UUID，如果是预约未来的会议，不会返回UUID &gt; * 可以通过[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)获取历史会议的UUID 
        :type conf_uuid: str
        :param part_attendee_info: 被邀请的部分与会者信息。 &gt; * 只返回被邀请的前20条软终端与会者信息和前20条硬终端与会者信息 &gt; * 不返回会中主动加入的与会者信息 &gt; * “[[查询会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0017.html)](tag:hws)[[查询会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0017.html)](tag:hk)”和“[[查询会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0018.html)](tag:hws)[[查询会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0018.html)](tag:hk)”接口，返回预约会议时邀请的与会者和会中主持人邀请的与会者 &gt; * “[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”、“[[查询在线会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0026.html)](tag:hws)[[查询在线会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0026.html)](tag:hk)”、“[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)”和“[[查询历史会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0052.html)](tag:hws)[[查询历史会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0052.html)](tag:hk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ”接口返回预约会议时邀请的与会者。不返回会中主持人邀请的与会者 
        :type part_attendee_info: list[:class:`huaweicloudsdkmeeting.v1.PartAttendee`]
        :param terminl_count: 硬终端个数，如IdeaHub，TE30等。
        :type terminl_count: int
        :param normal_count: 软终端个数，如PC端、手机端App等。
        :type normal_count: int
        :param dept_name: 会议预定者的企业名称。
        :type dept_name: str
        :param vmr_id: 云会议室的ID。
        :type vmr_id: str
        :param role: 与会者角色。 * chair ：主持人 * general ：来宾 * audience ： 观众 &gt; * 仅在查询会议详情时返回 &gt; * 返回查询者本身的角色 
        :type role: str
        :param webinar: 是否是网络研讨会。
        :type webinar: bool
        :param online_attendee_amount: 当前在线与会人数。包含被邀入会和主动入会的与会者。 &gt; 仅在“[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”接口中返回。 
        :type online_attendee_amount: int
        :param multi_stream_flag: 标识是否为多流视频会议。 * 1：多流会议 
        :type multi_stream_flag: int
        :param conf_mode: 会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 
        :type conf_mode: str
        :param schedule_vmr: VMR预约记录。 true: VMR预约记录 false：普通会议 &gt; 该参数将废弃，请勿使用。 
        :type schedule_vmr: bool
        :param concurrent_participants: 会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 
        :type concurrent_participants: int
        :param pic_display: 
        :type pic_display: :class:`huaweicloudsdkmeeting.v1.MultiPicDisplayDO`
        :param sub_confs: 周期子会议列表。
        :type sub_confs: list[:class:`huaweicloudsdkmeeting.v1.CycleSubConf`]
        :param cycle_sub_conf_id: 第一个周期子会议的UUID。
        :type cycle_sub_conf_id: str
        """
        
        

        self._conference_id = None
        self._subject = None
        self._size = None
        self._time_zone_id = None
        self._start_time = None
        self._end_time = None
        self._media_types = None
        self._conference_state = None
        self._language = None
        self._access_number = None
        self._password_entry = None
        self._user_uuid = None
        self._scheduser_name = None
        self._conference_type = None
        self._conf_type = None
        self._cycle_params = None
        self._is_auto_mute = None
        self._is_auto_record = None
        self._chair_join_uri = None
        self._guest_join_uri = None
        self._audience_join_uri = None
        self._record_type = None
        self._aux_address = None
        self._live_address = None
        self._record_aux_stream = None
        self._record_auth_type = None
        self._live_url = None
        self._conf_config_info = None
        self._vmr_flag = None
        self._is_has_record_file = None
        self._vmr_conference_id = None
        self._conf_uuid = None
        self._part_attendee_info = None
        self._terminl_count = None
        self._normal_count = None
        self._dept_name = None
        self._vmr_id = None
        self._role = None
        self._webinar = None
        self._online_attendee_amount = None
        self._multi_stream_flag = None
        self._conf_mode = None
        self._schedule_vmr = None
        self._concurrent_participants = None
        self._pic_display = None
        self._sub_confs = None
        self._cycle_sub_conf_id = None
        self.discriminator = None

        if conference_id is not None:
            self.conference_id = conference_id
        if subject is not None:
            self.subject = subject
        if size is not None:
            self.size = size
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if media_types is not None:
            self.media_types = media_types
        if conference_state is not None:
            self.conference_state = conference_state
        if language is not None:
            self.language = language
        if access_number is not None:
            self.access_number = access_number
        if password_entry is not None:
            self.password_entry = password_entry
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if conference_type is not None:
            self.conference_type = conference_type
        if conf_type is not None:
            self.conf_type = conf_type
        if cycle_params is not None:
            self.cycle_params = cycle_params
        if is_auto_mute is not None:
            self.is_auto_mute = is_auto_mute
        if is_auto_record is not None:
            self.is_auto_record = is_auto_record
        if chair_join_uri is not None:
            self.chair_join_uri = chair_join_uri
        if guest_join_uri is not None:
            self.guest_join_uri = guest_join_uri
        if audience_join_uri is not None:
            self.audience_join_uri = audience_join_uri
        if record_type is not None:
            self.record_type = record_type
        if aux_address is not None:
            self.aux_address = aux_address
        if live_address is not None:
            self.live_address = live_address
        if record_aux_stream is not None:
            self.record_aux_stream = record_aux_stream
        if record_auth_type is not None:
            self.record_auth_type = record_auth_type
        if live_url is not None:
            self.live_url = live_url
        if conf_config_info is not None:
            self.conf_config_info = conf_config_info
        if vmr_flag is not None:
            self.vmr_flag = vmr_flag
        if is_has_record_file is not None:
            self.is_has_record_file = is_has_record_file
        if vmr_conference_id is not None:
            self.vmr_conference_id = vmr_conference_id
        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if part_attendee_info is not None:
            self.part_attendee_info = part_attendee_info
        if terminl_count is not None:
            self.terminl_count = terminl_count
        if normal_count is not None:
            self.normal_count = normal_count
        if dept_name is not None:
            self.dept_name = dept_name
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if role is not None:
            self.role = role
        if webinar is not None:
            self.webinar = webinar
        if online_attendee_amount is not None:
            self.online_attendee_amount = online_attendee_amount
        if multi_stream_flag is not None:
            self.multi_stream_flag = multi_stream_flag
        if conf_mode is not None:
            self.conf_mode = conf_mode
        if schedule_vmr is not None:
            self.schedule_vmr = schedule_vmr
        if concurrent_participants is not None:
            self.concurrent_participants = concurrent_participants
        if pic_display is not None:
            self.pic_display = pic_display
        if sub_confs is not None:
            self.sub_confs = sub_confs
        if cycle_sub_conf_id is not None:
            self.cycle_sub_conf_id = cycle_sub_conf_id

    @property
    def conference_id(self):
        """Gets the conference_id of this ConferenceInfo.

        会议ID。

        :return: The conference_id of this ConferenceInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this ConferenceInfo.

        会议ID。

        :param conference_id: The conference_id of this ConferenceInfo.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def subject(self):
        """Gets the subject of this ConferenceInfo.

        会议主题。

        :return: The subject of this ConferenceInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ConferenceInfo.

        会议主题。

        :param subject: The subject of this ConferenceInfo.
        :type subject: str
        """
        self._subject = subject

    @property
    def size(self):
        """Gets the size of this ConferenceInfo.

        会议预约时添加的会议者数量。

        :return: The size of this ConferenceInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ConferenceInfo.

        会议预约时添加的会议者数量。

        :param size: The size of this ConferenceInfo.
        :type size: int
        """
        self._size = size

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this ConferenceInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。

        :return: The time_zone_id of this ConferenceInfo.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this ConferenceInfo.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。

        :param time_zone_id: The time_zone_id of this ConferenceInfo.
        :type time_zone_id: str
        """
        self._time_zone_id = time_zone_id

    @property
    def start_time(self):
        """Gets the start_time of this ConferenceInfo.

        会议起始时间 (YYYY-MM-DD HH:MM )。

        :return: The start_time of this ConferenceInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ConferenceInfo.

        会议起始时间 (YYYY-MM-DD HH:MM )。

        :param start_time: The start_time of this ConferenceInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ConferenceInfo.

        会议结束时间 (YYYY-MM-DD HH:MM )。

        :return: The end_time of this ConferenceInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ConferenceInfo.

        会议结束时间 (YYYY-MM-DD HH:MM )。

        :param end_time: The end_time of this ConferenceInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def media_types(self):
        """Gets the media_types of this ConferenceInfo.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔。 - Voice: 语音 - Video: 标清视频 - HDVideo: 高清视频 - Data: 数据

        :return: The media_types of this ConferenceInfo.
        :rtype: str
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this ConferenceInfo.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔。 - Voice: 语音 - Video: 标清视频 - HDVideo: 高清视频 - Data: 数据

        :param media_types: The media_types of this ConferenceInfo.
        :type media_types: str
        """
        self._media_types = media_types

    @property
    def conference_state(self):
        """Gets the conference_state of this ConferenceInfo.

        会议状态。 - Schedule: 预定状态 - Creating: 正在创建状态 - Created: 会议已经被创建，并正在召开 - Destroyed: 会议已经关闭

        :return: The conference_state of this ConferenceInfo.
        :rtype: str
        """
        return self._conference_state

    @conference_state.setter
    def conference_state(self, conference_state):
        """Sets the conference_state of this ConferenceInfo.

        会议状态。 - Schedule: 预定状态 - Creating: 正在创建状态 - Created: 会议已经被创建，并正在召开 - Destroyed: 会议已经关闭

        :param conference_state: The conference_state of this ConferenceInfo.
        :type conference_state: str
        """
        self._conference_state = conference_state

    @property
    def language(self):
        """Gets the language of this ConferenceInfo.

        会议通知短信或邮件的语言。默认中文。 * zh-CN：中文 * en-US：英文 

        :return: The language of this ConferenceInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConferenceInfo.

        会议通知短信或邮件的语言。默认中文。 * zh-CN：中文 * en-US：英文 

        :param language: The language of this ConferenceInfo.
        :type language: str
        """
        self._language = language

    @property
    def access_number(self):
        """Gets the access_number of this ConferenceInfo.

        会议接入的SIP号码。

        :return: The access_number of this ConferenceInfo.
        :rtype: str
        """
        return self._access_number

    @access_number.setter
    def access_number(self, access_number):
        """Sets the access_number of this ConferenceInfo.

        会议接入的SIP号码。

        :param access_number: The access_number of this ConferenceInfo.
        :type access_number: str
        """
        self._access_number = access_number

    @property
    def password_entry(self):
        """Gets the password_entry of this ConferenceInfo.

        会议密码。 > * 创建会议时，返回主持人密码和来宾密码 > * 主持人查询会议时，返回主持人密码和来宾密码来 > * 宾查询会议时，返回来宾密码

        :return: The password_entry of this ConferenceInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PasswordEntry`]
        """
        return self._password_entry

    @password_entry.setter
    def password_entry(self, password_entry):
        """Sets the password_entry of this ConferenceInfo.

        会议密码。 > * 创建会议时，返回主持人密码和来宾密码 > * 主持人查询会议时，返回主持人密码和来宾密码来 > * 宾查询会议时，返回来宾密码

        :param password_entry: The password_entry of this ConferenceInfo.
        :type password_entry: list[:class:`huaweicloudsdkmeeting.v1.PasswordEntry`]
        """
        self._password_entry = password_entry

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ConferenceInfo.

        会议预订者的用户UUID。

        :return: The user_uuid of this ConferenceInfo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ConferenceInfo.

        会议预订者的用户UUID。

        :param user_uuid: The user_uuid of this ConferenceInfo.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this ConferenceInfo.

        会议预订者名称。

        :return: The scheduser_name of this ConferenceInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this ConferenceInfo.

        会议预订者名称。

        :param scheduser_name: The scheduser_name of this ConferenceInfo.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def conference_type(self):
        """Gets the conference_type of this ConferenceInfo.

        会议类型。 - 0: 普通会议 - 2: 周期性会议

        :return: The conference_type of this ConferenceInfo.
        :rtype: int
        """
        return self._conference_type

    @conference_type.setter
    def conference_type(self, conference_type):
        """Sets the conference_type of this ConferenceInfo.

        会议类型。 - 0: 普通会议 - 2: 周期性会议

        :param conference_type: The conference_type of this ConferenceInfo.
        :type conference_type: int
        """
        self._conference_type = conference_type

    @property
    def conf_type(self):
        """Gets the conf_type of this ConferenceInfo.

        会议类型。 - FUTURE：将来开始的会议（创建时） - IMMEDIATELY：立即开始的会议（创建时） - CYCLE：周期会议

        :return: The conf_type of this ConferenceInfo.
        :rtype: str
        """
        return self._conf_type

    @conf_type.setter
    def conf_type(self, conf_type):
        """Sets the conf_type of this ConferenceInfo.

        会议类型。 - FUTURE：将来开始的会议（创建时） - IMMEDIATELY：立即开始的会议（创建时） - CYCLE：周期会议

        :param conf_type: The conf_type of this ConferenceInfo.
        :type conf_type: str
        """
        self._conf_type = conf_type

    @property
    def cycle_params(self):
        """Gets the cycle_params of this ConferenceInfo.

        :return: The cycle_params of this ConferenceInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        """
        return self._cycle_params

    @cycle_params.setter
    def cycle_params(self, cycle_params):
        """Sets the cycle_params of this ConferenceInfo.

        :param cycle_params: The cycle_params of this ConferenceInfo.
        :type cycle_params: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        """
        self._cycle_params = cycle_params

    @property
    def is_auto_mute(self):
        """Gets the is_auto_mute of this ConferenceInfo.

        是否入会自动静音。 - 0: 不自动静音 - 1: 自动静音

        :return: The is_auto_mute of this ConferenceInfo.
        :rtype: int
        """
        return self._is_auto_mute

    @is_auto_mute.setter
    def is_auto_mute(self, is_auto_mute):
        """Sets the is_auto_mute of this ConferenceInfo.

        是否入会自动静音。 - 0: 不自动静音 - 1: 自动静音

        :param is_auto_mute: The is_auto_mute of this ConferenceInfo.
        :type is_auto_mute: int
        """
        self._is_auto_mute = is_auto_mute

    @property
    def is_auto_record(self):
        """Gets the is_auto_record of this ConferenceInfo.

        是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动

        :return: The is_auto_record of this ConferenceInfo.
        :rtype: int
        """
        return self._is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, is_auto_record):
        """Sets the is_auto_record of this ConferenceInfo.

        是否自动开启云录制。 - 0: 不自动启动 - 1: 自动启动

        :param is_auto_record: The is_auto_record of this ConferenceInfo.
        :type is_auto_record: int
        """
        self._is_auto_record = is_auto_record

    @property
    def chair_join_uri(self):
        """Gets the chair_join_uri of this ConferenceInfo.

        主持人会议链接地址。

        :return: The chair_join_uri of this ConferenceInfo.
        :rtype: str
        """
        return self._chair_join_uri

    @chair_join_uri.setter
    def chair_join_uri(self, chair_join_uri):
        """Sets the chair_join_uri of this ConferenceInfo.

        主持人会议链接地址。

        :param chair_join_uri: The chair_join_uri of this ConferenceInfo.
        :type chair_join_uri: str
        """
        self._chair_join_uri = chair_join_uri

    @property
    def guest_join_uri(self):
        """Gets the guest_join_uri of this ConferenceInfo.

        普通与会者会议链接地址。

        :return: The guest_join_uri of this ConferenceInfo.
        :rtype: str
        """
        return self._guest_join_uri

    @guest_join_uri.setter
    def guest_join_uri(self, guest_join_uri):
        """Sets the guest_join_uri of this ConferenceInfo.

        普通与会者会议链接地址。

        :param guest_join_uri: The guest_join_uri of this ConferenceInfo.
        :type guest_join_uri: str
        """
        self._guest_join_uri = guest_join_uri

    @property
    def audience_join_uri(self):
        """Gets the audience_join_uri of this ConferenceInfo.

        网络研讨会观众会议链接地址。

        :return: The audience_join_uri of this ConferenceInfo.
        :rtype: str
        """
        return self._audience_join_uri

    @audience_join_uri.setter
    def audience_join_uri(self, audience_join_uri):
        """Sets the audience_join_uri of this ConferenceInfo.

        网络研讨会观众会议链接地址。

        :param audience_join_uri: The audience_join_uri of this ConferenceInfo.
        :type audience_join_uri: str
        """
        self._audience_join_uri = audience_join_uri

    @property
    def record_type(self):
        """Gets the record_type of this ConferenceInfo.

        录播类型。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播

        :return: The record_type of this ConferenceInfo.
        :rtype: int
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this ConferenceInfo.

        录播类型。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播

        :param record_type: The record_type of this ConferenceInfo.
        :type record_type: int
        """
        self._record_type = record_type

    @property
    def aux_address(self):
        """Gets the aux_address of this ConferenceInfo.

        辅流直播推流地址。

        :return: The aux_address of this ConferenceInfo.
        :rtype: str
        """
        return self._aux_address

    @aux_address.setter
    def aux_address(self, aux_address):
        """Sets the aux_address of this ConferenceInfo.

        辅流直播推流地址。

        :param aux_address: The aux_address of this ConferenceInfo.
        :type aux_address: str
        """
        self._aux_address = aux_address

    @property
    def live_address(self):
        """Gets the live_address of this ConferenceInfo.

        主流直播推流地址。

        :return: The live_address of this ConferenceInfo.
        :rtype: str
        """
        return self._live_address

    @live_address.setter
    def live_address(self, live_address):
        """Sets the live_address of this ConferenceInfo.

        主流直播推流地址。

        :param live_address: The live_address of this ConferenceInfo.
        :type live_address: str
        """
        self._live_address = live_address

    @property
    def record_aux_stream(self):
        """Gets the record_aux_stream of this ConferenceInfo.

        是否录制辅流。  - 0: 否  - 1: 是

        :return: The record_aux_stream of this ConferenceInfo.
        :rtype: int
        """
        return self._record_aux_stream

    @record_aux_stream.setter
    def record_aux_stream(self, record_aux_stream):
        """Sets the record_aux_stream of this ConferenceInfo.

        是否录制辅流。  - 0: 否  - 1: 是

        :param record_aux_stream: The record_aux_stream of this ConferenceInfo.
        :type record_aux_stream: int
        """
        self._record_aux_stream = record_aux_stream

    @property
    def record_auth_type(self):
        """Gets the record_auth_type of this ConferenceInfo.

        观看/下载录播的鉴权方式。  - 0: 可通过链接观看/下载  - 1: 企业用户可观看/下载  - 2: 与会者可观看/下载

        :return: The record_auth_type of this ConferenceInfo.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        """Sets the record_auth_type of this ConferenceInfo.

        观看/下载录播的鉴权方式。  - 0: 可通过链接观看/下载  - 1: 企业用户可观看/下载  - 2: 与会者可观看/下载

        :param record_auth_type: The record_auth_type of this ConferenceInfo.
        :type record_auth_type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def live_url(self):
        """Gets the live_url of this ConferenceInfo.

        直播观看地址。

        :return: The live_url of this ConferenceInfo.
        :rtype: str
        """
        return self._live_url

    @live_url.setter
    def live_url(self, live_url):
        """Sets the live_url of this ConferenceInfo.

        直播观看地址。

        :param live_url: The live_url of this ConferenceInfo.
        :type live_url: str
        """
        self._live_url = live_url

    @property
    def conf_config_info(self):
        """Gets the conf_config_info of this ConferenceInfo.

        :return: The conf_config_info of this ConferenceInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        """Sets the conf_config_info of this ConferenceInfo.

        :param conf_config_info: The conf_config_info of this ConferenceInfo.
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        """
        self._conf_config_info = conf_config_info

    @property
    def vmr_flag(self):
        """Gets the vmr_flag of this ConferenceInfo.

        是否使用云会议室或个人会议ID召开预约会议。 - 0: 不使用云会议室或个人会议ID - 1: 使用云会议室或个人会议ID

        :return: The vmr_flag of this ConferenceInfo.
        :rtype: int
        """
        return self._vmr_flag

    @vmr_flag.setter
    def vmr_flag(self, vmr_flag):
        """Sets the vmr_flag of this ConferenceInfo.

        是否使用云会议室或个人会议ID召开预约会议。 - 0: 不使用云会议室或个人会议ID - 1: 使用云会议室或个人会议ID

        :param vmr_flag: The vmr_flag of this ConferenceInfo.
        :type vmr_flag: int
        """
        self._vmr_flag = vmr_flag

    @property
    def is_has_record_file(self):
        """Gets the is_has_record_file of this ConferenceInfo.

        是否有会议录制文件。仅历史会议查询时返回。 - true: 有录制文件 - false: 没有录制文件

        :return: The is_has_record_file of this ConferenceInfo.
        :rtype: bool
        """
        return self._is_has_record_file

    @is_has_record_file.setter
    def is_has_record_file(self, is_has_record_file):
        """Sets the is_has_record_file of this ConferenceInfo.

        是否有会议录制文件。仅历史会议查询时返回。 - true: 有录制文件 - false: 没有录制文件

        :param is_has_record_file: The is_has_record_file of this ConferenceInfo.
        :type is_has_record_file: bool
        """
        self._is_has_record_file = is_has_record_file

    @property
    def vmr_conference_id(self):
        """Gets the vmr_conference_id of this ConferenceInfo.

        云会议室会议ID或个人会议ID，如果vmrFlag为\"1\"，则该字段不为空。

        :return: The vmr_conference_id of this ConferenceInfo.
        :rtype: str
        """
        return self._vmr_conference_id

    @vmr_conference_id.setter
    def vmr_conference_id(self, vmr_conference_id):
        """Sets the vmr_conference_id of this ConferenceInfo.

        云会议室会议ID或个人会议ID，如果vmrFlag为\"1\"，则该字段不为空。

        :param vmr_conference_id: The vmr_conference_id of this ConferenceInfo.
        :type vmr_conference_id: str
        """
        self._vmr_conference_id = vmr_conference_id

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this ConferenceInfo.

        会议的UUID。 > * 只有创建立即开始的会议才返回UUID，如果是预约未来的会议，不会返回UUID > * 可以通过[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)获取历史会议的UUID 

        :return: The conf_uuid of this ConferenceInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this ConferenceInfo.

        会议的UUID。 > * 只有创建立即开始的会议才返回UUID，如果是预约未来的会议，不会返回UUID > * 可以通过[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)获取历史会议的UUID 

        :param conf_uuid: The conf_uuid of this ConferenceInfo.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def part_attendee_info(self):
        """Gets the part_attendee_info of this ConferenceInfo.

        被邀请的部分与会者信息。 > * 只返回被邀请的前20条软终端与会者信息和前20条硬终端与会者信息 > * 不返回会中主动加入的与会者信息 > * “[[查询会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0017.html)](tag:hws)[[查询会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0017.html)](tag:hk)”和“[[查询会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0018.html)](tag:hws)[[查询会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0018.html)](tag:hk)”接口，返回预约会议时邀请的与会者和会中主持人邀请的与会者 > * “[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”、“[[查询在线会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0026.html)](tag:hws)[[查询在线会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0026.html)](tag:hk)”、“[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)”和“[[查询历史会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0052.html)](tag:hws)[[查询历史会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0052.html)](tag:hk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ”接口返回预约会议时邀请的与会者。不返回会中主持人邀请的与会者 

        :return: The part_attendee_info of this ConferenceInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PartAttendee`]
        """
        return self._part_attendee_info

    @part_attendee_info.setter
    def part_attendee_info(self, part_attendee_info):
        """Sets the part_attendee_info of this ConferenceInfo.

        被邀请的部分与会者信息。 > * 只返回被邀请的前20条软终端与会者信息和前20条硬终端与会者信息 > * 不返回会中主动加入的与会者信息 > * “[[查询会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0017.html)](tag:hws)[[查询会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0017.html)](tag:hk)”和“[[查询会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0018.html)](tag:hws)[[查询会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0018.html)](tag:hk)”接口，返回预约会议时邀请的与会者和会中主持人邀请的与会者 > * “[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”、“[[查询在线会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0026.html)](tag:hws)[[查询在线会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0026.html)](tag:hk)”、“[[查询历史会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0051.html)](tag:hws)[[查询历史会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0051.html)](tag:hk)”和“[[查询历史会议详情](https://support.huaweicloud.com/api-meeting/meeting_21_0052.html)](tag:hws)[[查询历史会议详情](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0052.html)](tag:hk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ”接口返回预约会议时邀请的与会者。不返回会中主持人邀请的与会者 

        :param part_attendee_info: The part_attendee_info of this ConferenceInfo.
        :type part_attendee_info: list[:class:`huaweicloudsdkmeeting.v1.PartAttendee`]
        """
        self._part_attendee_info = part_attendee_info

    @property
    def terminl_count(self):
        """Gets the terminl_count of this ConferenceInfo.

        硬终端个数，如IdeaHub，TE30等。

        :return: The terminl_count of this ConferenceInfo.
        :rtype: int
        """
        return self._terminl_count

    @terminl_count.setter
    def terminl_count(self, terminl_count):
        """Sets the terminl_count of this ConferenceInfo.

        硬终端个数，如IdeaHub，TE30等。

        :param terminl_count: The terminl_count of this ConferenceInfo.
        :type terminl_count: int
        """
        self._terminl_count = terminl_count

    @property
    def normal_count(self):
        """Gets the normal_count of this ConferenceInfo.

        软终端个数，如PC端、手机端App等。

        :return: The normal_count of this ConferenceInfo.
        :rtype: int
        """
        return self._normal_count

    @normal_count.setter
    def normal_count(self, normal_count):
        """Sets the normal_count of this ConferenceInfo.

        软终端个数，如PC端、手机端App等。

        :param normal_count: The normal_count of this ConferenceInfo.
        :type normal_count: int
        """
        self._normal_count = normal_count

    @property
    def dept_name(self):
        """Gets the dept_name of this ConferenceInfo.

        会议预定者的企业名称。

        :return: The dept_name of this ConferenceInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ConferenceInfo.

        会议预定者的企业名称。

        :param dept_name: The dept_name of this ConferenceInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def vmr_id(self):
        """Gets the vmr_id of this ConferenceInfo.

        云会议室的ID。

        :return: The vmr_id of this ConferenceInfo.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this ConferenceInfo.

        云会议室的ID。

        :param vmr_id: The vmr_id of this ConferenceInfo.
        :type vmr_id: str
        """
        self._vmr_id = vmr_id

    @property
    def role(self):
        """Gets the role of this ConferenceInfo.

        与会者角色。 * chair ：主持人 * general ：来宾 * audience ： 观众 > * 仅在查询会议详情时返回 > * 返回查询者本身的角色 

        :return: The role of this ConferenceInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ConferenceInfo.

        与会者角色。 * chair ：主持人 * general ：来宾 * audience ： 观众 > * 仅在查询会议详情时返回 > * 返回查询者本身的角色 

        :param role: The role of this ConferenceInfo.
        :type role: str
        """
        self._role = role

    @property
    def webinar(self):
        """Gets the webinar of this ConferenceInfo.

        是否是网络研讨会。

        :return: The webinar of this ConferenceInfo.
        :rtype: bool
        """
        return self._webinar

    @webinar.setter
    def webinar(self, webinar):
        """Sets the webinar of this ConferenceInfo.

        是否是网络研讨会。

        :param webinar: The webinar of this ConferenceInfo.
        :type webinar: bool
        """
        self._webinar = webinar

    @property
    def online_attendee_amount(self):
        """Gets the online_attendee_amount of this ConferenceInfo.

        当前在线与会人数。包含被邀入会和主动入会的与会者。 > 仅在“[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”接口中返回。 

        :return: The online_attendee_amount of this ConferenceInfo.
        :rtype: int
        """
        return self._online_attendee_amount

    @online_attendee_amount.setter
    def online_attendee_amount(self, online_attendee_amount):
        """Sets the online_attendee_amount of this ConferenceInfo.

        当前在线与会人数。包含被邀入会和主动入会的与会者。 > 仅在“[[查询在线会议列表](https://support.huaweicloud.com/api-meeting/meeting_21_0025.html)](tag:hws)[[查询在线会议列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0025.html)](tag:hk)”接口中返回。 

        :param online_attendee_amount: The online_attendee_amount of this ConferenceInfo.
        :type online_attendee_amount: int
        """
        self._online_attendee_amount = online_attendee_amount

    @property
    def multi_stream_flag(self):
        """Gets the multi_stream_flag of this ConferenceInfo.

        标识是否为多流视频会议。 * 1：多流会议 

        :return: The multi_stream_flag of this ConferenceInfo.
        :rtype: int
        """
        return self._multi_stream_flag

    @multi_stream_flag.setter
    def multi_stream_flag(self, multi_stream_flag):
        """Sets the multi_stream_flag of this ConferenceInfo.

        标识是否为多流视频会议。 * 1：多流会议 

        :param multi_stream_flag: The multi_stream_flag of this ConferenceInfo.
        :type multi_stream_flag: int
        """
        self._multi_stream_flag = multi_stream_flag

    @property
    def conf_mode(self):
        """Gets the conf_mode of this ConferenceInfo.

        会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 

        :return: The conf_mode of this ConferenceInfo.
        :rtype: str
        """
        return self._conf_mode

    @conf_mode.setter
    def conf_mode(self, conf_mode):
        """Sets the conf_mode of this ConferenceInfo.

        会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 

        :param conf_mode: The conf_mode of this ConferenceInfo.
        :type conf_mode: str
        """
        self._conf_mode = conf_mode

    @property
    def schedule_vmr(self):
        """Gets the schedule_vmr of this ConferenceInfo.

        VMR预约记录。 true: VMR预约记录 false：普通会议 > 该参数将废弃，请勿使用。 

        :return: The schedule_vmr of this ConferenceInfo.
        :rtype: bool
        """
        return self._schedule_vmr

    @schedule_vmr.setter
    def schedule_vmr(self, schedule_vmr):
        """Sets the schedule_vmr of this ConferenceInfo.

        VMR预约记录。 true: VMR预约记录 false：普通会议 > 该参数将废弃，请勿使用。 

        :param schedule_vmr: The schedule_vmr of this ConferenceInfo.
        :type schedule_vmr: bool
        """
        self._schedule_vmr = schedule_vmr

    @property
    def concurrent_participants(self):
        """Gets the concurrent_participants of this ConferenceInfo.

        会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 

        :return: The concurrent_participants of this ConferenceInfo.
        :rtype: int
        """
        return self._concurrent_participants

    @concurrent_participants.setter
    def concurrent_participants(self, concurrent_participants):
        """Sets the concurrent_participants of this ConferenceInfo.

        会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 

        :param concurrent_participants: The concurrent_participants of this ConferenceInfo.
        :type concurrent_participants: int
        """
        self._concurrent_participants = concurrent_participants

    @property
    def pic_display(self):
        """Gets the pic_display of this ConferenceInfo.

        :return: The pic_display of this ConferenceInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.MultiPicDisplayDO`
        """
        return self._pic_display

    @pic_display.setter
    def pic_display(self, pic_display):
        """Sets the pic_display of this ConferenceInfo.

        :param pic_display: The pic_display of this ConferenceInfo.
        :type pic_display: :class:`huaweicloudsdkmeeting.v1.MultiPicDisplayDO`
        """
        self._pic_display = pic_display

    @property
    def sub_confs(self):
        """Gets the sub_confs of this ConferenceInfo.

        周期子会议列表。

        :return: The sub_confs of this ConferenceInfo.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.CycleSubConf`]
        """
        return self._sub_confs

    @sub_confs.setter
    def sub_confs(self, sub_confs):
        """Sets the sub_confs of this ConferenceInfo.

        周期子会议列表。

        :param sub_confs: The sub_confs of this ConferenceInfo.
        :type sub_confs: list[:class:`huaweicloudsdkmeeting.v1.CycleSubConf`]
        """
        self._sub_confs = sub_confs

    @property
    def cycle_sub_conf_id(self):
        """Gets the cycle_sub_conf_id of this ConferenceInfo.

        第一个周期子会议的UUID。

        :return: The cycle_sub_conf_id of this ConferenceInfo.
        :rtype: str
        """
        return self._cycle_sub_conf_id

    @cycle_sub_conf_id.setter
    def cycle_sub_conf_id(self, cycle_sub_conf_id):
        """Sets the cycle_sub_conf_id of this ConferenceInfo.

        第一个周期子会议的UUID。

        :param cycle_sub_conf_id: The cycle_sub_conf_id of this ConferenceInfo.
        :type cycle_sub_conf_id: str
        """
        self._cycle_sub_conf_id = cycle_sub_conf_id

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
        if not isinstance(other, ConferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
