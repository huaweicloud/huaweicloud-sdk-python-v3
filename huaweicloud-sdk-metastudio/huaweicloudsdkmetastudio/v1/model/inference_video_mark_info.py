# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InferenceVideoMarkInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_start_time': 'str',
        'video_end_time': 'str',
        'chat_video_start_time': 'str',
        'chat_video_end_time': 'str'
    }

    attribute_map = {
        'video_start_time': 'video_start_time',
        'video_end_time': 'video_end_time',
        'chat_video_start_time': 'chat_video_start_time',
        'chat_video_end_time': 'chat_video_end_time'
    }

    def __init__(self, video_start_time=None, video_end_time=None, chat_video_start_time=None, chat_video_end_time=None):
        r"""InferenceVideoMarkInfo

        The model defined in huaweicloud sdk

        :param video_start_time: 选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。
        :type video_start_time: str
        :param video_end_time: 选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。
        :type video_end_time: str
        :param chat_video_start_time: 选取推理数据预处理智能交互视频起始时间。格式：“HH:MM:SS.mmm”。
        :type chat_video_start_time: str
        :param chat_video_end_time: 选取推理数据预处理智能交互视频结束时间。格式：“HH:MM:SS.mmm”。
        :type chat_video_end_time: str
        """
        
        

        self._video_start_time = None
        self._video_end_time = None
        self._chat_video_start_time = None
        self._chat_video_end_time = None
        self.discriminator = None

        if video_start_time is not None:
            self.video_start_time = video_start_time
        if video_end_time is not None:
            self.video_end_time = video_end_time
        if chat_video_start_time is not None:
            self.chat_video_start_time = chat_video_start_time
        if chat_video_end_time is not None:
            self.chat_video_end_time = chat_video_end_time

    @property
    def video_start_time(self):
        r"""Gets the video_start_time of this InferenceVideoMarkInfo.

        选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。

        :return: The video_start_time of this InferenceVideoMarkInfo.
        :rtype: str
        """
        return self._video_start_time

    @video_start_time.setter
    def video_start_time(self, video_start_time):
        r"""Sets the video_start_time of this InferenceVideoMarkInfo.

        选取推理数据预处理视频起始时间。格式：“HH:MM:SS.mmm”。

        :param video_start_time: The video_start_time of this InferenceVideoMarkInfo.
        :type video_start_time: str
        """
        self._video_start_time = video_start_time

    @property
    def video_end_time(self):
        r"""Gets the video_end_time of this InferenceVideoMarkInfo.

        选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。

        :return: The video_end_time of this InferenceVideoMarkInfo.
        :rtype: str
        """
        return self._video_end_time

    @video_end_time.setter
    def video_end_time(self, video_end_time):
        r"""Sets the video_end_time of this InferenceVideoMarkInfo.

        选取推理数据预处理视频结束时间。格式：“HH:MM:SS.mmm”。

        :param video_end_time: The video_end_time of this InferenceVideoMarkInfo.
        :type video_end_time: str
        """
        self._video_end_time = video_end_time

    @property
    def chat_video_start_time(self):
        r"""Gets the chat_video_start_time of this InferenceVideoMarkInfo.

        选取推理数据预处理智能交互视频起始时间。格式：“HH:MM:SS.mmm”。

        :return: The chat_video_start_time of this InferenceVideoMarkInfo.
        :rtype: str
        """
        return self._chat_video_start_time

    @chat_video_start_time.setter
    def chat_video_start_time(self, chat_video_start_time):
        r"""Sets the chat_video_start_time of this InferenceVideoMarkInfo.

        选取推理数据预处理智能交互视频起始时间。格式：“HH:MM:SS.mmm”。

        :param chat_video_start_time: The chat_video_start_time of this InferenceVideoMarkInfo.
        :type chat_video_start_time: str
        """
        self._chat_video_start_time = chat_video_start_time

    @property
    def chat_video_end_time(self):
        r"""Gets the chat_video_end_time of this InferenceVideoMarkInfo.

        选取推理数据预处理智能交互视频结束时间。格式：“HH:MM:SS.mmm”。

        :return: The chat_video_end_time of this InferenceVideoMarkInfo.
        :rtype: str
        """
        return self._chat_video_end_time

    @chat_video_end_time.setter
    def chat_video_end_time(self, chat_video_end_time):
        r"""Sets the chat_video_end_time of this InferenceVideoMarkInfo.

        选取推理数据预处理智能交互视频结束时间。格式：“HH:MM:SS.mmm”。

        :param chat_video_end_time: The chat_video_end_time of this InferenceVideoMarkInfo.
        :type chat_video_end_time: str
        """
        self._chat_video_end_time = chat_video_end_time

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
        if not isinstance(other, InferenceVideoMarkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
