# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildCommandRiskDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remediation': 'str',
        'build_instruction': 'str'
    }

    attribute_map = {
        'remediation': 'remediation',
        'build_instruction': 'build_instruction'
    }

    def __init__(self, remediation=None, build_instruction=None):
        r"""BuildCommandRiskDetailResponseInfo

        The model defined in huaweicloud sdk

        :param remediation: **参数解释** 风险的处置建议 **取值范围** 字符长度0-65534位
        :type remediation: str
        :param build_instruction: **参数解释** 存在风险的构建指令 **取值范围** 字符长度0-256位
        :type build_instruction: str
        """
        
        

        self._remediation = None
        self._build_instruction = None
        self.discriminator = None

        if remediation is not None:
            self.remediation = remediation
        if build_instruction is not None:
            self.build_instruction = build_instruction

    @property
    def remediation(self):
        r"""Gets the remediation of this BuildCommandRiskDetailResponseInfo.

        **参数解释** 风险的处置建议 **取值范围** 字符长度0-65534位

        :return: The remediation of this BuildCommandRiskDetailResponseInfo.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        r"""Sets the remediation of this BuildCommandRiskDetailResponseInfo.

        **参数解释** 风险的处置建议 **取值范围** 字符长度0-65534位

        :param remediation: The remediation of this BuildCommandRiskDetailResponseInfo.
        :type remediation: str
        """
        self._remediation = remediation

    @property
    def build_instruction(self):
        r"""Gets the build_instruction of this BuildCommandRiskDetailResponseInfo.

        **参数解释** 存在风险的构建指令 **取值范围** 字符长度0-256位

        :return: The build_instruction of this BuildCommandRiskDetailResponseInfo.
        :rtype: str
        """
        return self._build_instruction

    @build_instruction.setter
    def build_instruction(self, build_instruction):
        r"""Sets the build_instruction of this BuildCommandRiskDetailResponseInfo.

        **参数解释** 存在风险的构建指令 **取值范围** 字符长度0-256位

        :param build_instruction: The build_instruction of this BuildCommandRiskDetailResponseInfo.
        :type build_instruction: str
        """
        self._build_instruction = build_instruction

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
        if not isinstance(other, BuildCommandRiskDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
