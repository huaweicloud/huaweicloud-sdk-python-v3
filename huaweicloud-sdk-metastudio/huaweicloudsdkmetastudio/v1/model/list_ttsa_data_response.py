# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTtsaDataResponse(SdkResponse):

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
        'start_time': 'str',
        'end_time': 'str',
        'is_tail': 'bool',
        'audio': 'str',
        'blendshapes': 'list[str]',
        'animations': 'list[AnimationItem]',
        'motions': 'list[MotionItem]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'is_tail': 'is_tail',
        'audio': 'audio',
        'blendshapes': 'blendshapes',
        'animations': 'animations',
        'motions': 'motions',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, start_time=None, end_time=None, is_tail=None, audio=None, blendshapes=None, animations=None, motions=None, x_request_id=None):
        r"""ListTtsaDataResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param start_time: 驱动任务开始时间，格式遵循：RFC 3339， 例 “2020-07-30T10:43:17Z”
        :type start_time: str
        :param end_time: 驱动任务结束时间，格式遵循：RFC 3339， 例 “2020-07-30T10:45:17Z”
        :type end_time: str
        :param is_tail: 是否为尾部(任务数据已全部生成，后续没有新的数据)
        :type is_tail: bool
        :param audio: 音频数据，Base64编码，1秒内的数据。
        :type audio: str
        :param blendshapes: 语音驱动的表情基数据。
        :type blendshapes: list[str]
        :param animations: 手工指定的动作库动作数据。
        :type animations: list[:class:`huaweicloudsdkmetastudio.v1.AnimationItem`]
        :param motions: 语义驱动的智能动作数据。
        :type motions: list[:class:`huaweicloudsdkmetastudio.v1.MotionItem`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListTtsaDataResponse, self).__init__()

        self._job_id = None
        self._start_time = None
        self._end_time = None
        self._is_tail = None
        self._audio = None
        self._blendshapes = None
        self._animations = None
        self._motions = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if is_tail is not None:
            self.is_tail = is_tail
        if audio is not None:
            self.audio = audio
        if blendshapes is not None:
            self.blendshapes = blendshapes
        if animations is not None:
            self.animations = animations
        if motions is not None:
            self.motions = motions
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ListTtsaDataResponse.

        任务ID。

        :return: The job_id of this ListTtsaDataResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListTtsaDataResponse.

        任务ID。

        :param job_id: The job_id of this ListTtsaDataResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTtsaDataResponse.

        驱动任务开始时间，格式遵循：RFC 3339， 例 “2020-07-30T10:43:17Z”

        :return: The start_time of this ListTtsaDataResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTtsaDataResponse.

        驱动任务开始时间，格式遵循：RFC 3339， 例 “2020-07-30T10:43:17Z”

        :param start_time: The start_time of this ListTtsaDataResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTtsaDataResponse.

        驱动任务结束时间，格式遵循：RFC 3339， 例 “2020-07-30T10:45:17Z”

        :return: The end_time of this ListTtsaDataResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTtsaDataResponse.

        驱动任务结束时间，格式遵循：RFC 3339， 例 “2020-07-30T10:45:17Z”

        :param end_time: The end_time of this ListTtsaDataResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_tail(self):
        r"""Gets the is_tail of this ListTtsaDataResponse.

        是否为尾部(任务数据已全部生成，后续没有新的数据)

        :return: The is_tail of this ListTtsaDataResponse.
        :rtype: bool
        """
        return self._is_tail

    @is_tail.setter
    def is_tail(self, is_tail):
        r"""Sets the is_tail of this ListTtsaDataResponse.

        是否为尾部(任务数据已全部生成，后续没有新的数据)

        :param is_tail: The is_tail of this ListTtsaDataResponse.
        :type is_tail: bool
        """
        self._is_tail = is_tail

    @property
    def audio(self):
        r"""Gets the audio of this ListTtsaDataResponse.

        音频数据，Base64编码，1秒内的数据。

        :return: The audio of this ListTtsaDataResponse.
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this ListTtsaDataResponse.

        音频数据，Base64编码，1秒内的数据。

        :param audio: The audio of this ListTtsaDataResponse.
        :type audio: str
        """
        self._audio = audio

    @property
    def blendshapes(self):
        r"""Gets the blendshapes of this ListTtsaDataResponse.

        语音驱动的表情基数据。

        :return: The blendshapes of this ListTtsaDataResponse.
        :rtype: list[str]
        """
        return self._blendshapes

    @blendshapes.setter
    def blendshapes(self, blendshapes):
        r"""Sets the blendshapes of this ListTtsaDataResponse.

        语音驱动的表情基数据。

        :param blendshapes: The blendshapes of this ListTtsaDataResponse.
        :type blendshapes: list[str]
        """
        self._blendshapes = blendshapes

    @property
    def animations(self):
        r"""Gets the animations of this ListTtsaDataResponse.

        手工指定的动作库动作数据。

        :return: The animations of this ListTtsaDataResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AnimationItem`]
        """
        return self._animations

    @animations.setter
    def animations(self, animations):
        r"""Sets the animations of this ListTtsaDataResponse.

        手工指定的动作库动作数据。

        :param animations: The animations of this ListTtsaDataResponse.
        :type animations: list[:class:`huaweicloudsdkmetastudio.v1.AnimationItem`]
        """
        self._animations = animations

    @property
    def motions(self):
        r"""Gets the motions of this ListTtsaDataResponse.

        语义驱动的智能动作数据。

        :return: The motions of this ListTtsaDataResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.MotionItem`]
        """
        return self._motions

    @motions.setter
    def motions(self, motions):
        r"""Sets the motions of this ListTtsaDataResponse.

        语义驱动的智能动作数据。

        :param motions: The motions of this ListTtsaDataResponse.
        :type motions: list[:class:`huaweicloudsdkmetastudio.v1.MotionItem`]
        """
        self._motions = motions

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTtsaDataResponse.

        :return: The x_request_id of this ListTtsaDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTtsaDataResponse.

        :param x_request_id: The x_request_id of this ListTtsaDataResponse.
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
        if not isinstance(other, ListTtsaDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
