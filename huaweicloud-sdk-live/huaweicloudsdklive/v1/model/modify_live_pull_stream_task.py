# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyLivePullStreamTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'source_urls': 'list[str]',
        'vod_loop_time': 'str',
        'vod_refresh_type': 'str',
        'vod_start_video_index': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'vod_start_video_time': 'int',
        'callback_events': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'source_urls': 'source_urls',
        'vod_loop_time': 'vod_loop_time',
        'vod_refresh_type': 'vod_refresh_type',
        'vod_start_video_index': 'vod_start_video_index',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vod_start_video_time': 'vod_start_video_time',
        'callback_events': 'callback_events'
    }

    def __init__(self, task_id=None, status=None, source_urls=None, vod_loop_time=None, vod_refresh_type=None, vod_start_video_index=None, start_time=None, end_time=None, vod_start_video_time=None, callback_events=None):
        r"""ModifyLivePullStreamTask

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param status: pause停用/enable启用
        :type status: str
        :param source_urls: 拉流源URL
        :type source_urls: list[str]
        :param vod_loop_time: 缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\&quot;\&quot;）时按缺省值生效
        :type vod_loop_time: str
        :param vod_refresh_type: 缺省值 immediate_new_source，可选 immediate_new_source、continue_from_file_start、continue_from_break_point
        :type vod_refresh_type: str
        :param vod_start_video_index: 缺省值 0，指定播放文件的下标，从0开始表示第一个文件，最大值 len(source_urls)-1
        :type vod_start_video_index: int
        :param start_time: 任务启动时间，时间格式： \&quot;2006-01-02T15:04:05Z\&quot; 必须小于结束时间，缺省为当前时间
        :type start_time: datetime
        :param end_time: 任务结束时间，时间格式： \&quot;2006-01-02T15:04:05Z\&quot; 必须大于开始时间，至多为开始时间+7天
        :type end_time: datetime
        :param vod_start_video_time: 缺省值 0，指定从上述指定文件的第几秒开始播放
        :type vod_start_video_time: int
        :param callback_events: 要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart 仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish 仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig 仅PullVodPushLive可用，任务更新 - TaskAlarm: 用于告警事件通知
        :type callback_events: list[str]
        """
        
        

        self._task_id = None
        self._status = None
        self._source_urls = None
        self._vod_loop_time = None
        self._vod_refresh_type = None
        self._vod_start_video_index = None
        self._start_time = None
        self._end_time = None
        self._vod_start_video_time = None
        self._callback_events = None
        self.discriminator = None

        self.task_id = task_id
        if status is not None:
            self.status = status
        if source_urls is not None:
            self.source_urls = source_urls
        if vod_loop_time is not None:
            self.vod_loop_time = vod_loop_time
        if vod_refresh_type is not None:
            self.vod_refresh_type = vod_refresh_type
        if vod_start_video_index is not None:
            self.vod_start_video_index = vod_start_video_index
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vod_start_video_time is not None:
            self.vod_start_video_time = vod_start_video_time
        if callback_events is not None:
            self.callback_events = callback_events

    @property
    def task_id(self):
        r"""Gets the task_id of this ModifyLivePullStreamTask.

        任务id

        :return: The task_id of this ModifyLivePullStreamTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ModifyLivePullStreamTask.

        任务id

        :param task_id: The task_id of this ModifyLivePullStreamTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ModifyLivePullStreamTask.

        pause停用/enable启用

        :return: The status of this ModifyLivePullStreamTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModifyLivePullStreamTask.

        pause停用/enable启用

        :param status: The status of this ModifyLivePullStreamTask.
        :type status: str
        """
        self._status = status

    @property
    def source_urls(self):
        r"""Gets the source_urls of this ModifyLivePullStreamTask.

        拉流源URL

        :return: The source_urls of this ModifyLivePullStreamTask.
        :rtype: list[str]
        """
        return self._source_urls

    @source_urls.setter
    def source_urls(self, source_urls):
        r"""Sets the source_urls of this ModifyLivePullStreamTask.

        拉流源URL

        :param source_urls: The source_urls of this ModifyLivePullStreamTask.
        :type source_urls: list[str]
        """
        self._source_urls = source_urls

    @property
    def vod_loop_time(self):
        r"""Gets the vod_loop_time of this ModifyLivePullStreamTask.

        缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\"\"）时按缺省值生效

        :return: The vod_loop_time of this ModifyLivePullStreamTask.
        :rtype: str
        """
        return self._vod_loop_time

    @vod_loop_time.setter
    def vod_loop_time(self, vod_loop_time):
        r"""Sets the vod_loop_time of this ModifyLivePullStreamTask.

        缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\"\"）时按缺省值生效

        :param vod_loop_time: The vod_loop_time of this ModifyLivePullStreamTask.
        :type vod_loop_time: str
        """
        self._vod_loop_time = vod_loop_time

    @property
    def vod_refresh_type(self):
        r"""Gets the vod_refresh_type of this ModifyLivePullStreamTask.

        缺省值 immediate_new_source，可选 immediate_new_source、continue_from_file_start、continue_from_break_point

        :return: The vod_refresh_type of this ModifyLivePullStreamTask.
        :rtype: str
        """
        return self._vod_refresh_type

    @vod_refresh_type.setter
    def vod_refresh_type(self, vod_refresh_type):
        r"""Sets the vod_refresh_type of this ModifyLivePullStreamTask.

        缺省值 immediate_new_source，可选 immediate_new_source、continue_from_file_start、continue_from_break_point

        :param vod_refresh_type: The vod_refresh_type of this ModifyLivePullStreamTask.
        :type vod_refresh_type: str
        """
        self._vod_refresh_type = vod_refresh_type

    @property
    def vod_start_video_index(self):
        r"""Gets the vod_start_video_index of this ModifyLivePullStreamTask.

        缺省值 0，指定播放文件的下标，从0开始表示第一个文件，最大值 len(source_urls)-1

        :return: The vod_start_video_index of this ModifyLivePullStreamTask.
        :rtype: int
        """
        return self._vod_start_video_index

    @vod_start_video_index.setter
    def vod_start_video_index(self, vod_start_video_index):
        r"""Sets the vod_start_video_index of this ModifyLivePullStreamTask.

        缺省值 0，指定播放文件的下标，从0开始表示第一个文件，最大值 len(source_urls)-1

        :param vod_start_video_index: The vod_start_video_index of this ModifyLivePullStreamTask.
        :type vod_start_video_index: int
        """
        self._vod_start_video_index = vod_start_video_index

    @property
    def start_time(self):
        r"""Gets the start_time of this ModifyLivePullStreamTask.

        任务启动时间，时间格式： \"2006-01-02T15:04:05Z\" 必须小于结束时间，缺省为当前时间

        :return: The start_time of this ModifyLivePullStreamTask.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ModifyLivePullStreamTask.

        任务启动时间，时间格式： \"2006-01-02T15:04:05Z\" 必须小于结束时间，缺省为当前时间

        :param start_time: The start_time of this ModifyLivePullStreamTask.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ModifyLivePullStreamTask.

        任务结束时间，时间格式： \"2006-01-02T15:04:05Z\" 必须大于开始时间，至多为开始时间+7天

        :return: The end_time of this ModifyLivePullStreamTask.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ModifyLivePullStreamTask.

        任务结束时间，时间格式： \"2006-01-02T15:04:05Z\" 必须大于开始时间，至多为开始时间+7天

        :param end_time: The end_time of this ModifyLivePullStreamTask.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def vod_start_video_time(self):
        r"""Gets the vod_start_video_time of this ModifyLivePullStreamTask.

        缺省值 0，指定从上述指定文件的第几秒开始播放

        :return: The vod_start_video_time of this ModifyLivePullStreamTask.
        :rtype: int
        """
        return self._vod_start_video_time

    @vod_start_video_time.setter
    def vod_start_video_time(self, vod_start_video_time):
        r"""Sets the vod_start_video_time of this ModifyLivePullStreamTask.

        缺省值 0，指定从上述指定文件的第几秒开始播放

        :param vod_start_video_time: The vod_start_video_time of this ModifyLivePullStreamTask.
        :type vod_start_video_time: int
        """
        self._vod_start_video_time = vod_start_video_time

    @property
    def callback_events(self):
        r"""Gets the callback_events of this ModifyLivePullStreamTask.

        要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart 仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish 仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig 仅PullVodPushLive可用，任务更新 - TaskAlarm: 用于告警事件通知

        :return: The callback_events of this ModifyLivePullStreamTask.
        :rtype: list[str]
        """
        return self._callback_events

    @callback_events.setter
    def callback_events(self, callback_events):
        r"""Sets the callback_events of this ModifyLivePullStreamTask.

        要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart 仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish 仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig 仅PullVodPushLive可用，任务更新 - TaskAlarm: 用于告警事件通知

        :param callback_events: The callback_events of this ModifyLivePullStreamTask.
        :type callback_events: list[str]
        """
        self._callback_events = callback_events

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyLivePullStreamTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
