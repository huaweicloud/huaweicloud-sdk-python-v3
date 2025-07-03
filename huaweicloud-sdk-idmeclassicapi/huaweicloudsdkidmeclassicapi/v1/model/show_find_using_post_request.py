# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFindUsingPostRequest:

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
        'page_size_path': 'int',
        'cur_page_path': 'int',
        'identifier': 'str',
        'model_name': 'str',
        'body': 'RDMParamVOQueryRequestVo'
    }

    attribute_map = {
        'cur_page': 'curPage',
        'end_index': 'endIndex',
        'max_page_size': 'maxPageSize',
        'page_size': 'pageSize',
        'start_index': 'startIndex',
        'total_pages': 'totalPages',
        'total_rows': 'totalRows',
        'page_size_path': 'pageSizePath',
        'cur_page_path': 'curPagePath',
        'identifier': 'identifier',
        'model_name': 'modelName',
        'body': 'body'
    }

    def __init__(self, cur_page=None, end_index=None, max_page_size=None, page_size=None, start_index=None, total_pages=None, total_rows=None, page_size_path=None, cur_page_path=None, identifier=None, model_name=None, body=None):
        r"""ShowFindUsingPostRequest

        The model defined in huaweicloud sdk

        :param cur_page: **参数解释：**  当前页。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 
        :type cur_page: int
        :param end_index: **参数解释：**  结束索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 
        :type end_index: int
        :param max_page_size: **参数解释：**  最大分页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 
        :type max_page_size: int
        :param page_size: **参数解释：**  每页大小。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 
        :type page_size: int
        :param start_index: **参数解释：**  起始索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 
        :type start_index: int
        :param total_pages: **参数解释：**  总页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 
        :type total_pages: int
        :param total_rows: **参数解释：**  总行数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 
        :type total_rows: int
        :param page_size_path: **参数解释：**  分页大小（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  1-1000。  **默认取值：**  不涉及。 
        :type page_size_path: int
        :param cur_page_path: **参数解释：**  当前页数（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 
        :type cur_page_path: int
        :param identifier: **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 
        :type identifier: str
        :param model_name: **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。
        :type model_name: str
        :param body: Body of the ShowFindUsingPostRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestVo`
        """
        
        

        self._cur_page = None
        self._end_index = None
        self._max_page_size = None
        self._page_size = None
        self._start_index = None
        self._total_pages = None
        self._total_rows = None
        self._page_size_path = None
        self._cur_page_path = None
        self._identifier = None
        self._model_name = None
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
        self.page_size_path = page_size_path
        self.cur_page_path = cur_page_path
        self.identifier = identifier
        self.model_name = model_name
        if body is not None:
            self.body = body

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ShowFindUsingPostRequest.

        **参数解释：**  当前页。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 

        :return: The cur_page of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ShowFindUsingPostRequest.

        **参数解释：**  当前页。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 

        :param cur_page: The cur_page of this ShowFindUsingPostRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def end_index(self):
        r"""Gets the end_index of this ShowFindUsingPostRequest.

        **参数解释：**  结束索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :return: The end_index of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        r"""Sets the end_index of this ShowFindUsingPostRequest.

        **参数解释：**  结束索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :param end_index: The end_index of this ShowFindUsingPostRequest.
        :type end_index: int
        """
        self._end_index = end_index

    @property
    def max_page_size(self):
        r"""Gets the max_page_size of this ShowFindUsingPostRequest.

        **参数解释：**  最大分页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 

        :return: The max_page_size of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._max_page_size

    @max_page_size.setter
    def max_page_size(self, max_page_size):
        r"""Sets the max_page_size of this ShowFindUsingPostRequest.

        **参数解释：**  最大分页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 

        :param max_page_size: The max_page_size of this ShowFindUsingPostRequest.
        :type max_page_size: int
        """
        self._max_page_size = max_page_size

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowFindUsingPostRequest.

        **参数解释：**  每页大小。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 

        :return: The page_size of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowFindUsingPostRequest.

        **参数解释：**  每页大小。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1000。 

        :param page_size: The page_size of this ShowFindUsingPostRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_index(self):
        r"""Gets the start_index of this ShowFindUsingPostRequest.

        **参数解释：**  起始索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :return: The start_index of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        r"""Sets the start_index of this ShowFindUsingPostRequest.

        **参数解释：**  起始索引。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :param start_index: The start_index of this ShowFindUsingPostRequest.
        :type start_index: int
        """
        self._start_index = start_index

    @property
    def total_pages(self):
        r"""Gets the total_pages of this ShowFindUsingPostRequest.

        **参数解释：**  总页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :return: The total_pages of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        r"""Sets the total_pages of this ShowFindUsingPostRequest.

        **参数解释：**  总页数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :param total_pages: The total_pages of this ShowFindUsingPostRequest.
        :type total_pages: int
        """
        self._total_pages = total_pages

    @property
    def total_rows(self):
        r"""Gets the total_rows of this ShowFindUsingPostRequest.

        **参数解释：**  总行数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :return: The total_rows of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this ShowFindUsingPostRequest.

        **参数解释：**  总行数。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  0。 

        :param total_rows: The total_rows of this ShowFindUsingPostRequest.
        :type total_rows: int
        """
        self._total_rows = total_rows

    @property
    def page_size_path(self):
        r"""Gets the page_size_path of this ShowFindUsingPostRequest.

        **参数解释：**  分页大小（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  1-1000。  **默认取值：**  不涉及。 

        :return: The page_size_path of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._page_size_path

    @page_size_path.setter
    def page_size_path(self, page_size_path):
        r"""Sets the page_size_path of this ShowFindUsingPostRequest.

        **参数解释：**  分页大小（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  1-1000。  **默认取值：**  不涉及。 

        :param page_size_path: The page_size_path of this ShowFindUsingPostRequest.
        :type page_size_path: int
        """
        self._page_size_path = page_size_path

    @property
    def cur_page_path(self):
        r"""Gets the cur_page_path of this ShowFindUsingPostRequest.

        **参数解释：**  当前页数（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 

        :return: The cur_page_path of this ShowFindUsingPostRequest.
        :rtype: int
        """
        return self._cur_page_path

    @cur_page_path.setter
    def cur_page_path(self, cur_page_path):
        r"""Sets the cur_page_path of this ShowFindUsingPostRequest.

        **参数解释：**  当前页数（路径参数）。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  1。 

        :param cur_page_path: The cur_page_path of this ShowFindUsingPostRequest.
        :type cur_page_path: int
        """
        self._cur_page_path = cur_page_path

    @property
    def identifier(self):
        r"""Gets the identifier of this ShowFindUsingPostRequest.

        **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 

        :return: The identifier of this ShowFindUsingPostRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this ShowFindUsingPostRequest.

        **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 

        :param identifier: The identifier of this ShowFindUsingPostRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        r"""Gets the model_name of this ShowFindUsingPostRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。

        :return: The model_name of this ShowFindUsingPostRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ShowFindUsingPostRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。

        :param model_name: The model_name of this ShowFindUsingPostRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def body(self):
        r"""Gets the body of this ShowFindUsingPostRequest.

        :return: The body of this ShowFindUsingPostRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestVo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowFindUsingPostRequest.

        :param body: The body of this ShowFindUsingPostRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOQueryRequestVo`
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
        if not isinstance(other, ShowFindUsingPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
