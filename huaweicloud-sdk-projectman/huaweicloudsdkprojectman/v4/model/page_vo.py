# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'str',
        'size': 'str',
        'count': 'str'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size',
        'count': 'count'
    }

    def __init__(self, page=None, size=None, count=None):
        r"""PageVO

        The model defined in huaweicloud sdk

        :param page: 当前页
        :type page: str
        :param size: 每页条数
        :type size: str
        :param count: 数据总数
        :type count: str
        """
        
        

        self._page = None
        self._size = None
        self._count = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if count is not None:
            self.count = count

    @property
    def page(self):
        r"""Gets the page of this PageVO.

        当前页

        :return: The page of this PageVO.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this PageVO.

        当前页

        :param page: The page of this PageVO.
        :type page: str
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this PageVO.

        每页条数

        :return: The size of this PageVO.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PageVO.

        每页条数

        :param size: The size of this PageVO.
        :type size: str
        """
        self._size = size

    @property
    def count(self):
        r"""Gets the count of this PageVO.

        数据总数

        :return: The count of this PageVO.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PageVO.

        数据总数

        :param count: The count of this PageVO.
        :type count: str
        """
        self._count = count

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
        if not isinstance(other, PageVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
