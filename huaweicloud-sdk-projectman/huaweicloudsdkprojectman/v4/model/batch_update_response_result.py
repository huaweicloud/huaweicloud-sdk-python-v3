# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project': 'BatchUpdateResponseResultProject',
        'journal_ids': 'list[str]',
        'error_issues': 'list[int]',
        'versions_issues': 'list[str]',
        'success_issues': 'list[str]'
    }

    attribute_map = {
        'project': 'project',
        'journal_ids': 'journal_ids',
        'error_issues': 'error_issues',
        'versions_issues': 'versions_issues',
        'success_issues': 'success_issues'
    }

    def __init__(self, project=None, journal_ids=None, error_issues=None, versions_issues=None, success_issues=None):
        r"""BatchUpdateResponseResult

        The model defined in huaweicloud sdk

        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.BatchUpdateResponseResultProject`
        :param journal_ids: **参数解释：** 历史记录id。 **取值范围：** 不涉及。
        :type journal_ids: list[str]
        :param error_issues: **参数解释：** 编辑失败的工作项。 **取值范围：** 不涉及。
        :type error_issues: list[int]
        :param versions_issues: **参数解释：** 工作项的迭代版本。 **取值范围：** 不涉及。
        :type versions_issues: list[str]
        :param success_issues: **参数解释：** 编辑成功的工作项。 **取值范围：** 不涉及。
        :type success_issues: list[str]
        """
        
        

        self._project = None
        self._journal_ids = None
        self._error_issues = None
        self._versions_issues = None
        self._success_issues = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if journal_ids is not None:
            self.journal_ids = journal_ids
        if error_issues is not None:
            self.error_issues = error_issues
        if versions_issues is not None:
            self.versions_issues = versions_issues
        if success_issues is not None:
            self.success_issues = success_issues

    @property
    def project(self):
        r"""Gets the project of this BatchUpdateResponseResult.

        :return: The project of this BatchUpdateResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchUpdateResponseResultProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this BatchUpdateResponseResult.

        :param project: The project of this BatchUpdateResponseResult.
        :type project: :class:`huaweicloudsdkprojectman.v4.BatchUpdateResponseResultProject`
        """
        self._project = project

    @property
    def journal_ids(self):
        r"""Gets the journal_ids of this BatchUpdateResponseResult.

        **参数解释：** 历史记录id。 **取值范围：** 不涉及。

        :return: The journal_ids of this BatchUpdateResponseResult.
        :rtype: list[str]
        """
        return self._journal_ids

    @journal_ids.setter
    def journal_ids(self, journal_ids):
        r"""Sets the journal_ids of this BatchUpdateResponseResult.

        **参数解释：** 历史记录id。 **取值范围：** 不涉及。

        :param journal_ids: The journal_ids of this BatchUpdateResponseResult.
        :type journal_ids: list[str]
        """
        self._journal_ids = journal_ids

    @property
    def error_issues(self):
        r"""Gets the error_issues of this BatchUpdateResponseResult.

        **参数解释：** 编辑失败的工作项。 **取值范围：** 不涉及。

        :return: The error_issues of this BatchUpdateResponseResult.
        :rtype: list[int]
        """
        return self._error_issues

    @error_issues.setter
    def error_issues(self, error_issues):
        r"""Sets the error_issues of this BatchUpdateResponseResult.

        **参数解释：** 编辑失败的工作项。 **取值范围：** 不涉及。

        :param error_issues: The error_issues of this BatchUpdateResponseResult.
        :type error_issues: list[int]
        """
        self._error_issues = error_issues

    @property
    def versions_issues(self):
        r"""Gets the versions_issues of this BatchUpdateResponseResult.

        **参数解释：** 工作项的迭代版本。 **取值范围：** 不涉及。

        :return: The versions_issues of this BatchUpdateResponseResult.
        :rtype: list[str]
        """
        return self._versions_issues

    @versions_issues.setter
    def versions_issues(self, versions_issues):
        r"""Sets the versions_issues of this BatchUpdateResponseResult.

        **参数解释：** 工作项的迭代版本。 **取值范围：** 不涉及。

        :param versions_issues: The versions_issues of this BatchUpdateResponseResult.
        :type versions_issues: list[str]
        """
        self._versions_issues = versions_issues

    @property
    def success_issues(self):
        r"""Gets the success_issues of this BatchUpdateResponseResult.

        **参数解释：** 编辑成功的工作项。 **取值范围：** 不涉及。

        :return: The success_issues of this BatchUpdateResponseResult.
        :rtype: list[str]
        """
        return self._success_issues

    @success_issues.setter
    def success_issues(self, success_issues):
        r"""Sets the success_issues of this BatchUpdateResponseResult.

        **参数解释：** 编辑成功的工作项。 **取值范围：** 不涉及。

        :param success_issues: The success_issues of this BatchUpdateResponseResult.
        :type success_issues: list[str]
        """
        self._success_issues = success_issues

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
        if not isinstance(other, BatchUpdateResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
