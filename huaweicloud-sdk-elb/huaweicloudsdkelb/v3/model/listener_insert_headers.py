# coding: utf-8

import six

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
        'x_forwarded_tls_cipher': 'bool'
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
        'x_forwarded_tls_cipher': 'X-Forwarded-TLS-Cipher'
    }

    def __init__(self, x_forwarded_elb_ip=None, x_forwarded_port=None, x_forwarded_for_port=None, x_forwarded_host=None, x_forwarded_proto=None, x_real_ip=None, x_forwarded_elb_id=None, x_forwarded_tls_certificate_id=None, x_forwarded_tls_protocol=None, x_forwarded_tls_cipher=None):
        """ListenerInsertHeaders

        The model defined in huaweicloud sdk

        :param x_forwarded_elb_ip: X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端云服务器。
        :type x_forwarded_elb_ip: bool
        :param x_forwarded_port: X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端云服务器。
        :type x_forwarded_port: bool
        :param x_forwarded_for_port: X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端云服务器。
        :type x_forwarded_for_port: bool
        :param x_forwarded_host: X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端云服务器。
        :type x_forwarded_host: bool
        :param x_forwarded_proto: X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端云服务器。
        :type x_forwarded_proto: bool
        :param x_real_ip: X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端云服务器。
        :type x_real_ip: bool
        :param x_forwarded_elb_id: X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端云服务器。
        :type x_forwarded_elb_id: bool
        :param x_forwarded_tls_certificate_id: X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端云服务器。
        :type x_forwarded_tls_certificate_id: bool
        :param x_forwarded_tls_protocol: X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端云服务器。
        :type x_forwarded_tls_protocol: bool
        :param x_forwarded_tls_cipher: X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端云服务器。
        :type x_forwarded_tls_cipher: bool
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

    @property
    def x_forwarded_elb_ip(self):
        """Gets the x_forwarded_elb_ip of this ListenerInsertHeaders.

        X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端云服务器。

        :return: The x_forwarded_elb_ip of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_elb_ip

    @x_forwarded_elb_ip.setter
    def x_forwarded_elb_ip(self, x_forwarded_elb_ip):
        """Sets the x_forwarded_elb_ip of this ListenerInsertHeaders.

        X-Forwarded-ELB-IP设为true可以将ELB实例的eip地址从报文的http头中带到后端云服务器。

        :param x_forwarded_elb_ip: The x_forwarded_elb_ip of this ListenerInsertHeaders.
        :type x_forwarded_elb_ip: bool
        """
        self._x_forwarded_elb_ip = x_forwarded_elb_ip

    @property
    def x_forwarded_port(self):
        """Gets the x_forwarded_port of this ListenerInsertHeaders.

        X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端云服务器。

        :return: The x_forwarded_port of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_port

    @x_forwarded_port.setter
    def x_forwarded_port(self, x_forwarded_port):
        """Sets the x_forwarded_port of this ListenerInsertHeaders.

        X-Forwarded-Port设为true可以将ELB实例的监听端口从报文的http头中带到后端云服务器。

        :param x_forwarded_port: The x_forwarded_port of this ListenerInsertHeaders.
        :type x_forwarded_port: bool
        """
        self._x_forwarded_port = x_forwarded_port

    @property
    def x_forwarded_for_port(self):
        """Gets the x_forwarded_for_port of this ListenerInsertHeaders.

        X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端云服务器。

        :return: The x_forwarded_for_port of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_for_port

    @x_forwarded_for_port.setter
    def x_forwarded_for_port(self, x_forwarded_for_port):
        """Sets the x_forwarded_for_port of this ListenerInsertHeaders.

        X-Forwarded-For-Port设为true可以将客户端的源端口从报文的http头中带到后端云服务器。

        :param x_forwarded_for_port: The x_forwarded_for_port of this ListenerInsertHeaders.
        :type x_forwarded_for_port: bool
        """
        self._x_forwarded_for_port = x_forwarded_for_port

    @property
    def x_forwarded_host(self):
        """Gets the x_forwarded_host of this ListenerInsertHeaders.

        X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端云服务器。

        :return: The x_forwarded_host of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_host

    @x_forwarded_host.setter
    def x_forwarded_host(self, x_forwarded_host):
        """Sets the x_forwarded_host of this ListenerInsertHeaders.

        X-Forwarded-Host设为true可以将客户请求头的X-Forwarded-Host设置为请求头的Host带到后端云服务器。

        :param x_forwarded_host: The x_forwarded_host of this ListenerInsertHeaders.
        :type x_forwarded_host: bool
        """
        self._x_forwarded_host = x_forwarded_host

    @property
    def x_forwarded_proto(self):
        """Gets the x_forwarded_proto of this ListenerInsertHeaders.

        X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端云服务器。

        :return: The x_forwarded_proto of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_proto

    @x_forwarded_proto.setter
    def x_forwarded_proto(self, x_forwarded_proto):
        """Sets the x_forwarded_proto of this ListenerInsertHeaders.

        X-Forwarded-Proto设为true可以将负载均衡器实例的监听协议通过报文的http头带到后端云服务器。

        :param x_forwarded_proto: The x_forwarded_proto of this ListenerInsertHeaders.
        :type x_forwarded_proto: bool
        """
        self._x_forwarded_proto = x_forwarded_proto

    @property
    def x_real_ip(self):
        """Gets the x_real_ip of this ListenerInsertHeaders.

        X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端云服务器。

        :return: The x_real_ip of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_real_ip

    @x_real_ip.setter
    def x_real_ip(self, x_real_ip):
        """Sets the x_real_ip of this ListenerInsertHeaders.

        X-Real-IP设为true可以将客户端的IP通过报文的http头带到后端云服务器。

        :param x_real_ip: The x_real_ip of this ListenerInsertHeaders.
        :type x_real_ip: bool
        """
        self._x_real_ip = x_real_ip

    @property
    def x_forwarded_elb_id(self):
        """Gets the x_forwarded_elb_id of this ListenerInsertHeaders.

        X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端云服务器。

        :return: The x_forwarded_elb_id of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_elb_id

    @x_forwarded_elb_id.setter
    def x_forwarded_elb_id(self, x_forwarded_elb_id):
        """Sets the x_forwarded_elb_id of this ListenerInsertHeaders.

        X-Forwarded-ELB-ID设为true可以将负载均衡器实例的ID通过报文的http头带到后端云服务器。

        :param x_forwarded_elb_id: The x_forwarded_elb_id of this ListenerInsertHeaders.
        :type x_forwarded_elb_id: bool
        """
        self._x_forwarded_elb_id = x_forwarded_elb_id

    @property
    def x_forwarded_tls_certificate_id(self):
        """Gets the x_forwarded_tls_certificate_id of this ListenerInsertHeaders.

        X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端云服务器。

        :return: The x_forwarded_tls_certificate_id of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_certificate_id

    @x_forwarded_tls_certificate_id.setter
    def x_forwarded_tls_certificate_id(self, x_forwarded_tls_certificate_id):
        """Sets the x_forwarded_tls_certificate_id of this ListenerInsertHeaders.

        X-Forwarded-TLS-Certificate-ID设为true可以将负载均衡器实例的证书ID通过报文的http头带到后端云服务器。

        :param x_forwarded_tls_certificate_id: The x_forwarded_tls_certificate_id of this ListenerInsertHeaders.
        :type x_forwarded_tls_certificate_id: bool
        """
        self._x_forwarded_tls_certificate_id = x_forwarded_tls_certificate_id

    @property
    def x_forwarded_tls_protocol(self):
        """Gets the x_forwarded_tls_protocol of this ListenerInsertHeaders.

        X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端云服务器。

        :return: The x_forwarded_tls_protocol of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_protocol

    @x_forwarded_tls_protocol.setter
    def x_forwarded_tls_protocol(self, x_forwarded_tls_protocol):
        """Sets the x_forwarded_tls_protocol of this ListenerInsertHeaders.

        X-Forwarded-TLS-Protocol设为true可以将负载均衡器实例的算法协议通过报文的http头带到后端云服务器。

        :param x_forwarded_tls_protocol: The x_forwarded_tls_protocol of this ListenerInsertHeaders.
        :type x_forwarded_tls_protocol: bool
        """
        self._x_forwarded_tls_protocol = x_forwarded_tls_protocol

    @property
    def x_forwarded_tls_cipher(self):
        """Gets the x_forwarded_tls_cipher of this ListenerInsertHeaders.

        X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端云服务器。

        :return: The x_forwarded_tls_cipher of this ListenerInsertHeaders.
        :rtype: bool
        """
        return self._x_forwarded_tls_cipher

    @x_forwarded_tls_cipher.setter
    def x_forwarded_tls_cipher(self, x_forwarded_tls_cipher):
        """Sets the x_forwarded_tls_cipher of this ListenerInsertHeaders.

        X-Forwarded-TLS-Cipher设为true可以将负载均衡器实例的算法套件通过报文的http头带到后端云服务器。

        :param x_forwarded_tls_cipher: The x_forwarded_tls_cipher of this ListenerInsertHeaders.
        :type x_forwarded_tls_cipher: bool
        """
        self._x_forwarded_tls_cipher = x_forwarded_tls_cipher

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
        if not isinstance(other, ListenerInsertHeaders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
