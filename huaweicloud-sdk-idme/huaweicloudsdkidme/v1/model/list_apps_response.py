# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_num': 'int',
        'page_size': 'int',
        'total_size': 'int',
        'total_pages': 'int',
        'result': 'list[ListAppsResponseBodyResult]'
    }

    attribute_map = {
        'page_num': 'page_num',
        'page_size': 'page_size',
        'total_size': 'total_size',
        'total_pages': 'total_pages',
        'result': 'result'
    }

    def __init__(self, page_num=None, page_size=None, total_size=None, total_pages=None, result=None):
        """ListAppsResponse

        The model defined in huaweicloud sdk

        :param page_num: 分页查询时，每页最多展示的记录数。
        :type page_num: int
        :param page_size: 分页查询的页数。
        :type page_size: int
        :param total_size: 总共条数。
        :type total_size: int
        :param total_pages: 总页数。
        :type total_pages: int
        :param result: 应用详情。
        :type result: list[:class:`huaweicloudsdkidme.v1.ListAppsResponseBodyResult`]
        """
        
        super(ListAppsResponse, self).__init__()

        self._page_num = None
        self._page_size = None
        self._total_size = None
        self._total_pages = None
        self._result = None
        self.discriminator = None

        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if total_size is not None:
            self.total_size = total_size
        if total_pages is not None:
            self.total_pages = total_pages
        if result is not None:
            self.result = result

    @property
    def page_num(self):
        """Gets the page_num of this ListAppsResponse.

        分页查询时，每页最多展示的记录数。

        :return: The page_num of this ListAppsResponse.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListAppsResponse.

        分页查询时，每页最多展示的记录数。

        :param page_num: The page_num of this ListAppsResponse.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListAppsResponse.

        分页查询的页数。

        :return: The page_size of this ListAppsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListAppsResponse.

        分页查询的页数。

        :param page_size: The page_size of this ListAppsResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_size(self):
        """Gets the total_size of this ListAppsResponse.

        总共条数。

        :return: The total_size of this ListAppsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ListAppsResponse.

        总共条数。

        :param total_size: The total_size of this ListAppsResponse.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def total_pages(self):
        """Gets the total_pages of this ListAppsResponse.

        总页数。

        :return: The total_pages of this ListAppsResponse.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this ListAppsResponse.

        总页数。

        :param total_pages: The total_pages of this ListAppsResponse.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def result(self):
        """Gets the result of this ListAppsResponse.

        应用详情。

        :return: The result of this ListAppsResponse.
        :rtype: list[:class:`huaweicloudsdkidme.v1.ListAppsResponseBodyResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListAppsResponse.

        应用详情。

        :param result: The result of this ListAppsResponse.
        :type result: list[:class:`huaweicloudsdkidme.v1.ListAppsResponseBodyResult`]
        """
        self._result = result

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
        if not isinstance(other, ListAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
