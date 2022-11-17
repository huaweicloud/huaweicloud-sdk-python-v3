# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipsByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagReq]',
        'limit': 'int',
        'offset': 'int',
        'action': 'str',
        'matches': 'list[MatchReq]'
    }

    attribute_map = {
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'matches': 'matches'
    }

    def __init__(self, tags=None, limit=None, offset=None, action=None, matches=None):
        """ListPublicipsByTagsRequestBody

        The model defined in huaweicloud sdk

        :param tags: 包含标签，最多包含10个key。  每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。  Key不能重复，同一个key中values不能重复。
        :type tags: list[:class:`huaweicloudsdkeip.v2.TagReq`]
        :param limit: 查询记录数（action为count时无此参数）
        :type limit: int
        :param offset: 索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）
        :type offset: int
        :param action: 操作标识：  filter分页查询  count查询总数
        :type action: str
        :param matches: 搜索字段，key为要匹配的字段，当前仅支持resource_name。value为匹配的值。此字段为固定字典值。
        :type matches: list[:class:`huaweicloudsdkeip.v2.MatchReq`]
        """
        
        

        self._tags = None
        self._limit = None
        self._offset = None
        self._action = None
        self._matches = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.action = action
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListPublicipsByTagsRequestBody.

        包含标签，最多包含10个key。  每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。  Key不能重复，同一个key中values不能重复。

        :return: The tags of this ListPublicipsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkeip.v2.TagReq`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListPublicipsByTagsRequestBody.

        包含标签，最多包含10个key。  每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。  Key不能重复，同一个key中values不能重复。

        :param tags: The tags of this ListPublicipsByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkeip.v2.TagReq`]
        """
        self._tags = tags

    @property
    def limit(self):
        """Gets the limit of this ListPublicipsByTagsRequestBody.

        查询记录数（action为count时无此参数）

        :return: The limit of this ListPublicipsByTagsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicipsByTagsRequestBody.

        查询记录数（action为count时无此参数）

        :param limit: The limit of this ListPublicipsByTagsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPublicipsByTagsRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）

        :return: The offset of this ListPublicipsByTagsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublicipsByTagsRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）

        :param offset: The offset of this ListPublicipsByTagsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ListPublicipsByTagsRequestBody.

        操作标识：  filter分页查询  count查询总数

        :return: The action of this ListPublicipsByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListPublicipsByTagsRequestBody.

        操作标识：  filter分页查询  count查询总数

        :param action: The action of this ListPublicipsByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListPublicipsByTagsRequestBody.

        搜索字段，key为要匹配的字段，当前仅支持resource_name。value为匹配的值。此字段为固定字典值。

        :return: The matches of this ListPublicipsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkeip.v2.MatchReq`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListPublicipsByTagsRequestBody.

        搜索字段，key为要匹配的字段，当前仅支持resource_name。value为匹配的值。此字段为固定字典值。

        :param matches: The matches of this ListPublicipsByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkeip.v2.MatchReq`]
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
        if not isinstance(other, ListPublicipsByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
