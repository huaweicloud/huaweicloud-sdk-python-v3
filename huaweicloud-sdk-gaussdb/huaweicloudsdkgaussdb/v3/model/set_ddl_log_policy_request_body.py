# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDdlLogPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_status': 'str',
        'keep_days': 'int'
    }

    attribute_map = {
        'switch_status': 'switch_status',
        'keep_days': 'keep_days'
    }

    def __init__(self, switch_status=None, keep_days=None):
        r"""SetDdlLogPolicyRequestBody

        The model defined in huaweicloud sdk

        :param switch_status: **参数解释**：  设置DDL日志下载功能开关。  **约束限制**：  不涉及。  **取值范围**：  - ON，开启。 - OFF，关闭。  **默认取值**：  不涉及。 
        :type switch_status: str
        :param keep_days: **参数解释**：  设置DDL日志保留天数。  **约束限制**：  不涉及。  **取值范围**：  1~30。  **默认取值**：  3。 
        :type keep_days: int
        """
        
        

        self._switch_status = None
        self._keep_days = None
        self.discriminator = None

        self.switch_status = switch_status
        self.keep_days = keep_days

    @property
    def switch_status(self):
        r"""Gets the switch_status of this SetDdlLogPolicyRequestBody.

        **参数解释**：  设置DDL日志下载功能开关。  **约束限制**：  不涉及。  **取值范围**：  - ON，开启。 - OFF，关闭。  **默认取值**：  不涉及。 

        :return: The switch_status of this SetDdlLogPolicyRequestBody.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        r"""Sets the switch_status of this SetDdlLogPolicyRequestBody.

        **参数解释**：  设置DDL日志下载功能开关。  **约束限制**：  不涉及。  **取值范围**：  - ON，开启。 - OFF，关闭。  **默认取值**：  不涉及。 

        :param switch_status: The switch_status of this SetDdlLogPolicyRequestBody.
        :type switch_status: str
        """
        self._switch_status = switch_status

    @property
    def keep_days(self):
        r"""Gets the keep_days of this SetDdlLogPolicyRequestBody.

        **参数解释**：  设置DDL日志保留天数。  **约束限制**：  不涉及。  **取值范围**：  1~30。  **默认取值**：  3。 

        :return: The keep_days of this SetDdlLogPolicyRequestBody.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this SetDdlLogPolicyRequestBody.

        **参数解释**：  设置DDL日志保留天数。  **约束限制**：  不涉及。  **取值范围**：  1~30。  **默认取值**：  3。 

        :param keep_days: The keep_days of this SetDdlLogPolicyRequestBody.
        :type keep_days: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, SetDdlLogPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
