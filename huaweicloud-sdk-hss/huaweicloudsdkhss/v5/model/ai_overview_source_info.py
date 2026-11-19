# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOverviewSourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_agents': 'int',
        'protected_agents': 'int',
        'unprotected_agents': 'int'
    }

    attribute_map = {
        'total_agents': 'total_agents',
        'protected_agents': 'protected_agents',
        'unprotected_agents': 'unprotected_agents'
    }

    def __init__(self, total_agents=None, protected_agents=None, unprotected_agents=None):
        r"""AiOverviewSourceInfo

        The model defined in huaweicloud sdk

        :param total_agents: **参数解释**： 智能体总数 **取值范围**： 最小值0，最大值2000000 
        :type total_agents: int
        :param protected_agents: **参数解释**： 已防护智能体数量 **取值范围**： 最小值0，最大值2000000 
        :type protected_agents: int
        :param unprotected_agents: **参数解释**： 未防护智能体数量 **取值范围**： 最小值0，最大值2000000 
        :type unprotected_agents: int
        """
        
        

        self._total_agents = None
        self._protected_agents = None
        self._unprotected_agents = None
        self.discriminator = None

        if total_agents is not None:
            self.total_agents = total_agents
        if protected_agents is not None:
            self.protected_agents = protected_agents
        if unprotected_agents is not None:
            self.unprotected_agents = unprotected_agents

    @property
    def total_agents(self):
        r"""Gets the total_agents of this AiOverviewSourceInfo.

        **参数解释**： 智能体总数 **取值范围**： 最小值0，最大值2000000 

        :return: The total_agents of this AiOverviewSourceInfo.
        :rtype: int
        """
        return self._total_agents

    @total_agents.setter
    def total_agents(self, total_agents):
        r"""Sets the total_agents of this AiOverviewSourceInfo.

        **参数解释**： 智能体总数 **取值范围**： 最小值0，最大值2000000 

        :param total_agents: The total_agents of this AiOverviewSourceInfo.
        :type total_agents: int
        """
        self._total_agents = total_agents

    @property
    def protected_agents(self):
        r"""Gets the protected_agents of this AiOverviewSourceInfo.

        **参数解释**： 已防护智能体数量 **取值范围**： 最小值0，最大值2000000 

        :return: The protected_agents of this AiOverviewSourceInfo.
        :rtype: int
        """
        return self._protected_agents

    @protected_agents.setter
    def protected_agents(self, protected_agents):
        r"""Sets the protected_agents of this AiOverviewSourceInfo.

        **参数解释**： 已防护智能体数量 **取值范围**： 最小值0，最大值2000000 

        :param protected_agents: The protected_agents of this AiOverviewSourceInfo.
        :type protected_agents: int
        """
        self._protected_agents = protected_agents

    @property
    def unprotected_agents(self):
        r"""Gets the unprotected_agents of this AiOverviewSourceInfo.

        **参数解释**： 未防护智能体数量 **取值范围**： 最小值0，最大值2000000 

        :return: The unprotected_agents of this AiOverviewSourceInfo.
        :rtype: int
        """
        return self._unprotected_agents

    @unprotected_agents.setter
    def unprotected_agents(self, unprotected_agents):
        r"""Sets the unprotected_agents of this AiOverviewSourceInfo.

        **参数解释**： 未防护智能体数量 **取值范围**： 最小值0，最大值2000000 

        :param unprotected_agents: The unprotected_agents of this AiOverviewSourceInfo.
        :type unprotected_agents: int
        """
        self._unprotected_agents = unprotected_agents

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
        if not isinstance(other, AiOverviewSourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
