# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachSubNetworkInterfaceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'str',
        'security_groups': 'list[str]',
        'security_enabled': 'bool'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'security_groups': 'security_groups',
        'security_enabled': 'security_enabled'
    }

    def __init__(self, parent_id=None, security_groups=None, security_enabled=None):
        r"""AttachSubNetworkInterfaceOption

        The model defined in huaweicloud sdk

        :param parent_id: **参数解释**： 辅助弹性网卡所挂载的弹性网卡的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type parent_id: str
        :param security_groups: **参数解释**： 辅助弹性网卡关联的安全组的ID列表。例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;]。 **取值范围**： 如果请求时不指定此参数，辅助弹性网卡创建后会自动关联默认安全组。
        :type security_groups: list[str]
        :param security_enabled: **参数解释**： 辅助弹性网卡安全使能标记，如果不使能则安全组不生效。 **取值范围**： 不涉及。
        :type security_enabled: bool
        """
        
        

        self._parent_id = None
        self._security_groups = None
        self._security_enabled = None
        self.discriminator = None

        self.parent_id = parent_id
        if security_groups is not None:
            self.security_groups = security_groups
        if security_enabled is not None:
            self.security_enabled = security_enabled

    @property
    def parent_id(self):
        r"""Gets the parent_id of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡所挂载的弹性网卡的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The parent_id of this AttachSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡所挂载的弹性网卡的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param parent_id: The parent_id of this AttachSubNetworkInterfaceOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡关联的安全组的ID列表。例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]。 **取值范围**： 如果请求时不指定此参数，辅助弹性网卡创建后会自动关联默认安全组。

        :return: The security_groups of this AttachSubNetworkInterfaceOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡关联的安全组的ID列表。例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"]。 **取值范围**： 如果请求时不指定此参数，辅助弹性网卡创建后会自动关联默认安全组。

        :param security_groups: The security_groups of this AttachSubNetworkInterfaceOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def security_enabled(self):
        r"""Gets the security_enabled of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡安全使能标记，如果不使能则安全组不生效。 **取值范围**： 不涉及。

        :return: The security_enabled of this AttachSubNetworkInterfaceOption.
        :rtype: bool
        """
        return self._security_enabled

    @security_enabled.setter
    def security_enabled(self, security_enabled):
        r"""Sets the security_enabled of this AttachSubNetworkInterfaceOption.

        **参数解释**： 辅助弹性网卡安全使能标记，如果不使能则安全组不生效。 **取值范围**： 不涉及。

        :param security_enabled: The security_enabled of this AttachSubNetworkInterfaceOption.
        :type security_enabled: bool
        """
        self._security_enabled = security_enabled

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
        if not isinstance(other, AttachSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
