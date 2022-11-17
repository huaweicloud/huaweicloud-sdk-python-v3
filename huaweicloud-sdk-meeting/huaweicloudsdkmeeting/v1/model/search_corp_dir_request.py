# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, dept_code=None, query_sub_dept=None, search_scope=None):
        """SearchCorpDirRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件。支持帐号、SIP号码、名称、手机、邮箱模糊搜索。
        :type search_key: str
        :param dept_code: 部门编码。 
        :type dept_code: str
        :param query_sub_dept: 是否查询子部门下的用户。 默认值：true。 
        :type query_sub_dept: bool
        :param search_scope: 搜索范围。默认值为ALL。 * NORMAL_USER - 查询普通用户。返回普通用户（响应中isHardTerminal&#x3D;false，type&#x3D;NORMAL_USER） * HARD_TERMINAL - 查询硬终端用户。返回大屏用户（响应中isHardTerminal&#x3D;false，type&#x3D;WHITE_BOARD）和硬终端用户（响应中isHardTerminal&#x3D;true，type&#x3D;HARD_TERMINAL） * ALL - 查询所有用户。 
        :type search_scope: str
        """
        
        

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

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchCorpDirRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchCorpDirRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchCorpDirRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchCorpDirRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchCorpDirRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchCorpDirRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :return: The offset of this SearchCorpDirRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchCorpDirRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :param offset: The offset of this SearchCorpDirRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchCorpDirRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchCorpDirRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchCorpDirRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchCorpDirRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchCorpDirRequest.

        搜索条件。支持帐号、SIP号码、名称、手机、邮箱模糊搜索。

        :return: The search_key of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchCorpDirRequest.

        搜索条件。支持帐号、SIP号码、名称、手机、邮箱模糊搜索。

        :param search_key: The search_key of this SearchCorpDirRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def dept_code(self):
        """Gets the dept_code of this SearchCorpDirRequest.

        部门编码。 

        :return: The dept_code of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this SearchCorpDirRequest.

        部门编码。 

        :param dept_code: The dept_code of this SearchCorpDirRequest.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def query_sub_dept(self):
        """Gets the query_sub_dept of this SearchCorpDirRequest.

        是否查询子部门下的用户。 默认值：true。 

        :return: The query_sub_dept of this SearchCorpDirRequest.
        :rtype: bool
        """
        return self._query_sub_dept

    @query_sub_dept.setter
    def query_sub_dept(self, query_sub_dept):
        """Sets the query_sub_dept of this SearchCorpDirRequest.

        是否查询子部门下的用户。 默认值：true。 

        :param query_sub_dept: The query_sub_dept of this SearchCorpDirRequest.
        :type query_sub_dept: bool
        """
        self._query_sub_dept = query_sub_dept

    @property
    def search_scope(self):
        """Gets the search_scope of this SearchCorpDirRequest.

        搜索范围。默认值为ALL。 * NORMAL_USER - 查询普通用户。返回普通用户（响应中isHardTerminal=false，type=NORMAL_USER） * HARD_TERMINAL - 查询硬终端用户。返回大屏用户（响应中isHardTerminal=false，type=WHITE_BOARD）和硬终端用户（响应中isHardTerminal=true，type=HARD_TERMINAL） * ALL - 查询所有用户。 

        :return: The search_scope of this SearchCorpDirRequest.
        :rtype: str
        """
        return self._search_scope

    @search_scope.setter
    def search_scope(self, search_scope):
        """Sets the search_scope of this SearchCorpDirRequest.

        搜索范围。默认值为ALL。 * NORMAL_USER - 查询普通用户。返回普通用户（响应中isHardTerminal=false，type=NORMAL_USER） * HARD_TERMINAL - 查询硬终端用户。返回大屏用户（响应中isHardTerminal=false，type=WHITE_BOARD）和硬终端用户（响应中isHardTerminal=true，type=HARD_TERMINAL） * ALL - 查询所有用户。 

        :param search_scope: The search_scope of this SearchCorpDirRequest.
        :type search_scope: str
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
        if not isinstance(other, SearchCorpDirRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
