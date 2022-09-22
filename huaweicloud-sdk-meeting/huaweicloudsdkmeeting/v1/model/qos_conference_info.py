# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QosConferenceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'conference_id': 'str',
        'subject': 'str',
        'scheduser_name': 'str',
        'dept_name': 'str',
        'alarm': 'str',
        'audio_alarm': 'str',
        'video_alarm': 'str',
        'screen_alarm': 'str',
        'cpu_alarm': 'str',
        'time_zone_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'duration': 'int',
        'participants': 'int',
        'webinar': 'bool'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'conference_id': 'conferenceID',
        'subject': 'subject',
        'scheduser_name': 'scheduserName',
        'dept_name': 'deptName',
        'alarm': 'alarm',
        'audio_alarm': 'audioAlarm',
        'video_alarm': 'videoAlarm',
        'screen_alarm': 'screenAlarm',
        'cpu_alarm': 'cpuAlarm',
        'time_zone_id': 'timeZoneID',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'duration': 'duration',
        'participants': 'participants',
        'webinar': 'webinar'
    }

    def __init__(self, conf_uuid=None, conference_id=None, subject=None, scheduser_name=None, dept_name=None, alarm=None, audio_alarm=None, video_alarm=None, screen_alarm=None, cpu_alarm=None, time_zone_id=None, start_time=None, end_time=None, duration=None, participants=None, webinar=None):
        """QosConferenceInfo

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议UUID。
        :type conf_uuid: str
        :param conference_id: 会议ID。
        :type conference_id: str
        :param subject: 会议主题。
        :type subject: str
        :param scheduser_name: 会议预订者名称。
        :type scheduser_name: str
        :param dept_name: 部门名称。
        :type dept_name: str
        :param alarm: 总体告警 。 * YES：会议的音频、视频、屏幕共享、CPU任一项产生告警，总体告警就为YES * NO：无告警
        :type alarm: str
        :param audio_alarm: 音频告警 。 * YES：会议中任一与会者存在音频告警，会议音频告警就为YES * NO：无音频告警
        :type audio_alarm: str
        :param video_alarm: 视频告警。 * YES：会议中任一与会者存在视频告警，会议视频告警就为YES * NO：无音视频警
        :type video_alarm: str
        :param screen_alarm: 屏幕共享告警 YES/NO。 * YES：会议中任一与会者存在屏幕共享告警，会议屏幕共享告警就为YES * NO：无屏幕共享告警
        :type screen_alarm: str
        :param cpu_alarm: CPU告警。 * YES：会议中任一与会者存在CPU告警，会议CPU告警就为YES * NO：无CPU告警
        :type cpu_alarm: str
        :param time_zone_id: 时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 &gt; 举例：“timeZoneID”:\&quot;26\&quot;，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 
        :type time_zone_id: str
        :param start_time: 会议开始时间(UTC时间), Unix时间戳（单位毫秒）。
        :type start_time: int
        :param end_time: 会议结束时间(UTC时间), Unix时间戳（单位毫秒）。 &gt; * 在线会议：会议召开中，endTime &#x3D; 会议预计结束时间 &gt; * 历史会议：会议已结束，endTime &#x3D; 会议实际结束时间
        :type end_time: int
        :param duration: 会议召开时长（分钟）。 &gt; * 在线会议：会议召开中，duration &#x3D; 0 &gt; * 历史会议：会议已结束，duration &#x3D; 会议实际召开时间
        :type duration: int
        :param participants: 与会方数。 &gt; 同一用户多次进出会议属于不同的与会方，与会方数计算多次。
        :type participants: int
        :param webinar: 是否网络研讨会。
        :type webinar: bool
        """
        
        

        self._conf_uuid = None
        self._conference_id = None
        self._subject = None
        self._scheduser_name = None
        self._dept_name = None
        self._alarm = None
        self._audio_alarm = None
        self._video_alarm = None
        self._screen_alarm = None
        self._cpu_alarm = None
        self._time_zone_id = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._participants = None
        self._webinar = None
        self.discriminator = None

        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if conference_id is not None:
            self.conference_id = conference_id
        if subject is not None:
            self.subject = subject
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if dept_name is not None:
            self.dept_name = dept_name
        if alarm is not None:
            self.alarm = alarm
        if audio_alarm is not None:
            self.audio_alarm = audio_alarm
        if video_alarm is not None:
            self.video_alarm = video_alarm
        if screen_alarm is not None:
            self.screen_alarm = screen_alarm
        if cpu_alarm is not None:
            self.cpu_alarm = cpu_alarm
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if participants is not None:
            self.participants = participants
        if webinar is not None:
            self.webinar = webinar

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this QosConferenceInfo.

        会议UUID。

        :return: The conf_uuid of this QosConferenceInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this QosConferenceInfo.

        会议UUID。

        :param conf_uuid: The conf_uuid of this QosConferenceInfo.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conference_id(self):
        """Gets the conference_id of this QosConferenceInfo.

        会议ID。

        :return: The conference_id of this QosConferenceInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this QosConferenceInfo.

        会议ID。

        :param conference_id: The conference_id of this QosConferenceInfo.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def subject(self):
        """Gets the subject of this QosConferenceInfo.

        会议主题。

        :return: The subject of this QosConferenceInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this QosConferenceInfo.

        会议主题。

        :param subject: The subject of this QosConferenceInfo.
        :type subject: str
        """
        self._subject = subject

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this QosConferenceInfo.

        会议预订者名称。

        :return: The scheduser_name of this QosConferenceInfo.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this QosConferenceInfo.

        会议预订者名称。

        :param scheduser_name: The scheduser_name of this QosConferenceInfo.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def dept_name(self):
        """Gets the dept_name of this QosConferenceInfo.

        部门名称。

        :return: The dept_name of this QosConferenceInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this QosConferenceInfo.

        部门名称。

        :param dept_name: The dept_name of this QosConferenceInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def alarm(self):
        """Gets the alarm of this QosConferenceInfo.

        总体告警 。 * YES：会议的音频、视频、屏幕共享、CPU任一项产生告警，总体告警就为YES * NO：无告警

        :return: The alarm of this QosConferenceInfo.
        :rtype: str
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """Sets the alarm of this QosConferenceInfo.

        总体告警 。 * YES：会议的音频、视频、屏幕共享、CPU任一项产生告警，总体告警就为YES * NO：无告警

        :param alarm: The alarm of this QosConferenceInfo.
        :type alarm: str
        """
        self._alarm = alarm

    @property
    def audio_alarm(self):
        """Gets the audio_alarm of this QosConferenceInfo.

        音频告警 。 * YES：会议中任一与会者存在音频告警，会议音频告警就为YES * NO：无音频告警

        :return: The audio_alarm of this QosConferenceInfo.
        :rtype: str
        """
        return self._audio_alarm

    @audio_alarm.setter
    def audio_alarm(self, audio_alarm):
        """Sets the audio_alarm of this QosConferenceInfo.

        音频告警 。 * YES：会议中任一与会者存在音频告警，会议音频告警就为YES * NO：无音频告警

        :param audio_alarm: The audio_alarm of this QosConferenceInfo.
        :type audio_alarm: str
        """
        self._audio_alarm = audio_alarm

    @property
    def video_alarm(self):
        """Gets the video_alarm of this QosConferenceInfo.

        视频告警。 * YES：会议中任一与会者存在视频告警，会议视频告警就为YES * NO：无音视频警

        :return: The video_alarm of this QosConferenceInfo.
        :rtype: str
        """
        return self._video_alarm

    @video_alarm.setter
    def video_alarm(self, video_alarm):
        """Sets the video_alarm of this QosConferenceInfo.

        视频告警。 * YES：会议中任一与会者存在视频告警，会议视频告警就为YES * NO：无音视频警

        :param video_alarm: The video_alarm of this QosConferenceInfo.
        :type video_alarm: str
        """
        self._video_alarm = video_alarm

    @property
    def screen_alarm(self):
        """Gets the screen_alarm of this QosConferenceInfo.

        屏幕共享告警 YES/NO。 * YES：会议中任一与会者存在屏幕共享告警，会议屏幕共享告警就为YES * NO：无屏幕共享告警

        :return: The screen_alarm of this QosConferenceInfo.
        :rtype: str
        """
        return self._screen_alarm

    @screen_alarm.setter
    def screen_alarm(self, screen_alarm):
        """Sets the screen_alarm of this QosConferenceInfo.

        屏幕共享告警 YES/NO。 * YES：会议中任一与会者存在屏幕共享告警，会议屏幕共享告警就为YES * NO：无屏幕共享告警

        :param screen_alarm: The screen_alarm of this QosConferenceInfo.
        :type screen_alarm: str
        """
        self._screen_alarm = screen_alarm

    @property
    def cpu_alarm(self):
        """Gets the cpu_alarm of this QosConferenceInfo.

        CPU告警。 * YES：会议中任一与会者存在CPU告警，会议CPU告警就为YES * NO：无CPU告警

        :return: The cpu_alarm of this QosConferenceInfo.
        :rtype: str
        """
        return self._cpu_alarm

    @cpu_alarm.setter
    def cpu_alarm(self, cpu_alarm):
        """Sets the cpu_alarm of this QosConferenceInfo.

        CPU告警。 * YES：会议中任一与会者存在CPU告警，会议CPU告警就为YES * NO：无CPU告警

        :param cpu_alarm: The cpu_alarm of this QosConferenceInfo.
        :type cpu_alarm: str
        """
        self._cpu_alarm = cpu_alarm

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this QosConferenceInfo.

        时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :return: The time_zone_id of this QosConferenceInfo.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this QosConferenceInfo.

        时区信息，参考[[时区映射关系](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hws)[[时区映射关系](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html#ZH-CN_TOPIC_0212714472__table137407441463)](tag:hk)。 > 举例：“timeZoneID”:\"26\"，则通过华为云会议发送的会议通知中的时间将会标记为如“2021/11/11 星期四 00:00 - 02:00 (GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦”。 

        :param time_zone_id: The time_zone_id of this QosConferenceInfo.
        :type time_zone_id: str
        """
        self._time_zone_id = time_zone_id

    @property
    def start_time(self):
        """Gets the start_time of this QosConferenceInfo.

        会议开始时间(UTC时间), Unix时间戳（单位毫秒）。

        :return: The start_time of this QosConferenceInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QosConferenceInfo.

        会议开始时间(UTC时间), Unix时间戳（单位毫秒）。

        :param start_time: The start_time of this QosConferenceInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QosConferenceInfo.

        会议结束时间(UTC时间), Unix时间戳（单位毫秒）。 > * 在线会议：会议召开中，endTime = 会议预计结束时间 > * 历史会议：会议已结束，endTime = 会议实际结束时间

        :return: The end_time of this QosConferenceInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QosConferenceInfo.

        会议结束时间(UTC时间), Unix时间戳（单位毫秒）。 > * 在线会议：会议召开中，endTime = 会议预计结束时间 > * 历史会议：会议已结束，endTime = 会议实际结束时间

        :param end_time: The end_time of this QosConferenceInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this QosConferenceInfo.

        会议召开时长（分钟）。 > * 在线会议：会议召开中，duration = 0 > * 历史会议：会议已结束，duration = 会议实际召开时间

        :return: The duration of this QosConferenceInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this QosConferenceInfo.

        会议召开时长（分钟）。 > * 在线会议：会议召开中，duration = 0 > * 历史会议：会议已结束，duration = 会议实际召开时间

        :param duration: The duration of this QosConferenceInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def participants(self):
        """Gets the participants of this QosConferenceInfo.

        与会方数。 > 同一用户多次进出会议属于不同的与会方，与会方数计算多次。

        :return: The participants of this QosConferenceInfo.
        :rtype: int
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this QosConferenceInfo.

        与会方数。 > 同一用户多次进出会议属于不同的与会方，与会方数计算多次。

        :param participants: The participants of this QosConferenceInfo.
        :type participants: int
        """
        self._participants = participants

    @property
    def webinar(self):
        """Gets the webinar of this QosConferenceInfo.

        是否网络研讨会。

        :return: The webinar of this QosConferenceInfo.
        :rtype: bool
        """
        return self._webinar

    @webinar.setter
    def webinar(self, webinar):
        """Sets the webinar of this QosConferenceInfo.

        是否网络研讨会。

        :param webinar: The webinar of this QosConferenceInfo.
        :type webinar: bool
        """
        self._webinar = webinar

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
        if not isinstance(other, QosConferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
