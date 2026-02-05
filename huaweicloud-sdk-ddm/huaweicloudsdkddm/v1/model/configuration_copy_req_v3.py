# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationCopyReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'new_name': 'new_name',
        'description': 'description'
    }

    def __init__(self, new_name=None, description=None):
        r"""ConfigurationCopyReqV3

        The model defined in huaweicloud sdk

        :param new_name: **参数解释**：  新参数组的名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type new_name: str
        :param description: **参数解释**：  描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type description: str
        """
        
        

        self._new_name = None
        self._description = None
        self.discriminator = None

        self.new_name = new_name
        if description is not None:
            self.description = description

    @property
    def new_name(self):
        r"""Gets the new_name of this ConfigurationCopyReqV3.

        **参数解释**：  新参数组的名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The new_name of this ConfigurationCopyReqV3.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        r"""Sets the new_name of this ConfigurationCopyReqV3.

        **参数解释**：  新参数组的名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param new_name: The new_name of this ConfigurationCopyReqV3.
        :type new_name: str
        """
        self._new_name = new_name

    @property
    def description(self):
        r"""Gets the description of this ConfigurationCopyReqV3.

        **参数解释**：  描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The description of this ConfigurationCopyReqV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationCopyReqV3.

        **参数解释**：  描述。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param description: The description of this ConfigurationCopyReqV3.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConfigurationCopyReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
