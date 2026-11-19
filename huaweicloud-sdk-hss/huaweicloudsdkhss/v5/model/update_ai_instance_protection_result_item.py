# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiInstanceProtectionResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'succeed': 'bool',
        'error_msg': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'succeed': 'succeed',
        'error_msg': 'error_msg'
    }

    def __init__(self, agent_id=None, succeed=None, error_msg=None):
        r"""UpdateAiInstanceProtectionResultItem

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 
        :type agent_id: str
        :param succeed: **参数解释**： 处理是否成功 **取值范围**： - true：成功 - false：失败 
        :type succeed: bool
        :param error_msg: **参数解释**： 错误消息，仅失败时返回 **取值范围**： 字符长度为0-256位 
        :type error_msg: str
        """
        
        

        self._agent_id = None
        self._succeed = None
        self._error_msg = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if succeed is not None:
            self.succeed = succeed
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def agent_id(self):
        r"""Gets the agent_id of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :return: The agent_id of this UpdateAiInstanceProtectionResultItem.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :param agent_id: The agent_id of this UpdateAiInstanceProtectionResultItem.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def succeed(self):
        r"""Gets the succeed of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 处理是否成功 **取值范围**： - true：成功 - false：失败 

        :return: The succeed of this UpdateAiInstanceProtectionResultItem.
        :rtype: bool
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        r"""Sets the succeed of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 处理是否成功 **取值范围**： - true：成功 - false：失败 

        :param succeed: The succeed of this UpdateAiInstanceProtectionResultItem.
        :type succeed: bool
        """
        self._succeed = succeed

    @property
    def error_msg(self):
        r"""Gets the error_msg of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 错误消息，仅失败时返回 **取值范围**： 字符长度为0-256位 

        :return: The error_msg of this UpdateAiInstanceProtectionResultItem.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this UpdateAiInstanceProtectionResultItem.

        **参数解释**： 错误消息，仅失败时返回 **取值范围**： 字符长度为0-256位 

        :param error_msg: The error_msg of this UpdateAiInstanceProtectionResultItem.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, UpdateAiInstanceProtectionResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
