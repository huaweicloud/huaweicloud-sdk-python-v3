# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDocRequestDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str',
        'title': 'str',
        'instance_id': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'document_id': 'document_id',
        'title': 'title',
        'instance_id': 'instance_id',
        'modifier': 'modifier'
    }

    def __init__(self, document_id=None, title=None, instance_id=None, modifier=None):
        r"""UpdateDocRequestDto

        The model defined in huaweicloud sdk

        :param document_id: **参数解释**：  kooPage文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type document_id: str
        :param title: **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type title: str
        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param modifier: **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._document_id = None
        self._title = None
        self._instance_id = None
        self._modifier = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if title is not None:
            self.title = title
        if instance_id is not None:
            self.instance_id = instance_id
        if modifier is not None:
            self.modifier = modifier

    @property
    def document_id(self):
        r"""Gets the document_id of this UpdateDocRequestDto.

        **参数解释**：  kooPage文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The document_id of this UpdateDocRequestDto.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this UpdateDocRequestDto.

        **参数解释**：  kooPage文档ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param document_id: The document_id of this UpdateDocRequestDto.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def title(self):
        r"""Gets the title of this UpdateDocRequestDto.

        **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The title of this UpdateDocRequestDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UpdateDocRequestDto.

        **参数解释**：  文档标题。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param title: The title of this UpdateDocRequestDto.
        :type title: str
        """
        self._title = title

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateDocRequestDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this UpdateDocRequestDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateDocRequestDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this UpdateDocRequestDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def modifier(self):
        r"""Gets the modifier of this UpdateDocRequestDto.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this UpdateDocRequestDto.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this UpdateDocRequestDto.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this UpdateDocRequestDto.
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
        if not isinstance(other, UpdateDocRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
