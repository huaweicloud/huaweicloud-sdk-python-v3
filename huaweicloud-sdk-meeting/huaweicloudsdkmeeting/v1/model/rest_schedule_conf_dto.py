# coding: utf-8

import pprint
import re

import six





class RestScheduleConfDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_type': 'int',
        'start_time': 'str',
        'length': 'int',
        'subject': 'str',
        'media_types': 'str',
        'groupuri': 'str',
        'attendees': 'list[RestAttendeeDTO]',
        'is_auto_record': 'int',
        'encrypt_mode': 'int',
        'language': 'str',
        'time_zone_id': 'str',
        'record_type': 'int',
        'live_address': 'str',
        'aux_address': 'str',
        'record_aux_stream': 'int',
        'conf_config_info': 'RestConfConfigDTO',
        'record_auth_type': 'int',
        'vmr_flag': 'int',
        'cycle_params': 'CycleParams',
        'vmr_id': 'str',
        'concurrent_participants': 'int'
    }

    attribute_map = {
        'conference_type': 'conferenceType',
        'start_time': 'startTime',
        'length': 'length',
        'subject': 'subject',
        'media_types': 'mediaTypes',
        'groupuri': 'groupuri',
        'attendees': 'attendees',
        'is_auto_record': 'isAutoRecord',
        'encrypt_mode': 'encryptMode',
        'language': 'language',
        'time_zone_id': 'timeZoneID',
        'record_type': 'recordType',
        'live_address': 'liveAddress',
        'aux_address': 'auxAddress',
        'record_aux_stream': 'recordAuxStream',
        'conf_config_info': 'confConfigInfo',
        'record_auth_type': 'recordAuthType',
        'vmr_flag': 'vmrFlag',
        'cycle_params': 'cycleParams',
        'vmr_id': 'vmrID',
        'concurrent_participants': 'concurrentParticipants'
    }

    def __init__(self, conference_type=0, start_time=None, length=30, subject=None, media_types=None, groupuri=None, attendees=None, is_auto_record=0, encrypt_mode=None, language=None, time_zone_id=None, record_type=0, live_address=None, aux_address=None, record_aux_stream=None, conf_config_info=None, record_auth_type=None, vmr_flag=0, cycle_params=None, vmr_id=None, concurrent_participants=None):
        """RestScheduleConfDTO - a model defined in huaweicloud sdk"""
        
        

        self._conference_type = None
        self._start_time = None
        self._length = None
        self._subject = None
        self._media_types = None
        self._groupuri = None
        self._attendees = None
        self._is_auto_record = None
        self._encrypt_mode = None
        self._language = None
        self._time_zone_id = None
        self._record_type = None
        self._live_address = None
        self._aux_address = None
        self._record_aux_stream = None
        self._conf_config_info = None
        self._record_auth_type = None
        self._vmr_flag = None
        self._cycle_params = None
        self._vmr_id = None
        self._concurrent_participants = None
        self.discriminator = None

        if conference_type is not None:
            self.conference_type = conference_type
        if start_time is not None:
            self.start_time = start_time
        if length is not None:
            self.length = length
        if subject is not None:
            self.subject = subject
        self.media_types = media_types
        if groupuri is not None:
            self.groupuri = groupuri
        if attendees is not None:
            self.attendees = attendees
        if is_auto_record is not None:
            self.is_auto_record = is_auto_record
        if encrypt_mode is not None:
            self.encrypt_mode = encrypt_mode
        if language is not None:
            self.language = language
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if record_type is not None:
            self.record_type = record_type
        if live_address is not None:
            self.live_address = live_address
        if aux_address is not None:
            self.aux_address = aux_address
        if record_aux_stream is not None:
            self.record_aux_stream = record_aux_stream
        if conf_config_info is not None:
            self.conf_config_info = conf_config_info
        if record_auth_type is not None:
            self.record_auth_type = record_auth_type
        if vmr_flag is not None:
            self.vmr_flag = vmr_flag
        if cycle_params is not None:
            self.cycle_params = cycle_params
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if concurrent_participants is not None:
            self.concurrent_participants = concurrent_participants

    @property
    def conference_type(self):
        """Gets the conference_type of this RestScheduleConfDTO.

        创建会议类型（默认为普通会议）。 - 0: 普通会议。 - 1: 周期会议，此时cycleParams必须填写。

        :return: The conference_type of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._conference_type

    @conference_type.setter
    def conference_type(self, conference_type):
        """Sets the conference_type of this RestScheduleConfDTO.

        创建会议类型（默认为普通会议）。 - 0: 普通会议。 - 1: 周期会议，此时cycleParams必须填写。

        :param conference_type: The conference_type of this RestScheduleConfDTO.
        :type: int
        """
        self._conference_type = conference_type

    @property
    def start_time(self):
        """Gets the start_time of this RestScheduleConfDTO.

        会议开始时间（UTC时间）。 预定创建会议时，如果没有指定开始时间，或填空串，则表示会议马上开始。 格式：yyyy-MM-dd HH:mm

        :return: The start_time of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RestScheduleConfDTO.

        会议开始时间（UTC时间）。 预定创建会议时，如果没有指定开始时间，或填空串，则表示会议马上开始。 格式：yyyy-MM-dd HH:mm

        :param start_time: The start_time of this RestScheduleConfDTO.
        :type: str
        """
        self._start_time = start_time

    @property
    def length(self):
        """Gets the length of this RestScheduleConfDTO.

        会议持续时长，单位分钟，最大值为1440，最短15。default：30。

        :return: The length of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this RestScheduleConfDTO.

        会议持续时长，单位分钟，最大值为1440，最短15。default：30。

        :param length: The length of this RestScheduleConfDTO.
        :type: int
        """
        self._length = length

    @property
    def subject(self):
        """Gets the subject of this RestScheduleConfDTO.

        会议主题。长度限制为128个字符。

        :return: The subject of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this RestScheduleConfDTO.

        会议主题。长度限制为128个字符。

        :param subject: The subject of this RestScheduleConfDTO.
        :type: str
        """
        self._subject = subject

    @property
    def media_types(self):
        """Gets the media_types of this RestScheduleConfDTO.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔，枚举值如下： - Voice: 语音。 - Video: 标清视频。 - HDVideo: 高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video） - Telepresence: 智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段） - Data: 多媒体（系统配置决定是否自动添加Data）。

        :return: The media_types of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this RestScheduleConfDTO.

        会议的媒体类型。 由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔，枚举值如下： - Voice: 语音。 - Video: 标清视频。 - HDVideo: 高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video） - Telepresence: 智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段） - Data: 多媒体（系统配置决定是否自动添加Data）。

        :param media_types: The media_types of this RestScheduleConfDTO.
        :type: str
        """
        self._media_types = media_types

    @property
    def groupuri(self):
        """Gets the groupuri of this RestScheduleConfDTO.

        软终端创建即时会议时在当前字段带临时群组ID，由服务器在邀请其他与会者时在或者conference-info头域中携带。长度限制为31个字符。

        :return: The groupuri of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._groupuri

    @groupuri.setter
    def groupuri(self, groupuri):
        """Sets the groupuri of this RestScheduleConfDTO.

        软终端创建即时会议时在当前字段带临时群组ID，由服务器在邀请其他与会者时在或者conference-info头域中携带。长度限制为31个字符。

        :param groupuri: The groupuri of this RestScheduleConfDTO.
        :type: str
        """
        self._groupuri = groupuri

    @property
    def attendees(self):
        """Gets the attendees of this RestScheduleConfDTO.

        与会者列表。该列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。

        :return: The attendees of this RestScheduleConfDTO.
        :rtype: list[RestAttendeeDTO]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this RestScheduleConfDTO.

        与会者列表。该列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。

        :param attendees: The attendees of this RestScheduleConfDTO.
        :type: list[RestAttendeeDTO]
        """
        self._attendees = attendees

    @property
    def is_auto_record(self):
        """Gets the is_auto_record of this RestScheduleConfDTO.

        会议是否自动启动录制，在录播类型为:录播、直播+录播时有效。默认为不自动启动。 - 0: 不自动启动录制 - 1: 自动启动录制

        :return: The is_auto_record of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, is_auto_record):
        """Sets the is_auto_record of this RestScheduleConfDTO.

        会议是否自动启动录制，在录播类型为:录播、直播+录播时有效。默认为不自动启动。 - 0: 不自动启动录制 - 1: 自动启动录制

        :param is_auto_record: The is_auto_record of this RestScheduleConfDTO.
        :type: int
        """
        self._is_auto_record = is_auto_record

    @property
    def encrypt_mode(self):
        """Gets the encrypt_mode of this RestScheduleConfDTO.

        会议媒体加密模式。默认值由企业级的配置填充。 - 0: 自适应加密 - 1: 强制加密 - 2: 不加密

        :return: The encrypt_mode of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._encrypt_mode

    @encrypt_mode.setter
    def encrypt_mode(self, encrypt_mode):
        """Sets the encrypt_mode of this RestScheduleConfDTO.

        会议媒体加密模式。默认值由企业级的配置填充。 - 0: 自适应加密 - 1: 强制加密 - 2: 不加密

        :param encrypt_mode: The encrypt_mode of this RestScheduleConfDTO.
        :type: int
        """
        self._encrypt_mode = encrypt_mode

    @property
    def language(self):
        """Gets the language of this RestScheduleConfDTO.

        会议的默认语言，默认值由会议云服务定义。 对于系统支持的语言，按照RFC3066规范传递。 - zh-CN: 简体中文。 - en-US: 美国英文。

        :return: The language of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RestScheduleConfDTO.

        会议的默认语言，默认值由会议云服务定义。 对于系统支持的语言，按照RFC3066规范传递。 - zh-CN: 简体中文。 - en-US: 美国英文。

        :param language: The language of this RestScheduleConfDTO.
        :type: str
        """
        self._language = language

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this RestScheduleConfDTO.

        开始时间的时区信息。时区信息，参考时区映射关系。

        :return: The time_zone_id of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this RestScheduleConfDTO.

        开始时间的时区信息。时区信息，参考时区映射关系。

        :param time_zone_id: The time_zone_id of this RestScheduleConfDTO.
        :type: str
        """
        self._time_zone_id = time_zone_id

    @property
    def record_type(self):
        """Gets the record_type of this RestScheduleConfDTO.

        录播类型。默认为禁用。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播

        :return: The record_type of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this RestScheduleConfDTO.

        录播类型。默认为禁用。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播

        :param record_type: The record_type of this RestScheduleConfDTO.
        :type: int
        """
        self._record_type = record_type

    @property
    def live_address(self):
        """Gets the live_address of this RestScheduleConfDTO.

        主流直播地址，最大不超过255个字符。在录播类型为 :直播、直播+录播时有效。

        :return: The live_address of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._live_address

    @live_address.setter
    def live_address(self, live_address):
        """Sets the live_address of this RestScheduleConfDTO.

        主流直播地址，最大不超过255个字符。在录播类型为 :直播、直播+录播时有效。

        :param live_address: The live_address of this RestScheduleConfDTO.
        :type: str
        """
        self._live_address = live_address

    @property
    def aux_address(self):
        """Gets the aux_address of this RestScheduleConfDTO.

        辅流直播地址，最大不超过255个字符。在录播类型为: 直播、直播+录播时有效。

        :return: The aux_address of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._aux_address

    @aux_address.setter
    def aux_address(self, aux_address):
        """Sets the aux_address of this RestScheduleConfDTO.

        辅流直播地址，最大不超过255个字符。在录播类型为: 直播、直播+录播时有效。

        :param aux_address: The aux_address of this RestScheduleConfDTO.
        :type: str
        """
        self._aux_address = aux_address

    @property
    def record_aux_stream(self):
        """Gets the record_aux_stream of this RestScheduleConfDTO.

        是否录制辅流，在录播类型为：录播、录播+直播时有效。  - 0: 不录制。  - 1: 录制。

        :return: The record_aux_stream of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._record_aux_stream

    @record_aux_stream.setter
    def record_aux_stream(self, record_aux_stream):
        """Sets the record_aux_stream of this RestScheduleConfDTO.

        是否录制辅流，在录播类型为：录播、录播+直播时有效。  - 0: 不录制。  - 1: 录制。

        :param record_aux_stream: The record_aux_stream of this RestScheduleConfDTO.
        :type: int
        """
        self._record_aux_stream = record_aux_stream

    @property
    def conf_config_info(self):
        """Gets the conf_config_info of this RestScheduleConfDTO.


        :return: The conf_config_info of this RestScheduleConfDTO.
        :rtype: RestConfConfigDTO
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        """Sets the conf_config_info of this RestScheduleConfDTO.


        :param conf_config_info: The conf_config_info of this RestScheduleConfDTO.
        :type: RestConfConfigDTO
        """
        self._conf_config_info = conf_config_info

    @property
    def record_auth_type(self):
        """Gets the record_auth_type of this RestScheduleConfDTO.

        录播鉴权方式，在录播类型为:录播、直播+录播时有效。 - 0: 老的鉴权方式，url中携带token鉴权。 - 1: 企业内会议用户鉴权。 - 2: 会议内会议用户鉴权。

        :return: The record_auth_type of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        """Sets the record_auth_type of this RestScheduleConfDTO.

        录播鉴权方式，在录播类型为:录播、直播+录播时有效。 - 0: 老的鉴权方式，url中携带token鉴权。 - 1: 企业内会议用户鉴权。 - 2: 会议内会议用户鉴权。

        :param record_auth_type: The record_auth_type of this RestScheduleConfDTO.
        :type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def vmr_flag(self):
        """Gets the vmr_flag of this RestScheduleConfDTO.

        是否使用云会议室召开预约会议。默认不使用云会议室。 - 0: 不使用云会议室。 - 1: 使用云会议室。

        :return: The vmr_flag of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._vmr_flag

    @vmr_flag.setter
    def vmr_flag(self, vmr_flag):
        """Sets the vmr_flag of this RestScheduleConfDTO.

        是否使用云会议室召开预约会议。默认不使用云会议室。 - 0: 不使用云会议室。 - 1: 使用云会议室。

        :param vmr_flag: The vmr_flag of this RestScheduleConfDTO.
        :type: int
        """
        self._vmr_flag = vmr_flag

    @property
    def cycle_params(self):
        """Gets the cycle_params of this RestScheduleConfDTO.


        :return: The cycle_params of this RestScheduleConfDTO.
        :rtype: CycleParams
        """
        return self._cycle_params

    @cycle_params.setter
    def cycle_params(self, cycle_params):
        """Sets the cycle_params of this RestScheduleConfDTO.


        :param cycle_params: The cycle_params of this RestScheduleConfDTO.
        :type: CycleParams
        """
        self._cycle_params = cycle_params

    @property
    def vmr_id(self):
        """Gets the vmr_id of this RestScheduleConfDTO.

        用于识别用户开会时绑定的云会议室。最大长度不超过512个字符。 - 不为空，则用ID查询云会议室信息。 - 为空，则查用户所有云会议室，如果有个人云会议室，用个人云会议室ID；没有个人云会议室，取最小云会议室ID。

        :return: The vmr_id of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this RestScheduleConfDTO.

        用于识别用户开会时绑定的云会议室。最大长度不超过512个字符。 - 不为空，则用ID查询云会议室信息。 - 为空，则查用户所有云会议室，如果有个人云会议室，用个人云会议室ID；没有个人云会议室，取最小云会议室ID。

        :param vmr_id: The vmr_id of this RestScheduleConfDTO.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def concurrent_participants(self):
        """Gets the concurrent_participants of this RestScheduleConfDTO.

        会议方数，会议最大与会人数限制

        :return: The concurrent_participants of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._concurrent_participants

    @concurrent_participants.setter
    def concurrent_participants(self, concurrent_participants):
        """Sets the concurrent_participants of this RestScheduleConfDTO.

        会议方数，会议最大与会人数限制

        :param concurrent_participants: The concurrent_participants of this RestScheduleConfDTO.
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
        if not isinstance(other, RestScheduleConfDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
