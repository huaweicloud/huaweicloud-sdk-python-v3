# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoViewDTO:

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
        'total_pages': 'int'
    }

    attribute_map = {
        'cur_page': 'curPage',
        'page_size': 'pageSize',
        'total_rows': 'totalRows',
        'total_pages': 'totalPages'
    }

    def __init__(self, cur_page=None, page_size=None, total_rows=None, total_pages=None):
        r"""PageInfoViewDTO

        The model defined in huaweicloud sdk

        :param cur_page: **参数解释：**  当前页。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type cur_page: int
        :param page_size: **参数解释：**  每页大小。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type page_size: int
        :param total_rows: **参数解释：**  总行数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type total_rows: int
        :param total_pages: **参数解释：**  总页数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type total_pages: int
        """
        
        

        self._cur_page = None
        self._page_size = None
        self._total_rows = None
        self._total_pages = None
        self.discriminator = None

        if cur_page is not None:
            self.cur_page = cur_page
        if page_size is not None:
            self.page_size = page_size
        if total_rows is not None:
            self.total_rows = total_rows
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def cur_page(self):
        r"""Gets the cur_page of this PageInfoViewDTO.

        **参数解释：**  当前页。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The cur_page of this PageInfoViewDTO.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this PageInfoViewDTO.

        **参数解释：**  当前页。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param cur_page: The cur_page of this PageInfoViewDTO.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def page_size(self):
        r"""Gets the page_size of this PageInfoViewDTO.

        **参数解释：**  每页大小。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The page_size of this PageInfoViewDTO.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this PageInfoViewDTO.

        **参数解释：**  每页大小。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param page_size: The page_size of this PageInfoViewDTO.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_rows(self):
        r"""Gets the total_rows of this PageInfoViewDTO.

        **参数解释：**  总行数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The total_rows of this PageInfoViewDTO.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this PageInfoViewDTO.

        **参数解释：**  总行数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param total_rows: The total_rows of this PageInfoViewDTO.
        :type total_rows: int
        """
        self._total_rows = total_rows

    @property
    def total_pages(self):
        r"""Gets the total_pages of this PageInfoViewDTO.

        **参数解释：**  总页数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The total_pages of this PageInfoViewDTO.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        r"""Sets the total_pages of this PageInfoViewDTO.

        **参数解释：**  总页数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param total_pages: The total_pages of this PageInfoViewDTO.
        :type total_pages: int
        """
        self._total_pages = total_pages

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
        if not isinstance(other, PageInfoViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
