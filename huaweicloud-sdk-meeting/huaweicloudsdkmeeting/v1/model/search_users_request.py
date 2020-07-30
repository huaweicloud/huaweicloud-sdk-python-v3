# coding: utf-8

import pprint
import re

import six





class SearchUsersRequest:


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
        'sort_field': 'str',
        'is_asc': 'bool',
        'dept_code': 'str',
        'enable_sub_dept': 'bool',
        'admin_type': 'int',
        'enable_room': 'bool',
        'user_type': 'list[int]',
        'status': 'int'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'sort_field': 'sortField',
        'is_asc': 'isAsc',
        'dept_code': 'deptCode',
        'enable_sub_dept': 'enableSubDept',
        'admin_type': 'adminType',
        'enable_room': 'enableRoom',
        'user_type': 'userType',
        'status': 'status'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=100, search_key=None, sort_field=None, is_asc=None, dept_code=None, enable_sub_dept=None, admin_type=None, enable_room=None, user_type=None, status=None):
        """SearchUsersRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._sort_field = None
        self._is_asc = None
        self._dept_code = None
        self._enable_sub_dept = None
        self._admin_type = None
        self._enable_room = None
        self._user_type = None
        self._status = None
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
        if sort_field is not None:
            self.sort_field = sort_field
        if is_asc is not None:
            self.is_asc = is_asc
        if dept_code is not None:
            self.dept_code = dept_code
        if enable_sub_dept is not None:
            self.enable_sub_dept = enable_sub_dept
        if admin_type is not None:
            self.admin_type = admin_type
        if enable_room is not None:
            self.enable_room = enable_room
        if user_type is not None:
            self.user_type = user_type
        if status is not None:
            self.status = status

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchUsersRequest.


        :return: The x_request_id of this SearchUsersRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchUsersRequest.


        :param x_request_id: The x_request_id of this SearchUsersRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchUsersRequest.


        :return: The accept_language of this SearchUsersRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchUsersRequest.


        :param accept_language: The accept_language of this SearchUsersRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchUsersRequest.


        :return: The offset of this SearchUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchUsersRequest.


        :param offset: The offset of this SearchUsersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchUsersRequest.


        :return: The limit of this SearchUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchUsersRequest.


        :param limit: The limit of this SearchUsersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchUsersRequest.


        :return: The search_key of this SearchUsersRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchUsersRequest.


        :param search_key: The search_key of this SearchUsersRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def sort_field(self):
        """Gets the sort_field of this SearchUsersRequest.


        :return: The sort_field of this SearchUsersRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this SearchUsersRequest.


        :param sort_field: The sort_field of this SearchUsersRequest.
        :type: str
        """
        self._sort_field = sort_field

    @property
    def is_asc(self):
        """Gets the is_asc of this SearchUsersRequest.


        :return: The is_asc of this SearchUsersRequest.
        :rtype: bool
        """
        return self._is_asc

    @is_asc.setter
    def is_asc(self, is_asc):
        """Sets the is_asc of this SearchUsersRequest.


        :param is_asc: The is_asc of this SearchUsersRequest.
        :type: bool
        """
        self._is_asc = is_asc

    @property
    def dept_code(self):
        """Gets the dept_code of this SearchUsersRequest.


        :return: The dept_code of this SearchUsersRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this SearchUsersRequest.


        :param dept_code: The dept_code of this SearchUsersRequest.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def enable_sub_dept(self):
        """Gets the enable_sub_dept of this SearchUsersRequest.


        :return: The enable_sub_dept of this SearchUsersRequest.
        :rtype: bool
        """
        return self._enable_sub_dept

    @enable_sub_dept.setter
    def enable_sub_dept(self, enable_sub_dept):
        """Sets the enable_sub_dept of this SearchUsersRequest.


        :param enable_sub_dept: The enable_sub_dept of this SearchUsersRequest.
        :type: bool
        """
        self._enable_sub_dept = enable_sub_dept

    @property
    def admin_type(self):
        """Gets the admin_type of this SearchUsersRequest.


        :return: The admin_type of this SearchUsersRequest.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this SearchUsersRequest.


        :param admin_type: The admin_type of this SearchUsersRequest.
        :type: int
        """
        self._admin_type = admin_type

    @property
    def enable_room(self):
        """Gets the enable_room of this SearchUsersRequest.


        :return: The enable_room of this SearchUsersRequest.
        :rtype: bool
        """
        return self._enable_room

    @enable_room.setter
    def enable_room(self, enable_room):
        """Sets the enable_room of this SearchUsersRequest.


        :param enable_room: The enable_room of this SearchUsersRequest.
        :type: bool
        """
        self._enable_room = enable_room

    @property
    def user_type(self):
        """Gets the user_type of this SearchUsersRequest.


        :return: The user_type of this SearchUsersRequest.
        :rtype: list[int]
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this SearchUsersRequest.


        :param user_type: The user_type of this SearchUsersRequest.
        :type: list[int]
        """
        self._user_type = user_type

    @property
    def status(self):
        """Gets the status of this SearchUsersRequest.


        :return: The status of this SearchUsersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchUsersRequest.


        :param status: The status of this SearchUsersRequest.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, SearchUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
