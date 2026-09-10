# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningTargetAgent:

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
        'id': 'str',
        'version': 'str',
        'node_type': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'version': 'version',
        'node_type': 'node_type',
        'node_id': 'node_id'
    }

    def __init__(self, type=None, id=None, version=None, node_type=None, node_id=None):
        r"""OpsTuningTargetAgent

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 智能体类型，区分优化目标是单智能体还是工作流。  **约束限制：** 不涉及  **取值范围：** 单智能体agent，工作流workflow。  **默认取值：** 无
        :type type: str
        :param id: **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无
        :type id: str
        :param version: **参数解释：** 智能体版本。  **约束限制：** 不涉及  **取值范围：** 版本号字符串。  **默认取值：** latest
        :type version: str
        :param node_type: **参数解释：** 工作流节点类型，仅当type为workflow时有效，指定优化工作流中的哪类节点。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 意图识别intent_detection，大模型llm。  **默认取值：** 无
        :type node_type: str
        :param node_id: **参数解释：** 工作流节点ID，对应工作流中特定节点的唯一标识。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的工作流需要是“已提交”状态。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 有效节点标识符字符串。  **默认取值：** 无
        :type node_id: str
        """
        
        

        self._type = None
        self._id = None
        self._version = None
        self._node_type = None
        self._node_id = None
        self.discriminator = None

        self.type = type
        self.id = id
        if version is not None:
            self.version = version
        if node_type is not None:
            self.node_type = node_type
        if node_id is not None:
            self.node_id = node_id

    @property
    def type(self):
        r"""Gets the type of this OpsTuningTargetAgent.

        **参数解释：** 智能体类型，区分优化目标是单智能体还是工作流。  **约束限制：** 不涉及  **取值范围：** 单智能体agent，工作流workflow。  **默认取值：** 无

        :return: The type of this OpsTuningTargetAgent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsTuningTargetAgent.

        **参数解释：** 智能体类型，区分优化目标是单智能体还是工作流。  **约束限制：** 不涉及  **取值范围：** 单智能体agent，工作流workflow。  **默认取值：** 无

        :param type: The type of this OpsTuningTargetAgent.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this OpsTuningTargetAgent.

        **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无

        :return: The id of this OpsTuningTargetAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsTuningTargetAgent.

        **参数解释：** 智能体ID，对应AgentArts平台中的智能体实例。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的智能体需要是“已提交”状态。  **约束限制：** 必须是系统中存在的真实ID。  **取值范围：** 有效标识符字符串。  **默认取值：** 无

        :param id: The id of this OpsTuningTargetAgent.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this OpsTuningTargetAgent.

        **参数解释：** 智能体版本。  **约束限制：** 不涉及  **取值范围：** 版本号字符串。  **默认取值：** latest

        :return: The version of this OpsTuningTargetAgent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OpsTuningTargetAgent.

        **参数解释：** 智能体版本。  **约束限制：** 不涉及  **取值范围：** 版本号字符串。  **默认取值：** latest

        :param version: The version of this OpsTuningTargetAgent.
        :type version: str
        """
        self._version = version

    @property
    def node_type(self):
        r"""Gets the node_type of this OpsTuningTargetAgent.

        **参数解释：** 工作流节点类型，仅当type为workflow时有效，指定优化工作流中的哪类节点。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 意图识别intent_detection，大模型llm。  **默认取值：** 无

        :return: The node_type of this OpsTuningTargetAgent.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this OpsTuningTargetAgent.

        **参数解释：** 工作流节点类型，仅当type为workflow时有效，指定优化工作流中的哪类节点。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 意图识别intent_detection，大模型llm。  **默认取值：** 无

        :param node_type: The node_type of this OpsTuningTargetAgent.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_id(self):
        r"""Gets the node_id of this OpsTuningTargetAgent.

        **参数解释：** 工作流节点ID，对应工作流中特定节点的唯一标识。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的工作流需要是“已提交”状态。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 有效节点标识符字符串。  **默认取值：** 无

        :return: The node_id of this OpsTuningTargetAgent.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this OpsTuningTargetAgent.

        **参数解释：** 工作流节点ID，对应工作流中特定节点的唯一标识。 可在AgentArts平台“智能体管理”页面获取ID，注意对应的工作流需要是“已提交”状态。  **约束限制：** 仅当type为workflow时生效。  **取值范围：** 有效节点标识符字符串。  **默认取值：** 无

        :param node_id: The node_id of this OpsTuningTargetAgent.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, OpsTuningTargetAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
