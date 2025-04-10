# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[DomainTags]',
        'limit': 'int',
        'offset': 'int',
        'matches': 'list[ResourceTag]'
    }

    attribute_map = {
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches'
    }

    def __init__(self, tags=None, limit=None, offset=None, matches=None):
        r"""ListResourceInstancesRequestBody

        The model defined in huaweicloud sdk

        :param tags: 标签列表。 最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkccm.v1.DomainTags`]
        :param limit: 每页条目数量，取值如下： - 10：每页显示10条资源信息。 - 20：每页显示20条资源信息。 - 50：每页显示50条资源信息。
        :type limit: int
        :param offset: 索引位置，偏移量，从offset指定的下一条数据开始查询。
        :type offset: int
        :param matches: 搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。
        :type matches: list[:class:`huaweicloudsdkccm.v1.ResourceTag`]
        """
        
        

        self._tags = None
        self._limit = None
        self._offset = None
        self._matches = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        r"""Gets the tags of this ListResourceInstancesRequestBody.

        标签列表。 最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ListResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkccm.v1.DomainTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListResourceInstancesRequestBody.

        标签列表。 最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListResourceInstancesRequestBody.
        :type tags: list[:class:`huaweicloudsdkccm.v1.DomainTags`]
        """
        self._tags = tags

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceInstancesRequestBody.

        每页条目数量，取值如下： - 10：每页显示10条资源信息。 - 20：每页显示20条资源信息。 - 50：每页显示50条资源信息。

        :return: The limit of this ListResourceInstancesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceInstancesRequestBody.

        每页条目数量，取值如下： - 10：每页显示10条资源信息。 - 20：每页显示20条资源信息。 - 50：每页显示50条资源信息。

        :param limit: The limit of this ListResourceInstancesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceInstancesRequestBody.

        索引位置，偏移量，从offset指定的下一条数据开始查询。

        :return: The offset of this ListResourceInstancesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceInstancesRequestBody.

        索引位置，偏移量，从offset指定的下一条数据开始查询。

        :param offset: The offset of this ListResourceInstancesRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def matches(self):
        r"""Gets the matches of this ListResourceInstancesRequestBody.

        搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。

        :return: The matches of this ListResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkccm.v1.ResourceTag`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListResourceInstancesRequestBody.

        搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。

        :param matches: The matches of this ListResourceInstancesRequestBody.
        :type matches: list[:class:`huaweicloudsdkccm.v1.ResourceTag`]
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
        if not isinstance(other, ListResourceInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
