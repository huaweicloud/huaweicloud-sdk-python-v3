# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientCert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'validation': 'int',
        'trusted_cert': 'str',
        'hosts': 'str'
    }

    attribute_map = {
        'validation': 'validation',
        'trusted_cert': 'trusted_cert',
        'hosts': 'hosts'
    }

    def __init__(self, validation=None, trusted_cert=None, hosts=None):
        """ClientCert

        The model defined in huaweicloud sdk

        :param validation: 客户端证书配置开关，1：打开；0：关闭。
        :type validation: int
        :param trusted_cert: 客户端CA证书的内容，仅支持PEM格式。
        :type trusted_cert: str
        :param hosts: 客户端CA证书指定的域名。   &gt; 1. 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求。   &gt; 2. 最多可配置100个域名，多个域名用“,”或“|”分隔。
        :type hosts: str
        """
        
        

        self._validation = None
        self._trusted_cert = None
        self._hosts = None
        self.discriminator = None

        self.validation = validation
        self.trusted_cert = trusted_cert
        if hosts is not None:
            self.hosts = hosts

    @property
    def validation(self):
        """Gets the validation of this ClientCert.

        客户端证书配置开关，1：打开；0：关闭。

        :return: The validation of this ClientCert.
        :rtype: int
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this ClientCert.

        客户端证书配置开关，1：打开；0：关闭。

        :param validation: The validation of this ClientCert.
        :type validation: int
        """
        self._validation = validation

    @property
    def trusted_cert(self):
        """Gets the trusted_cert of this ClientCert.

        客户端CA证书的内容，仅支持PEM格式。

        :return: The trusted_cert of this ClientCert.
        :rtype: str
        """
        return self._trusted_cert

    @trusted_cert.setter
    def trusted_cert(self, trusted_cert):
        """Sets the trusted_cert of this ClientCert.

        客户端CA证书的内容，仅支持PEM格式。

        :param trusted_cert: The trusted_cert of this ClientCert.
        :type trusted_cert: str
        """
        self._trusted_cert = trusted_cert

    @property
    def hosts(self):
        """Gets the hosts of this ClientCert.

        客户端CA证书指定的域名。   > 1. 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求。   > 2. 最多可配置100个域名，多个域名用“,”或“|”分隔。

        :return: The hosts of this ClientCert.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ClientCert.

        客户端CA证书指定的域名。   > 1. 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求。   > 2. 最多可配置100个域名，多个域名用“,”或“|”分隔。

        :param hosts: The hosts of this ClientCert.
        :type hosts: str
        """
        self._hosts = hosts

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
        if not isinstance(other, ClientCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
