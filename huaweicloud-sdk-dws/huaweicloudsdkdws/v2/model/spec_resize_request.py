# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecResizeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_flavor_id': 'str',
        'force_backup': 'bool',
        'change_mode': 'str'
    }

    attribute_map = {
        'target_flavor_id': 'target_flavor_id',
        'force_backup': 'force_backup',
        'change_mode': 'change_mode'
    }

    def __init__(self, target_flavor_id=None, force_backup=None, change_mode=None):
        r"""SpecResizeRequest

        The model defined in huaweicloud sdk

        :param target_flavor_id: **参数解释**： 目标规格ID。 **取值范围**： 不涉及。
        :type target_flavor_id: str
        :param force_backup: **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。
        :type force_backup: bool
        :param change_mode: **参数解释**： 规格变更模式。 **约束限制**： 不涉及。 **取值范围**： online：在线模式； offline：离线模式； **默认取值**： offline
        :type change_mode: str
        """
        
        

        self._target_flavor_id = None
        self._force_backup = None
        self._change_mode = None
        self.discriminator = None

        self.target_flavor_id = target_flavor_id
        if force_backup is not None:
            self.force_backup = force_backup
        if change_mode is not None:
            self.change_mode = change_mode

    @property
    def target_flavor_id(self):
        r"""Gets the target_flavor_id of this SpecResizeRequest.

        **参数解释**： 目标规格ID。 **取值范围**： 不涉及。

        :return: The target_flavor_id of this SpecResizeRequest.
        :rtype: str
        """
        return self._target_flavor_id

    @target_flavor_id.setter
    def target_flavor_id(self, target_flavor_id):
        r"""Sets the target_flavor_id of this SpecResizeRequest.

        **参数解释**： 目标规格ID。 **取值范围**： 不涉及。

        :param target_flavor_id: The target_flavor_id of this SpecResizeRequest.
        :type target_flavor_id: str
        """
        self._target_flavor_id = target_flavor_id

    @property
    def force_backup(self):
        r"""Gets the force_backup of this SpecResizeRequest.

        **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。

        :return: The force_backup of this SpecResizeRequest.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        r"""Sets the force_backup of this SpecResizeRequest.

        **参数解释**： 强制备份。字段已废弃，不再生效。 **取值范围**： 不涉及。

        :param force_backup: The force_backup of this SpecResizeRequest.
        :type force_backup: bool
        """
        self._force_backup = force_backup

    @property
    def change_mode(self):
        r"""Gets the change_mode of this SpecResizeRequest.

        **参数解释**： 规格变更模式。 **约束限制**： 不涉及。 **取值范围**： online：在线模式； offline：离线模式； **默认取值**： offline

        :return: The change_mode of this SpecResizeRequest.
        :rtype: str
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        r"""Sets the change_mode of this SpecResizeRequest.

        **参数解释**： 规格变更模式。 **约束限制**： 不涉及。 **取值范围**： online：在线模式； offline：离线模式； **默认取值**： offline

        :param change_mode: The change_mode of this SpecResizeRequest.
        :type change_mode: str
        """
        self._change_mode = change_mode

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
        if not isinstance(other, SpecResizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
