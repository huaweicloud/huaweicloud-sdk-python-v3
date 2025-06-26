# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleAuthority:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'right_list': 'list[str]'
    }

    attribute_map = {
        'role': 'role',
        'right_list': 'right_list'
    }

    def __init__(self, role=None, right_list=None):
        r"""RoleAuthority

        The model defined in huaweicloud sdk

        :param role: **参数解释**： 角色名称。 **取值范围**： 不涉及。
        :type role: str
        :param right_list: **参数解释**： 权限列表。 **取值范围**： 不涉及。
        :type right_list: list[str]
        """
        
        

        self._role = None
        self._right_list = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if right_list is not None:
            self.right_list = right_list

    @property
    def role(self):
        r"""Gets the role of this RoleAuthority.

        **参数解释**： 角色名称。 **取值范围**： 不涉及。

        :return: The role of this RoleAuthority.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this RoleAuthority.

        **参数解释**： 角色名称。 **取值范围**： 不涉及。

        :param role: The role of this RoleAuthority.
        :type role: str
        """
        self._role = role

    @property
    def right_list(self):
        r"""Gets the right_list of this RoleAuthority.

        **参数解释**： 权限列表。 **取值范围**： 不涉及。

        :return: The right_list of this RoleAuthority.
        :rtype: list[str]
        """
        return self._right_list

    @right_list.setter
    def right_list(self, right_list):
        r"""Sets the right_list of this RoleAuthority.

        **参数解释**： 权限列表。 **取值范围**： 不涉及。

        :param right_list: The right_list of this RoleAuthority.
        :type right_list: list[str]
        """
        self._right_list = right_list

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
        if not isinstance(other, RoleAuthority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
