# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryGeneralCommitRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reject_unsigned_commits': 'bool',
        'reject_not_signed_by_gpg': 'bool',
        'deny_delete_tag': 'bool',
        'prevent_secrets': 'bool',
        'deny_force_push': 'bool'
    }

    attribute_map = {
        'reject_unsigned_commits': 'reject_unsigned_commits',
        'reject_not_signed_by_gpg': 'reject_not_signed_by_gpg',
        'deny_delete_tag': 'deny_delete_tag',
        'prevent_secrets': 'prevent_secrets',
        'deny_force_push': 'deny_force_push'
    }

    def __init__(self, reject_unsigned_commits=None, reject_not_signed_by_gpg=None, deny_delete_tag=None, prevent_secrets=None, deny_force_push=None):
        r"""ShowRepositoryGeneralCommitRuleResponse

        The model defined in huaweicloud sdk

        :param reject_unsigned_commits: **参数解释：** 是否拒绝未Signed-off-by签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未Signed-off-by签名的提交。 - false，允许未Signed-off-by签名的提交。 **默认取值：** 不涉及。
        :type reject_unsigned_commits: bool
        :param reject_not_signed_by_gpg: **参数解释：** 是否拒绝未GPG签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未GPG签名的提交。 - false，允许未GPG签名的提交。 **默认取值：** 不涉及。
        :type reject_not_signed_by_gpg: bool
        :param deny_delete_tag: **参数解释：** 是否不允许删除Tags。 **约束限制：** 不涉及。 **取值范围：** - true，不允许删除Tags。 - false，允许删除Tags。 **默认取值：** 不涉及。
        :type deny_delete_tag: bool
        :param prevent_secrets: **参数解释：** 是否阻止包含涉密文件的提交。 **约束限制：** 不涉及。 **取值范围：** - true，阻止包含涉密文件的提交。 - false，允许包含涉密文件的提交。 **默认取值：** 不涉及。
        :type prevent_secrets: bool
        :param deny_force_push: **参数解释：** 是否禁止强制推送。 **约束限制：** 不涉及。 **取值范围：** - true，禁止强制推送。 - false，允许强制推送。 **默认取值：** 不涉及。
        :type deny_force_push: bool
        """
        
        super(ShowRepositoryGeneralCommitRuleResponse, self).__init__()

        self._reject_unsigned_commits = None
        self._reject_not_signed_by_gpg = None
        self._deny_delete_tag = None
        self._prevent_secrets = None
        self._deny_force_push = None
        self.discriminator = None

        if reject_unsigned_commits is not None:
            self.reject_unsigned_commits = reject_unsigned_commits
        if reject_not_signed_by_gpg is not None:
            self.reject_not_signed_by_gpg = reject_not_signed_by_gpg
        if deny_delete_tag is not None:
            self.deny_delete_tag = deny_delete_tag
        if prevent_secrets is not None:
            self.prevent_secrets = prevent_secrets
        if deny_force_push is not None:
            self.deny_force_push = deny_force_push

    @property
    def reject_unsigned_commits(self):
        r"""Gets the reject_unsigned_commits of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否拒绝未Signed-off-by签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未Signed-off-by签名的提交。 - false，允许未Signed-off-by签名的提交。 **默认取值：** 不涉及。

        :return: The reject_unsigned_commits of this ShowRepositoryGeneralCommitRuleResponse.
        :rtype: bool
        """
        return self._reject_unsigned_commits

    @reject_unsigned_commits.setter
    def reject_unsigned_commits(self, reject_unsigned_commits):
        r"""Sets the reject_unsigned_commits of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否拒绝未Signed-off-by签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未Signed-off-by签名的提交。 - false，允许未Signed-off-by签名的提交。 **默认取值：** 不涉及。

        :param reject_unsigned_commits: The reject_unsigned_commits of this ShowRepositoryGeneralCommitRuleResponse.
        :type reject_unsigned_commits: bool
        """
        self._reject_unsigned_commits = reject_unsigned_commits

    @property
    def reject_not_signed_by_gpg(self):
        r"""Gets the reject_not_signed_by_gpg of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否拒绝未GPG签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未GPG签名的提交。 - false，允许未GPG签名的提交。 **默认取值：** 不涉及。

        :return: The reject_not_signed_by_gpg of this ShowRepositoryGeneralCommitRuleResponse.
        :rtype: bool
        """
        return self._reject_not_signed_by_gpg

    @reject_not_signed_by_gpg.setter
    def reject_not_signed_by_gpg(self, reject_not_signed_by_gpg):
        r"""Sets the reject_not_signed_by_gpg of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否拒绝未GPG签名的提交。 **约束限制：** 不涉及。 **取值范围：** - true，拒绝未GPG签名的提交。 - false，允许未GPG签名的提交。 **默认取值：** 不涉及。

        :param reject_not_signed_by_gpg: The reject_not_signed_by_gpg of this ShowRepositoryGeneralCommitRuleResponse.
        :type reject_not_signed_by_gpg: bool
        """
        self._reject_not_signed_by_gpg = reject_not_signed_by_gpg

    @property
    def deny_delete_tag(self):
        r"""Gets the deny_delete_tag of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否不允许删除Tags。 **约束限制：** 不涉及。 **取值范围：** - true，不允许删除Tags。 - false，允许删除Tags。 **默认取值：** 不涉及。

        :return: The deny_delete_tag of this ShowRepositoryGeneralCommitRuleResponse.
        :rtype: bool
        """
        return self._deny_delete_tag

    @deny_delete_tag.setter
    def deny_delete_tag(self, deny_delete_tag):
        r"""Sets the deny_delete_tag of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否不允许删除Tags。 **约束限制：** 不涉及。 **取值范围：** - true，不允许删除Tags。 - false，允许删除Tags。 **默认取值：** 不涉及。

        :param deny_delete_tag: The deny_delete_tag of this ShowRepositoryGeneralCommitRuleResponse.
        :type deny_delete_tag: bool
        """
        self._deny_delete_tag = deny_delete_tag

    @property
    def prevent_secrets(self):
        r"""Gets the prevent_secrets of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否阻止包含涉密文件的提交。 **约束限制：** 不涉及。 **取值范围：** - true，阻止包含涉密文件的提交。 - false，允许包含涉密文件的提交。 **默认取值：** 不涉及。

        :return: The prevent_secrets of this ShowRepositoryGeneralCommitRuleResponse.
        :rtype: bool
        """
        return self._prevent_secrets

    @prevent_secrets.setter
    def prevent_secrets(self, prevent_secrets):
        r"""Sets the prevent_secrets of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否阻止包含涉密文件的提交。 **约束限制：** 不涉及。 **取值范围：** - true，阻止包含涉密文件的提交。 - false，允许包含涉密文件的提交。 **默认取值：** 不涉及。

        :param prevent_secrets: The prevent_secrets of this ShowRepositoryGeneralCommitRuleResponse.
        :type prevent_secrets: bool
        """
        self._prevent_secrets = prevent_secrets

    @property
    def deny_force_push(self):
        r"""Gets the deny_force_push of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否禁止强制推送。 **约束限制：** 不涉及。 **取值范围：** - true，禁止强制推送。 - false，允许强制推送。 **默认取值：** 不涉及。

        :return: The deny_force_push of this ShowRepositoryGeneralCommitRuleResponse.
        :rtype: bool
        """
        return self._deny_force_push

    @deny_force_push.setter
    def deny_force_push(self, deny_force_push):
        r"""Sets the deny_force_push of this ShowRepositoryGeneralCommitRuleResponse.

        **参数解释：** 是否禁止强制推送。 **约束限制：** 不涉及。 **取值范围：** - true，禁止强制推送。 - false，允许强制推送。 **默认取值：** 不涉及。

        :param deny_force_push: The deny_force_push of this ShowRepositoryGeneralCommitRuleResponse.
        :type deny_force_push: bool
        """
        self._deny_force_push = deny_force_push

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
        if not isinstance(other, ShowRepositoryGeneralCommitRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
