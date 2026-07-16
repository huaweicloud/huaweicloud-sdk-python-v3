# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIntranetConnectionRequestBody:

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
        'reason': 'str'
    }

    attribute_map = {
        'action': 'action',
        'reason': 'reason'
    }

    def __init__(self, action=None, reason=None):
        r"""UpdateIntranetConnectionRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 内网接入申请操作。 **约束限制：** 不涉及。 **取值范围：** - APPROVE：通过申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - REJECT： 拒绝申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - CANCEL： 取消授权，只有当内网接入申请处于“通过”（CONNECTED）状态时，才可进行取消授权操作。 - RETRY：  重试申请，只有当内网接入申请处于“异常”状态并且异常原因为“连接失败，请重试”时，才可进行重试操作。 **默认取值：** 不涉及。
        :type action: str
        :param reason: **参数解释：** 拒绝时可以填入拒绝的原因。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type reason: str
        """
        
        

        self._action = None
        self._reason = None
        self.discriminator = None

        self.action = action
        if reason is not None:
            self.reason = reason

    @property
    def action(self):
        r"""Gets the action of this UpdateIntranetConnectionRequestBody.

        **参数解释：** 内网接入申请操作。 **约束限制：** 不涉及。 **取值范围：** - APPROVE：通过申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - REJECT： 拒绝申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - CANCEL： 取消授权，只有当内网接入申请处于“通过”（CONNECTED）状态时，才可进行取消授权操作。 - RETRY：  重试申请，只有当内网接入申请处于“异常”状态并且异常原因为“连接失败，请重试”时，才可进行重试操作。 **默认取值：** 不涉及。

        :return: The action of this UpdateIntranetConnectionRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateIntranetConnectionRequestBody.

        **参数解释：** 内网接入申请操作。 **约束限制：** 不涉及。 **取值范围：** - APPROVE：通过申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - REJECT： 拒绝申请。只有当内网接入申请处于“审批中”状态时，才可进行此操作。 - CANCEL： 取消授权，只有当内网接入申请处于“通过”（CONNECTED）状态时，才可进行取消授权操作。 - RETRY：  重试申请，只有当内网接入申请处于“异常”状态并且异常原因为“连接失败，请重试”时，才可进行重试操作。 **默认取值：** 不涉及。

        :param action: The action of this UpdateIntranetConnectionRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def reason(self):
        r"""Gets the reason of this UpdateIntranetConnectionRequestBody.

        **参数解释：** 拒绝时可以填入拒绝的原因。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The reason of this UpdateIntranetConnectionRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this UpdateIntranetConnectionRequestBody.

        **参数解释：** 拒绝时可以填入拒绝的原因。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param reason: The reason of this UpdateIntranetConnectionRequestBody.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, UpdateIntranetConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
