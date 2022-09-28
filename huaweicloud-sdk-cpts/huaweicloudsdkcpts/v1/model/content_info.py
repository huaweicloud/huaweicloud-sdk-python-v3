# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'body_type': 'int',
        'bodys': 'list[object]',
        'check_end_length': 'object',
        'check_end_str': 'object',
        'check_end_type': 'object',
        'connect_timeout': 'int',
        'connect_type': 'int',
        'headers': 'list[ContentHeader]',
        'http_version': 'str',
        'method': 'str',
        'name': 'str',
        'protocol_type': 'int',
        'return_timeout': 'int',
        'return_timeout_param': 'str',
        'url': 'str'
    }

    attribute_map = {
        'body_type': 'body_type',
        'bodys': 'bodys',
        'check_end_length': 'check_end_length',
        'check_end_str': 'check_end_str',
        'check_end_type': 'check_end_type',
        'connect_timeout': 'connect_timeout',
        'connect_type': 'connect_type',
        'headers': 'headers',
        'http_version': 'http_version',
        'method': 'method',
        'name': 'name',
        'protocol_type': 'protocol_type',
        'return_timeout': 'return_timeout',
        'return_timeout_param': 'return_timeout_param',
        'url': 'url'
    }

    def __init__(self, body_type=None, bodys=None, check_end_length=None, check_end_str=None, check_end_type=None, connect_timeout=None, connect_type=None, headers=None, http_version=None, method=None, name=None, protocol_type=None, return_timeout=None, return_timeout_param=None, url=None):
        """ContentInfo

        The model defined in huaweicloud sdk

        :param body_type: body_type
        :type body_type: int
        :param bodys: bodys
        :type bodys: list[object]
        :param check_end_length: TCP/UDP协议返回数据长度
        :type check_end_length: object
        :param check_end_str: TCP/UDP协议返回结束符
        :type check_end_str: object
        :param check_end_type: TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符
        :type check_end_type: object
        :param connect_timeout: connect_timeout
        :type connect_timeout: int
        :param connect_type: connect_type
        :type connect_type: int
        :param headers: headers
        :type headers: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        :param http_version: http_version
        :type http_version: str
        :param method: method
        :type method: str
        :param name: name
        :type name: str
        :param protocol_type: protocol_type
        :type protocol_type: int
        :param return_timeout: return_timeout
        :type return_timeout: int
        :param return_timeout_param: return_timeout_param
        :type return_timeout_param: str
        :param url: url
        :type url: str
        """
        
        

        self._body_type = None
        self._bodys = None
        self._check_end_length = None
        self._check_end_str = None
        self._check_end_type = None
        self._connect_timeout = None
        self._connect_type = None
        self._headers = None
        self._http_version = None
        self._method = None
        self._name = None
        self._protocol_type = None
        self._return_timeout = None
        self._return_timeout_param = None
        self._url = None
        self.discriminator = None

        if body_type is not None:
            self.body_type = body_type
        if bodys is not None:
            self.bodys = bodys
        if check_end_length is not None:
            self.check_end_length = check_end_length
        if check_end_str is not None:
            self.check_end_str = check_end_str
        if check_end_type is not None:
            self.check_end_type = check_end_type
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if connect_type is not None:
            self.connect_type = connect_type
        if headers is not None:
            self.headers = headers
        if http_version is not None:
            self.http_version = http_version
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if return_timeout is not None:
            self.return_timeout = return_timeout
        if return_timeout_param is not None:
            self.return_timeout_param = return_timeout_param
        if url is not None:
            self.url = url

    @property
    def body_type(self):
        """Gets the body_type of this ContentInfo.

        body_type

        :return: The body_type of this ContentInfo.
        :rtype: int
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this ContentInfo.

        body_type

        :param body_type: The body_type of this ContentInfo.
        :type body_type: int
        """
        self._body_type = body_type

    @property
    def bodys(self):
        """Gets the bodys of this ContentInfo.

        bodys

        :return: The bodys of this ContentInfo.
        :rtype: list[object]
        """
        return self._bodys

    @bodys.setter
    def bodys(self, bodys):
        """Sets the bodys of this ContentInfo.

        bodys

        :param bodys: The bodys of this ContentInfo.
        :type bodys: list[object]
        """
        self._bodys = bodys

    @property
    def check_end_length(self):
        """Gets the check_end_length of this ContentInfo.

        TCP/UDP协议返回数据长度

        :return: The check_end_length of this ContentInfo.
        :rtype: object
        """
        return self._check_end_length

    @check_end_length.setter
    def check_end_length(self, check_end_length):
        """Sets the check_end_length of this ContentInfo.

        TCP/UDP协议返回数据长度

        :param check_end_length: The check_end_length of this ContentInfo.
        :type check_end_length: object
        """
        self._check_end_length = check_end_length

    @property
    def check_end_str(self):
        """Gets the check_end_str of this ContentInfo.

        TCP/UDP协议返回结束符

        :return: The check_end_str of this ContentInfo.
        :rtype: object
        """
        return self._check_end_str

    @check_end_str.setter
    def check_end_str(self, check_end_str):
        """Sets the check_end_str of this ContentInfo.

        TCP/UDP协议返回结束符

        :param check_end_str: The check_end_str of this ContentInfo.
        :type check_end_str: object
        """
        self._check_end_str = check_end_str

    @property
    def check_end_type(self):
        """Gets the check_end_type of this ContentInfo.

        TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符

        :return: The check_end_type of this ContentInfo.
        :rtype: object
        """
        return self._check_end_type

    @check_end_type.setter
    def check_end_type(self, check_end_type):
        """Sets the check_end_type of this ContentInfo.

        TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符

        :param check_end_type: The check_end_type of this ContentInfo.
        :type check_end_type: object
        """
        self._check_end_type = check_end_type

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this ContentInfo.

        connect_timeout

        :return: The connect_timeout of this ContentInfo.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this ContentInfo.

        connect_timeout

        :param connect_timeout: The connect_timeout of this ContentInfo.
        :type connect_timeout: int
        """
        self._connect_timeout = connect_timeout

    @property
    def connect_type(self):
        """Gets the connect_type of this ContentInfo.

        connect_type

        :return: The connect_type of this ContentInfo.
        :rtype: int
        """
        return self._connect_type

    @connect_type.setter
    def connect_type(self, connect_type):
        """Sets the connect_type of this ContentInfo.

        connect_type

        :param connect_type: The connect_type of this ContentInfo.
        :type connect_type: int
        """
        self._connect_type = connect_type

    @property
    def headers(self):
        """Gets the headers of this ContentInfo.

        headers

        :return: The headers of this ContentInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ContentInfo.

        headers

        :param headers: The headers of this ContentInfo.
        :type headers: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        """
        self._headers = headers

    @property
    def http_version(self):
        """Gets the http_version of this ContentInfo.

        http_version

        :return: The http_version of this ContentInfo.
        :rtype: str
        """
        return self._http_version

    @http_version.setter
    def http_version(self, http_version):
        """Sets the http_version of this ContentInfo.

        http_version

        :param http_version: The http_version of this ContentInfo.
        :type http_version: str
        """
        self._http_version = http_version

    @property
    def method(self):
        """Gets the method of this ContentInfo.

        method

        :return: The method of this ContentInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ContentInfo.

        method

        :param method: The method of this ContentInfo.
        :type method: str
        """
        self._method = method

    @property
    def name(self):
        """Gets the name of this ContentInfo.

        name

        :return: The name of this ContentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentInfo.

        name

        :param name: The name of this ContentInfo.
        :type name: str
        """
        self._name = name

    @property
    def protocol_type(self):
        """Gets the protocol_type of this ContentInfo.

        protocol_type

        :return: The protocol_type of this ContentInfo.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this ContentInfo.

        protocol_type

        :param protocol_type: The protocol_type of this ContentInfo.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def return_timeout(self):
        """Gets the return_timeout of this ContentInfo.

        return_timeout

        :return: The return_timeout of this ContentInfo.
        :rtype: int
        """
        return self._return_timeout

    @return_timeout.setter
    def return_timeout(self, return_timeout):
        """Sets the return_timeout of this ContentInfo.

        return_timeout

        :param return_timeout: The return_timeout of this ContentInfo.
        :type return_timeout: int
        """
        self._return_timeout = return_timeout

    @property
    def return_timeout_param(self):
        """Gets the return_timeout_param of this ContentInfo.

        return_timeout_param

        :return: The return_timeout_param of this ContentInfo.
        :rtype: str
        """
        return self._return_timeout_param

    @return_timeout_param.setter
    def return_timeout_param(self, return_timeout_param):
        """Sets the return_timeout_param of this ContentInfo.

        return_timeout_param

        :param return_timeout_param: The return_timeout_param of this ContentInfo.
        :type return_timeout_param: str
        """
        self._return_timeout_param = return_timeout_param

    @property
    def url(self):
        """Gets the url of this ContentInfo.

        url

        :return: The url of this ContentInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContentInfo.

        url

        :param url: The url of this ContentInfo.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
