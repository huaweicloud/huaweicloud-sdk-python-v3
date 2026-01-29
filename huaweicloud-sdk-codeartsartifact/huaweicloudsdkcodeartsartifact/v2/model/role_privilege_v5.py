# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RolePrivilegeV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'privileges': 'list[PrivilegeParam]'
    }

    attribute_map = {
        'privileges': 'privileges'
    }

    def __init__(self, privileges=None):
        r"""RolePrivilegeV5

        The model defined in huaweicloud sdk

        :param privileges: **参数解释**: 权限信息。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type privileges: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeParam`]
        """
        
        

        self._privileges = None
        self.discriminator = None

        self.privileges = privileges

    @property
    def privileges(self):
        r"""Gets the privileges of this RolePrivilegeV5.

        **参数解释**: 权限信息。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The privileges of this RolePrivilegeV5.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeParam`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        r"""Sets the privileges of this RolePrivilegeV5.

        **参数解释**: 权限信息。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param privileges: The privileges of this RolePrivilegeV5.
        :type privileges: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeParam`]
        """
        self._privileges = privileges

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
        if not isinstance(other, RolePrivilegeV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
