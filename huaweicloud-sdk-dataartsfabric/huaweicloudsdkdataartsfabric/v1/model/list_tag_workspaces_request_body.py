# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagWorkspacesRequestBody:

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
        'tags': 'list[ResourceTagParam]',
        'matches': 'list[TagMatch]',
        'sys_tags': 'list[SystemTagParam]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None, sys_tags=None):
        r"""ListTagWorkspacesRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。
        :type tags: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTagParam`]
        :param matches: 搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。
        :type matches: list[:class:`huaweicloudsdkdataartsfabric.v1.TagMatch`]
        :param sys_tags: 系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。
        :type sys_tags: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTagParam`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self._sys_tags = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListTagWorkspacesRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段

        :return: The without_any_tag of this ListTagWorkspacesRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListTagWorkspacesRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段

        :param without_any_tag: The without_any_tag of this ListTagWorkspacesRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListTagWorkspacesRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。

        :return: The tags of this ListTagWorkspacesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTagParam`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListTagWorkspacesRequestBody.

        包含标签，最多包含50个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。

        :param tags: The tags of this ListTagWorkspacesRequestBody.
        :type tags: list[:class:`huaweicloudsdkdataartsfabric.v1.ResourceTagParam`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this ListTagWorkspacesRequestBody.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。

        :return: The matches of this ListTagWorkspacesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.TagMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListTagWorkspacesRequestBody.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。

        :param matches: The matches of this ListTagWorkspacesRequestBody.
        :type matches: list[:class:`huaweicloudsdkdataartsfabric.v1.TagMatch`]
        """
        self._matches = matches

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListTagWorkspacesRequestBody.

        系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。

        :return: The sys_tags of this ListTagWorkspacesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTagParam`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListTagWorkspacesRequestBody.

        系统标签列表，目前只包含一个tag结构体。key下面只包含一个value。

        :param sys_tags: The sys_tags of this ListTagWorkspacesRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkdataartsfabric.v1.SystemTagParam`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ListTagWorkspacesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
