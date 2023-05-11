# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagValues]',
        'tags_any': 'list[TagValues]',
        'not_tags': 'list[TagValues]',
        'not_tags_any': 'list[TagValues]',
        'limit': 'int',
        'offset': 'int',
        'action': 'str',
        'matches': 'list[Match]'
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
        """ListTagReq

        The model defined in huaweicloud sdk

        :param tags: 包含标签。 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type tags: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        :param tags_any: 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type tags_any: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        :param not_tags: 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type not_tags: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        :param not_tags_any: 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。
        :type not_tags_any: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        :param limit: 每页返回的资源个数。  取值范围：1~1000  参数取值说明：  如果action为filter时，默认为1000。 如果action为count时，无此参数。
        :type limit: int
        :param offset: 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  参数取值说明： 查询第一页数据时，不需要传入此参数。 查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 如果action为filter时，默认为0，必须为数字，不能为负数。 如果action为count时，无此参数。
        :type offset: int
        :param action: 操作标识（区分大小写）。  取值范围：  filter：分页过滤查询 count：查询总条数
        :type action: str
        :param matches: key为要匹配的字段，value为匹配的值。  如果value为空字符串则精确匹配，否则模糊匹配。
        :type matches: list[:class:`huaweicloudsdkdns.v2.Match`]
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
        """Gets the tags of this ListTagReq.

        包含标签。 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The tags of this ListTagReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListTagReq.

        包含标签。 最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param tags: The tags of this ListTagReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The tags_any of this ListTagReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param tags_any: The tags_any of this ListTagReq.
        :type tags_any: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The not_tags of this ListTagReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param not_tags: The not_tags of this ListTagReq.
        :type not_tags: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :return: The not_tags_any of this ListTagReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListTagReq.

        最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。

        :param not_tags_any: The not_tags_any of this ListTagReq.
        :type not_tags_any: list[:class:`huaweicloudsdkdns.v2.TagValues`]
        """
        self._not_tags_any = not_tags_any

    @property
    def limit(self):
        """Gets the limit of this ListTagReq.

        每页返回的资源个数。  取值范围：1~1000  参数取值说明：  如果action为filter时，默认为1000。 如果action为count时，无此参数。

        :return: The limit of this ListTagReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagReq.

        每页返回的资源个数。  取值范围：1~1000  参数取值说明：  如果action为filter时，默认为1000。 如果action为count时，无此参数。

        :param limit: The limit of this ListTagReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTagReq.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  参数取值说明： 查询第一页数据时，不需要传入此参数。 查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 如果action为filter时，默认为0，必须为数字，不能为负数。 如果action为count时，无此参数。

        :return: The offset of this ListTagReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTagReq.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  参数取值说明： 查询第一页数据时，不需要传入此参数。 查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 如果action为filter时，默认为0，必须为数字，不能为负数。 如果action为count时，无此参数。

        :param offset: The offset of this ListTagReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ListTagReq.

        操作标识（区分大小写）。  取值范围：  filter：分页过滤查询 count：查询总条数

        :return: The action of this ListTagReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListTagReq.

        操作标识（区分大小写）。  取值范围：  filter：分页过滤查询 count：查询总条数

        :param action: The action of this ListTagReq.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListTagReq.

        key为要匹配的字段，value为匹配的值。  如果value为空字符串则精确匹配，否则模糊匹配。

        :return: The matches of this ListTagReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListTagReq.

        key为要匹配的字段，value为匹配的值。  如果value为空字符串则精确匹配，否则模糊匹配。

        :param matches: The matches of this ListTagReq.
        :type matches: list[:class:`huaweicloudsdkdns.v2.Match`]
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
        if not isinstance(other, ListTagReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
