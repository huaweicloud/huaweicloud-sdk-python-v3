# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectTranscriberJobResponse(SdkResponse):

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
        'status': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'segments': 'list[Segment]',
        'audio_duration': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'segments': 'segments',
        'audio_duration': 'audio_duration'
    }

    def __init__(self, job_id=None, status=None, create_time=None, start_time=None, finish_time=None, segments=None, audio_duration=None):
        r"""CollectTranscriberJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 录音文件识别任务标识符。  使用“callback_url”回调url时，该字段会随结果发送至用户服务器。 使用get接口查询，不会出现该字段
        :type job_id: str
        :param status: 当前识别状态。具体状态如下所示：  WAITING 等待识别。 FINISHED 识别已经完成。 ERROR 识别过程中发生错误。
        :type status: str
        :param create_time: 任务创建时间, 遵循 RFC 3339格式。 格式示例：2018-12-04T13:10:29.310Z。
        :type create_time: str
        :param start_time: 开始识别时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。
        :type start_time: str
        :param finish_time: 识别完成时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。 
        :type finish_time: str
        :param segments: 转写结果, 多句结果的数组。 
        :type segments: list[:class:`huaweicloudsdksis.v1.Segment`]
        :param audio_duration: 音频时长，单位ms
        :type audio_duration: int
        """
        
        super(CollectTranscriberJobResponse, self).__init__()

        self._job_id = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._finish_time = None
        self._segments = None
        self._audio_duration = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if segments is not None:
            self.segments = segments
        if audio_duration is not None:
            self.audio_duration = audio_duration

    @property
    def job_id(self):
        r"""Gets the job_id of this CollectTranscriberJobResponse.

        录音文件识别任务标识符。  使用“callback_url”回调url时，该字段会随结果发送至用户服务器。 使用get接口查询，不会出现该字段

        :return: The job_id of this CollectTranscriberJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CollectTranscriberJobResponse.

        录音文件识别任务标识符。  使用“callback_url”回调url时，该字段会随结果发送至用户服务器。 使用get接口查询，不会出现该字段

        :param job_id: The job_id of this CollectTranscriberJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this CollectTranscriberJobResponse.

        当前识别状态。具体状态如下所示：  WAITING 等待识别。 FINISHED 识别已经完成。 ERROR 识别过程中发生错误。

        :return: The status of this CollectTranscriberJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CollectTranscriberJobResponse.

        当前识别状态。具体状态如下所示：  WAITING 等待识别。 FINISHED 识别已经完成。 ERROR 识别过程中发生错误。

        :param status: The status of this CollectTranscriberJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this CollectTranscriberJobResponse.

        任务创建时间, 遵循 RFC 3339格式。 格式示例：2018-12-04T13:10:29.310Z。

        :return: The create_time of this CollectTranscriberJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CollectTranscriberJobResponse.

        任务创建时间, 遵循 RFC 3339格式。 格式示例：2018-12-04T13:10:29.310Z。

        :param create_time: The create_time of this CollectTranscriberJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this CollectTranscriberJobResponse.

        开始识别时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。

        :return: The start_time of this CollectTranscriberJobResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CollectTranscriberJobResponse.

        开始识别时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。

        :param start_time: The start_time of this CollectTranscriberJobResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this CollectTranscriberJobResponse.

        识别完成时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。 

        :return: The finish_time of this CollectTranscriberJobResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this CollectTranscriberJobResponse.

        识别完成时间, 遵循 RFC 3339格式。 当status为FINISHED或ERROR时存在。 格式示例：2018-12-04T13:10:29.310Z。 

        :param finish_time: The finish_time of this CollectTranscriberJobResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def segments(self):
        r"""Gets the segments of this CollectTranscriberJobResponse.

        转写结果, 多句结果的数组。 

        :return: The segments of this CollectTranscriberJobResponse.
        :rtype: list[:class:`huaweicloudsdksis.v1.Segment`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        r"""Sets the segments of this CollectTranscriberJobResponse.

        转写结果, 多句结果的数组。 

        :param segments: The segments of this CollectTranscriberJobResponse.
        :type segments: list[:class:`huaweicloudsdksis.v1.Segment`]
        """
        self._segments = segments

    @property
    def audio_duration(self):
        r"""Gets the audio_duration of this CollectTranscriberJobResponse.

        音频时长，单位ms

        :return: The audio_duration of this CollectTranscriberJobResponse.
        :rtype: int
        """
        return self._audio_duration

    @audio_duration.setter
    def audio_duration(self, audio_duration):
        r"""Sets the audio_duration of this CollectTranscriberJobResponse.

        音频时长，单位ms

        :param audio_duration: The audio_duration of this CollectTranscriberJobResponse.
        :type audio_duration: int
        """
        self._audio_duration = audio_duration

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
        if not isinstance(other, CollectTranscriberJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
