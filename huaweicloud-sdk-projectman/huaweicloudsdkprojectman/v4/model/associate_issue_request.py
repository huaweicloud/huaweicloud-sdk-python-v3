# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateIssueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uu_id': 'str',
        'attach_project_uu_id': 'str',
        'issue_id': 'int',
        'associated_issue_id_list': 'list[str]',
        'unassociated_issue_id_list': 'list[str]'
    }

    attribute_map = {
        'project_uu_id': 'projectUUId',
        'attach_project_uu_id': 'attachProjectUUId',
        'issue_id': 'issueId',
        'associated_issue_id_list': 'associatedIssueIdList',
        'unassociated_issue_id_list': 'unassociatedIssueIdList'
    }

    def __init__(self, project_uu_id=None, attach_project_uu_id=None, issue_id=None, associated_issue_id_list=None, unassociated_issue_id_list=None):
        r"""AssociateIssueRequest

        The model defined in huaweicloud sdk

        :param project_uu_id: **参数解释**： 源项目UUID。标识执行关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。
        :type project_uu_id: str
        :param attach_project_uu_id: **参数解释**： 目标项目UUID。标识待关联工作项所属的项目;跨项目关联时必填,同项目关联时可省略。 **约束限制**： 32位UUID字符串;若与projectUUId不同则视为跨项目关联。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。
        :type attach_project_uu_id: str
        :param issue_id: **参数解释**： 源工作项ID。即需要建立关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type issue_id: int
        :param associated_issue_id_list: **参数解释**： 待关联工作项ID列表。本次操作需要新增关联关系的目标工作项ID集合。 **约束限制**： 每个元素为字符串形式的工作项ID(服务端自动转换为整数);不能包含issueId自身;单工作项关联总数受系统上限约束。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type associated_issue_id_list: list[str]
        :param unassociated_issue_id_list: **参数解释**： 待取消关联工作项ID列表。本次操作需要解除关联关系的目标工作项ID集合;可在同一次请求中混合使用以支持关联关系调整。 **约束限制**： 每个元素为字符串形式的工作项ID;仅处理已存在的关联关系。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type unassociated_issue_id_list: list[str]
        """
        
        

        self._project_uu_id = None
        self._attach_project_uu_id = None
        self._issue_id = None
        self._associated_issue_id_list = None
        self._unassociated_issue_id_list = None
        self.discriminator = None

        self.project_uu_id = project_uu_id
        if attach_project_uu_id is not None:
            self.attach_project_uu_id = attach_project_uu_id
        self.issue_id = issue_id
        if associated_issue_id_list is not None:
            self.associated_issue_id_list = associated_issue_id_list
        if unassociated_issue_id_list is not None:
            self.unassociated_issue_id_list = unassociated_issue_id_list

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this AssociateIssueRequest.

        **参数解释**： 源项目UUID。标识执行关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :return: The project_uu_id of this AssociateIssueRequest.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this AssociateIssueRequest.

        **参数解释**： 源项目UUID。标识执行关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :param project_uu_id: The project_uu_id of this AssociateIssueRequest.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def attach_project_uu_id(self):
        r"""Gets the attach_project_uu_id of this AssociateIssueRequest.

        **参数解释**： 目标项目UUID。标识待关联工作项所属的项目;跨项目关联时必填,同项目关联时可省略。 **约束限制**： 32位UUID字符串;若与projectUUId不同则视为跨项目关联。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :return: The attach_project_uu_id of this AssociateIssueRequest.
        :rtype: str
        """
        return self._attach_project_uu_id

    @attach_project_uu_id.setter
    def attach_project_uu_id(self, attach_project_uu_id):
        r"""Sets the attach_project_uu_id of this AssociateIssueRequest.

        **参数解释**： 目标项目UUID。标识待关联工作项所属的项目;跨项目关联时必填,同项目关联时可省略。 **约束限制**： 32位UUID字符串;若与projectUUId不同则视为跨项目关联。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :param attach_project_uu_id: The attach_project_uu_id of this AssociateIssueRequest.
        :type attach_project_uu_id: str
        """
        self._attach_project_uu_id = attach_project_uu_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AssociateIssueRequest.

        **参数解释**： 源工作项ID。即需要建立关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The issue_id of this AssociateIssueRequest.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AssociateIssueRequest.

        **参数解释**： 源工作项ID。即需要建立关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param issue_id: The issue_id of this AssociateIssueRequest.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def associated_issue_id_list(self):
        r"""Gets the associated_issue_id_list of this AssociateIssueRequest.

        **参数解释**： 待关联工作项ID列表。本次操作需要新增关联关系的目标工作项ID集合。 **约束限制**： 每个元素为字符串形式的工作项ID(服务端自动转换为整数);不能包含issueId自身;单工作项关联总数受系统上限约束。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The associated_issue_id_list of this AssociateIssueRequest.
        :rtype: list[str]
        """
        return self._associated_issue_id_list

    @associated_issue_id_list.setter
    def associated_issue_id_list(self, associated_issue_id_list):
        r"""Sets the associated_issue_id_list of this AssociateIssueRequest.

        **参数解释**： 待关联工作项ID列表。本次操作需要新增关联关系的目标工作项ID集合。 **约束限制**： 每个元素为字符串形式的工作项ID(服务端自动转换为整数);不能包含issueId自身;单工作项关联总数受系统上限约束。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param associated_issue_id_list: The associated_issue_id_list of this AssociateIssueRequest.
        :type associated_issue_id_list: list[str]
        """
        self._associated_issue_id_list = associated_issue_id_list

    @property
    def unassociated_issue_id_list(self):
        r"""Gets the unassociated_issue_id_list of this AssociateIssueRequest.

        **参数解释**： 待取消关联工作项ID列表。本次操作需要解除关联关系的目标工作项ID集合;可在同一次请求中混合使用以支持关联关系调整。 **约束限制**： 每个元素为字符串形式的工作项ID;仅处理已存在的关联关系。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The unassociated_issue_id_list of this AssociateIssueRequest.
        :rtype: list[str]
        """
        return self._unassociated_issue_id_list

    @unassociated_issue_id_list.setter
    def unassociated_issue_id_list(self, unassociated_issue_id_list):
        r"""Sets the unassociated_issue_id_list of this AssociateIssueRequest.

        **参数解释**： 待取消关联工作项ID列表。本次操作需要解除关联关系的目标工作项ID集合;可在同一次请求中混合使用以支持关联关系调整。 **约束限制**： 每个元素为字符串形式的工作项ID;仅处理已存在的关联关系。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param unassociated_issue_id_list: The unassociated_issue_id_list of this AssociateIssueRequest.
        :type unassociated_issue_id_list: list[str]
        """
        self._unassociated_issue_id_list = unassociated_issue_id_list

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
        if not isinstance(other, AssociateIssueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
