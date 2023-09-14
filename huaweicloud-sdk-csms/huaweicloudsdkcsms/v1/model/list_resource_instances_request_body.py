# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'offset': 'str',
        'action': 'str',
        'tags': 'list[Tag]',
        'matches': 'list[TagMatches]',
        'sequence': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'tags': 'tags',
        'matches': 'matches',
        'sequence': 'sequence'
    }

    def __init__(self, limit=None, offset=None, action=None, tags=None, matches=None, sequence=None):
        """ListResourceInstancesRequestBody

        The model defined in huaweicloud sdk

        :param limit: 查询记录数（“action”为“count”时，无需设置此参数），如果“action”为“filter”，默认为“10”。 limit的取值范围为“1-1000”。
        :type limit: str
        :param offset: 索引位置。从offset指定的下一条数据开始查询。查询第一页数据时，将查询前一页数据时响应体中的值带入此参数（“action”为“count”时，无需设置此参数）。如果“action”为“filter”，offset默认为“0”。 offset必须为数字，不能为负数。
        :type offset: str
        :param action: 操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。
        :type action: str
        :param tags: 标签列表，key和value键值对的集合。最多不超过10个。
        :type tags: list[:class:`huaweicloudsdkcsms.v1.Tag`]
        :param matches: 搜索字段。  - key为搜索的字段，目前仅支持搜索凭据名称，值为“resource_name”。  - value为模糊匹配的值，最大长度为255个字符。为空返回空值。
        :type matches: list[:class:`huaweicloudsdkcsms.v1.TagMatches`]
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._limit = None
        self._offset = None
        self._action = None
        self._tags = None
        self._matches = None
        self._sequence = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.action = action
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches
        if sequence is not None:
            self.sequence = sequence

    @property
    def limit(self):
        """Gets the limit of this ListResourceInstancesRequestBody.

        查询记录数（“action”为“count”时，无需设置此参数），如果“action”为“filter”，默认为“10”。 limit的取值范围为“1-1000”。

        :return: The limit of this ListResourceInstancesRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceInstancesRequestBody.

        查询记录数（“action”为“count”时，无需设置此参数），如果“action”为“filter”，默认为“10”。 limit的取值范围为“1-1000”。

        :param limit: The limit of this ListResourceInstancesRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListResourceInstancesRequestBody.

        索引位置。从offset指定的下一条数据开始查询。查询第一页数据时，将查询前一页数据时响应体中的值带入此参数（“action”为“count”时，无需设置此参数）。如果“action”为“filter”，offset默认为“0”。 offset必须为数字，不能为负数。

        :return: The offset of this ListResourceInstancesRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourceInstancesRequestBody.

        索引位置。从offset指定的下一条数据开始查询。查询第一页数据时，将查询前一页数据时响应体中的值带入此参数（“action”为“count”时，无需设置此参数）。如果“action”为“filter”，offset默认为“0”。 offset必须为数字，不能为负数。

        :param offset: The offset of this ListResourceInstancesRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ListResourceInstancesRequestBody.

        操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。

        :return: The action of this ListResourceInstancesRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListResourceInstancesRequestBody.

        操作标识（可设置为“filter”或者“count”）。  - filter：表示过滤。  - count：表示查询总条数。

        :param action: The action of this ListResourceInstancesRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        """Gets the tags of this ListResourceInstancesRequestBody.

        标签列表，key和value键值对的集合。最多不超过10个。

        :return: The tags of this ListResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListResourceInstancesRequestBody.

        标签列表，key和value键值对的集合。最多不超过10个。

        :param tags: The tags of this ListResourceInstancesRequestBody.
        :type tags: list[:class:`huaweicloudsdkcsms.v1.Tag`]
        """
        self._tags = tags

    @property
    def matches(self):
        """Gets the matches of this ListResourceInstancesRequestBody.

        搜索字段。  - key为搜索的字段，目前仅支持搜索凭据名称，值为“resource_name”。  - value为模糊匹配的值，最大长度为255个字符。为空返回空值。

        :return: The matches of this ListResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.TagMatches`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListResourceInstancesRequestBody.

        搜索字段。  - key为搜索的字段，目前仅支持搜索凭据名称，值为“resource_name”。  - value为模糊匹配的值，最大长度为255个字符。为空返回空值。

        :param matches: The matches of this ListResourceInstancesRequestBody.
        :type matches: list[:class:`huaweicloudsdkcsms.v1.TagMatches`]
        """
        self._matches = matches

    @property
    def sequence(self):
        """Gets the sequence of this ListResourceInstancesRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this ListResourceInstancesRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ListResourceInstancesRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this ListResourceInstancesRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, ListResourceInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
