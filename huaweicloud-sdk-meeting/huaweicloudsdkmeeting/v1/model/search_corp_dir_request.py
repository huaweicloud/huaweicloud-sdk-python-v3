# coding: utf-8

import pprint
import re

import six





class SearchCorpDirRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'dept_code': 'str',
        'query_sub_dept': 'bool',
        'search_scope': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'dept_code': 'deptCode',
        'query_sub_dept': 'querySubDept',
        'search_scope': 'searchScope'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=0, limit=100, search_key=None, dept_code=None, query_sub_dept=True, search_scope='ALL'):
        """SearchCorpDirRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._dept_code = None
        self._query_sub_dept = None
        self._search_scope = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if dept_code is not None:
            self.dept_code = dept_code
        if query_sub_dept is not None:
            self.query_sub_dept = query_sub_dept
        if search_scope is not None:
            self.search_scope = search_scope

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchCorpDirRequest.


        :return: The x_request_id of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchCorpDirRequest.


        :param x_request_id: The x_request_id of this SearchCorpDirRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchCorpDirRequest.


        :return: The accept_language of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchCorpDirRequest.


        :param accept_language: The accept_language of this SearchCorpDirRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchCorpDirRequest.


        :return: The offset of this SearchCorpDirRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchCorpDirRequest.


        :param offset: The offset of this SearchCorpDirRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchCorpDirRequest.


        :return: The limit of this SearchCorpDirRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchCorpDirRequest.


        :param limit: The limit of this SearchCorpDirRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchCorpDirRequest.


        :return: The search_key of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchCorpDirRequest.


        :param search_key: The search_key of this SearchCorpDirRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def dept_code(self):
        """Gets the dept_code of this SearchCorpDirRequest.


        :return: The dept_code of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this SearchCorpDirRequest.


        :param dept_code: The dept_code of this SearchCorpDirRequest.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def query_sub_dept(self):
        """Gets the query_sub_dept of this SearchCorpDirRequest.


        :return: The query_sub_dept of this SearchCorpDirRequest.
        :rtype: bool
        """
        return self._query_sub_dept

    @query_sub_dept.setter
    def query_sub_dept(self, query_sub_dept):
        """Sets the query_sub_dept of this SearchCorpDirRequest.


        :param query_sub_dept: The query_sub_dept of this SearchCorpDirRequest.
        :type: bool
        """
        self._query_sub_dept = query_sub_dept

    @property
    def search_scope(self):
        """Gets the search_scope of this SearchCorpDirRequest.


        :return: The search_scope of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._search_scope

    @search_scope.setter
    def search_scope(self, search_scope):
        """Sets the search_scope of this SearchCorpDirRequest.


        :param search_scope: The search_scope of this SearchCorpDirRequest.
        :type: str
        """
        self._search_scope = search_scope

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
        if not isinstance(other, SearchCorpDirRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
