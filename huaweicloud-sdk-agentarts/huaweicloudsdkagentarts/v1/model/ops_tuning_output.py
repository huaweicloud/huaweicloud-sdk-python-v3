# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tools': 'list[OpsToolOutput]',
        'skills': 'list[OpsSkillOutput]'
    }

    attribute_map = {
        'tools': 'tools',
        'skills': 'skills'
    }

    def __init__(self, tools=None, skills=None):
        r"""OpsTuningOutput

        The model defined in huaweicloud sdk

        :param tools: **参数解释：** 待优化的工具列表，type为tool时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。
        :type tools: list[:class:`huaweicloudsdkagentarts.v1.OpsToolOutput`]
        :param skills: **参数解释：** 待优化的技能列表，type为skill时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。
        :type skills: list[:class:`huaweicloudsdkagentarts.v1.OpsSkillOutput`]
        """
        
        

        self._tools = None
        self._skills = None
        self.discriminator = None

        if tools is not None:
            self.tools = tools
        if skills is not None:
            self.skills = skills

    @property
    def tools(self):
        r"""Gets the tools of this OpsTuningOutput.

        **参数解释：** 待优化的工具列表，type为tool时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。

        :return: The tools of this OpsTuningOutput.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsToolOutput`]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        r"""Sets the tools of this OpsTuningOutput.

        **参数解释：** 待优化的工具列表，type为tool时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。

        :param tools: The tools of this OpsTuningOutput.
        :type tools: list[:class:`huaweicloudsdkagentarts.v1.OpsToolOutput`]
        """
        self._tools = tools

    @property
    def skills(self):
        r"""Gets the skills of this OpsTuningOutput.

        **参数解释：** 待优化的技能列表，type为skill时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。

        :return: The skills of this OpsTuningOutput.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSkillOutput`]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        r"""Sets the skills of this OpsTuningOutput.

        **参数解释：** 待优化的技能列表，type为skill时必填。  **约束限制：** 不涉及  **取值范围：** 数组长度0-10。  **默认取值：** 空数组。

        :param skills: The skills of this OpsTuningOutput.
        :type skills: list[:class:`huaweicloudsdkagentarts.v1.OpsSkillOutput`]
        """
        self._skills = skills

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
        if not isinstance(other, OpsTuningOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
