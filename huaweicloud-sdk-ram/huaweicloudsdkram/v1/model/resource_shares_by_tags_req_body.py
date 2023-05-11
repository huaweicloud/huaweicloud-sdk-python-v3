# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSharesByTagsReqBody:

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
        'tags': 'list[TagFilter]',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None):
        """ResourceSharesByTagsReqBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源。
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含20个key，每个key下面的value最多20个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是\&quot;与\&quot;的关系，key-value结构中value是\&quot;或\&quot;的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        :param matches: 资源共享实例绑定标签列表的匹配字段。
        :type matches: list[:class:`huaweicloudsdkram.v1.Match`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ResourceSharesByTagsReqBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源。

        :return: The without_any_tag of this ResourceSharesByTagsReqBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ResourceSharesByTagsReqBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源。

        :param without_any_tag: The without_any_tag of this ResourceSharesByTagsReqBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        """Gets the tags of this ResourceSharesByTagsReqBody.

        包含标签，最多包含20个key，每个key下面的value最多20个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是\"与\"的关系，key-value结构中value是\"或\"的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ResourceSharesByTagsReqBody.
        :rtype: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceSharesByTagsReqBody.

        包含标签，最多包含20个key，每个key下面的value最多20个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是\"与\"的关系，key-value结构中value是\"或\"的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ResourceSharesByTagsReqBody.
        :type tags: list[:class:`huaweicloudsdkram.v1.TagFilter`]
        """
        self._tags = tags

    @property
    def matches(self):
        """Gets the matches of this ResourceSharesByTagsReqBody.

        资源共享实例绑定标签列表的匹配字段。

        :return: The matches of this ResourceSharesByTagsReqBody.
        :rtype: list[:class:`huaweicloudsdkram.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ResourceSharesByTagsReqBody.

        资源共享实例绑定标签列表的匹配字段。

        :param matches: The matches of this ResourceSharesByTagsReqBody.
        :type matches: list[:class:`huaweicloudsdkram.v1.Match`]
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
        if not isinstance(other, ResourceSharesByTagsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
