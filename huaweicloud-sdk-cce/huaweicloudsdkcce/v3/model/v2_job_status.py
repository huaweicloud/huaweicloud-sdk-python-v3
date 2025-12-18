# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2JobStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'reason': 'str',
        'completion_time': 'str'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'reason',
        'completion_time': 'completionTime'
    }

    def __init__(self, status=None, reason=None, completion_time=None):
        r"""V2JobStatus

        The model defined in huaweicloud sdk

        :param status: **参数解释**： Job的状态 **约束限制**： 不涉及 **取值范围**： - Initializing：未执行 - Running：执行中 - Failed：执行失败 - Success：执行成功  **默认取值**： 不涉及
        :type status: str
        :param reason: **参数解释**： Job执行失败的原因 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type reason: str
        :param completion_time: **参数解释**： Job完成时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type completion_time: str
        """
        
        

        self._status = None
        self._reason = None
        self._completion_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if completion_time is not None:
            self.completion_time = completion_time

    @property
    def status(self):
        r"""Gets the status of this V2JobStatus.

        **参数解释**： Job的状态 **约束限制**： 不涉及 **取值范围**： - Initializing：未执行 - Running：执行中 - Failed：执行失败 - Success：执行成功  **默认取值**： 不涉及

        :return: The status of this V2JobStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this V2JobStatus.

        **参数解释**： Job的状态 **约束限制**： 不涉及 **取值范围**： - Initializing：未执行 - Running：执行中 - Failed：执行失败 - Success：执行成功  **默认取值**： 不涉及

        :param status: The status of this V2JobStatus.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this V2JobStatus.

        **参数解释**： Job执行失败的原因 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The reason of this V2JobStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this V2JobStatus.

        **参数解释**： Job执行失败的原因 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param reason: The reason of this V2JobStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def completion_time(self):
        r"""Gets the completion_time of this V2JobStatus.

        **参数解释**： Job完成时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The completion_time of this V2JobStatus.
        :rtype: str
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        r"""Sets the completion_time of this V2JobStatus.

        **参数解释**： Job完成时间 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param completion_time: The completion_time of this V2JobStatus.
        :type completion_time: str
        """
        self._completion_time = completion_time

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
        if not isinstance(other, V2JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
