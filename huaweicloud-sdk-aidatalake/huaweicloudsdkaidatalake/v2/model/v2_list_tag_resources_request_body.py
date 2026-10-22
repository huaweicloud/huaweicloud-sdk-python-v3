# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2ListTagResourcesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[V2ResourceTagParam]',
        'matches': 'list[V2TagMatch]',
        'sys_tags': 'list[V2SystemTagParam]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None, sys_tags=None):
        r"""V2ListTagResourcesRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: **参数解释**：不包含任意一个标签。 **约束限制**：不涉及。 **取值范围**：   - true：查询不包含任意一个标签的资源，此时忽略“tags”过滤字段。   - false：该条件不生效，即返回所有资源或按“tags”，“matches”等条件过滤。 **默认取值**：不涉及。 
        :type without_any_tag: bool
        :param tags: **参数解释**：包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。 **约束限制**：最大数量为20个。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTagParam`]
        :param matches: **参数解释**：前缀搜索字段。key为固定字典值，当前只支持resource_name，表示基于资源名称前缀搜索。value为匹配的值。 **约束限制**：不涉及。 
        :type matches: list[:class:`huaweicloudsdkaidatalake.v2.V2TagMatch`]
        :param sys_tags: **参数解释**：系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。 **约束限制**：不涉及。 
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.V2SystemTagParam`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self._sys_tags = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this V2ListTagResourcesRequestBody.

        **参数解释**：不包含任意一个标签。 **约束限制**：不涉及。 **取值范围**：   - true：查询不包含任意一个标签的资源，此时忽略“tags”过滤字段。   - false：该条件不生效，即返回所有资源或按“tags”，“matches”等条件过滤。 **默认取值**：不涉及。 

        :return: The without_any_tag of this V2ListTagResourcesRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this V2ListTagResourcesRequestBody.

        **参数解释**：不包含任意一个标签。 **约束限制**：不涉及。 **取值范围**：   - true：查询不包含任意一个标签的资源，此时忽略“tags”过滤字段。   - false：该条件不生效，即返回所有资源或按“tags”，“matches”等条件过滤。 **默认取值**：不涉及。 

        :param without_any_tag: The without_any_tag of this V2ListTagResourcesRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this V2ListTagResourcesRequestBody.

        **参数解释**：包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。 **约束限制**：最大数量为20个。 

        :return: The tags of this V2ListTagResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTagParam`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this V2ListTagResourcesRequestBody.

        **参数解释**：包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。 **约束限制**：最大数量为20个。 

        :param tags: The tags of this V2ListTagResourcesRequestBody.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTagParam`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this V2ListTagResourcesRequestBody.

        **参数解释**：前缀搜索字段。key为固定字典值，当前只支持resource_name，表示基于资源名称前缀搜索。value为匹配的值。 **约束限制**：不涉及。 

        :return: The matches of this V2ListTagResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2TagMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this V2ListTagResourcesRequestBody.

        **参数解释**：前缀搜索字段。key为固定字典值，当前只支持resource_name，表示基于资源名称前缀搜索。value为匹配的值。 **约束限制**：不涉及。 

        :param matches: The matches of this V2ListTagResourcesRequestBody.
        :type matches: list[:class:`huaweicloudsdkaidatalake.v2.V2TagMatch`]
        """
        self._matches = matches

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this V2ListTagResourcesRequestBody.

        **参数解释**：系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。 **约束限制**：不涉及。 

        :return: The sys_tags of this V2ListTagResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2SystemTagParam`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this V2ListTagResourcesRequestBody.

        **参数解释**：系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。 **约束限制**：不涉及。 

        :param sys_tags: The sys_tags of this V2ListTagResourcesRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.V2SystemTagParam`]
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
        if not isinstance(other, V2ListTagResourcesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
