# coding: utf-8

import six

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
        'reason': 'str'
    }

    attribute_map = {
        'phase': 'phase',
        'reason': 'reason'
    }

    def __init__(self, phase=None, reason=None):
        """JobStatus

        The model defined in huaweicloud sdk

        :param phase: 任务的状态，有如下四种状态：  - JobPhaseInitializing JobPhase &#x3D; \&quot;Initializing\&quot; - JobPhaseRunning JobPhase &#x3D; \&quot;Running\&quot; - JobPhaseFailed JobPhase &#x3D; \&quot;Failed\&quot; - JobPhaseSuccess JobPhase &#x3D; \&quot;Success\&quot;
        :type phase: str
        :param reason: 任务变为当前状态的原因
        :type reason: str
        """
        
        

        self._phase = None
        self._reason = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason

    @property
    def phase(self):
        """Gets the phase of this JobStatus.

        任务的状态，有如下四种状态：  - JobPhaseInitializing JobPhase = \"Initializing\" - JobPhaseRunning JobPhase = \"Running\" - JobPhaseFailed JobPhase = \"Failed\" - JobPhaseSuccess JobPhase = \"Success\"

        :return: The phase of this JobStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this JobStatus.

        任务的状态，有如下四种状态：  - JobPhaseInitializing JobPhase = \"Initializing\" - JobPhaseRunning JobPhase = \"Running\" - JobPhaseFailed JobPhase = \"Failed\" - JobPhaseSuccess JobPhase = \"Success\"

        :param phase: The phase of this JobStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this JobStatus.

        任务变为当前状态的原因

        :return: The reason of this JobStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this JobStatus.

        任务变为当前状态的原因

        :param reason: The reason of this JobStatus.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
