# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimExtensionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'ordering': 'str',
        'search': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'ordering': 'ordering',
        'search': 'search'
    }

    def __init__(self, offset=None, limit=None, ordering=None, search=None):
        r"""ListSimExtensionsRequest

        The model defined in huaweicloud sdk

        :param offset: A page number within the paginated result set.
        :type offset: int
        :param limit: Number of results to return per page.default_limit &#x3D; 10.
        :type limit: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        """
        
        

        self._offset = None
        self._limit = None
        self._ordering = None
        self._search = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if ordering is not None:
            self.ordering = ordering
        if search is not None:
            self.search = search

    @property
    def offset(self):
        r"""Gets the offset of this ListSimExtensionsRequest.

        A page number within the paginated result set.

        :return: The offset of this ListSimExtensionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimExtensionsRequest.

        A page number within the paginated result set.

        :param offset: The offset of this ListSimExtensionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSimExtensionsRequest.

        Number of results to return per page.default_limit = 10.

        :return: The limit of this ListSimExtensionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimExtensionsRequest.

        Number of results to return per page.default_limit = 10.

        :param limit: The limit of this ListSimExtensionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimExtensionsRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimExtensionsRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimExtensionsRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimExtensionsRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def search(self):
        r"""Gets the search of this ListSimExtensionsRequest.

        A search term.

        :return: The search of this ListSimExtensionsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimExtensionsRequest.

        A search term.

        :param search: The search of this ListSimExtensionsRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListSimExtensionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
