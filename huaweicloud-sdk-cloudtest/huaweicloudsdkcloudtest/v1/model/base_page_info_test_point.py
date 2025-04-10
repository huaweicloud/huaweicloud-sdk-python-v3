# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasePageInfoTestPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'list': 'list[TestPoint]',
        'offset': 'int',
        'pages': 'int',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'list': 'list',
        'offset': 'offset',
        'pages': 'pages',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, limit=None, list=None, offset=None, pages=None, size=None, total=None):
        r"""BasePageInfoTestPoint

        The model defined in huaweicloud sdk

        :param limit: 
        :type limit: int
        :param list: 
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TestPoint`]
        :param offset: 
        :type offset: int
        :param pages: 
        :type pages: int
        :param size: 
        :type size: int
        :param total: 
        :type total: int
        """
        
        

        self._limit = None
        self._list = None
        self._offset = None
        self._pages = None
        self._size = None
        self._total = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if list is not None:
            self.list = list
        if offset is not None:
            self.offset = offset
        if pages is not None:
            self.pages = pages
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def limit(self):
        r"""Gets the limit of this BasePageInfoTestPoint.

        :return: The limit of this BasePageInfoTestPoint.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BasePageInfoTestPoint.

        :param limit: The limit of this BasePageInfoTestPoint.
        :type limit: int
        """
        self._limit = limit

    @property
    def list(self):
        r"""Gets the list of this BasePageInfoTestPoint.

        :return: The list of this BasePageInfoTestPoint.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestPoint`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this BasePageInfoTestPoint.

        :param list: The list of this BasePageInfoTestPoint.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TestPoint`]
        """
        self._list = list

    @property
    def offset(self):
        r"""Gets the offset of this BasePageInfoTestPoint.

        :return: The offset of this BasePageInfoTestPoint.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BasePageInfoTestPoint.

        :param offset: The offset of this BasePageInfoTestPoint.
        :type offset: int
        """
        self._offset = offset

    @property
    def pages(self):
        r"""Gets the pages of this BasePageInfoTestPoint.

        :return: The pages of this BasePageInfoTestPoint.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this BasePageInfoTestPoint.

        :param pages: The pages of this BasePageInfoTestPoint.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        r"""Gets the size of this BasePageInfoTestPoint.

        :return: The size of this BasePageInfoTestPoint.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BasePageInfoTestPoint.

        :param size: The size of this BasePageInfoTestPoint.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this BasePageInfoTestPoint.

        :return: The total of this BasePageInfoTestPoint.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BasePageInfoTestPoint.

        :param total: The total of this BasePageInfoTestPoint.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, BasePageInfoTestPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
