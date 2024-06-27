# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasePageInfoTemplateV2:

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
        'list': 'list[TemplateV2]',
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
        """BasePageInfoTemplateV2

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param list: 
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TemplateV2`]
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
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
        """Gets the limit of this BasePageInfoTemplateV2.

        每页显示的条目数量，最大支持200条

        :return: The limit of this BasePageInfoTemplateV2.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BasePageInfoTemplateV2.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this BasePageInfoTemplateV2.
        :type limit: int
        """
        self._limit = limit

    @property
    def list(self):
        """Gets the list of this BasePageInfoTemplateV2.

        :return: The list of this BasePageInfoTemplateV2.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TemplateV2`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this BasePageInfoTemplateV2.

        :param list: The list of this BasePageInfoTemplateV2.
        :type list: list[:class:`huaweicloudsdkcloudtest.v1.TemplateV2`]
        """
        self._list = list

    @property
    def offset(self):
        """Gets the offset of this BasePageInfoTemplateV2.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this BasePageInfoTemplateV2.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BasePageInfoTemplateV2.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this BasePageInfoTemplateV2.
        :type offset: int
        """
        self._offset = offset

    @property
    def pages(self):
        """Gets the pages of this BasePageInfoTemplateV2.

        :return: The pages of this BasePageInfoTemplateV2.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this BasePageInfoTemplateV2.

        :param pages: The pages of this BasePageInfoTemplateV2.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        """Gets the size of this BasePageInfoTemplateV2.

        :return: The size of this BasePageInfoTemplateV2.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BasePageInfoTemplateV2.

        :param size: The size of this BasePageInfoTemplateV2.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this BasePageInfoTemplateV2.

        :return: The total of this BasePageInfoTemplateV2.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BasePageInfoTemplateV2.

        :param total: The total of this BasePageInfoTemplateV2.
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
        if not isinstance(other, BasePageInfoTemplateV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
