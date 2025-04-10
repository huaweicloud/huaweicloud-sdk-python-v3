# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceByFilterTagRequestBody:

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
        'tags': 'list[AggTag]',
        'matches': 'list[Tag]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, action=None, limit=None, offset=None, tags=None, matches=None):
        r"""ListResourceByFilterTagRequestBody

        The model defined in huaweicloud sdk

        :param action: 动作。|- filter：过滤。 count：查询总条数。
        :type action: str
        :param limit: 查询结果数量限制
        :type limit: int
        :param offset: 查询结果偏移
        :type offset: int
        :param tags: 是否包含以下tag（多个key取\&quot;与\&quot;关系，多个value取\&quot;或\&quot;关系）
        :type tags: list[:class:`huaweicloudsdkcc.v2.AggTag`]
        :param matches: 是否匹配以下tag，key必须为\&quot;resource_name\&quot;，value如果有值则模糊匹配，如果为空字符串则精确匹配
        :type matches: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        
        

        self._action = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def action(self):
        r"""Gets the action of this ListResourceByFilterTagRequestBody.

        动作。|- filter：过滤。 count：查询总条数。

        :return: The action of this ListResourceByFilterTagRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListResourceByFilterTagRequestBody.

        动作。|- filter：过滤。 count：查询总条数。

        :param action: The action of this ListResourceByFilterTagRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceByFilterTagRequestBody.

        查询结果数量限制

        :return: The limit of this ListResourceByFilterTagRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceByFilterTagRequestBody.

        查询结果数量限制

        :param limit: The limit of this ListResourceByFilterTagRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceByFilterTagRequestBody.

        查询结果偏移

        :return: The offset of this ListResourceByFilterTagRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceByFilterTagRequestBody.

        查询结果偏移

        :param offset: The offset of this ListResourceByFilterTagRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this ListResourceByFilterTagRequestBody.

        是否包含以下tag（多个key取\"与\"关系，多个value取\"或\"关系）

        :return: The tags of this ListResourceByFilterTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.AggTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListResourceByFilterTagRequestBody.

        是否包含以下tag（多个key取\"与\"关系，多个value取\"或\"关系）

        :param tags: The tags of this ListResourceByFilterTagRequestBody.
        :type tags: list[:class:`huaweicloudsdkcc.v2.AggTag`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this ListResourceByFilterTagRequestBody.

        是否匹配以下tag，key必须为\"resource_name\"，value如果有值则模糊匹配，如果为空字符串则精确匹配

        :return: The matches of this ListResourceByFilterTagRequestBody.
        :rtype: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ListResourceByFilterTagRequestBody.

        是否匹配以下tag，key必须为\"resource_name\"，value如果有值则模糊匹配，如果为空字符串则精确匹配

        :param matches: The matches of this ListResourceByFilterTagRequestBody.
        :type matches: list[:class:`huaweicloudsdkcc.v2.Tag`]
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
        if not isinstance(other, ListResourceByFilterTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
