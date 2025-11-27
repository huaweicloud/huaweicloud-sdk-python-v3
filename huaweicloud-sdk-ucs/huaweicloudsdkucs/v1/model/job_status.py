# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'reason': 'str',
        'completion_time': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'phase': 'phase',
        'reason': 'reason',
        'completion_time': 'completionTime',
        'start_time': 'startTime'
    }

    def __init__(self, phase=None, reason=None, completion_time=None, start_time=None):
        r"""JobStatus

        The model defined in huaweicloud sdk

        :param phase: Job phase
        :type phase: str
        :param reason: Job reason
        :type reason: str
        :param completion_time: Job完成时间
        :type completion_time: str
        :param start_time: Job开始时间
        :type start_time: str
        """
        
        

        self._phase = None
        self._reason = None
        self._completion_time = None
        self._start_time = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason
        if completion_time is not None:
            self.completion_time = completion_time
        if start_time is not None:
            self.start_time = start_time

    @property
    def phase(self):
        r"""Gets the phase of this JobStatus.

        Job phase

        :return: The phase of this JobStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this JobStatus.

        Job phase

        :param phase: The phase of this JobStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def reason(self):
        r"""Gets the reason of this JobStatus.

        Job reason

        :return: The reason of this JobStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this JobStatus.

        Job reason

        :param reason: The reason of this JobStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def completion_time(self):
        r"""Gets the completion_time of this JobStatus.

        Job完成时间

        :return: The completion_time of this JobStatus.
        :rtype: str
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        r"""Sets the completion_time of this JobStatus.

        Job完成时间

        :param completion_time: The completion_time of this JobStatus.
        :type completion_time: str
        """
        self._completion_time = completion_time

    @property
    def start_time(self):
        r"""Gets the start_time of this JobStatus.

        Job开始时间

        :return: The start_time of this JobStatus.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobStatus.

        Job开始时间

        :param start_time: The start_time of this JobStatus.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
