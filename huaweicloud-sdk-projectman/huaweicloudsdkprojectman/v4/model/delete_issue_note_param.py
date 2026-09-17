# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIssueNoteParam:

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
        'project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'projectId',
        'type': 'type'
    }

    def __init__(self, id=None, project_id=None, type=None):
        r"""DeleteIssueNoteParam

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 评论ID。标识需要删除的工作项评论唯一记录。 **约束限制**： 评论必须存在，且当前用户必须是该评论的创建者。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type id: int
        :param project_id: **参数解释**： 项目ID。标识当前评论所属的项目，用于权限校验与服务可用性校验。 **约束限制**： 32位UUID字符串，且必须与评论对应工作项所属项目保持一致。 **取值范围**： 32个字符，由小写字母和数字组成。 **默认取值**： 不涉及。
        :type project_id: str
        :param type: **参数解释**： 工作项类型。标识当前操作对应的工作项类型分类。 **约束限制**： 不涉及。 **取值范围**： - scrum：Scrum项目类型工作项 - 其他类型取值请参考实际业务定义。 **默认取值**： 不涉及。
        :type type: str
        """
        
        

        self._id = None
        self._project_id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this DeleteIssueNoteParam.

        **参数解释**： 评论ID。标识需要删除的工作项评论唯一记录。 **约束限制**： 评论必须存在，且当前用户必须是该评论的创建者。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The id of this DeleteIssueNoteParam.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteIssueNoteParam.

        **参数解释**： 评论ID。标识需要删除的工作项评论唯一记录。 **约束限制**： 评论必须存在，且当前用户必须是该评论的创建者。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param id: The id of this DeleteIssueNoteParam.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this DeleteIssueNoteParam.

        **参数解释**： 项目ID。标识当前评论所属的项目，用于权限校验与服务可用性校验。 **约束限制**： 32位UUID字符串，且必须与评论对应工作项所属项目保持一致。 **取值范围**： 32个字符，由小写字母和数字组成。 **默认取值**： 不涉及。

        :return: The project_id of this DeleteIssueNoteParam.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeleteIssueNoteParam.

        **参数解释**： 项目ID。标识当前评论所属的项目，用于权限校验与服务可用性校验。 **约束限制**： 32位UUID字符串，且必须与评论对应工作项所属项目保持一致。 **取值范围**： 32个字符，由小写字母和数字组成。 **默认取值**： 不涉及。

        :param project_id: The project_id of this DeleteIssueNoteParam.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this DeleteIssueNoteParam.

        **参数解释**： 工作项类型。标识当前操作对应的工作项类型分类。 **约束限制**： 不涉及。 **取值范围**： - scrum：Scrum项目类型工作项 - 其他类型取值请参考实际业务定义。 **默认取值**： 不涉及。

        :return: The type of this DeleteIssueNoteParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteIssueNoteParam.

        **参数解释**： 工作项类型。标识当前操作对应的工作项类型分类。 **约束限制**： 不涉及。 **取值范围**： - scrum：Scrum项目类型工作项 - 其他类型取值请参考实际业务定义。 **默认取值**： 不涉及。

        :param type: The type of this DeleteIssueNoteParam.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DeleteIssueNoteParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
