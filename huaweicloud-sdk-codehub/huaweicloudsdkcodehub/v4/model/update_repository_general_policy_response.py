# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepositoryGeneralPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable_fork': 'bool',
        'generate_pre_merge_ref': 'bool',
        'branch_name_regex': 'str',
        'tag_name_regex': 'str',
        'forbidden_developer_create_branch': 'bool',
        'create_branch_whitelist_users': 'list[PushRuleDevelopersDto]'
    }

    attribute_map = {
        'disable_fork': 'disable_fork',
        'generate_pre_merge_ref': 'generate_pre_merge_ref',
        'branch_name_regex': 'branch_name_regex',
        'tag_name_regex': 'tag_name_regex',
        'forbidden_developer_create_branch': 'forbidden_developer_create_branch',
        'create_branch_whitelist_users': 'create_branch_whitelist_users'
    }

    def __init__(self, disable_fork=None, generate_pre_merge_ref=None, branch_name_regex=None, tag_name_regex=None, forbidden_developer_create_branch=None, create_branch_whitelist_users=None):
        r"""UpdateRepositoryGeneralPolicyResponse

        The model defined in huaweicloud sdk

        :param disable_fork: **参数解释：** 是否禁止fork该仓库。 **约束限制：** 不涉及。 **取值范围：** - true，禁止fork。 - false，允许fork。 **默认取值：** 不涉及。
        :type disable_fork: bool
        :param generate_pre_merge_ref: **参数解释：** 是否预合并MR。 **约束限制：** 不涉及。 **取值范围：** - true，禁止预合并MR。 - false，允许预合并MR。 **默认取值：** 不涉及。
        :type generate_pre_merge_ref: bool
        :param branch_name_regex: **参数解释：** 分支名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type branch_name_regex: str
        :param tag_name_regex: **参数解释：** Tag名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_name_regex: str
        :param forbidden_developer_create_branch: **参数解释：** 是否禁止开发者创建分支。 **约束限制：** 不涉及。 **取值范围：** - true，禁止开发者创建分支。 - false，允许开发者创建分支。
        :type forbidden_developer_create_branch: bool
        :param create_branch_whitelist_users: **参数解释：** 开发人员创建分支权限白名单。
        :type create_branch_whitelist_users: list[:class:`huaweicloudsdkcodehub.v4.PushRuleDevelopersDto`]
        """
        
        super(UpdateRepositoryGeneralPolicyResponse, self).__init__()

        self._disable_fork = None
        self._generate_pre_merge_ref = None
        self._branch_name_regex = None
        self._tag_name_regex = None
        self._forbidden_developer_create_branch = None
        self._create_branch_whitelist_users = None
        self.discriminator = None

        if disable_fork is not None:
            self.disable_fork = disable_fork
        if generate_pre_merge_ref is not None:
            self.generate_pre_merge_ref = generate_pre_merge_ref
        if branch_name_regex is not None:
            self.branch_name_regex = branch_name_regex
        if tag_name_regex is not None:
            self.tag_name_regex = tag_name_regex
        if forbidden_developer_create_branch is not None:
            self.forbidden_developer_create_branch = forbidden_developer_create_branch
        if create_branch_whitelist_users is not None:
            self.create_branch_whitelist_users = create_branch_whitelist_users

    @property
    def disable_fork(self):
        r"""Gets the disable_fork of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否禁止fork该仓库。 **约束限制：** 不涉及。 **取值范围：** - true，禁止fork。 - false，允许fork。 **默认取值：** 不涉及。

        :return: The disable_fork of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: bool
        """
        return self._disable_fork

    @disable_fork.setter
    def disable_fork(self, disable_fork):
        r"""Sets the disable_fork of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否禁止fork该仓库。 **约束限制：** 不涉及。 **取值范围：** - true，禁止fork。 - false，允许fork。 **默认取值：** 不涉及。

        :param disable_fork: The disable_fork of this UpdateRepositoryGeneralPolicyResponse.
        :type disable_fork: bool
        """
        self._disable_fork = disable_fork

    @property
    def generate_pre_merge_ref(self):
        r"""Gets the generate_pre_merge_ref of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否预合并MR。 **约束限制：** 不涉及。 **取值范围：** - true，禁止预合并MR。 - false，允许预合并MR。 **默认取值：** 不涉及。

        :return: The generate_pre_merge_ref of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: bool
        """
        return self._generate_pre_merge_ref

    @generate_pre_merge_ref.setter
    def generate_pre_merge_ref(self, generate_pre_merge_ref):
        r"""Sets the generate_pre_merge_ref of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否预合并MR。 **约束限制：** 不涉及。 **取值范围：** - true，禁止预合并MR。 - false，允许预合并MR。 **默认取值：** 不涉及。

        :param generate_pre_merge_ref: The generate_pre_merge_ref of this UpdateRepositoryGeneralPolicyResponse.
        :type generate_pre_merge_ref: bool
        """
        self._generate_pre_merge_ref = generate_pre_merge_ref

    @property
    def branch_name_regex(self):
        r"""Gets the branch_name_regex of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 分支名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The branch_name_regex of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: str
        """
        return self._branch_name_regex

    @branch_name_regex.setter
    def branch_name_regex(self, branch_name_regex):
        r"""Sets the branch_name_regex of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 分支名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param branch_name_regex: The branch_name_regex of this UpdateRepositoryGeneralPolicyResponse.
        :type branch_name_regex: str
        """
        self._branch_name_regex = branch_name_regex

    @property
    def tag_name_regex(self):
        r"""Gets the tag_name_regex of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** Tag名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_name_regex of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: str
        """
        return self._tag_name_regex

    @tag_name_regex.setter
    def tag_name_regex(self, tag_name_regex):
        r"""Sets the tag_name_regex of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** Tag名规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_name_regex: The tag_name_regex of this UpdateRepositoryGeneralPolicyResponse.
        :type tag_name_regex: str
        """
        self._tag_name_regex = tag_name_regex

    @property
    def forbidden_developer_create_branch(self):
        r"""Gets the forbidden_developer_create_branch of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否禁止开发者创建分支。 **约束限制：** 不涉及。 **取值范围：** - true，禁止开发者创建分支。 - false，允许开发者创建分支。

        :return: The forbidden_developer_create_branch of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: bool
        """
        return self._forbidden_developer_create_branch

    @forbidden_developer_create_branch.setter
    def forbidden_developer_create_branch(self, forbidden_developer_create_branch):
        r"""Sets the forbidden_developer_create_branch of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 是否禁止开发者创建分支。 **约束限制：** 不涉及。 **取值范围：** - true，禁止开发者创建分支。 - false，允许开发者创建分支。

        :param forbidden_developer_create_branch: The forbidden_developer_create_branch of this UpdateRepositoryGeneralPolicyResponse.
        :type forbidden_developer_create_branch: bool
        """
        self._forbidden_developer_create_branch = forbidden_developer_create_branch

    @property
    def create_branch_whitelist_users(self):
        r"""Gets the create_branch_whitelist_users of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 开发人员创建分支权限白名单。

        :return: The create_branch_whitelist_users of this UpdateRepositoryGeneralPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.PushRuleDevelopersDto`]
        """
        return self._create_branch_whitelist_users

    @create_branch_whitelist_users.setter
    def create_branch_whitelist_users(self, create_branch_whitelist_users):
        r"""Sets the create_branch_whitelist_users of this UpdateRepositoryGeneralPolicyResponse.

        **参数解释：** 开发人员创建分支权限白名单。

        :param create_branch_whitelist_users: The create_branch_whitelist_users of this UpdateRepositoryGeneralPolicyResponse.
        :type create_branch_whitelist_users: list[:class:`huaweicloudsdkcodehub.v4.PushRuleDevelopersDto`]
        """
        self._create_branch_whitelist_users = create_branch_whitelist_users

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
        if not isinstance(other, UpdateRepositoryGeneralPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
