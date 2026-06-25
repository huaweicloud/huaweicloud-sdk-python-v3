# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedAction:

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
        'last_accessed': 'datetime',
        'role_sources': 'list[str]',
        'identity_policy_sources': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'last_accessed': 'last_accessed',
        'role_sources': 'role_sources',
        'identity_policy_sources': 'identity_policy_sources'
    }

    def __init__(self, action=None, last_accessed=None, role_sources=None, identity_policy_sources=None):
        r"""UnusedAction

        The model defined in huaweicloud sdk

        :param action: 授权项名称。
        :type action: str
        :param last_accessed: 用户使用授权项的最后访问时间。
        :type last_accessed: datetime
        :param role_sources: 通过该操作访问的角色来源列表。
        :type role_sources: list[str]
        :param identity_policy_sources: 通过该操作访问的身份策略来源列表。
        :type identity_policy_sources: list[str]
        """
        
        

        self._action = None
        self._last_accessed = None
        self._role_sources = None
        self._identity_policy_sources = None
        self.discriminator = None

        self.action = action
        if last_accessed is not None:
            self.last_accessed = last_accessed
        if role_sources is not None:
            self.role_sources = role_sources
        if identity_policy_sources is not None:
            self.identity_policy_sources = identity_policy_sources

    @property
    def action(self):
        r"""Gets the action of this UnusedAction.

        授权项名称。

        :return: The action of this UnusedAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UnusedAction.

        授权项名称。

        :param action: The action of this UnusedAction.
        :type action: str
        """
        self._action = action

    @property
    def last_accessed(self):
        r"""Gets the last_accessed of this UnusedAction.

        用户使用授权项的最后访问时间。

        :return: The last_accessed of this UnusedAction.
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        r"""Sets the last_accessed of this UnusedAction.

        用户使用授权项的最后访问时间。

        :param last_accessed: The last_accessed of this UnusedAction.
        :type last_accessed: datetime
        """
        self._last_accessed = last_accessed

    @property
    def role_sources(self):
        r"""Gets the role_sources of this UnusedAction.

        通过该操作访问的角色来源列表。

        :return: The role_sources of this UnusedAction.
        :rtype: list[str]
        """
        return self._role_sources

    @role_sources.setter
    def role_sources(self, role_sources):
        r"""Sets the role_sources of this UnusedAction.

        通过该操作访问的角色来源列表。

        :param role_sources: The role_sources of this UnusedAction.
        :type role_sources: list[str]
        """
        self._role_sources = role_sources

    @property
    def identity_policy_sources(self):
        r"""Gets the identity_policy_sources of this UnusedAction.

        通过该操作访问的身份策略来源列表。

        :return: The identity_policy_sources of this UnusedAction.
        :rtype: list[str]
        """
        return self._identity_policy_sources

    @identity_policy_sources.setter
    def identity_policy_sources(self, identity_policy_sources):
        r"""Sets the identity_policy_sources of this UnusedAction.

        通过该操作访问的身份策略来源列表。

        :param identity_policy_sources: The identity_policy_sources of this UnusedAction.
        :type identity_policy_sources: list[str]
        """
        self._identity_policy_sources = identity_policy_sources

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
        if not isinstance(other, UnusedAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
