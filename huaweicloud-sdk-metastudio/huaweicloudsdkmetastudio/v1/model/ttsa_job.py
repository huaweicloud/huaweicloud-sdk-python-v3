# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TTSAJob:

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
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'content_duration': 'float',
        'job_type': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'content_duration': 'content_duration',
        'job_type': 'job_type'
    }

    def __init__(self, job_id=None, state=None, start_time=None, end_time=None, content_duration=None, job_type=None):
        r"""TTSAJob

        The model defined in huaweicloud sdk

        :param job_id: 语音驱动任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败
        :type state: str
        :param start_time: 任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type start_time: str
        :param end_time: 任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type end_time: str
        :param content_duration: 语音驱动内容时长。  单位:秒。
        :type content_duration: float
        :param job_type: 任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作
        :type job_type: str
        """
        
        

        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._content_duration = None
        self._job_type = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if content_duration is not None:
            self.content_duration = content_duration
        if job_type is not None:
            self.job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this TTSAJob.

        语音驱动任务ID。

        :return: The job_id of this TTSAJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TTSAJob.

        语音驱动任务ID。

        :param job_id: The job_id of this TTSAJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this TTSAJob.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :return: The state of this TTSAJob.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TTSAJob.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :param state: The state of this TTSAJob.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        r"""Gets the start_time of this TTSAJob.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The start_time of this TTSAJob.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TTSAJob.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param start_time: The start_time of this TTSAJob.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TTSAJob.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The end_time of this TTSAJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TTSAJob.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param end_time: The end_time of this TTSAJob.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def content_duration(self):
        r"""Gets the content_duration of this TTSAJob.

        语音驱动内容时长。  单位:秒。

        :return: The content_duration of this TTSAJob.
        :rtype: float
        """
        return self._content_duration

    @content_duration.setter
    def content_duration(self, content_duration):
        r"""Sets the content_duration of this TTSAJob.

        语音驱动内容时长。  单位:秒。

        :param content_duration: The content_duration of this TTSAJob.
        :type content_duration: float
        """
        self._content_duration = content_duration

    @property
    def job_type(self):
        r"""Gets the job_type of this TTSAJob.

        任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作

        :return: The job_type of this TTSAJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this TTSAJob.

        任务类型。 * REAL_JOB：实时任务。如数字人交互。 * UNREAL_JOB：非实时任务。如数字人视频制作

        :param job_type: The job_type of this TTSAJob.
        :type job_type: str
        """
        self._job_type = job_type

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
        if not isinstance(other, TTSAJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
