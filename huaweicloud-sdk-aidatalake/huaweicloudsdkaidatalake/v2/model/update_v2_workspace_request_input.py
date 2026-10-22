# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2WorkspaceRequestInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'tags': 'list[V2ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, tags=None):
        r"""UpdateV2WorkspaceRequestInput

        The model defined in huaweicloud sdk

        :param name: **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param description: **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 
        :type description: str
        :param tags: **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        
        

        self._name = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this UpdateV2WorkspaceRequestInput.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this UpdateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateV2WorkspaceRequestInput.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this UpdateV2WorkspaceRequestInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateV2WorkspaceRequestInput.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :return: The description of this UpdateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2WorkspaceRequestInput.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :param description: The description of this UpdateV2WorkspaceRequestInput.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this UpdateV2WorkspaceRequestInput.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :return: The tags of this UpdateV2WorkspaceRequestInput.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateV2WorkspaceRequestInput.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :param tags: The tags of this UpdateV2WorkspaceRequestInput.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateV2WorkspaceRequestInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
