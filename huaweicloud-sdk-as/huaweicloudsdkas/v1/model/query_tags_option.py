# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTagsOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagsMultiValue]',
        'tags_any': 'list[TagsMultiValue]',
        'not_tags': 'list[TagsMultiValue]',
        'not_tags_any': 'list[TagsMultiValue]',
        'limit': 'str',
        'marker': 'str',
        'action': 'str',
        'offset': 'str',
        'matches': 'list[Matches]'
    }

    attribute_map = {
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'limit': 'limit',
        'marker': 'marker',
        'action': 'action',
        'offset': 'offset',
        'matches': 'matches'
    }

    def __init__(self, tags=None, tags_any=None, not_tags=None, not_tags_any=None, limit=None, marker=None, action=None, offset=None, matches=None):
        r"""QueryTagsOption

        The model defined in huaweicloud sdk

        :param tags: 过滤条件，包含标签，最多包含10个Tag，结构体不能缺失。
        :type tags: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        :param tags_any: 过滤条件，包含任意标签，最多包含10个Tag。
        :type tags_any: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        :param not_tags: 过滤条件，不包含标签，最多包含10个Tag。
        :type not_tags: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        :param not_tags_any: 过滤条件，不包含任意标签，最多包含10个Tag。
        :type not_tags_any: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        :param limit: 查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000，不能为负数，最小值为1。
        :type limit: str
        :param marker: 分页位置标识（资源ID或索引位置）。
        :type marker: str
        :param action: 操作标识（仅限filter，count）：filter（过滤）：即分页查询。count（查询总条数）：按照条件将总条数返回即可。
        :type action: str
        :param offset: （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。必须为数字，不能为负数。action：count时，无此参数。action：filter时，默认为0
        :type offset: str
        :param matches: 模糊搜索字段。
        :type matches: list[:class:`huaweicloudsdkas.v1.Matches`]
        """
        
        

        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._limit = None
        self._marker = None
        self._action = None
        self._offset = None
        self._matches = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.action = action
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        r"""Gets the tags of this QueryTagsOption.

        过滤条件，包含标签，最多包含10个Tag，结构体不能缺失。

        :return: The tags of this QueryTagsOption.
        :rtype: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QueryTagsOption.

        过滤条件，包含标签，最多包含10个Tag，结构体不能缺失。

        :param tags: The tags of this QueryTagsOption.
        :type tags: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        r"""Gets the tags_any of this QueryTagsOption.

        过滤条件，包含任意标签，最多包含10个Tag。

        :return: The tags_any of this QueryTagsOption.
        :rtype: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        r"""Sets the tags_any of this QueryTagsOption.

        过滤条件，包含任意标签，最多包含10个Tag。

        :param tags_any: The tags_any of this QueryTagsOption.
        :type tags_any: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        r"""Gets the not_tags of this QueryTagsOption.

        过滤条件，不包含标签，最多包含10个Tag。

        :return: The not_tags of this QueryTagsOption.
        :rtype: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this QueryTagsOption.

        过滤条件，不包含标签，最多包含10个Tag。

        :param not_tags: The not_tags of this QueryTagsOption.
        :type not_tags: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        r"""Gets the not_tags_any of this QueryTagsOption.

        过滤条件，不包含任意标签，最多包含10个Tag。

        :return: The not_tags_any of this QueryTagsOption.
        :rtype: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        r"""Sets the not_tags_any of this QueryTagsOption.

        过滤条件，不包含任意标签，最多包含10个Tag。

        :param not_tags_any: The not_tags_any of this QueryTagsOption.
        :type not_tags_any: list[:class:`huaweicloudsdkas.v1.TagsMultiValue`]
        """
        self._not_tags_any = not_tags_any

    @property
    def limit(self):
        r"""Gets the limit of this QueryTagsOption.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000，不能为负数，最小值为1。

        :return: The limit of this QueryTagsOption.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryTagsOption.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000，不能为负数，最小值为1。

        :param limit: The limit of this QueryTagsOption.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this QueryTagsOption.

        分页位置标识（资源ID或索引位置）。

        :return: The marker of this QueryTagsOption.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this QueryTagsOption.

        分页位置标识（资源ID或索引位置）。

        :param marker: The marker of this QueryTagsOption.
        :type marker: str
        """
        self._marker = marker

    @property
    def action(self):
        r"""Gets the action of this QueryTagsOption.

        操作标识（仅限filter，count）：filter（过滤）：即分页查询。count（查询总条数）：按照条件将总条数返回即可。

        :return: The action of this QueryTagsOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this QueryTagsOption.

        操作标识（仅限filter，count）：filter（过滤）：即分页查询。count（查询总条数）：按照条件将总条数返回即可。

        :param action: The action of this QueryTagsOption.
        :type action: str
        """
        self._action = action

    @property
    def offset(self):
        r"""Gets the offset of this QueryTagsOption.

        （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。必须为数字，不能为负数。action：count时，无此参数。action：filter时，默认为0

        :return: The offset of this QueryTagsOption.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryTagsOption.

        （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。必须为数字，不能为负数。action：count时，无此参数。action：filter时，默认为0

        :param offset: The offset of this QueryTagsOption.
        :type offset: str
        """
        self._offset = offset

    @property
    def matches(self):
        r"""Gets the matches of this QueryTagsOption.

        模糊搜索字段。

        :return: The matches of this QueryTagsOption.
        :rtype: list[:class:`huaweicloudsdkas.v1.Matches`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this QueryTagsOption.

        模糊搜索字段。

        :param matches: The matches of this QueryTagsOption.
        :type matches: list[:class:`huaweicloudsdkas.v1.Matches`]
        """
        self._matches = matches

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
        if not isinstance(other, QueryTagsOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
