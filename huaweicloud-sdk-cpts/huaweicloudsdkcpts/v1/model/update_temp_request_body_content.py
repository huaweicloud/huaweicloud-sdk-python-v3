# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTempRequestBodyContent:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'http_version': 'str',
        'method': 'str',
        'connect_timeout': 'int',
        'return_timeout': 'int',
        'return_timeout_param': 'str',
        'connect_type': 'int',
        'check_end_type': 'str',
        'check_end_length': 'str',
        'check_end_str': 'str',
        'name': 'str',
        'protocol_type': 'int',
        'headers': 'list[UpdateCaseRequestBodyContentHeaders]',
        'body': 'str',
        'bodys': 'list[str]',
        'body_type': 'int'
    }

    attribute_map = {
        'url': 'url',
        'http_version': 'http_version',
        'method': 'method',
        'connect_timeout': 'connect_timeout',
        'return_timeout': 'return_timeout',
        'return_timeout_param': 'return_timeout_param',
        'connect_type': 'connect_type',
        'check_end_type': 'check_end_type',
        'check_end_length': 'check_end_length',
        'check_end_str': 'check_end_str',
        'name': 'name',
        'protocol_type': 'protocol_type',
        'headers': 'headers',
        'body': 'body',
        'bodys': 'bodys',
        'body_type': 'body_type'
    }

    def __init__(self, url=None, http_version=None, method=None, connect_timeout=None, return_timeout=None, return_timeout_param=None, connect_type=None, check_end_type=None, check_end_length=None, check_end_str=None, name=None, protocol_type=None, headers=None, body=None, bodys=None, body_type=None):
        """UpdateTempRequestBodyContent - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._http_version = None
        self._method = None
        self._connect_timeout = None
        self._return_timeout = None
        self._return_timeout_param = None
        self._connect_type = None
        self._check_end_type = None
        self._check_end_length = None
        self._check_end_str = None
        self._name = None
        self._protocol_type = None
        self._headers = None
        self._body = None
        self._bodys = None
        self._body_type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if http_version is not None:
            self.http_version = http_version
        if method is not None:
            self.method = method
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if return_timeout is not None:
            self.return_timeout = return_timeout
        if return_timeout_param is not None:
            self.return_timeout_param = return_timeout_param
        if connect_type is not None:
            self.connect_type = connect_type
        if check_end_type is not None:
            self.check_end_type = check_end_type
        if check_end_length is not None:
            self.check_end_length = check_end_length
        if check_end_str is not None:
            self.check_end_str = check_end_str
        if name is not None:
            self.name = name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body
        if bodys is not None:
            self.bodys = bodys
        if body_type is not None:
            self.body_type = body_type

    @property
    def url(self):
        """Gets the url of this UpdateTempRequestBodyContent.

        url

        :return: The url of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateTempRequestBodyContent.

        url

        :param url: The url of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._url = url

    @property
    def http_version(self):
        """Gets the http_version of this UpdateTempRequestBodyContent.

        http_version

        :return: The http_version of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._http_version

    @http_version.setter
    def http_version(self, http_version):
        """Sets the http_version of this UpdateTempRequestBodyContent.

        http_version

        :param http_version: The http_version of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._http_version = http_version

    @property
    def method(self):
        """Gets the method of this UpdateTempRequestBodyContent.

        method

        :return: The method of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this UpdateTempRequestBodyContent.

        method

        :param method: The method of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._method = method

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this UpdateTempRequestBodyContent.

        connect_timeout

        :return: The connect_timeout of this UpdateTempRequestBodyContent.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this UpdateTempRequestBodyContent.

        connect_timeout

        :param connect_timeout: The connect_timeout of this UpdateTempRequestBodyContent.
        :type: int
        """
        self._connect_timeout = connect_timeout

    @property
    def return_timeout(self):
        """Gets the return_timeout of this UpdateTempRequestBodyContent.

        return_timeout

        :return: The return_timeout of this UpdateTempRequestBodyContent.
        :rtype: int
        """
        return self._return_timeout

    @return_timeout.setter
    def return_timeout(self, return_timeout):
        """Sets the return_timeout of this UpdateTempRequestBodyContent.

        return_timeout

        :param return_timeout: The return_timeout of this UpdateTempRequestBodyContent.
        :type: int
        """
        self._return_timeout = return_timeout

    @property
    def return_timeout_param(self):
        """Gets the return_timeout_param of this UpdateTempRequestBodyContent.

        return_timeout_param

        :return: The return_timeout_param of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._return_timeout_param

    @return_timeout_param.setter
    def return_timeout_param(self, return_timeout_param):
        """Sets the return_timeout_param of this UpdateTempRequestBodyContent.

        return_timeout_param

        :param return_timeout_param: The return_timeout_param of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._return_timeout_param = return_timeout_param

    @property
    def connect_type(self):
        """Gets the connect_type of this UpdateTempRequestBodyContent.

        connect_type

        :return: The connect_type of this UpdateTempRequestBodyContent.
        :rtype: int
        """
        return self._connect_type

    @connect_type.setter
    def connect_type(self, connect_type):
        """Sets the connect_type of this UpdateTempRequestBodyContent.

        connect_type

        :param connect_type: The connect_type of this UpdateTempRequestBodyContent.
        :type: int
        """
        self._connect_type = connect_type

    @property
    def check_end_type(self):
        """Gets the check_end_type of this UpdateTempRequestBodyContent.

        check_end_type

        :return: The check_end_type of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._check_end_type

    @check_end_type.setter
    def check_end_type(self, check_end_type):
        """Sets the check_end_type of this UpdateTempRequestBodyContent.

        check_end_type

        :param check_end_type: The check_end_type of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._check_end_type = check_end_type

    @property
    def check_end_length(self):
        """Gets the check_end_length of this UpdateTempRequestBodyContent.

        check_end_length

        :return: The check_end_length of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._check_end_length

    @check_end_length.setter
    def check_end_length(self, check_end_length):
        """Sets the check_end_length of this UpdateTempRequestBodyContent.

        check_end_length

        :param check_end_length: The check_end_length of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._check_end_length = check_end_length

    @property
    def check_end_str(self):
        """Gets the check_end_str of this UpdateTempRequestBodyContent.

        check_end_str

        :return: The check_end_str of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._check_end_str

    @check_end_str.setter
    def check_end_str(self, check_end_str):
        """Sets the check_end_str of this UpdateTempRequestBodyContent.

        check_end_str

        :param check_end_str: The check_end_str of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._check_end_str = check_end_str

    @property
    def name(self):
        """Gets the name of this UpdateTempRequestBodyContent.

        name

        :return: The name of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTempRequestBodyContent.

        name

        :param name: The name of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._name = name

    @property
    def protocol_type(self):
        """Gets the protocol_type of this UpdateTempRequestBodyContent.

        protocol_type

        :return: The protocol_type of this UpdateTempRequestBodyContent.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this UpdateTempRequestBodyContent.

        protocol_type

        :param protocol_type: The protocol_type of this UpdateTempRequestBodyContent.
        :type: int
        """
        self._protocol_type = protocol_type

    @property
    def headers(self):
        """Gets the headers of this UpdateTempRequestBodyContent.

        headers

        :return: The headers of this UpdateTempRequestBodyContent.
        :rtype: list[UpdateCaseRequestBodyContentHeaders]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this UpdateTempRequestBodyContent.

        headers

        :param headers: The headers of this UpdateTempRequestBodyContent.
        :type: list[UpdateCaseRequestBodyContentHeaders]
        """
        self._headers = headers

    @property
    def body(self):
        """Gets the body of this UpdateTempRequestBodyContent.

        body

        :return: The body of this UpdateTempRequestBodyContent.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTempRequestBodyContent.

        body

        :param body: The body of this UpdateTempRequestBodyContent.
        :type: str
        """
        self._body = body

    @property
    def bodys(self):
        """Gets the bodys of this UpdateTempRequestBodyContent.

        bodys

        :return: The bodys of this UpdateTempRequestBodyContent.
        :rtype: list[str]
        """
        return self._bodys

    @bodys.setter
    def bodys(self, bodys):
        """Sets the bodys of this UpdateTempRequestBodyContent.

        bodys

        :param bodys: The bodys of this UpdateTempRequestBodyContent.
        :type: list[str]
        """
        self._bodys = bodys

    @property
    def body_type(self):
        """Gets the body_type of this UpdateTempRequestBodyContent.

        body_type

        :return: The body_type of this UpdateTempRequestBodyContent.
        :rtype: int
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this UpdateTempRequestBodyContent.

        body_type

        :param body_type: The body_type of this UpdateTempRequestBodyContent.
        :type: int
        """
        self._body_type = body_type

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
        if not isinstance(other, UpdateTempRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
