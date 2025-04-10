# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'int',
        'source_port': 'str',
        'dest_port': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'source_port': 'source_port',
        'dest_port': 'dest_port',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, protocol=None, source_port=None, dest_port=None, description=None, name=None):
        r"""ServiceItem

        The model defined in huaweicloud sdk

        :param protocol: 协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,RuleServiceDto.type为0时不能为空。
        :type protocol: int
        :param source_port: 源端口
        :type source_port: str
        :param dest_port: 目的端口
        :type dest_port: str
        :param description: 服务成员描述
        :type description: str
        :param name: 服务成员名称
        :type name: str
        """
        
        

        self._protocol = None
        self._source_port = None
        self._dest_port = None
        self._description = None
        self._name = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if source_port is not None:
            self.source_port = source_port
        if dest_port is not None:
            self.dest_port = dest_port
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this ServiceItem.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,RuleServiceDto.type为0时不能为空。

        :return: The protocol of this ServiceItem.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ServiceItem.

        协议类型：TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1,RuleServiceDto.type为0时不能为空。

        :param protocol: The protocol of this ServiceItem.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def source_port(self):
        r"""Gets the source_port of this ServiceItem.

        源端口

        :return: The source_port of this ServiceItem.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this ServiceItem.

        源端口

        :param source_port: The source_port of this ServiceItem.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def dest_port(self):
        r"""Gets the dest_port of this ServiceItem.

        目的端口

        :return: The dest_port of this ServiceItem.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        r"""Sets the dest_port of this ServiceItem.

        目的端口

        :param dest_port: The dest_port of this ServiceItem.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def description(self):
        r"""Gets the description of this ServiceItem.

        服务成员描述

        :return: The description of this ServiceItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceItem.

        服务成员描述

        :param description: The description of this ServiceItem.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this ServiceItem.

        服务成员名称

        :return: The name of this ServiceItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceItem.

        服务成员名称

        :param name: The name of this ServiceItem.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ServiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
