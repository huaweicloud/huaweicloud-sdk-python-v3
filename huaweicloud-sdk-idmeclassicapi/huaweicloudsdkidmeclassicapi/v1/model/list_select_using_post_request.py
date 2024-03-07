# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSelectUsingPostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_page': 'int',
        'end_index': 'int',
        'max_page_size': 'int',
        'page_size': 'int',
        'start_index': 'int',
        'total_pages': 'int',
        'total_rows': 'int',
        'identifier': 'str',
        'model_name': 'str',
        'page_size_path': 'int',
        'cur_page_path': 'int',
        'body': 'RDMParamVOQueryRequestSelectedVo'
    }

    attribute_map = {
        'cur_page': 'curPage',
        'end_index': 'endIndex',
        'max_page_size': 'maxPageSize',
        'page_size': 'pageSize',
        'start_index': 'startIndex',
        'total_pages': 'totalPages',
        'total_rows': 'totalRows',
        'identifier': 'identifier',
        'model_name': 'modelName',
        'page_size_path': 'pageSizePath',
        'cur_page_path': 'curPagePath',
        'body': 'body'
    }

    def __init__(self, cur_page=None, end_index=None, max_page_size=None, page_size=None, start_index=None, total_pages=None, total_rows=None, identifier=None, model_name=None, page_size_path=None, cur_page_path=None, body=None):
        """ListSelectUsingPostRequest

        The model defined in huaweicloud sdk

        :param cur_page: 当前页。
        :type cur_page: int
        :param end_index: 结束索引。
        :type end_index: int
        :param max_page_size: 最大分页数。
        :type max_page_size: int
        :param page_size: 每页大小。
        :type page_size: int
        :param start_index: 起始索引。
        :type start_index: int
        :param total_pages: 总页数。
        :type total_pages: int
        :param total_rows: 总行数。
        :type total_rows: int
        :param identifier: 应用ID。
        :type identifier: str
        :param model_name: 数据模型的英文名称。
        :type model_name: str
        :param page_size_path: 分页大小（路径参数）。
        :type page_size_path: int
        :param cur_page_path: 当前页数（路径参数）。
        :type cur_page_path: int
        :param body: Body of the ListSelectUsingPostRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestSelectedVo`
        """
        
        

        self._cur_page = None
        self._end_index = None
        self._max_page_size = None
        self._page_size = None
        self._start_index = None
        self._total_pages = None
        self._total_rows = None
        self._identifier = None
        self._model_name = None
        self._page_size_path = None
        self._cur_page_path = None
        self._body = None
        self.discriminator = None

        if cur_page is not None:
            self.cur_page = cur_page
        if end_index is not None:
            self.end_index = end_index
        if max_page_size is not None:
            self.max_page_size = max_page_size
        if page_size is not None:
            self.page_size = page_size
        if start_index is not None:
            self.start_index = start_index
        if total_pages is not None:
            self.total_pages = total_pages
        if total_rows is not None:
            self.total_rows = total_rows
        self.identifier = identifier
        self.model_name = model_name
        self.page_size_path = page_size_path
        self.cur_page_path = cur_page_path
        if body is not None:
            self.body = body

    @property
    def cur_page(self):
        """Gets the cur_page of this ListSelectUsingPostRequest.

        当前页。

        :return: The cur_page of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        """Sets the cur_page of this ListSelectUsingPostRequest.

        当前页。

        :param cur_page: The cur_page of this ListSelectUsingPostRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def end_index(self):
        """Gets the end_index of this ListSelectUsingPostRequest.

        结束索引。

        :return: The end_index of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this ListSelectUsingPostRequest.

        结束索引。

        :param end_index: The end_index of this ListSelectUsingPostRequest.
        :type end_index: int
        """
        self._end_index = end_index

    @property
    def max_page_size(self):
        """Gets the max_page_size of this ListSelectUsingPostRequest.

        最大分页数。

        :return: The max_page_size of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._max_page_size

    @max_page_size.setter
    def max_page_size(self, max_page_size):
        """Sets the max_page_size of this ListSelectUsingPostRequest.

        最大分页数。

        :param max_page_size: The max_page_size of this ListSelectUsingPostRequest.
        :type max_page_size: int
        """
        self._max_page_size = max_page_size

    @property
    def page_size(self):
        """Gets the page_size of this ListSelectUsingPostRequest.

        每页大小。

        :return: The page_size of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListSelectUsingPostRequest.

        每页大小。

        :param page_size: The page_size of this ListSelectUsingPostRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_index(self):
        """Gets the start_index of this ListSelectUsingPostRequest.

        起始索引。

        :return: The start_index of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this ListSelectUsingPostRequest.

        起始索引。

        :param start_index: The start_index of this ListSelectUsingPostRequest.
        :type start_index: int
        """
        self._start_index = start_index

    @property
    def total_pages(self):
        """Gets the total_pages of this ListSelectUsingPostRequest.

        总页数。

        :return: The total_pages of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this ListSelectUsingPostRequest.

        总页数。

        :param total_pages: The total_pages of this ListSelectUsingPostRequest.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def total_rows(self):
        """Gets the total_rows of this ListSelectUsingPostRequest.

        总行数。

        :return: The total_rows of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this ListSelectUsingPostRequest.

        总行数。

        :param total_rows: The total_rows of this ListSelectUsingPostRequest.
        :type total_rows: int
        """
        self._total_rows = total_rows

    @property
    def identifier(self):
        """Gets the identifier of this ListSelectUsingPostRequest.

        应用ID。

        :return: The identifier of this ListSelectUsingPostRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ListSelectUsingPostRequest.

        应用ID。

        :param identifier: The identifier of this ListSelectUsingPostRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        """Gets the model_name of this ListSelectUsingPostRequest.

        数据模型的英文名称。

        :return: The model_name of this ListSelectUsingPostRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ListSelectUsingPostRequest.

        数据模型的英文名称。

        :param model_name: The model_name of this ListSelectUsingPostRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def page_size_path(self):
        """Gets the page_size_path of this ListSelectUsingPostRequest.

        分页大小（路径参数）。

        :return: The page_size_path of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._page_size_path

    @page_size_path.setter
    def page_size_path(self, page_size_path):
        """Sets the page_size_path of this ListSelectUsingPostRequest.

        分页大小（路径参数）。

        :param page_size_path: The page_size_path of this ListSelectUsingPostRequest.
        :type page_size_path: int
        """
        self._page_size_path = page_size_path

    @property
    def cur_page_path(self):
        """Gets the cur_page_path of this ListSelectUsingPostRequest.

        当前页数（路径参数）。

        :return: The cur_page_path of this ListSelectUsingPostRequest.
        :rtype: int
        """
        return self._cur_page_path

    @cur_page_path.setter
    def cur_page_path(self, cur_page_path):
        """Sets the cur_page_path of this ListSelectUsingPostRequest.

        当前页数（路径参数）。

        :param cur_page_path: The cur_page_path of this ListSelectUsingPostRequest.
        :type cur_page_path: int
        """
        self._cur_page_path = cur_page_path

    @property
    def body(self):
        """Gets the body of this ListSelectUsingPostRequest.

        :return: The body of this ListSelectUsingPostRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestSelectedVo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListSelectUsingPostRequest.

        :param body: The body of this ListSelectUsingPostRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestSelectedVo`
        """
        self._body = body

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
        if not isinstance(other, ListSelectUsingPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
