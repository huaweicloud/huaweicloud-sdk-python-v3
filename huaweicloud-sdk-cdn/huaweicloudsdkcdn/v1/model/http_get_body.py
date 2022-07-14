# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpGetBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'https_status': 'str',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'certificate_source': 'int',
        'http2_status': 'str',
        'tls_version': 'str'
    }

    attribute_map = {
        'https_status': 'https_status',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'certificate_source': 'certificate_source',
        'http2_status': 'http2_status',
        'tls_version': 'tls_version'
    }

    def __init__(self, https_status=None, certificate_name=None, certificate_value=None, certificate_source=None, http2_status=None, tls_version=None):
        """HttpGetBody

        The model defined in huaweicloud sdk

        :param https_status: HTTPS证书是否启用。（on：开启，off：关闭）
        :type https_status: str
        :param certificate_name: 证书名字。（长度限制为3-32字符）。当证书开启时必返回该字段。
        :type certificate_name: str
        :param certificate_value: HTTPS协议使用的证书内容，当证书开启时必返回该字段。取值范围：PEM编码格式。
        :type certificate_value: str
        :param certificate_source: 证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必返回该字段。
        :type certificate_source: int
        :param http2_status: 是否使用HTTP2.0。（on：是，off：否）
        :type http2_status: str
        :param tls_version: 传输层安全性协议，目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议。当证书开启时返回该字段，默认全部开启，不可全部关闭。
        :type tls_version: str
        """
        
        

        self._https_status = None
        self._certificate_name = None
        self._certificate_value = None
        self._certificate_source = None
        self._http2_status = None
        self._tls_version = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_value is not None:
            self.certificate_value = certificate_value
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if http2_status is not None:
            self.http2_status = http2_status
        if tls_version is not None:
            self.tls_version = tls_version

    @property
    def https_status(self):
        """Gets the https_status of this HttpGetBody.

        HTTPS证书是否启用。（on：开启，off：关闭）

        :return: The https_status of this HttpGetBody.
        :rtype: str
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpGetBody.

        HTTPS证书是否启用。（on：开启，off：关闭）

        :param https_status: The https_status of this HttpGetBody.
        :type https_status: str
        """
        self._https_status = https_status

    @property
    def certificate_name(self):
        """Gets the certificate_name of this HttpGetBody.

        证书名字。（长度限制为3-32字符）。当证书开启时必返回该字段。

        :return: The certificate_name of this HttpGetBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this HttpGetBody.

        证书名字。（长度限制为3-32字符）。当证书开启时必返回该字段。

        :param certificate_name: The certificate_name of this HttpGetBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        """Gets the certificate_value of this HttpGetBody.

        HTTPS协议使用的证书内容，当证书开启时必返回该字段。取值范围：PEM编码格式。

        :return: The certificate_value of this HttpGetBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        """Sets the certificate_value of this HttpGetBody.

        HTTPS协议使用的证书内容，当证书开启时必返回该字段。取值范围：PEM编码格式。

        :param certificate_value: The certificate_value of this HttpGetBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def certificate_source(self):
        """Gets the certificate_source of this HttpGetBody.

        证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必返回该字段。

        :return: The certificate_source of this HttpGetBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        """Sets the certificate_source of this HttpGetBody.

        证书来源。1：代表华为云托管证书；0：表示自有证书。 默认值0。当证书开启时必返回该字段。

        :param certificate_source: The certificate_source of this HttpGetBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def http2_status(self):
        """Gets the http2_status of this HttpGetBody.

        是否使用HTTP2.0。（on：是，off：否）

        :return: The http2_status of this HttpGetBody.
        :rtype: str
        """
        return self._http2_status

    @http2_status.setter
    def http2_status(self, http2_status):
        """Sets the http2_status of this HttpGetBody.

        是否使用HTTP2.0。（on：是，off：否）

        :param http2_status: The http2_status of this HttpGetBody.
        :type http2_status: str
        """
        self._http2_status = http2_status

    @property
    def tls_version(self):
        """Gets the tls_version of this HttpGetBody.

        传输层安全性协议，目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议。当证书开启时返回该字段，默认全部开启，不可全部关闭。

        :return: The tls_version of this HttpGetBody.
        :rtype: str
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version):
        """Sets the tls_version of this HttpGetBody.

        传输层安全性协议，目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议。当证书开启时返回该字段，默认全部开启，不可全部关闭。

        :param tls_version: The tls_version of this HttpGetBody.
        :type tls_version: str
        """
        self._tls_version = tls_version

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
        if not isinstance(other, HttpGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
