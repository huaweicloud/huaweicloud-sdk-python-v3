# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureServiceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dest_port': 'str',
        'protocol': 'int',
        'source_port': 'str'
    }

    attribute_map = {
        'dest_port': 'dest_port',
        'protocol': 'protocol',
        'source_port': 'source_port'
    }

    def __init__(self, dest_port=None, protocol=None, source_port=None):
        r"""CaptureServiceDto

        The model defined in huaweicloud sdk

        :param dest_port: 目的端口
        :type dest_port: str
        :param protocol: 协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空
        :type protocol: int
        :param source_port: 源端口
        :type source_port: str
        """
        
        

        self._dest_port = None
        self._protocol = None
        self._source_port = None
        self.discriminator = None

        if dest_port is not None:
            self.dest_port = dest_port
        self.protocol = protocol
        if source_port is not None:
            self.source_port = source_port

    @property
    def dest_port(self):
        r"""Gets the dest_port of this CaptureServiceDto.

        目的端口

        :return: The dest_port of this CaptureServiceDto.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        r"""Sets the dest_port of this CaptureServiceDto.

        目的端口

        :param dest_port: The dest_port of this CaptureServiceDto.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def protocol(self):
        r"""Gets the protocol of this CaptureServiceDto.

        协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空

        :return: The protocol of this CaptureServiceDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CaptureServiceDto.

        协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空

        :param protocol: The protocol of this CaptureServiceDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def source_port(self):
        r"""Gets the source_port of this CaptureServiceDto.

        源端口

        :return: The source_port of this CaptureServiceDto.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this CaptureServiceDto.

        源端口

        :param source_port: The source_port of this CaptureServiceDto.
        :type source_port: str
        """
        self._source_port = source_port

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
        if not isinstance(other, CaptureServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
