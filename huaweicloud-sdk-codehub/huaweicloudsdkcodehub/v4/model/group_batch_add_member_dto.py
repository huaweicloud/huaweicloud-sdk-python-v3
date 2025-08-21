# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupBatchAddMemberDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_id': 'str',
        'user_id': 'str',
        'name': 'str',
        'nick_name': 'str',
        'domain_name': 'str',
        'domain_id': 'str',
        'repo_role_id': 'str',
        'req_role_id': 'str',
        'repo_role_name': 'str',
        'req_role_name': 'str'
    }

    attribute_map = {
        'iam_id': 'iam_id',
        'user_id': 'user_id',
        'name': 'name',
        'nick_name': 'nick_name',
        'domain_name': 'domain_name',
        'domain_id': 'domain_id',
        'repo_role_id': 'repo_role_id',
        'req_role_id': 'req_role_id',
        'repo_role_name': 'repo_role_name',
        'req_role_name': 'req_role_name'
    }

    def __init__(self, iam_id=None, user_id=None, name=None, nick_name=None, domain_name=None, domain_id=None, repo_role_id=None, req_role_id=None, repo_role_name=None, req_role_name=None):
        r"""GroupBatchAddMemberDto

        The model defined in huaweicloud sdk

        :param iam_id: **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type iam_id: str
        :param user_id: **参数解释：** 用户userId。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type user_id: str
        :param name: **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param nick_name: **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type nick_name: str
        :param domain_name: **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type domain_name: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type domain_id: str
        :param repo_role_id: **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type repo_role_id: str
        :param req_role_id: **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type req_role_id: str
        :param repo_role_name: **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type repo_role_name: str
        :param req_role_name: **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type req_role_name: str
        """
        
        

        self._iam_id = None
        self._user_id = None
        self._name = None
        self._nick_name = None
        self._domain_name = None
        self._domain_id = None
        self._repo_role_id = None
        self._req_role_id = None
        self._repo_role_name = None
        self._req_role_name = None
        self.discriminator = None

        if iam_id is not None:
            self.iam_id = iam_id
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_id is not None:
            self.domain_id = domain_id
        if repo_role_id is not None:
            self.repo_role_id = repo_role_id
        if req_role_id is not None:
            self.req_role_id = req_role_id
        if repo_role_name is not None:
            self.repo_role_name = repo_role_name
        if req_role_name is not None:
            self.req_role_name = req_role_name

    @property
    def iam_id(self):
        r"""Gets the iam_id of this GroupBatchAddMemberDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The iam_id of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this GroupBatchAddMemberDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param iam_id: The iam_id of this GroupBatchAddMemberDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def user_id(self):
        r"""Gets the user_id of this GroupBatchAddMemberDto.

        **参数解释：** 用户userId。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The user_id of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GroupBatchAddMemberDto.

        **参数解释：** 用户userId。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param user_id: The user_id of this GroupBatchAddMemberDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this GroupBatchAddMemberDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupBatchAddMemberDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this GroupBatchAddMemberDto.
        :type name: str
        """
        self._name = name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this GroupBatchAddMemberDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The nick_name of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this GroupBatchAddMemberDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param nick_name: The nick_name of this GroupBatchAddMemberDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this GroupBatchAddMemberDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The domain_name of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this GroupBatchAddMemberDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param domain_name: The domain_name of this GroupBatchAddMemberDto.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupBatchAddMemberDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The domain_id of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupBatchAddMemberDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param domain_id: The domain_id of this GroupBatchAddMemberDto.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def repo_role_id(self):
        r"""Gets the repo_role_id of this GroupBatchAddMemberDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The repo_role_id of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._repo_role_id

    @repo_role_id.setter
    def repo_role_id(self, repo_role_id):
        r"""Sets the repo_role_id of this GroupBatchAddMemberDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param repo_role_id: The repo_role_id of this GroupBatchAddMemberDto.
        :type repo_role_id: str
        """
        self._repo_role_id = repo_role_id

    @property
    def req_role_id(self):
        r"""Gets the req_role_id of this GroupBatchAddMemberDto.

        **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The req_role_id of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._req_role_id

    @req_role_id.setter
    def req_role_id(self, req_role_id):
        r"""Sets the req_role_id of this GroupBatchAddMemberDto.

        **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param req_role_id: The req_role_id of this GroupBatchAddMemberDto.
        :type req_role_id: str
        """
        self._req_role_id = req_role_id

    @property
    def repo_role_name(self):
        r"""Gets the repo_role_name of this GroupBatchAddMemberDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The repo_role_name of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._repo_role_name

    @repo_role_name.setter
    def repo_role_name(self, repo_role_name):
        r"""Sets the repo_role_name of this GroupBatchAddMemberDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param repo_role_name: The repo_role_name of this GroupBatchAddMemberDto.
        :type repo_role_name: str
        """
        self._repo_role_name = repo_role_name

    @property
    def req_role_name(self):
        r"""Gets the req_role_name of this GroupBatchAddMemberDto.

        **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The req_role_name of this GroupBatchAddMemberDto.
        :rtype: str
        """
        return self._req_role_name

    @req_role_name.setter
    def req_role_name(self, req_role_name):
        r"""Sets the req_role_name of this GroupBatchAddMemberDto.

        **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param req_role_name: The req_role_name of this GroupBatchAddMemberDto.
        :type req_role_name: str
        """
        self._req_role_name = req_role_name

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
        if not isinstance(other, GroupBatchAddMemberDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
