# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesByTagRequestBody:

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
        'tags': 'list[ScsTag]',
        'tags_any': 'list[ScsTag]',
        'not_tags': 'list[ScsTag]',
        'not_tags_any': 'list[ScsTag]',
        'limit': 'int',
        'offset': 'int',
        'action': 'str',
        'matches': 'list[ScsMatch]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, limit=None, offset=None, action=None, matches=None):
        r"""ListCertificatesByTagRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。  - true  - false
        :type without_any_tag: bool
        :param tags: 标签列表。 包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        :param tags_any: 标签列表。 包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        :param not_tags: 标签列表。 不包含标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        :param not_tags_any: 标签列表。 不包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        :param limit: 每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。
        :type limit: int
        :param offset: 索引位置，偏移量，从offset指定的下一条数据开始查询。
        :type offset: int
        :param action: 操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。
        :type action: str
        :param matches: 搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。
        :type matches: list[:class:`huaweicloudsdkscm.v3.ScsMatch`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._limit = None
        self._offset = None
        self._action = None
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
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if action is not None:
            self.action = action
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListCertificatesByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。  - true  - false

        :return: The without_any_tag of this ListCertificatesByTagRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListCertificatesByTagRequestBody.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。  - true  - false

        :param without_any_tag: The without_any_tag of this ListCertificatesByTagRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListCertificatesByTagRequestBody.

        标签列表。 包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ListCertificatesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListCertificatesByTagRequestBody.

        标签列表。 包含标签，最多包含20个key，每个key下面的value最多20个，每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListCertificatesByTagRequestBody.
        :type tags: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        r"""Gets the tags_any of this ListCertificatesByTagRequestBody.

        标签列表。 包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The tags_any of this ListCertificatesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        r"""Sets the tags_any of this ListCertificatesByTagRequestBody.

        标签列表。 包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this ListCertificatesByTagRequestBody.
        :type tags_any: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        r"""Gets the not_tags of this ListCertificatesByTagRequestBody.

        标签列表。 不包含标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags of this ListCertificatesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this ListCertificatesByTagRequestBody.

        标签列表。 不包含标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this ListCertificatesByTagRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        r"""Gets the not_tags_any of this ListCertificatesByTagRequestBody.

        标签列表。 不包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags_any of this ListCertificatesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        r"""Sets the not_tags_any of this ListCertificatesByTagRequestBody.

        标签列表。 不包含任意标签，最多包含20个key，每个key下面的value最多20个, 每个key对应的value可以为空数组但结构体不能缺失。Key不能重复，同一个key中values不能重复。结果返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this ListCertificatesByTagRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdkscm.v3.ScsTag`]
        """
        self._not_tags_any = not_tags_any

    @property
    def limit(self):
        r"""Gets the limit of this ListCertificatesByTagRequestBody.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :return: The limit of this ListCertificatesByTagRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCertificatesByTagRequestBody.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :param limit: The limit of this ListCertificatesByTagRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCertificatesByTagRequestBody.

        索引位置，偏移量，从offset指定的下一条数据开始查询。

        :return: The offset of this ListCertificatesByTagRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCertificatesByTagRequestBody.

        索引位置，偏移量，从offset指定的下一条数据开始查询。

        :param offset: The offset of this ListCertificatesByTagRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def action(self):
        r"""Gets the action of this ListCertificatesByTagRequestBody.

        操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。

        :return: The action of this ListCertificatesByTagRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListCertificatesByTagRequestBody.

        操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。

        :param action: The action of this ListCertificatesByTagRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        r"""Gets the matches of this ListCertificatesByTagRequestBody.

        搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。

        :return: The matches of this ListCertificatesByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.ScsMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListCertificatesByTagRequestBody.

        搜索字段。 key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值，不能包含重复的key或不支持的key。

        :param matches: The matches of this ListCertificatesByTagRequestBody.
        :type matches: list[:class:`huaweicloudsdkscm.v3.ScsMatch`]
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
        if not isinstance(other, ListCertificatesByTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
