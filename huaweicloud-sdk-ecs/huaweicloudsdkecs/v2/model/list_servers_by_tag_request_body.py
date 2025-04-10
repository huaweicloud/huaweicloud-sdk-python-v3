# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersByTagRequestBody:

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
        'tags': 'list[ServerTags]',
        'not_tags': 'list[ServerTags]',
        'matches': 'list[ServerTagMatch]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'not_tags': 'not_tags',
        'matches': 'matches'
    }

    def __init__(self, action=None, limit=None, offset=None, tags=None, not_tags=None, matches=None):
        r"""ListServersByTagRequestBody

        The model defined in huaweicloud sdk

        :param action: 值为filter：表示按标签过滤弹性云服务器，返回符合条件的云服务器列表。
        :type action: str
        :param limit: 查询返回的云服务器数量限制，最多为1000，不能为负数。  - 如果action的值为count时，此参数无效。 - 如果action的值为filter时，limit必填，取值范围[0-1000]，如果不传值，系统默认limit值为1000。
        :type limit: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0。  查询第一页数据时，可以不传入此参数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter时，必填，如果用户不传值，系统默认offset值为0。
        :type offset: str
        :param tags: 查询包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。
        :type tags: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        :param not_tags: 查询不包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。
        :type not_tags: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        :param matches: 搜索字段，用于按条件搜索弹性云服务器。  当前仅支持按resource_name进行搜索
        :type matches: list[:class:`huaweicloudsdkecs.v2.ServerTagMatch`]
        """
        
        

        self._action = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._not_tags = None
        self._matches = None
        self.discriminator = None

        self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if not_tags is not None:
            self.not_tags = not_tags
        if matches is not None:
            self.matches = matches

    @property
    def action(self):
        r"""Gets the action of this ListServersByTagRequestBody.

        值为filter：表示按标签过滤弹性云服务器，返回符合条件的云服务器列表。

        :return: The action of this ListServersByTagRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListServersByTagRequestBody.

        值为filter：表示按标签过滤弹性云服务器，返回符合条件的云服务器列表。

        :param action: The action of this ListServersByTagRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        r"""Gets the limit of this ListServersByTagRequestBody.

        查询返回的云服务器数量限制，最多为1000，不能为负数。  - 如果action的值为count时，此参数无效。 - 如果action的值为filter时，limit必填，取值范围[0-1000]，如果不传值，系统默认limit值为1000。

        :return: The limit of this ListServersByTagRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServersByTagRequestBody.

        查询返回的云服务器数量限制，最多为1000，不能为负数。  - 如果action的值为count时，此参数无效。 - 如果action的值为filter时，limit必填，取值范围[0-1000]，如果不传值，系统默认limit值为1000。

        :param limit: The limit of this ListServersByTagRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListServersByTagRequestBody.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0。  查询第一页数据时，可以不传入此参数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter时，必填，如果用户不传值，系统默认offset值为0。

        :return: The offset of this ListServersByTagRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServersByTagRequestBody.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0。  查询第一页数据时，可以不传入此参数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter时，必填，如果用户不传值，系统默认offset值为0。

        :param offset: The offset of this ListServersByTagRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this ListServersByTagRequestBody.

        查询包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。

        :return: The tags of this ListServersByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListServersByTagRequestBody.

        查询包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。

        :param tags: The tags of this ListServersByTagRequestBody.
        :type tags: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        """
        self._tags = tags

    @property
    def not_tags(self):
        r"""Gets the not_tags of this ListServersByTagRequestBody.

        查询不包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。

        :return: The not_tags of this ListServersByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        r"""Sets the not_tags of this ListServersByTagRequestBody.

        查询不包含所有指定标签的弹性云服务器。  - 最多包含10个key，每个key下面的value最多10个。 - 结构体不能缺失。 - key不能为空或者空字符串。 - key不能重复。 - 同一个key中values不能重复。

        :param not_tags: The not_tags of this ListServersByTagRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkecs.v2.ServerTags`]
        """
        self._not_tags = not_tags

    @property
    def matches(self):
        r"""Gets the matches of this ListServersByTagRequestBody.

        搜索字段，用于按条件搜索弹性云服务器。  当前仅支持按resource_name进行搜索

        :return: The matches of this ListServersByTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerTagMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListServersByTagRequestBody.

        搜索字段，用于按条件搜索弹性云服务器。  当前仅支持按resource_name进行搜索

        :param matches: The matches of this ListServersByTagRequestBody.
        :type matches: list[:class:`huaweicloudsdkecs.v2.ServerTagMatch`]
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
        if not isinstance(other, ListServersByTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
