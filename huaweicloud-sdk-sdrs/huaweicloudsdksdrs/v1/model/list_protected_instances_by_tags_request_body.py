# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectedInstancesByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagParams]',
        'tags_any': 'list[TagParams]',
        'not_tags': 'list[TagParams]',
        'not_tags_any': 'list[TagParams]',
        'limit': 'str',
        'offset': 'str',
        'action': 'str',
        'matches': 'list[MatchParams]'
    }

    attribute_map = {
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'matches': 'matches'
    }

    def __init__(self, tags=None, tags_any=None, not_tags=None, not_tags_any=None, limit=None, offset=None, action=None, matches=None):
        """ListProtectedInstancesByTagsRequestBody

        The model defined in huaweicloud sdk

        :param tags: 包含标签，最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        :param tags_any: 包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        :param not_tags: 不包含标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        :param not_tags_any: 不包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        :param limit: 查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。
        :type limit: str
        :param offset: 索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: str
        :param action: 操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。如果是filter就按照过滤条件查询，如果是count，只需要返回总条数，禁止返回其他字段。
        :type action: str
        :param matches: 搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。目前只有resource_name，后续再扩展。
        :type matches: list[:class:`huaweicloudsdksdrs.v1.MatchParams`]
        """
        
        

        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._limit = None
        self._offset = None
        self._action = None
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
        if offset is not None:
            self.offset = offset
        self.action = action
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListProtectedInstancesByTagsRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ListProtectedInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListProtectedInstancesByTagsRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListProtectedInstancesByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListProtectedInstancesByTagsRequestBody.

        包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The tags_any of this ListProtectedInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListProtectedInstancesByTagsRequestBody.

        包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this ListProtectedInstancesByTagsRequestBody.
        :type tags_any: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListProtectedInstancesByTagsRequestBody.

        不包含标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags of this ListProtectedInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListProtectedInstancesByTagsRequestBody.

        不包含标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this ListProtectedInstancesByTagsRequestBody.
        :type not_tags: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListProtectedInstancesByTagsRequestBody.

        不包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags_any of this ListProtectedInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListProtectedInstancesByTagsRequestBody.

        不包含任意标签，最多包含10个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this ListProtectedInstancesByTagsRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdksdrs.v1.TagParams`]
        """
        self._not_tags_any = not_tags_any

    @property
    def limit(self):
        """Gets the limit of this ListProtectedInstancesByTagsRequestBody.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。

        :return: The limit of this ListProtectedInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProtectedInstancesByTagsRequestBody.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。

        :param limit: The limit of this ListProtectedInstancesByTagsRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProtectedInstancesByTagsRequestBody.

        索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListProtectedInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProtectedInstancesByTagsRequestBody.

        索引位置，偏移量（action为count时无此参数）从第一条数据偏移offset条数据后开始查询，如果action为filter默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListProtectedInstancesByTagsRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ListProtectedInstancesByTagsRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。如果是filter就按照过滤条件查询，如果是count，只需要返回总条数，禁止返回其他字段。

        :return: The action of this ListProtectedInstancesByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListProtectedInstancesByTagsRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。如果是filter就按照过滤条件查询，如果是count，只需要返回总条数，禁止返回其他字段。

        :param action: The action of this ListProtectedInstancesByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListProtectedInstancesByTagsRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。目前只有resource_name，后续再扩展。

        :return: The matches of this ListProtectedInstancesByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.MatchParams`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListProtectedInstancesByTagsRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。目前只有resource_name，后续再扩展。

        :param matches: The matches of this ListProtectedInstancesByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdksdrs.v1.MatchParams`]
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
        if not isinstance(other, ListProtectedInstancesByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
