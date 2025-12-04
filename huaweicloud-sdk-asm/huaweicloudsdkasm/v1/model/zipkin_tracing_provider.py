# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ZipkinTracingProvider:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'port': 'int'
    }

    attribute_map = {
        'service': 'service',
        'port': 'port'
    }

    def __init__(self, service=None, port=None):
        r"""ZipkinTracingProvider

        The model defined in huaweicloud sdk

        :param service: zipkin服务地址
        :type service: str
        :param port: zipkin服务端口
        :type port: int
        """
        
        

        self._service = None
        self._port = None
        self.discriminator = None

        if service is not None:
            self.service = service
        if port is not None:
            self.port = port

    @property
    def service(self):
        r"""Gets the service of this ZipkinTracingProvider.

        zipkin服务地址

        :return: The service of this ZipkinTracingProvider.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ZipkinTracingProvider.

        zipkin服务地址

        :param service: The service of this ZipkinTracingProvider.
        :type service: str
        """
        self._service = service

    @property
    def port(self):
        r"""Gets the port of this ZipkinTracingProvider.

        zipkin服务端口

        :return: The port of this ZipkinTracingProvider.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ZipkinTracingProvider.

        zipkin服务端口

        :param port: The port of this ZipkinTracingProvider.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, ZipkinTracingProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
