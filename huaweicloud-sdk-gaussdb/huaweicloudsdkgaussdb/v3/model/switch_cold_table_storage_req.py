# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchColdTableStorageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tables': 'list[TableTarget]'
    }

    attribute_map = {
        'action': 'action',
        'tables': 'tables'
    }

    def __init__(self, action=None, tables=None):
        r"""SwitchColdTableStorageReq

        The model defined in huaweicloud sdk

        :param action: **参数解释**：  操作类型。  **约束限制**：  不涉及。  **取值范围**：  - archive：创建冷表。 - unarchive：回迁冷表。  **默认取值**：  不涉及。
        :type action: str
        :param tables: **参数解释**：  需要操作的表信息。  **约束限制**：  数组长度小于等于50。
        :type tables: list[:class:`huaweicloudsdkgaussdb.v3.TableTarget`]
        """
        
        

        self._action = None
        self._tables = None
        self.discriminator = None

        self.action = action
        self.tables = tables

    @property
    def action(self):
        r"""Gets the action of this SwitchColdTableStorageReq.

        **参数解释**：  操作类型。  **约束限制**：  不涉及。  **取值范围**：  - archive：创建冷表。 - unarchive：回迁冷表。  **默认取值**：  不涉及。

        :return: The action of this SwitchColdTableStorageReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SwitchColdTableStorageReq.

        **参数解释**：  操作类型。  **约束限制**：  不涉及。  **取值范围**：  - archive：创建冷表。 - unarchive：回迁冷表。  **默认取值**：  不涉及。

        :param action: The action of this SwitchColdTableStorageReq.
        :type action: str
        """
        self._action = action

    @property
    def tables(self):
        r"""Gets the tables of this SwitchColdTableStorageReq.

        **参数解释**：  需要操作的表信息。  **约束限制**：  数组长度小于等于50。

        :return: The tables of this SwitchColdTableStorageReq.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TableTarget`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this SwitchColdTableStorageReq.

        **参数解释**：  需要操作的表信息。  **约束限制**：  数组长度小于等于50。

        :param tables: The tables of this SwitchColdTableStorageReq.
        :type tables: list[:class:`huaweicloudsdkgaussdb.v3.TableTarget`]
        """
        self._tables = tables

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
        if not isinstance(other, SwitchColdTableStorageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
