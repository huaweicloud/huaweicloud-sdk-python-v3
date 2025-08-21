# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitRuleDto:

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
        'repository_id': 'int',
        'commit_message_regex': 'str',
        'commit_message_negative_regex': 'str',
        'prohibited_file_name_regex': 'str',
        'author_email_regex': 'str',
        'max_file_size': 'int',
        'allowed_max_file_size': 'int',
        'effective_date': 'str',
        'binary_gate_enabled': 'bool',
        'privileged_users': 'list[RepositoryUserBasicDto]',
        'allowed_modify_binary': 'bool',
        'allowed_binary_file_name_regex': 'str',
        'author_regex': 'object',
        'updated_at': 'str',
        'skip_rule_check': 'bool',
        'skip_rule_end_date': 'str',
        'name': 'str',
        'branch_name': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'commit_message_regex': 'commit_message_regex',
        'commit_message_negative_regex': 'commit_message_negative_regex',
        'prohibited_file_name_regex': 'prohibited_file_name_regex',
        'author_email_regex': 'author_email_regex',
        'max_file_size': 'max_file_size',
        'allowed_max_file_size': 'allowed_max_file_size',
        'effective_date': 'effective_date',
        'binary_gate_enabled': 'binary_gate_enabled',
        'privileged_users': 'privileged_users',
        'allowed_modify_binary': 'allowed_modify_binary',
        'allowed_binary_file_name_regex': 'allowed_binary_file_name_regex',
        'author_regex': 'author_regex',
        'updated_at': 'updated_at',
        'skip_rule_check': 'skip_rule_check',
        'skip_rule_end_date': 'skip_rule_end_date',
        'name': 'name',
        'branch_name': 'branch_name',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, repository_id=None, commit_message_regex=None, commit_message_negative_regex=None, prohibited_file_name_regex=None, author_email_regex=None, max_file_size=None, allowed_max_file_size=None, effective_date=None, binary_gate_enabled=None, privileged_users=None, allowed_modify_binary=None, allowed_binary_file_name_regex=None, author_regex=None, updated_at=None, skip_rule_check=None, skip_rule_end_date=None, name=None, branch_name=None, created_at=None):
        r"""CommitRuleDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 主键ID。 **取值范围：** 不涉及。
        :type id: int
        :param repository_id: **参数解释：** 仓库ID。 **取值范围：** 不涉及。
        :type repository_id: int
        :param commit_message_regex: **参数解释：** 提交信息匹配规则。
        :type commit_message_regex: str
        :param commit_message_negative_regex: **参数解释：** 提交信息负面匹配规则。
        :type commit_message_negative_regex: str
        :param prohibited_file_name_regex: **参数解释：** 禁止提交的文件名称。
        :type prohibited_file_name_regex: str
        :param author_email_regex: **参数解释：** 提交人邮箱地址。
        :type author_email_regex: str
        :param max_file_size: **参数解释：** 单文件大小限制（MB）。
        :type max_file_size: int
        :param allowed_max_file_size: **参数解释：** 允许的最大单文件大小（MB）。
        :type allowed_max_file_size: int
        :param effective_date: **参数解释：** 规则生效时间。
        :type effective_date: str
        :param binary_gate_enabled: **参数解释：** 是否禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。
        :type binary_gate_enabled: bool
        :param privileged_users: **参数解释：** 特权用户（特权用户可直接推送所有二进制文件入库）。
        :type privileged_users: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`]
        :param allowed_modify_binary: **参数解释：** 是否允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。
        :type allowed_modify_binary: bool
        :param allowed_binary_file_name_regex: **参数解释：** 二进制文件白名单（可直接入库的文件）。
        :type allowed_binary_file_name_regex: str
        :param author_regex: **参数解释：** 提交人。
        :type author_regex: object
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param skip_rule_check: **参数解释：** 是否跳过规则检测。 **约束限制：** 不涉及。 **取值范围：** - true，跳过规则检测。 - false，不跳过规则检测。
        :type skip_rule_check: bool
        :param skip_rule_end_date: **参数解释：** 失效时间。
        :type skip_rule_end_date: str
        :param name: **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param branch_name: **参数解释：** 分支规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type branch_name: str
        :param created_at: **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type created_at: str
        """
        
        

        self._id = None
        self._repository_id = None
        self._commit_message_regex = None
        self._commit_message_negative_regex = None
        self._prohibited_file_name_regex = None
        self._author_email_regex = None
        self._max_file_size = None
        self._allowed_max_file_size = None
        self._effective_date = None
        self._binary_gate_enabled = None
        self._privileged_users = None
        self._allowed_modify_binary = None
        self._allowed_binary_file_name_regex = None
        self._author_regex = None
        self._updated_at = None
        self._skip_rule_check = None
        self._skip_rule_end_date = None
        self._name = None
        self._branch_name = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if commit_message_regex is not None:
            self.commit_message_regex = commit_message_regex
        if commit_message_negative_regex is not None:
            self.commit_message_negative_regex = commit_message_negative_regex
        if prohibited_file_name_regex is not None:
            self.prohibited_file_name_regex = prohibited_file_name_regex
        if author_email_regex is not None:
            self.author_email_regex = author_email_regex
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if allowed_max_file_size is not None:
            self.allowed_max_file_size = allowed_max_file_size
        if effective_date is not None:
            self.effective_date = effective_date
        if binary_gate_enabled is not None:
            self.binary_gate_enabled = binary_gate_enabled
        if privileged_users is not None:
            self.privileged_users = privileged_users
        if allowed_modify_binary is not None:
            self.allowed_modify_binary = allowed_modify_binary
        if allowed_binary_file_name_regex is not None:
            self.allowed_binary_file_name_regex = allowed_binary_file_name_regex
        if author_regex is not None:
            self.author_regex = author_regex
        if updated_at is not None:
            self.updated_at = updated_at
        if skip_rule_check is not None:
            self.skip_rule_check = skip_rule_check
        if skip_rule_end_date is not None:
            self.skip_rule_end_date = skip_rule_end_date
        if name is not None:
            self.name = name
        if branch_name is not None:
            self.branch_name = branch_name
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this CommitRuleDto.

        **参数解释：** 主键ID。 **取值范围：** 不涉及。

        :return: The id of this CommitRuleDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommitRuleDto.

        **参数解释：** 主键ID。 **取值范围：** 不涉及。

        :param id: The id of this CommitRuleDto.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this CommitRuleDto.

        **参数解释：** 仓库ID。 **取值范围：** 不涉及。

        :return: The repository_id of this CommitRuleDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this CommitRuleDto.

        **参数解释：** 仓库ID。 **取值范围：** 不涉及。

        :param repository_id: The repository_id of this CommitRuleDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def commit_message_regex(self):
        r"""Gets the commit_message_regex of this CommitRuleDto.

        **参数解释：** 提交信息匹配规则。

        :return: The commit_message_regex of this CommitRuleDto.
        :rtype: str
        """
        return self._commit_message_regex

    @commit_message_regex.setter
    def commit_message_regex(self, commit_message_regex):
        r"""Sets the commit_message_regex of this CommitRuleDto.

        **参数解释：** 提交信息匹配规则。

        :param commit_message_regex: The commit_message_regex of this CommitRuleDto.
        :type commit_message_regex: str
        """
        self._commit_message_regex = commit_message_regex

    @property
    def commit_message_negative_regex(self):
        r"""Gets the commit_message_negative_regex of this CommitRuleDto.

        **参数解释：** 提交信息负面匹配规则。

        :return: The commit_message_negative_regex of this CommitRuleDto.
        :rtype: str
        """
        return self._commit_message_negative_regex

    @commit_message_negative_regex.setter
    def commit_message_negative_regex(self, commit_message_negative_regex):
        r"""Sets the commit_message_negative_regex of this CommitRuleDto.

        **参数解释：** 提交信息负面匹配规则。

        :param commit_message_negative_regex: The commit_message_negative_regex of this CommitRuleDto.
        :type commit_message_negative_regex: str
        """
        self._commit_message_negative_regex = commit_message_negative_regex

    @property
    def prohibited_file_name_regex(self):
        r"""Gets the prohibited_file_name_regex of this CommitRuleDto.

        **参数解释：** 禁止提交的文件名称。

        :return: The prohibited_file_name_regex of this CommitRuleDto.
        :rtype: str
        """
        return self._prohibited_file_name_regex

    @prohibited_file_name_regex.setter
    def prohibited_file_name_regex(self, prohibited_file_name_regex):
        r"""Sets the prohibited_file_name_regex of this CommitRuleDto.

        **参数解释：** 禁止提交的文件名称。

        :param prohibited_file_name_regex: The prohibited_file_name_regex of this CommitRuleDto.
        :type prohibited_file_name_regex: str
        """
        self._prohibited_file_name_regex = prohibited_file_name_regex

    @property
    def author_email_regex(self):
        r"""Gets the author_email_regex of this CommitRuleDto.

        **参数解释：** 提交人邮箱地址。

        :return: The author_email_regex of this CommitRuleDto.
        :rtype: str
        """
        return self._author_email_regex

    @author_email_regex.setter
    def author_email_regex(self, author_email_regex):
        r"""Sets the author_email_regex of this CommitRuleDto.

        **参数解释：** 提交人邮箱地址。

        :param author_email_regex: The author_email_regex of this CommitRuleDto.
        :type author_email_regex: str
        """
        self._author_email_regex = author_email_regex

    @property
    def max_file_size(self):
        r"""Gets the max_file_size of this CommitRuleDto.

        **参数解释：** 单文件大小限制（MB）。

        :return: The max_file_size of this CommitRuleDto.
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        r"""Sets the max_file_size of this CommitRuleDto.

        **参数解释：** 单文件大小限制（MB）。

        :param max_file_size: The max_file_size of this CommitRuleDto.
        :type max_file_size: int
        """
        self._max_file_size = max_file_size

    @property
    def allowed_max_file_size(self):
        r"""Gets the allowed_max_file_size of this CommitRuleDto.

        **参数解释：** 允许的最大单文件大小（MB）。

        :return: The allowed_max_file_size of this CommitRuleDto.
        :rtype: int
        """
        return self._allowed_max_file_size

    @allowed_max_file_size.setter
    def allowed_max_file_size(self, allowed_max_file_size):
        r"""Sets the allowed_max_file_size of this CommitRuleDto.

        **参数解释：** 允许的最大单文件大小（MB）。

        :param allowed_max_file_size: The allowed_max_file_size of this CommitRuleDto.
        :type allowed_max_file_size: int
        """
        self._allowed_max_file_size = allowed_max_file_size

    @property
    def effective_date(self):
        r"""Gets the effective_date of this CommitRuleDto.

        **参数解释：** 规则生效时间。

        :return: The effective_date of this CommitRuleDto.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        r"""Sets the effective_date of this CommitRuleDto.

        **参数解释：** 规则生效时间。

        :param effective_date: The effective_date of this CommitRuleDto.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def binary_gate_enabled(self):
        r"""Gets the binary_gate_enabled of this CommitRuleDto.

        **参数解释：** 是否禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。

        :return: The binary_gate_enabled of this CommitRuleDto.
        :rtype: bool
        """
        return self._binary_gate_enabled

    @binary_gate_enabled.setter
    def binary_gate_enabled(self, binary_gate_enabled):
        r"""Sets the binary_gate_enabled of this CommitRuleDto.

        **参数解释：** 是否禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。

        :param binary_gate_enabled: The binary_gate_enabled of this CommitRuleDto.
        :type binary_gate_enabled: bool
        """
        self._binary_gate_enabled = binary_gate_enabled

    @property
    def privileged_users(self):
        r"""Gets the privileged_users of this CommitRuleDto.

        **参数解释：** 特权用户（特权用户可直接推送所有二进制文件入库）。

        :return: The privileged_users of this CommitRuleDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`]
        """
        return self._privileged_users

    @privileged_users.setter
    def privileged_users(self, privileged_users):
        r"""Sets the privileged_users of this CommitRuleDto.

        **参数解释：** 特权用户（特权用户可直接推送所有二进制文件入库）。

        :param privileged_users: The privileged_users of this CommitRuleDto.
        :type privileged_users: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`]
        """
        self._privileged_users = privileged_users

    @property
    def allowed_modify_binary(self):
        r"""Gets the allowed_modify_binary of this CommitRuleDto.

        **参数解释：** 是否允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。

        :return: The allowed_modify_binary of this CommitRuleDto.
        :rtype: bool
        """
        return self._allowed_modify_binary

    @allowed_modify_binary.setter
    def allowed_modify_binary(self, allowed_modify_binary):
        r"""Sets the allowed_modify_binary of this CommitRuleDto.

        **参数解释：** 是否允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。

        :param allowed_modify_binary: The allowed_modify_binary of this CommitRuleDto.
        :type allowed_modify_binary: bool
        """
        self._allowed_modify_binary = allowed_modify_binary

    @property
    def allowed_binary_file_name_regex(self):
        r"""Gets the allowed_binary_file_name_regex of this CommitRuleDto.

        **参数解释：** 二进制文件白名单（可直接入库的文件）。

        :return: The allowed_binary_file_name_regex of this CommitRuleDto.
        :rtype: str
        """
        return self._allowed_binary_file_name_regex

    @allowed_binary_file_name_regex.setter
    def allowed_binary_file_name_regex(self, allowed_binary_file_name_regex):
        r"""Sets the allowed_binary_file_name_regex of this CommitRuleDto.

        **参数解释：** 二进制文件白名单（可直接入库的文件）。

        :param allowed_binary_file_name_regex: The allowed_binary_file_name_regex of this CommitRuleDto.
        :type allowed_binary_file_name_regex: str
        """
        self._allowed_binary_file_name_regex = allowed_binary_file_name_regex

    @property
    def author_regex(self):
        r"""Gets the author_regex of this CommitRuleDto.

        **参数解释：** 提交人。

        :return: The author_regex of this CommitRuleDto.
        :rtype: object
        """
        return self._author_regex

    @author_regex.setter
    def author_regex(self, author_regex):
        r"""Sets the author_regex of this CommitRuleDto.

        **参数解释：** 提交人。

        :param author_regex: The author_regex of this CommitRuleDto.
        :type author_regex: object
        """
        self._author_regex = author_regex

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CommitRuleDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this CommitRuleDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CommitRuleDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this CommitRuleDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def skip_rule_check(self):
        r"""Gets the skip_rule_check of this CommitRuleDto.

        **参数解释：** 是否跳过规则检测。 **约束限制：** 不涉及。 **取值范围：** - true，跳过规则检测。 - false，不跳过规则检测。

        :return: The skip_rule_check of this CommitRuleDto.
        :rtype: bool
        """
        return self._skip_rule_check

    @skip_rule_check.setter
    def skip_rule_check(self, skip_rule_check):
        r"""Sets the skip_rule_check of this CommitRuleDto.

        **参数解释：** 是否跳过规则检测。 **约束限制：** 不涉及。 **取值范围：** - true，跳过规则检测。 - false，不跳过规则检测。

        :param skip_rule_check: The skip_rule_check of this CommitRuleDto.
        :type skip_rule_check: bool
        """
        self._skip_rule_check = skip_rule_check

    @property
    def skip_rule_end_date(self):
        r"""Gets the skip_rule_end_date of this CommitRuleDto.

        **参数解释：** 失效时间。

        :return: The skip_rule_end_date of this CommitRuleDto.
        :rtype: str
        """
        return self._skip_rule_end_date

    @skip_rule_end_date.setter
    def skip_rule_end_date(self, skip_rule_end_date):
        r"""Sets the skip_rule_end_date of this CommitRuleDto.

        **参数解释：** 失效时间。

        :param skip_rule_end_date: The skip_rule_end_date of this CommitRuleDto.
        :type skip_rule_end_date: str
        """
        self._skip_rule_end_date = skip_rule_end_date

    @property
    def name(self):
        r"""Gets the name of this CommitRuleDto.

        **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this CommitRuleDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CommitRuleDto.

        **参数解释：** 规则名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this CommitRuleDto.
        :type name: str
        """
        self._name = name

    @property
    def branch_name(self):
        r"""Gets the branch_name of this CommitRuleDto.

        **参数解释：** 分支规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The branch_name of this CommitRuleDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this CommitRuleDto.

        **参数解释：** 分支规则。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param branch_name: The branch_name of this CommitRuleDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def created_at(self):
        r"""Gets the created_at of this CommitRuleDto.

        **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The created_at of this CommitRuleDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CommitRuleDto.

        **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param created_at: The created_at of this CommitRuleDto.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, CommitRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
