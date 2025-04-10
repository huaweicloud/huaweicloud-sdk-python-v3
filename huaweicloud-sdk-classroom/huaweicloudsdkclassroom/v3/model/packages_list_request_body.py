# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackagesListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'PackageFilter',
        'page_size': 'int',
        'start_index': 'int'
    }

    attribute_map = {
        'filter': 'filter',
        'page_size': 'page_size',
        'start_index': 'start_index'
    }

    def __init__(self, filter=None, page_size=None, start_index=None):
        r"""PackagesListRequestBody

        The model defined in huaweicloud sdk

        :param filter: 
        :type filter: :class:`huaweicloudsdkclassroom.v3.PackageFilter`
        :param page_size: 每页数量
        :type page_size: int
        :param start_index: 起始页
        :type start_index: int
        """
        
        

        self._filter = None
        self._page_size = None
        self._start_index = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if page_size is not None:
            self.page_size = page_size
        if start_index is not None:
            self.start_index = start_index

    @property
    def filter(self):
        r"""Gets the filter of this PackagesListRequestBody.

        :return: The filter of this PackagesListRequestBody.
        :rtype: :class:`huaweicloudsdkclassroom.v3.PackageFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this PackagesListRequestBody.

        :param filter: The filter of this PackagesListRequestBody.
        :type filter: :class:`huaweicloudsdkclassroom.v3.PackageFilter`
        """
        self._filter = filter

    @property
    def page_size(self):
        r"""Gets the page_size of this PackagesListRequestBody.

        每页数量

        :return: The page_size of this PackagesListRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this PackagesListRequestBody.

        每页数量

        :param page_size: The page_size of this PackagesListRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_index(self):
        r"""Gets the start_index of this PackagesListRequestBody.

        起始页

        :return: The start_index of this PackagesListRequestBody.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        r"""Sets the start_index of this PackagesListRequestBody.

        起始页

        :param start_index: The start_index of this PackagesListRequestBody.
        :type start_index: int
        """
        self._start_index = start_index

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
        if not isinstance(other, PackagesListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
