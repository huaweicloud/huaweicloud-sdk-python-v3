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
        'language': 'LanguageEnum',
        'rtc_room_info': 'RTCRoomInfoList',
        'chat_subtitle_config': 'SmartChatSubtitleConfig',
        'video_config': 'SmartChatVideoConfig',
        'chat_video_type': 'str',
        'region': 'str',
        'chat_access_address': 'str',
        'is_transparent': 'bool',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'language': 'language',
        'rtc_room_info': 'rtc_room_info',
        'chat_subtitle_config': 'chat_subtitle_config',
        'video_config': 'video_config',
        'chat_video_type': 'chat_video_type',
        'region': 'region',
        'chat_access_address': 'chat_access_address',
        'is_transparent': 'is_transparent',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, language=None, rtc_room_info=None, chat_subtitle_config=None, video_config=None, chat_video_type=None, region=None, chat_access_address=None, is_transparent=None, x_request_id=None):
        """StartSmartChatJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 智能交互对话任务ID。
        :type job_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param chat_subtitle_config: 
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        :param chat_video_type: 智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏
        :type chat_video_type: str
        :param region: 算力所在region。 * cn-north-4: 北京4 * cn-southwest-2: 贵阳1
        :type region: str
        :param chat_access_address: 智能交互接入地址。
        :type chat_access_address: str
        :param is_transparent: 是否透明背景
        :type is_transparent: bool
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(StartSmartChatJobResponse, self).__init__()

        self._job_id = None
        self._language = None
        self._rtc_room_info = None
        self._chat_subtitle_config = None
        self._video_config = None
        self._chat_video_type = None
        self._region = None
        self._chat_access_address = None
        self._is_transparent = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if language is not None:
            self.language = language
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if chat_subtitle_config is not None:
            self.chat_subtitle_config = chat_subtitle_config
        if video_config is not None:
            self.video_config = video_config
        if chat_video_type is not None:
            self.chat_video_type = chat_video_type
        if region is not None:
            self.region = region
        if chat_access_address is not None:
            self.chat_access_address = chat_access_address
        if is_transparent is not None:
            self.is_transparent = is_transparent
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
    def language(self):
        """Gets the language of this StartSmartChatJobResponse.

        :return: The language of this StartSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this StartSmartChatJobResponse.

        :param language: The language of this StartSmartChatJobResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

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
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        """Sets the chat_subtitle_config of this StartSmartChatJobResponse.

        :param chat_subtitle_config: The chat_subtitle_config of this StartSmartChatJobResponse.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def video_config(self):
        """Gets the video_config of this StartSmartChatJobResponse.

        :return: The video_config of this StartSmartChatJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this StartSmartChatJobResponse.

        :param video_config: The video_config of this StartSmartChatJobResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.SmartChatVideoConfig`
        """
        self._video_config = video_config

    @property
    def chat_video_type(self):
        """Gets the chat_video_type of this StartSmartChatJobResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :return: The chat_video_type of this StartSmartChatJobResponse.
        :rtype: str
        """
        return self._chat_video_type

    @chat_video_type.setter
    def chat_video_type(self, chat_video_type):
        """Sets the chat_video_type of this StartSmartChatJobResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :param chat_video_type: The chat_video_type of this StartSmartChatJobResponse.
        :type chat_video_type: str
        """
        self._chat_video_type = chat_video_type

    @property
    def region(self):
        """Gets the region of this StartSmartChatJobResponse.

        算力所在region。 * cn-north-4: 北京4 * cn-southwest-2: 贵阳1

        :return: The region of this StartSmartChatJobResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this StartSmartChatJobResponse.

        算力所在region。 * cn-north-4: 北京4 * cn-southwest-2: 贵阳1

        :param region: The region of this StartSmartChatJobResponse.
        :type region: str
        """
        self._region = region

    @property
    def chat_access_address(self):
        """Gets the chat_access_address of this StartSmartChatJobResponse.

        智能交互接入地址。

        :return: The chat_access_address of this StartSmartChatJobResponse.
        :rtype: str
        """
        return self._chat_access_address

    @chat_access_address.setter
    def chat_access_address(self, chat_access_address):
        """Sets the chat_access_address of this StartSmartChatJobResponse.

        智能交互接入地址。

        :param chat_access_address: The chat_access_address of this StartSmartChatJobResponse.
        :type chat_access_address: str
        """
        self._chat_access_address = chat_access_address

    @property
    def is_transparent(self):
        """Gets the is_transparent of this StartSmartChatJobResponse.

        是否透明背景

        :return: The is_transparent of this StartSmartChatJobResponse.
        :rtype: bool
        """
        return self._is_transparent

    @is_transparent.setter
    def is_transparent(self, is_transparent):
        """Sets the is_transparent of this StartSmartChatJobResponse.

        是否透明背景

        :param is_transparent: The is_transparent of this StartSmartChatJobResponse.
        :type is_transparent: bool
        """
        self._is_transparent = is_transparent

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
