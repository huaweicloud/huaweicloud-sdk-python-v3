# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceSslDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'ip': 'str',
        'port': 'str',
        'domain_name': 'str',
        'ssl_expired_at': 'str',
        'ssl_validated': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'ip': 'ip',
        'port': 'port',
        'domain_name': 'domain_name',
        'ssl_expired_at': 'ssl_expired_at',
        'ssl_validated': 'ssl_validated'
    }

    def __init__(self, enabled=None, ip=None, port=None, domain_name=None, ssl_expired_at=None, ssl_validated=None):
        r"""ShowInstanceSslDetailResponse

        The model defined in huaweicloud sdk

        :param enabled: 开启或关闭SSL。true：开启/false：关闭
        :type enabled: bool
        :param ip: SSL连接IP。
        :type ip: str
        :param port: SSL连接端口。
        :type port: str
        :param domain_name: SSL连接域名。
        :type domain_name: str
        :param ssl_expired_at: SSL证书有效期（UTC时间）。
        :type ssl_expired_at: str
        :param ssl_validated: SSL证书是否有效。
        :type ssl_validated: bool
        """
        
        super(ShowInstanceSslDetailResponse, self).__init__()

        self._enabled = None
        self._ip = None
        self._port = None
        self._domain_name = None
        self._ssl_expired_at = None
        self._ssl_validated = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if domain_name is not None:
            self.domain_name = domain_name
        if ssl_expired_at is not None:
            self.ssl_expired_at = ssl_expired_at
        if ssl_validated is not None:
            self.ssl_validated = ssl_validated

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowInstanceSslDetailResponse.

        开启或关闭SSL。true：开启/false：关闭

        :return: The enabled of this ShowInstanceSslDetailResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowInstanceSslDetailResponse.

        开启或关闭SSL。true：开启/false：关闭

        :param enabled: The enabled of this ShowInstanceSslDetailResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def ip(self):
        r"""Gets the ip of this ShowInstanceSslDetailResponse.

        SSL连接IP。

        :return: The ip of this ShowInstanceSslDetailResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ShowInstanceSslDetailResponse.

        SSL连接IP。

        :param ip: The ip of this ShowInstanceSslDetailResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this ShowInstanceSslDetailResponse.

        SSL连接端口。

        :return: The port of this ShowInstanceSslDetailResponse.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowInstanceSslDetailResponse.

        SSL连接端口。

        :param port: The port of this ShowInstanceSslDetailResponse.
        :type port: str
        """
        self._port = port

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowInstanceSslDetailResponse.

        SSL连接域名。

        :return: The domain_name of this ShowInstanceSslDetailResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowInstanceSslDetailResponse.

        SSL连接域名。

        :param domain_name: The domain_name of this ShowInstanceSslDetailResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def ssl_expired_at(self):
        r"""Gets the ssl_expired_at of this ShowInstanceSslDetailResponse.

        SSL证书有效期（UTC时间）。

        :return: The ssl_expired_at of this ShowInstanceSslDetailResponse.
        :rtype: str
        """
        return self._ssl_expired_at

    @ssl_expired_at.setter
    def ssl_expired_at(self, ssl_expired_at):
        r"""Sets the ssl_expired_at of this ShowInstanceSslDetailResponse.

        SSL证书有效期（UTC时间）。

        :param ssl_expired_at: The ssl_expired_at of this ShowInstanceSslDetailResponse.
        :type ssl_expired_at: str
        """
        self._ssl_expired_at = ssl_expired_at

    @property
    def ssl_validated(self):
        r"""Gets the ssl_validated of this ShowInstanceSslDetailResponse.

        SSL证书是否有效。

        :return: The ssl_validated of this ShowInstanceSslDetailResponse.
        :rtype: bool
        """
        return self._ssl_validated

    @ssl_validated.setter
    def ssl_validated(self, ssl_validated):
        r"""Sets the ssl_validated of this ShowInstanceSslDetailResponse.

        SSL证书是否有效。

        :param ssl_validated: The ssl_validated of this ShowInstanceSslDetailResponse.
        :type ssl_validated: bool
        """
        self._ssl_validated = ssl_validated

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
        if not isinstance(other, ShowInstanceSslDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
