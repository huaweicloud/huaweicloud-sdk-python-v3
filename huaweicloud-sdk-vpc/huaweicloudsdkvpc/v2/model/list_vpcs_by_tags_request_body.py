# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcsByTagsRequestBody:

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
        'limit': 'int',
        'offset': 'int',
        'matches': 'list[Match]',
        'tags': 'list[ListTag]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches',
        'tags': 'tags'
    }

    def __init__(self, action=None, limit=None, offset=None, matches=None, tags=None):
        """ListVpcsByTagsRequestBody

        The model defined in huaweicloud sdk

        :param action: 功能说明：操作标识 取值范围：filter(过滤)，count(查询总条数)
        :type action: str
        :param limit: 功能说明：查询记录数 取值范围：1-1000 约束：action为count时此参数不生效；action为filter时默认为1000
        :type limit: int
        :param offset: 功能说明：索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数 约束：action为count时无此参数；action为filter时默认为0；必须为数字，不能为负数
        :type offset: int
        :param matches: 功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：当前仅支持resource_name
        :type matches: list[:class:`huaweicloudsdkvpc.v2.Match`]
        :param tags: 包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复
        :type tags: list[:class:`huaweicloudsdkvpc.v2.ListTag`]
        """
        
        

        self._action = None
        self._limit = None
        self._offset = None
        self._matches = None
        self._tags = None
        self.discriminator = None

        self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags

    @property
    def action(self):
        """Gets the action of this ListVpcsByTagsRequestBody.

        功能说明：操作标识 取值范围：filter(过滤)，count(查询总条数)

        :return: The action of this ListVpcsByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListVpcsByTagsRequestBody.

        功能说明：操作标识 取值范围：filter(过滤)，count(查询总条数)

        :param action: The action of this ListVpcsByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        """Gets the limit of this ListVpcsByTagsRequestBody.

        功能说明：查询记录数 取值范围：1-1000 约束：action为count时此参数不生效；action为filter时默认为1000

        :return: The limit of this ListVpcsByTagsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcsByTagsRequestBody.

        功能说明：查询记录数 取值范围：1-1000 约束：action为count时此参数不生效；action为filter时默认为1000

        :param limit: The limit of this ListVpcsByTagsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVpcsByTagsRequestBody.

        功能说明：索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数 约束：action为count时无此参数；action为filter时默认为0；必须为数字，不能为负数

        :return: The offset of this ListVpcsByTagsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVpcsByTagsRequestBody.

        功能说明：索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数 约束：action为count时无此参数；action为filter时默认为0；必须为数字，不能为负数

        :param offset: The offset of this ListVpcsByTagsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def matches(self):
        """Gets the matches of this ListVpcsByTagsRequestBody.

        功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：当前仅支持resource_name

        :return: The matches of this ListVpcsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListVpcsByTagsRequestBody.

        功能说明：搜索字段，key为要匹配的字段，value为匹配的值 约束：当前仅支持resource_name

        :param matches: The matches of this ListVpcsByTagsRequestBody.
        :type matches: list[:class:`huaweicloudsdkvpc.v2.Match`]
        """
        self._matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListVpcsByTagsRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复

        :return: The tags of this ListVpcsByTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ListTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListVpcsByTagsRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复

        :param tags: The tags of this ListVpcsByTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpc.v2.ListTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ListVpcsByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
