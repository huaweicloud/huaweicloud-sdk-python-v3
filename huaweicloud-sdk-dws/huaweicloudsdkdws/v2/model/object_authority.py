# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectAuthority:

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
        'role_authority': 'list[RoleAuthority]'
    }

    attribute_map = {
        'name': 'name',
        'role_authority': 'role_authority'
    }

    def __init__(self, name=None, role_authority=None):
        r"""ObjectAuthority

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 对象名称。 **取值范围**： 不涉及。
        :type name: str
        :param role_authority: **参数解释**： 角色权限集合。 **取值范围**： 不涉及。
        :type role_authority: list[:class:`huaweicloudsdkdws.v2.RoleAuthority`]
        """
        
        

        self._name = None
        self._role_authority = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if role_authority is not None:
            self.role_authority = role_authority

    @property
    def name(self):
        r"""Gets the name of this ObjectAuthority.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :return: The name of this ObjectAuthority.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectAuthority.

        **参数解释**： 对象名称。 **取值范围**： 不涉及。

        :param name: The name of this ObjectAuthority.
        :type name: str
        """
        self._name = name

    @property
    def role_authority(self):
        r"""Gets the role_authority of this ObjectAuthority.

        **参数解释**： 角色权限集合。 **取值范围**： 不涉及。

        :return: The role_authority of this ObjectAuthority.
        :rtype: list[:class:`huaweicloudsdkdws.v2.RoleAuthority`]
        """
        return self._role_authority

    @role_authority.setter
    def role_authority(self, role_authority):
        r"""Sets the role_authority of this ObjectAuthority.

        **参数解释**： 角色权限集合。 **取值范围**： 不涉及。

        :param role_authority: The role_authority of this ObjectAuthority.
        :type role_authority: list[:class:`huaweicloudsdkdws.v2.RoleAuthority`]
        """
        self._role_authority = role_authority

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObjectAuthority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
