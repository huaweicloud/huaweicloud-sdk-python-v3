# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContributorDto:

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
        'email': 'str',
        'commits': 'int',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'commits': 'commits',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name'
    }

    def __init__(self, name=None, email=None, commits=None, nick_name=None, tenant_name=None, user_name=None):
        r"""ContributorDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param email: **参数解释：** 邮箱。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type email: str
        :param commits: **参数解释：** 提交数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type commits: int
        :param nick_name: **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tenant_name: str
        :param user_name: **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type user_name: str
        """
        
        

        self._name = None
        self._email = None
        self._commits = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if commits is not None:
            self.commits = commits
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this ContributorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this ContributorDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ContributorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this ContributorDto.
        :type name: str
        """
        self._name = name

    @property
    def email(self):
        r"""Gets the email of this ContributorDto.

        **参数解释：** 邮箱。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The email of this ContributorDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ContributorDto.

        **参数解释：** 邮箱。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param email: The email of this ContributorDto.
        :type email: str
        """
        self._email = email

    @property
    def commits(self):
        r"""Gets the commits of this ContributorDto.

        **参数解释：** 提交数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The commits of this ContributorDto.
        :rtype: int
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        r"""Sets the commits of this ContributorDto.

        **参数解释：** 提交数量。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param commits: The commits of this ContributorDto.
        :type commits: int
        """
        self._commits = commits

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ContributorDto.

        **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The nick_name of this ContributorDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ContributorDto.

        **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param nick_name: The nick_name of this ContributorDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ContributorDto.

        **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tenant_name of this ContributorDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ContributorDto.

        **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tenant_name: The tenant_name of this ContributorDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ContributorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The user_name of this ContributorDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ContributorDto.

        **参数解释：** 用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param user_name: The user_name of this ContributorDto.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ContributorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
