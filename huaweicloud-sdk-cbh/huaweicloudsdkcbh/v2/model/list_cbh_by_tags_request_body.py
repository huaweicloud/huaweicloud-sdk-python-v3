# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCBHByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[Tags]',
        'tags_any': 'list[Tags]',
        'not_tags': 'list[Tags]',
        'not_tags_any': 'list[Tags]',
        'sys_tags': 'list[Tags]',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'sys_tags': 'sys_tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, sys_tags=None, matches=None):
        """ListCBHByTagsRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源。  此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。  Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系， key-value结构中value是或的关系。  无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        :param tags_any: 包含任意标签，最多包含50个key，每个key下面的value最多10个,每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        :param not_tags: 不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        :param not_tags_any: 不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        :param sys_tags: 仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  key：_sys_enterprise_project_id  value：企业项目id列表  目前TMS调用时，key下面只包含一个value。0表示默认企业项目  sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。。
        :type sys_tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        :param matches: 搜索字段,key为要匹配的字段，如resource_name等。  value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。  根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。  resource_id为精确匹配。第一期只做resource_name，后续再扩展。
        :type matches: list[:class:`huaweicloudsdkcbh.v2.Match`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._sys_tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ListCBHByTagsRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源。  此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :return: The without_any_tag of this ListCBHByTagsRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ListCBHByTagsRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源。  此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :param without_any_tag: The without_any_tag of this ListCBHByTagsRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        """Gets the tags of this ListCBHByTagsRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。  Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系， key-value结构中value是或的关系。  无tag过滤条件时返回全量数据。

        :return: The tags of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListCBHByTagsRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。  Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系， key-value结构中value是或的关系。  无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListCBHByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListCBHByTagsRequestBody.

        包含任意标签，最多包含50个key，每个key下面的value最多10个,每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The tags_any of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListCBHByTagsRequestBody.

        包含任意标签，最多包含50个key，每个key下面的value最多10个,每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this ListCBHByTagsRequestBody.
        :type tags_any: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListCBHByTagsRequestBody.

        不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The not_tags of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListCBHByTagsRequestBody.

        不包含标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this ListCBHByTagsRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListCBHByTagsRequestBody.

        不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The not_tags_any of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListCBHByTagsRequestBody.

        不包含任意标签，最多包含50个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。  结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this ListCBHByTagsRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        self._not_tags_any = not_tags_any

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ListCBHByTagsRequestBody.

        仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  key：_sys_enterprise_project_id  value：企业项目id列表  目前TMS调用时，key下面只包含一个value。0表示默认企业项目  sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。。

        :return: The sys_tags of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ListCBHByTagsRequestBody.

        仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  key：_sys_enterprise_project_id  value：企业项目id列表  目前TMS调用时，key下面只包含一个value。0表示默认企业项目  sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。。

        :param sys_tags: The sys_tags of this ListCBHByTagsRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkcbh.v2.Tags`]
        """
        self._sys_tags = sys_tags

    @property
    def matches(self):
        """Gets the matches of this ListCBHByTagsRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。  value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。  根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。  resource_id为精确匹配。第一期只做resource_name，后续再扩展。

        :return: The matches of this ListCBHByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListCBHByTagsRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。  value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。  根据key的值确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配（多数服务不存在资源名称为空的情况，因此此类情况返回空列表）。  resource_id为精确匹配。第一期只做resource_name，后续再扩展。

        :param matches: The matches of this ListCBHByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkcbh.v2.Match`]
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
        if not isinstance(other, ListCBHByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
