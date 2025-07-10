# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimAlgorithmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'ordering': 'str',
        'image_repo_id': 'int',
        'search': 'str'
    }

    attribute_map = {
        'category': 'category',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'ordering': 'ordering',
        'image_repo_id': 'image_repo_id',
        'search': 'search'
    }

    def __init__(self, category=None, limit=None, name=None, offset=None, ordering=None, image_repo_id=None, search=None):
        r"""ListSimAlgorithmsRequest

        The model defined in huaweicloud sdk

        :param category: 算法类型  * &#x60;code&#x60; - Code * &#x60;artifact&#x60; - Artifact * &#x60;image&#x60; - Image
        :type category: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param name: 
        :type name: str
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param image_repo_id: 
        :type image_repo_id: int
        :param search: A search term.
        :type search: str
        """
        
        

        self._category = None
        self._limit = None
        self._name = None
        self._offset = None
        self._ordering = None
        self._image_repo_id = None
        self._search = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if ordering is not None:
            self.ordering = ordering
        if image_repo_id is not None:
            self.image_repo_id = image_repo_id
        if search is not None:
            self.search = search

    @property
    def category(self):
        r"""Gets the category of this ListSimAlgorithmsRequest.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :return: The category of this ListSimAlgorithmsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListSimAlgorithmsRequest.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :param category: The category of this ListSimAlgorithmsRequest.
        :type category: str
        """
        self._category = category

    @property
    def limit(self):
        r"""Gets the limit of this ListSimAlgorithmsRequest.

        Number of results to return per page.

        :return: The limit of this ListSimAlgorithmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimAlgorithmsRequest.

        Number of results to return per page.

        :param limit: The limit of this ListSimAlgorithmsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListSimAlgorithmsRequest.

        :return: The name of this ListSimAlgorithmsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSimAlgorithmsRequest.

        :param name: The name of this ListSimAlgorithmsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListSimAlgorithmsRequest.

        The initial index from which to return the results.

        :return: The offset of this ListSimAlgorithmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimAlgorithmsRequest.

        The initial index from which to return the results.

        :param offset: The offset of this ListSimAlgorithmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimAlgorithmsRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimAlgorithmsRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimAlgorithmsRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimAlgorithmsRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def image_repo_id(self):
        r"""Gets the image_repo_id of this ListSimAlgorithmsRequest.

        :return: The image_repo_id of this ListSimAlgorithmsRequest.
        :rtype: int
        """
        return self._image_repo_id

    @image_repo_id.setter
    def image_repo_id(self, image_repo_id):
        r"""Sets the image_repo_id of this ListSimAlgorithmsRequest.

        :param image_repo_id: The image_repo_id of this ListSimAlgorithmsRequest.
        :type image_repo_id: int
        """
        self._image_repo_id = image_repo_id

    @property
    def search(self):
        r"""Gets the search of this ListSimAlgorithmsRequest.

        A search term.

        :return: The search of this ListSimAlgorithmsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimAlgorithmsRequest.

        A search term.

        :param search: The search of this ListSimAlgorithmsRequest.
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
        if not isinstance(other, ListSimAlgorithmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
