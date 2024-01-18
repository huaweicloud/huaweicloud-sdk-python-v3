# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSmartChatJobResponse(SdkResponse):

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
        'rtc_room_info': 'RTCRoomInfoList',
        'chat_subtitle_config': 'ChatSubtitleConfig',
        'video_config': 'ChatVideoConfigRsp',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'rtc_room_info': 'rtc_room_info',
        'chat_subtitle_config': 'chat_subtitle_config',
        'video_config': 'video_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, rtc_room_info=None, chat_subtitle_config=None, video_config=None, x_request_id=None):
        """StartSmartChatJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 智能交互对话任务ID。
        :type job_id: str
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param chat_subtitle_config: 
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.ChatVideoConfigRsp`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(StartSmartChatJobResponse, self).__init__()

        self._job_id = None
        self._rtc_room_info = None
        self._chat_subtitle_config = None
        self._video_config = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if chat_subtitle_config is not None:
            self.chat_subtitle_config = chat_subtitle_config
        if video_config is not None:
            self.video_config = video_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this StartSmartChatJobResponse.

        智能交互对话任务ID。

        :return: The job_id of this StartSmartChatJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartSmartChatJobResponse.

        智能交互对话任务ID。

        :param job_id: The job_id of this StartSmartChatJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def rtc_room_info(self):
        """Gets the rtc_room_info of this StartSmartChatJobResponse.

        :return: The rtc_room_info of this StartSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        """Sets the rtc_room_info of this StartSmartChatJobResponse.

        :param rtc_room_info: The rtc_room_info of this StartSmartChatJobResponse.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

    @property
    def chat_subtitle_config(self):
        """Gets the chat_subtitle_config of this StartSmartChatJobResponse.

        :return: The chat_subtitle_config of this StartSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        """Sets the chat_subtitle_config of this StartSmartChatJobResponse.

        :param chat_subtitle_config: The chat_subtitle_config of this StartSmartChatJobResponse.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def video_config(self):
        """Gets the video_config of this StartSmartChatJobResponse.

        :return: The video_config of this StartSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChatVideoConfigRsp`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this StartSmartChatJobResponse.

        :param video_config: The video_config of this StartSmartChatJobResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.ChatVideoConfigRsp`
        """
        self._video_config = video_config

    @property
    def x_request_id(self):
        """Gets the x_request_id of this StartSmartChatJobResponse.

        :return: The x_request_id of this StartSmartChatJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this StartSmartChatJobResponse.

        :param x_request_id: The x_request_id of this StartSmartChatJobResponse.
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
        if not isinstance(other, StartSmartChatJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
