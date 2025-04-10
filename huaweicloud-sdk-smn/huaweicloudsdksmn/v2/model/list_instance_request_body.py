# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ResourceTags]',
        'tags_any': 'list[ResourceTags]',
        'not_tags': 'list[ResourceTags]',
        'not_tags_any': 'list[ResourceTags]',
        'offset': 'str',
        'limit': 'str',
        'action': 'str',
        'matches': 'list[TagMatch]',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'matches': 'matches',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, tags=None, tags_any=None, not_tags=None, not_tags_any=None, offset=None, limit=None, action=None, matches=None, without_any_tag=None):
        r"""ListInstanceRequestBody

        The model defined in huaweicloud sdk

        :param tags: 最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与的关系。
        :type tags: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        :param tags_any: 最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或的关系。
        :type tags_any: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        :param not_tags: 最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与非的关系。
        :type not_tags: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        :param not_tags_any: 最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或非的关系。
        :type not_tags_any: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        :param offset: 索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。  action为count时无此参数。  action为filter时，默认为0，必须为数字，且不能为负数。
        :type offset: str
        :param limit: 查询记录数。  action为count时无此参数。  action为filter时，默认为1000。limit最多为1000，不能为负数，最小值为1。
        :type limit: str
        :param action: 操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。 为filter时表示分页查询，为count只需按照条件将总条数返回即可。
        :type action: str
        :param matches: 搜索字段。  key为要匹配的字段，当前只支持resource_name。  value为匹配的值，当前为精确匹配。
        :type matches: list[:class:`huaweicloudsdksmn.v2.TagMatch`]
        :param without_any_tag: 不包含任意一个标签。该字段为true时查询所有不带标签的资源，此时忽略“tags”、“tags_any”、“not_tags”、“not_tags_any”字段。
        :type without_any_tag: bool
        """
        
        

        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._offset = None
        self._limit = None
        self._action = None
        self._matches = None
        self._without_any_tag = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.action = action
        if matches is not None:
            self.matches = matches
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与的关系。

        :return: The tags of this ListInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与的关系。

        :param tags: The tags of this ListInstanceRequestBody.
        :type tags: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        r"""Gets the tags_any of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或的关系。

        :return: The tags_any of this ListInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        r"""Sets the tags_any of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或的关系。

        :param tags_any: The tags_any of this ListInstanceRequestBody.
        :type tags_any: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        r"""Gets the not_tags of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与非的关系。

        :return: The not_tags of this ListInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为与非的关系。

        :param not_tags: The not_tags of this ListInstanceRequestBody.
        :type not_tags: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        r"""Gets the not_tags_any of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或非的关系。

        :return: The not_tags_any of this ListInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        r"""Sets the not_tags_any of this ListInstanceRequestBody.

        最多包含10个key，每个key最多包含10个value，结构体不能缺失。key不能为空或者空字符串。key不能重复，同一个key中value不能重复，不同key对应的资源之间为或非的关系。

        :param not_tags_any: The not_tags_any of this ListInstanceRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdksmn.v2.ResourceTags`]
        """
        self._not_tags_any = not_tags_any

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。  action为count时无此参数。  action为filter时，默认为0，必须为数字，且不能为负数。

        :return: The offset of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。  action为count时无此参数。  action为filter时，默认为0，必须为数字，且不能为负数。

        :param offset: The offset of this ListInstanceRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceRequestBody.

        查询记录数。  action为count时无此参数。  action为filter时，默认为1000。limit最多为1000，不能为负数，最小值为1。

        :return: The limit of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceRequestBody.

        查询记录数。  action为count时无此参数。  action为filter时，默认为1000。limit最多为1000，不能为负数，最小值为1。

        :param limit: The limit of this ListInstanceRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def action(self):
        r"""Gets the action of this ListInstanceRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。 为filter时表示分页查询，为count只需按照条件将总条数返回即可。

        :return: The action of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListInstanceRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数)。 为filter时表示分页查询，为count只需按照条件将总条数返回即可。

        :param action: The action of this ListInstanceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        r"""Gets the matches of this ListInstanceRequestBody.

        搜索字段。  key为要匹配的字段，当前只支持resource_name。  value为匹配的值，当前为精确匹配。

        :return: The matches of this ListInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.TagMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListInstanceRequestBody.

        搜索字段。  key为要匹配的字段，当前只支持resource_name。  value为匹配的值，当前为精确匹配。

        :param matches: The matches of this ListInstanceRequestBody.
        :type matches: list[:class:`huaweicloudsdksmn.v2.TagMatch`]
        """
        self._matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ListInstanceRequestBody.

        不包含任意一个标签。该字段为true时查询所有不带标签的资源，此时忽略“tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :return: The without_any_tag of this ListInstanceRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ListInstanceRequestBody.

        不包含任意一个标签。该字段为true时查询所有不带标签的资源，此时忽略“tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :param without_any_tag: The without_any_tag of this ListInstanceRequestBody.
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
        if not isinstance(other, ListInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
