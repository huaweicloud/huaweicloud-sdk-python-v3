# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HeaderMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_disposition': 'str',
        'content_language': 'str',
        'access_control_allow_origin': 'str',
        'access_control_allow_methods': 'str',
        'access_control_max_age': 'str',
        'access_control_expose_headers': 'str'
    }

    attribute_map = {
        'content_disposition': 'Content-Disposition',
        'content_language': 'Content-Language',
        'access_control_allow_origin': 'Access-Control-Allow-Origin',
        'access_control_allow_methods': 'Access-Control-Allow-Methods',
        'access_control_max_age': 'Access-Control-Max-Age',
        'access_control_expose_headers': 'Access-Control-Expose-Headers'
    }

    def __init__(self, content_disposition=None, content_language=None, access_control_allow_origin=None, access_control_allow_methods=None, access_control_max_age=None, access_control_expose_headers=None):
        r"""HeaderMap

        The model defined in huaweicloud sdk

        :param content_disposition: 指示回复的内容该以何种形式展示
        :type content_disposition: str
        :param content_language: 说明访问者希望采用的语言或语言组合
        :type content_language: str
        :param access_control_allow_origin: 指定了该响应的资源是否被允许与给定的origin共享
        :type access_control_allow_origin: str
        :param access_control_allow_methods: 明确了客户端所要访问的资源允许使用的方法或方法列表
        :type access_control_allow_methods: str
        :param access_control_max_age: Access-Control-Allow-Methods 和Access-Control-Allow-Headers 提供的信息可以被缓存多久
        :type access_control_max_age: str
        :param access_control_expose_headers: 列出了哪些首部可以作为响应的一部分暴露给外部
        :type access_control_expose_headers: str
        """
        
        

        self._content_disposition = None
        self._content_language = None
        self._access_control_allow_origin = None
        self._access_control_allow_methods = None
        self._access_control_max_age = None
        self._access_control_expose_headers = None
        self.discriminator = None

        if content_disposition is not None:
            self.content_disposition = content_disposition
        if content_language is not None:
            self.content_language = content_language
        if access_control_allow_origin is not None:
            self.access_control_allow_origin = access_control_allow_origin
        if access_control_allow_methods is not None:
            self.access_control_allow_methods = access_control_allow_methods
        if access_control_max_age is not None:
            self.access_control_max_age = access_control_max_age
        if access_control_expose_headers is not None:
            self.access_control_expose_headers = access_control_expose_headers

    @property
    def content_disposition(self):
        r"""Gets the content_disposition of this HeaderMap.

        指示回复的内容该以何种形式展示

        :return: The content_disposition of this HeaderMap.
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        r"""Sets the content_disposition of this HeaderMap.

        指示回复的内容该以何种形式展示

        :param content_disposition: The content_disposition of this HeaderMap.
        :type content_disposition: str
        """
        self._content_disposition = content_disposition

    @property
    def content_language(self):
        r"""Gets the content_language of this HeaderMap.

        说明访问者希望采用的语言或语言组合

        :return: The content_language of this HeaderMap.
        :rtype: str
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        r"""Sets the content_language of this HeaderMap.

        说明访问者希望采用的语言或语言组合

        :param content_language: The content_language of this HeaderMap.
        :type content_language: str
        """
        self._content_language = content_language

    @property
    def access_control_allow_origin(self):
        r"""Gets the access_control_allow_origin of this HeaderMap.

        指定了该响应的资源是否被允许与给定的origin共享

        :return: The access_control_allow_origin of this HeaderMap.
        :rtype: str
        """
        return self._access_control_allow_origin

    @access_control_allow_origin.setter
    def access_control_allow_origin(self, access_control_allow_origin):
        r"""Sets the access_control_allow_origin of this HeaderMap.

        指定了该响应的资源是否被允许与给定的origin共享

        :param access_control_allow_origin: The access_control_allow_origin of this HeaderMap.
        :type access_control_allow_origin: str
        """
        self._access_control_allow_origin = access_control_allow_origin

    @property
    def access_control_allow_methods(self):
        r"""Gets the access_control_allow_methods of this HeaderMap.

        明确了客户端所要访问的资源允许使用的方法或方法列表

        :return: The access_control_allow_methods of this HeaderMap.
        :rtype: str
        """
        return self._access_control_allow_methods

    @access_control_allow_methods.setter
    def access_control_allow_methods(self, access_control_allow_methods):
        r"""Sets the access_control_allow_methods of this HeaderMap.

        明确了客户端所要访问的资源允许使用的方法或方法列表

        :param access_control_allow_methods: The access_control_allow_methods of this HeaderMap.
        :type access_control_allow_methods: str
        """
        self._access_control_allow_methods = access_control_allow_methods

    @property
    def access_control_max_age(self):
        r"""Gets the access_control_max_age of this HeaderMap.

        Access-Control-Allow-Methods 和Access-Control-Allow-Headers 提供的信息可以被缓存多久

        :return: The access_control_max_age of this HeaderMap.
        :rtype: str
        """
        return self._access_control_max_age

    @access_control_max_age.setter
    def access_control_max_age(self, access_control_max_age):
        r"""Sets the access_control_max_age of this HeaderMap.

        Access-Control-Allow-Methods 和Access-Control-Allow-Headers 提供的信息可以被缓存多久

        :param access_control_max_age: The access_control_max_age of this HeaderMap.
        :type access_control_max_age: str
        """
        self._access_control_max_age = access_control_max_age

    @property
    def access_control_expose_headers(self):
        r"""Gets the access_control_expose_headers of this HeaderMap.

        列出了哪些首部可以作为响应的一部分暴露给外部

        :return: The access_control_expose_headers of this HeaderMap.
        :rtype: str
        """
        return self._access_control_expose_headers

    @access_control_expose_headers.setter
    def access_control_expose_headers(self, access_control_expose_headers):
        r"""Sets the access_control_expose_headers of this HeaderMap.

        列出了哪些首部可以作为响应的一部分暴露给外部

        :param access_control_expose_headers: The access_control_expose_headers of this HeaderMap.
        :type access_control_expose_headers: str
        """
        self._access_control_expose_headers = access_control_expose_headers

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
        if not isinstance(other, HeaderMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
