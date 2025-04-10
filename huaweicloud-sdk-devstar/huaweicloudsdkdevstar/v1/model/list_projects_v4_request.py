# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectsV4Request:

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
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'keyword': 'keyword',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, keyword=None, limit=None, offset=None):
        r"""ListProjectsV4Request

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param keyword: 搜索关键字,支持按名称和描述搜索，默认null
        :type keyword: str
        :param limit: 每页显示的条目数量,默认100
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询,默认0
        :type offset: int
        """
        
        

        self._x_language = None
        self._keyword = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if keyword is not None:
            self.keyword = keyword
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        r"""Gets the x_language of this ListProjectsV4Request.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this ListProjectsV4Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListProjectsV4Request.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this ListProjectsV4Request.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def keyword(self):
        r"""Gets the keyword of this ListProjectsV4Request.

        搜索关键字,支持按名称和描述搜索，默认null

        :return: The keyword of this ListProjectsV4Request.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListProjectsV4Request.

        搜索关键字,支持按名称和描述搜索，默认null

        :param keyword: The keyword of this ListProjectsV4Request.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectsV4Request.

        每页显示的条目数量,默认100

        :return: The limit of this ListProjectsV4Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectsV4Request.

        每页显示的条目数量,默认100

        :param limit: The limit of this ListProjectsV4Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectsV4Request.

        偏移量，表示从此偏移量开始查询,默认0

        :return: The offset of this ListProjectsV4Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectsV4Request.

        偏移量，表示从此偏移量开始查询,默认0

        :param offset: The offset of this ListProjectsV4Request.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListProjectsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
