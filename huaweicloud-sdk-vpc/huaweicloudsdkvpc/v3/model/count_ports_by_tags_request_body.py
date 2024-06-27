# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountPortsByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'matches': 'list[Match]',
        'tags': 'list[ListTag]'
    }

    attribute_map = {
        'matches': 'matches',
        'tags': 'tags'
    }

    def __init__(self, matches=None, tags=None):
        """CountPortsByTagsRequestBody

        The model defined in huaweicloud sdk

        :param matches: 功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：key为固定字典值，不能包含重复的key或不支持的key，当前key仅支持resource_name
        :type matches: list[:class:`huaweicloudsdkvpc.v3.Match`]
        :param tags: 包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失 。 Key不能重复，同一个key中values不能重复。 结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        """
        
        

        self._matches = None
        self._tags = None
        self.discriminator = None

        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags

    @property
    def matches(self):
        """Gets the matches of this CountPortsByTagsRequestBody.

        功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：key为固定字典值，不能包含重复的key或不支持的key，当前key仅支持resource_name

        :return: The matches of this CountPortsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this CountPortsByTagsRequestBody.

        功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：key为固定字典值，不能包含重复的key或不支持的key，当前key仅支持resource_name

        :param matches: The matches of this CountPortsByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkvpc.v3.Match`]
        """
        self._matches = matches

    @property
    def tags(self):
        """Gets the tags of this CountPortsByTagsRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失 。 Key不能重复，同一个key中values不能重复。 结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this CountPortsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CountPortsByTagsRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失 。 Key不能重复，同一个key中values不能重复。 结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this CountPortsByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ListTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CountPortsByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
