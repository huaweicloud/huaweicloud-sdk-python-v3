# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DigitalHumanModelingJobInfo:

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
        'error_info': 'ErrorResponse'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_info': 'error_info'
    }

    def __init__(self, job_id=None, state=None, start_time=None, end_time=None, error_info=None):
        r"""DigitalHumanModelingJobInfo

        The model defined in huaweicloud sdk

        :param job_id: 照片建模任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消
        :type state: str
        :param start_time: 任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type start_time: str
        :param end_time: 任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type end_time: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        
        

        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._error_info = None
        self.discriminator = None

        self.job_id = job_id
        self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_info is not None:
            self.error_info = error_info

    @property
    def job_id(self):
        r"""Gets the job_id of this DigitalHumanModelingJobInfo.

        照片建模任务ID。

        :return: The job_id of this DigitalHumanModelingJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DigitalHumanModelingJobInfo.

        照片建模任务ID。

        :param job_id: The job_id of this DigitalHumanModelingJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this DigitalHumanModelingJobInfo.

        任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :return: The state of this DigitalHumanModelingJobInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DigitalHumanModelingJobInfo.

        任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :param state: The state of this DigitalHumanModelingJobInfo.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        r"""Gets the start_time of this DigitalHumanModelingJobInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The start_time of this DigitalHumanModelingJobInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DigitalHumanModelingJobInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param start_time: The start_time of this DigitalHumanModelingJobInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DigitalHumanModelingJobInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The end_time of this DigitalHumanModelingJobInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DigitalHumanModelingJobInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param end_time: The end_time of this DigitalHumanModelingJobInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_info(self):
        r"""Gets the error_info of this DigitalHumanModelingJobInfo.

        :return: The error_info of this DigitalHumanModelingJobInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this DigitalHumanModelingJobInfo.

        :param error_info: The error_info of this DigitalHumanModelingJobInfo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

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
        if not isinstance(other, DigitalHumanModelingJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
