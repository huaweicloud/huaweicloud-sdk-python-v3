# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'str',
        'limit': 'str',
        'action': 'str',
        'matches': 'list[QueryMatchItem]',
        'tags': 'list[QueryTagItem]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'matches': 'matches',
        'tags': 'tags'
    }

    def __init__(self, offset=None, limit=None, action=None, matches=None, tags=None):
        r"""ListInstancesByTagsRequestBody

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 索引位置偏移量，表示从第一条数据偏移offset条数据后开始查询。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值必须为数字，不能为负数。 **取值范围：** 不涉及。 **默认取值：** 默认取0值，表示从第一条数据开始查询。
        :type offset: str
        :param limit: **参数解释：** 查询记录数。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值范围：1~100。不传该参数时，默认查询前100条实例信息。 **取值范围：** 1~100 **默认取值：** 不涉及。
        :type limit: str
        :param action: **参数解释：** 操作标识。 **约束限制：** - 取值为“count”，表示仅返回总记录数，禁止返回其他字段。 - 取值为“filter”，表示根据标签过滤条件查询实例。 **取值范围：** count和filter **默认取值：** 不涉及。
        :type action: str
        :param matches: **参数解释：** 搜索字段。 **约束限制：**   - 该字段值为空，表示不按照实例名称或实例ID查询。   - 该字段值不为空， **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type matches: list[:class:`huaweicloudsdkdds.v3.QueryMatchItem`]
        :param tags: **参数解释：** 包含标签。 **约束限制：** 最多包含10个key。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkdds.v3.QueryTagItem`]
        """
        
        

        self._offset = None
        self._limit = None
        self._action = None
        self._matches = None
        self._tags = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.action = action
        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesByTagsRequestBody.

        **参数解释：** 索引位置偏移量，表示从第一条数据偏移offset条数据后开始查询。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值必须为数字，不能为负数。 **取值范围：** 不涉及。 **默认取值：** 默认取0值，表示从第一条数据开始查询。

        :return: The offset of this ListInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesByTagsRequestBody.

        **参数解释：** 索引位置偏移量，表示从第一条数据偏移offset条数据后开始查询。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值必须为数字，不能为负数。 **取值范围：** 不涉及。 **默认取值：** 默认取0值，表示从第一条数据开始查询。

        :param offset: The offset of this ListInstancesByTagsRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesByTagsRequestBody.

        **参数解释：** 查询记录数。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值范围：1~100。不传该参数时，默认查询前100条实例信息。 **取值范围：** 1~100 **默认取值：** 不涉及。

        :return: The limit of this ListInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesByTagsRequestBody.

        **参数解释：** 查询记录数。 **约束限制：**   - “action”值为“count”时，不传该参数。   - “action”值为“filter”时，取值范围：1~100。不传该参数时，默认查询前100条实例信息。 **取值范围：** 1~100 **默认取值：** 不涉及。

        :param limit: The limit of this ListInstancesByTagsRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def action(self):
        r"""Gets the action of this ListInstancesByTagsRequestBody.

        **参数解释：** 操作标识。 **约束限制：** - 取值为“count”，表示仅返回总记录数，禁止返回其他字段。 - 取值为“filter”，表示根据标签过滤条件查询实例。 **取值范围：** count和filter **默认取值：** 不涉及。

        :return: The action of this ListInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListInstancesByTagsRequestBody.

        **参数解释：** 操作标识。 **约束限制：** - 取值为“count”，表示仅返回总记录数，禁止返回其他字段。 - 取值为“filter”，表示根据标签过滤条件查询实例。 **取值范围：** count和filter **默认取值：** 不涉及。

        :param action: The action of this ListInstancesByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        r"""Gets the matches of this ListInstancesByTagsRequestBody.

        **参数解释：** 搜索字段。 **约束限制：**   - 该字段值为空，表示不按照实例名称或实例ID查询。   - 该字段值不为空， **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The matches of this ListInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.QueryMatchItem`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListInstancesByTagsRequestBody.

        **参数解释：** 搜索字段。 **约束限制：**   - 该字段值为空，表示不按照实例名称或实例ID查询。   - 该字段值不为空， **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param matches: The matches of this ListInstancesByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkdds.v3.QueryMatchItem`]
        """
        self._matches = matches

    @property
    def tags(self):
        r"""Gets the tags of this ListInstancesByTagsRequestBody.

        **参数解释：** 包含标签。 **约束限制：** 最多包含10个key。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this ListInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.QueryTagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstancesByTagsRequestBody.

        **参数解释：** 包含标签。 **约束限制：** 最多包含10个key。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this ListInstancesByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkdds.v3.QueryTagItem`]
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
        if not isinstance(other, ListInstancesByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
