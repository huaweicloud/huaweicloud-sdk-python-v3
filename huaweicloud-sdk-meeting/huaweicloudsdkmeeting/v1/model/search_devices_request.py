# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDevicesRequest:

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
        'model': 'str',
        'dept_code': 'str',
        'enable_sub_dept': 'bool'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'model': 'model',
        'dept_code': 'deptCode',
        'enable_sub_dept': 'enableSubDept'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, model=None, dept_code=None, enable_sub_dept=None):
        """SearchDevicesRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量，若超过最大数量，则返回最后一页。
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件。支持名称、SN模糊查询。
        :type search_key: str
        :param model: 终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。
        :type model: str
        :param dept_code: 部门编码，默认为根部门。 默认值：1。
        :type dept_code: str
        :param enable_sub_dept: 是否查询子部门。 默认值：true。 
        :type enable_sub_dept: bool
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._model = None
        self._dept_code = None
        self._enable_sub_dept = None
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
        if model is not None:
            self.model = model
        if dept_code is not None:
            self.dept_code = dept_code
        if enable_sub_dept is not None:
            self.enable_sub_dept = enable_sub_dept

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchDevicesRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchDevicesRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchDevicesRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchDevicesRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchDevicesRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchDevicesRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchDevicesRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchDevicesRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchDevicesRequest.

        查询偏移量，若超过最大数量，则返回最后一页。

        :return: The offset of this SearchDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchDevicesRequest.

        查询偏移量，若超过最大数量，则返回最后一页。

        :param offset: The offset of this SearchDevicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchDevicesRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchDevicesRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchDevicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchDevicesRequest.

        搜索条件。支持名称、SN模糊查询。

        :return: The search_key of this SearchDevicesRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchDevicesRequest.

        搜索条件。支持名称、SN模糊查询。

        :param search_key: The search_key of this SearchDevicesRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def model(self):
        """Gets the model of this SearchDevicesRequest.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :return: The model of this SearchDevicesRequest.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SearchDevicesRequest.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :param model: The model of this SearchDevicesRequest.
        :type model: str
        """
        self._model = model

    @property
    def dept_code(self):
        """Gets the dept_code of this SearchDevicesRequest.

        部门编码，默认为根部门。 默认值：1。

        :return: The dept_code of this SearchDevicesRequest.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this SearchDevicesRequest.

        部门编码，默认为根部门。 默认值：1。

        :param dept_code: The dept_code of this SearchDevicesRequest.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def enable_sub_dept(self):
        """Gets the enable_sub_dept of this SearchDevicesRequest.

        是否查询子部门。 默认值：true。 

        :return: The enable_sub_dept of this SearchDevicesRequest.
        :rtype: bool
        """
        return self._enable_sub_dept

    @enable_sub_dept.setter
    def enable_sub_dept(self, enable_sub_dept):
        """Sets the enable_sub_dept of this SearchDevicesRequest.

        是否查询子部门。 默认值：true。 

        :param enable_sub_dept: The enable_sub_dept of this SearchDevicesRequest.
        :type enable_sub_dept: bool
        """
        self._enable_sub_dept = enable_sub_dept

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
        if not isinstance(other, SearchDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
