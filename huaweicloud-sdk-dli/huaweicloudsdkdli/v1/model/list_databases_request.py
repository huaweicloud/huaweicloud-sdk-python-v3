# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'limit': 'int',
        'offset': 'int',
        'tags': 'str',
        'with_priv': 'bool'
    }

    attribute_map = {
        'keyword': 'keyword',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'with_priv': 'with-priv'
    }

    def __init__(self, keyword=None, limit=None, offset=None, tags=None, with_priv=None):
        """ListDatabasesRequest

        The model defined in huaweicloud sdk

        :param keyword: 过滤关键字
        :type keyword: str
        :param limit: 查询数量
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        :param tags: 标签过滤
        :type tags: str
        :param with_priv: 是否返回隐私信息
        :type with_priv: bool
        """
        
        

        self._keyword = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._with_priv = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if with_priv is not None:
            self.with_priv = with_priv

    @property
    def keyword(self):
        """Gets the keyword of this ListDatabasesRequest.

        过滤关键字

        :return: The keyword of this ListDatabasesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListDatabasesRequest.

        过滤关键字

        :param keyword: The keyword of this ListDatabasesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def limit(self):
        """Gets the limit of this ListDatabasesRequest.

        查询数量

        :return: The limit of this ListDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabasesRequest.

        查询数量

        :param limit: The limit of this ListDatabasesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDatabasesRequest.

        查询偏移量

        :return: The offset of this ListDatabasesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabasesRequest.

        查询偏移量

        :param offset: The offset of this ListDatabasesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListDatabasesRequest.

        标签过滤

        :return: The tags of this ListDatabasesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListDatabasesRequest.

        标签过滤

        :param tags: The tags of this ListDatabasesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def with_priv(self):
        """Gets the with_priv of this ListDatabasesRequest.

        是否返回隐私信息

        :return: The with_priv of this ListDatabasesRequest.
        :rtype: bool
        """
        return self._with_priv

    @with_priv.setter
    def with_priv(self, with_priv):
        """Sets the with_priv of this ListDatabasesRequest.

        是否返回隐私信息

        :param with_priv: The with_priv of this ListDatabasesRequest.
        :type with_priv: bool
        """
        self._with_priv = with_priv

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
        if not isinstance(other, ListDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
