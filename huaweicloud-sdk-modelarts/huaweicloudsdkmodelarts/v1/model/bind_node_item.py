# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindNodeItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'quota_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'quota_name': 'quotaName'
    }

    def __init__(self, name=None, quota_name=None):
        r"""BindNodeItem

        The model defined in huaweicloud sdk

        :param name: **参数解释**：换绑的节点的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param quota_name: **参数解释**：节点绑定的逻辑子池的ID。值为空则节点不绑定任何逻辑子池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type quota_name: str
        """
        
        

        self._name = None
        self._quota_name = None
        self.discriminator = None

        self.name = name
        if quota_name is not None:
            self.quota_name = quota_name

    @property
    def name(self):
        r"""Gets the name of this BindNodeItem.

        **参数解释**：换绑的节点的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this BindNodeItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BindNodeItem.

        **参数解释**：换绑的节点的名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this BindNodeItem.
        :type name: str
        """
        self._name = name

    @property
    def quota_name(self):
        r"""Gets the quota_name of this BindNodeItem.

        **参数解释**：节点绑定的逻辑子池的ID。值为空则节点不绑定任何逻辑子池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The quota_name of this BindNodeItem.
        :rtype: str
        """
        return self._quota_name

    @quota_name.setter
    def quota_name(self, quota_name):
        r"""Sets the quota_name of this BindNodeItem.

        **参数解释**：节点绑定的逻辑子池的ID。值为空则节点不绑定任何逻辑子池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param quota_name: The quota_name of this BindNodeItem.
        :type quota_name: str
        """
        self._quota_name = quota_name

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
        if not isinstance(other, BindNodeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
