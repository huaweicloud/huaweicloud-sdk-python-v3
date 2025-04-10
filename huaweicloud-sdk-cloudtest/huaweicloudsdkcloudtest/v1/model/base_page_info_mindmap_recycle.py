# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasePageInfoMindmapRecycle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'list': 'list[MindmapRecycle]',
        'limit': 'int',
        'offset': 'int',
        'pages': 'int',
        'size': 'int'
    }

    attribute_map = {
        'total': 'total',
        'list': 'list',
        'limit': 'limit',
        'offset': 'offset',
        'pages': 'pages',
        'size': 'size'
    }

    def __init__(self, total=None, list=None, limit=None, offset=None, pages=None, size=None):
        r"""BasePageInfoMindmapRecycle

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param list: 入参集合
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.MindmapRecycle`]
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param pages: 总页数
        :type pages: int
        :param size: 每页条数
        :type size: int
        """
        
        

        self._total = None
        self._list = None
        self._limit = None
        self._offset = None
        self._pages = None
        self._size = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if list is not None:
            self.list = list
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if pages is not None:
            self.pages = pages
        if size is not None:
            self.size = size

    @property
    def total(self):
        r"""Gets the total of this BasePageInfoMindmapRecycle.

        总条数

        :return: The total of this BasePageInfoMindmapRecycle.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BasePageInfoMindmapRecycle.

        总条数

        :param total: The total of this BasePageInfoMindmapRecycle.
        :type total: int
        """
        self._total = total

    @property
    def list(self):
        r"""Gets the list of this BasePageInfoMindmapRecycle.

        入参集合

        :return: The list of this BasePageInfoMindmapRecycle.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.MindmapRecycle`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this BasePageInfoMindmapRecycle.

        入参集合

        :param list: The list of this BasePageInfoMindmapRecycle.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.MindmapRecycle`]
        """
        self._list = list

    @property
    def limit(self):
        r"""Gets the limit of this BasePageInfoMindmapRecycle.

        每页显示的条目数量，最大支持200条

        :return: The limit of this BasePageInfoMindmapRecycle.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BasePageInfoMindmapRecycle.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this BasePageInfoMindmapRecycle.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this BasePageInfoMindmapRecycle.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this BasePageInfoMindmapRecycle.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BasePageInfoMindmapRecycle.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this BasePageInfoMindmapRecycle.
        :type offset: int
        """
        self._offset = offset

    @property
    def pages(self):
        r"""Gets the pages of this BasePageInfoMindmapRecycle.

        总页数

        :return: The pages of this BasePageInfoMindmapRecycle.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this BasePageInfoMindmapRecycle.

        总页数

        :param pages: The pages of this BasePageInfoMindmapRecycle.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        r"""Gets the size of this BasePageInfoMindmapRecycle.

        每页条数

        :return: The size of this BasePageInfoMindmapRecycle.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BasePageInfoMindmapRecycle.

        每页条数

        :param size: The size of this BasePageInfoMindmapRecycle.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, BasePageInfoMindmapRecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
