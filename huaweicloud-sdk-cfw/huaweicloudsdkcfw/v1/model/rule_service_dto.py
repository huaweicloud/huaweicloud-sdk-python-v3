# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleServiceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'protocol': 'int',
        'source_port': 'str',
        'dest_port': 'str',
        'service_set_id': 'str',
        'service_set_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'protocol': 'protocol',
        'source_port': 'source_port',
        'dest_port': 'dest_port',
        'service_set_id': 'service_set_id',
        'service_set_name': 'service_set_name'
    }

    def __init__(self, type=None, protocol=None, source_port=None, dest_port=None, service_set_id=None, service_set_name=None):
        """RuleServiceDto

        The model defined in huaweicloud sdk

        :param type: 服务输入类型，0为手动输入类型，1为自动输入类型
        :type type: int
        :param protocol: 协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: int
        :param source_port: 源端口
        :type source_port: str
        :param dest_port: 目的端口
        :type dest_port: str
        :param service_set_id: 服务组id，手动类型为空，自动类型为非空
        :type service_set_id: str
        :param service_set_name: 服务组名称
        :type service_set_name: str
        """
        
        

        self._type = None
        self._protocol = None
        self._source_port = None
        self._dest_port = None
        self._service_set_id = None
        self._service_set_name = None
        self.discriminator = None

        self.type = type
        if protocol is not None:
            self.protocol = protocol
        if source_port is not None:
            self.source_port = source_port
        if dest_port is not None:
            self.dest_port = dest_port
        if service_set_id is not None:
            self.service_set_id = service_set_id
        if service_set_name is not None:
            self.service_set_name = service_set_name

    @property
    def type(self):
        """Gets the type of this RuleServiceDto.

        服务输入类型，0为手动输入类型，1为自动输入类型

        :return: The type of this RuleServiceDto.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleServiceDto.

        服务输入类型，0为手动输入类型，1为自动输入类型

        :param type: The type of this RuleServiceDto.
        :type type: int
        """
        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this RuleServiceDto.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this RuleServiceDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this RuleServiceDto.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this RuleServiceDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def source_port(self):
        """Gets the source_port of this RuleServiceDto.

        源端口

        :return: The source_port of this RuleServiceDto.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this RuleServiceDto.

        源端口

        :param source_port: The source_port of this RuleServiceDto.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def dest_port(self):
        """Gets the dest_port of this RuleServiceDto.

        目的端口

        :return: The dest_port of this RuleServiceDto.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this RuleServiceDto.

        目的端口

        :param dest_port: The dest_port of this RuleServiceDto.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def service_set_id(self):
        """Gets the service_set_id of this RuleServiceDto.

        服务组id，手动类型为空，自动类型为非空

        :return: The service_set_id of this RuleServiceDto.
        :rtype: str
        """
        return self._service_set_id

    @service_set_id.setter
    def service_set_id(self, service_set_id):
        """Sets the service_set_id of this RuleServiceDto.

        服务组id，手动类型为空，自动类型为非空

        :param service_set_id: The service_set_id of this RuleServiceDto.
        :type service_set_id: str
        """
        self._service_set_id = service_set_id

    @property
    def service_set_name(self):
        """Gets the service_set_name of this RuleServiceDto.

        服务组名称

        :return: The service_set_name of this RuleServiceDto.
        :rtype: str
        """
        return self._service_set_name

    @service_set_name.setter
    def service_set_name(self, service_set_name):
        """Sets the service_set_name of this RuleServiceDto.

        服务组名称

        :param service_set_name: The service_set_name of this RuleServiceDto.
        :type service_set_name: str
        """
        self._service_set_name = service_set_name

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
        if not isinstance(other, RuleServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
