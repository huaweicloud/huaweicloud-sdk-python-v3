# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpPutBody:

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
        'private_key': 'str',
        'certificate_source': 'int',
        'http2_status': 'str',
        'tls_version': 'str'
    }

    attribute_map = {
        'https_status': 'https_status',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'private_key': 'private_key',
        'certificate_source': 'certificate_source',
        'http2_status': 'http2_status',
        'tls_version': 'tls_version'
    }

    def __init__(self, https_status=None, certificate_name=None, certificate_value=None, private_key=None, certificate_source=None, http2_status=None, tls_version=None):
        r"""HttpPutBody

        The model defined in huaweicloud sdk

        :param https_status: HTTPS证书是否启用，on：开启，off：关闭。
        :type https_status: str
        :param certificate_name: 证书名字，长度限制为3-64字符。  &gt; 当证书开启时必传。
        :type certificate_name: str
        :param certificate_value: HTTPS协议使用的证书内容，当证书开启时必传。  &gt; PEM编码格式。
        :type certificate_value: str
        :param private_key: HTTPS协议使用的私钥，当证书开启时必传。  &gt; PEM编码格式。
        :type private_key: str
        :param certificate_source: 证书来源,0：自有证书。  &gt; 证书开启时必传
        :type certificate_source: int
        :param http2_status: 是否使用HTTP2.0，on：是，off：否。  &gt; 默认关闭，https_status&#x3D;off时，该值不生效。
        :type http2_status: str
        :param tls_version: 传输层安全性协议， 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议，CDN默认开启TLS1.1/1.2/1.3，不可全部关闭。  &gt; 1.需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1。  &gt; 2.多版本开启时，使用逗号拼接传输，例：TLSv1.1,TLSv1.2。
        :type tls_version: str
        """
        
        

        self._https_status = None
        self._certificate_name = None
        self._certificate_value = None
        self._private_key = None
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
        if private_key is not None:
            self.private_key = private_key
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if http2_status is not None:
            self.http2_status = http2_status
        if tls_version is not None:
            self.tls_version = tls_version

    @property
    def https_status(self):
        r"""Gets the https_status of this HttpPutBody.

        HTTPS证书是否启用，on：开启，off：关闭。

        :return: The https_status of this HttpPutBody.
        :rtype: str
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        r"""Sets the https_status of this HttpPutBody.

        HTTPS证书是否启用，on：开启，off：关闭。

        :param https_status: The https_status of this HttpPutBody.
        :type https_status: str
        """
        self._https_status = https_status

    @property
    def certificate_name(self):
        r"""Gets the certificate_name of this HttpPutBody.

        证书名字，长度限制为3-64字符。  > 当证书开启时必传。

        :return: The certificate_name of this HttpPutBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        r"""Sets the certificate_name of this HttpPutBody.

        证书名字，长度限制为3-64字符。  > 当证书开启时必传。

        :param certificate_name: The certificate_name of this HttpPutBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        r"""Gets the certificate_value of this HttpPutBody.

        HTTPS协议使用的证书内容，当证书开启时必传。  > PEM编码格式。

        :return: The certificate_value of this HttpPutBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        r"""Sets the certificate_value of this HttpPutBody.

        HTTPS协议使用的证书内容，当证书开启时必传。  > PEM编码格式。

        :param certificate_value: The certificate_value of this HttpPutBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def private_key(self):
        r"""Gets the private_key of this HttpPutBody.

        HTTPS协议使用的私钥，当证书开启时必传。  > PEM编码格式。

        :return: The private_key of this HttpPutBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this HttpPutBody.

        HTTPS协议使用的私钥，当证书开启时必传。  > PEM编码格式。

        :param private_key: The private_key of this HttpPutBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_source(self):
        r"""Gets the certificate_source of this HttpPutBody.

        证书来源,0：自有证书。  > 证书开启时必传

        :return: The certificate_source of this HttpPutBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        r"""Sets the certificate_source of this HttpPutBody.

        证书来源,0：自有证书。  > 证书开启时必传

        :param certificate_source: The certificate_source of this HttpPutBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def http2_status(self):
        r"""Gets the http2_status of this HttpPutBody.

        是否使用HTTP2.0，on：是，off：否。  > 默认关闭，https_status=off时，该值不生效。

        :return: The http2_status of this HttpPutBody.
        :rtype: str
        """
        return self._http2_status

    @http2_status.setter
    def http2_status(self, http2_status):
        r"""Sets the http2_status of this HttpPutBody.

        是否使用HTTP2.0，on：是，off：否。  > 默认关闭，https_status=off时，该值不生效。

        :param http2_status: The http2_status of this HttpPutBody.
        :type http2_status: str
        """
        self._http2_status = http2_status

    @property
    def tls_version(self):
        r"""Gets the tls_version of this HttpPutBody.

        传输层安全性协议， 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议，CDN默认开启TLS1.1/1.2/1.3，不可全部关闭。  > 1.需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1。  > 2.多版本开启时，使用逗号拼接传输，例：TLSv1.1,TLSv1.2。

        :return: The tls_version of this HttpPutBody.
        :rtype: str
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version):
        r"""Sets the tls_version of this HttpPutBody.

        传输层安全性协议， 目前支持TLSv1.0/1.1/1.2/1.3四个版本的协议，CDN默认开启TLS1.1/1.2/1.3，不可全部关闭。  > 1.需开启连续或单个版本号，例：不可仅开启TLS1.0/1.2而关闭TLS1.1。  > 2.多版本开启时，使用逗号拼接传输，例：TLSv1.1,TLSv1.2。

        :param tls_version: The tls_version of this HttpPutBody.
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
        if not isinstance(other, HttpPutBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
