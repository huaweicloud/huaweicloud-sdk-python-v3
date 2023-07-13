# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInstanceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'matches': 'list[ResourceInstanceTagRequestMatches]',
        'not_tags': 'list[TagKeyValuesBean]',
        'tags': 'list[TagKeyValuesBean]',
        'tags_any': 'list[TagKeyValuesBean]',
        'not_tags_any': 'list[TagKeyValuesBean]',
        'sys_tags': 'TagKeyValuesBean',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'matches': 'matches',
        'not_tags': 'not_tags',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags_any': 'not_tags_any',
        'sys_tags': 'sys_tags',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, matches=None, not_tags=None, tags=None, tags_any=None, not_tags_any=None, sys_tags=None, without_any_tag=None):
        """ResourceInstanceTagRequest

        The model defined in huaweicloud sdk

        :param matches: 搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。 根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。resource_id为精确匹配。第一期只做resource_name，后续再扩展。
        :type matches: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceTagRequestMatches`]
        :param not_tags: 不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据
        :type not_tags: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        :param tags: 包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据
        :type tags: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        :param tags_any: 包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据
        :type tags_any: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        :param not_tags_any: 不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据
        :type not_tags_any: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        :param sys_tags: 
        :type sys_tags: :class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`
        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段
        :type without_any_tag: bool
        """
        
        

        self._matches = None
        self._not_tags = None
        self._tags = None
        self._tags_any = None
        self._not_tags_any = None
        self._sys_tags = None
        self._without_any_tag = None
        self.discriminator = None

        if matches is not None:
            self.matches = matches
        if not_tags is not None:
            self.not_tags = not_tags
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def matches(self):
        """Gets the matches of this ResourceInstanceTagRequest.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。 根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。resource_id为精确匹配。第一期只做resource_name，后续再扩展。

        :return: The matches of this ResourceInstanceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceTagRequestMatches`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ResourceInstanceTagRequest.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。 根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。resource_id为精确匹配。第一期只做resource_name，后续再扩展。

        :param matches: The matches of this ResourceInstanceTagRequest.
        :type matches: list[:class:`huaweicloudsdkdbss.v1.ResourceInstanceTagRequestMatches`]
        """
        self._matches = matches

    @property
    def not_tags(self):
        """Gets the not_tags of this ResourceInstanceTagRequest.

        不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :return: The not_tags of this ResourceInstanceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ResourceInstanceTagRequest.

        不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :param not_tags: The not_tags of this ResourceInstanceTagRequest.
        :type not_tags: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        self._not_tags = not_tags

    @property
    def tags(self):
        """Gets the tags of this ResourceInstanceTagRequest.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据

        :return: The tags of this ResourceInstanceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceInstanceTagRequest.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据

        :param tags: The tags of this ResourceInstanceTagRequest.
        :type tags: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ResourceInstanceTagRequest.

        包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :return: The tags_any of this ResourceInstanceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ResourceInstanceTagRequest.

        包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :param tags_any: The tags_any of this ResourceInstanceTagRequest.
        :type tags_any: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        self._tags_any = tags_any

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ResourceInstanceTagRequest.

        不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :return: The not_tags_any of this ResourceInstanceTagRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ResourceInstanceTagRequest.

        不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据

        :param not_tags_any: The not_tags_any of this ResourceInstanceTagRequest.
        :type not_tags_any: list[:class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`]
        """
        self._not_tags_any = not_tags_any

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ResourceInstanceTagRequest.

        :return: The sys_tags of this ResourceInstanceTagRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ResourceInstanceTagRequest.

        :param sys_tags: The sys_tags of this ResourceInstanceTagRequest.
        :type sys_tags: :class:`huaweicloudsdkdbss.v1.TagKeyValuesBean`
        """
        self._sys_tags = sys_tags

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ResourceInstanceTagRequest.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段

        :return: The without_any_tag of this ResourceInstanceTagRequest.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ResourceInstanceTagRequest.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段

        :param without_any_tag: The without_any_tag of this ResourceInstanceTagRequest.
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
        if not isinstance(other, ResourceInstanceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
