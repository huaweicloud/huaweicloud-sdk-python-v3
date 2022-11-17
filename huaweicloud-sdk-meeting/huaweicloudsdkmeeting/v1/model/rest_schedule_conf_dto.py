# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, start_time=None, length=None, subject=None, media_types=None, groupuri=None, attendees=None, is_auto_record=None, encrypt_mode=None, language=None, time_zone_id=None, record_type=None, live_address=None, aux_address=None, record_aux_stream=None, conf_config_info=None, record_auth_type=None, vmr_flag=None, cycle_params=None, vmr_id=None, concurrent_participants=None):
        """RestScheduleConfDTO

        The model defined in huaweicloud sdk

        :param start_time: 会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 &gt; * 创建预约会议时，如果没有指定开始时间或填空串，则表示会议马上开始 &gt; * 时间是UTC时间，即0时区的时间
        :type start_time: str
        :param length: 会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。
        :type length: int
        :param subject: 会议主题。最多128个字符。
        :type subject: str
        :param media_types: 会议的媒体类型。 - Voice: 语音会议 - HDVideo: 视频会议
        :type media_types: str
        :param groupuri: 软终端创建即时会议时在当前字段带临时群组ID，由服务器在邀请其他与会者时在或者conference-info头域中携带。长度限制为31个字符。
        :type groupuri: str
        :param attendees: 与会者列表。
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.RestAttendeeDTO`]
        :param is_auto_record: 会议是否自动启动录制，在录播类型为:录播、直播+录播时有效。默认为不自动启动。 - 0: 不自动启动录制 - 1: 自动启动录制
        :type is_auto_record: int
        :param encrypt_mode: 会议媒体加密模式。默认值由企业级的配置填充。 - 0: 自适应加密 - 1: 强制加密 - 2: 不加密
        :type encrypt_mode: int
        :param language: 会议通知短信或邮件的语言。默认中文。 - zh-CN: 简体中文 - en-US: 美国英文
        :type language: str
        :param time_zone_id: 会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 &gt; * 举例：“timeZoneID”:\&quot;26\&quot;，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 &gt; * 非周期会议，如果会议通知是通过第三方系统发送，则这个字段不用填写。
        :type time_zone_id: str
        :param record_type: 录播类型。默认为禁用。 - 0: 禁用 - 1: 直播 - 2: 录播 - 3: 直播+录播
        :type record_type: int
        :param live_address: 主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。
        :type live_address: str
        :param aux_address: 辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。
        :type aux_address: str
        :param record_aux_stream: 是否录制辅流，在录播类型为：录播、录播+直播时有效。默认只录制视频主流，不录制辅流。  - 0: 不录制  - 1: 录制
        :type record_aux_stream: int
        :param conf_config_info: 
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        :param record_auth_type: 录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载
        :type record_auth_type: int
        :param vmr_flag: 是否使用云会议室或者个人会议ID召开预约会议。默认0。 - 0: 不使用云会议室或者个人会议ID - 1: 使用云会议室或者个人会议ID
        :type vmr_flag: int
        :param cycle_params: 
        :type cycle_params: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        :param vmr_id: 绑定给当前创会帐号的VMR ID。通过[[查询云会议室及个人会议ID](https://support.huaweicloud.com/api-meeting/meeting_21_1106.html)](tag:hws)[[查询云会议室及个人会议ID](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1106.html)](tag:hk)接口获取。 &gt; * vmrID取上述查询接口中返回的id，不是vmrId &gt; * 创建个人会议ID的会议时，使用vmrMode&#x3D;0的VMR；创建云会议室的会议时，使用vmrMode&#x3D;1的VMR
        :type vmr_id: str
        :param concurrent_participants: 会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 
        :type concurrent_participants: int
        """
        
        

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
    def start_time(self):
        """Gets the start_time of this RestScheduleConfDTO.

        会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 > * 创建预约会议时，如果没有指定开始时间或填空串，则表示会议马上开始 > * 时间是UTC时间，即0时区的时间

        :return: The start_time of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RestScheduleConfDTO.

        会议开始时间（UTC时间）。格式：yyyy-MM-dd HH:mm。 > * 创建预约会议时，如果没有指定开始时间或填空串，则表示会议马上开始 > * 时间是UTC时间，即0时区的时间

        :param start_time: The start_time of this RestScheduleConfDTO.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def length(self):
        """Gets the length of this RestScheduleConfDTO.

        会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。

        :return: The length of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this RestScheduleConfDTO.

        会议持续时长，单位分钟。默认30分钟。最大1440分钟（24小时），最小15分钟。

        :param length: The length of this RestScheduleConfDTO.
        :type length: int
        """
        self._length = length

    @property
    def subject(self):
        """Gets the subject of this RestScheduleConfDTO.

        会议主题。最多128个字符。

        :return: The subject of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this RestScheduleConfDTO.

        会议主题。最多128个字符。

        :param subject: The subject of this RestScheduleConfDTO.
        :type subject: str
        """
        self._subject = subject

    @property
    def media_types(self):
        """Gets the media_types of this RestScheduleConfDTO.

        会议的媒体类型。 - Voice: 语音会议 - HDVideo: 视频会议

        :return: The media_types of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this RestScheduleConfDTO.

        会议的媒体类型。 - Voice: 语音会议 - HDVideo: 视频会议

        :param media_types: The media_types of this RestScheduleConfDTO.
        :type media_types: str
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
        :type groupuri: str
        """
        self._groupuri = groupuri

    @property
    def attendees(self):
        """Gets the attendees of this RestScheduleConfDTO.

        与会者列表。

        :return: The attendees of this RestScheduleConfDTO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RestAttendeeDTO`]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this RestScheduleConfDTO.

        与会者列表。

        :param attendees: The attendees of this RestScheduleConfDTO.
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.RestAttendeeDTO`]
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
        :type is_auto_record: int
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
        :type encrypt_mode: int
        """
        self._encrypt_mode = encrypt_mode

    @property
    def language(self):
        """Gets the language of this RestScheduleConfDTO.

        会议通知短信或邮件的语言。默认中文。 - zh-CN: 简体中文 - en-US: 美国英文

        :return: The language of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RestScheduleConfDTO.

        会议通知短信或邮件的语言。默认中文。 - zh-CN: 简体中文 - en-US: 美国英文

        :param language: The language of this RestScheduleConfDTO.
        :type language: str
        """
        self._language = language

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this RestScheduleConfDTO.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 > * 非周期会议，如果会议通知是通过第三方系统发送，则这个字段不用填写。

        :return: The time_zone_id of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this RestScheduleConfDTO.

        会议通知中会议时间的时区信息。时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > * 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 > * 非周期会议，如果会议通知是通过第三方系统发送，则这个字段不用填写。

        :param time_zone_id: The time_zone_id of this RestScheduleConfDTO.
        :type time_zone_id: str
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
        :type record_type: int
        """
        self._record_type = record_type

    @property
    def live_address(self):
        """Gets the live_address of this RestScheduleConfDTO.

        主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :return: The live_address of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._live_address

    @live_address.setter
    def live_address(self, live_address):
        """Sets the live_address of this RestScheduleConfDTO.

        主流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :param live_address: The live_address of this RestScheduleConfDTO.
        :type live_address: str
        """
        self._live_address = live_address

    @property
    def aux_address(self):
        """Gets the aux_address of this RestScheduleConfDTO.

        辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :return: The aux_address of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._aux_address

    @aux_address.setter
    def aux_address(self, aux_address):
        """Sets the aux_address of this RestScheduleConfDTO.

        辅流直播推流地址，在录播类型为 :直播、直播+录播时有效。最大不超过255个字符。

        :param aux_address: The aux_address of this RestScheduleConfDTO.
        :type aux_address: str
        """
        self._aux_address = aux_address

    @property
    def record_aux_stream(self):
        """Gets the record_aux_stream of this RestScheduleConfDTO.

        是否录制辅流，在录播类型为：录播、录播+直播时有效。默认只录制视频主流，不录制辅流。  - 0: 不录制  - 1: 录制

        :return: The record_aux_stream of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._record_aux_stream

    @record_aux_stream.setter
    def record_aux_stream(self, record_aux_stream):
        """Sets the record_aux_stream of this RestScheduleConfDTO.

        是否录制辅流，在录播类型为：录播、录播+直播时有效。默认只录制视频主流，不录制辅流。  - 0: 不录制  - 1: 录制

        :param record_aux_stream: The record_aux_stream of this RestScheduleConfDTO.
        :type record_aux_stream: int
        """
        self._record_aux_stream = record_aux_stream

    @property
    def conf_config_info(self):
        """Gets the conf_config_info of this RestScheduleConfDTO.

        :return: The conf_config_info of this RestScheduleConfDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        """
        return self._conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, conf_config_info):
        """Sets the conf_config_info of this RestScheduleConfDTO.

        :param conf_config_info: The conf_config_info of this RestScheduleConfDTO.
        :type conf_config_info: :class:`huaweicloudsdkmeeting.v1.RestConfConfigDTO`
        """
        self._conf_config_info = conf_config_info

    @property
    def record_auth_type(self):
        """Gets the record_auth_type of this RestScheduleConfDTO.

        录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载

        :return: The record_auth_type of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        """Sets the record_auth_type of this RestScheduleConfDTO.

        录播观看鉴权方式，在录播类型为:录播、直播+录播时有效。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载

        :param record_auth_type: The record_auth_type of this RestScheduleConfDTO.
        :type record_auth_type: int
        """
        self._record_auth_type = record_auth_type

    @property
    def vmr_flag(self):
        """Gets the vmr_flag of this RestScheduleConfDTO.

        是否使用云会议室或者个人会议ID召开预约会议。默认0。 - 0: 不使用云会议室或者个人会议ID - 1: 使用云会议室或者个人会议ID

        :return: The vmr_flag of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._vmr_flag

    @vmr_flag.setter
    def vmr_flag(self, vmr_flag):
        """Sets the vmr_flag of this RestScheduleConfDTO.

        是否使用云会议室或者个人会议ID召开预约会议。默认0。 - 0: 不使用云会议室或者个人会议ID - 1: 使用云会议室或者个人会议ID

        :param vmr_flag: The vmr_flag of this RestScheduleConfDTO.
        :type vmr_flag: int
        """
        self._vmr_flag = vmr_flag

    @property
    def cycle_params(self):
        """Gets the cycle_params of this RestScheduleConfDTO.

        :return: The cycle_params of this RestScheduleConfDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        """
        return self._cycle_params

    @cycle_params.setter
    def cycle_params(self, cycle_params):
        """Sets the cycle_params of this RestScheduleConfDTO.

        :param cycle_params: The cycle_params of this RestScheduleConfDTO.
        :type cycle_params: :class:`huaweicloudsdkmeeting.v1.CycleParams`
        """
        self._cycle_params = cycle_params

    @property
    def vmr_id(self):
        """Gets the vmr_id of this RestScheduleConfDTO.

        绑定给当前创会帐号的VMR ID。通过[[查询云会议室及个人会议ID](https://support.huaweicloud.com/api-meeting/meeting_21_1106.html)](tag:hws)[[查询云会议室及个人会议ID](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1106.html)](tag:hk)接口获取。 > * vmrID取上述查询接口中返回的id，不是vmrId > * 创建个人会议ID的会议时，使用vmrMode=0的VMR；创建云会议室的会议时，使用vmrMode=1的VMR

        :return: The vmr_id of this RestScheduleConfDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this RestScheduleConfDTO.

        绑定给当前创会帐号的VMR ID。通过[[查询云会议室及个人会议ID](https://support.huaweicloud.com/api-meeting/meeting_21_1106.html)](tag:hws)[[查询云会议室及个人会议ID](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_1106.html)](tag:hk)接口获取。 > * vmrID取上述查询接口中返回的id，不是vmrId > * 创建个人会议ID的会议时，使用vmrMode=0的VMR；创建云会议室的会议时，使用vmrMode=1的VMR

        :param vmr_id: The vmr_id of this RestScheduleConfDTO.
        :type vmr_id: str
        """
        self._vmr_id = vmr_id

    @property
    def concurrent_participants(self):
        """Gets the concurrent_participants of this RestScheduleConfDTO.

        会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 

        :return: The concurrent_participants of this RestScheduleConfDTO.
        :rtype: int
        """
        return self._concurrent_participants

    @concurrent_participants.setter
    def concurrent_participants(self, concurrent_participants):
        """Sets the concurrent_participants of this RestScheduleConfDTO.

        会议最大与会人数。默认值0。 * 0：无限制 * 大于0：会议最大与会人数 

        :param concurrent_participants: The concurrent_participants of this RestScheduleConfDTO.
        :type concurrent_participants: int
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
        if not isinstance(other, RestScheduleConfDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
