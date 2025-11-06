# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicableInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_id': 'str',
        'entity_name': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_name': 'entity_name'
    }

    def __init__(self, entity_id=None, entity_name=None):
        r"""ApplicableInstanceInfo

        The model defined in huaweicloud sdk

        :param entity_id: **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type entity_id: str
        :param entity_name: **参数解释**：  实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type entity_name: str
        """
        
        

        self._entity_id = None
        self._entity_name = None
        self.discriminator = None

        self.entity_id = entity_id
        self.entity_name = entity_name

    @property
    def entity_id(self):
        r"""Gets the entity_id of this ApplicableInstanceInfo.

        **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The entity_id of this ApplicableInstanceInfo.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this ApplicableInstanceInfo.

        **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param entity_id: The entity_id of this ApplicableInstanceInfo.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def entity_name(self):
        r"""Gets the entity_name of this ApplicableInstanceInfo.

        **参数解释**：  实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The entity_name of this ApplicableInstanceInfo.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        r"""Sets the entity_name of this ApplicableInstanceInfo.

        **参数解释**：  实例名称  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param entity_name: The entity_name of this ApplicableInstanceInfo.
        :type entity_name: str
        """
        self._entity_name = entity_name

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
        if not isinstance(other, ApplicableInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
