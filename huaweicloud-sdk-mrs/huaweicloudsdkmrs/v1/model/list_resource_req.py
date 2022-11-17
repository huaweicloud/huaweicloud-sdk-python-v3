# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagWithMultiValue]',
        'tags_any': 'list[TagWithMultiValue]',
        'not_tags': 'list[TagWithMultiValue]',
        'not_tags_any': 'list[TagWithMultiValue]',
        'action': 'str',
        'limit': 'int',
        'offset': 'int',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches'
    }

    def __init__(self, tags=None, tags_any=None, not_tags=None, not_tags_any=None, action=None, limit=None, offset=None, matches=None):
        """ListResourceReq

        The model defined in huaweicloud sdk

        :param tags: 返回结果包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。
        :type tags: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        :param tags_any: 返回结果包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type tags_any: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        :param not_tags: 返回结果不包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type not_tags: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        :param not_tags_any: 返回结果不包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type not_tags_any: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        :param action: 操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。  如果是filter则为分页查询，如果是count会按照条件将总条数返回。
        :type action: str
        :param limit: 查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。
        :type limit: int
        :param offset: （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数。
        :type offset: int
        :param matches: 搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索，如果value为空字符串精确匹配。
        :type matches: list[:class:`huaweicloudsdkmrs.v1.Match`]
        """
        
        

        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._action = None
        self._limit = None
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
        self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListResourceReq.

        返回结果包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。

        :return: The tags of this ListResourceReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListResourceReq.

        返回结果包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。

        :param tags: The tags of this ListResourceReq.
        :type tags: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListResourceReq.

        返回结果包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The tags_any of this ListResourceReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListResourceReq.

        返回结果包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param tags_any: The tags_any of this ListResourceReq.
        :type tags_any: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListResourceReq.

        返回结果不包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The not_tags of this ListResourceReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListResourceReq.

        返回结果不包含该参数中所有标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param not_tags: The not_tags of this ListResourceReq.
        :type not_tags: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListResourceReq.

        返回结果不包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The not_tags_any of this ListResourceReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListResourceReq.

        返回结果不包含该参数中任意一个标签对应的资源，该参数最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param not_tags_any: The not_tags_any of this ListResourceReq.
        :type not_tags_any: list[:class:`huaweicloudsdkmrs.v1.TagWithMultiValue`]
        """
        self._not_tags_any = not_tags_any

    @property
    def action(self):
        """Gets the action of this ListResourceReq.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。  如果是filter则为分页查询，如果是count会按照条件将总条数返回。

        :return: The action of this ListResourceReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListResourceReq.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。  如果是filter则为分页查询，如果是count会按照条件将总条数返回。

        :param action: The action of this ListResourceReq.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        """Gets the limit of this ListResourceReq.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。

        :return: The limit of this ListResourceReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceReq.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1。

        :param limit: The limit of this ListResourceReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListResourceReq.

        （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数。

        :return: The offset of this ListResourceReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourceReq.

        （索引位置），从offset指定的下一条数据开始查询。查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数。

        :param offset: The offset of this ListResourceReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def matches(self):
        """Gets the matches of this ListResourceReq.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索，如果value为空字符串精确匹配。

        :return: The matches of this ListResourceReq.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListResourceReq.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索，如果value为空字符串精确匹配。

        :param matches: The matches of this ListResourceReq.
        :type matches: list[:class:`huaweicloudsdkmrs.v1.Match`]
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
        if not isinstance(other, ListResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
