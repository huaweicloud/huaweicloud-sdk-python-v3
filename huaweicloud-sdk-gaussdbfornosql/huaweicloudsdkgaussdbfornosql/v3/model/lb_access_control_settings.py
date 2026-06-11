# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LbAccessControlSettings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'type': 'str',
        'ip_groups': 'list[IpGroupsDetail]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'type': 'type',
        'ip_groups': 'ip_groups'
    }

    def __init__(self, enabled=None, type=None, ip_groups=None):
        r"""LbAccessControlSettings

        The model defined in huaweicloud sdk

        :param enabled: **参数解释：** 是否开启负载均衡访问控制。 **约束限制：** 不涉及。 **取值范围：**  -true。  -false。 **默认取值：** 不涉及。
        :type enabled: bool
        :param type: **参数解释：** 黑白名单类型。 **约束限制：** 仅支持设置黑名单或白名单中的一种，当配置切换时，原配置会失效。 **取值范围：**  -blackList黑名单  -whiteList白名单。 **默认取值：** 不涉及。
        :type type: str
        :param ip_groups: **参数解释：** IP地址组中包含的IP或网段列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.IpGroupsDetail`]
        """
        
        

        self._enabled = None
        self._type = None
        self._ip_groups = None
        self.discriminator = None

        self.enabled = enabled
        self.type = type
        self.ip_groups = ip_groups

    @property
    def enabled(self):
        r"""Gets the enabled of this LbAccessControlSettings.

        **参数解释：** 是否开启负载均衡访问控制。 **约束限制：** 不涉及。 **取值范围：**  -true。  -false。 **默认取值：** 不涉及。

        :return: The enabled of this LbAccessControlSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this LbAccessControlSettings.

        **参数解释：** 是否开启负载均衡访问控制。 **约束限制：** 不涉及。 **取值范围：**  -true。  -false。 **默认取值：** 不涉及。

        :param enabled: The enabled of this LbAccessControlSettings.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def type(self):
        r"""Gets the type of this LbAccessControlSettings.

        **参数解释：** 黑白名单类型。 **约束限制：** 仅支持设置黑名单或白名单中的一种，当配置切换时，原配置会失效。 **取值范围：**  -blackList黑名单  -whiteList白名单。 **默认取值：** 不涉及。

        :return: The type of this LbAccessControlSettings.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LbAccessControlSettings.

        **参数解释：** 黑白名单类型。 **约束限制：** 仅支持设置黑名单或白名单中的一种，当配置切换时，原配置会失效。 **取值范围：**  -blackList黑名单  -whiteList白名单。 **默认取值：** 不涉及。

        :param type: The type of this LbAccessControlSettings.
        :type type: str
        """
        self._type = type

    @property
    def ip_groups(self):
        r"""Gets the ip_groups of this LbAccessControlSettings.

        **参数解释：** IP地址组中包含的IP或网段列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The ip_groups of this LbAccessControlSettings.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.IpGroupsDetail`]
        """
        return self._ip_groups

    @ip_groups.setter
    def ip_groups(self, ip_groups):
        r"""Sets the ip_groups of this LbAccessControlSettings.

        **参数解释：** IP地址组中包含的IP或网段列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param ip_groups: The ip_groups of this LbAccessControlSettings.
        :type ip_groups: list[:class:`huaweicloudsdkgaussdbfornosql.v3.IpGroupsDetail`]
        """
        self._ip_groups = ip_groups

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
        if not isinstance(other, LbAccessControlSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
