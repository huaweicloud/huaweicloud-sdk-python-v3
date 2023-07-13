# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'port': 'str',
        'port_type': 'int',
        'sign_search': 'str',
        'offset': 'int',
        'limit': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'pub_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'port': 'port',
        'port_type': 'port_type',
        'sign_search': 'sign_search',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'pub_name': 'pub_name'
    }

    def __init__(self, type=None, port=None, port_type=None, sign_search=None, offset=None, limit=None, start_time=None, end_time=None, pub_name=None):
        """ListPortInfosRequest

        The model defined in huaweicloud sdk

        :param type: 操作类型。 - 0：查询通道号列表 - 1：查询绑定关系列表 
        :type type: int
        :param port: 通道号。 
        :type port: str
        :param port_type: 通道号类型。 - 1：普通 - 3：前缀号段  - 5：后缀号段 
        :type port_type: int
        :param sign_search: 单个通道号签名。  &gt; 不支持多个签名查询，支持模糊搜索。长度要求0-18。 
        :type sign_search: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param start_time: 开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type start_time: datetime
        :param end_time: 结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type end_time: datetime
        :param pub_name: 服务号名称。  &gt; - type&#x3D;1时，此字段作为过滤条件 &gt; - type&#x3D;0时，不作为过滤条件 
        :type pub_name: str
        """
        
        

        self._type = None
        self._port = None
        self._port_type = None
        self._sign_search = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self._pub_name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if port is not None:
            self.port = port
        if port_type is not None:
            self.port_type = port_type
        if sign_search is not None:
            self.sign_search = sign_search
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if pub_name is not None:
            self.pub_name = pub_name

    @property
    def type(self):
        """Gets the type of this ListPortInfosRequest.

        操作类型。 - 0：查询通道号列表 - 1：查询绑定关系列表 

        :return: The type of this ListPortInfosRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPortInfosRequest.

        操作类型。 - 0：查询通道号列表 - 1：查询绑定关系列表 

        :param type: The type of this ListPortInfosRequest.
        :type type: int
        """
        self._type = type

    @property
    def port(self):
        """Gets the port of this ListPortInfosRequest.

        通道号。 

        :return: The port of this ListPortInfosRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListPortInfosRequest.

        通道号。 

        :param port: The port of this ListPortInfosRequest.
        :type port: str
        """
        self._port = port

    @property
    def port_type(self):
        """Gets the port_type of this ListPortInfosRequest.

        通道号类型。 - 1：普通 - 3：前缀号段  - 5：后缀号段 

        :return: The port_type of this ListPortInfosRequest.
        :rtype: int
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this ListPortInfosRequest.

        通道号类型。 - 1：普通 - 3：前缀号段  - 5：后缀号段 

        :param port_type: The port_type of this ListPortInfosRequest.
        :type port_type: int
        """
        self._port_type = port_type

    @property
    def sign_search(self):
        """Gets the sign_search of this ListPortInfosRequest.

        单个通道号签名。  > 不支持多个签名查询，支持模糊搜索。长度要求0-18。 

        :return: The sign_search of this ListPortInfosRequest.
        :rtype: str
        """
        return self._sign_search

    @sign_search.setter
    def sign_search(self, sign_search):
        """Sets the sign_search of this ListPortInfosRequest.

        单个通道号签名。  > 不支持多个签名查询，支持模糊搜索。长度要求0-18。 

        :param sign_search: The sign_search of this ListPortInfosRequest.
        :type sign_search: str
        """
        self._sign_search = sign_search

    @property
    def offset(self):
        """Gets the offset of this ListPortInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListPortInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPortInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListPortInfosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPortInfosRequest.

        每页显示的条目数量。

        :return: The limit of this ListPortInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortInfosRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPortInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListPortInfosRequest.

        开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The start_time of this ListPortInfosRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListPortInfosRequest.

        开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param start_time: The start_time of this ListPortInfosRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListPortInfosRequest.

        结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The end_time of this ListPortInfosRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListPortInfosRequest.

        结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param end_time: The end_time of this ListPortInfosRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def pub_name(self):
        """Gets the pub_name of this ListPortInfosRequest.

        服务号名称。  > - type=1时，此字段作为过滤条件 > - type=0时，不作为过滤条件 

        :return: The pub_name of this ListPortInfosRequest.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this ListPortInfosRequest.

        服务号名称。  > - type=1时，此字段作为过滤条件 > - type=0时，不作为过滤条件 

        :param pub_name: The pub_name of this ListPortInfosRequest.
        :type pub_name: str
        """
        self._pub_name = pub_name

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
        if not isinstance(other, ListPortInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
