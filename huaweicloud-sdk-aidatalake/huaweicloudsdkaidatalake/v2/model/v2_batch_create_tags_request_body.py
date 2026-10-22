# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2BatchCreateTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[V2ResourceTag]',
        'sys_tags': 'list[SystemTag]'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, tags=None, sys_tags=None):
        r"""V2BatchCreateTagsRequestBody

        The model defined in huaweicloud sdk

        :param tags: **参数解释**：批量新增请求体标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 **默认取值**：不涉及。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        :param sys_tags: **参数解释**：系统标签列表，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 **约束限制**：不涉及。 
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        
        

        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def tags(self):
        r"""Gets the tags of this V2BatchCreateTagsRequestBody.

        **参数解释**：批量新增请求体标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 **默认取值**：不涉及。 

        :return: The tags of this V2BatchCreateTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this V2BatchCreateTagsRequestBody.

        **参数解释**：批量新增请求体标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 **默认取值**：不涉及。 

        :param tags: The tags of this V2BatchCreateTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this V2BatchCreateTagsRequestBody.

        **参数解释**：系统标签列表，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 **约束限制**：不涉及。 

        :return: The sys_tags of this V2BatchCreateTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this V2BatchCreateTagsRequestBody.

        **参数解释**：系统标签列表，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 **约束限制**：不涉及。 

        :param sys_tags: The sys_tags of this V2BatchCreateTagsRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, V2BatchCreateTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
