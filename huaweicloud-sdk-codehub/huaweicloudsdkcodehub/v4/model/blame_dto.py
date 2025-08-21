# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlameDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit': 'RepositoryCommitDto',
        'avatar_url': 'str',
        'lines': 'list[LineContentDto]',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'avatar_url': 'avatar_url',
        'lines': 'lines',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name'
    }

    def __init__(self, commit=None, avatar_url=None, lines=None, nick_name=None, tenant_name=None, user_name=None):
        r"""BlameDto

        The model defined in huaweicloud sdk

        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        :param avatar_url: **参数解释：** 头像链接 **取值范围：** 不涉及。
        :type avatar_url: str
        :param lines: 行信息
        :type lines: list[:class:`huaweicloudsdkcodehub.v4.LineContentDto`]
        :param nick_name: **参数解释：** 昵称 **取值范围：** 不涉及。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名称。 **取值范围：** 不涉及。
        :type tenant_name: str
        :param user_name: **参数解释：** 用户名。 **取值范围：** 不涉及。
        :type user_name: str
        """
        
        

        self._commit = None
        self._avatar_url = None
        self._lines = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if lines is not None:
            self.lines = lines
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def commit(self):
        r"""Gets the commit of this BlameDto.

        :return: The commit of this BlameDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this BlameDto.

        :param commit: The commit of this BlameDto.
        :type commit: :class:`huaweicloudsdkcodehub.v4.RepositoryCommitDto`
        """
        self._commit = commit

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this BlameDto.

        **参数解释：** 头像链接 **取值范围：** 不涉及。

        :return: The avatar_url of this BlameDto.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this BlameDto.

        **参数解释：** 头像链接 **取值范围：** 不涉及。

        :param avatar_url: The avatar_url of this BlameDto.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def lines(self):
        r"""Gets the lines of this BlameDto.

        行信息

        :return: The lines of this BlameDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.LineContentDto`]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this BlameDto.

        行信息

        :param lines: The lines of this BlameDto.
        :type lines: list[:class:`huaweicloudsdkcodehub.v4.LineContentDto`]
        """
        self._lines = lines

    @property
    def nick_name(self):
        r"""Gets the nick_name of this BlameDto.

        **参数解释：** 昵称 **取值范围：** 不涉及。

        :return: The nick_name of this BlameDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this BlameDto.

        **参数解释：** 昵称 **取值范围：** 不涉及。

        :param nick_name: The nick_name of this BlameDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this BlameDto.

        **参数解释：** 租户名称。 **取值范围：** 不涉及。

        :return: The tenant_name of this BlameDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this BlameDto.

        **参数解释：** 租户名称。 **取值范围：** 不涉及。

        :param tenant_name: The tenant_name of this BlameDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this BlameDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :return: The user_name of this BlameDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this BlameDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :param user_name: The user_name of this BlameDto.
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
        if not isinstance(other, BlameDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
