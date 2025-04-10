# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndividualStreamJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'user_id': 'str',
        'is_record_audio': 'bool',
        'video_type': 'str',
        'select_stream_type': 'str',
        'max_idle_time': 'int',
        'record_param': 'RecordParam'
    }

    attribute_map = {
        'room_id': 'room_id',
        'user_id': 'user_id',
        'is_record_audio': 'is_record_audio',
        'video_type': 'video_type',
        'select_stream_type': 'select_stream_type',
        'max_idle_time': 'max_idle_time',
        'record_param': 'record_param'
    }

    def __init__(self, room_id=None, user_id=None, is_record_audio=None, video_type=None, select_stream_type=None, max_idle_time=None, record_param=None):
        r"""IndividualStreamJobReq

        The model defined in huaweicloud sdk

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
        """
        
        

        self._room_id = None
        self._user_id = None
        self._is_record_audio = None
        self._video_type = None
        self._select_stream_type = None
        self._max_idle_time = None
        self._record_param = None
        self.discriminator = None

        self.room_id = room_id
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

    @property
    def room_id(self):
        r"""Gets the room_id of this IndividualStreamJobReq.

        房间id

        :return: The room_id of this IndividualStreamJobReq.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this IndividualStreamJobReq.

        房间id

        :param room_id: The room_id of this IndividualStreamJobReq.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def user_id(self):
        r"""Gets the user_id of this IndividualStreamJobReq.

        选看的用户id，单个录制任务内保证唯一

        :return: The user_id of this IndividualStreamJobReq.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this IndividualStreamJobReq.

        选看的用户id，单个录制任务内保证唯一

        :param user_id: The user_id of this IndividualStreamJobReq.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def is_record_audio(self):
        r"""Gets the is_record_audio of this IndividualStreamJobReq.

         是否录制音频。  - true：录制音频 - false：不录制音频  缺省为true。 

        :return: The is_record_audio of this IndividualStreamJobReq.
        :rtype: bool
        """
        return self._is_record_audio

    @is_record_audio.setter
    def is_record_audio(self, is_record_audio):
        r"""Sets the is_record_audio of this IndividualStreamJobReq.

         是否录制音频。  - true：录制音频 - false：不录制音频  缺省为true。 

        :param is_record_audio: The is_record_audio of this IndividualStreamJobReq.
        :type is_record_audio: bool
        """
        self._is_record_audio = is_record_audio

    @property
    def video_type(self):
        r"""Gets the video_type of this IndividualStreamJobReq.

        标识视频流的类型，可选摄像头流或者屏幕分享流，未填写表示不录制视频。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :return: The video_type of this IndividualStreamJobReq.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        r"""Sets the video_type of this IndividualStreamJobReq.

        标识视频流的类型，可选摄像头流或者屏幕分享流，未填写表示不录制视频。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :param video_type: The video_type of this IndividualStreamJobReq.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def select_stream_type(self):
        r"""Gets the select_stream_type of this IndividualStreamJobReq.

        指定窗口拉取的分辨率档位。  - LD - SD - HD - FHD  缺省为FHD。 

        :return: The select_stream_type of this IndividualStreamJobReq.
        :rtype: str
        """
        return self._select_stream_type

    @select_stream_type.setter
    def select_stream_type(self, select_stream_type):
        r"""Sets the select_stream_type of this IndividualStreamJobReq.

        指定窗口拉取的分辨率档位。  - LD - SD - HD - FHD  缺省为FHD。 

        :param select_stream_type: The select_stream_type of this IndividualStreamJobReq.
        :type select_stream_type: str
        """
        self._select_stream_type = select_stream_type

    @property
    def max_idle_time(self):
        r"""Gets the max_idle_time of this IndividualStreamJobReq.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :return: The max_idle_time of this IndividualStreamJobReq.
        :rtype: int
        """
        return self._max_idle_time

    @max_idle_time.setter
    def max_idle_time(self, max_idle_time):
        r"""Sets the max_idle_time of this IndividualStreamJobReq.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :param max_idle_time: The max_idle_time of this IndividualStreamJobReq.
        :type max_idle_time: int
        """
        self._max_idle_time = max_idle_time

    @property
    def record_param(self):
        r"""Gets the record_param of this IndividualStreamJobReq.

        :return: The record_param of this IndividualStreamJobReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        return self._record_param

    @record_param.setter
    def record_param(self, record_param):
        r"""Sets the record_param of this IndividualStreamJobReq.

        :param record_param: The record_param of this IndividualStreamJobReq.
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        self._record_param = record_param

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
        if not isinstance(other, IndividualStreamJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
