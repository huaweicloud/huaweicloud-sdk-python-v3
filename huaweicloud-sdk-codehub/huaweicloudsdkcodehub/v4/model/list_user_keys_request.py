# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserKeysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'query': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'query': 'query'
    }

    def __init__(self, offset=None, limit=None, query=None):
        r"""ListUserKeysRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param query: **参数解释：** key的标题名称。 **取值范围：** 字符串长度不少于1，不超过2000。
        :type query: str
        """
        
        

        self._offset = None
        self._limit = None
        self._query = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if query is not None:
            self.query = query

    @property
    def offset(self):
        r"""Gets the offset of this ListUserKeysRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListUserKeysRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserKeysRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListUserKeysRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUserKeysRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListUserKeysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserKeysRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListUserKeysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def query(self):
        r"""Gets the query of this ListUserKeysRequest.

        **参数解释：** key的标题名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :return: The query of this ListUserKeysRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListUserKeysRequest.

        **参数解释：** key的标题名称。 **取值范围：** 字符串长度不少于1，不超过2000。

        :param query: The query of this ListUserKeysRequest.
        :type query: str
        """
        self._query = query

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
        if not isinstance(other, ListUserKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
