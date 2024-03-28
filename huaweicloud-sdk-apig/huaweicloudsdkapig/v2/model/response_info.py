# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'body': 'str',
        'headers': 'list[ResponseInfoHeader]'
    }

    attribute_map = {
        'status': 'status',
        'body': 'body',
        'headers': 'headers'
    }

    def __init__(self, status=None, body=None, headers=None):
        """ResponseInfo

        The model defined in huaweicloud sdk

        :param status: 响应的HTTP状态码。范围为200-599，但不允许为444。
        :type status: int
        :param body: 响应的Body模板
        :type body: str
        :param headers: 自定义的响应头
        :type headers: list[:class:`huaweicloudsdkapig.v2.ResponseInfoHeader`]
        """
        
        

        self._status = None
        self._body = None
        self._headers = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if body is not None:
            self.body = body
        if headers is not None:
            self.headers = headers

    @property
    def status(self):
        """Gets the status of this ResponseInfo.

        响应的HTTP状态码。范围为200-599，但不允许为444。

        :return: The status of this ResponseInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseInfo.

        响应的HTTP状态码。范围为200-599，但不允许为444。

        :param status: The status of this ResponseInfo.
        :type status: int
        """
        self._status = status

    @property
    def body(self):
        """Gets the body of this ResponseInfo.

        响应的Body模板

        :return: The body of this ResponseInfo.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResponseInfo.

        响应的Body模板

        :param body: The body of this ResponseInfo.
        :type body: str
        """
        self._body = body

    @property
    def headers(self):
        """Gets the headers of this ResponseInfo.

        自定义的响应头

        :return: The headers of this ResponseInfo.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ResponseInfoHeader`]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ResponseInfo.

        自定义的响应头

        :param headers: The headers of this ResponseInfo.
        :type headers: list[:class:`huaweicloudsdkapig.v2.ResponseInfoHeader`]
        """
        self._headers = headers

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
        if not isinstance(other, ResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
