# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordAuditRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_type': 'str',
        'interval_record_start_time': 'str',
        'interval_record_end_time': 'str',
        'op_type': 'str',
        'audio_record': 'bool',
        'fps': 'str',
        'duration': 'str',
        'resolution': 'str',
        'event_enable': 'bool',
        'file_suffix': 'str',
        'regit_paths': 'str'
    }

    attribute_map = {
        'record_type': 'record_type',
        'interval_record_start_time': 'interval_record_start_time',
        'interval_record_end_time': 'interval_record_end_time',
        'op_type': 'op_type',
        'audio_record': 'audio_record',
        'fps': 'fps',
        'duration': 'duration',
        'resolution': 'resolution',
        'event_enable': 'event_enable',
        'file_suffix': 'file_suffix',
        'regit_paths': 'regit_paths'
    }

    def __init__(self, record_type=None, interval_record_start_time=None, interval_record_end_time=None, op_type=None, audio_record=None, fps=None, duration=None, resolution=None, event_enable=None, file_suffix=None, regit_paths=None):
        """RecordAuditRule

        The model defined in huaweicloud sdk

        :param record_type: 录制类型。取值为： whole：表示全程录屏。 interval：表示间隔录屏。 userOperations：表示用户操作录屏。 sessionMonitoring：监听会话生命周期录屏。
        :type record_type: str
        :param interval_record_start_time: 间隔录制开始时间，仅录制类型为interval时有效 \&quot;hh:mm\&quot;
        :type interval_record_start_time: str
        :param interval_record_end_time: 间隔录制结束时间，仅录制类型为interval时有效格式 \&quot;hh:mm\&quot;
        :type interval_record_end_time: str
        :param op_type: 操作触发类型，仅录制类型为userOperations时有效。取值为： input：表示用户输入内容即启动录屏。 filecopy：表示用户拷贝文件即启动录屏。
        :type op_type: str
        :param audio_record: 是否开启音频录制开关。取值为： false：表示关闭。 true：表示开启。
        :type audio_record: bool
        :param fps: 录制帧率。取值为：2/5/10/15
        :type fps: str
        :param duration: 录制视频单文件时长（分钟）。取值为：10/20/30/60
        :type duration: str
        :param resolution: 分辨率设置。取值为：720P/1080P/original
        :type resolution: str
        :param event_enable: 是否启动关键事件审计。取值为： false：表示关闭。 true：表示开启。
        :type event_enable: bool
        :param file_suffix: 文件后缀，多个用\&quot;|\&quot;分隔
        :type file_suffix: str
        :param regit_paths: 注册表路径，多个用\&quot;|\&quot;分隔
        :type regit_paths: str
        """
        
        

        self._record_type = None
        self._interval_record_start_time = None
        self._interval_record_end_time = None
        self._op_type = None
        self._audio_record = None
        self._fps = None
        self._duration = None
        self._resolution = None
        self._event_enable = None
        self._file_suffix = None
        self._regit_paths = None
        self.discriminator = None

        if record_type is not None:
            self.record_type = record_type
        if interval_record_start_time is not None:
            self.interval_record_start_time = interval_record_start_time
        if interval_record_end_time is not None:
            self.interval_record_end_time = interval_record_end_time
        if op_type is not None:
            self.op_type = op_type
        if audio_record is not None:
            self.audio_record = audio_record
        if fps is not None:
            self.fps = fps
        if duration is not None:
            self.duration = duration
        if resolution is not None:
            self.resolution = resolution
        if event_enable is not None:
            self.event_enable = event_enable
        if file_suffix is not None:
            self.file_suffix = file_suffix
        if regit_paths is not None:
            self.regit_paths = regit_paths

    @property
    def record_type(self):
        """Gets the record_type of this RecordAuditRule.

        录制类型。取值为： whole：表示全程录屏。 interval：表示间隔录屏。 userOperations：表示用户操作录屏。 sessionMonitoring：监听会话生命周期录屏。

        :return: The record_type of this RecordAuditRule.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this RecordAuditRule.

        录制类型。取值为： whole：表示全程录屏。 interval：表示间隔录屏。 userOperations：表示用户操作录屏。 sessionMonitoring：监听会话生命周期录屏。

        :param record_type: The record_type of this RecordAuditRule.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def interval_record_start_time(self):
        """Gets the interval_record_start_time of this RecordAuditRule.

        间隔录制开始时间，仅录制类型为interval时有效 \"hh:mm\"

        :return: The interval_record_start_time of this RecordAuditRule.
        :rtype: str
        """
        return self._interval_record_start_time

    @interval_record_start_time.setter
    def interval_record_start_time(self, interval_record_start_time):
        """Sets the interval_record_start_time of this RecordAuditRule.

        间隔录制开始时间，仅录制类型为interval时有效 \"hh:mm\"

        :param interval_record_start_time: The interval_record_start_time of this RecordAuditRule.
        :type interval_record_start_time: str
        """
        self._interval_record_start_time = interval_record_start_time

    @property
    def interval_record_end_time(self):
        """Gets the interval_record_end_time of this RecordAuditRule.

        间隔录制结束时间，仅录制类型为interval时有效格式 \"hh:mm\"

        :return: The interval_record_end_time of this RecordAuditRule.
        :rtype: str
        """
        return self._interval_record_end_time

    @interval_record_end_time.setter
    def interval_record_end_time(self, interval_record_end_time):
        """Sets the interval_record_end_time of this RecordAuditRule.

        间隔录制结束时间，仅录制类型为interval时有效格式 \"hh:mm\"

        :param interval_record_end_time: The interval_record_end_time of this RecordAuditRule.
        :type interval_record_end_time: str
        """
        self._interval_record_end_time = interval_record_end_time

    @property
    def op_type(self):
        """Gets the op_type of this RecordAuditRule.

        操作触发类型，仅录制类型为userOperations时有效。取值为： input：表示用户输入内容即启动录屏。 filecopy：表示用户拷贝文件即启动录屏。

        :return: The op_type of this RecordAuditRule.
        :rtype: str
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        """Sets the op_type of this RecordAuditRule.

        操作触发类型，仅录制类型为userOperations时有效。取值为： input：表示用户输入内容即启动录屏。 filecopy：表示用户拷贝文件即启动录屏。

        :param op_type: The op_type of this RecordAuditRule.
        :type op_type: str
        """
        self._op_type = op_type

    @property
    def audio_record(self):
        """Gets the audio_record of this RecordAuditRule.

        是否开启音频录制开关。取值为： false：表示关闭。 true：表示开启。

        :return: The audio_record of this RecordAuditRule.
        :rtype: bool
        """
        return self._audio_record

    @audio_record.setter
    def audio_record(self, audio_record):
        """Sets the audio_record of this RecordAuditRule.

        是否开启音频录制开关。取值为： false：表示关闭。 true：表示开启。

        :param audio_record: The audio_record of this RecordAuditRule.
        :type audio_record: bool
        """
        self._audio_record = audio_record

    @property
    def fps(self):
        """Gets the fps of this RecordAuditRule.

        录制帧率。取值为：2/5/10/15

        :return: The fps of this RecordAuditRule.
        :rtype: str
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this RecordAuditRule.

        录制帧率。取值为：2/5/10/15

        :param fps: The fps of this RecordAuditRule.
        :type fps: str
        """
        self._fps = fps

    @property
    def duration(self):
        """Gets the duration of this RecordAuditRule.

        录制视频单文件时长（分钟）。取值为：10/20/30/60

        :return: The duration of this RecordAuditRule.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RecordAuditRule.

        录制视频单文件时长（分钟）。取值为：10/20/30/60

        :param duration: The duration of this RecordAuditRule.
        :type duration: str
        """
        self._duration = duration

    @property
    def resolution(self):
        """Gets the resolution of this RecordAuditRule.

        分辨率设置。取值为：720P/1080P/original

        :return: The resolution of this RecordAuditRule.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this RecordAuditRule.

        分辨率设置。取值为：720P/1080P/original

        :param resolution: The resolution of this RecordAuditRule.
        :type resolution: str
        """
        self._resolution = resolution

    @property
    def event_enable(self):
        """Gets the event_enable of this RecordAuditRule.

        是否启动关键事件审计。取值为： false：表示关闭。 true：表示开启。

        :return: The event_enable of this RecordAuditRule.
        :rtype: bool
        """
        return self._event_enable

    @event_enable.setter
    def event_enable(self, event_enable):
        """Sets the event_enable of this RecordAuditRule.

        是否启动关键事件审计。取值为： false：表示关闭。 true：表示开启。

        :param event_enable: The event_enable of this RecordAuditRule.
        :type event_enable: bool
        """
        self._event_enable = event_enable

    @property
    def file_suffix(self):
        """Gets the file_suffix of this RecordAuditRule.

        文件后缀，多个用\"|\"分隔

        :return: The file_suffix of this RecordAuditRule.
        :rtype: str
        """
        return self._file_suffix

    @file_suffix.setter
    def file_suffix(self, file_suffix):
        """Sets the file_suffix of this RecordAuditRule.

        文件后缀，多个用\"|\"分隔

        :param file_suffix: The file_suffix of this RecordAuditRule.
        :type file_suffix: str
        """
        self._file_suffix = file_suffix

    @property
    def regit_paths(self):
        """Gets the regit_paths of this RecordAuditRule.

        注册表路径，多个用\"|\"分隔

        :return: The regit_paths of this RecordAuditRule.
        :rtype: str
        """
        return self._regit_paths

    @regit_paths.setter
    def regit_paths(self, regit_paths):
        """Sets the regit_paths of this RecordAuditRule.

        注册表路径，多个用\"|\"分隔

        :param regit_paths: The regit_paths of this RecordAuditRule.
        :type regit_paths: str
        """
        self._regit_paths = regit_paths

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
        if not isinstance(other, RecordAuditRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
