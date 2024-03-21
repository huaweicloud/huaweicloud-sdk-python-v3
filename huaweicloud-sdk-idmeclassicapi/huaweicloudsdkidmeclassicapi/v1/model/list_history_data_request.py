# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryDataRequest:

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
        'page_size': 'int',
        'total_rows': 'int',
        'total_pages': 'int',
        'limit': 'int',
        'offset': 'int',
        'identifier': 'str',
        'model_name': 'str',
        'page_size_path': 'int',
        'cur_page_path': 'int',
        'body': 'RDMParamVOMongPageRequest'
    }

    attribute_map = {
        'cur_page': 'curPage',
        'page_size': 'pageSize',
        'total_rows': 'totalRows',
        'total_pages': 'totalPages',
        'limit': 'limit',
        'offset': 'offset',
        'identifier': 'identifier',
        'model_name': 'modelName',
        'page_size_path': 'pageSizePath',
        'cur_page_path': 'curPagePath',
        'body': 'body'
    }

    def __init__(self, cur_page=None, page_size=None, total_rows=None, total_pages=None, limit=None, offset=None, identifier=None, model_name=None, page_size_path=None, cur_page_path=None, body=None):
        """ListHistoryDataRequest

        The model defined in huaweicloud sdk

        :param cur_page: 当前页。
        :type cur_page: int
        :param page_size: 每页大小。
        :type page_size: int
        :param total_rows: 总行数。
        :type total_rows: int
        :param total_pages: 总页数。
        :type total_pages: int
        :param limit: 每页显示条目数量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。
        :type limit: int
        :param offset: 偏移量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。
        :type offset: int
        :param identifier: 应用ID。
        :type identifier: str
        :param model_name: 数据模型的英文名称。
        :type model_name: str
        :param page_size_path: 分页大小（路径参数）。
        :type page_size_path: int
        :param cur_page_path: 当前页数（路径参数）。
        :type cur_page_path: int
        :param body: Body of the ListHistoryDataRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMongPageRequest`
        """
        
        

        self._cur_page = None
        self._page_size = None
        self._total_rows = None
        self._total_pages = None
        self._limit = None
        self._offset = None
        self._identifier = None
        self._model_name = None
        self._page_size_path = None
        self._cur_page_path = None
        self._body = None
        self.discriminator = None

        if cur_page is not None:
            self.cur_page = cur_page
        if page_size is not None:
            self.page_size = page_size
        if total_rows is not None:
            self.total_rows = total_rows
        if total_pages is not None:
            self.total_pages = total_pages
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.identifier = identifier
        self.model_name = model_name
        self.page_size_path = page_size_path
        self.cur_page_path = cur_page_path
        if body is not None:
            self.body = body

    @property
    def cur_page(self):
        """Gets the cur_page of this ListHistoryDataRequest.

        当前页。

        :return: The cur_page of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        """Sets the cur_page of this ListHistoryDataRequest.

        当前页。

        :param cur_page: The cur_page of this ListHistoryDataRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def page_size(self):
        """Gets the page_size of this ListHistoryDataRequest.

        每页大小。

        :return: The page_size of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListHistoryDataRequest.

        每页大小。

        :param page_size: The page_size of this ListHistoryDataRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_rows(self):
        """Gets the total_rows of this ListHistoryDataRequest.

        总行数。

        :return: The total_rows of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this ListHistoryDataRequest.

        总行数。

        :param total_rows: The total_rows of this ListHistoryDataRequest.
        :type total_rows: int
        """
        self._total_rows = total_rows

    @property
    def total_pages(self):
        """Gets the total_pages of this ListHistoryDataRequest.

        总页数。

        :return: The total_pages of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this ListHistoryDataRequest.

        总页数。

        :param total_pages: The total_pages of this ListHistoryDataRequest.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def limit(self):
        """Gets the limit of this ListHistoryDataRequest.

        每页显示条目数量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。

        :return: The limit of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHistoryDataRequest.

        每页显示条目数量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。

        :param limit: The limit of this ListHistoryDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListHistoryDataRequest.

        偏移量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。

        :return: The offset of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHistoryDataRequest.

        偏移量，limit和offset均传正确的数值时才起作用，且优先级高于pageSize和curPage。

        :param offset: The offset of this ListHistoryDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def identifier(self):
        """Gets the identifier of this ListHistoryDataRequest.

        应用ID。

        :return: The identifier of this ListHistoryDataRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ListHistoryDataRequest.

        应用ID。

        :param identifier: The identifier of this ListHistoryDataRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        """Gets the model_name of this ListHistoryDataRequest.

        数据模型的英文名称。

        :return: The model_name of this ListHistoryDataRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ListHistoryDataRequest.

        数据模型的英文名称。

        :param model_name: The model_name of this ListHistoryDataRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def page_size_path(self):
        """Gets the page_size_path of this ListHistoryDataRequest.

        分页大小（路径参数）。

        :return: The page_size_path of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._page_size_path

    @page_size_path.setter
    def page_size_path(self, page_size_path):
        """Sets the page_size_path of this ListHistoryDataRequest.

        分页大小（路径参数）。

        :param page_size_path: The page_size_path of this ListHistoryDataRequest.
        :type page_size_path: int
        """
        self._page_size_path = page_size_path

    @property
    def cur_page_path(self):
        """Gets the cur_page_path of this ListHistoryDataRequest.

        当前页数（路径参数）。

        :return: The cur_page_path of this ListHistoryDataRequest.
        :rtype: int
        """
        return self._cur_page_path

    @cur_page_path.setter
    def cur_page_path(self, cur_page_path):
        """Sets the cur_page_path of this ListHistoryDataRequest.

        当前页数（路径参数）。

        :param cur_page_path: The cur_page_path of this ListHistoryDataRequest.
        :type cur_page_path: int
        """
        self._cur_page_path = cur_page_path

    @property
    def body(self):
        """Gets the body of this ListHistoryDataRequest.

        :return: The body of this ListHistoryDataRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMongPageRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListHistoryDataRequest.

        :param body: The body of this ListHistoryDataRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMongPageRequest`
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
        if not isinstance(other, ListHistoryDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
