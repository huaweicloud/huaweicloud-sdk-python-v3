# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LivePullStreamTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'source_type': 'str',
        'source_urls': 'list[str]',
        'domain': 'str',
        'app_name': 'str',
        'stream_name': 'str',
        'push_args': 'str',
        'destination_url': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'vod_loop_time': 'str',
        'vod_refresh_type': 'str',
        'vod_start_video_index': 'int',
        'vod_start_video_time': 'int',
        'backup_source_type': 'str',
        'backup_source_urls': 'list[str]',
        'callback_events': 'list[str]',
        'callback_url': 'str'
    }

    attribute_map = {
        'region': 'region',
        'source_type': 'source_type',
        'source_urls': 'source_urls',
        'domain': 'domain',
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'push_args': 'push_args',
        'destination_url': 'destination_url',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vod_loop_time': 'vod_loop_time',
        'vod_refresh_type': 'vod_refresh_type',
        'vod_start_video_index': 'vod_start_video_index',
        'vod_start_video_time': 'vod_start_video_time',
        'backup_source_type': 'backup_source_type',
        'backup_source_urls': 'backup_source_urls',
        'callback_events': 'callback_events',
        'callback_url': 'callback_url'
    }

    def __init__(self, region=None, source_type=None, source_urls=None, domain=None, app_name=None, stream_name=None, push_args=None, destination_url=None, start_time=None, end_time=None, vod_loop_time=None, vod_refresh_type=None, vod_start_video_index=None, vod_start_video_time=None, backup_source_type=None, backup_source_urls=None, callback_events=None, callback_url=None):
        r"""LivePullStreamTask

        The model defined in huaweicloud sdk

        :param region: 任务执行区域，如果指定推流域名，则region需要与推流域名直播源站一致，缺省为租户归属region
        :type region: str
        :param source_type: 拉流源类型 PullLivePushLive：拉转推（拉直播推直播） PullVodPushLive：轮播（拉点播推直播）
        :type source_type: str
        :param source_urls: 拉流源URL 当 source_type 为 PullLivePushLive 时，只能填写一个URL 当 source_type 为 PullVodPushLive 时，可以指定多个轮播源文件URL
        :type source_urls: list[str]
        :param domain: 推流域名
        :type domain: str
        :param app_name: 推流app
        :type app_name: str
        :param stream_name: 推流流名
        :type stream_name: str
        :param push_args: 推流参数
        :type push_args: str
        :param destination_url: 完整的目标URL。 如果指定此参数，domain、app_name和stream_name需要传入空字符串或不传。
        :type destination_url: str
        :param start_time: 任务启动时间，时间格式： \&quot;2006-01-02T15:04:05Z\&quot; 必须小于结束时间，缺省为当前时间
        :type start_time: datetime
        :param end_time: 任务结束时间，时间格式： \&quot;2006-01-02T15:04:05Z\&quot; 必须大于开始时间，至多为开始时间+7天
        :type end_time: datetime
        :param vod_loop_time: 轮播播放次数，仅当source_type为PullVodPushLive生效。缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\&quot;\&quot;）时按缺省值生效
        :type vod_loop_time: str
        :param vod_refresh_type: 轮播文件播放形式，仅当source_type为PullVodPushLive生效。缺省值immediate_new_source immediate_new_source：立即播放新的文件源 continue_from_file_start：从上次断流URL文件重新播放（更新任务时有效） continue_from_break_point：从上次断流URL文件断流位置重新播放（更新任务时有效）
        :type vod_refresh_type: str
        :param vod_start_video_index: 指定播放文件的下标，仅当source_type为PullVodPushLive生效。缺省值 0，从0开始表示第一个文件，最大值 len(source_urls)-1
        :type vod_start_video_index: int
        :param vod_start_video_time: 缺省值 0，指定从上述指定文件的第几秒开始播放，仅当source_type为PullVodPushLive生效
        :type vod_start_video_time: int
        :param backup_source_type: 备源的类型 - PullLivePushLive：直播 注意事项： 1. 仅当source_type为PullVodPushLive生效。 2. 主直播源拉流中断时，自动使用备源进行拉流。
        :type backup_source_type: str
        :param backup_source_urls: 备源URL，仅当source_type为PullVodPushLive生效。
        :type backup_source_urls: list[str]
        :param callback_events: 要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart：仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish：仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig：仅PullVodPushLive可用，任务更新 - TaskAlarm：用于告警事件通知
        :type callback_events: list[str]
        :param callback_url: 回调接收地址
        :type callback_url: str
        """
        
        

        self._region = None
        self._source_type = None
        self._source_urls = None
        self._domain = None
        self._app_name = None
        self._stream_name = None
        self._push_args = None
        self._destination_url = None
        self._start_time = None
        self._end_time = None
        self._vod_loop_time = None
        self._vod_refresh_type = None
        self._vod_start_video_index = None
        self._vod_start_video_time = None
        self._backup_source_type = None
        self._backup_source_urls = None
        self._callback_events = None
        self._callback_url = None
        self.discriminator = None

        if region is not None:
            self.region = region
        self.source_type = source_type
        self.source_urls = source_urls
        if domain is not None:
            self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if stream_name is not None:
            self.stream_name = stream_name
        if push_args is not None:
            self.push_args = push_args
        if destination_url is not None:
            self.destination_url = destination_url
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vod_loop_time is not None:
            self.vod_loop_time = vod_loop_time
        if vod_refresh_type is not None:
            self.vod_refresh_type = vod_refresh_type
        if vod_start_video_index is not None:
            self.vod_start_video_index = vod_start_video_index
        if vod_start_video_time is not None:
            self.vod_start_video_time = vod_start_video_time
        if backup_source_type is not None:
            self.backup_source_type = backup_source_type
        if backup_source_urls is not None:
            self.backup_source_urls = backup_source_urls
        if callback_events is not None:
            self.callback_events = callback_events
        if callback_url is not None:
            self.callback_url = callback_url

    @property
    def region(self):
        r"""Gets the region of this LivePullStreamTask.

        任务执行区域，如果指定推流域名，则region需要与推流域名直播源站一致，缺省为租户归属region

        :return: The region of this LivePullStreamTask.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this LivePullStreamTask.

        任务执行区域，如果指定推流域名，则region需要与推流域名直播源站一致，缺省为租户归属region

        :param region: The region of this LivePullStreamTask.
        :type region: str
        """
        self._region = region

    @property
    def source_type(self):
        r"""Gets the source_type of this LivePullStreamTask.

        拉流源类型 PullLivePushLive：拉转推（拉直播推直播） PullVodPushLive：轮播（拉点播推直播）

        :return: The source_type of this LivePullStreamTask.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this LivePullStreamTask.

        拉流源类型 PullLivePushLive：拉转推（拉直播推直播） PullVodPushLive：轮播（拉点播推直播）

        :param source_type: The source_type of this LivePullStreamTask.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_urls(self):
        r"""Gets the source_urls of this LivePullStreamTask.

        拉流源URL 当 source_type 为 PullLivePushLive 时，只能填写一个URL 当 source_type 为 PullVodPushLive 时，可以指定多个轮播源文件URL

        :return: The source_urls of this LivePullStreamTask.
        :rtype: list[str]
        """
        return self._source_urls

    @source_urls.setter
    def source_urls(self, source_urls):
        r"""Sets the source_urls of this LivePullStreamTask.

        拉流源URL 当 source_type 为 PullLivePushLive 时，只能填写一个URL 当 source_type 为 PullVodPushLive 时，可以指定多个轮播源文件URL

        :param source_urls: The source_urls of this LivePullStreamTask.
        :type source_urls: list[str]
        """
        self._source_urls = source_urls

    @property
    def domain(self):
        r"""Gets the domain of this LivePullStreamTask.

        推流域名

        :return: The domain of this LivePullStreamTask.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this LivePullStreamTask.

        推流域名

        :param domain: The domain of this LivePullStreamTask.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this LivePullStreamTask.

        推流app

        :return: The app_name of this LivePullStreamTask.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this LivePullStreamTask.

        推流app

        :param app_name: The app_name of this LivePullStreamTask.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        r"""Gets the stream_name of this LivePullStreamTask.

        推流流名

        :return: The stream_name of this LivePullStreamTask.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this LivePullStreamTask.

        推流流名

        :param stream_name: The stream_name of this LivePullStreamTask.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def push_args(self):
        r"""Gets the push_args of this LivePullStreamTask.

        推流参数

        :return: The push_args of this LivePullStreamTask.
        :rtype: str
        """
        return self._push_args

    @push_args.setter
    def push_args(self, push_args):
        r"""Sets the push_args of this LivePullStreamTask.

        推流参数

        :param push_args: The push_args of this LivePullStreamTask.
        :type push_args: str
        """
        self._push_args = push_args

    @property
    def destination_url(self):
        r"""Gets the destination_url of this LivePullStreamTask.

        完整的目标URL。 如果指定此参数，domain、app_name和stream_name需要传入空字符串或不传。

        :return: The destination_url of this LivePullStreamTask.
        :rtype: str
        """
        return self._destination_url

    @destination_url.setter
    def destination_url(self, destination_url):
        r"""Sets the destination_url of this LivePullStreamTask.

        完整的目标URL。 如果指定此参数，domain、app_name和stream_name需要传入空字符串或不传。

        :param destination_url: The destination_url of this LivePullStreamTask.
        :type destination_url: str
        """
        self._destination_url = destination_url

    @property
    def start_time(self):
        r"""Gets the start_time of this LivePullStreamTask.

        任务启动时间，时间格式： \"2006-01-02T15:04:05Z\" 必须小于结束时间，缺省为当前时间

        :return: The start_time of this LivePullStreamTask.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this LivePullStreamTask.

        任务启动时间，时间格式： \"2006-01-02T15:04:05Z\" 必须小于结束时间，缺省为当前时间

        :param start_time: The start_time of this LivePullStreamTask.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this LivePullStreamTask.

        任务结束时间，时间格式： \"2006-01-02T15:04:05Z\" 必须大于开始时间，至多为开始时间+7天

        :return: The end_time of this LivePullStreamTask.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this LivePullStreamTask.

        任务结束时间，时间格式： \"2006-01-02T15:04:05Z\" 必须大于开始时间，至多为开始时间+7天

        :param end_time: The end_time of this LivePullStreamTask.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def vod_loop_time(self):
        r"""Gets the vod_loop_time of this LivePullStreamTask.

        轮播播放次数，仅当source_type为PullVodPushLive生效。缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\"\"）时按缺省值生效

        :return: The vod_loop_time of this LivePullStreamTask.
        :rtype: str
        """
        return self._vod_loop_time

    @vod_loop_time.setter
    def vod_loop_time(self, vod_loop_time):
        r"""Sets the vod_loop_time of this LivePullStreamTask.

        轮播播放次数，仅当source_type为PullVodPushLive生效。缺省值”-1”。-1：无限轮播，以结束时间为准；N：按文件列表播放N轮，以播放完成和结束时间先到的为准。不传、为空（\"\"）时按缺省值生效

        :param vod_loop_time: The vod_loop_time of this LivePullStreamTask.
        :type vod_loop_time: str
        """
        self._vod_loop_time = vod_loop_time

    @property
    def vod_refresh_type(self):
        r"""Gets the vod_refresh_type of this LivePullStreamTask.

        轮播文件播放形式，仅当source_type为PullVodPushLive生效。缺省值immediate_new_source immediate_new_source：立即播放新的文件源 continue_from_file_start：从上次断流URL文件重新播放（更新任务时有效） continue_from_break_point：从上次断流URL文件断流位置重新播放（更新任务时有效）

        :return: The vod_refresh_type of this LivePullStreamTask.
        :rtype: str
        """
        return self._vod_refresh_type

    @vod_refresh_type.setter
    def vod_refresh_type(self, vod_refresh_type):
        r"""Sets the vod_refresh_type of this LivePullStreamTask.

        轮播文件播放形式，仅当source_type为PullVodPushLive生效。缺省值immediate_new_source immediate_new_source：立即播放新的文件源 continue_from_file_start：从上次断流URL文件重新播放（更新任务时有效） continue_from_break_point：从上次断流URL文件断流位置重新播放（更新任务时有效）

        :param vod_refresh_type: The vod_refresh_type of this LivePullStreamTask.
        :type vod_refresh_type: str
        """
        self._vod_refresh_type = vod_refresh_type

    @property
    def vod_start_video_index(self):
        r"""Gets the vod_start_video_index of this LivePullStreamTask.

        指定播放文件的下标，仅当source_type为PullVodPushLive生效。缺省值 0，从0开始表示第一个文件，最大值 len(source_urls)-1

        :return: The vod_start_video_index of this LivePullStreamTask.
        :rtype: int
        """
        return self._vod_start_video_index

    @vod_start_video_index.setter
    def vod_start_video_index(self, vod_start_video_index):
        r"""Sets the vod_start_video_index of this LivePullStreamTask.

        指定播放文件的下标，仅当source_type为PullVodPushLive生效。缺省值 0，从0开始表示第一个文件，最大值 len(source_urls)-1

        :param vod_start_video_index: The vod_start_video_index of this LivePullStreamTask.
        :type vod_start_video_index: int
        """
        self._vod_start_video_index = vod_start_video_index

    @property
    def vod_start_video_time(self):
        r"""Gets the vod_start_video_time of this LivePullStreamTask.

        缺省值 0，指定从上述指定文件的第几秒开始播放，仅当source_type为PullVodPushLive生效

        :return: The vod_start_video_time of this LivePullStreamTask.
        :rtype: int
        """
        return self._vod_start_video_time

    @vod_start_video_time.setter
    def vod_start_video_time(self, vod_start_video_time):
        r"""Sets the vod_start_video_time of this LivePullStreamTask.

        缺省值 0，指定从上述指定文件的第几秒开始播放，仅当source_type为PullVodPushLive生效

        :param vod_start_video_time: The vod_start_video_time of this LivePullStreamTask.
        :type vod_start_video_time: int
        """
        self._vod_start_video_time = vod_start_video_time

    @property
    def backup_source_type(self):
        r"""Gets the backup_source_type of this LivePullStreamTask.

        备源的类型 - PullLivePushLive：直播 注意事项： 1. 仅当source_type为PullVodPushLive生效。 2. 主直播源拉流中断时，自动使用备源进行拉流。

        :return: The backup_source_type of this LivePullStreamTask.
        :rtype: str
        """
        return self._backup_source_type

    @backup_source_type.setter
    def backup_source_type(self, backup_source_type):
        r"""Sets the backup_source_type of this LivePullStreamTask.

        备源的类型 - PullLivePushLive：直播 注意事项： 1. 仅当source_type为PullVodPushLive生效。 2. 主直播源拉流中断时，自动使用备源进行拉流。

        :param backup_source_type: The backup_source_type of this LivePullStreamTask.
        :type backup_source_type: str
        """
        self._backup_source_type = backup_source_type

    @property
    def backup_source_urls(self):
        r"""Gets the backup_source_urls of this LivePullStreamTask.

        备源URL，仅当source_type为PullVodPushLive生效。

        :return: The backup_source_urls of this LivePullStreamTask.
        :rtype: list[str]
        """
        return self._backup_source_urls

    @backup_source_urls.setter
    def backup_source_urls(self, backup_source_urls):
        r"""Sets the backup_source_urls of this LivePullStreamTask.

        备源URL，仅当source_type为PullVodPushLive生效。

        :param backup_source_urls: The backup_source_urls of this LivePullStreamTask.
        :type backup_source_urls: list[str]
        """
        self._backup_source_urls = backup_source_urls

    @property
    def callback_events(self):
        r"""Gets the callback_events of this LivePullStreamTask.

        要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart：仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish：仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig：仅PullVodPushLive可用，任务更新 - TaskAlarm：用于告警事件通知

        :return: The callback_events of this LivePullStreamTask.
        :rtype: list[str]
        """
        return self._callback_events

    @callback_events.setter
    def callback_events(self, callback_events):
        r"""Sets the callback_events of this LivePullStreamTask.

        要回调的事件列表（不填则回调全部） - TaskStart：任务启动回调 - TaskExit：任务停止回调 - VodSourceFileStart：仅PullVodPushLive可用，文件启动切换 - VodSourceFileFinish：仅PullVodPushLive可用，文件播放完毕 - ResetTaskConfig：仅PullVodPushLive可用，任务更新 - TaskAlarm：用于告警事件通知

        :param callback_events: The callback_events of this LivePullStreamTask.
        :type callback_events: list[str]
        """
        self._callback_events = callback_events

    @property
    def callback_url(self):
        r"""Gets the callback_url of this LivePullStreamTask.

        回调接收地址

        :return: The callback_url of this LivePullStreamTask.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this LivePullStreamTask.

        回调接收地址

        :param callback_url: The callback_url of this LivePullStreamTask.
        :type callback_url: str
        """
        self._callback_url = callback_url

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
        if not isinstance(other, LivePullStreamTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
