# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'attachment_id': 'str',
        'comment': 'str',
        'comment_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'attachment_id': 'attachment_id',
        'comment': 'comment',
        'comment_id': 'comment_id'
    }

    def __init__(self, action=None, attachment_id=None, comment=None, comment_id=None):
        r"""ModifyTaskInfo

        The model defined in huaweicloud sdk

        :param action: **参数解释**: 更新的待办动作 - TERMINATE 终止待办 - CONTINUE 继续执行 - ADD_COMMENT 添加评论 - DELETE_COMMENT 删除评论  - ADD_ATTACHMENT 添加附件 - DELETE_ATTACHMENT 删除附件   **约束限制**: - TERMINATE 不涉及 - CONTINUE 不涉及 - ADD_COMMENT 需要和请求参数comment配合使用 - DELETE_COMMENT 需要和请求参数comment_id配合使用  - ADD_ATTACHMENT 需要和请求参数attachment_id配合使用 - DELETE_ATTACHMENT 需要和请求参数attachment_id配合使用    **取值范围**: - TERMINATE - CONTINUE - ADD_COMMENT - DELETE_COMMENT  - ADD_ATTACHMENT - DELETE_ATTACHMENT  **默认值**:  ADD_ATTACHMENT 添加评论
        :type action: str
        :param attachment_id: 附件id
        :type attachment_id: str
        :param comment: 待办评论内容
        :type comment: str
        :param comment_id: 待办评论id
        :type comment_id: str
        """
        
        

        self._action = None
        self._attachment_id = None
        self._comment = None
        self._comment_id = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if comment is not None:
            self.comment = comment
        if comment_id is not None:
            self.comment_id = comment_id

    @property
    def action(self):
        r"""Gets the action of this ModifyTaskInfo.

        **参数解释**: 更新的待办动作 - TERMINATE 终止待办 - CONTINUE 继续执行 - ADD_COMMENT 添加评论 - DELETE_COMMENT 删除评论  - ADD_ATTACHMENT 添加附件 - DELETE_ATTACHMENT 删除附件   **约束限制**: - TERMINATE 不涉及 - CONTINUE 不涉及 - ADD_COMMENT 需要和请求参数comment配合使用 - DELETE_COMMENT 需要和请求参数comment_id配合使用  - ADD_ATTACHMENT 需要和请求参数attachment_id配合使用 - DELETE_ATTACHMENT 需要和请求参数attachment_id配合使用    **取值范围**: - TERMINATE - CONTINUE - ADD_COMMENT - DELETE_COMMENT  - ADD_ATTACHMENT - DELETE_ATTACHMENT  **默认值**:  ADD_ATTACHMENT 添加评论

        :return: The action of this ModifyTaskInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ModifyTaskInfo.

        **参数解释**: 更新的待办动作 - TERMINATE 终止待办 - CONTINUE 继续执行 - ADD_COMMENT 添加评论 - DELETE_COMMENT 删除评论  - ADD_ATTACHMENT 添加附件 - DELETE_ATTACHMENT 删除附件   **约束限制**: - TERMINATE 不涉及 - CONTINUE 不涉及 - ADD_COMMENT 需要和请求参数comment配合使用 - DELETE_COMMENT 需要和请求参数comment_id配合使用  - ADD_ATTACHMENT 需要和请求参数attachment_id配合使用 - DELETE_ATTACHMENT 需要和请求参数attachment_id配合使用    **取值范围**: - TERMINATE - CONTINUE - ADD_COMMENT - DELETE_COMMENT  - ADD_ATTACHMENT - DELETE_ATTACHMENT  **默认值**:  ADD_ATTACHMENT 添加评论

        :param action: The action of this ModifyTaskInfo.
        :type action: str
        """
        self._action = action

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this ModifyTaskInfo.

        附件id

        :return: The attachment_id of this ModifyTaskInfo.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this ModifyTaskInfo.

        附件id

        :param attachment_id: The attachment_id of this ModifyTaskInfo.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def comment(self):
        r"""Gets the comment of this ModifyTaskInfo.

        待办评论内容

        :return: The comment of this ModifyTaskInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ModifyTaskInfo.

        待办评论内容

        :param comment: The comment of this ModifyTaskInfo.
        :type comment: str
        """
        self._comment = comment

    @property
    def comment_id(self):
        r"""Gets the comment_id of this ModifyTaskInfo.

        待办评论id

        :return: The comment_id of this ModifyTaskInfo.
        :rtype: str
        """
        return self._comment_id

    @comment_id.setter
    def comment_id(self, comment_id):
        r"""Sets the comment_id of this ModifyTaskInfo.

        待办评论id

        :param comment_id: The comment_id of this ModifyTaskInfo.
        :type comment_id: str
        """
        self._comment_id = comment_id

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
        if not isinstance(other, ModifyTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
