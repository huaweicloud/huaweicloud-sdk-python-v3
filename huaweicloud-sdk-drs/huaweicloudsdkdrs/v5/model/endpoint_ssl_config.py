# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointSslConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssl_link': 'bool',
        'ssl_cert_name': 'str',
        'ssl_cert_key': 'str',
        'ssl_cert_check_sum': 'str',
        'ssl_cert_password': 'str'
    }

    attribute_map = {
        'ssl_link': 'ssl_link',
        'ssl_cert_name': 'ssl_cert_name',
        'ssl_cert_key': 'ssl_cert_key',
        'ssl_cert_check_sum': 'ssl_cert_check_sum',
        'ssl_cert_password': 'ssl_cert_password'
    }

    def __init__(self, ssl_link=None, ssl_cert_name=None, ssl_cert_key=None, ssl_cert_check_sum=None, ssl_cert_password=None):
        r"""EndpointSslConfig

        The model defined in huaweicloud sdk

        :param ssl_link: 是否SSL安全连接。如果数据库启用了SSL安全连接，参数值为true。
        :type ssl_link: bool
        :param ssl_cert_name: SSL证书名字。
        :type ssl_cert_name: str
        :param ssl_cert_key: SSL证书内容，用base64加密。
        :type ssl_cert_key: str
        :param ssl_cert_check_sum: SSL证书内容checksum值，后端校验，源库安全连接必选。
        :type ssl_cert_check_sum: str
        :param ssl_cert_password: SSL证书密码，证书文件后缀为.p12时必填。
        :type ssl_cert_password: str
        """
        
        

        self._ssl_link = None
        self._ssl_cert_name = None
        self._ssl_cert_key = None
        self._ssl_cert_check_sum = None
        self._ssl_cert_password = None
        self.discriminator = None

        if ssl_link is not None:
            self.ssl_link = ssl_link
        if ssl_cert_name is not None:
            self.ssl_cert_name = ssl_cert_name
        if ssl_cert_key is not None:
            self.ssl_cert_key = ssl_cert_key
        if ssl_cert_check_sum is not None:
            self.ssl_cert_check_sum = ssl_cert_check_sum
        if ssl_cert_password is not None:
            self.ssl_cert_password = ssl_cert_password

    @property
    def ssl_link(self):
        r"""Gets the ssl_link of this EndpointSslConfig.

        是否SSL安全连接。如果数据库启用了SSL安全连接，参数值为true。

        :return: The ssl_link of this EndpointSslConfig.
        :rtype: bool
        """
        return self._ssl_link

    @ssl_link.setter
    def ssl_link(self, ssl_link):
        r"""Sets the ssl_link of this EndpointSslConfig.

        是否SSL安全连接。如果数据库启用了SSL安全连接，参数值为true。

        :param ssl_link: The ssl_link of this EndpointSslConfig.
        :type ssl_link: bool
        """
        self._ssl_link = ssl_link

    @property
    def ssl_cert_name(self):
        r"""Gets the ssl_cert_name of this EndpointSslConfig.

        SSL证书名字。

        :return: The ssl_cert_name of this EndpointSslConfig.
        :rtype: str
        """
        return self._ssl_cert_name

    @ssl_cert_name.setter
    def ssl_cert_name(self, ssl_cert_name):
        r"""Sets the ssl_cert_name of this EndpointSslConfig.

        SSL证书名字。

        :param ssl_cert_name: The ssl_cert_name of this EndpointSslConfig.
        :type ssl_cert_name: str
        """
        self._ssl_cert_name = ssl_cert_name

    @property
    def ssl_cert_key(self):
        r"""Gets the ssl_cert_key of this EndpointSslConfig.

        SSL证书内容，用base64加密。

        :return: The ssl_cert_key of this EndpointSslConfig.
        :rtype: str
        """
        return self._ssl_cert_key

    @ssl_cert_key.setter
    def ssl_cert_key(self, ssl_cert_key):
        r"""Sets the ssl_cert_key of this EndpointSslConfig.

        SSL证书内容，用base64加密。

        :param ssl_cert_key: The ssl_cert_key of this EndpointSslConfig.
        :type ssl_cert_key: str
        """
        self._ssl_cert_key = ssl_cert_key

    @property
    def ssl_cert_check_sum(self):
        r"""Gets the ssl_cert_check_sum of this EndpointSslConfig.

        SSL证书内容checksum值，后端校验，源库安全连接必选。

        :return: The ssl_cert_check_sum of this EndpointSslConfig.
        :rtype: str
        """
        return self._ssl_cert_check_sum

    @ssl_cert_check_sum.setter
    def ssl_cert_check_sum(self, ssl_cert_check_sum):
        r"""Sets the ssl_cert_check_sum of this EndpointSslConfig.

        SSL证书内容checksum值，后端校验，源库安全连接必选。

        :param ssl_cert_check_sum: The ssl_cert_check_sum of this EndpointSslConfig.
        :type ssl_cert_check_sum: str
        """
        self._ssl_cert_check_sum = ssl_cert_check_sum

    @property
    def ssl_cert_password(self):
        r"""Gets the ssl_cert_password of this EndpointSslConfig.

        SSL证书密码，证书文件后缀为.p12时必填。

        :return: The ssl_cert_password of this EndpointSslConfig.
        :rtype: str
        """
        return self._ssl_cert_password

    @ssl_cert_password.setter
    def ssl_cert_password(self, ssl_cert_password):
        r"""Sets the ssl_cert_password of this EndpointSslConfig.

        SSL证书密码，证书文件后缀为.p12时必填。

        :param ssl_cert_password: The ssl_cert_password of this EndpointSslConfig.
        :type ssl_cert_password: str
        """
        self._ssl_cert_password = ssl_cert_password

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
        if not isinstance(other, EndpointSslConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
