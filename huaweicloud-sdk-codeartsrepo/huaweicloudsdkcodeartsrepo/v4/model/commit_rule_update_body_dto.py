# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitRuleUpdateBodyDto:

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
        'branch_name': 'str',
        'commit_message_regex': 'str',
        'commit_message_negative_regex': 'str',
        'author_regex': 'str',
        'author_email_regex': 'str',
        'prohibited_file_name_regex': 'str',
        'max_file_size': 'int',
        'binary_gate_enabled': 'bool',
        'allowed_modify_binary': 'bool',
        'allowed_binary_file_name_regex': 'str',
        'privileged_user_ids': 'list[int]',
        'effective_date': 'str',
        'skip_rule_check': 'bool',
        'skip_rule_end_date': 'str'
    }

    attribute_map = {
        'name': 'name',
        'branch_name': 'branch_name',
        'commit_message_regex': 'commit_message_regex',
        'commit_message_negative_regex': 'commit_message_negative_regex',
        'author_regex': 'author_regex',
        'author_email_regex': 'author_email_regex',
        'prohibited_file_name_regex': 'prohibited_file_name_regex',
        'max_file_size': 'max_file_size',
        'binary_gate_enabled': 'binary_gate_enabled',
        'allowed_modify_binary': 'allowed_modify_binary',
        'allowed_binary_file_name_regex': 'allowed_binary_file_name_regex',
        'privileged_user_ids': 'privileged_user_ids',
        'effective_date': 'effective_date',
        'skip_rule_check': 'skip_rule_check',
        'skip_rule_end_date': 'skip_rule_end_date'
    }

    def __init__(self, name=None, branch_name=None, commit_message_regex=None, commit_message_negative_regex=None, author_regex=None, author_email_regex=None, prohibited_file_name_regex=None, max_file_size=None, binary_gate_enabled=None, allowed_modify_binary=None, allowed_binary_file_name_regex=None, privileged_user_ids=None, effective_date=None, skip_rule_check=None, skip_rule_end_date=None):
        r"""CommitRuleUpdateBodyDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 规则名称。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param branch_name: **参数解释：** 分支规则。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type branch_name: str
        :param commit_message_regex: **参数解释：** 提交信息匹配规则。 所有提交消息都必须进行正则表达式匹配， 例如: \\d+\\..*。 若符合正则匹配，则允许提交。若此字段为空，则允许任何提交消息。 您也可以设置在提交信息中必须包含工作项单号，实现代码的E2E追溯。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type commit_message_regex: str
        :param commit_message_negative_regex: **参数解释：** 提交信息负面匹配规则。 所有提交消息都必须进行正则表达式匹配，例如: \\d+\\..*。 符合正则匹配，则不允许提交。若此字段为空，则允许任何提交消息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type commit_message_negative_regex: str
        :param author_regex: **参数解释：** 提交人的正则表达式。 提交人必须进行正则表达式匹配， 例如: /([a-zA-Z]\\d){7}/。如果此字段为空，则允许任何提交人。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type author_regex: str
        :param author_email_regex: **参数解释：** 提交人邮箱地址的正则表达式。 所有提交者邮箱地址都必须进行正则表达式匹配， 例如: @my-company.com$。如果此字段为空，则允许任何提交邮箱地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type author_email_regex: str
        :param prohibited_file_name_regex: **参数解释：** 禁止提交的文件名称的正则表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type prohibited_file_name_regex: str
        :param max_file_size: **参数解释：** 单文件大小限制（MB）。 单文件大小超过上述规格的添加或更新推送将被拒绝，Repo建议的最佳上限值为50MB。 系统支持单文件提交的最大值为300MB。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 50
        :type max_file_size: int
        :param binary_gate_enabled: **参数解释：** 禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。 **默认取值：** 不涉及。
        :type binary_gate_enabled: bool
        :param allowed_modify_binary: **参数解释：** 允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。 **默认取值：** 不涉及。
        :type allowed_modify_binary: bool
        :param allowed_binary_file_name_regex: **参数解释：** 二进制文件白名单（可直接入库的文件）。 所有被推送的二进制文件名必须进行正则表达式匹配， 例如: (\\.png|\\.xls|\\.xlsx|\\.docx|\\.doc)$ 。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type allowed_binary_file_name_regex: str
        :param privileged_user_ids: **参数解释：** 特权用户ID列表（特权用户可直接推送所有二进制文件入库。 只有特权用户能推送二进制文件。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type privileged_user_ids: list[int]
        :param effective_date: **参数解释：** 规则生效时间， 例如: 2025-8-19。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type effective_date: str
        :param skip_rule_check: **参数解释：** 跳过规则检测。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type skip_rule_check: bool
        :param skip_rule_end_date: **参数解释：** 跳过规则检测失效时间， 例如: 2025-8-19 10:00:00。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type skip_rule_end_date: str
        """
        
        

        self._name = None
        self._branch_name = None
        self._commit_message_regex = None
        self._commit_message_negative_regex = None
        self._author_regex = None
        self._author_email_regex = None
        self._prohibited_file_name_regex = None
        self._max_file_size = None
        self._binary_gate_enabled = None
        self._allowed_modify_binary = None
        self._allowed_binary_file_name_regex = None
        self._privileged_user_ids = None
        self._effective_date = None
        self._skip_rule_check = None
        self._skip_rule_end_date = None
        self.discriminator = None

        self.name = name
        self.branch_name = branch_name
        if commit_message_regex is not None:
            self.commit_message_regex = commit_message_regex
        if commit_message_negative_regex is not None:
            self.commit_message_negative_regex = commit_message_negative_regex
        if author_regex is not None:
            self.author_regex = author_regex
        if author_email_regex is not None:
            self.author_email_regex = author_email_regex
        if prohibited_file_name_regex is not None:
            self.prohibited_file_name_regex = prohibited_file_name_regex
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if binary_gate_enabled is not None:
            self.binary_gate_enabled = binary_gate_enabled
        if allowed_modify_binary is not None:
            self.allowed_modify_binary = allowed_modify_binary
        if allowed_binary_file_name_regex is not None:
            self.allowed_binary_file_name_regex = allowed_binary_file_name_regex
        if privileged_user_ids is not None:
            self.privileged_user_ids = privileged_user_ids
        if effective_date is not None:
            self.effective_date = effective_date
        if skip_rule_check is not None:
            self.skip_rule_check = skip_rule_check
        if skip_rule_end_date is not None:
            self.skip_rule_end_date = skip_rule_end_date

    @property
    def name(self):
        r"""Gets the name of this CommitRuleUpdateBodyDto.

        **参数解释：** 规则名称。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CommitRuleUpdateBodyDto.

        **参数解释：** 规则名称。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this CommitRuleUpdateBodyDto.
        :type name: str
        """
        self._name = name

    @property
    def branch_name(self):
        r"""Gets the branch_name of this CommitRuleUpdateBodyDto.

        **参数解释：** 分支规则。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The branch_name of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this CommitRuleUpdateBodyDto.

        **参数解释：** 分支规则。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param branch_name: The branch_name of this CommitRuleUpdateBodyDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def commit_message_regex(self):
        r"""Gets the commit_message_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交信息匹配规则。 所有提交消息都必须进行正则表达式匹配， 例如: \\d+\\..*。 若符合正则匹配，则允许提交。若此字段为空，则允许任何提交消息。 您也可以设置在提交信息中必须包含工作项单号，实现代码的E2E追溯。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The commit_message_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._commit_message_regex

    @commit_message_regex.setter
    def commit_message_regex(self, commit_message_regex):
        r"""Sets the commit_message_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交信息匹配规则。 所有提交消息都必须进行正则表达式匹配， 例如: \\d+\\..*。 若符合正则匹配，则允许提交。若此字段为空，则允许任何提交消息。 您也可以设置在提交信息中必须包含工作项单号，实现代码的E2E追溯。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param commit_message_regex: The commit_message_regex of this CommitRuleUpdateBodyDto.
        :type commit_message_regex: str
        """
        self._commit_message_regex = commit_message_regex

    @property
    def commit_message_negative_regex(self):
        r"""Gets the commit_message_negative_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交信息负面匹配规则。 所有提交消息都必须进行正则表达式匹配，例如: \\d+\\..*。 符合正则匹配，则不允许提交。若此字段为空，则允许任何提交消息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The commit_message_negative_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._commit_message_negative_regex

    @commit_message_negative_regex.setter
    def commit_message_negative_regex(self, commit_message_negative_regex):
        r"""Sets the commit_message_negative_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交信息负面匹配规则。 所有提交消息都必须进行正则表达式匹配，例如: \\d+\\..*。 符合正则匹配，则不允许提交。若此字段为空，则允许任何提交消息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param commit_message_negative_regex: The commit_message_negative_regex of this CommitRuleUpdateBodyDto.
        :type commit_message_negative_regex: str
        """
        self._commit_message_negative_regex = commit_message_negative_regex

    @property
    def author_regex(self):
        r"""Gets the author_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交人的正则表达式。 提交人必须进行正则表达式匹配， 例如: /([a-zA-Z]\\d){7}/。如果此字段为空，则允许任何提交人。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The author_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._author_regex

    @author_regex.setter
    def author_regex(self, author_regex):
        r"""Sets the author_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交人的正则表达式。 提交人必须进行正则表达式匹配， 例如: /([a-zA-Z]\\d){7}/。如果此字段为空，则允许任何提交人。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param author_regex: The author_regex of this CommitRuleUpdateBodyDto.
        :type author_regex: str
        """
        self._author_regex = author_regex

    @property
    def author_email_regex(self):
        r"""Gets the author_email_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交人邮箱地址的正则表达式。 所有提交者邮箱地址都必须进行正则表达式匹配， 例如: @my-company.com$。如果此字段为空，则允许任何提交邮箱地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The author_email_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._author_email_regex

    @author_email_regex.setter
    def author_email_regex(self, author_email_regex):
        r"""Sets the author_email_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 提交人邮箱地址的正则表达式。 所有提交者邮箱地址都必须进行正则表达式匹配， 例如: @my-company.com$。如果此字段为空，则允许任何提交邮箱地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param author_email_regex: The author_email_regex of this CommitRuleUpdateBodyDto.
        :type author_email_regex: str
        """
        self._author_email_regex = author_email_regex

    @property
    def prohibited_file_name_regex(self):
        r"""Gets the prohibited_file_name_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 禁止提交的文件名称的正则表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The prohibited_file_name_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._prohibited_file_name_regex

    @prohibited_file_name_regex.setter
    def prohibited_file_name_regex(self, prohibited_file_name_regex):
        r"""Sets the prohibited_file_name_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 禁止提交的文件名称的正则表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param prohibited_file_name_regex: The prohibited_file_name_regex of this CommitRuleUpdateBodyDto.
        :type prohibited_file_name_regex: str
        """
        self._prohibited_file_name_regex = prohibited_file_name_regex

    @property
    def max_file_size(self):
        r"""Gets the max_file_size of this CommitRuleUpdateBodyDto.

        **参数解释：** 单文件大小限制（MB）。 单文件大小超过上述规格的添加或更新推送将被拒绝，Repo建议的最佳上限值为50MB。 系统支持单文件提交的最大值为300MB。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 50

        :return: The max_file_size of this CommitRuleUpdateBodyDto.
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        r"""Sets the max_file_size of this CommitRuleUpdateBodyDto.

        **参数解释：** 单文件大小限制（MB）。 单文件大小超过上述规格的添加或更新推送将被拒绝，Repo建议的最佳上限值为50MB。 系统支持单文件提交的最大值为300MB。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 50

        :param max_file_size: The max_file_size of this CommitRuleUpdateBodyDto.
        :type max_file_size: int
        """
        self._max_file_size = max_file_size

    @property
    def binary_gate_enabled(self):
        r"""Gets the binary_gate_enabled of this CommitRuleUpdateBodyDto.

        **参数解释：** 禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。 **默认取值：** 不涉及。

        :return: The binary_gate_enabled of this CommitRuleUpdateBodyDto.
        :rtype: bool
        """
        return self._binary_gate_enabled

    @binary_gate_enabled.setter
    def binary_gate_enabled(self, binary_gate_enabled):
        r"""Sets the binary_gate_enabled of this CommitRuleUpdateBodyDto.

        **参数解释：** 禁止新增二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，禁止新增二进制文件。 - false，允许新增二进制文件。 **默认取值：** 不涉及。

        :param binary_gate_enabled: The binary_gate_enabled of this CommitRuleUpdateBodyDto.
        :type binary_gate_enabled: bool
        """
        self._binary_gate_enabled = binary_gate_enabled

    @property
    def allowed_modify_binary(self):
        r"""Gets the allowed_modify_binary of this CommitRuleUpdateBodyDto.

        **参数解释：** 允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。 **默认取值：** 不涉及。

        :return: The allowed_modify_binary of this CommitRuleUpdateBodyDto.
        :rtype: bool
        """
        return self._allowed_modify_binary

    @allowed_modify_binary.setter
    def allowed_modify_binary(self, allowed_modify_binary):
        r"""Sets the allowed_modify_binary of this CommitRuleUpdateBodyDto.

        **参数解释：** 允许修改二进制文件（对特权用户无效）。 **约束限制：** 不涉及。 **取值范围：** - true，允许修改二进制文件。 - false，禁止修改二进制文件。 **默认取值：** 不涉及。

        :param allowed_modify_binary: The allowed_modify_binary of this CommitRuleUpdateBodyDto.
        :type allowed_modify_binary: bool
        """
        self._allowed_modify_binary = allowed_modify_binary

    @property
    def allowed_binary_file_name_regex(self):
        r"""Gets the allowed_binary_file_name_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 二进制文件白名单（可直接入库的文件）。 所有被推送的二进制文件名必须进行正则表达式匹配， 例如: (\\.png|\\.xls|\\.xlsx|\\.docx|\\.doc)$ 。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The allowed_binary_file_name_regex of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._allowed_binary_file_name_regex

    @allowed_binary_file_name_regex.setter
    def allowed_binary_file_name_regex(self, allowed_binary_file_name_regex):
        r"""Sets the allowed_binary_file_name_regex of this CommitRuleUpdateBodyDto.

        **参数解释：** 二进制文件白名单（可直接入库的文件）。 所有被推送的二进制文件名必须进行正则表达式匹配， 例如: (\\.png|\\.xls|\\.xlsx|\\.docx|\\.doc)$ 。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param allowed_binary_file_name_regex: The allowed_binary_file_name_regex of this CommitRuleUpdateBodyDto.
        :type allowed_binary_file_name_regex: str
        """
        self._allowed_binary_file_name_regex = allowed_binary_file_name_regex

    @property
    def privileged_user_ids(self):
        r"""Gets the privileged_user_ids of this CommitRuleUpdateBodyDto.

        **参数解释：** 特权用户ID列表（特权用户可直接推送所有二进制文件入库。 只有特权用户能推送二进制文件。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The privileged_user_ids of this CommitRuleUpdateBodyDto.
        :rtype: list[int]
        """
        return self._privileged_user_ids

    @privileged_user_ids.setter
    def privileged_user_ids(self, privileged_user_ids):
        r"""Sets the privileged_user_ids of this CommitRuleUpdateBodyDto.

        **参数解释：** 特权用户ID列表（特权用户可直接推送所有二进制文件入库。 只有特权用户能推送二进制文件。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param privileged_user_ids: The privileged_user_ids of this CommitRuleUpdateBodyDto.
        :type privileged_user_ids: list[int]
        """
        self._privileged_user_ids = privileged_user_ids

    @property
    def effective_date(self):
        r"""Gets the effective_date of this CommitRuleUpdateBodyDto.

        **参数解释：** 规则生效时间， 例如: 2025-8-19。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The effective_date of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        r"""Sets the effective_date of this CommitRuleUpdateBodyDto.

        **参数解释：** 规则生效时间， 例如: 2025-8-19。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param effective_date: The effective_date of this CommitRuleUpdateBodyDto.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def skip_rule_check(self):
        r"""Gets the skip_rule_check of this CommitRuleUpdateBodyDto.

        **参数解释：** 跳过规则检测。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The skip_rule_check of this CommitRuleUpdateBodyDto.
        :rtype: bool
        """
        return self._skip_rule_check

    @skip_rule_check.setter
    def skip_rule_check(self, skip_rule_check):
        r"""Sets the skip_rule_check of this CommitRuleUpdateBodyDto.

        **参数解释：** 跳过规则检测。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param skip_rule_check: The skip_rule_check of this CommitRuleUpdateBodyDto.
        :type skip_rule_check: bool
        """
        self._skip_rule_check = skip_rule_check

    @property
    def skip_rule_end_date(self):
        r"""Gets the skip_rule_end_date of this CommitRuleUpdateBodyDto.

        **参数解释：** 跳过规则检测失效时间， 例如: 2025-8-19 10:00:00。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The skip_rule_end_date of this CommitRuleUpdateBodyDto.
        :rtype: str
        """
        return self._skip_rule_end_date

    @skip_rule_end_date.setter
    def skip_rule_end_date(self, skip_rule_end_date):
        r"""Sets the skip_rule_end_date of this CommitRuleUpdateBodyDto.

        **参数解释：** 跳过规则检测失效时间， 例如: 2025-8-19 10:00:00。 **约束限制：** 仅CR仓库支持此参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param skip_rule_end_date: The skip_rule_end_date of this CommitRuleUpdateBodyDto.
        :type skip_rule_end_date: str
        """
        self._skip_rule_end_date = skip_rule_end_date

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
        if not isinstance(other, CommitRuleUpdateBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
