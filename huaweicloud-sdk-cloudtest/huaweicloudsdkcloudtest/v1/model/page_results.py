# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_list': 'list[VariableRes]',
        'page_no': 'int',
        'page_size': 'int',
        'total_page': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'page_list': 'page_list',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'total_page': 'total_page',
        'total_size': 'total_size'
    }

    def __init__(self, page_list=None, page_no=None, page_size=None, total_page=None, total_size=None):
        """PageResults

        The model defined in huaweicloud sdk

        :param page_list: 
        :type page_list: list[:class:`huaweicloudsdkcloudtest.v1.VariableRes`]
        :param page_no: 
        :type page_no: int
        :param page_size: 
        :type page_size: int
        :param total_page: 
        :type total_page: int
        :param total_size: 
        :type total_size: int
        """
        
        

        self._page_list = None
        self._page_no = None
        self._page_size = None
        self._total_page = None
        self._total_size = None
        self.discriminator = None

        if page_list is not None:
            self.page_list = page_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if total_page is not None:
            self.total_page = total_page
        if total_size is not None:
            self.total_size = total_size

    @property
    def page_list(self):
        """Gets the page_list of this PageResults.

        :return: The page_list of this PageResults.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.VariableRes`]
        """
        return self._page_list

    @page_list.setter
    def page_list(self, page_list):
        """Sets the page_list of this PageResults.

        :param page_list: The page_list of this PageResults.
        :type page_list: list[:class:`huaweicloudsdkcloudtest.v1.VariableRes`]
        """
        self._page_list = page_list

    @property
    def page_no(self):
        """Gets the page_no of this PageResults.

        :return: The page_no of this PageResults.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this PageResults.

        :param page_no: The page_no of this PageResults.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this PageResults.

        :return: The page_size of this PageResults.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PageResults.

        :param page_size: The page_size of this PageResults.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_page(self):
        """Gets the total_page of this PageResults.

        :return: The total_page of this PageResults.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this PageResults.

        :param total_page: The total_page of this PageResults.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_size(self):
        """Gets the total_size of this PageResults.

        :return: The total_size of this PageResults.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this PageResults.

        :param total_size: The total_size of this PageResults.
        :type total_size: int
        """
        self._total_size = total_size

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
        if not isinstance(other, PageResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
