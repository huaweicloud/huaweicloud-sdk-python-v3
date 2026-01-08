# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListenerInsertHeaders:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_forwarded_elb_ip': 'bool',
        'x_forwarded_port': 'bool',
        'x_forwarded_for_port': 'bool',
        'x_forwarded_host': 'bool',
        'x_forwarded_proto': 'bool',
        'x_real_ip': 'bool',
        'x_forwarded_elb_id': 'bool',
        'x_forwarded_tls_certificate_id': 'bool',
        'x_forwarded_tls_protocol': 'bool',
        'x_forwarded_tls_cipher': 'bool',
        'x_forwarded_tls_protocol_alias': 'str',
        'x_forwarded_tls_cipher_alias': 'str',
        'x_forwarded_for_processing_mode': 'str',
        'x_forwarded_clientcert_subjectdn_enable': 'bool',
        'x_forwarded_clientcert_subjectdn_alias': 'str',
        'x_forwarded_clientcert_issuerdn_enable': 'bool',
        'x_forwarded_clientcert_issuerdn_alias': 'str',
        'x_forwarded_clientcert_fingerprint_enable': 'bool',
        'x_forwarded_clientcert_fingerprint_alias': 'str',
        'x_forwarded_clientcert_clientverify_enable': 'bool',
        'x_forwarded_clientcert_clientverify_alias': 'str',
        'x_forwarded_clientcert_serialnumber_enable': 'bool',
        'x_forwarded_clientcert_serialnumber_alias': 'str',
        'x_forwarded_clientcert_enable': 'bool',
        'x_forwarded_clientcert_alias': 'str',
        'x_forwarded_clientcert_ciphers_enable': 'bool',
        'x_forwarded_clientcert_ciphers_alias': 'str',
        'x_forwarded_clientcert_end_enable': 'bool',
        'x_forwarded_clientcert_end_alias': 'str',
        'x_forwarded_tls_alpn_protocol_enable': 'bool',
        'x_forwarded_tls_alpn_protocol_alias': 'str',
        'x_forwarded_tls_sni_enable': 'bool',
        'x_forwarded_tls_sni_alias': 'str',
        'x_forwarded_tls_ja3_enable': 'bool',
        'x_forwarded_tls_ja3_alias': 'str',
        'x_forwarded_tls_ja4_enable': 'bool',
        'x_forwarded_tls_ja4_alias': 'str'
    }

    attribute_map = {
        'x_forwarded_elb_ip': 'X-Forwarded-ELB-IP',
        'x_forwarded_port': 'X-Forwarded-Port',
        'x_forwarded_for_port': 'X-Forwarded-For-Port',
        'x_forwarded_host': 'X-Forwarded-Host',
        'x_forwarded_proto': 'X-Forwarded-Proto',
        'x_real_ip': 'X-Real-IP',
        'x_forwarded_elb_id': 'X-Forwarded-ELB-ID',
        'x_forwarded_tls_certificate_id': 'X-Forwarded-TLS-Certificate-ID',
        'x_forwarded_tls_protocol': 'X-Forwarded-TLS-Protocol',
        'x_forwarded_tls_cipher': 'X-Forwarded-TLS-Cipher',
        'x_forwarded_tls_protocol_alias': 'X-Forwarded-TLS-Protocol-alias',
        'x_forwarded_tls_cipher_alias': 'X-Forwarded-TLS-Cipher-alias',
        'x_forwarded_for_processing_mode': 'X-Forwarded-For-Processing-Mode',
        'x_forwarded_clientcert_subjectdn_enable': 'X-Forwarded-Clientcert-subjectdn-enable',
        'x_forwarded_clientcert_subjectdn_alias': 'X-Forwarded-Clientcert-subjectdn-alias',
        'x_forwarded_clientcert_issuerdn_enable': 'X-Forwarded-Clientcert-issuerdn-enable',
        'x_forwarded_clientcert_issuerdn_alias': 'X-Forwarded-Clientcert-issuerdn-alias',
        'x_forwarded_clientcert_fingerprint_enable': 'X-Forwarded-Clientcert-fingerprint-enable',
        'x_forwarded_clientcert_fingerprint_alias': 'X-Forwarded-Clientcert-fingerprint-alias',
        'x_forwarded_clientcert_clientverify_enable': 'X-Forwarded-Clientcert-clientverify-enable',
        'x_forwarded_clientcert_clientverify_alias': 'X-Forwarded-Clientcert-clientverify-alias',
        'x_forwarded_clientcert_serialnumber_enable': 'X-Forwarded-Clientcert-serialnumber-enable',
        'x_forwarded_clientcert_serialnumber_alias': 'X-Forwarded-Clientcert-serialnumber-alias',
        'x_forwarded_clientcert_enable': 'X-Forwarded-Clientcert-enable',
        'x_forwarded_clientcert_alias': 'X-Forwarded-Clientcert-alias',
        'x_forwarded_clientcert_ciphers_enable': 'X-Forwarded-Clientcert-ciphers-enable',
        'x_forwarded_clientcert_ciphers_alias': 'X-Forwarded-Clientcert-ciphers-alias',
        'x_forwarded_clientcert_end_enable': 'X-Forwarded-Clientcert-end-enable',
        'x_forwarded_clientcert_end_alias': 'X-Forwarded-Clientcert-end-alias',
        'x_forwarded_tls_alpn_protocol_enable': 'X-Forwarded-Tls-Alpn-Protocol-enable',
        'x_forwarded_tls_alpn_protocol_alias': 'X-Forwarded-Tls-Alpn-Protocol-alias',
        'x_forwarded_tls_sni_enable': 'X-Forwarded-Tls-Sni-enable',
        'x_forwarded_tls_sni_alias': 'X-Forwarded-Tls-Sni-alias',
        'x_forwarded_tls_ja3_enable': 'X-Forwarded-Tls-Ja3-enable',
        'x_forwarded_tls_ja3_alias': 'X-Forwarded-Tls-Ja3-alias',
        'x_forwarded_tls_ja4_enable': 'X-Forwarded-Tls-Ja4-enable',
        'x_forwarded_tls_ja4_alias': 'X-Forwarded-Tls-Ja4-alias'
    }

    def __init__(self, x_forwarded_elb_ip=None, x_forwarded_port=None, x_forwarded_for_port=None, x_forwarded_host=None, x_forwarded_proto=None, x_real_ip=None, x_forwarded_elb_id=None, x_forwarded_tls_certificate_id=None, x_forwarded_tls_protocol=None, x_forwarded_tls_cipher=None, x_forwarded_tls_protocol_alias=None, x_forwarded_tls_cipher_alias=None, x_forwarded_for_processing_mode=None, x_forwarded_clientcert_subjectdn_enable=None, x_forwarded_clientcert_subjectdn_alias=None, x_forwarded_clientcert_issuerdn_enable=None, x_forwarded_clientcert_issuerdn_alias=None, x_forwarded_clientcert_fingerprint_enable=None, x_forwarded_clientcert_fingerprint_alias=None, x_forwarded_clientcert_clientverify_enable=None, x_forwarded_clientcert_clientverify_alias=None, x_forwarded_clientcert_serialnumber_enable=None, x_forwarded_clientcert_serialnumber_alias=None, x_forwarded_clientcert_enable=None, x_forwarded_clientcert_alias=None, x_forwarded_clientcert_ciphers_enable=None, x_forwarded_clientcert_ciphers_alias=None, x_forwarded_clientcert_end_enable=None, x_forwarded_clientcert_end_alias=None, x_forwarded_tls_alpn_protocol_enable=None, x_forwarded_tls_alpn_protocol_alias=None, x_forwarded_tls_sni_enable=None, x_forwarded_tls_sni_alias=None, x_forwarded_tls_ja3_enable=None, x_forwarded_tls_ja3_alias=None, x_forwarded_tls_ja4_enable=None, x_forwarded_tls_ja4_alias=None):
        r"""ListenerInsertHeaders

        The model defined in huaweicloud sdk

        :param x_forwarded_elb_ip: **参数解释**：X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端服务器。
        :type x_forwarded_elb_ip: bool
        :param x_forwarded_port: **参数解释**：X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端服务器。
        :type x_forwarded_port: bool
        :param x_forwarded_for_port: **参数解释**：X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端服务器。
        :type x_forwarded_for_port: bool
        :param x_forwarded_host: **参数解释**：X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端服务器。
        :type x_forwarded_host: bool
        :param x_forwarded_proto: **参数解释**：X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端服务器。
        :type x_forwarded_proto: bool
        :param x_real_ip: **参数解释**：X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端服务器。
        :type x_real_ip: bool
        :param x_forwarded_elb_id: **参数解释**：X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端服务器。
        :type x_forwarded_elb_id: bool
        :param x_forwarded_tls_certificate_id: **参数解释**：X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端服务器。
        :type x_forwarded_tls_certificate_id: bool
        :param x_forwarded_tls_protocol: **参数解释**：X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端服务器。
        :type x_forwarded_tls_protocol: bool
        :param x_forwarded_tls_cipher: **参数解释**：X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端服务器。
        :type x_forwarded_tls_cipher: bool
        :param x_forwarded_tls_protocol_alias: **参数解释**：自定义X-Forwarded-TLS-Protocol头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Protocol 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_protocol_alias: str
        :param x_forwarded_tls_cipher_alias: **参数解释**：自定义X-Forwarded-TLS-Cipher头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Cipher 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_cipher_alias: str
        :param x_forwarded_for_processing_mode: **参数解释**：处理X-Forwarded-For头字段的模式： 配置 append，将请求发送至后端服务之前把最后一跳 IP 加入X-Forwarded-For头字段； 配置 remove，请求发送至后端服务之前删除X-Forwarded-For标头，无论请求是否携带X-Forwarded-For头字段； 配置preserve，保留请求中已有的X-Forwarded-For标头；  **约束限制**：仅HTTP、HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段；  **取值范围**：append、remove、preserve  **默认取值**：append
        :type x_forwarded_for_processing_mode: str
        :param x_forwarded_clientcert_subjectdn_enable: **参数解释**：是否通过X-Forwarded-Clientcert-subjectdn头字段获取访问负载均衡实例客户端证书的所有者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_subjectdn_enable: bool
        :param x_forwarded_clientcert_subjectdn_alias: **参数解释**：自定义X-Forwarded-Clientcert-subjectdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-subjectdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_subjectdn_alias: str
        :param x_forwarded_clientcert_issuerdn_enable: **参数解释**：是否通过X-Forwarded-Clientcert-issuerdn头字段获取访问负载均衡实例客户端证书的发行者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_issuerdn_enable: bool
        :param x_forwarded_clientcert_issuerdn_alias: **参数解释**：自定义X-Forwarded-Clientcert-issuerdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-issuerdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_issuerdn_alias: str
        :param x_forwarded_clientcert_fingerprint_enable: **参数解释**：是否通过X-Forwarded-Clientcert-fingerprint头字段获取访问负载均衡实例客户端证书的指纹取值。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_fingerprint_enable: bool
        :param x_forwarded_clientcert_fingerprint_alias: **参数解释**：自定义X-Forwarded-Clientcert-fingerprint头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-fingerprint-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_fingerprint_alias: str
        :param x_forwarded_clientcert_clientverify_enable: **参数解释**：是否通过X-Forwarded-Clientcert-clientverify头字段获取对访问负载均衡实例客户端证书的校验结果。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_clientverify_enable: bool
        :param x_forwarded_clientcert_clientverify_alias: **参数解释**：自定义X-Forwarded-Clientcert-clientverify头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-clientverify-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_clientverify_alias: str
        :param x_forwarded_clientcert_serialnumber_enable: **参数解释**：是否通过X-Forwarded-Clientcert-serialnumber 头字段获取客户端证书的序列号信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_serialnumber_enable: bool
        :param x_forwarded_clientcert_serialnumber_alias: **参数解释**：自定义X-Forwarded-Clientcert-serialnumber头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-serialnumber-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_serialnumber_alias: str
        :param x_forwarded_clientcert_enable: **参数解释**：是否通过X-Forwarded-Clientcert 头字段获取客户端证书的内容。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_enable: bool
        :param x_forwarded_clientcert_alias: **参数解释**：自定义X-Forwarded-Clientcert头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_alias: str
        :param x_forwarded_clientcert_ciphers_enable: **参数解释**：是否通过X-Forwarded-Clientcert-ciphers 头字段获取客户端支持的TLS加密套件。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_ciphers_enable: bool
        :param x_forwarded_clientcert_ciphers_alias: **参数解释**：自定义X-Forwarded-Clientcert-ciphers头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-ciphers-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_ciphers_alias: str
        :param x_forwarded_clientcert_end_enable: **参数解释**：是否通过X-Forwarded-Clientcert-end 头字段获取客户端证书的结束日期。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_clientcert_end_enable: bool
        :param x_forwarded_clientcert_end_alias: **参数解释**：自定义X-Forwarded-Clientcert-end头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-end-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_clientcert_end_alias: str
        :param x_forwarded_tls_alpn_protocol_enable: **参数解释**：是否通过X-Forwarded-Tls-Alpn-Protocol 头字段获取客户端和服务器之间ALPN（Application-Layer Protocol Negotiation）协商的应用层协议。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_tls_alpn_protocol_enable: bool
        :param x_forwarded_tls_alpn_protocol_alias: **参数解释**：自定义X-Forwarded-Tls-Alpn-Protocol头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Alpn-Protocol-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_alpn_protocol_alias: str
        :param x_forwarded_tls_sni_enable: **参数解释**：是否通过X-Forwarded-Tls-Sni 头字段获取客户端访问的sni证书的域名。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_tls_sni_enable: bool
        :param x_forwarded_tls_sni_alias: **参数解释**：自定义X-Forwarded-Tls-Sni头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Sni-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_sni_alias: str
        :param x_forwarded_tls_ja3_enable: **参数解释**：是否通过X-Forwarded-Tls-Ja3头字段获取访问负载均衡实例客户端的ja3指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_tls_ja3_enable: bool
        :param x_forwarded_tls_ja3_alias: **参数解释**：自定义X-Forwarded-Tls-Ja3头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja3-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_ja3_alias: str
        :param x_forwarded_tls_ja4_enable: **参数解释**：是否通过X-Forwarded-Tls-Ja4头字段获取访问负载均衡实例客户端的ja4指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false
        :type x_forwarded_tls_ja4_enable: bool
        :param x_forwarded_tls_ja4_alias: **参数解释**：自定义X-Forwarded-Tls-Ja4头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja4-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无
        :type x_forwarded_tls_ja4_alias: str
        """
        
        

        self._x_forwarded_elb_ip = None
        self._x_forwarded_port = None
        self._x_forwarded_for_port = None
        self._x_forwarded_host = None
        self._x_forwarded_proto = None
        self._x_real_ip = None
        self._x_forwarded_elb_id = None
        self._x_forwarded_tls_certificate_id = None
        self._x_forwarded_tls_protocol = None
        self._x_forwarded_tls_cipher = None
        self._x_forwarded_tls_protocol_alias = None
        self._x_forwarded_tls_cipher_alias = None
        self._x_forwarded_for_processing_mode = None
        self._x_forwarded_clientcert_subjectdn_enable = None
        self._x_forwarded_clientcert_subjectdn_alias = None
        self._x_forwarded_clientcert_issuerdn_enable = None
        self._x_forwarded_clientcert_issuerdn_alias = None
        self._x_forwarded_clientcert_fingerprint_enable = None
        self._x_forwarded_clientcert_fingerprint_alias = None
        self._x_forwarded_clientcert_clientverify_enable = None
        self._x_forwarded_clientcert_clientverify_alias = None
        self._x_forwarded_clientcert_serialnumber_enable = None
        self._x_forwarded_clientcert_serialnumber_alias = None
        self._x_forwarded_clientcert_enable = None
        self._x_forwarded_clientcert_alias = None
        self._x_forwarded_clientcert_ciphers_enable = None
        self._x_forwarded_clientcert_ciphers_alias = None
        self._x_forwarded_clientcert_end_enable = None
        self._x_forwarded_clientcert_end_alias = None
        self._x_forwarded_tls_alpn_protocol_enable = None
        self._x_forwarded_tls_alpn_protocol_alias = None
        self._x_forwarded_tls_sni_enable = None
        self._x_forwarded_tls_sni_alias = None
        self._x_forwarded_tls_ja3_enable = None
        self._x_forwarded_tls_ja3_alias = None
        self._x_forwarded_tls_ja4_enable = None
        self._x_forwarded_tls_ja4_alias = None
        self.discriminator = None

        if x_forwarded_elb_ip is not None:
            self.x_forwarded_elb_ip = x_forwarded_elb_ip
        if x_forwarded_port is not None:
            self.x_forwarded_port = x_forwarded_port
        if x_forwarded_for_port is not None:
            self.x_forwarded_for_port = x_forwarded_for_port
        if x_forwarded_host is not None:
            self.x_forwarded_host = x_forwarded_host
        if x_forwarded_proto is not None:
            self.x_forwarded_proto = x_forwarded_proto
        if x_real_ip is not None:
            self.x_real_ip = x_real_ip
        if x_forwarded_elb_id is not None:
            self.x_forwarded_elb_id = x_forwarded_elb_id
        if x_forwarded_tls_certificate_id is not None:
            self.x_forwarded_tls_certificate_id = x_forwarded_tls_certificate_id
        if x_forwarded_tls_protocol is not None:
            self.x_forwarded_tls_protocol = x_forwarded_tls_protocol
        if x_forwarded_tls_cipher is not None:
            self.x_forwarded_tls_cipher = x_forwarded_tls_cipher
        if x_forwarded_tls_protocol_alias is not None:
            self.x_forwarded_tls_protocol_alias = x_forwarded_tls_protocol_alias
        if x_forwarded_tls_cipher_alias is not None:
            self.x_forwarded_tls_cipher_alias = x_forwarded_tls_cipher_alias
        if x_forwarded_for_processing_mode is not None:
            self.x_forwarded_for_processing_mode = x_forwarded_for_processing_mode
        if x_forwarded_clientcert_subjectdn_enable is not None:
            self.x_forwarded_clientcert_subjectdn_enable = x_forwarded_clientcert_subjectdn_enable
        if x_forwarded_clientcert_subjectdn_alias is not None:
            self.x_forwarded_clientcert_subjectdn_alias = x_forwarded_clientcert_subjectdn_alias
        if x_forwarded_clientcert_issuerdn_enable is not None:
            self.x_forwarded_clientcert_issuerdn_enable = x_forwarded_clientcert_issuerdn_enable
        if x_forwarded_clientcert_issuerdn_alias is not None:
            self.x_forwarded_clientcert_issuerdn_alias = x_forwarded_clientcert_issuerdn_alias
        if x_forwarded_clientcert_fingerprint_enable is not None:
            self.x_forwarded_clientcert_fingerprint_enable = x_forwarded_clientcert_fingerprint_enable
        if x_forwarded_clientcert_fingerprint_alias is not None:
            self.x_forwarded_clientcert_fingerprint_alias = x_forwarded_clientcert_fingerprint_alias
        if x_forwarded_clientcert_clientverify_enable is not None:
            self.x_forwarded_clientcert_clientverify_enable = x_forwarded_clientcert_clientverify_enable
        if x_forwarded_clientcert_clientverify_alias is not None:
            self.x_forwarded_clientcert_clientverify_alias = x_forwarded_clientcert_clientverify_alias
        if x_forwarded_clientcert_serialnumber_enable is not None:
            self.x_forwarded_clientcert_serialnumber_enable = x_forwarded_clientcert_serialnumber_enable
        if x_forwarded_clientcert_serialnumber_alias is not None:
            self.x_forwarded_clientcert_serialnumber_alias = x_forwarded_clientcert_serialnumber_alias
        if x_forwarded_clientcert_enable is not None:
            self.x_forwarded_clientcert_enable = x_forwarded_clientcert_enable
        if x_forwarded_clientcert_alias is not None:
            self.x_forwarded_clientcert_alias = x_forwarded_clientcert_alias
        if x_forwarded_clientcert_ciphers_enable is not None:
            self.x_forwarded_clientcert_ciphers_enable = x_forwarded_clientcert_ciphers_enable
        if x_forwarded_clientcert_ciphers_alias is not None:
            self.x_forwarded_clientcert_ciphers_alias = x_forwarded_clientcert_ciphers_alias
        if x_forwarded_clientcert_end_enable is not None:
            self.x_forwarded_clientcert_end_enable = x_forwarded_clientcert_end_enable
        if x_forwarded_clientcert_end_alias is not None:
            self.x_forwarded_clientcert_end_alias = x_forwarded_clientcert_end_alias
        if x_forwarded_tls_alpn_protocol_enable is not None:
            self.x_forwarded_tls_alpn_protocol_enable = x_forwarded_tls_alpn_protocol_enable
        if x_forwarded_tls_alpn_protocol_alias is not None:
            self.x_forwarded_tls_alpn_protocol_alias = x_forwarded_tls_alpn_protocol_alias
        if x_forwarded_tls_sni_enable is not None:
            self.x_forwarded_tls_sni_enable = x_forwarded_tls_sni_enable
        if x_forwarded_tls_sni_alias is not None:
            self.x_forwarded_tls_sni_alias = x_forwarded_tls_sni_alias
        if x_forwarded_tls_ja3_enable is not None:
            self.x_forwarded_tls_ja3_enable = x_forwarded_tls_ja3_enable
        if x_forwarded_tls_ja3_alias is not None:
            self.x_forwarded_tls_ja3_alias = x_forwarded_tls_ja3_alias
        if x_forwarded_tls_ja4_enable is not None:
            self.x_forwarded_tls_ja4_enable = x_forwarded_tls_ja4_enable
        if x_forwarded_tls_ja4_alias is not None:
            self.x_forwarded_tls_ja4_alias = x_forwarded_tls_ja4_alias

    @property
    def x_forwarded_elb_ip(self):
        r"""Gets the x_forwarded_elb_ip of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端服务器。

        :return: The x_forwarded_elb_ip of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_elb_ip

    @x_forwarded_elb_ip.setter
    def x_forwarded_elb_ip(self, x_forwarded_elb_ip):
        r"""Sets the x_forwarded_elb_ip of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端服务器。

        :param x_forwarded_elb_ip: The x_forwarded_elb_ip of this ListenerInsertHeaders.
        :type x_forwarded_elb_ip: bool
        """
        self._x_forwarded_elb_ip = x_forwarded_elb_ip

    @property
    def x_forwarded_port(self):
        r"""Gets the x_forwarded_port of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端服务器。

        :return: The x_forwarded_port of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_port

    @x_forwarded_port.setter
    def x_forwarded_port(self, x_forwarded_port):
        r"""Sets the x_forwarded_port of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端服务器。

        :param x_forwarded_port: The x_forwarded_port of this ListenerInsertHeaders.
        :type x_forwarded_port: bool
        """
        self._x_forwarded_port = x_forwarded_port

    @property
    def x_forwarded_for_port(self):
        r"""Gets the x_forwarded_for_port of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端服务器。

        :return: The x_forwarded_for_port of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_for_port

    @x_forwarded_for_port.setter
    def x_forwarded_for_port(self, x_forwarded_for_port):
        r"""Sets the x_forwarded_for_port of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端服务器。

        :param x_forwarded_for_port: The x_forwarded_for_port of this ListenerInsertHeaders.
        :type x_forwarded_for_port: bool
        """
        self._x_forwarded_for_port = x_forwarded_for_port

    @property
    def x_forwarded_host(self):
        r"""Gets the x_forwarded_host of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端服务器。

        :return: The x_forwarded_host of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_host

    @x_forwarded_host.setter
    def x_forwarded_host(self, x_forwarded_host):
        r"""Sets the x_forwarded_host of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端服务器。

        :param x_forwarded_host: The x_forwarded_host of this ListenerInsertHeaders.
        :type x_forwarded_host: bool
        """
        self._x_forwarded_host = x_forwarded_host

    @property
    def x_forwarded_proto(self):
        r"""Gets the x_forwarded_proto of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端服务器。

        :return: The x_forwarded_proto of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_proto

    @x_forwarded_proto.setter
    def x_forwarded_proto(self, x_forwarded_proto):
        r"""Sets the x_forwarded_proto of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端服务器。

        :param x_forwarded_proto: The x_forwarded_proto of this ListenerInsertHeaders.
        :type x_forwarded_proto: bool
        """
        self._x_forwarded_proto = x_forwarded_proto

    @property
    def x_real_ip(self):
        r"""Gets the x_real_ip of this ListenerInsertHeaders.

        **参数解释**：X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端服务器。

        :return: The x_real_ip of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_real_ip

    @x_real_ip.setter
    def x_real_ip(self, x_real_ip):
        r"""Sets the x_real_ip of this ListenerInsertHeaders.

        **参数解释**：X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端服务器。

        :param x_real_ip: The x_real_ip of this ListenerInsertHeaders.
        :type x_real_ip: bool
        """
        self._x_real_ip = x_real_ip

    @property
    def x_forwarded_elb_id(self):
        r"""Gets the x_forwarded_elb_id of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端服务器。

        :return: The x_forwarded_elb_id of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_elb_id

    @x_forwarded_elb_id.setter
    def x_forwarded_elb_id(self, x_forwarded_elb_id):
        r"""Sets the x_forwarded_elb_id of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端服务器。

        :param x_forwarded_elb_id: The x_forwarded_elb_id of this ListenerInsertHeaders.
        :type x_forwarded_elb_id: bool
        """
        self._x_forwarded_elb_id = x_forwarded_elb_id

    @property
    def x_forwarded_tls_certificate_id(self):
        r"""Gets the x_forwarded_tls_certificate_id of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端服务器。

        :return: The x_forwarded_tls_certificate_id of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_certificate_id

    @x_forwarded_tls_certificate_id.setter
    def x_forwarded_tls_certificate_id(self, x_forwarded_tls_certificate_id):
        r"""Sets the x_forwarded_tls_certificate_id of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端服务器。

        :param x_forwarded_tls_certificate_id: The x_forwarded_tls_certificate_id of this ListenerInsertHeaders.
        :type x_forwarded_tls_certificate_id: bool
        """
        self._x_forwarded_tls_certificate_id = x_forwarded_tls_certificate_id

    @property
    def x_forwarded_tls_protocol(self):
        r"""Gets the x_forwarded_tls_protocol of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端服务器。

        :return: The x_forwarded_tls_protocol of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_protocol

    @x_forwarded_tls_protocol.setter
    def x_forwarded_tls_protocol(self, x_forwarded_tls_protocol):
        r"""Sets the x_forwarded_tls_protocol of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端服务器。

        :param x_forwarded_tls_protocol: The x_forwarded_tls_protocol of this ListenerInsertHeaders.
        :type x_forwarded_tls_protocol: bool
        """
        self._x_forwarded_tls_protocol = x_forwarded_tls_protocol

    @property
    def x_forwarded_tls_cipher(self):
        r"""Gets the x_forwarded_tls_cipher of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端服务器。

        :return: The x_forwarded_tls_cipher of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_cipher

    @x_forwarded_tls_cipher.setter
    def x_forwarded_tls_cipher(self, x_forwarded_tls_cipher):
        r"""Sets the x_forwarded_tls_cipher of this ListenerInsertHeaders.

        **参数解释**：X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端服务器。

        :param x_forwarded_tls_cipher: The x_forwarded_tls_cipher of this ListenerInsertHeaders.
        :type x_forwarded_tls_cipher: bool
        """
        self._x_forwarded_tls_cipher = x_forwarded_tls_cipher

    @property
    def x_forwarded_tls_protocol_alias(self):
        r"""Gets the x_forwarded_tls_protocol_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-TLS-Protocol头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Protocol 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_protocol_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_protocol_alias

    @x_forwarded_tls_protocol_alias.setter
    def x_forwarded_tls_protocol_alias(self, x_forwarded_tls_protocol_alias):
        r"""Sets the x_forwarded_tls_protocol_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-TLS-Protocol头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Protocol 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_protocol_alias: The x_forwarded_tls_protocol_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_protocol_alias: str
        """
        self._x_forwarded_tls_protocol_alias = x_forwarded_tls_protocol_alias

    @property
    def x_forwarded_tls_cipher_alias(self):
        r"""Gets the x_forwarded_tls_cipher_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-TLS-Cipher头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Cipher 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_cipher_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_cipher_alias

    @x_forwarded_tls_cipher_alias.setter
    def x_forwarded_tls_cipher_alias(self, x_forwarded_tls_cipher_alias):
        r"""Sets the x_forwarded_tls_cipher_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-TLS-Cipher头字段名称。  **约束限制**：只有当 X-Forwarded-TLS-Cipher 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_cipher_alias: The x_forwarded_tls_cipher_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_cipher_alias: str
        """
        self._x_forwarded_tls_cipher_alias = x_forwarded_tls_cipher_alias

    @property
    def x_forwarded_for_processing_mode(self):
        r"""Gets the x_forwarded_for_processing_mode of this ListenerInsertHeaders.

        **参数解释**：处理X-Forwarded-For头字段的模式： 配置 append，将请求发送至后端服务之前把最后一跳 IP 加入X-Forwarded-For头字段； 配置 remove，请求发送至后端服务之前删除X-Forwarded-For标头，无论请求是否携带X-Forwarded-For头字段； 配置preserve，保留请求中已有的X-Forwarded-For标头；  **约束限制**：仅HTTP、HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段；  **取值范围**：append、remove、preserve  **默认取值**：append

        :return: The x_forwarded_for_processing_mode of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_for_processing_mode

    @x_forwarded_for_processing_mode.setter
    def x_forwarded_for_processing_mode(self, x_forwarded_for_processing_mode):
        r"""Sets the x_forwarded_for_processing_mode of this ListenerInsertHeaders.

        **参数解释**：处理X-Forwarded-For头字段的模式： 配置 append，将请求发送至后端服务之前把最后一跳 IP 加入X-Forwarded-For头字段； 配置 remove，请求发送至后端服务之前删除X-Forwarded-For标头，无论请求是否携带X-Forwarded-For头字段； 配置preserve，保留请求中已有的X-Forwarded-For标头；  **约束限制**：仅HTTP、HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段；  **取值范围**：append、remove、preserve  **默认取值**：append

        :param x_forwarded_for_processing_mode: The x_forwarded_for_processing_mode of this ListenerInsertHeaders.
        :type x_forwarded_for_processing_mode: str
        """
        self._x_forwarded_for_processing_mode = x_forwarded_for_processing_mode

    @property
    def x_forwarded_clientcert_subjectdn_enable(self):
        r"""Gets the x_forwarded_clientcert_subjectdn_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-subjectdn头字段获取访问负载均衡实例客户端证书的所有者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_subjectdn_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_subjectdn_enable

    @x_forwarded_clientcert_subjectdn_enable.setter
    def x_forwarded_clientcert_subjectdn_enable(self, x_forwarded_clientcert_subjectdn_enable):
        r"""Sets the x_forwarded_clientcert_subjectdn_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-subjectdn头字段获取访问负载均衡实例客户端证书的所有者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_subjectdn_enable: The x_forwarded_clientcert_subjectdn_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_subjectdn_enable: bool
        """
        self._x_forwarded_clientcert_subjectdn_enable = x_forwarded_clientcert_subjectdn_enable

    @property
    def x_forwarded_clientcert_subjectdn_alias(self):
        r"""Gets the x_forwarded_clientcert_subjectdn_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-subjectdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-subjectdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_subjectdn_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_subjectdn_alias

    @x_forwarded_clientcert_subjectdn_alias.setter
    def x_forwarded_clientcert_subjectdn_alias(self, x_forwarded_clientcert_subjectdn_alias):
        r"""Sets the x_forwarded_clientcert_subjectdn_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-subjectdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-subjectdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_subjectdn_alias: The x_forwarded_clientcert_subjectdn_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_subjectdn_alias: str
        """
        self._x_forwarded_clientcert_subjectdn_alias = x_forwarded_clientcert_subjectdn_alias

    @property
    def x_forwarded_clientcert_issuerdn_enable(self):
        r"""Gets the x_forwarded_clientcert_issuerdn_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-issuerdn头字段获取访问负载均衡实例客户端证书的发行者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_issuerdn_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_issuerdn_enable

    @x_forwarded_clientcert_issuerdn_enable.setter
    def x_forwarded_clientcert_issuerdn_enable(self, x_forwarded_clientcert_issuerdn_enable):
        r"""Sets the x_forwarded_clientcert_issuerdn_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-issuerdn头字段获取访问负载均衡实例客户端证书的发行者信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_issuerdn_enable: The x_forwarded_clientcert_issuerdn_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_issuerdn_enable: bool
        """
        self._x_forwarded_clientcert_issuerdn_enable = x_forwarded_clientcert_issuerdn_enable

    @property
    def x_forwarded_clientcert_issuerdn_alias(self):
        r"""Gets the x_forwarded_clientcert_issuerdn_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-issuerdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-issuerdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_issuerdn_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_issuerdn_alias

    @x_forwarded_clientcert_issuerdn_alias.setter
    def x_forwarded_clientcert_issuerdn_alias(self, x_forwarded_clientcert_issuerdn_alias):
        r"""Sets the x_forwarded_clientcert_issuerdn_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-issuerdn头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-issuerdn-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_issuerdn_alias: The x_forwarded_clientcert_issuerdn_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_issuerdn_alias: str
        """
        self._x_forwarded_clientcert_issuerdn_alias = x_forwarded_clientcert_issuerdn_alias

    @property
    def x_forwarded_clientcert_fingerprint_enable(self):
        r"""Gets the x_forwarded_clientcert_fingerprint_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-fingerprint头字段获取访问负载均衡实例客户端证书的指纹取值。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_fingerprint_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_fingerprint_enable

    @x_forwarded_clientcert_fingerprint_enable.setter
    def x_forwarded_clientcert_fingerprint_enable(self, x_forwarded_clientcert_fingerprint_enable):
        r"""Sets the x_forwarded_clientcert_fingerprint_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-fingerprint头字段获取访问负载均衡实例客户端证书的指纹取值。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_fingerprint_enable: The x_forwarded_clientcert_fingerprint_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_fingerprint_enable: bool
        """
        self._x_forwarded_clientcert_fingerprint_enable = x_forwarded_clientcert_fingerprint_enable

    @property
    def x_forwarded_clientcert_fingerprint_alias(self):
        r"""Gets the x_forwarded_clientcert_fingerprint_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-fingerprint头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-fingerprint-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_fingerprint_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_fingerprint_alias

    @x_forwarded_clientcert_fingerprint_alias.setter
    def x_forwarded_clientcert_fingerprint_alias(self, x_forwarded_clientcert_fingerprint_alias):
        r"""Sets the x_forwarded_clientcert_fingerprint_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-fingerprint头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-fingerprint-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_fingerprint_alias: The x_forwarded_clientcert_fingerprint_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_fingerprint_alias: str
        """
        self._x_forwarded_clientcert_fingerprint_alias = x_forwarded_clientcert_fingerprint_alias

    @property
    def x_forwarded_clientcert_clientverify_enable(self):
        r"""Gets the x_forwarded_clientcert_clientverify_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-clientverify头字段获取对访问负载均衡实例客户端证书的校验结果。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_clientverify_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_clientverify_enable

    @x_forwarded_clientcert_clientverify_enable.setter
    def x_forwarded_clientcert_clientverify_enable(self, x_forwarded_clientcert_clientverify_enable):
        r"""Sets the x_forwarded_clientcert_clientverify_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-clientverify头字段获取对访问负载均衡实例客户端证书的校验结果。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_clientverify_enable: The x_forwarded_clientcert_clientverify_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_clientverify_enable: bool
        """
        self._x_forwarded_clientcert_clientverify_enable = x_forwarded_clientcert_clientverify_enable

    @property
    def x_forwarded_clientcert_clientverify_alias(self):
        r"""Gets the x_forwarded_clientcert_clientverify_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-clientverify头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-clientverify-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_clientverify_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_clientverify_alias

    @x_forwarded_clientcert_clientverify_alias.setter
    def x_forwarded_clientcert_clientverify_alias(self, x_forwarded_clientcert_clientverify_alias):
        r"""Sets the x_forwarded_clientcert_clientverify_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-clientverify头字段名称。  **约束限制**：只有当 X-Forwarded-Clientcert-clientverify-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_clientverify_alias: The x_forwarded_clientcert_clientverify_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_clientverify_alias: str
        """
        self._x_forwarded_clientcert_clientverify_alias = x_forwarded_clientcert_clientverify_alias

    @property
    def x_forwarded_clientcert_serialnumber_enable(self):
        r"""Gets the x_forwarded_clientcert_serialnumber_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-serialnumber 头字段获取客户端证书的序列号信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_serialnumber_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_serialnumber_enable

    @x_forwarded_clientcert_serialnumber_enable.setter
    def x_forwarded_clientcert_serialnumber_enable(self, x_forwarded_clientcert_serialnumber_enable):
        r"""Sets the x_forwarded_clientcert_serialnumber_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-serialnumber 头字段获取客户端证书的序列号信息。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_serialnumber_enable: The x_forwarded_clientcert_serialnumber_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_serialnumber_enable: bool
        """
        self._x_forwarded_clientcert_serialnumber_enable = x_forwarded_clientcert_serialnumber_enable

    @property
    def x_forwarded_clientcert_serialnumber_alias(self):
        r"""Gets the x_forwarded_clientcert_serialnumber_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-serialnumber头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-serialnumber-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_serialnumber_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_serialnumber_alias

    @x_forwarded_clientcert_serialnumber_alias.setter
    def x_forwarded_clientcert_serialnumber_alias(self, x_forwarded_clientcert_serialnumber_alias):
        r"""Sets the x_forwarded_clientcert_serialnumber_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-serialnumber头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-serialnumber-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_serialnumber_alias: The x_forwarded_clientcert_serialnumber_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_serialnumber_alias: str
        """
        self._x_forwarded_clientcert_serialnumber_alias = x_forwarded_clientcert_serialnumber_alias

    @property
    def x_forwarded_clientcert_enable(self):
        r"""Gets the x_forwarded_clientcert_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert 头字段获取客户端证书的内容。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_enable

    @x_forwarded_clientcert_enable.setter
    def x_forwarded_clientcert_enable(self, x_forwarded_clientcert_enable):
        r"""Sets the x_forwarded_clientcert_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert 头字段获取客户端证书的内容。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_enable: The x_forwarded_clientcert_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_enable: bool
        """
        self._x_forwarded_clientcert_enable = x_forwarded_clientcert_enable

    @property
    def x_forwarded_clientcert_alias(self):
        r"""Gets the x_forwarded_clientcert_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_alias

    @x_forwarded_clientcert_alias.setter
    def x_forwarded_clientcert_alias(self, x_forwarded_clientcert_alias):
        r"""Sets the x_forwarded_clientcert_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_alias: The x_forwarded_clientcert_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_alias: str
        """
        self._x_forwarded_clientcert_alias = x_forwarded_clientcert_alias

    @property
    def x_forwarded_clientcert_ciphers_enable(self):
        r"""Gets the x_forwarded_clientcert_ciphers_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-ciphers 头字段获取客户端支持的TLS加密套件。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_ciphers_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_ciphers_enable

    @x_forwarded_clientcert_ciphers_enable.setter
    def x_forwarded_clientcert_ciphers_enable(self, x_forwarded_clientcert_ciphers_enable):
        r"""Sets the x_forwarded_clientcert_ciphers_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-ciphers 头字段获取客户端支持的TLS加密套件。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_ciphers_enable: The x_forwarded_clientcert_ciphers_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_ciphers_enable: bool
        """
        self._x_forwarded_clientcert_ciphers_enable = x_forwarded_clientcert_ciphers_enable

    @property
    def x_forwarded_clientcert_ciphers_alias(self):
        r"""Gets the x_forwarded_clientcert_ciphers_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-ciphers头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-ciphers-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_ciphers_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_ciphers_alias

    @x_forwarded_clientcert_ciphers_alias.setter
    def x_forwarded_clientcert_ciphers_alias(self, x_forwarded_clientcert_ciphers_alias):
        r"""Sets the x_forwarded_clientcert_ciphers_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-ciphers头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-ciphers-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_ciphers_alias: The x_forwarded_clientcert_ciphers_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_ciphers_alias: str
        """
        self._x_forwarded_clientcert_ciphers_alias = x_forwarded_clientcert_ciphers_alias

    @property
    def x_forwarded_clientcert_end_enable(self):
        r"""Gets the x_forwarded_clientcert_end_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-end 头字段获取客户端证书的结束日期。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_clientcert_end_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_clientcert_end_enable

    @x_forwarded_clientcert_end_enable.setter
    def x_forwarded_clientcert_end_enable(self, x_forwarded_clientcert_end_enable):
        r"""Sets the x_forwarded_clientcert_end_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Clientcert-end 头字段获取客户端证书的结束日期。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_clientcert_end_enable: The x_forwarded_clientcert_end_enable of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_end_enable: bool
        """
        self._x_forwarded_clientcert_end_enable = x_forwarded_clientcert_end_enable

    @property
    def x_forwarded_clientcert_end_alias(self):
        r"""Gets the x_forwarded_clientcert_end_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-end头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-end-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_clientcert_end_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_clientcert_end_alias

    @x_forwarded_clientcert_end_alias.setter
    def x_forwarded_clientcert_end_alias(self, x_forwarded_clientcert_end_alias):
        r"""Sets the x_forwarded_clientcert_end_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Clientcert-end头字段名称。  **约束限制**：只有当X-Forwarded-Clientcert-end-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC、TLS协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_clientcert_end_alias: The x_forwarded_clientcert_end_alias of this ListenerInsertHeaders.
        :type x_forwarded_clientcert_end_alias: str
        """
        self._x_forwarded_clientcert_end_alias = x_forwarded_clientcert_end_alias

    @property
    def x_forwarded_tls_alpn_protocol_enable(self):
        r"""Gets the x_forwarded_tls_alpn_protocol_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Alpn-Protocol 头字段获取客户端和服务器之间ALPN（Application-Layer Protocol Negotiation）协商的应用层协议。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_tls_alpn_protocol_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_alpn_protocol_enable

    @x_forwarded_tls_alpn_protocol_enable.setter
    def x_forwarded_tls_alpn_protocol_enable(self, x_forwarded_tls_alpn_protocol_enable):
        r"""Sets the x_forwarded_tls_alpn_protocol_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Alpn-Protocol 头字段获取客户端和服务器之间ALPN（Application-Layer Protocol Negotiation）协商的应用层协议。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_tls_alpn_protocol_enable: The x_forwarded_tls_alpn_protocol_enable of this ListenerInsertHeaders.
        :type x_forwarded_tls_alpn_protocol_enable: bool
        """
        self._x_forwarded_tls_alpn_protocol_enable = x_forwarded_tls_alpn_protocol_enable

    @property
    def x_forwarded_tls_alpn_protocol_alias(self):
        r"""Gets the x_forwarded_tls_alpn_protocol_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Alpn-Protocol头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Alpn-Protocol-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_alpn_protocol_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_alpn_protocol_alias

    @x_forwarded_tls_alpn_protocol_alias.setter
    def x_forwarded_tls_alpn_protocol_alias(self, x_forwarded_tls_alpn_protocol_alias):
        r"""Sets the x_forwarded_tls_alpn_protocol_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Alpn-Protocol头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Alpn-Protocol-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_alpn_protocol_alias: The x_forwarded_tls_alpn_protocol_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_alpn_protocol_alias: str
        """
        self._x_forwarded_tls_alpn_protocol_alias = x_forwarded_tls_alpn_protocol_alias

    @property
    def x_forwarded_tls_sni_enable(self):
        r"""Gets the x_forwarded_tls_sni_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Sni 头字段获取客户端访问的sni证书的域名。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_tls_sni_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_sni_enable

    @x_forwarded_tls_sni_enable.setter
    def x_forwarded_tls_sni_enable(self, x_forwarded_tls_sni_enable):
        r"""Sets the x_forwarded_tls_sni_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Sni 头字段获取客户端访问的sni证书的域名。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_tls_sni_enable: The x_forwarded_tls_sni_enable of this ListenerInsertHeaders.
        :type x_forwarded_tls_sni_enable: bool
        """
        self._x_forwarded_tls_sni_enable = x_forwarded_tls_sni_enable

    @property
    def x_forwarded_tls_sni_alias(self):
        r"""Gets the x_forwarded_tls_sni_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Sni头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Sni-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_sni_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_sni_alias

    @x_forwarded_tls_sni_alias.setter
    def x_forwarded_tls_sni_alias(self, x_forwarded_tls_sni_alias):
        r"""Sets the x_forwarded_tls_sni_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Sni头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Sni-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_sni_alias: The x_forwarded_tls_sni_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_sni_alias: str
        """
        self._x_forwarded_tls_sni_alias = x_forwarded_tls_sni_alias

    @property
    def x_forwarded_tls_ja3_enable(self):
        r"""Gets the x_forwarded_tls_ja3_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Ja3头字段获取访问负载均衡实例客户端的ja3指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_tls_ja3_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_ja3_enable

    @x_forwarded_tls_ja3_enable.setter
    def x_forwarded_tls_ja3_enable(self, x_forwarded_tls_ja3_enable):
        r"""Sets the x_forwarded_tls_ja3_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Ja3头字段获取访问负载均衡实例客户端的ja3指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_tls_ja3_enable: The x_forwarded_tls_ja3_enable of this ListenerInsertHeaders.
        :type x_forwarded_tls_ja3_enable: bool
        """
        self._x_forwarded_tls_ja3_enable = x_forwarded_tls_ja3_enable

    @property
    def x_forwarded_tls_ja3_alias(self):
        r"""Gets the x_forwarded_tls_ja3_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Ja3头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja3-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_ja3_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_ja3_alias

    @x_forwarded_tls_ja3_alias.setter
    def x_forwarded_tls_ja3_alias(self, x_forwarded_tls_ja3_alias):
        r"""Sets the x_forwarded_tls_ja3_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Ja3头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja3-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_ja3_alias: The x_forwarded_tls_ja3_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_ja3_alias: str
        """
        self._x_forwarded_tls_ja3_alias = x_forwarded_tls_ja3_alias

    @property
    def x_forwarded_tls_ja4_enable(self):
        r"""Gets the x_forwarded_tls_ja4_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Ja4头字段获取访问负载均衡实例客户端的ja4指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :return: The x_forwarded_tls_ja4_enable of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_ja4_enable

    @x_forwarded_tls_ja4_enable.setter
    def x_forwarded_tls_ja4_enable(self, x_forwarded_tls_ja4_enable):
        r"""Sets the x_forwarded_tls_ja4_enable of this ListenerInsertHeaders.

        **参数解释**：是否通过X-Forwarded-Tls-Ja4头字段获取访问负载均衡实例客户端的ja4指纹。  **约束限制**：仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段。  **取值范围**：true、false  **默认取值**：false

        :param x_forwarded_tls_ja4_enable: The x_forwarded_tls_ja4_enable of this ListenerInsertHeaders.
        :type x_forwarded_tls_ja4_enable: bool
        """
        self._x_forwarded_tls_ja4_enable = x_forwarded_tls_ja4_enable

    @property
    def x_forwarded_tls_ja4_alias(self):
        r"""Gets the x_forwarded_tls_ja4_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Ja4头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja4-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :return: The x_forwarded_tls_ja4_alias of this ListenerInsertHeaders.
        :rtype: str
        """
        return self._x_forwarded_tls_ja4_alias

    @x_forwarded_tls_ja4_alias.setter
    def x_forwarded_tls_ja4_alias(self, x_forwarded_tls_ja4_alias):
        r"""Sets the x_forwarded_tls_ja4_alias of this ListenerInsertHeaders.

        **参数解释**：自定义X-Forwarded-Tls-Ja4头字段名称。  **约束限制**：只有当X-Forwarded-Tls-Ja4-enable 的值为 true 时，此值才会生效。仅HTTPS、TERMINATED_HTTPS、QUIC协议的监听器支持该字段  **取值范围**：1~40 个字符。支持字母 a~z、短划线（-）、下划线（_）和数字。  **默认取值**：无

        :param x_forwarded_tls_ja4_alias: The x_forwarded_tls_ja4_alias of this ListenerInsertHeaders.
        :type x_forwarded_tls_ja4_alias: str
        """
        self._x_forwarded_tls_ja4_alias = x_forwarded_tls_ja4_alias

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
        if not isinstance(other, ListenerInsertHeaders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
