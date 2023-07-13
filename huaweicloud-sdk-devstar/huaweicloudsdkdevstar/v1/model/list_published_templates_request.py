# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublishedTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'keyword': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'keyword': 'keyword',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, keyword=None, offset=None, limit=None):
        """ListPublishedTemplatesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 
        :type x_language: str
        :param keyword: 搜索关键字，支持按名称和描述搜索，默认null。
        :type keyword: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页的模板条数，默认10。
        :type limit: int
        """
        
        

        self._x_language = None
        self._keyword = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if keyword is not None:
            self.keyword = keyword
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListPublishedTemplatesRequest.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :return: The x_language of this ListPublishedTemplatesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPublishedTemplatesRequest.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :param x_language: The x_language of this ListPublishedTemplatesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def keyword(self):
        """Gets the keyword of this ListPublishedTemplatesRequest.

        搜索关键字，支持按名称和描述搜索，默认null。

        :return: The keyword of this ListPublishedTemplatesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListPublishedTemplatesRequest.

        搜索关键字，支持按名称和描述搜索，默认null。

        :param keyword: The keyword of this ListPublishedTemplatesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def offset(self):
        """Gets the offset of this ListPublishedTemplatesRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListPublishedTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublishedTemplatesRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListPublishedTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPublishedTemplatesRequest.

        每页的模板条数，默认10。

        :return: The limit of this ListPublishedTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublishedTemplatesRequest.

        每页的模板条数，默认10。

        :param limit: The limit of this ListPublishedTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPublishedTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
