# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAsyncTtsJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'code': 'str',
        'message': 'str',
        'audio_file_url': 'str',
        'audio_info_file_url': 'str',
        'audio_srt_file_url': 'str',
        'audio_action_file_url': 'str'
    }

    attribute_map = {
        'state': 'state',
        'code': 'code',
        'message': 'message',
        'audio_file_url': 'audio_file_url',
        'audio_info_file_url': 'audio_info_file_url',
        'audio_srt_file_url': 'audio_srt_file_url',
        'audio_action_file_url': 'audio_action_file_url'
    }

    def __init__(self, state=None, code=None, message=None, audio_file_url=None, audio_info_file_url=None, audio_srt_file_url=None, audio_action_file_url=None):
        r"""ShowAsyncTtsJobResponse

        The model defined in huaweicloud sdk

        :param state: 音频文件是否已生成完成。该标记为PROCESSING时，应该每隔3秒再次调用本接口获取音频文件(WAITING 等待中,PROCESSING 处理中,SUCCEED 成功,FAILED 失败)。当存在该字段时，会返回以下文件的下载链接。
        :type state: str
        :param code: 返回码。
        :type code: str
        :param message: 异常信息。
        :type message: str
        :param audio_file_url: 音频文件下载链接，有效期为1个小时。
        :type audio_file_url: str
        :param audio_info_file_url: 音频信息文件下载链接，有效期为1个小时。
        :type audio_info_file_url: str
        :param audio_srt_file_url: 字幕文件下载链接，有效期为1个小时。
        :type audio_srt_file_url: str
        :param audio_action_file_url: 动作信息文件下载链接，有效期为1个小时。
        :type audio_action_file_url: str
        """
        
        super().__init__()

        self._state = None
        self._code = None
        self._message = None
        self._audio_file_url = None
        self._audio_info_file_url = None
        self._audio_srt_file_url = None
        self._audio_action_file_url = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if audio_file_url is not None:
            self.audio_file_url = audio_file_url
        if audio_info_file_url is not None:
            self.audio_info_file_url = audio_info_file_url
        if audio_srt_file_url is not None:
            self.audio_srt_file_url = audio_srt_file_url
        if audio_action_file_url is not None:
            self.audio_action_file_url = audio_action_file_url

    @property
    def state(self):
        r"""Gets the state of this ShowAsyncTtsJobResponse.

        音频文件是否已生成完成。该标记为PROCESSING时，应该每隔3秒再次调用本接口获取音频文件(WAITING 等待中,PROCESSING 处理中,SUCCEED 成功,FAILED 失败)。当存在该字段时，会返回以下文件的下载链接。

        :return: The state of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowAsyncTtsJobResponse.

        音频文件是否已生成完成。该标记为PROCESSING时，应该每隔3秒再次调用本接口获取音频文件(WAITING 等待中,PROCESSING 处理中,SUCCEED 成功,FAILED 失败)。当存在该字段时，会返回以下文件的下载链接。

        :param state: The state of this ShowAsyncTtsJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def code(self):
        r"""Gets the code of this ShowAsyncTtsJobResponse.

        返回码。

        :return: The code of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowAsyncTtsJobResponse.

        返回码。

        :param code: The code of this ShowAsyncTtsJobResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ShowAsyncTtsJobResponse.

        异常信息。

        :return: The message of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowAsyncTtsJobResponse.

        异常信息。

        :param message: The message of this ShowAsyncTtsJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def audio_file_url(self):
        r"""Gets the audio_file_url of this ShowAsyncTtsJobResponse.

        音频文件下载链接，有效期为1个小时。

        :return: The audio_file_url of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._audio_file_url

    @audio_file_url.setter
    def audio_file_url(self, audio_file_url):
        r"""Sets the audio_file_url of this ShowAsyncTtsJobResponse.

        音频文件下载链接，有效期为1个小时。

        :param audio_file_url: The audio_file_url of this ShowAsyncTtsJobResponse.
        :type audio_file_url: str
        """
        self._audio_file_url = audio_file_url

    @property
    def audio_info_file_url(self):
        r"""Gets the audio_info_file_url of this ShowAsyncTtsJobResponse.

        音频信息文件下载链接，有效期为1个小时。

        :return: The audio_info_file_url of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._audio_info_file_url

    @audio_info_file_url.setter
    def audio_info_file_url(self, audio_info_file_url):
        r"""Sets the audio_info_file_url of this ShowAsyncTtsJobResponse.

        音频信息文件下载链接，有效期为1个小时。

        :param audio_info_file_url: The audio_info_file_url of this ShowAsyncTtsJobResponse.
        :type audio_info_file_url: str
        """
        self._audio_info_file_url = audio_info_file_url

    @property
    def audio_srt_file_url(self):
        r"""Gets the audio_srt_file_url of this ShowAsyncTtsJobResponse.

        字幕文件下载链接，有效期为1个小时。

        :return: The audio_srt_file_url of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._audio_srt_file_url

    @audio_srt_file_url.setter
    def audio_srt_file_url(self, audio_srt_file_url):
        r"""Sets the audio_srt_file_url of this ShowAsyncTtsJobResponse.

        字幕文件下载链接，有效期为1个小时。

        :param audio_srt_file_url: The audio_srt_file_url of this ShowAsyncTtsJobResponse.
        :type audio_srt_file_url: str
        """
        self._audio_srt_file_url = audio_srt_file_url

    @property
    def audio_action_file_url(self):
        r"""Gets the audio_action_file_url of this ShowAsyncTtsJobResponse.

        动作信息文件下载链接，有效期为1个小时。

        :return: The audio_action_file_url of this ShowAsyncTtsJobResponse.
        :rtype: str
        """
        return self._audio_action_file_url

    @audio_action_file_url.setter
    def audio_action_file_url(self, audio_action_file_url):
        r"""Sets the audio_action_file_url of this ShowAsyncTtsJobResponse.

        动作信息文件下载链接，有效期为1个小时。

        :param audio_action_file_url: The audio_action_file_url of this ShowAsyncTtsJobResponse.
        :type audio_action_file_url: str
        """
        self._audio_action_file_url = audio_action_file_url

    def to_dict(self):
        import warnings
        warnings.warn("ShowAsyncTtsJobResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowAsyncTtsJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
