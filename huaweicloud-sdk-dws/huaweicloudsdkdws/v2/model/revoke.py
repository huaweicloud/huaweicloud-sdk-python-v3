# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Revoke:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission': 'str',
        'revoke_with': 'bool'
    }

    attribute_map = {
        'permission': 'permission',
        'revoke_with': 'revoke_with'
    }

    def __init__(self, permission=None, revoke_with=None):
        r"""Revoke

        The model defined in huaweicloud sdk

        :param permission: **参数解释**： 权限名称，根据不通数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）
        :type permission: str
        :param revoke_with: **参数解释**： 是否仅移除授权选项。 **取值范围**： 不涉及。
        :type revoke_with: bool
        """
        
        

        self._permission = None
        self._revoke_with = None
        self.discriminator = None

        self.permission = permission
        self.revoke_with = revoke_with

    @property
    def permission(self):
        r"""Gets the permission of this Revoke.

        **参数解释**： 权限名称，根据不通数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）

        :return: The permission of this Revoke.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this Revoke.

        **参数解释**： 权限名称，根据不通数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）

        :param permission: The permission of this Revoke.
        :type permission: str
        """
        self._permission = permission

    @property
    def revoke_with(self):
        r"""Gets the revoke_with of this Revoke.

        **参数解释**： 是否仅移除授权选项。 **取值范围**： 不涉及。

        :return: The revoke_with of this Revoke.
        :rtype: bool
        """
        return self._revoke_with

    @revoke_with.setter
    def revoke_with(self, revoke_with):
        r"""Sets the revoke_with of this Revoke.

        **参数解释**： 是否仅移除授权选项。 **取值范围**： 不涉及。

        :param revoke_with: The revoke_with of this Revoke.
        :type revoke_with: bool
        """
        self._revoke_with = revoke_with

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
        if not isinstance(other, Revoke):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
