# coding: utf-8

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
        'status': 'str',
        'trusted_cert': 'str',
        'hosts': 'str',
        'trusted_certs': 'list[ClientCertTrustedCerts]',
        'sm_trusted_certs': 'list[ClientCertTrustedCerts]',
        'sm_cert_hosts': 'str'
    }

    attribute_map = {
        'status': 'status',
        'trusted_cert': 'trusted_cert',
        'hosts': 'hosts',
        'trusted_certs': 'trusted_certs',
        'sm_trusted_certs': 'sm_trusted_certs',
        'sm_cert_hosts': 'sm_cert_hosts'
    }

    def __init__(self, status=None, trusted_cert=None, hosts=None, trusted_certs=None, sm_trusted_certs=None, sm_cert_hosts=None):
        r"""ClientCert

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 客户端证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及
        :type status: str
        :param trusted_cert: **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type trusted_cert: str
        :param hosts: **参数解释：** 客户端CA证书指定的域名 **约束限制：** - 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求 - 最多可配置100个域名 - 多个域名用“,”或“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: str
        :param trusted_certs: **参数解释：** 多证书场景下客户端CA证书列表 **约束限制：** 不涉及
        :type trusted_certs: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        :param sm_trusted_certs: **参数解释：** 国密证书场景下客户端CA证书列表 **约束限制：** - 开启国密证书后配置 - 仅支持PEM格式
        :type sm_trusted_certs: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        :param sm_cert_hosts: **参数解释：** 国密证书指定访问的客户端域名 **约束限制：** - 开启国密证书后配置 - 最多可配置100个域名 - 多个域名用“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sm_cert_hosts: str
        """
        
        

        self._status = None
        self._trusted_cert = None
        self._hosts = None
        self._trusted_certs = None
        self._sm_trusted_certs = None
        self._sm_cert_hosts = None
        self.discriminator = None

        self.status = status
        if trusted_cert is not None:
            self.trusted_cert = trusted_cert
        if hosts is not None:
            self.hosts = hosts
        if trusted_certs is not None:
            self.trusted_certs = trusted_certs
        if sm_trusted_certs is not None:
            self.sm_trusted_certs = sm_trusted_certs
        if sm_cert_hosts is not None:
            self.sm_cert_hosts = sm_cert_hosts

    @property
    def status(self):
        r"""Gets the status of this ClientCert.

        **参数解释：** 客户端证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及

        :return: The status of this ClientCert.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClientCert.

        **参数解释：** 客户端证书配置开关 **约束限制：** 不涉及 **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及

        :param status: The status of this ClientCert.
        :type status: str
        """
        self._status = status

    @property
    def trusted_cert(self):
        r"""Gets the trusted_cert of this ClientCert.

        **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The trusted_cert of this ClientCert.
        :rtype: str
        """
        return self._trusted_cert

    @trusted_cert.setter
    def trusted_cert(self, trusted_cert):
        r"""Sets the trusted_cert of this ClientCert.

        **参数解释：** 客户端CA证书的内容 **约束限制：** 仅支持PEM格式 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param trusted_cert: The trusted_cert of this ClientCert.
        :type trusted_cert: str
        """
        self._trusted_cert = trusted_cert

    @property
    def hosts(self):
        r"""Gets the hosts of this ClientCert.

        **参数解释：** 客户端CA证书指定的域名 **约束限制：** - 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求 - 最多可配置100个域名 - 多个域名用“,”或“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this ClientCert.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ClientCert.

        **参数解释：** 客户端CA证书指定的域名 **约束限制：** - 如果不配置域名，则CDN会放行所有持有该CA证书的客户端请求 - 最多可配置100个域名 - 多个域名用“,”或“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this ClientCert.
        :type hosts: str
        """
        self._hosts = hosts

    @property
    def trusted_certs(self):
        r"""Gets the trusted_certs of this ClientCert.

        **参数解释：** 多证书场景下客户端CA证书列表 **约束限制：** 不涉及

        :return: The trusted_certs of this ClientCert.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        """
        return self._trusted_certs

    @trusted_certs.setter
    def trusted_certs(self, trusted_certs):
        r"""Sets the trusted_certs of this ClientCert.

        **参数解释：** 多证书场景下客户端CA证书列表 **约束限制：** 不涉及

        :param trusted_certs: The trusted_certs of this ClientCert.
        :type trusted_certs: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        """
        self._trusted_certs = trusted_certs

    @property
    def sm_trusted_certs(self):
        r"""Gets the sm_trusted_certs of this ClientCert.

        **参数解释：** 国密证书场景下客户端CA证书列表 **约束限制：** - 开启国密证书后配置 - 仅支持PEM格式

        :return: The sm_trusted_certs of this ClientCert.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        """
        return self._sm_trusted_certs

    @sm_trusted_certs.setter
    def sm_trusted_certs(self, sm_trusted_certs):
        r"""Sets the sm_trusted_certs of this ClientCert.

        **参数解释：** 国密证书场景下客户端CA证书列表 **约束限制：** - 开启国密证书后配置 - 仅支持PEM格式

        :param sm_trusted_certs: The sm_trusted_certs of this ClientCert.
        :type sm_trusted_certs: list[:class:`huaweicloudsdkcdn.v2.ClientCertTrustedCerts`]
        """
        self._sm_trusted_certs = sm_trusted_certs

    @property
    def sm_cert_hosts(self):
        r"""Gets the sm_cert_hosts of this ClientCert.

        **参数解释：** 国密证书指定访问的客户端域名 **约束限制：** - 开启国密证书后配置 - 最多可配置100个域名 - 多个域名用“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sm_cert_hosts of this ClientCert.
        :rtype: str
        """
        return self._sm_cert_hosts

    @sm_cert_hosts.setter
    def sm_cert_hosts(self, sm_cert_hosts):
        r"""Sets the sm_cert_hosts of this ClientCert.

        **参数解释：** 国密证书指定访问的客户端域名 **约束限制：** - 开启国密证书后配置 - 最多可配置100个域名 - 多个域名用“|”分隔  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sm_cert_hosts: The sm_cert_hosts of this ClientCert.
        :type sm_cert_hosts: str
        """
        self._sm_cert_hosts = sm_cert_hosts

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
        if not isinstance(other, ClientCert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
