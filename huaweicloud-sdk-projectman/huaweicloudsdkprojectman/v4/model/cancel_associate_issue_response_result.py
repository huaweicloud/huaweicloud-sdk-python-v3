# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelAssociateIssueResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'issue_id': 'int',
        'project_id': 'int',
        'associate_type': 'str',
        'associate_issue_id': 'int',
        'associate_project_id': 'int',
        'created_on': 'datetime',
        'author_id': 'int',
        'flag': 'bool'
    }

    attribute_map = {
        'identifier': 'identifier',
        'issue_id': 'issueId',
        'project_id': 'projectId',
        'associate_type': 'associateType',
        'associate_issue_id': 'associateIssueId',
        'associate_project_id': 'associateProjectId',
        'created_on': 'createdOn',
        'author_id': 'authorId',
        'flag': 'flag'
    }

    def __init__(self, identifier=None, issue_id=None, project_id=None, associate_type=None, associate_issue_id=None, associate_project_id=None, created_on=None, author_id=None, flag=None):
        r"""CancelAssociateIssueResponseResult

        The model defined in huaweicloud sdk

        :param identifier: **参数解释**： 关联关系唯一标识。 **取值范围**： 32个字符,由小写字母和数字组成。
        :type identifier: str
        :param issue_id: **参数解释**： 源工作项ID。 **取值范围**： 不涉及。
        :type issue_id: int
        :param project_id: **参数解释**： 源项目数字ID。 **取值范围**： 不涉及。
        :type project_id: int
        :param associate_type: **参数解释**： 关联类型。 **取值范围**： - associate：关联工作项。
        :type associate_type: str
        :param associate_issue_id: **参数解释**： 被关联工作项ID。 **取值范围**： 不涉及。
        :type associate_issue_id: int
        :param associate_project_id: **参数解释**： 被关联项目数字ID。 **取值范围**： 不涉及。
        :type associate_project_id: int
        :param created_on: **参数解释**： 关联关系创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。
        :type created_on: datetime
        :param author_id: **参数解释**： 创建该关联关系的用户ID。 **取值范围**： 不涉及。
        :type author_id: int
        :param flag: **参数解释**： 关联关系有效标识。 **取值范围**： - true：关联有效。 - false：关联已失效。
        :type flag: bool
        """
        
        

        self._identifier = None
        self._issue_id = None
        self._project_id = None
        self._associate_type = None
        self._associate_issue_id = None
        self._associate_project_id = None
        self._created_on = None
        self._author_id = None
        self._flag = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if issue_id is not None:
            self.issue_id = issue_id
        if project_id is not None:
            self.project_id = project_id
        if associate_type is not None:
            self.associate_type = associate_type
        if associate_issue_id is not None:
            self.associate_issue_id = associate_issue_id
        if associate_project_id is not None:
            self.associate_project_id = associate_project_id
        if created_on is not None:
            self.created_on = created_on
        if author_id is not None:
            self.author_id = author_id
        if flag is not None:
            self.flag = flag

    @property
    def identifier(self):
        r"""Gets the identifier of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系唯一标识。 **取值范围**： 32个字符,由小写字母和数字组成。

        :return: The identifier of this CancelAssociateIssueResponseResult.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系唯一标识。 **取值范围**： 32个字符,由小写字母和数字组成。

        :param identifier: The identifier of this CancelAssociateIssueResponseResult.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 源工作项ID。 **取值范围**： 不涉及。

        :return: The issue_id of this CancelAssociateIssueResponseResult.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 源工作项ID。 **取值范围**： 不涉及。

        :param issue_id: The issue_id of this CancelAssociateIssueResponseResult.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 源项目数字ID。 **取值范围**： 不涉及。

        :return: The project_id of this CancelAssociateIssueResponseResult.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 源项目数字ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this CancelAssociateIssueResponseResult.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def associate_type(self):
        r"""Gets the associate_type of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联类型。 **取值范围**： - associate：关联工作项。

        :return: The associate_type of this CancelAssociateIssueResponseResult.
        :rtype: str
        """
        return self._associate_type

    @associate_type.setter
    def associate_type(self, associate_type):
        r"""Sets the associate_type of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联类型。 **取值范围**： - associate：关联工作项。

        :param associate_type: The associate_type of this CancelAssociateIssueResponseResult.
        :type associate_type: str
        """
        self._associate_type = associate_type

    @property
    def associate_issue_id(self):
        r"""Gets the associate_issue_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 被关联工作项ID。 **取值范围**： 不涉及。

        :return: The associate_issue_id of this CancelAssociateIssueResponseResult.
        :rtype: int
        """
        return self._associate_issue_id

    @associate_issue_id.setter
    def associate_issue_id(self, associate_issue_id):
        r"""Sets the associate_issue_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 被关联工作项ID。 **取值范围**： 不涉及。

        :param associate_issue_id: The associate_issue_id of this CancelAssociateIssueResponseResult.
        :type associate_issue_id: int
        """
        self._associate_issue_id = associate_issue_id

    @property
    def associate_project_id(self):
        r"""Gets the associate_project_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 被关联项目数字ID。 **取值范围**： 不涉及。

        :return: The associate_project_id of this CancelAssociateIssueResponseResult.
        :rtype: int
        """
        return self._associate_project_id

    @associate_project_id.setter
    def associate_project_id(self, associate_project_id):
        r"""Sets the associate_project_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 被关联项目数字ID。 **取值范围**： 不涉及。

        :param associate_project_id: The associate_project_id of this CancelAssociateIssueResponseResult.
        :type associate_project_id: int
        """
        self._associate_project_id = associate_project_id

    @property
    def created_on(self):
        r"""Gets the created_on of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。

        :return: The created_on of this CancelAssociateIssueResponseResult.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        r"""Sets the created_on of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。

        :param created_on: The created_on of this CancelAssociateIssueResponseResult.
        :type created_on: datetime
        """
        self._created_on = created_on

    @property
    def author_id(self):
        r"""Gets the author_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 创建该关联关系的用户ID。 **取值范围**： 不涉及。

        :return: The author_id of this CancelAssociateIssueResponseResult.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this CancelAssociateIssueResponseResult.

        **参数解释**： 创建该关联关系的用户ID。 **取值范围**： 不涉及。

        :param author_id: The author_id of this CancelAssociateIssueResponseResult.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def flag(self):
        r"""Gets the flag of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系有效标识。 **取值范围**： - true：关联有效。 - false：关联已失效。

        :return: The flag of this CancelAssociateIssueResponseResult.
        :rtype: bool
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this CancelAssociateIssueResponseResult.

        **参数解释**： 关联关系有效标识。 **取值范围**： - true：关联有效。 - false：关联已失效。

        :param flag: The flag of this CancelAssociateIssueResponseResult.
        :type flag: bool
        """
        self._flag = flag

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
        if not isinstance(other, CancelAssociateIssueResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
