# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScreenRecordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'desktop_pool_id': 'str',
        'username': 'str',
        'size': 'int',
        'type': 'str',
        'status': 'str',
        'video_filename': 'str',
        'event_filename': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'update_time': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'id': 'id',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'desktop_pool_id': 'desktop_pool_id',
        'username': 'username',
        'size': 'size',
        'type': 'type',
        'status': 'status',
        'video_filename': 'video_filename',
        'event_filename': 'event_filename',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'update_time': 'update_time',
        'duration': 'duration'
    }

    def __init__(self, id=None, desktop_id=None, desktop_name=None, desktop_pool_id=None, username=None, size=None, type=None, status=None, video_filename=None, event_filename=None, start_time=None, end_time=None, update_time=None, duration=None):
        """ShowScreenRecordResponse

        The model defined in huaweicloud sdk

        :param id: 主键UUID。
        :type id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param desktop_pool_id: 桌面池ID。
        :type desktop_pool_id: str
        :param username: 用户名称。
        :type username: str
        :param size: 文件大小（Byte）。
        :type size: int
        :param type: 录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - USER_OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。
        :type type: str
        :param status: 录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - REC_FAILED：录制失败。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。 - UPLOAD_FAILED：上传失败。
        :type status: str
        :param video_filename: 录屏文件名称。
        :type video_filename: str
        :param event_filename: 事件文件名称。
        :type event_filename: str
        :param start_time: 开始时间（2024-10-15T10:04:41.263Z）。
        :type start_time: str
        :param end_time: 结束时间（2024-10-15T11:04:41.263Z）。
        :type end_time: str
        :param update_time: 更新时间（2024-10-15T11:04:41.263Z）。
        :type update_time: str
        :param duration: 视频时长（秒）。
        :type duration: int
        """
        
        super(ShowScreenRecordResponse, self).__init__()

        self._id = None
        self._desktop_id = None
        self._desktop_name = None
        self._desktop_pool_id = None
        self._username = None
        self._size = None
        self._type = None
        self._status = None
        self._video_filename = None
        self._event_filename = None
        self._start_time = None
        self._end_time = None
        self._update_time = None
        self._duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if username is not None:
            self.username = username
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if video_filename is not None:
            self.video_filename = video_filename
        if event_filename is not None:
            self.event_filename = event_filename
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if update_time is not None:
            self.update_time = update_time
        if duration is not None:
            self.duration = duration

    @property
    def id(self):
        """Gets the id of this ShowScreenRecordResponse.

        主键UUID。

        :return: The id of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowScreenRecordResponse.

        主键UUID。

        :param id: The id of this ShowScreenRecordResponse.
        :type id: str
        """
        self._id = id

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ShowScreenRecordResponse.

        桌面ID。

        :return: The desktop_id of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ShowScreenRecordResponse.

        桌面ID。

        :param desktop_id: The desktop_id of this ShowScreenRecordResponse.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this ShowScreenRecordResponse.

        桌面名称。

        :return: The desktop_name of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this ShowScreenRecordResponse.

        桌面名称。

        :param desktop_name: The desktop_name of this ShowScreenRecordResponse.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_pool_id(self):
        """Gets the desktop_pool_id of this ShowScreenRecordResponse.

        桌面池ID。

        :return: The desktop_pool_id of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        """Sets the desktop_pool_id of this ShowScreenRecordResponse.

        桌面池ID。

        :param desktop_pool_id: The desktop_pool_id of this ShowScreenRecordResponse.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def username(self):
        """Gets the username of this ShowScreenRecordResponse.

        用户名称。

        :return: The username of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ShowScreenRecordResponse.

        用户名称。

        :param username: The username of this ShowScreenRecordResponse.
        :type username: str
        """
        self._username = username

    @property
    def size(self):
        """Gets the size of this ShowScreenRecordResponse.

        文件大小（Byte）。

        :return: The size of this ShowScreenRecordResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowScreenRecordResponse.

        文件大小（Byte）。

        :param size: The size of this ShowScreenRecordResponse.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this ShowScreenRecordResponse.

        录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - USER_OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。

        :return: The type of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowScreenRecordResponse.

        录屏类型。 - FULL：全程录屏。 - INTERVAL：间隔录屏。 - USER_OPERATION：用户操作录屏。 - SESSION：监听会话生命周期录屏。

        :param type: The type of this ShowScreenRecordResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ShowScreenRecordResponse.

        录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - REC_FAILED：录制失败。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。 - UPLOAD_FAILED：上传失败。

        :return: The status of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowScreenRecordResponse.

        录屏状态。 - RECORDING：录制中。 - REC_COMPLETED：录制完成。 - REC_FAILED：录制失败。 - UPLOADING：上传中。 - UPLOAD_COMPLETED：上传完成。 - UPLOAD_FAILED：上传失败。

        :param status: The status of this ShowScreenRecordResponse.
        :type status: str
        """
        self._status = status

    @property
    def video_filename(self):
        """Gets the video_filename of this ShowScreenRecordResponse.

        录屏文件名称。

        :return: The video_filename of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._video_filename

    @video_filename.setter
    def video_filename(self, video_filename):
        """Sets the video_filename of this ShowScreenRecordResponse.

        录屏文件名称。

        :param video_filename: The video_filename of this ShowScreenRecordResponse.
        :type video_filename: str
        """
        self._video_filename = video_filename

    @property
    def event_filename(self):
        """Gets the event_filename of this ShowScreenRecordResponse.

        事件文件名称。

        :return: The event_filename of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._event_filename

    @event_filename.setter
    def event_filename(self, event_filename):
        """Sets the event_filename of this ShowScreenRecordResponse.

        事件文件名称。

        :param event_filename: The event_filename of this ShowScreenRecordResponse.
        :type event_filename: str
        """
        self._event_filename = event_filename

    @property
    def start_time(self):
        """Gets the start_time of this ShowScreenRecordResponse.

        开始时间（2024-10-15T10:04:41.263Z）。

        :return: The start_time of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowScreenRecordResponse.

        开始时间（2024-10-15T10:04:41.263Z）。

        :param start_time: The start_time of this ShowScreenRecordResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowScreenRecordResponse.

        结束时间（2024-10-15T11:04:41.263Z）。

        :return: The end_time of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowScreenRecordResponse.

        结束时间（2024-10-15T11:04:41.263Z）。

        :param end_time: The end_time of this ShowScreenRecordResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowScreenRecordResponse.

        更新时间（2024-10-15T11:04:41.263Z）。

        :return: The update_time of this ShowScreenRecordResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowScreenRecordResponse.

        更新时间（2024-10-15T11:04:41.263Z）。

        :param update_time: The update_time of this ShowScreenRecordResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def duration(self):
        """Gets the duration of this ShowScreenRecordResponse.

        视频时长（秒）。

        :return: The duration of this ShowScreenRecordResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ShowScreenRecordResponse.

        视频时长（秒）。

        :param duration: The duration of this ShowScreenRecordResponse.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, ShowScreenRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
