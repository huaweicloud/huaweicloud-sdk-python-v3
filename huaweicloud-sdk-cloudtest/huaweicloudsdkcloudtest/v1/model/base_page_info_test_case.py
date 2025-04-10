# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasePageInfoTestCase:

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
        'list': 'list[TestCase]',
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
        r"""BasePageInfoTestCase

        The model defined in huaweicloud sdk

        :param limit: 
        :type limit: int
        :param list: 
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TestCase`]
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
        r"""Gets the limit of this BasePageInfoTestCase.

        :return: The limit of this BasePageInfoTestCase.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BasePageInfoTestCase.

        :param limit: The limit of this BasePageInfoTestCase.
        :type limit: int
        """
        self._limit = limit

    @property
    def list(self):
        r"""Gets the list of this BasePageInfoTestCase.

        :return: The list of this BasePageInfoTestCase.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCase`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this BasePageInfoTestCase.

        :param list: The list of this BasePageInfoTestCase.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TestCase`]
        """
        self._list = list

    @property
    def offset(self):
        r"""Gets the offset of this BasePageInfoTestCase.

        :return: The offset of this BasePageInfoTestCase.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BasePageInfoTestCase.

        :param offset: The offset of this BasePageInfoTestCase.
        :type offset: int
        """
        self._offset = offset

    @property
    def pages(self):
        r"""Gets the pages of this BasePageInfoTestCase.

        :return: The pages of this BasePageInfoTestCase.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this BasePageInfoTestCase.

        :param pages: The pages of this BasePageInfoTestCase.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        r"""Gets the size of this BasePageInfoTestCase.

        :return: The size of this BasePageInfoTestCase.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BasePageInfoTestCase.

        :param size: The size of this BasePageInfoTestCase.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this BasePageInfoTestCase.

        :return: The total of this BasePageInfoTestCase.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BasePageInfoTestCase.

        :param total: The total of this BasePageInfoTestCase.
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
        if not isinstance(other, BasePageInfoTestCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
