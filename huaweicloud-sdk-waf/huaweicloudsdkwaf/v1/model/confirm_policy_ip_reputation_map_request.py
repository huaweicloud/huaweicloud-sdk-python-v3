# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmPolicyIpReputationMapRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lang': 'str',
        'type': 'str'
    }

    attribute_map = {
        'lang': 'lang',
        'type': 'type'
    }

    def __init__(self, lang=None, type=None):
        r"""ConfirmPolicyIpReputationMapRequest

        The model defined in huaweicloud sdk

        :param lang: **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn
        :type lang: str
        :param type: **参数解释：** 防护选项的详细信息的类型，当前仅支持“idc”。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        """
        
        

        self._lang = None
        self._type = None
        self.discriminator = None

        self.lang = lang
        self.type = type

    @property
    def lang(self):
        r"""Gets the lang of this ConfirmPolicyIpReputationMapRequest.

        **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn

        :return: The lang of this ConfirmPolicyIpReputationMapRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this ConfirmPolicyIpReputationMapRequest.

        **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn

        :param lang: The lang of this ConfirmPolicyIpReputationMapRequest.
        :type lang: str
        """
        self._lang = lang

    @property
    def type(self):
        r"""Gets the type of this ConfirmPolicyIpReputationMapRequest.

        **参数解释：** 防护选项的详细信息的类型，当前仅支持“idc”。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this ConfirmPolicyIpReputationMapRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfirmPolicyIpReputationMapRequest.

        **参数解释：** 防护选项的详细信息的类型，当前仅支持“idc”。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this ConfirmPolicyIpReputationMapRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ConfirmPolicyIpReputationMapRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
