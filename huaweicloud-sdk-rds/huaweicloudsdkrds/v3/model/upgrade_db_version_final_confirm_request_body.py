# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDbVersionFinalConfirmRequestBody:

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
        'force_rollback': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'force_rollback': 'force_rollback'
    }

    def __init__(self, action=None, force_rollback=None):
        r"""UpgradeDbVersionFinalConfirmRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释**  要进行的操作。confirm表示确认完成升级，rollback表示要回滚至原始版本  **取值范围**  confirm,rollback  **约束限制**  不涉及  **默认取值**  不涉及
        :type action: str
        :param force_rollback: **参数解释**  回滚时是否强制回滚  **取值范围**  true,false  **约束限制**  不涉及  **默认取值**  false
        :type force_rollback: bool
        """
        
        

        self._action = None
        self._force_rollback = None
        self.discriminator = None

        self.action = action
        if force_rollback is not None:
            self.force_rollback = force_rollback

    @property
    def action(self):
        r"""Gets the action of this UpgradeDbVersionFinalConfirmRequestBody.

        **参数解释**  要进行的操作。confirm表示确认完成升级，rollback表示要回滚至原始版本  **取值范围**  confirm,rollback  **约束限制**  不涉及  **默认取值**  不涉及

        :return: The action of this UpgradeDbVersionFinalConfirmRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpgradeDbVersionFinalConfirmRequestBody.

        **参数解释**  要进行的操作。confirm表示确认完成升级，rollback表示要回滚至原始版本  **取值范围**  confirm,rollback  **约束限制**  不涉及  **默认取值**  不涉及

        :param action: The action of this UpgradeDbVersionFinalConfirmRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def force_rollback(self):
        r"""Gets the force_rollback of this UpgradeDbVersionFinalConfirmRequestBody.

        **参数解释**  回滚时是否强制回滚  **取值范围**  true,false  **约束限制**  不涉及  **默认取值**  false

        :return: The force_rollback of this UpgradeDbVersionFinalConfirmRequestBody.
        :rtype: bool
        """
        return self._force_rollback

    @force_rollback.setter
    def force_rollback(self, force_rollback):
        r"""Sets the force_rollback of this UpgradeDbVersionFinalConfirmRequestBody.

        **参数解释**  回滚时是否强制回滚  **取值范围**  true,false  **约束限制**  不涉及  **默认取值**  false

        :param force_rollback: The force_rollback of this UpgradeDbVersionFinalConfirmRequestBody.
        :type force_rollback: bool
        """
        self._force_rollback = force_rollback

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
        if not isinstance(other, UpgradeDbVersionFinalConfirmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
