# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIndividualStreamJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'stream_name': 'str',
        'app_id': 'str',
        'room_id': 'str',
        'user_id': 'str',
        'is_record_audio': 'bool',
        'video_type': 'str',
        'select_stream_type': 'str',
        'max_idle_time': 'int',
        'record_param': 'RecordParam',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'stop_reason': 'str',
        'description': 'str',
        'start_time': 'str',
        'stop_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'stream_name': 'stream_name',
        'app_id': 'app_id',
        'room_id': 'room_id',
        'user_id': 'user_id',
        'is_record_audio': 'is_record_audio',
        'video_type': 'video_type',
        'select_stream_type': 'select_stream_type',
        'max_idle_time': 'max_idle_time',
        'record_param': 'record_param',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'stop_reason': 'stop_reason',
        'description': 'description',
        'start_time': 'start_time',
        'stop_time': 'stop_time',
        'x_request_id': 'X-request-Id'
    }

    def __init__(self, job_id=None, stream_name=None, app_id=None, room_id=None, user_id=None, is_record_audio=None, video_type=None, select_stream_type=None, max_idle_time=None, record_param=None, create_time=None, update_time=None, state=None, stop_reason=None, description=None, start_time=None, stop_time=None, x_request_id=None):
        """ShowIndividualStreamJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务编号
        :type job_id: str
        :param stream_name: 流名
        :type stream_name: str
        :param app_id: 应用id
        :type app_id: str
        :param room_id: 房间id
        :type room_id: str
        :param user_id: 选看的用户id，单个录制任务内保证唯一
        :type user_id: str
        :param is_record_audio:  是否录制音频。  - true：录制音频 - false：不录制音频  缺省为true。 
        :type is_record_audio: bool
        :param video_type: 标识视频流的类型，可选摄像头流或者屏幕分享流，未填写表示不录制视频。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 
        :type video_type: str
        :param select_stream_type: 指定窗口拉取的分辨率档位。  - LD - SD - HD - FHD  缺省为FHD。 
        :type select_stream_type: str
        :param max_idle_time: 最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 
        :type max_idle_time: int
        :param record_param: 
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        :param create_time: 创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type create_time: str
        :param update_time: 更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        :param state: 任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 
        :type state: str
        :param stop_reason: 任务结束原因
        :type stop_reason: str
        :param description: 针对任务状态的详细信息描述
        :type description: str
        :param start_time: 任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type start_time: str
        :param stop_time: 任务完成时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type stop_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowIndividualStreamJobResponse, self).__init__()

        self._job_id = None
        self._stream_name = None
        self._app_id = None
        self._room_id = None
        self._user_id = None
        self._is_record_audio = None
        self._video_type = None
        self._select_stream_type = None
        self._max_idle_time = None
        self._record_param = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._stop_reason = None
        self._description = None
        self._start_time = None
        self._stop_time = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if stream_name is not None:
            self.stream_name = stream_name
        if app_id is not None:
            self.app_id = app_id
        if room_id is not None:
            self.room_id = room_id
        if user_id is not None:
            self.user_id = user_id
        if is_record_audio is not None:
            self.is_record_audio = is_record_audio
        if video_type is not None:
            self.video_type = video_type
        if select_stream_type is not None:
            self.select_stream_type = select_stream_type
        if max_idle_time is not None:
            self.max_idle_time = max_idle_time
        if record_param is not None:
            self.record_param = record_param
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if stop_reason is not None:
            self.stop_reason = stop_reason
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowIndividualStreamJobResponse.

        任务编号

        :return: The job_id of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowIndividualStreamJobResponse.

        任务编号

        :param job_id: The job_id of this ShowIndividualStreamJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowIndividualStreamJobResponse.

        流名

        :return: The stream_name of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowIndividualStreamJobResponse.

        流名

        :param stream_name: The stream_name of this ShowIndividualStreamJobResponse.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def app_id(self):
        """Gets the app_id of this ShowIndividualStreamJobResponse.

        应用id

        :return: The app_id of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowIndividualStreamJobResponse.

        应用id

        :param app_id: The app_id of this ShowIndividualStreamJobResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def room_id(self):
        """Gets the room_id of this ShowIndividualStreamJobResponse.

        房间id

        :return: The room_id of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ShowIndividualStreamJobResponse.

        房间id

        :param room_id: The room_id of this ShowIndividualStreamJobResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def user_id(self):
        """Gets the user_id of this ShowIndividualStreamJobResponse.

        选看的用户id，单个录制任务内保证唯一

        :return: The user_id of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowIndividualStreamJobResponse.

        选看的用户id，单个录制任务内保证唯一

        :param user_id: The user_id of this ShowIndividualStreamJobResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def is_record_audio(self):
        """Gets the is_record_audio of this ShowIndividualStreamJobResponse.

         是否录制音频。  - true：录制音频 - false：不录制音频  缺省为true。 

        :return: The is_record_audio of this ShowIndividualStreamJobResponse.
        :rtype: bool
        """
        return self._is_record_audio

    @is_record_audio.setter
    def is_record_audio(self, is_record_audio):
        """Sets the is_record_audio of this ShowIndividualStreamJobResponse.

         是否录制音频。  - true：录制音频 - false：不录制音频  缺省为true。 

        :param is_record_audio: The is_record_audio of this ShowIndividualStreamJobResponse.
        :type is_record_audio: bool
        """
        self._is_record_audio = is_record_audio

    @property
    def video_type(self):
        """Gets the video_type of this ShowIndividualStreamJobResponse.

        标识视频流的类型，可选摄像头流或者屏幕分享流，未填写表示不录制视频。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :return: The video_type of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this ShowIndividualStreamJobResponse.

        标识视频流的类型，可选摄像头流或者屏幕分享流，未填写表示不录制视频。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :param video_type: The video_type of this ShowIndividualStreamJobResponse.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def select_stream_type(self):
        """Gets the select_stream_type of this ShowIndividualStreamJobResponse.

        指定窗口拉取的分辨率档位。  - LD - SD - HD - FHD  缺省为FHD。 

        :return: The select_stream_type of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._select_stream_type

    @select_stream_type.setter
    def select_stream_type(self, select_stream_type):
        """Sets the select_stream_type of this ShowIndividualStreamJobResponse.

        指定窗口拉取的分辨率档位。  - LD - SD - HD - FHD  缺省为FHD。 

        :param select_stream_type: The select_stream_type of this ShowIndividualStreamJobResponse.
        :type select_stream_type: str
        """
        self._select_stream_type = select_stream_type

    @property
    def max_idle_time(self):
        """Gets the max_idle_time of this ShowIndividualStreamJobResponse.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :return: The max_idle_time of this ShowIndividualStreamJobResponse.
        :rtype: int
        """
        return self._max_idle_time

    @max_idle_time.setter
    def max_idle_time(self, max_idle_time):
        """Sets the max_idle_time of this ShowIndividualStreamJobResponse.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :param max_idle_time: The max_idle_time of this ShowIndividualStreamJobResponse.
        :type max_idle_time: int
        """
        self._max_idle_time = max_idle_time

    @property
    def record_param(self):
        """Gets the record_param of this ShowIndividualStreamJobResponse.


        :return: The record_param of this ShowIndividualStreamJobResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        return self._record_param

    @record_param.setter
    def record_param(self, record_param):
        """Sets the record_param of this ShowIndividualStreamJobResponse.


        :param record_param: The record_param of this ShowIndividualStreamJobResponse.
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        self._record_param = record_param

    @property
    def create_time(self):
        """Gets the create_time of this ShowIndividualStreamJobResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The create_time of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowIndividualStreamJobResponse.

        创建时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param create_time: The create_time of this ShowIndividualStreamJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowIndividualStreamJobResponse.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowIndividualStreamJobResponse.

        更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this ShowIndividualStreamJobResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this ShowIndividualStreamJobResponse.

        任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 

        :return: The state of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowIndividualStreamJobResponse.

        任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 

        :param state: The state of this ShowIndividualStreamJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def stop_reason(self):
        """Gets the stop_reason of this ShowIndividualStreamJobResponse.

        任务结束原因

        :return: The stop_reason of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._stop_reason

    @stop_reason.setter
    def stop_reason(self, stop_reason):
        """Sets the stop_reason of this ShowIndividualStreamJobResponse.

        任务结束原因

        :param stop_reason: The stop_reason of this ShowIndividualStreamJobResponse.
        :type stop_reason: str
        """
        self._stop_reason = stop_reason

    @property
    def description(self):
        """Gets the description of this ShowIndividualStreamJobResponse.

        针对任务状态的详细信息描述

        :return: The description of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowIndividualStreamJobResponse.

        针对任务状态的详细信息描述

        :param description: The description of this ShowIndividualStreamJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this ShowIndividualStreamJobResponse.

        任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The start_time of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowIndividualStreamJobResponse.

        任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param start_time: The start_time of this ShowIndividualStreamJobResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this ShowIndividualStreamJobResponse.

        任务完成时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The stop_time of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this ShowIndividualStreamJobResponse.

        任务完成时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param stop_time: The stop_time of this ShowIndividualStreamJobResponse.
        :type stop_time: str
        """
        self._stop_time = stop_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowIndividualStreamJobResponse.


        :return: The x_request_id of this ShowIndividualStreamJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowIndividualStreamJobResponse.


        :param x_request_id: The x_request_id of this ShowIndividualStreamJobResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowIndividualStreamJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
