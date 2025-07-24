# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharesByTagRequestBody:

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
        'limit': 'str',
        'offset': 'str',
        'without_any_tag': 'bool',
        'tags': 'list[Tag]',
        'matches': 'list[ResourceTag]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, action=None, limit=None, offset=None, without_any_tag=None, tags=None, matches=None):
        r"""ListSharesByTagRequestBody

        The model defined in huaweicloud sdk

        :param action: 通过标签查询文件系统列表的操作类型。仅支持取值为\&quot;filter\&quot; 或 \&quot;count\&quot;。
        :type action: str
        :param limit: 设置返回的文件系统个数的最大值。
        :type limit: str
        :param offset: 设置返回的文件系统的偏移量
        :type offset: str
        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。该字段为false或者未提供该参数时，该条件不生效，即返回所有资源或按\&quot;tags\&quot;，\&quot;matches\&quot;等条件过滤。
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.Tag`]
        :param matches: 搜索字段,key为要匹配的字段，仅支持取值“resource_name”。value为匹配的值，当value以“\\*”结尾时，为前缀搜索。例如：value值为“sfsturbo\\*”时，返回名称为“sfsturbo”开头的所有资源列表。
        :type matches: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        
        

        self._action = None
        self._limit = None
        self._offset = None
        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def action(self):
        r"""Gets the action of this ListSharesByTagRequestBody.

        通过标签查询文件系统列表的操作类型。仅支持取值为\"filter\" 或 \"count\"。

        :return: The action of this ListSharesByTagRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListSharesByTagRequestBody.

        通过标签查询文件系统列表的操作类型。仅支持取值为\"filter\" 或 \"count\"。

        :param action: The action of this ListSharesByTagRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        r"""Gets the limit of this ListSharesByTagRequestBody.

        设置返回的文件系统个数的最大值。

        :return: The limit of this ListSharesByTagRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSharesByTagRequestBody.

        设置返回的文件系统个数的最大值。

        :param limit: The limit of this ListSharesByTagRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSharesByTagRequestBody.

        设置返回的文件系统的偏移量

        :return: The offset of this ListSharesByTagRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSharesByTagRequestBody.

        设置返回的文件系统的偏移量

        :param offset: The offset of this ListSharesByTagRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListSharesByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。该字段为false或者未提供该参数时，该条件不生效，即返回所有资源或按\"tags\"，\"matches\"等条件过滤。

        :return: The without_any_tag of this ListSharesByTagRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListSharesByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”字段。该字段为false或者未提供该参数时，该条件不生效，即返回所有资源或按\"tags\"，\"matches\"等条件过滤。

        :param without_any_tag: The without_any_tag of this ListSharesByTagRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListSharesByTagRequestBody.

        包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ListSharesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListSharesByTagRequestBody.

        包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListSharesByTagRequestBody.
        :type tags: list[:class:`huaweicloudsdksfsturbo.v1.Tag`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this ListSharesByTagRequestBody.

        搜索字段,key为要匹配的字段，仅支持取值“resource_name”。value为匹配的值，当value以“\\*”结尾时，为前缀搜索。例如：value值为“sfsturbo\\*”时，返回名称为“sfsturbo”开头的所有资源列表。

        :return: The matches of this ListSharesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListSharesByTagRequestBody.

        搜索字段,key为要匹配的字段，仅支持取值“resource_name”。value为匹配的值，当value以“\\*”结尾时，为前缀搜索。例如：value值为“sfsturbo\\*”时，返回名称为“sfsturbo”开头的所有资源列表。

        :param matches: The matches of this ListSharesByTagRequestBody.
        :type matches: list[:class:`huaweicloudsdksfsturbo.v1.ResourceTag`]
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
        if not isinstance(other, ListSharesByTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
