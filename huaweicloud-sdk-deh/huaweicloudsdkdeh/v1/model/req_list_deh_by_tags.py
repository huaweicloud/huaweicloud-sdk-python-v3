# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqListDehByTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]',
        'not_tags': 'list[Tag]',
        'limit': 'int',
        'offset': 'int',
        'action': 'str',
        'tags_any': 'list[Tag]',
        'not_tags_any': 'list[Tag]',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'tags': 'tags',
        'not_tags': 'not_tags',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'tags_any': 'tags_any',
        'not_tags_any': 'not_tags_any',
        'matches': 'matches'
    }

    def __init__(self, tags=None, not_tags=None, limit=None, offset=None, action=None, tags_any=None, not_tags_any=None, matches=None):
        """ReqListDehByTags

        The model defined in huaweicloud sdk

        :param tags: 查询包含所有指定标签的专属主机结构体不能缺失。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。
        :type tags: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        :param not_tags: 查询不包含所有指定标签的专属主机。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。
        :type not_tags: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        :param limit: 查询返回的专属主机数量限制，最多为1000，不能为负数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，limit默认为1000。
        :type limit: int
        :param offset: 索引位置，从offset指定的下一条数据开始查询。必须为数字，不能为负数。 查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，offset默认为0。
        :type offset: int
        :param action: 操作标识，包括filter和count两种。 1.filter：表示按标签过滤专属主机，返回符合条件的专属主机列表。此时，为分页查询。 2.count：表示按标签搜索专属主机，返回符合条件的专属主机个数。
        :type action: str
        :param tags_any: 包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回包含标签的资源列表，key之间是“或”的关系，key-value结构中value是“或”的关系。 4.无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        :param not_tags_any: 不包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回不包含标签的资源列表，key之间是“或”的关系，key-value结构中value是或的关系。 4.无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        :param matches: 搜索字段，用于按条件搜索专属主机。  当前仅支持按resource_name进行搜索。
        :type matches: list[:class:`huaweicloudsdkdeh.v1.Match`]
        """
        
        

        self._tags = None
        self._not_tags = None
        self._limit = None
        self._offset = None
        self._action = None
        self._tags_any = None
        self._not_tags_any = None
        self._matches = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if not_tags is not None:
            self.not_tags = not_tags
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.action = action
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        """Gets the tags of this ReqListDehByTags.

        查询包含所有指定标签的专属主机结构体不能缺失。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。

        :return: The tags of this ReqListDehByTags.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReqListDehByTags.

        查询包含所有指定标签的专属主机结构体不能缺失。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。

        :param tags: The tags of this ReqListDehByTags.
        :type tags: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        self._tags = tags

    @property
    def not_tags(self):
        """Gets the not_tags of this ReqListDehByTags.

        查询不包含所有指定标签的专属主机。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。

        :return: The not_tags of this ReqListDehByTags.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ReqListDehByTags.

        查询不包含所有指定标签的专属主机。 1.最多包含10个key，每个key下面的value最多10个。 2.结构体不能缺失。 3.key不能为空或者空字符串。 4.key不能重复。 5.同一个key中value不能重复。

        :param not_tags: The not_tags of this ReqListDehByTags.
        :type not_tags: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        self._not_tags = not_tags

    @property
    def limit(self):
        """Gets the limit of this ReqListDehByTags.

        查询返回的专属主机数量限制，最多为1000，不能为负数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，limit默认为1000。

        :return: The limit of this ReqListDehByTags.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ReqListDehByTags.

        查询返回的专属主机数量限制，最多为1000，不能为负数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，limit默认为1000。

        :param limit: The limit of this ReqListDehByTags.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ReqListDehByTags.

        索引位置，从offset指定的下一条数据开始查询。必须为数字，不能为负数。 查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，offset默认为0。

        :return: The offset of this ReqListDehByTags.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ReqListDehByTags.

        索引位置，从offset指定的下一条数据开始查询。必须为数字，不能为负数。 查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。 1.如果action的值为count，此参数无效。 2.如果action的值为filter，offset默认为0。

        :param offset: The offset of this ReqListDehByTags.
        :type offset: int
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ReqListDehByTags.

        操作标识，包括filter和count两种。 1.filter：表示按标签过滤专属主机，返回符合条件的专属主机列表。此时，为分页查询。 2.count：表示按标签搜索专属主机，返回符合条件的专属主机个数。

        :return: The action of this ReqListDehByTags.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ReqListDehByTags.

        操作标识，包括filter和count两种。 1.filter：表示按标签过滤专属主机，返回符合条件的专属主机列表。此时，为分页查询。 2.count：表示按标签搜索专属主机，返回符合条件的专属主机个数。

        :param action: The action of this ReqListDehByTags.
        :type action: str
        """
        self._action = action

    @property
    def tags_any(self):
        """Gets the tags_any of this ReqListDehByTags.

        包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回包含标签的资源列表，key之间是“或”的关系，key-value结构中value是“或”的关系。 4.无过滤条件时返回全量数据。

        :return: The tags_any of this ReqListDehByTags.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ReqListDehByTags.

        包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回包含标签的资源列表，key之间是“或”的关系，key-value结构中value是“或”的关系。 4.无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this ReqListDehByTags.
        :type tags_any: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        self._tags_any = tags_any

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ReqListDehByTags.

        不包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回不包含标签的资源列表，key之间是“或”的关系，key-value结构中value是或的关系。 4.无过滤条件时返回全量数据。

        :return: The not_tags_any of this ReqListDehByTags.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ReqListDehByTags.

        不包含任意标签。 1.最多包含10个key，每个key下面的value最多10个，每个key对应的value可以为空数组但结构体不能缺失。 2.key不能重复，同一个key中value不能重复。 3.结果返回不包含标签的资源列表，key之间是“或”的关系，key-value结构中value是或的关系。 4.无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this ReqListDehByTags.
        :type not_tags_any: list[:class:`huaweicloudsdkdeh.v1.Tag`]
        """
        self._not_tags_any = not_tags_any

    @property
    def matches(self):
        """Gets the matches of this ReqListDehByTags.

        搜索字段，用于按条件搜索专属主机。  当前仅支持按resource_name进行搜索。

        :return: The matches of this ReqListDehByTags.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ReqListDehByTags.

        搜索字段，用于按条件搜索专属主机。  当前仅支持按resource_name进行搜索。

        :param matches: The matches of this ReqListDehByTags.
        :type matches: list[:class:`huaweicloudsdkdeh.v1.Match`]
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
        if not isinstance(other, ReqListDehByTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
