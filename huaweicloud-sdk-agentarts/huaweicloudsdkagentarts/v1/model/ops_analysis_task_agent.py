# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAnalysisTaskAgent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, type=None, id=None):
        r"""OpsAnalysisTaskAgent

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 智能体类型。  **约束限制：** 不涉及  **取值范围：** agent：单智能体，workflow：工作流，agentrun：部署在运行时的智能体，third_party：三方接入观测的智能体。  **默认取值：** 无
        :type type: str
        :param id: **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无
        :type id: str
        """
        
        

        self._type = None
        self._id = None
        self.discriminator = None

        self.type = type
        self.id = id

    @property
    def type(self):
        r"""Gets the type of this OpsAnalysisTaskAgent.

        **参数解释：** 智能体类型。  **约束限制：** 不涉及  **取值范围：** agent：单智能体，workflow：工作流，agentrun：部署在运行时的智能体，third_party：三方接入观测的智能体。  **默认取值：** 无

        :return: The type of this OpsAnalysisTaskAgent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsAnalysisTaskAgent.

        **参数解释：** 智能体类型。  **约束限制：** 不涉及  **取值范围：** agent：单智能体，workflow：工作流，agentrun：部署在运行时的智能体，third_party：三方接入观测的智能体。  **默认取值：** 无

        :param type: The type of this OpsAnalysisTaskAgent.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this OpsAnalysisTaskAgent.

        **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无

        :return: The id of this OpsAnalysisTaskAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsAnalysisTaskAgent.

        **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无

        :param id: The id of this OpsAnalysisTaskAgent.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, OpsAnalysisTaskAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
