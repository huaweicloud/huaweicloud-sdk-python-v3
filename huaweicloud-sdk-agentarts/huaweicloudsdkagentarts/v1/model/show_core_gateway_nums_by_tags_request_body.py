# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCoreGatewayNumsByTagsRequestBody:

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
        'tags': 'list[CoreGatewaysTagValuesForTMS]',
        'matches': 'list[CoreGatewaysMatchForTMS]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None):
        r"""ShowCoreGatewayNumsByTagsRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: **参数解释：** 是否查询所有不带标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略 “tags”字段； - false：返回所有资源或按“tags”、“matches”等条件过滤。 **默认取值：** false。 
        :type without_any_tag: bool
        :param tags: **参数解释：** 指定查询的资源中需要包含哪些标签，结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。 **约束限制：** 数组内key不能重复，同一个key中values不能重复，每个key对应的value可以为空数组但结构体不能缺失。 **取值范围：** 数组长度最大为20。 **默认取值：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysTagValuesForTMS`]
        :param matches: **参数解释：** 标签键值匹配字段，key为要匹配的字段。 **约束限制：** key为固定字典值，只支持resource_name，不能包含重复的key或不支持的key。支持根据value的值做前缀搜索。 **取值范围：** 数组长度最大为1。 **默认取值：** 不涉及。 
        :type matches: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysMatchForTMS`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 是否查询所有不带标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略 “tags”字段； - false：返回所有资源或按“tags”、“matches”等条件过滤。 **默认取值：** false。 

        :return: The without_any_tag of this ShowCoreGatewayNumsByTagsRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 是否查询所有不带标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略 “tags”字段； - false：返回所有资源或按“tags”、“matches”等条件过滤。 **默认取值：** false。 

        :param without_any_tag: The without_any_tag of this ShowCoreGatewayNumsByTagsRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 指定查询的资源中需要包含哪些标签，结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。 **约束限制：** 数组内key不能重复，同一个key中values不能重复，每个key对应的value可以为空数组但结构体不能缺失。 **取值范围：** 数组长度最大为20。 **默认取值：** 不涉及。 

        :return: The tags of this ShowCoreGatewayNumsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysTagValuesForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 指定查询的资源中需要包含哪些标签，结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。 **约束限制：** 数组内key不能重复，同一个key中values不能重复，每个key对应的value可以为空数组但结构体不能缺失。 **取值范围：** 数组长度最大为20。 **默认取值：** 不涉及。 

        :param tags: The tags of this ShowCoreGatewayNumsByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysTagValuesForTMS`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 标签键值匹配字段，key为要匹配的字段。 **约束限制：** key为固定字典值，只支持resource_name，不能包含重复的key或不支持的key。支持根据value的值做前缀搜索。 **取值范围：** 数组长度最大为1。 **默认取值：** 不涉及。 

        :return: The matches of this ShowCoreGatewayNumsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysMatchForTMS`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ShowCoreGatewayNumsByTagsRequestBody.

        **参数解释：** 标签键值匹配字段，key为要匹配的字段。 **约束限制：** key为固定字典值，只支持resource_name，不能包含重复的key或不支持的key。支持根据value的值做前缀搜索。 **取值范围：** 数组长度最大为1。 **默认取值：** 不涉及。 

        :param matches: The matches of this ShowCoreGatewayNumsByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewaysMatchForTMS`]
        """
        self._matches = matches

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
        if not isinstance(other, ShowCoreGatewayNumsByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
