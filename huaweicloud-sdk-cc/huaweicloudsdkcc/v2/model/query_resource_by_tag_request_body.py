# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryResourceByTagRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'without_any_tag': 'bool',
        'tags': 'list[QueryTag]',
        'tags_any': 'list[QueryTag]',
        'not_tags': 'list[QueryTag]',
        'not_tags_any': 'list[QueryTag]',
        'matches': 'list[TmsMatch]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'matches': 'matches'
    }

    def __init__(self, request_id=None, without_any_tag=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, matches=None):
        """QueryResourceByTagRequestBody

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。
        :type without_any_tag: bool
        :param tags: 包含标签，最多包含20个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        :param tags_any: 包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        :param not_tags: 不包含标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        :param not_tags_any: 不包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        :param matches: 是否匹配以下tag，key必须为\&quot;resource_name\&quot;，value如果有值则模糊匹配，如果为空字符串则精确匹配。
        :type matches: list[:class:`huaweicloudsdkcc.v2.TmsMatch`]
        """
        
        

        self._request_id = None
        self._without_any_tag = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._matches = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
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
        if matches is not None:
            self.matches = matches

    @property
    def request_id(self):
        """Gets the request_id of this QueryResourceByTagRequestBody.

        请求ID。

        :return: The request_id of this QueryResourceByTagRequestBody.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this QueryResourceByTagRequestBody.

        请求ID。

        :param request_id: The request_id of this QueryResourceByTagRequestBody.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this QueryResourceByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :return: The without_any_tag of this QueryResourceByTagRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this QueryResourceByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :param without_any_tag: The without_any_tag of this QueryResourceByTagRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        """Gets the tags of this QueryResourceByTagRequestBody.

        包含标签，最多包含20个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this QueryResourceByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryResourceByTagRequestBody.

        包含标签，最多包含20个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this QueryResourceByTagRequestBody.
        :type tags: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this QueryResourceByTagRequestBody.

        包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The tags_any of this QueryResourceByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this QueryResourceByTagRequestBody.

        包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this QueryResourceByTagRequestBody.
        :type tags_any: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this QueryResourceByTagRequestBody.

        不包含标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags of this QueryResourceByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this QueryResourceByTagRequestBody.

        不包含标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this QueryResourceByTagRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this QueryResourceByTagRequestBody.

        不包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags_any of this QueryResourceByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this QueryResourceByTagRequestBody.

        不包含任意标签，最多包含20个key，每个key下面的value最多10个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this QueryResourceByTagRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdkcc.v2.QueryTag`]
        """
        self._not_tags_any = not_tags_any

    @property
    def matches(self):
        """Gets the matches of this QueryResourceByTagRequestBody.

        是否匹配以下tag，key必须为\"resource_name\"，value如果有值则模糊匹配，如果为空字符串则精确匹配。

        :return: The matches of this QueryResourceByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.TmsMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this QueryResourceByTagRequestBody.

        是否匹配以下tag，key必须为\"resource_name\"，value如果有值则模糊匹配，如果为空字符串则精确匹配。

        :param matches: The matches of this QueryResourceByTagRequestBody.
        :type matches: list[:class:`huaweicloudsdkcc.v2.TmsMatch`]
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
        if not isinstance(other, QueryResourceByTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
