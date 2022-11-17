# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMixJobResponse(SdkResponse):

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
        'mix_param': 'MixParam',
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
        'mix_param': 'mix_param',
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

    def __init__(self, job_id=None, stream_name=None, app_id=None, room_id=None, mix_param=None, record_param=None, create_time=None, update_time=None, state=None, stop_reason=None, description=None, start_time=None, stop_time=None, x_request_id=None):
        """CreateMixJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务编号，可以用于修改、查看和停止合流任务
        :type job_id: str
        :param stream_name: 流名
        :type stream_name: str
        :param app_id: 应用id
        :type app_id: str
        :param room_id: 房间id
        :type room_id: str
        :param mix_param: 
        :type mix_param: :class:`huaweicloudsdkcloudrtc.v2.MixParam`
        :param record_param: 
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        :param create_time: 任务创建的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type create_time: str
        :param update_time: 任务中的布局更新的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        :param state: 任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 
        :type state: str
        :param stop_reason: 任务结束原因
        :type stop_reason: str
        :param description: 状态描述，对state字段的一些补充说明，可用于人工查阅。
        :type description: str
        :param start_time: 任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type start_time: str
        :param stop_time: 任务结束时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type stop_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateMixJobResponse, self).__init__()

        self._job_id = None
        self._stream_name = None
        self._app_id = None
        self._room_id = None
        self._mix_param = None
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
        if mix_param is not None:
            self.mix_param = mix_param
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
        """Gets the job_id of this CreateMixJobResponse.

        任务编号，可以用于修改、查看和停止合流任务

        :return: The job_id of this CreateMixJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateMixJobResponse.

        任务编号，可以用于修改、查看和停止合流任务

        :param job_id: The job_id of this CreateMixJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def stream_name(self):
        """Gets the stream_name of this CreateMixJobResponse.

        流名

        :return: The stream_name of this CreateMixJobResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this CreateMixJobResponse.

        流名

        :param stream_name: The stream_name of this CreateMixJobResponse.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def app_id(self):
        """Gets the app_id of this CreateMixJobResponse.

        应用id

        :return: The app_id of this CreateMixJobResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateMixJobResponse.

        应用id

        :param app_id: The app_id of this CreateMixJobResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def room_id(self):
        """Gets the room_id of this CreateMixJobResponse.

        房间id

        :return: The room_id of this CreateMixJobResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this CreateMixJobResponse.

        房间id

        :param room_id: The room_id of this CreateMixJobResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def mix_param(self):
        """Gets the mix_param of this CreateMixJobResponse.

        :return: The mix_param of this CreateMixJobResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.MixParam`
        """
        return self._mix_param

    @mix_param.setter
    def mix_param(self, mix_param):
        """Sets the mix_param of this CreateMixJobResponse.

        :param mix_param: The mix_param of this CreateMixJobResponse.
        :type mix_param: :class:`huaweicloudsdkcloudrtc.v2.MixParam`
        """
        self._mix_param = mix_param

    @property
    def record_param(self):
        """Gets the record_param of this CreateMixJobResponse.

        :return: The record_param of this CreateMixJobResponse.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        return self._record_param

    @record_param.setter
    def record_param(self, record_param):
        """Sets the record_param of this CreateMixJobResponse.

        :param record_param: The record_param of this CreateMixJobResponse.
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        self._record_param = record_param

    @property
    def create_time(self):
        """Gets the create_time of this CreateMixJobResponse.

        任务创建的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The create_time of this CreateMixJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateMixJobResponse.

        任务创建的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param create_time: The create_time of this CreateMixJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateMixJobResponse.

        任务中的布局更新的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this CreateMixJobResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateMixJobResponse.

        任务中的布局更新的时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this CreateMixJobResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this CreateMixJobResponse.

        任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 

        :return: The state of this CreateMixJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateMixJobResponse.

        任务状态。  - INIT：任务正在初始化 - RUNNING：任务正在运行 - STOPPED：任务已停止 

        :param state: The state of this CreateMixJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def stop_reason(self):
        """Gets the stop_reason of this CreateMixJobResponse.

        任务结束原因

        :return: The stop_reason of this CreateMixJobResponse.
        :rtype: str
        """
        return self._stop_reason

    @stop_reason.setter
    def stop_reason(self, stop_reason):
        """Sets the stop_reason of this CreateMixJobResponse.

        任务结束原因

        :param stop_reason: The stop_reason of this CreateMixJobResponse.
        :type stop_reason: str
        """
        self._stop_reason = stop_reason

    @property
    def description(self):
        """Gets the description of this CreateMixJobResponse.

        状态描述，对state字段的一些补充说明，可用于人工查阅。

        :return: The description of this CreateMixJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateMixJobResponse.

        状态描述，对state字段的一些补充说明，可用于人工查阅。

        :param description: The description of this CreateMixJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this CreateMixJobResponse.

        任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The start_time of this CreateMixJobResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateMixJobResponse.

        任务开始时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param start_time: The start_time of this CreateMixJobResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this CreateMixJobResponse.

        任务结束时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The stop_time of this CreateMixJobResponse.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this CreateMixJobResponse.

        任务结束时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param stop_time: The stop_time of this CreateMixJobResponse.
        :type stop_time: str
        """
        self._stop_time = stop_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateMixJobResponse.

        :return: The x_request_id of this CreateMixJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateMixJobResponse.

        :param x_request_id: The x_request_id of this CreateMixJobResponse.
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
        if not isinstance(other, CreateMixJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
