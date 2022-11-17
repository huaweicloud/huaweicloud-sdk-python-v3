# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'status': 'int',
        'contains_un_active': 'bool'
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
        'status': 'status',
        'contains_un_active': 'containsUnActive'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, sort_field=None, is_asc=None, dept_code=None, enable_sub_dept=None, admin_type=None, enable_room=None, user_type=None, status=None, contains_un_active=None):
        """SearchUsersRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页。
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件，支持名称、手机、邮箱、帐号、第三方帐号模糊搜索。
        :type search_key: str
        :param sort_field: 排序字段名称 支持的取值： - userType - adminType - ldapAccount - deptCode - status - sortLevel
        :type sort_field: str
        :param is_asc: 是否按升序排序。
        :type is_asc: bool
        :param dept_code: 部门编码，不带则查询所有。
        :type dept_code: str
        :param enable_sub_dept: 是否查询子部门。 默认值: true 
        :type enable_sub_dept: bool
        :param admin_type: 根据管理员类型查询。 * 1：普通管理员 * 2：非管理员 
        :type admin_type: int
        :param enable_room: 是否开启智能协同白板功能功能位，不带则搜索所有。 &gt; 该参数将废弃，请勿使用。 
        :type enable_room: bool
        :param user_type: 用户类型。默认2。 * 2：普通用户 * 12：智慧屏用户 * 13：ideaHub用户 * 14: SmartRooms用户 
        :type user_type: list[int]
        :param status: 用户状态。不带则查询所有。 * 0：正常 * 1：停用。 
        :type status: int
        :param contains_un_active: 是否查询未激活的终端。 默认值: false 
        :type contains_un_active: bool
        """
        
        

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
        self._contains_un_active = None
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
        if contains_un_active is not None:
            self.contains_un_active = contains_un_active

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchUsersRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchUsersRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchUsersRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchUsersRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchUsersRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchUsersRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchUsersRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchUsersRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchUsersRequest.

        查询偏移量,若超过最大数量，则返回最后一页。

        :return: The offset of this SearchUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchUsersRequest.

        查询偏移量,若超过最大数量，则返回最后一页。

        :param offset: The offset of this SearchUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchUsersRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchUsersRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchUsersRequest.

        搜索条件，支持名称、手机、邮箱、帐号、第三方帐号模糊搜索。

        :return: The search_key of this SearchUsersRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchUsersRequest.

        搜索条件，支持名称、手机、邮箱、帐号、第三方帐号模糊搜索。

        :param search_key: The search_key of this SearchUsersRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def sort_field(self):
        """Gets the sort_field of this SearchUsersRequest.

        排序字段名称 支持的取值： - userType - adminType - ldapAccount - deptCode - status - sortLevel

        :return: The sort_field of this SearchUsersRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this SearchUsersRequest.

        排序字段名称 支持的取值： - userType - adminType - ldapAccount - deptCode - status - sortLevel

        :param sort_field: The sort_field of this SearchUsersRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def is_asc(self):
        """Gets the is_asc of this SearchUsersRequest.

        是否按升序排序。

        :return: The is_asc of this SearchUsersRequest.
        :rtype: bool
        """
        return self._is_asc

    @is_asc.setter
    def is_asc(self, is_asc):
        """Sets the is_asc of this SearchUsersRequest.

        是否按升序排序。

        :param is_asc: The is_asc of this SearchUsersRequest.
        :type is_asc: bool
        """
        self._is_asc = is_asc

    @property
    def dept_code(self):
        """Gets the dept_code of this SearchUsersRequest.

        部门编码，不带则查询所有。

        :return: The dept_code of this SearchUsersRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this SearchUsersRequest.

        部门编码，不带则查询所有。

        :param dept_code: The dept_code of this SearchUsersRequest.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def enable_sub_dept(self):
        """Gets the enable_sub_dept of this SearchUsersRequest.

        是否查询子部门。 默认值: true 

        :return: The enable_sub_dept of this SearchUsersRequest.
        :rtype: bool
        """
        return self._enable_sub_dept

    @enable_sub_dept.setter
    def enable_sub_dept(self, enable_sub_dept):
        """Sets the enable_sub_dept of this SearchUsersRequest.

        是否查询子部门。 默认值: true 

        :param enable_sub_dept: The enable_sub_dept of this SearchUsersRequest.
        :type enable_sub_dept: bool
        """
        self._enable_sub_dept = enable_sub_dept

    @property
    def admin_type(self):
        """Gets the admin_type of this SearchUsersRequest.

        根据管理员类型查询。 * 1：普通管理员 * 2：非管理员 

        :return: The admin_type of this SearchUsersRequest.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this SearchUsersRequest.

        根据管理员类型查询。 * 1：普通管理员 * 2：非管理员 

        :param admin_type: The admin_type of this SearchUsersRequest.
        :type admin_type: int
        """
        self._admin_type = admin_type

    @property
    def enable_room(self):
        """Gets the enable_room of this SearchUsersRequest.

        是否开启智能协同白板功能功能位，不带则搜索所有。 > 该参数将废弃，请勿使用。 

        :return: The enable_room of this SearchUsersRequest.
        :rtype: bool
        """
        return self._enable_room

    @enable_room.setter
    def enable_room(self, enable_room):
        """Sets the enable_room of this SearchUsersRequest.

        是否开启智能协同白板功能功能位，不带则搜索所有。 > 该参数将废弃，请勿使用。 

        :param enable_room: The enable_room of this SearchUsersRequest.
        :type enable_room: bool
        """
        self._enable_room = enable_room

    @property
    def user_type(self):
        """Gets the user_type of this SearchUsersRequest.

        用户类型。默认2。 * 2：普通用户 * 12：智慧屏用户 * 13：ideaHub用户 * 14: SmartRooms用户 

        :return: The user_type of this SearchUsersRequest.
        :rtype: list[int]
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this SearchUsersRequest.

        用户类型。默认2。 * 2：普通用户 * 12：智慧屏用户 * 13：ideaHub用户 * 14: SmartRooms用户 

        :param user_type: The user_type of this SearchUsersRequest.
        :type user_type: list[int]
        """
        self._user_type = user_type

    @property
    def status(self):
        """Gets the status of this SearchUsersRequest.

        用户状态。不带则查询所有。 * 0：正常 * 1：停用。 

        :return: The status of this SearchUsersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchUsersRequest.

        用户状态。不带则查询所有。 * 0：正常 * 1：停用。 

        :param status: The status of this SearchUsersRequest.
        :type status: int
        """
        self._status = status

    @property
    def contains_un_active(self):
        """Gets the contains_un_active of this SearchUsersRequest.

        是否查询未激活的终端。 默认值: false 

        :return: The contains_un_active of this SearchUsersRequest.
        :rtype: bool
        """
        return self._contains_un_active

    @contains_un_active.setter
    def contains_un_active(self, contains_un_active):
        """Sets the contains_un_active of this SearchUsersRequest.

        是否查询未激活的终端。 默认值: false 

        :param contains_un_active: The contains_un_active of this SearchUsersRequest.
        :type contains_un_active: bool
        """
        self._contains_un_active = contains_un_active

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
        if not isinstance(other, SearchUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
