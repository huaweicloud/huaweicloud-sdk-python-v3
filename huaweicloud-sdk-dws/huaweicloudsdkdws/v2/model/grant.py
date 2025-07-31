# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Grant:

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
        'grant_with': 'bool'
    }

    attribute_map = {
        'permission': 'permission',
        'grant_with': 'grant_with'
    }

    def __init__(self, permission=None, grant_with=None):
        r"""Grant

        The model defined in huaweicloud sdk

        :param permission: **参数解释**： 权限名称，根据不同数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）
        :type permission: str
        :param grant_with: **参数解释**： 是否包含授权选项。 **取值范围**： 不涉及。
        :type grant_with: bool
        """
        
        

        self._permission = None
        self._grant_with = None
        self.discriminator = None

        self.permission = permission
        self.grant_with = grant_with

    @property
    def permission(self):
        r"""Gets the permission of this Grant.

        **参数解释**： 权限名称，根据不同数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）

        :return: The permission of this Grant.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this Grant.

        **参数解释**： 权限名称，根据不同数据库对象类型，拥有权限不同。 **取值范围**： - database：CREATE | CONNECT | TEMPORARY | TEMP  ALL  PRIVILEGES - schema：CREATE | USAGE | ALTER | DROP  ALL  PRIVILEGES - table：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - view：SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER | ANALYZE | ANALYSE | VACUUM | ALTER | DROP  ALL  PRIVILEGES - column：SELECT | INSERT | UPDATE | REFERENCES  ALL  PRIVILEGES - function：EXECUTE  ALL  PRIVILEGES - sequence：SELECT | UPDATE | USAGE  ALL  PRIVILEGES - nodegroup：CREATE | USAGE | COMPUTE  ALL  PRIVILEGES - role：role_name（角色名称）

        :param permission: The permission of this Grant.
        :type permission: str
        """
        self._permission = permission

    @property
    def grant_with(self):
        r"""Gets the grant_with of this Grant.

        **参数解释**： 是否包含授权选项。 **取值范围**： 不涉及。

        :return: The grant_with of this Grant.
        :rtype: bool
        """
        return self._grant_with

    @grant_with.setter
    def grant_with(self, grant_with):
        r"""Sets the grant_with of this Grant.

        **参数解释**： 是否包含授权选项。 **取值范围**： 不涉及。

        :param grant_with: The grant_with of this Grant.
        :type grant_with: bool
        """
        self._grant_with = grant_with

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
        if not isinstance(other, Grant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
