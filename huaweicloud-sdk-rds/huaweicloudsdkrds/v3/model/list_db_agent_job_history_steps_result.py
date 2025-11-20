# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbAgentJobHistoryStepsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_id': 'str',
        'step_name': 'str',
        'run_status': 'str',
        'run_time': 'str',
        'run_duration': 'str',
        'message': 'str'
    }

    attribute_map = {
        'step_id': 'step_id',
        'step_name': 'step_name',
        'run_status': 'run_status',
        'run_time': 'run_time',
        'run_duration': 'run_duration',
        'message': 'message'
    }

    def __init__(self, step_id=None, step_name=None, run_status=None, run_time=None, run_duration=None, message=None):
        r"""ListDbAgentJobHistoryStepsResult

        The model defined in huaweicloud sdk

        :param step_id: 步骤id。
        :type step_id: str
        :param step_name: 步骤名。
        :type step_name: str
        :param run_status: 作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。
        :type run_status: str
        :param run_time: 作业执行开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type run_time: str
        :param run_duration: 作业执行时长。格式为hh:mm:ss
        :type run_duration: str
        :param message: 执行信息。
        :type message: str
        """
        
        

        self._step_id = None
        self._step_name = None
        self._run_status = None
        self._run_time = None
        self._run_duration = None
        self._message = None
        self.discriminator = None

        if step_id is not None:
            self.step_id = step_id
        if step_name is not None:
            self.step_name = step_name
        if run_status is not None:
            self.run_status = run_status
        if run_time is not None:
            self.run_time = run_time
        if run_duration is not None:
            self.run_duration = run_duration
        if message is not None:
            self.message = message

    @property
    def step_id(self):
        r"""Gets the step_id of this ListDbAgentJobHistoryStepsResult.

        步骤id。

        :return: The step_id of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        r"""Sets the step_id of this ListDbAgentJobHistoryStepsResult.

        步骤id。

        :param step_id: The step_id of this ListDbAgentJobHistoryStepsResult.
        :type step_id: str
        """
        self._step_id = step_id

    @property
    def step_name(self):
        r"""Gets the step_name of this ListDbAgentJobHistoryStepsResult.

        步骤名。

        :return: The step_name of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        r"""Sets the step_name of this ListDbAgentJobHistoryStepsResult.

        步骤名。

        :param step_name: The step_name of this ListDbAgentJobHistoryStepsResult.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def run_status(self):
        r"""Gets the run_status of this ListDbAgentJobHistoryStepsResult.

        作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。

        :return: The run_status of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this ListDbAgentJobHistoryStepsResult.

        作业执行状态。取值如下:  failed:失败。 succeeded:成功。 retrying:重试中。 canceled:已取消。 in_progress:正在运行。

        :param run_status: The run_status of this ListDbAgentJobHistoryStepsResult.
        :type run_status: str
        """
        self._run_status = run_status

    @property
    def run_time(self):
        r"""Gets the run_time of this ListDbAgentJobHistoryStepsResult.

        作业执行开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The run_time of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._run_time

    @run_time.setter
    def run_time(self, run_time):
        r"""Sets the run_time of this ListDbAgentJobHistoryStepsResult.

        作业执行开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param run_time: The run_time of this ListDbAgentJobHistoryStepsResult.
        :type run_time: str
        """
        self._run_time = run_time

    @property
    def run_duration(self):
        r"""Gets the run_duration of this ListDbAgentJobHistoryStepsResult.

        作业执行时长。格式为hh:mm:ss

        :return: The run_duration of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._run_duration

    @run_duration.setter
    def run_duration(self, run_duration):
        r"""Sets the run_duration of this ListDbAgentJobHistoryStepsResult.

        作业执行时长。格式为hh:mm:ss

        :param run_duration: The run_duration of this ListDbAgentJobHistoryStepsResult.
        :type run_duration: str
        """
        self._run_duration = run_duration

    @property
    def message(self):
        r"""Gets the message of this ListDbAgentJobHistoryStepsResult.

        执行信息。

        :return: The message of this ListDbAgentJobHistoryStepsResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListDbAgentJobHistoryStepsResult.

        执行信息。

        :param message: The message of this ListDbAgentJobHistoryStepsResult.
        :type message: str
        """
        self._message = message

    def to_dict(self):
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
        if not isinstance(other, ListDbAgentJobHistoryStepsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
