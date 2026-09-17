# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleMember:

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
        'desc': 'str',
        'permission': 'bool',
        'grant_with': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'permission': 'permission',
        'grant_with': 'grant_with'
    }

    def __init__(self, name=None, desc=None, permission=None, grant_with=None):
        r"""RoleMember

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 角色名。 **取值范围**： 不涉及。
        :type name: str
        :param desc: **参数解释**： 角色描述。 **取值范围**： 不涉及。
        :type desc: str
        :param permission: **参数解释**： 是否允许授予某个角色特定的权限。 **取值范围**： 不涉及。
        :type permission: bool
        :param grant_with: **参数解释**： 是否允许该角色将已获得的权限再转授给其他角色。 **取值范围**： 不涉及。
        :type grant_with: bool
        """
        
        

        self._name = None
        self._desc = None
        self._permission = None
        self._grant_with = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if permission is not None:
            self.permission = permission
        if grant_with is not None:
            self.grant_with = grant_with

    @property
    def name(self):
        r"""Gets the name of this RoleMember.

        **参数解释**： 角色名。 **取值范围**： 不涉及。

        :return: The name of this RoleMember.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RoleMember.

        **参数解释**： 角色名。 **取值范围**： 不涉及。

        :param name: The name of this RoleMember.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this RoleMember.

        **参数解释**： 角色描述。 **取值范围**： 不涉及。

        :return: The desc of this RoleMember.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this RoleMember.

        **参数解释**： 角色描述。 **取值范围**： 不涉及。

        :param desc: The desc of this RoleMember.
        :type desc: str
        """
        self._desc = desc

    @property
    def permission(self):
        r"""Gets the permission of this RoleMember.

        **参数解释**： 是否允许授予某个角色特定的权限。 **取值范围**： 不涉及。

        :return: The permission of this RoleMember.
        :rtype: bool
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this RoleMember.

        **参数解释**： 是否允许授予某个角色特定的权限。 **取值范围**： 不涉及。

        :param permission: The permission of this RoleMember.
        :type permission: bool
        """
        self._permission = permission

    @property
    def grant_with(self):
        r"""Gets the grant_with of this RoleMember.

        **参数解释**： 是否允许该角色将已获得的权限再转授给其他角色。 **取值范围**： 不涉及。

        :return: The grant_with of this RoleMember.
        :rtype: bool
        """
        return self._grant_with

    @grant_with.setter
    def grant_with(self, grant_with):
        r"""Sets the grant_with of this RoleMember.

        **参数解释**： 是否允许该角色将已获得的权限再转授给其他角色。 **取值范围**： 不涉及。

        :param grant_with: The grant_with of this RoleMember.
        :type grant_with: bool
        """
        self._grant_with = grant_with

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
        if not isinstance(other, RoleMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
