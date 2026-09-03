# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtocolReqVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic': 'BasicInfoVo',
        'headers': 'dict(str, str)',
        'method': 'str',
        'request_body': 'str',
        'url': 'str'
    }

    attribute_map = {
        'basic': 'basic',
        'headers': 'headers',
        'method': 'method',
        'request_body': 'request_body',
        'url': 'url'
    }

    def __init__(self, basic=None, headers=None, method=None, request_body=None, url=None):
        r"""ProtocolReqVo

        The model defined in huaweicloud sdk

        :param basic: 
        :type basic: :class:`huaweicloudsdkcloudtest.v1.BasicInfoVo`
        :param headers: 请求头
        :type headers: dict(str, str)
        :param method: 方法
        :type method: str
        :param request_body: 请求body体
        :type request_body: str
        :param url: url
        :type url: str
        """
        
        

        self._basic = None
        self._headers = None
        self._method = None
        self._request_body = None
        self._url = None
        self.discriminator = None

        if basic is not None:
            self.basic = basic
        if headers is not None:
            self.headers = headers
        if method is not None:
            self.method = method
        if request_body is not None:
            self.request_body = request_body
        if url is not None:
            self.url = url

    @property
    def basic(self):
        r"""Gets the basic of this ProtocolReqVo.

        :return: The basic of this ProtocolReqVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.BasicInfoVo`
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        r"""Sets the basic of this ProtocolReqVo.

        :param basic: The basic of this ProtocolReqVo.
        :type basic: :class:`huaweicloudsdkcloudtest.v1.BasicInfoVo`
        """
        self._basic = basic

    @property
    def headers(self):
        r"""Gets the headers of this ProtocolReqVo.

        请求头

        :return: The headers of this ProtocolReqVo.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this ProtocolReqVo.

        请求头

        :param headers: The headers of this ProtocolReqVo.
        :type headers: dict(str, str)
        """
        self._headers = headers

    @property
    def method(self):
        r"""Gets the method of this ProtocolReqVo.

        方法

        :return: The method of this ProtocolReqVo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this ProtocolReqVo.

        方法

        :param method: The method of this ProtocolReqVo.
        :type method: str
        """
        self._method = method

    @property
    def request_body(self):
        r"""Gets the request_body of this ProtocolReqVo.

        请求body体

        :return: The request_body of this ProtocolReqVo.
        :rtype: str
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        r"""Sets the request_body of this ProtocolReqVo.

        请求body体

        :param request_body: The request_body of this ProtocolReqVo.
        :type request_body: str
        """
        self._request_body = request_body

    @property
    def url(self):
        r"""Gets the url of this ProtocolReqVo.

        url

        :return: The url of this ProtocolReqVo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ProtocolReqVo.

        url

        :param url: The url of this ProtocolReqVo.
        :type url: str
        """
        self._url = url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtocolReqVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
