# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'service': 'str',
        'protocol': 'str',
        'status': 'str'
    }

    attribute_map = {
        'port': 'port',
        'service': 'service',
        'protocol': 'protocol',
        'status': 'status'
    }

    def __init__(self, port=None, service=None, protocol=None, status=None):
        """PortItem

        The model defined in huaweicloud sdk

        :param port: 端口号
        :type port: int
        :param service: 服务
        :type service: str
        :param protocol: 端口协议:   * TCP   * UDP 
        :type protocol: str
        :param status: 端口状态:   * filtered - 过滤的   * open - 开放 
        :type status: str
        """
        
        

        self._port = None
        self._service = None
        self._protocol = None
        self._status = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if service is not None:
            self.service = service
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status

    @property
    def port(self):
        """Gets the port of this PortItem.

        端口号

        :return: The port of this PortItem.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortItem.

        端口号

        :param port: The port of this PortItem.
        :type port: int
        """
        self._port = port

    @property
    def service(self):
        """Gets the service of this PortItem.

        服务

        :return: The service of this PortItem.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this PortItem.

        服务

        :param service: The service of this PortItem.
        :type service: str
        """
        self._service = service

    @property
    def protocol(self):
        """Gets the protocol of this PortItem.

        端口协议:   * TCP   * UDP 

        :return: The protocol of this PortItem.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PortItem.

        端口协议:   * TCP   * UDP 

        :param protocol: The protocol of this PortItem.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this PortItem.

        端口状态:   * filtered - 过滤的   * open - 开放 

        :return: The status of this PortItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PortItem.

        端口状态:   * filtered - 过滤的   * open - 开放 

        :param status: The status of this PortItem.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PortItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
