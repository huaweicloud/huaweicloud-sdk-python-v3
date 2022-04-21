# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeFlashAsrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'audio_duration': 'int',
        'flash_result': 'list[FlashResult]'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'audio_duration': 'audio_duration',
        'flash_result': 'flash_result'
    }

    def __init__(self, trace_id=None, audio_duration=None, flash_result=None):
        """RecognizeFlashAsrResponse

        The model defined in huaweicloud sdk

        :param trace_id: 服务内部的令牌，可用于在日志中追溯具体调用流程
        :type trace_id: str
        :param audio_duration: 音频时长
        :type audio_duration: int
        :param flash_result: 识别结果
        :type flash_result: list[:class:`huaweicloudsdksis.v1.FlashResult`]
        """
        
        super(RecognizeFlashAsrResponse, self).__init__()

        self._trace_id = None
        self._audio_duration = None
        self._flash_result = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if audio_duration is not None:
            self.audio_duration = audio_duration
        if flash_result is not None:
            self.flash_result = flash_result

    @property
    def trace_id(self):
        """Gets the trace_id of this RecognizeFlashAsrResponse.

        服务内部的令牌，可用于在日志中追溯具体调用流程

        :return: The trace_id of this RecognizeFlashAsrResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this RecognizeFlashAsrResponse.

        服务内部的令牌，可用于在日志中追溯具体调用流程

        :param trace_id: The trace_id of this RecognizeFlashAsrResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def audio_duration(self):
        """Gets the audio_duration of this RecognizeFlashAsrResponse.

        音频时长

        :return: The audio_duration of this RecognizeFlashAsrResponse.
        :rtype: int
        """
        return self._audio_duration

    @audio_duration.setter
    def audio_duration(self, audio_duration):
        """Sets the audio_duration of this RecognizeFlashAsrResponse.

        音频时长

        :param audio_duration: The audio_duration of this RecognizeFlashAsrResponse.
        :type audio_duration: int
        """
        self._audio_duration = audio_duration

    @property
    def flash_result(self):
        """Gets the flash_result of this RecognizeFlashAsrResponse.

        识别结果

        :return: The flash_result of this RecognizeFlashAsrResponse.
        :rtype: list[:class:`huaweicloudsdksis.v1.FlashResult`]
        """
        return self._flash_result

    @flash_result.setter
    def flash_result(self, flash_result):
        """Sets the flash_result of this RecognizeFlashAsrResponse.

        识别结果

        :param flash_result: The flash_result of this RecognizeFlashAsrResponse.
        :type flash_result: list[:class:`huaweicloudsdksis.v1.FlashResult`]
        """
        self._flash_result = flash_result

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
        if not isinstance(other, RecognizeFlashAsrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
