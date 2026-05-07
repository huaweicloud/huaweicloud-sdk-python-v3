# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentStatusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_status': 'str',
        'status_time': 'int',
        'abnormal_reason': 'str'
    }

    attribute_map = {
        'agent_status': 'agent_status',
        'status_time': 'status_time',
        'abnormal_reason': 'abnormal_reason'
    }

    def __init__(self, agent_status=None, status_time=None, abnormal_reason=None):
        r"""AgentStatusInfo

        The model defined in huaweicloud sdk

        :param agent_status: **参数解释**: Agent状态 **取值范围**: 包含如下3种。 - online：在线。 - offline：离线。 - agent_protect_interrupted：防护中断。
        :type agent_status: str
        :param status_time: **参数解释**： agent状态时间，采用时间戳，默认毫秒 **取值范围**： 0-4824695185000
        :type status_time: int
        :param abnormal_reason: **参数解释**： 异常原因 **取值范围**： 字符长度0-512位
        :type abnormal_reason: str
        """
        
        

        self._agent_status = None
        self._status_time = None
        self._abnormal_reason = None
        self.discriminator = None

        if agent_status is not None:
            self.agent_status = agent_status
        if status_time is not None:
            self.status_time = status_time
        if abnormal_reason is not None:
            self.abnormal_reason = abnormal_reason

    @property
    def agent_status(self):
        r"""Gets the agent_status of this AgentStatusInfo.

        **参数解释**: Agent状态 **取值范围**: 包含如下3种。 - online：在线。 - offline：离线。 - agent_protect_interrupted：防护中断。

        :return: The agent_status of this AgentStatusInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this AgentStatusInfo.

        **参数解释**: Agent状态 **取值范围**: 包含如下3种。 - online：在线。 - offline：离线。 - agent_protect_interrupted：防护中断。

        :param agent_status: The agent_status of this AgentStatusInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def status_time(self):
        r"""Gets the status_time of this AgentStatusInfo.

        **参数解释**： agent状态时间，采用时间戳，默认毫秒 **取值范围**： 0-4824695185000

        :return: The status_time of this AgentStatusInfo.
        :rtype: int
        """
        return self._status_time

    @status_time.setter
    def status_time(self, status_time):
        r"""Sets the status_time of this AgentStatusInfo.

        **参数解释**： agent状态时间，采用时间戳，默认毫秒 **取值范围**： 0-4824695185000

        :param status_time: The status_time of this AgentStatusInfo.
        :type status_time: int
        """
        self._status_time = status_time

    @property
    def abnormal_reason(self):
        r"""Gets the abnormal_reason of this AgentStatusInfo.

        **参数解释**： 异常原因 **取值范围**： 字符长度0-512位

        :return: The abnormal_reason of this AgentStatusInfo.
        :rtype: str
        """
        return self._abnormal_reason

    @abnormal_reason.setter
    def abnormal_reason(self, abnormal_reason):
        r"""Sets the abnormal_reason of this AgentStatusInfo.

        **参数解释**： 异常原因 **取值范围**： 字符长度0-512位

        :param abnormal_reason: The abnormal_reason of this AgentStatusInfo.
        :type abnormal_reason: str
        """
        self._abnormal_reason = abnormal_reason

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
        if not isinstance(other, AgentStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
