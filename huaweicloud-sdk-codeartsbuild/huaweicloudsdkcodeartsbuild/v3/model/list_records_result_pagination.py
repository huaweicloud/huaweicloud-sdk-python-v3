# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordsResultPagination:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'page': 'page',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, page=None, limit=None, total=None):
        r"""ListRecordsResultPagination

        The model defined in huaweicloud sdk

        :param page: 分页页数
        :type page: int
        :param limit: 每页数量
        :type limit: int
        :param total: 总数
        :type total: int
        """
        
        

        self._page = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def page(self):
        r"""Gets the page of this ListRecordsResultPagination.

        分页页数

        :return: The page of this ListRecordsResultPagination.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListRecordsResultPagination.

        分页页数

        :param page: The page of this ListRecordsResultPagination.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ListRecordsResultPagination.

        每页数量

        :return: The limit of this ListRecordsResultPagination.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecordsResultPagination.

        每页数量

        :param limit: The limit of this ListRecordsResultPagination.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListRecordsResultPagination.

        总数

        :return: The total of this ListRecordsResultPagination.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRecordsResultPagination.

        总数

        :param total: The total of this ListRecordsResultPagination.
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
        if not isinstance(other, ListRecordsResultPagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
