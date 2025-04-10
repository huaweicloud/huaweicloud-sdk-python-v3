# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferRuleBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'forward_protocol': 'str',
        'forward_port': 'int',
        'source_port': 'int',
        'source_ip': 'str'
    }

    attribute_map = {
        'forward_protocol': 'forward_protocol',
        'forward_port': 'forward_port',
        'source_port': 'source_port',
        'source_ip': 'source_ip'
    }

    def __init__(self, forward_protocol=None, forward_port=None, source_port=None, source_ip=None):
        r"""TransferRuleBody

        The model defined in huaweicloud sdk

        :param forward_protocol: 转发协议，tcp或udp
        :type forward_protocol: str
        :param forward_port: 转发端口
        :type forward_port: int
        :param source_port: 源站端口
        :type source_port: int
        :param source_ip: 源站IP，多个IP用逗号隔开，限制20个IP
        :type source_ip: str
        """
        
        

        self._forward_protocol = None
        self._forward_port = None
        self._source_port = None
        self._source_ip = None
        self.discriminator = None

        if forward_protocol is not None:
            self.forward_protocol = forward_protocol
        if forward_port is not None:
            self.forward_port = forward_port
        if source_port is not None:
            self.source_port = source_port
        if source_ip is not None:
            self.source_ip = source_ip

    @property
    def forward_protocol(self):
        r"""Gets the forward_protocol of this TransferRuleBody.

        转发协议，tcp或udp

        :return: The forward_protocol of this TransferRuleBody.
        :rtype: str
        """
        return self._forward_protocol

    @forward_protocol.setter
    def forward_protocol(self, forward_protocol):
        r"""Sets the forward_protocol of this TransferRuleBody.

        转发协议，tcp或udp

        :param forward_protocol: The forward_protocol of this TransferRuleBody.
        :type forward_protocol: str
        """
        self._forward_protocol = forward_protocol

    @property
    def forward_port(self):
        r"""Gets the forward_port of this TransferRuleBody.

        转发端口

        :return: The forward_port of this TransferRuleBody.
        :rtype: int
        """
        return self._forward_port

    @forward_port.setter
    def forward_port(self, forward_port):
        r"""Sets the forward_port of this TransferRuleBody.

        转发端口

        :param forward_port: The forward_port of this TransferRuleBody.
        :type forward_port: int
        """
        self._forward_port = forward_port

    @property
    def source_port(self):
        r"""Gets the source_port of this TransferRuleBody.

        源站端口

        :return: The source_port of this TransferRuleBody.
        :rtype: int
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this TransferRuleBody.

        源站端口

        :param source_port: The source_port of this TransferRuleBody.
        :type source_port: int
        """
        self._source_port = source_port

    @property
    def source_ip(self):
        r"""Gets the source_ip of this TransferRuleBody.

        源站IP，多个IP用逗号隔开，限制20个IP

        :return: The source_ip of this TransferRuleBody.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this TransferRuleBody.

        源站IP，多个IP用逗号隔开，限制20个IP

        :param source_ip: The source_ip of this TransferRuleBody.
        :type source_ip: str
        """
        self._source_ip = source_ip

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
        if not isinstance(other, TransferRuleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
