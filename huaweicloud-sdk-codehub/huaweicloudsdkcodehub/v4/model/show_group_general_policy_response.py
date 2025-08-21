# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupGeneralPolicyResponse(SdkResponse):

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
        'forbidden_developer_create_branch': 'bool',
        'forbidden_developer_create_tag': 'bool',
        'forbidden_committer_create_branch': 'bool',
        'branch_name_regex': 'str',
        'tag_name_regex': 'str',
        'generate_pre_merge_ref': 'bool',
        'forbidden_gitlab_access': 'bool',
        'rebase_disable_trigger_webhook': 'bool',
        'open_gpg_verified': 'bool'
    }

    attribute_map = {
        'disable_fork': 'disable_fork',
        'forbidden_developer_create_branch': 'forbidden_developer_create_branch',
        'forbidden_developer_create_tag': 'forbidden_developer_create_tag',
        'forbidden_committer_create_branch': 'forbidden_committer_create_branch',
        'branch_name_regex': 'branch_name_regex',
        'tag_name_regex': 'tag_name_regex',
        'generate_pre_merge_ref': 'generate_pre_merge_ref',
        'forbidden_gitlab_access': 'forbidden_gitlab_access',
        'rebase_disable_trigger_webhook': 'rebase_disable_trigger_webhook',
        'open_gpg_verified': 'open_gpg_verified'
    }

    def __init__(self, disable_fork=None, forbidden_developer_create_branch=None, forbidden_developer_create_tag=None, forbidden_committer_create_branch=None, branch_name_regex=None, tag_name_regex=None, generate_pre_merge_ref=None, forbidden_gitlab_access=None, rebase_disable_trigger_webhook=None, open_gpg_verified=None):
        r"""ShowGroupGeneralPolicyResponse

        The model defined in huaweicloud sdk

        :param disable_fork: **参数解释：** 是否禁用fork。
        :type disable_fork: bool
        :param forbidden_developer_create_branch: **参数解释：** 是否禁止开发者创建分支。
        :type forbidden_developer_create_branch: bool
        :param forbidden_developer_create_tag: **参数解释：** 是否禁用开发者创建tag。
        :type forbidden_developer_create_tag: bool
        :param forbidden_committer_create_branch: **参数解释：** 禁止开发者创建标签。
        :type forbidden_committer_create_branch: bool
        :param branch_name_regex: **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type branch_name_regex: str
        :param tag_name_regex: **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tag_name_regex: str
        :param generate_pre_merge_ref: **参数解释：** 生成合并请求预合并。
        :type generate_pre_merge_ref: bool
        :param forbidden_gitlab_access: **参数解释：** 是否禁止repo访问。
        :type forbidden_gitlab_access: bool
        :param rebase_disable_trigger_webhook: **参数解释：** MR rebase是否禁止触发webhook事件。
        :type rebase_disable_trigger_webhook: bool
        :param open_gpg_verified: **参数解释：** 是否开启gpg公钥验证。
        :type open_gpg_verified: bool
        """
        
        super(ShowGroupGeneralPolicyResponse, self).__init__()

        self._disable_fork = None
        self._forbidden_developer_create_branch = None
        self._forbidden_developer_create_tag = None
        self._forbidden_committer_create_branch = None
        self._branch_name_regex = None
        self._tag_name_regex = None
        self._generate_pre_merge_ref = None
        self._forbidden_gitlab_access = None
        self._rebase_disable_trigger_webhook = None
        self._open_gpg_verified = None
        self.discriminator = None

        if disable_fork is not None:
            self.disable_fork = disable_fork
        if forbidden_developer_create_branch is not None:
            self.forbidden_developer_create_branch = forbidden_developer_create_branch
        if forbidden_developer_create_tag is not None:
            self.forbidden_developer_create_tag = forbidden_developer_create_tag
        if forbidden_committer_create_branch is not None:
            self.forbidden_committer_create_branch = forbidden_committer_create_branch
        if branch_name_regex is not None:
            self.branch_name_regex = branch_name_regex
        if tag_name_regex is not None:
            self.tag_name_regex = tag_name_regex
        if generate_pre_merge_ref is not None:
            self.generate_pre_merge_ref = generate_pre_merge_ref
        if forbidden_gitlab_access is not None:
            self.forbidden_gitlab_access = forbidden_gitlab_access
        if rebase_disable_trigger_webhook is not None:
            self.rebase_disable_trigger_webhook = rebase_disable_trigger_webhook
        if open_gpg_verified is not None:
            self.open_gpg_verified = open_gpg_verified

    @property
    def disable_fork(self):
        r"""Gets the disable_fork of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁用fork。

        :return: The disable_fork of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._disable_fork

    @disable_fork.setter
    def disable_fork(self, disable_fork):
        r"""Sets the disable_fork of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁用fork。

        :param disable_fork: The disable_fork of this ShowGroupGeneralPolicyResponse.
        :type disable_fork: bool
        """
        self._disable_fork = disable_fork

    @property
    def forbidden_developer_create_branch(self):
        r"""Gets the forbidden_developer_create_branch of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁止开发者创建分支。

        :return: The forbidden_developer_create_branch of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._forbidden_developer_create_branch

    @forbidden_developer_create_branch.setter
    def forbidden_developer_create_branch(self, forbidden_developer_create_branch):
        r"""Sets the forbidden_developer_create_branch of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁止开发者创建分支。

        :param forbidden_developer_create_branch: The forbidden_developer_create_branch of this ShowGroupGeneralPolicyResponse.
        :type forbidden_developer_create_branch: bool
        """
        self._forbidden_developer_create_branch = forbidden_developer_create_branch

    @property
    def forbidden_developer_create_tag(self):
        r"""Gets the forbidden_developer_create_tag of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁用开发者创建tag。

        :return: The forbidden_developer_create_tag of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._forbidden_developer_create_tag

    @forbidden_developer_create_tag.setter
    def forbidden_developer_create_tag(self, forbidden_developer_create_tag):
        r"""Sets the forbidden_developer_create_tag of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁用开发者创建tag。

        :param forbidden_developer_create_tag: The forbidden_developer_create_tag of this ShowGroupGeneralPolicyResponse.
        :type forbidden_developer_create_tag: bool
        """
        self._forbidden_developer_create_tag = forbidden_developer_create_tag

    @property
    def forbidden_committer_create_branch(self):
        r"""Gets the forbidden_committer_create_branch of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 禁止开发者创建标签。

        :return: The forbidden_committer_create_branch of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._forbidden_committer_create_branch

    @forbidden_committer_create_branch.setter
    def forbidden_committer_create_branch(self, forbidden_committer_create_branch):
        r"""Sets the forbidden_committer_create_branch of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 禁止开发者创建标签。

        :param forbidden_committer_create_branch: The forbidden_committer_create_branch of this ShowGroupGeneralPolicyResponse.
        :type forbidden_committer_create_branch: bool
        """
        self._forbidden_committer_create_branch = forbidden_committer_create_branch

    @property
    def branch_name_regex(self):
        r"""Gets the branch_name_regex of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The branch_name_regex of this ShowGroupGeneralPolicyResponse.
        :rtype: str
        """
        return self._branch_name_regex

    @branch_name_regex.setter
    def branch_name_regex(self, branch_name_regex):
        r"""Sets the branch_name_regex of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 分支名称正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param branch_name_regex: The branch_name_regex of this ShowGroupGeneralPolicyResponse.
        :type branch_name_regex: str
        """
        self._branch_name_regex = branch_name_regex

    @property
    def tag_name_regex(self):
        r"""Gets the tag_name_regex of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tag_name_regex of this ShowGroupGeneralPolicyResponse.
        :rtype: str
        """
        return self._tag_name_regex

    @tag_name_regex.setter
    def tag_name_regex(self, tag_name_regex):
        r"""Sets the tag_name_regex of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 标签名正则表达式。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tag_name_regex: The tag_name_regex of this ShowGroupGeneralPolicyResponse.
        :type tag_name_regex: str
        """
        self._tag_name_regex = tag_name_regex

    @property
    def generate_pre_merge_ref(self):
        r"""Gets the generate_pre_merge_ref of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 生成合并请求预合并。

        :return: The generate_pre_merge_ref of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._generate_pre_merge_ref

    @generate_pre_merge_ref.setter
    def generate_pre_merge_ref(self, generate_pre_merge_ref):
        r"""Sets the generate_pre_merge_ref of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 生成合并请求预合并。

        :param generate_pre_merge_ref: The generate_pre_merge_ref of this ShowGroupGeneralPolicyResponse.
        :type generate_pre_merge_ref: bool
        """
        self._generate_pre_merge_ref = generate_pre_merge_ref

    @property
    def forbidden_gitlab_access(self):
        r"""Gets the forbidden_gitlab_access of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁止repo访问。

        :return: The forbidden_gitlab_access of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._forbidden_gitlab_access

    @forbidden_gitlab_access.setter
    def forbidden_gitlab_access(self, forbidden_gitlab_access):
        r"""Sets the forbidden_gitlab_access of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否禁止repo访问。

        :param forbidden_gitlab_access: The forbidden_gitlab_access of this ShowGroupGeneralPolicyResponse.
        :type forbidden_gitlab_access: bool
        """
        self._forbidden_gitlab_access = forbidden_gitlab_access

    @property
    def rebase_disable_trigger_webhook(self):
        r"""Gets the rebase_disable_trigger_webhook of this ShowGroupGeneralPolicyResponse.

        **参数解释：** MR rebase是否禁止触发webhook事件。

        :return: The rebase_disable_trigger_webhook of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._rebase_disable_trigger_webhook

    @rebase_disable_trigger_webhook.setter
    def rebase_disable_trigger_webhook(self, rebase_disable_trigger_webhook):
        r"""Sets the rebase_disable_trigger_webhook of this ShowGroupGeneralPolicyResponse.

        **参数解释：** MR rebase是否禁止触发webhook事件。

        :param rebase_disable_trigger_webhook: The rebase_disable_trigger_webhook of this ShowGroupGeneralPolicyResponse.
        :type rebase_disable_trigger_webhook: bool
        """
        self._rebase_disable_trigger_webhook = rebase_disable_trigger_webhook

    @property
    def open_gpg_verified(self):
        r"""Gets the open_gpg_verified of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否开启gpg公钥验证。

        :return: The open_gpg_verified of this ShowGroupGeneralPolicyResponse.
        :rtype: bool
        """
        return self._open_gpg_verified

    @open_gpg_verified.setter
    def open_gpg_verified(self, open_gpg_verified):
        r"""Sets the open_gpg_verified of this ShowGroupGeneralPolicyResponse.

        **参数解释：** 是否开启gpg公钥验证。

        :param open_gpg_verified: The open_gpg_verified of this ShowGroupGeneralPolicyResponse.
        :type open_gpg_verified: bool
        """
        self._open_gpg_verified = open_gpg_verified

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
        if not isinstance(other, ShowGroupGeneralPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
