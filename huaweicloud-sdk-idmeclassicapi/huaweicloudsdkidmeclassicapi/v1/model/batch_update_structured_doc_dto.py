# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateStructuredDocDto:

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
        'title': 'str',
        'template_id': 'str',
        'organization_id': 'str',
        'wiki_id': 'str',
        'parent_document_id': 'str',
        'instance_id': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'template_id': 'template_id',
        'organization_id': 'organization_id',
        'wiki_id': 'wiki_id',
        'parent_document_id': 'parent_document_id',
        'instance_id': 'instance_id',
        'modifier': 'modifier'
    }

    def __init__(self, id=None, title=None, template_id=None, organization_id=None, wiki_id=None, parent_document_id=None, instance_id=None, modifier=None):
        r"""BatchUpdateStructuredDocDto

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type id: str
        :param title: **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type title: str
        :param template_id: **参数解释**：  模板ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type template_id: str
        :param organization_id: **参数解释**：  团队ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type organization_id: str
        :param wiki_id: **参数解释**：  知识库ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type wiki_id: str
        :param parent_document_id: **参数解释**：  父文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type parent_document_id: str
        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param modifier: **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type modifier: str
        """
        
        

        self._id = None
        self._title = None
        self._template_id = None
        self._organization_id = None
        self._wiki_id = None
        self._parent_document_id = None
        self._instance_id = None
        self._modifier = None
        self.discriminator = None

        self.id = id
        if title is not None:
            self.title = title
        if template_id is not None:
            self.template_id = template_id
        if organization_id is not None:
            self.organization_id = organization_id
        if wiki_id is not None:
            self.wiki_id = wiki_id
        if parent_document_id is not None:
            self.parent_document_id = parent_document_id
        if instance_id is not None:
            self.instance_id = instance_id
        if modifier is not None:
            self.modifier = modifier

    @property
    def id(self):
        r"""Gets the id of this BatchUpdateStructuredDocDto.

        **参数解释**：  文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateStructuredDocDto.

        **参数解释**：  文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param id: The id of this BatchUpdateStructuredDocDto.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this BatchUpdateStructuredDocDto.

        **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The title of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this BatchUpdateStructuredDocDto.

        **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param title: The title of this BatchUpdateStructuredDocDto.
        :type title: str
        """
        self._title = title

    @property
    def template_id(self):
        r"""Gets the template_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  模板ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The template_id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  模板ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param template_id: The template_id of this BatchUpdateStructuredDocDto.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  团队ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The organization_id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  团队ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param organization_id: The organization_id of this BatchUpdateStructuredDocDto.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def wiki_id(self):
        r"""Gets the wiki_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  知识库ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The wiki_id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._wiki_id

    @wiki_id.setter
    def wiki_id(self, wiki_id):
        r"""Sets the wiki_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  知识库ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param wiki_id: The wiki_id of this BatchUpdateStructuredDocDto.
        :type wiki_id: str
        """
        self._wiki_id = wiki_id

    @property
    def parent_document_id(self):
        r"""Gets the parent_document_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  父文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The parent_document_id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._parent_document_id

    @parent_document_id.setter
    def parent_document_id(self, parent_document_id):
        r"""Sets the parent_document_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  父文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param parent_document_id: The parent_document_id of this BatchUpdateStructuredDocDto.
        :type parent_document_id: str
        """
        self._parent_document_id = parent_document_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchUpdateStructuredDocDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this BatchUpdateStructuredDocDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def modifier(self):
        r"""Gets the modifier of this BatchUpdateStructuredDocDto.

        **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The modifier of this BatchUpdateStructuredDocDto.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this BatchUpdateStructuredDocDto.

        **参数解释**：  修改人。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param modifier: The modifier of this BatchUpdateStructuredDocDto.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, BatchUpdateStructuredDocDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
