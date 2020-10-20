# coding: utf-8

import pprint
import re

import six





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
        'concurrent_participants': 'int'
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
        'concurrent_participants': 'concurrentParticipants'
    }

    def __init__(self, conference_id=None, subject=None, size=None, time_zone_id=None, start_time=None, end_time=None, media_types=None, conference_state=None, language=None, access_number=None, password_entry=None, user_uuid=None, scheduser_name=None, conference_type=None, conf_type=None, cycle_params=None, is_auto_mute=None, is_auto_record=None, chair_join_uri=None, guest_join_uri=None, audience_join_uri=None, record_type=None, aux_address=None, live_address=None, record_aux_stream=None, record_auth_type=None, live_url=None, conf_config_info=None, vmr_flag=None, is_has_record_file=False, vmr_conference_id=None, conf_uuid=None, part_attendee_info=None, terminl_count=None, normal_count=None, dept_name=None, vmr_id=None, concurrent_participants=None):
        """ConferenceInfo - a model defined in huaweicloud sdk"""
        
        

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
        self._concurrent_participants = None
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
        if concurrent_participants is not None:
            self.concurrent_participants = concurrent_participants

    @property
    def conference_id(self):
        """Gets the conference_id of this ConferenceInfo.

        会议ID。长度限制为32个字符。

        :return: The conference_id of this ConferenceInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this ConferenceInfo.

        会议ID。长度限制为32个字符。

        :param conference_id: The conference_id of this ConferenceInfo.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def subject(self):
        """Gets the subject of this ConferenceInfo.

        会议主题。长度限制为128个字符。

        :return: The subject of this ConferenceInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ConferenceInfo.

        会议主题。长度限制为128个字符。

        :param subject: The subject of this ConferenceInfo.
        :type: str
        """
        self._subject = subject

    @property
    def size(self):
        """Gets the size of this ConferenceInfo.

        会议方数。

        :return: The size of this ConferenceInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ConferenceInfo.

        会议方数。

        :param size: The size of this ConferenceInfo.
        :type: int
        """
        self._size = size

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this ConferenceInfo.

        时区参考。

        :return: The time_zone_id of this ConferenceInfo.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this ConferenceInfo.

        时区参考。

        :param time_zone_id: The time_zone_id of this ConferenceInfo.
        :type: str
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
        :type: str
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
        :type: str
        """
        self._end_time = end_time

    @property
    def media_types(self):
        """Gets the media_types of this ConferenceInfo.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔。 - Voice: 语音。 - Video: 标清视频。 - HDVideo: 高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video）。 - Telepresence: 智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段） - Data: 多媒体。

        :return: The media_types of this ConferenceInfo.
        :rtype: str
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this ConferenceInfo.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔。 - Voice: 语音。 - Video: 标清视频。 - HDVideo: 高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video）。 - Telepresence: 智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段） - Data: 多媒体。

        :param media_types: The media_types of this ConferenceInfo.
        :type: str
        """
        self._media_types = media_types

    @property
    def conference_state(self):
        """Gets the conference_state of this ConferenceInfo.

        目前只会返回Created和Schedule状态， 如果会议已经召开返回Created状态，否则返回Schedule状态。 - Schedule: 预定状态。 - Creating: 正在创建状态。 - Created: 会议已经被创建，并正在召开。 - Destroyed: 会议已经关闭。

        :return: The conference_state of this ConferenceInfo.
        :rtype: str
        """
        return self._conference_state

    @conference_state.setter
    def conference_state(self, conference_state):
        """Sets the conference_state of this ConferenceInfo.

        目前只会返回Created和Schedule状态， 如果会议已经召开返回Created状态，否则返回Schedule状态。 - Schedule: 预定状态。 - Creating: 正在创建状态。 - Created: 会议已经被创建，并正在召开。 - Destroyed: 会议已经关闭。

        :param conference_state: The conference_state of this ConferenceInfo.
        :type: str
        """
        self._conference_state = conference_state

    @property
    def language(self):
        """Gets the language of this ConferenceInfo.

        会议语言。

        :return: The language of this ConferenceInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConferenceInfo.

        会议语言。

        :param language: The language of this ConferenceInfo.
        :type: str
        """
        self._language = language

    @property
    def access_number(self):
        """Gets the access_number of this ConferenceInfo.

        会议接入码。

        :return: The access_number of this ConferenceInfo.
        :rtype: str
        """
        return self._access_number

    @access_number.setter
    def access_number(self, access_number):
        """Sets the access_number of this ConferenceInfo.

        会议接入码。

        :param access_number: The access_number of this ConferenceInfo.
        :type: str
        """
        self._access_number = access_number

    @property
    def password_entry(self):
        """Gets the password_entry of this ConferenceInfo.

        会议密码条目。预订者返回主持人密码和来宾密码。 - 主持人查询时返回主持人密码。 - 来宾查询时返回来宾密码。

        :return: The password_entry of this ConferenceInfo.
        :rtype: list[PasswordEntry]
        """
        return self._password_entry

    @password_entry.setter
    def password_entry(self, password_entry):
        """Sets the password_entry of this ConferenceInfo.

        会议密码条目。预订者返回主持人密码和来宾密码。 - 主持人查询时返回主持人密码。 - 来宾查询时返回来宾密码。

        :param password_entry: The password_entry of this ConferenceInfo.
        :type: list[PasswordEntry]
        """
        self._password_entry = password_entry

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ConferenceInfo.

        会议预订者UUID。

        :return: The user_uuid of this ConferenceInfo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ConferenceInfo.

        会议预订者UUID。

        :param user_uuid: The user_uuid of this ConferenceInfo.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this ConferenceInfo.

        会议预订者帐号名称。长度最大限制为96个字符。

        :return: The scheduser_name of this ConferenceInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this ConferenceInfo.

        会议预订者帐号名称。长度最大限制为96个字符。

        :param scheduser_name: The scheduser_name of this ConferenceInfo.
        :type: str
        """
        self._scheduser_name = scheduser_name

    @property
    def conference_type(self):
        """Gets the conference_type of this ConferenceInfo.

        - 0: 普通会议。 - 1: 周期会议。

        :return: The conference_type of this ConferenceInfo.
        :rtype: int
        """
        return self._conference_type

    @conference_type.setter
    def conference_type(self, conference_type):
        """Sets the conference_type of this ConferenceInfo.

        - 0: 普通会议。 - 1: 周期会议。

        :param conference_type: The conference_type of this ConferenceInfo.
        :type: int
        """
        self._conference_type = conference_type

    @property
    def conf_type(self):
        """Gets the conf_type of this ConferenceInfo.

        会议类型。 - FUTURE - IMMEDIATELY - CYCLE

        :return: The conf_type of this ConferenceInfo.
        :rtype: str
        """
        return self._conf_type

    @conf_type.setter
    def conf_type(self, conf_type):
        """Sets the conf_type of this ConferenceInfo.

        会议类型。 - FUTURE - IMMEDIATELY - CYCLE

        :param conf_type: The conf_type of this ConferenceInfo.
        :type: str
        """
        self._conf_type = conf_type

    @property
    def cycle_params(self):
        """Gets the cycle_params of this ConferenceInfo.


        :return: The cycle_params of this ConferenceInfo.
        :rtype: CycleParams
        """
        return self._cycle_params

    @cycle_params.setter
    def cycle_params(self, cycle_params):
        """Sets the cycle_params of this ConferenceInfo.


        :param cycle_params: The cycle_params of this ConferenceInfo.
        :type: CycleParams
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
        :type: int
        """
        self._is_auto_mute = is_auto_mute

    @property
    def is_auto_record(self):
        """Gets the is_auto_record of this ConferenceInfo.

        是否自动开启录音。 - 0: 不自动启动。 - 1: 自动启动。

        :return: The is_auto_record of this ConferenceInfo.
        :rtype: int
        """
        return self._is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, is_auto_record):
        """Sets the is_auto_record of this ConferenceInfo.

        是否自动开启录音。 - 0: 不自动启动。 - 1: 自动启动。

        :param is_auto_record: The is_auto_record of this ConferenceInfo.
        :type: int
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
        :type: str
        """
        self._chair_join_uri = chair_join_uri

    @property
    def guest_join_uri(self):
        """Gets the guest_join_uri of this ConferenceInfo.

        普通与会者会议链接地址。最大长度1024。

        :return: The guest_join_uri of this ConferenceInfo.
        :rtype: str
        """
        return self._guest_join_uri

    @guest_join_uri.setter
    def guest_join_uri(self, guest_join_uri):
        """Sets the guest_join_uri of this ConferenceInfo.

        普通与会者会议链接地址。最大长度1024。

        :param guest_join_uri: The guest_join_uri of this ConferenceInfo.
        :type: str
        """
        self._guest_join_uri = guest_join_uri

    @property
    def audience_join_uri(self):
        """Gets the audience_join_uri of this ConferenceInfo.

        旁听者会议链接地址。最大长度1024。（预留字段）

        :return: The audience_join_uri of this ConferenceInfo.
        :rtype: str
        """
        return self._audience_join_uri

    @audience_join_uri.setter
    def audience_join_uri(self, audience_join_uri):
        """Sets the audience_join_uri of this ConferenceInfo.

        旁听者会议链接地址。最大长度1024。（预留字段）

        :param audience_join_uri: The audience_join_uri of this ConferenceInfo.
        :type: str
        """
        self._audience_join_uri = audience_join_uri

    @property
    def record_type(self):
        """Gets the record_type of this ConferenceInfo.

        录播类型。 - 0: 禁用 。 - 1: 直播 。 - 2: 录播 。 - 3: 直播+录播。

        :return: The record_type of this ConferenceInfo.
        :rtype: int
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this ConferenceInfo.

        录播类型。 - 0: 禁用 。 - 1: 直播 。 - 2: 录播 。 - 3: 直播+录播。

        :param record_type: The record_type of this ConferenceInfo.
        :type: int
        """
        self._record_type = record_type

    @property
    def aux_address(self):
        """Gets the aux_address of this ConferenceInfo.

        辅流直播地址。

        :return: The aux_address of this ConferenceInfo.
        :rtype: str
        """
        return self._aux_address

    @aux_address.setter
    def aux_address(self, aux_address):
        """Sets the aux_address of this ConferenceInfo.

        辅流直播地址。

        :param aux_address: The aux_address of this ConferenceInfo.
        :type: str
        """
        self._aux_address = aux_address

    @property
    def live_address(self):
        """Gets the live_address of this ConferenceInfo.

        主流直播地址。

        :return: The live_address of this ConferenceInfo.
        :rtype: str
        """
        return self._live_address

    @live_address.setter
    def live_address(self, live_address):
        """Sets the live_address of this ConferenceInfo.

        主流直播地址。

        :param live_address: The live_address of this ConferenceInfo.
        :type: str
        """
        self._live_address = live_address

    @property
    def record_aux_stream(self):
        """Gets the record_aux_stream of this ConferenceInfo.

        是否录制辅流。  - 0: 否。  - 1: 是。

        :return: The record_aux_stream of this ConferenceInfo.
        :rtype: int
        """
        return self._record_aux_stream

    @record_aux_stream.setter
    def record_aux_stream(self, record_aux_stream):
        """Sets the record_aux_stream of this ConferenceInfo.

        是否录制辅流。  - 0: 否。  - 1: 是。

        :param record_aux_stream: The record_aux_stream of this ConferenceInfo.
        :type: int
        """
        self._record_aux_stream = record_aux_stream

    @property
    def record_auth_type(self):
        """Gets the record_auth_type of this ConferenceInfo.

        录播鉴权方式。录播类型为:录播、直播+录播时有效。  - 0: 老的鉴权方式，url中携带token鉴权。  - 1: 企业内会议用户鉴权。  - 2: 会议内会议用户鉴权。

        :return: The record_auth_type of this ConferenceInfo.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        """Sets the record_auth_type of this ConferenceInfo.

        录播鉴权方式。录播类型为:录播、直播+录播时有效。  - 0: 老的鉴权方式，url中携带token鉴权。  - 1: 企业内会议用户鉴权。  - 2: 会议内会议用户鉴权。

        :param record_auth_type: The record_auth_type of this ConferenceInfo.
        :type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def live_url(self):
        """Gets the live_url of this ConferenceInfo.

        直播地址。（配置直播房间时会返回）

        :return: The live_url of this ConferenceInfo.
        :rtype: str
        """
        return self._live_url

    @live_url.setter
    def live_url(self, live_url):
        """Sets the live_url of this ConferenceInfo.

        直播地址。（配置直播房间时会返回）

        :param live_url: The live_url of this ConferenceInfo.
        :type: str
        """
        self._live_url = live_url

    @property
    def conf_config_info(self):
        """Gets the conf_config_info of this ConferenceInfo.


        :return: The conf_config_info of this ConferenceInfo.
        :rtype: RestConfConfigDTO
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        """Sets the conf_config_info of this ConferenceInfo.


        :param conf_config_info: The conf_config_info of this ConferenceInfo.
        :type: RestConfConfigDTO
        """
        self._conf_config_info = conf_config_info

    @property
    def vmr_flag(self):
        """Gets the vmr_flag of this ConferenceInfo.

        是否使用云会议室召开预约会议。 - 0: 不使用云会议室; - 1: 使用云会议室。 界面显示会议ID需要使用vmrConferenceID作为会议ID；查询会议详情、登录会控、一键入会等会议业务操作依然使用conferenceID字段。

        :return: The vmr_flag of this ConferenceInfo.
        :rtype: int
        """
        return self._vmr_flag

    @vmr_flag.setter
    def vmr_flag(self, vmr_flag):
        """Sets the vmr_flag of this ConferenceInfo.

        是否使用云会议室召开预约会议。 - 0: 不使用云会议室; - 1: 使用云会议室。 界面显示会议ID需要使用vmrConferenceID作为会议ID；查询会议详情、登录会控、一键入会等会议业务操作依然使用conferenceID字段。

        :param vmr_flag: The vmr_flag of this ConferenceInfo.
        :type: int
        """
        self._vmr_flag = vmr_flag

    @property
    def is_has_record_file(self):
        """Gets the is_has_record_file of this ConferenceInfo.

        仅历史会议返回值有效。默认没有录制文件。 - True: 有录制文件。 - False: 没有录制文件。

        :return: The is_has_record_file of this ConferenceInfo.
        :rtype: bool
        """
        return self._is_has_record_file

    @is_has_record_file.setter
    def is_has_record_file(self, is_has_record_file):
        """Sets the is_has_record_file of this ConferenceInfo.

        仅历史会议返回值有效。默认没有录制文件。 - True: 有录制文件。 - False: 没有录制文件。

        :param is_has_record_file: The is_has_record_file of this ConferenceInfo.
        :type: bool
        """
        self._is_has_record_file = is_has_record_file

    @property
    def vmr_conference_id(self):
        """Gets the vmr_conference_id of this ConferenceInfo.

        云会议室id，如果vmrFlag为1，则该字段不为空。

        :return: The vmr_conference_id of this ConferenceInfo.
        :rtype: str
        """
        return self._vmr_conference_id

    @vmr_conference_id.setter
    def vmr_conference_id(self, vmr_conference_id):
        """Sets the vmr_conference_id of this ConferenceInfo.

        云会议室id，如果vmrFlag为1，则该字段不为空。

        :param vmr_conference_id: The vmr_conference_id of this ConferenceInfo.
        :type: str
        """
        self._vmr_conference_id = vmr_conference_id

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this ConferenceInfo.

        会议的UUID。

        :return: The conf_uuid of this ConferenceInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this ConferenceInfo.

        会议的UUID。

        :param conf_uuid: The conf_uuid of this ConferenceInfo.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def part_attendee_info(self):
        """Gets the part_attendee_info of this ConferenceInfo.

        与会方信息。硬件终端/与会人最多各显示20条记录。

        :return: The part_attendee_info of this ConferenceInfo.
        :rtype: list[PartAttendee]
        """
        return self._part_attendee_info

    @part_attendee_info.setter
    def part_attendee_info(self, part_attendee_info):
        """Sets the part_attendee_info of this ConferenceInfo.

        与会方信息。硬件终端/与会人最多各显示20条记录。

        :param part_attendee_info: The part_attendee_info of this ConferenceInfo.
        :type: list[PartAttendee]
        """
        self._part_attendee_info = part_attendee_info

    @property
    def terminl_count(self):
        """Gets the terminl_count of this ConferenceInfo.

        硬终端个数。

        :return: The terminl_count of this ConferenceInfo.
        :rtype: int
        """
        return self._terminl_count

    @terminl_count.setter
    def terminl_count(self, terminl_count):
        """Sets the terminl_count of this ConferenceInfo.

        硬终端个数。

        :param terminl_count: The terminl_count of this ConferenceInfo.
        :type: int
        """
        self._terminl_count = terminl_count

    @property
    def normal_count(self):
        """Gets the normal_count of this ConferenceInfo.

        普通终端个数。

        :return: The normal_count of this ConferenceInfo.
        :rtype: int
        """
        return self._normal_count

    @normal_count.setter
    def normal_count(self, normal_count):
        """Sets the normal_count of this ConferenceInfo.

        普通终端个数。

        :param normal_count: The normal_count of this ConferenceInfo.
        :type: int
        """
        self._normal_count = normal_count

    @property
    def dept_name(self):
        """Gets the dept_name of this ConferenceInfo.

        会议预定者的企业名称。最大长度96。

        :return: The dept_name of this ConferenceInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ConferenceInfo.

        会议预定者的企业名称。最大长度96。

        :param dept_name: The dept_name of this ConferenceInfo.
        :type: str
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
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def concurrent_participants(self):
        """Gets the concurrent_participants of this ConferenceInfo.

        会议方数，会议最大与会人数限制

        :return: The concurrent_participants of this ConferenceInfo.
        :rtype: int
        """
        return self._concurrent_participants

    @concurrent_participants.setter
    def concurrent_participants(self, concurrent_participants):
        """Sets the concurrent_participants of this ConferenceInfo.

        会议方数，会议最大与会人数限制

        :param concurrent_participants: The concurrent_participants of this ConferenceInfo.
        :type: int
        """
        self._concurrent_participants = concurrent_participants

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
