# coding: utf-8

import pprint
import re

import six





class CCEJobStatus:


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
        """CCEJobStatus - a model defined in huaweicloud sdk"""
        
        

        self._phase = None
        self._reason = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if reason is not None:
            self.reason = reason

    @property
    def phase(self):
        """Gets the phase of this CCEJobStatus.

        作业的状态，有如下四种状态：  - JobPhaseInitializing JobPhase = \"Initializing\" - JobPhaseRunning JobPhase = \"Running\" - JobPhaseFailed JobPhase = \"Failed\" - JobPhaseSuccess JobPhase = \"Success\"

        :return: The phase of this CCEJobStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this CCEJobStatus.

        作业的状态，有如下四种状态：  - JobPhaseInitializing JobPhase = \"Initializing\" - JobPhaseRunning JobPhase = \"Running\" - JobPhaseFailed JobPhase = \"Failed\" - JobPhaseSuccess JobPhase = \"Success\"

        :param phase: The phase of this CCEJobStatus.
        :type: str
        """
        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this CCEJobStatus.

        作业变为当前状态的原因

        :return: The reason of this CCEJobStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CCEJobStatus.

        作业变为当前状态的原因

        :param reason: The reason of this CCEJobStatus.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CCEJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
