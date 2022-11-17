# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tags': 'list[Tags]',
        'tags_any': 'list[Tags]',
        'not_tags': 'list[Tags]',
        'not_tags_any': 'list[Tags]',
        'limit': 'str',
        'offset': 'str',
        'matches': 'list[TagKeyValue]',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, action=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, limit=None, offset=None, matches=None, without_any_tag=None):
        """ListImageByTagsRequestBody

        The model defined in huaweicloud sdk

        :param action: 操作标识（区分大小写），支持filter、count。filter就是分页查询；count是只需按照条件将总条数返回即可。
        :type action: str
        :param tags: 包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。
        :type tags: list[:class:`huaweicloudsdkims.v2.Tags`]
        :param tags_any: 包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不允许为空列表，但可以不传递参数。
        :type tags_any: list[:class:`huaweicloudsdkims.v2.Tags`]
        :param not_tags: 不包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。
        :type not_tags: list[:class:`huaweicloudsdkims.v2.Tags`]
        :param not_tags_any: 不包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。
        :type not_tags_any: list[:class:`huaweicloudsdkims.v2.Tags`]
        :param limit: 最大查询记录数(action为count，时此参数无效）如果action为filter默认为10，limit最多为1000，不能为负数，最小值为1。
        :type limit: str
        :param offset: 索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数（action为count时，此参数无效），如果action为filter默认为0，不能为负数。
        :type offset: str
        :param matches: 搜索字段，key为要匹配的字段，如resource_name、resource_id等。value为匹配的值。多个matches的key不允许重复。不允许为空列表，但可以不传递参数。
        :type matches: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略tag、not_tags、tags_any、not_tags_any字段。
        :type without_any_tag: bool
        """
        
        

        self._action = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._limit = None
        self._offset = None
        self._matches = None
        self._without_any_tag = None
        self.discriminator = None

        self.action = action
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
        if matches is not None:
            self.matches = matches
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def action(self):
        """Gets the action of this ListImageByTagsRequestBody.

        操作标识（区分大小写），支持filter、count。filter就是分页查询；count是只需按照条件将总条数返回即可。

        :return: The action of this ListImageByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListImageByTagsRequestBody.

        操作标识（区分大小写），支持filter、count。filter就是分页查询；count是只需按照条件将总条数返回即可。

        :param action: The action of this ListImageByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        """Gets the tags of this ListImageByTagsRequestBody.

        包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :return: The tags of this ListImageByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListImageByTagsRequestBody.

        包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :param tags: The tags of this ListImageByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListImageByTagsRequestBody.

        包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不允许为空列表，但可以不传递参数。

        :return: The tags_any of this ListImageByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListImageByTagsRequestBody.

        包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不允许为空列表，但可以不传递参数。

        :param tags_any: The tags_any of this ListImageByTagsRequestBody.
        :type tags_any: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListImageByTagsRequestBody.

        不包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :return: The not_tags of this ListImageByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListImageByTagsRequestBody.

        不包含标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :param not_tags: The not_tags of this ListImageByTagsRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListImageByTagsRequestBody.

        不包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :return: The not_tags_any of this ListImageByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListImageByTagsRequestBody.

        不包含任意标签，最多包含10个key，每个key对应的values最多包含10个值，且key和values都不能重复。不能为空列表。

        :param not_tags_any: The not_tags_any of this ListImageByTagsRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdkims.v2.Tags`]
        """
        self._not_tags_any = not_tags_any

    @property
    def limit(self):
        """Gets the limit of this ListImageByTagsRequestBody.

        最大查询记录数(action为count，时此参数无效）如果action为filter默认为10，limit最多为1000，不能为负数，最小值为1。

        :return: The limit of this ListImageByTagsRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImageByTagsRequestBody.

        最大查询记录数(action为count，时此参数无效）如果action为filter默认为10，limit最多为1000，不能为负数，最小值为1。

        :param limit: The limit of this ListImageByTagsRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListImageByTagsRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数（action为count时，此参数无效），如果action为filter默认为0，不能为负数。

        :return: The offset of this ListImageByTagsRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListImageByTagsRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数（action为count时，此参数无效），如果action为filter默认为0，不能为负数。

        :param offset: The offset of this ListImageByTagsRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def matches(self):
        """Gets the matches of this ListImageByTagsRequestBody.

        搜索字段，key为要匹配的字段，如resource_name、resource_id等。value为匹配的值。多个matches的key不允许重复。不允许为空列表，但可以不传递参数。

        :return: The matches of this ListImageByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListImageByTagsRequestBody.

        搜索字段，key为要匹配的字段，如resource_name、resource_id等。value为匹配的值。多个matches的key不允许重复。不允许为空列表，但可以不传递参数。

        :param matches: The matches of this ListImageByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkims.v2.TagKeyValue`]
        """
        self._matches = matches

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ListImageByTagsRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略tag、not_tags、tags_any、not_tags_any字段。

        :return: The without_any_tag of this ListImageByTagsRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ListImageByTagsRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略tag、not_tags、tags_any、not_tags_any字段。

        :param without_any_tag: The without_any_tag of this ListImageByTagsRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

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
        if not isinstance(other, ListImageByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
