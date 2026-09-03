# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBackupRetainPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto': 'str',
        'manual': 'str',
        'instanceids': 'list[str]'
    }

    attribute_map = {
        'auto': 'auto',
        'manual': 'manual',
        'instanceids': 'instanceids'
    }

    def __init__(self, auto=None, manual=None, instanceids=None):
        r"""SetBackupRetainPolicyRequestBody

        The model defined in huaweicloud sdk

        :param auto: **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及       **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。
        :type auto: str
        :param manual: **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及      **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。
        :type manual: str
        :param instanceids: **参数解释**  实例ID列表，实例ID是实例的唯一标识。  **约束限制**  不涉及。  **取值范围**  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**  不涉及。
        :type instanceids: list[str]
        """
        
        

        self._auto = None
        self._manual = None
        self._instanceids = None
        self.discriminator = None

        self.auto = auto
        self.manual = manual
        self.instanceids = instanceids

    @property
    def auto(self):
        r"""Gets the auto of this SetBackupRetainPolicyRequestBody.

        **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及       **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。

        :return: The auto of this SetBackupRetainPolicyRequestBody.
        :rtype: str
        """
        return self._auto

    @auto.setter
    def auto(self, auto):
        r"""Sets the auto of this SetBackupRetainPolicyRequestBody.

        **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及       **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。

        :param auto: The auto of this SetBackupRetainPolicyRequestBody.
        :type auto: str
        """
        self._auto = auto

    @property
    def manual(self):
        r"""Gets the manual of this SetBackupRetainPolicyRequestBody.

        **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及      **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。

        :return: The manual of this SetBackupRetainPolicyRequestBody.
        :rtype: str
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        r"""Sets the manual of this SetBackupRetainPolicyRequestBody.

        **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及      **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及。

        :param manual: The manual of this SetBackupRetainPolicyRequestBody.
        :type manual: str
        """
        self._manual = manual

    @property
    def instanceids(self):
        r"""Gets the instanceids of this SetBackupRetainPolicyRequestBody.

        **参数解释**  实例ID列表，实例ID是实例的唯一标识。  **约束限制**  不涉及。  **取值范围**  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**  不涉及。

        :return: The instanceids of this SetBackupRetainPolicyRequestBody.
        :rtype: list[str]
        """
        return self._instanceids

    @instanceids.setter
    def instanceids(self, instanceids):
        r"""Sets the instanceids of this SetBackupRetainPolicyRequestBody.

        **参数解释**  实例ID列表，实例ID是实例的唯一标识。  **约束限制**  不涉及。  **取值范围**  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**  不涉及。

        :param instanceids: The instanceids of this SetBackupRetainPolicyRequestBody.
        :type instanceids: list[str]
        """
        self._instanceids = instanceids

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
        if not isinstance(other, SetBackupRetainPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
