# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoMotionCaptureInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'motion_capture_mode': 'str',
        'input_info': 'InputInfo',
        'output_info': 'OutputInfo',
        'job_id': 'str',
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'motion_capture_mode': 'motion_capture_mode',
        'input_info': 'input_info',
        'output_info': 'output_info',
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, motion_capture_mode=None, input_info=None, output_info=None, job_id=None, state=None, start_time=None, end_time=None):
        """VideoMotionCaptureInfo

        The model defined in huaweicloud sdk

        :param motion_capture_mode: 视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动
        :type motion_capture_mode: str
        :param input_info: 
        :type input_info: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        :param output_info: 
        :type output_info: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        :param job_id: 视频驱动任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待中 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败
        :type state: str
        :param start_time: 任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type start_time: str
        :param end_time: 任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type end_time: str
        """
        
        

        self._motion_capture_mode = None
        self._input_info = None
        self._output_info = None
        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if motion_capture_mode is not None:
            self.motion_capture_mode = motion_capture_mode
        if input_info is not None:
            self.input_info = input_info
        if output_info is not None:
            self.output_info = output_info
        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def motion_capture_mode(self):
        """Gets the motion_capture_mode of this VideoMotionCaptureInfo.

        视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动

        :return: The motion_capture_mode of this VideoMotionCaptureInfo.
        :rtype: str
        """
        return self._motion_capture_mode

    @motion_capture_mode.setter
    def motion_capture_mode(self, motion_capture_mode):
        """Sets the motion_capture_mode of this VideoMotionCaptureInfo.

        视频驱动模式。 * HEAD：头部 * HALF_BODY：半身 * FULL_BODY：全身 * AUTO：自动

        :param motion_capture_mode: The motion_capture_mode of this VideoMotionCaptureInfo.
        :type motion_capture_mode: str
        """
        self._motion_capture_mode = motion_capture_mode

    @property
    def input_info(self):
        """Gets the input_info of this VideoMotionCaptureInfo.

        :return: The input_info of this VideoMotionCaptureInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        """
        return self._input_info

    @input_info.setter
    def input_info(self, input_info):
        """Sets the input_info of this VideoMotionCaptureInfo.

        :param input_info: The input_info of this VideoMotionCaptureInfo.
        :type input_info: :class:`huaweicloudsdkmetastudio.v1.InputInfo`
        """
        self._input_info = input_info

    @property
    def output_info(self):
        """Gets the output_info of this VideoMotionCaptureInfo.

        :return: The output_info of this VideoMotionCaptureInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        """
        return self._output_info

    @output_info.setter
    def output_info(self, output_info):
        """Sets the output_info of this VideoMotionCaptureInfo.

        :param output_info: The output_info of this VideoMotionCaptureInfo.
        :type output_info: :class:`huaweicloudsdkmetastudio.v1.OutputInfo`
        """
        self._output_info = output_info

    @property
    def job_id(self):
        """Gets the job_id of this VideoMotionCaptureInfo.

        视频驱动任务ID。

        :return: The job_id of this VideoMotionCaptureInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this VideoMotionCaptureInfo.

        视频驱动任务ID。

        :param job_id: The job_id of this VideoMotionCaptureInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        """Gets the state of this VideoMotionCaptureInfo.

        任务的状态。 * WAITING：等待中 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :return: The state of this VideoMotionCaptureInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VideoMotionCaptureInfo.

        任务的状态。 * WAITING：等待中 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败

        :param state: The state of this VideoMotionCaptureInfo.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this VideoMotionCaptureInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The start_time of this VideoMotionCaptureInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this VideoMotionCaptureInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param start_time: The start_time of this VideoMotionCaptureInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this VideoMotionCaptureInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The end_time of this VideoMotionCaptureInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this VideoMotionCaptureInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param end_time: The end_time of this VideoMotionCaptureInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, VideoMotionCaptureInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
