# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryProtectedActionBasicBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'user_ids': 'list[object]',
        'user_team_ids': 'list[int]',
        'related_role_ids': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'user_ids': 'user_ids',
        'user_team_ids': 'user_team_ids',
        'related_role_ids': 'related_role_ids'
    }

    def __init__(self, enable=None, user_ids=None, user_team_ids=None, related_role_ids=None):
        r"""RepositoryProtectedActionBasicBodyDto

        The model defined in huaweicloud sdk

        :param enable: **参数解释：** 是否启用。 **约束限制：** 不涉及。 **取值范围：** - true，开启规则限制 - false，关闭规则限制 **默认取值：** 不涉及。
        :type enable: bool
        :param user_ids: **参数解释：** 用户ID列表。 **约束限制：** 不涉及。 **取值范围：** Integer **默认取值：** 不涉及。
        :type user_ids: list[object]
        :param user_team_ids: **参数解释：** 成员组ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type user_team_ids: list[int]
        :param related_role_ids: **参数解释：** 关联角色ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type related_role_ids: list[str]
        """
        
        

        self._enable = None
        self._user_ids = None
        self._user_team_ids = None
        self._related_role_ids = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if user_ids is not None:
            self.user_ids = user_ids
        if user_team_ids is not None:
            self.user_team_ids = user_team_ids
        if related_role_ids is not None:
            self.related_role_ids = related_role_ids

    @property
    def enable(self):
        r"""Gets the enable of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 是否启用。 **约束限制：** 不涉及。 **取值范围：** - true，开启规则限制 - false，关闭规则限制 **默认取值：** 不涉及。

        :return: The enable of this RepositoryProtectedActionBasicBodyDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 是否启用。 **约束限制：** 不涉及。 **取值范围：** - true，开启规则限制 - false，关闭规则限制 **默认取值：** 不涉及。

        :param enable: The enable of this RepositoryProtectedActionBasicBodyDto.
        :type enable: bool
        """
        self._enable = enable

    @property
    def user_ids(self):
        r"""Gets the user_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 用户ID列表。 **约束限制：** 不涉及。 **取值范围：** Integer **默认取值：** 不涉及。

        :return: The user_ids of this RepositoryProtectedActionBasicBodyDto.
        :rtype: list[object]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        r"""Sets the user_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 用户ID列表。 **约束限制：** 不涉及。 **取值范围：** Integer **默认取值：** 不涉及。

        :param user_ids: The user_ids of this RepositoryProtectedActionBasicBodyDto.
        :type user_ids: list[object]
        """
        self._user_ids = user_ids

    @property
    def user_team_ids(self):
        r"""Gets the user_team_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 成员组ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The user_team_ids of this RepositoryProtectedActionBasicBodyDto.
        :rtype: list[int]
        """
        return self._user_team_ids

    @user_team_ids.setter
    def user_team_ids(self, user_team_ids):
        r"""Sets the user_team_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 成员组ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param user_team_ids: The user_team_ids of this RepositoryProtectedActionBasicBodyDto.
        :type user_team_ids: list[int]
        """
        self._user_team_ids = user_team_ids

    @property
    def related_role_ids(self):
        r"""Gets the related_role_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 关联角色ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The related_role_ids of this RepositoryProtectedActionBasicBodyDto.
        :rtype: list[str]
        """
        return self._related_role_ids

    @related_role_ids.setter
    def related_role_ids(self, related_role_ids):
        r"""Sets the related_role_ids of this RepositoryProtectedActionBasicBodyDto.

        **参数解释：** 关联角色ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param related_role_ids: The related_role_ids of this RepositoryProtectedActionBasicBodyDto.
        :type related_role_ids: list[str]
        """
        self._related_role_ids = related_role_ids

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
        if not isinstance(other, RepositoryProtectedActionBasicBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
