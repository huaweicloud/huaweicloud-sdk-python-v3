# coding: utf-8

import pprint
import re

import six





class ListProjectsV4Request:


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
        'search': 'str',
        'project_type': 'str',
        'sort': 'str',
        'archive': 'str',
        'query_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'project_type': 'project_type',
        'sort': 'sort',
        'archive': 'archive',
        'query_type': 'query_type'
    }

    def __init__(self, offset=None, limit=None, search=None, project_type=None, sort=None, archive=None, query_type=None):
        """ListProjectsV4Request - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._search = None
        self._project_type = None
        self._sort = None
        self._archive = None
        self._query_type = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if search is not None:
            self.search = search
        if project_type is not None:
            self.project_type = project_type
        if sort is not None:
            self.sort = sort
        if archive is not None:
            self.archive = archive
        if query_type is not None:
            self.query_type = query_type

    @property
    def offset(self):
        """Gets the offset of this ListProjectsV4Request.


        :return: The offset of this ListProjectsV4Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectsV4Request.


        :param offset: The offset of this ListProjectsV4Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProjectsV4Request.


        :return: The limit of this ListProjectsV4Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectsV4Request.


        :param limit: The limit of this ListProjectsV4Request.
        :type: int
        """
        self._limit = limit

    @property
    def search(self):
        """Gets the search of this ListProjectsV4Request.


        :return: The search of this ListProjectsV4Request.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListProjectsV4Request.


        :param search: The search of this ListProjectsV4Request.
        :type: str
        """
        self._search = search

    @property
    def project_type(self):
        """Gets the project_type of this ListProjectsV4Request.


        :return: The project_type of this ListProjectsV4Request.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this ListProjectsV4Request.


        :param project_type: The project_type of this ListProjectsV4Request.
        :type: str
        """
        self._project_type = project_type

    @property
    def sort(self):
        """Gets the sort of this ListProjectsV4Request.


        :return: The sort of this ListProjectsV4Request.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListProjectsV4Request.


        :param sort: The sort of this ListProjectsV4Request.
        :type: str
        """
        self._sort = sort

    @property
    def archive(self):
        """Gets the archive of this ListProjectsV4Request.


        :return: The archive of this ListProjectsV4Request.
        :rtype: str
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this ListProjectsV4Request.


        :param archive: The archive of this ListProjectsV4Request.
        :type: str
        """
        self._archive = archive

    @property
    def query_type(self):
        """Gets the query_type of this ListProjectsV4Request.


        :return: The query_type of this ListProjectsV4Request.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListProjectsV4Request.


        :param query_type: The query_type of this ListProjectsV4Request.
        :type: str
        """
        self._query_type = query_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListProjectsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
