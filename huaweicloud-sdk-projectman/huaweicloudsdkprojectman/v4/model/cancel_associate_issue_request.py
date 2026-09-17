# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelAssociateIssueRequest:

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
        'attach_issue_id': 'int'
    }

    attribute_map = {
        'project_uu_id': 'projectUUId',
        'attach_project_uu_id': 'attachProjectUUId',
        'issue_id': 'issueId',
        'attach_issue_id': 'attachIssueId'
    }

    def __init__(self, project_uu_id=None, attach_project_uu_id=None, issue_id=None, attach_issue_id=None):
        r"""CancelAssociateIssueRequest

        The model defined in huaweicloud sdk

        :param project_uu_id: **参数解释**： 源项目UUID。标识执行取消关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。
        :type project_uu_id: str
        :param attach_project_uu_id: **参数解释**： 目标项目UUID。标识被取消关联工作项所属的项目;跨项目取消时必填。 **约束限制**： 32位UUID字符串。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。
        :type attach_project_uu_id: str
        :param issue_id: **参数解释**： 源工作项ID。即需要解除关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type issue_id: int
        :param attach_issue_id: **参数解释**： 待取消关联的目标工作项ID。 **约束限制**： 必须与源工作项已存在关联关系;不存在则返回错误码DEV_21_400806。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type attach_issue_id: int
        """
        
        

        self._project_uu_id = None
        self._attach_project_uu_id = None
        self._issue_id = None
        self._attach_issue_id = None
        self.discriminator = None

        self.project_uu_id = project_uu_id
        if attach_project_uu_id is not None:
            self.attach_project_uu_id = attach_project_uu_id
        self.issue_id = issue_id
        self.attach_issue_id = attach_issue_id

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this CancelAssociateIssueRequest.

        **参数解释**： 源项目UUID。标识执行取消关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :return: The project_uu_id of this CancelAssociateIssueRequest.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this CancelAssociateIssueRequest.

        **参数解释**： 源项目UUID。标识执行取消关联操作的源工作项所属项目。 **约束限制**： 32位UUID字符串,必填字段。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :param project_uu_id: The project_uu_id of this CancelAssociateIssueRequest.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def attach_project_uu_id(self):
        r"""Gets the attach_project_uu_id of this CancelAssociateIssueRequest.

        **参数解释**： 目标项目UUID。标识被取消关联工作项所属的项目;跨项目取消时必填。 **约束限制**： 32位UUID字符串。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :return: The attach_project_uu_id of this CancelAssociateIssueRequest.
        :rtype: str
        """
        return self._attach_project_uu_id

    @attach_project_uu_id.setter
    def attach_project_uu_id(self, attach_project_uu_id):
        r"""Sets the attach_project_uu_id of this CancelAssociateIssueRequest.

        **参数解释**： 目标项目UUID。标识被取消关联工作项所属的项目;跨项目取消时必填。 **约束限制**： 32位UUID字符串。 **取值范围**： 32个字符,由小写字母和数字组成。 **默认取值**： 不涉及。

        :param attach_project_uu_id: The attach_project_uu_id of this CancelAssociateIssueRequest.
        :type attach_project_uu_id: str
        """
        self._attach_project_uu_id = attach_project_uu_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this CancelAssociateIssueRequest.

        **参数解释**： 源工作项ID。即需要解除关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The issue_id of this CancelAssociateIssueRequest.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this CancelAssociateIssueRequest.

        **参数解释**： 源工作项ID。即需要解除关联关系的工作项唯一ID。 **约束限制**： 工作项必须存在且未被归档。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param issue_id: The issue_id of this CancelAssociateIssueRequest.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def attach_issue_id(self):
        r"""Gets the attach_issue_id of this CancelAssociateIssueRequest.

        **参数解释**： 待取消关联的目标工作项ID。 **约束限制**： 必须与源工作项已存在关联关系;不存在则返回错误码DEV_21_400806。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The attach_issue_id of this CancelAssociateIssueRequest.
        :rtype: int
        """
        return self._attach_issue_id

    @attach_issue_id.setter
    def attach_issue_id(self, attach_issue_id):
        r"""Sets the attach_issue_id of this CancelAssociateIssueRequest.

        **参数解释**： 待取消关联的目标工作项ID。 **约束限制**： 必须与源工作项已存在关联关系;不存在则返回错误码DEV_21_400806。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param attach_issue_id: The attach_issue_id of this CancelAssociateIssueRequest.
        :type attach_issue_id: int
        """
        self._attach_issue_id = attach_issue_id

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
        if not isinstance(other, CancelAssociateIssueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
