# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefectInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defect_id': 'str',
        'defect_checker_name': 'str',
        'defect_status': 'str',
        'defect_owner': 'str',
        'rule_system_tags': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'line_number': 'str',
        'defect_content': 'str',
        'defect_level': 'str',
        'file_path': 'str',
        'created_at': 'str',
        'issue_key': 'str',
        'fragment': 'list[DefectFragmentV2]',
        'events': 'list[DefectEvents]'
    }

    attribute_map = {
        'defect_id': 'defect_id',
        'defect_checker_name': 'defect_checker_name',
        'defect_status': 'defect_status',
        'defect_owner': 'defect_owner',
        'rule_system_tags': 'rule_system_tags',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'line_number': 'line_number',
        'defect_content': 'defect_content',
        'defect_level': 'defect_level',
        'file_path': 'file_path',
        'created_at': 'created_at',
        'issue_key': 'issue_key',
        'fragment': 'fragment',
        'events': 'events'
    }

    def __init__(self, defect_id=None, defect_checker_name=None, defect_status=None, defect_owner=None, rule_system_tags=None, rule_id=None, rule_name=None, line_number=None, defect_content=None, defect_level=None, file_path=None, created_at=None, issue_key=None, fragment=None, events=None):
        r"""DefectInfoV2

        The model defined in huaweicloud sdk

        :param defect_id: **参数解释：** MergeKey，问题ID。 **取值范围：** 不涉及。
        :type defect_id: str
        :param defect_checker_name: **参数解释：** 废弃字段。 **取值范围：** 不涉及。
        :type defect_checker_name: str
        :param defect_status: **参数解释：** 问题状态。 **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)
        :type defect_status: str
        :param defect_owner: **参数解释：** 问题责任人。 **取值范围：** 不涉及。
        :type defect_owner: str
        :param rule_system_tags: **参数解释：** 标签，多个标签用逗号隔开。 **取值范围：** 不涉及。
        :type rule_system_tags: str
        :param rule_id: **参数解释：** 规则ID。 **取值范围：** 不涉及。
        :type rule_id: str
        :param rule_name: **参数解释：** 规则名称。 **取值范围：** 不涉及。
        :type rule_name: str
        :param line_number: **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。
        :type line_number: str
        :param defect_content: **参数解释：** 问题详细描述。 **取值范围：** 不涉及。
        :type defect_content: str
        :param defect_level: **参数解释：** 问题级别。 **取值范围：** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。
        :type defect_level: str
        :param file_path: **参数解释：** 问题文件路径。 **取值范围：** 不涉及。
        :type file_path: str
        :param created_at: **参数解释：** 问题发现时间。使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。
        :type created_at: str
        :param issue_key: **参数解释：** 废弃字段。 **取值范围：** 不涉及。
        :type issue_key: str
        :param fragment: **参数解释：** 代码片段内容。
        :type fragment: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectFragmentV2`]
        :param events: **参数解释：** 调用链信息。
        :type events: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        """
        
        

        self._defect_id = None
        self._defect_checker_name = None
        self._defect_status = None
        self._defect_owner = None
        self._rule_system_tags = None
        self._rule_id = None
        self._rule_name = None
        self._line_number = None
        self._defect_content = None
        self._defect_level = None
        self._file_path = None
        self._created_at = None
        self._issue_key = None
        self._fragment = None
        self._events = None
        self.discriminator = None

        if defect_id is not None:
            self.defect_id = defect_id
        if defect_checker_name is not None:
            self.defect_checker_name = defect_checker_name
        if defect_status is not None:
            self.defect_status = defect_status
        if defect_owner is not None:
            self.defect_owner = defect_owner
        if rule_system_tags is not None:
            self.rule_system_tags = rule_system_tags
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if line_number is not None:
            self.line_number = line_number
        if defect_content is not None:
            self.defect_content = defect_content
        if defect_level is not None:
            self.defect_level = defect_level
        if file_path is not None:
            self.file_path = file_path
        if created_at is not None:
            self.created_at = created_at
        if issue_key is not None:
            self.issue_key = issue_key
        if fragment is not None:
            self.fragment = fragment
        if events is not None:
            self.events = events

    @property
    def defect_id(self):
        r"""Gets the defect_id of this DefectInfoV2.

        **参数解释：** MergeKey，问题ID。 **取值范围：** 不涉及。

        :return: The defect_id of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_id

    @defect_id.setter
    def defect_id(self, defect_id):
        r"""Sets the defect_id of this DefectInfoV2.

        **参数解释：** MergeKey，问题ID。 **取值范围：** 不涉及。

        :param defect_id: The defect_id of this DefectInfoV2.
        :type defect_id: str
        """
        self._defect_id = defect_id

    @property
    def defect_checker_name(self):
        r"""Gets the defect_checker_name of this DefectInfoV2.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :return: The defect_checker_name of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_checker_name

    @defect_checker_name.setter
    def defect_checker_name(self, defect_checker_name):
        r"""Sets the defect_checker_name of this DefectInfoV2.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :param defect_checker_name: The defect_checker_name of this DefectInfoV2.
        :type defect_checker_name: str
        """
        self._defect_checker_name = defect_checker_name

    @property
    def defect_status(self):
        r"""Gets the defect_status of this DefectInfoV2.

        **参数解释：** 问题状态。 **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)

        :return: The defect_status of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_status

    @defect_status.setter
    def defect_status(self, defect_status):
        r"""Sets the defect_status of this DefectInfoV2.

        **参数解释：** 问题状态。 **取值范围：** - 0：待处理。 - 1：已解决。 - 2：已忽略。 [- 3：重新打开（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm) [- 4：待审核（需打开忽略审核开关）。](tag:fcs,hcs,hcs_sm,hcs_site,hcs_sitesm)

        :param defect_status: The defect_status of this DefectInfoV2.
        :type defect_status: str
        """
        self._defect_status = defect_status

    @property
    def defect_owner(self):
        r"""Gets the defect_owner of this DefectInfoV2.

        **参数解释：** 问题责任人。 **取值范围：** 不涉及。

        :return: The defect_owner of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_owner

    @defect_owner.setter
    def defect_owner(self, defect_owner):
        r"""Sets the defect_owner of this DefectInfoV2.

        **参数解释：** 问题责任人。 **取值范围：** 不涉及。

        :param defect_owner: The defect_owner of this DefectInfoV2.
        :type defect_owner: str
        """
        self._defect_owner = defect_owner

    @property
    def rule_system_tags(self):
        r"""Gets the rule_system_tags of this DefectInfoV2.

        **参数解释：** 标签，多个标签用逗号隔开。 **取值范围：** 不涉及。

        :return: The rule_system_tags of this DefectInfoV2.
        :rtype: str
        """
        return self._rule_system_tags

    @rule_system_tags.setter
    def rule_system_tags(self, rule_system_tags):
        r"""Sets the rule_system_tags of this DefectInfoV2.

        **参数解释：** 标签，多个标签用逗号隔开。 **取值范围：** 不涉及。

        :param rule_system_tags: The rule_system_tags of this DefectInfoV2.
        :type rule_system_tags: str
        """
        self._rule_system_tags = rule_system_tags

    @property
    def rule_id(self):
        r"""Gets the rule_id of this DefectInfoV2.

        **参数解释：** 规则ID。 **取值范围：** 不涉及。

        :return: The rule_id of this DefectInfoV2.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this DefectInfoV2.

        **参数解释：** 规则ID。 **取值范围：** 不涉及。

        :param rule_id: The rule_id of this DefectInfoV2.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this DefectInfoV2.

        **参数解释：** 规则名称。 **取值范围：** 不涉及。

        :return: The rule_name of this DefectInfoV2.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this DefectInfoV2.

        **参数解释：** 规则名称。 **取值范围：** 不涉及。

        :param rule_name: The rule_name of this DefectInfoV2.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def line_number(self):
        r"""Gets the line_number of this DefectInfoV2.

        **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。

        :return: The line_number of this DefectInfoV2.
        :rtype: str
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        r"""Sets the line_number of this DefectInfoV2.

        **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。

        :param line_number: The line_number of this DefectInfoV2.
        :type line_number: str
        """
        self._line_number = line_number

    @property
    def defect_content(self):
        r"""Gets the defect_content of this DefectInfoV2.

        **参数解释：** 问题详细描述。 **取值范围：** 不涉及。

        :return: The defect_content of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_content

    @defect_content.setter
    def defect_content(self, defect_content):
        r"""Sets the defect_content of this DefectInfoV2.

        **参数解释：** 问题详细描述。 **取值范围：** 不涉及。

        :param defect_content: The defect_content of this DefectInfoV2.
        :type defect_content: str
        """
        self._defect_content = defect_content

    @property
    def defect_level(self):
        r"""Gets the defect_level of this DefectInfoV2.

        **参数解释：** 问题级别。 **取值范围：** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。

        :return: The defect_level of this DefectInfoV2.
        :rtype: str
        """
        return self._defect_level

    @defect_level.setter
    def defect_level(self, defect_level):
        r"""Sets the defect_level of this DefectInfoV2.

        **参数解释：** 问题级别。 **取值范围：** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。

        :param defect_level: The defect_level of this DefectInfoV2.
        :type defect_level: str
        """
        self._defect_level = defect_level

    @property
    def file_path(self):
        r"""Gets the file_path of this DefectInfoV2.

        **参数解释：** 问题文件路径。 **取值范围：** 不涉及。

        :return: The file_path of this DefectInfoV2.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this DefectInfoV2.

        **参数解释：** 问题文件路径。 **取值范围：** 不涉及。

        :param file_path: The file_path of this DefectInfoV2.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def created_at(self):
        r"""Gets the created_at of this DefectInfoV2.

        **参数解释：** 问题发现时间。使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :return: The created_at of this DefectInfoV2.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DefectInfoV2.

        **参数解释：** 问题发现时间。使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。例如：2020-09-25T12:05:00Z。 **取值范围：** 不涉及。

        :param created_at: The created_at of this DefectInfoV2.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def issue_key(self):
        r"""Gets the issue_key of this DefectInfoV2.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :return: The issue_key of this DefectInfoV2.
        :rtype: str
        """
        return self._issue_key

    @issue_key.setter
    def issue_key(self, issue_key):
        r"""Sets the issue_key of this DefectInfoV2.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :param issue_key: The issue_key of this DefectInfoV2.
        :type issue_key: str
        """
        self._issue_key = issue_key

    @property
    def fragment(self):
        r"""Gets the fragment of this DefectInfoV2.

        **参数解释：** 代码片段内容。

        :return: The fragment of this DefectInfoV2.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectFragmentV2`]
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        r"""Sets the fragment of this DefectInfoV2.

        **参数解释：** 代码片段内容。

        :param fragment: The fragment of this DefectInfoV2.
        :type fragment: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectFragmentV2`]
        """
        self._fragment = fragment

    @property
    def events(self):
        r"""Gets the events of this DefectInfoV2.

        **参数解释：** 调用链信息。

        :return: The events of this DefectInfoV2.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this DefectInfoV2.

        **参数解释：** 调用链信息。

        :param events: The events of this DefectInfoV2.
        :type events: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        """
        self._events = events

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
        if not isinstance(other, DefectInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
