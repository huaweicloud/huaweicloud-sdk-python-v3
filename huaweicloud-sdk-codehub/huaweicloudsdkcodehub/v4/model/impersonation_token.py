# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImpersonationToken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'revoked': 'bool',
        'created_at': 'str',
        'scopes': 'list[str]',
        'active': 'bool',
        'expires_at': 'str',
        'impersonation': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revoked': 'revoked',
        'created_at': 'created_at',
        'scopes': 'scopes',
        'active': 'active',
        'expires_at': 'expires_at',
        'impersonation': 'impersonation',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, revoked=None, created_at=None, scopes=None, active=None, expires_at=None, impersonation=None, description=None):
        r"""ImpersonationToken

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标示id。
        :type id: int
        :param name: **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param revoked: **参数解释：** 是否撤销。
        :type revoked: bool
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param scopes: **参数解释：** scope权限。 **取值范围：** 字符串长度不少于0，不超过1000。
        :type scopes: list[str]
        :param active: **参数解释：** 是否可用。
        :type active: bool
        :param expires_at: **参数解释：** 过期时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type expires_at: str
        :param impersonation: **参数解释：** 是否为个人token。
        :type impersonation: bool
        :param description: **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._revoked = None
        self._created_at = None
        self._scopes = None
        self._active = None
        self._expires_at = None
        self._impersonation = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if revoked is not None:
            self.revoked = revoked
        if created_at is not None:
            self.created_at = created_at
        if scopes is not None:
            self.scopes = scopes
        if active is not None:
            self.active = active
        if expires_at is not None:
            self.expires_at = expires_at
        if impersonation is not None:
            self.impersonation = impersonation
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ImpersonationToken.

        **参数解释：** 唯一标示id。

        :return: The id of this ImpersonationToken.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImpersonationToken.

        **参数解释：** 唯一标示id。

        :param id: The id of this ImpersonationToken.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ImpersonationToken.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this ImpersonationToken.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImpersonationToken.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this ImpersonationToken.
        :type name: str
        """
        self._name = name

    @property
    def revoked(self):
        r"""Gets the revoked of this ImpersonationToken.

        **参数解释：** 是否撤销。

        :return: The revoked of this ImpersonationToken.
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        r"""Sets the revoked of this ImpersonationToken.

        **参数解释：** 是否撤销。

        :param revoked: The revoked of this ImpersonationToken.
        :type revoked: bool
        """
        self._revoked = revoked

    @property
    def created_at(self):
        r"""Gets the created_at of this ImpersonationToken.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this ImpersonationToken.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ImpersonationToken.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this ImpersonationToken.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def scopes(self):
        r"""Gets the scopes of this ImpersonationToken.

        **参数解释：** scope权限。 **取值范围：** 字符串长度不少于0，不超过1000。

        :return: The scopes of this ImpersonationToken.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this ImpersonationToken.

        **参数解释：** scope权限。 **取值范围：** 字符串长度不少于0，不超过1000。

        :param scopes: The scopes of this ImpersonationToken.
        :type scopes: list[str]
        """
        self._scopes = scopes

    @property
    def active(self):
        r"""Gets the active of this ImpersonationToken.

        **参数解释：** 是否可用。

        :return: The active of this ImpersonationToken.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this ImpersonationToken.

        **参数解释：** 是否可用。

        :param active: The active of this ImpersonationToken.
        :type active: bool
        """
        self._active = active

    @property
    def expires_at(self):
        r"""Gets the expires_at of this ImpersonationToken.

        **参数解释：** 过期时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The expires_at of this ImpersonationToken.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this ImpersonationToken.

        **参数解释：** 过期时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param expires_at: The expires_at of this ImpersonationToken.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def impersonation(self):
        r"""Gets the impersonation of this ImpersonationToken.

        **参数解释：** 是否为个人token。

        :return: The impersonation of this ImpersonationToken.
        :rtype: bool
        """
        return self._impersonation

    @impersonation.setter
    def impersonation(self, impersonation):
        r"""Sets the impersonation of this ImpersonationToken.

        **参数解释：** 是否为个人token。

        :param impersonation: The impersonation of this ImpersonationToken.
        :type impersonation: bool
        """
        self._impersonation = impersonation

    @property
    def description(self):
        r"""Gets the description of this ImpersonationToken.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The description of this ImpersonationToken.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImpersonationToken.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param description: The description of this ImpersonationToken.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImpersonationToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
