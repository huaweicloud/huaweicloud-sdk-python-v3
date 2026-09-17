# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddCommentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'notes': 'str',
        'inner_text': 'str',
        'project_uu_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'notes': 'notes',
        'inner_text': 'innerText',
        'project_uu_id': 'projectUUId',
        'type': 'type'
    }

    def __init__(self, id=None, notes=None, inner_text=None, project_uu_id=None, type=None):
        r"""AddCommentsRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。
        :type id: str
        :param notes: **参数解释：** 工作项的URL编码后的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type notes: str
        :param inner_text: **参数解释：** 工作项的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type inner_text: str
        :param project_uu_id: **参数解释**： 项目的32位uuid。 **约束限制**： 由数字和英文组成的32字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_uu_id: str
        :param type: **参数解释**： 工作项所属项目类型。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。
        :type type: str
        """
        
        

        self._id = None
        self._notes = None
        self._inner_text = None
        self._project_uu_id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.notes = notes
        if inner_text is not None:
            self.inner_text = inner_text
        if project_uu_id is not None:
            self.project_uu_id = project_uu_id
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this AddCommentsRequest.

        **参数解释：** 工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :return: The id of this AddCommentsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddCommentsRequest.

        **参数解释：** 工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :param id: The id of this AddCommentsRequest.
        :type id: str
        """
        self._id = id

    @property
    def notes(self):
        r"""Gets the notes of this AddCommentsRequest.

        **参数解释：** 工作项的URL编码后的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The notes of this AddCommentsRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this AddCommentsRequest.

        **参数解释：** 工作项的URL编码后的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param notes: The notes of this AddCommentsRequest.
        :type notes: str
        """
        self._notes = notes

    @property
    def inner_text(self):
        r"""Gets the inner_text of this AddCommentsRequest.

        **参数解释：** 工作项的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The inner_text of this AddCommentsRequest.
        :rtype: str
        """
        return self._inner_text

    @inner_text.setter
    def inner_text(self, inner_text):
        r"""Sets the inner_text of this AddCommentsRequest.

        **参数解释：** 工作项的评论内容。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param inner_text: The inner_text of this AddCommentsRequest.
        :type inner_text: str
        """
        self._inner_text = inner_text

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this AddCommentsRequest.

        **参数解释**： 项目的32位uuid。 **约束限制**： 由数字和英文组成的32字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_uu_id of this AddCommentsRequest.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this AddCommentsRequest.

        **参数解释**： 项目的32位uuid。 **约束限制**： 由数字和英文组成的32字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_uu_id: The project_uu_id of this AddCommentsRequest.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def type(self):
        r"""Gets the type of this AddCommentsRequest.

        **参数解释**： 工作项所属项目类型。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。

        :return: The type of this AddCommentsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddCommentsRequest.

        **参数解释**： 工作项所属项目类型。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。

        :param type: The type of this AddCommentsRequest.
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
        if not isinstance(other, AddCommentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
