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
        'protocols': 'list[int]',
        'source_port': 'str',
        'dest_port': 'str',
        'service_set_id': 'str',
        'service_set_name': 'str',
        'custom_service': 'list[ServiceItem]',
        'predefined_group': 'list[str]',
        'service_group': 'list[str]',
        'service_group_names': 'list[ServiceGroupVO]',
        'service_set_type': 'int'
    }

    attribute_map = {
        'type': 'type',
        'protocol': 'protocol',
        'protocols': 'protocols',
        'source_port': 'source_port',
        'dest_port': 'dest_port',
        'service_set_id': 'service_set_id',
        'service_set_name': 'service_set_name',
        'custom_service': 'custom_service',
        'predefined_group': 'predefined_group',
        'service_group': 'service_group',
        'service_group_names': 'service_group_names',
        'service_set_type': 'service_set_type'
    }

    def __init__(self, type=None, protocol=None, protocols=None, source_port=None, dest_port=None, service_set_id=None, service_set_name=None, custom_service=None, predefined_group=None, service_group=None, service_group_names=None, service_set_type=None):
        """RuleServiceDto

        The model defined in huaweicloud sdk

        :param type: 服务输入类型，0为手动输入类型，1为自动输入类型
        :type type: int
        :param protocol: 协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: int
        :param protocols: 协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocols: list[int]
        :param source_port: 源端口
        :type source_port: str
        :param dest_port: 目的端口
        :type dest_port: str
        :param service_set_id: 服务组id，手动类型为空，自动类型为非空
        :type service_set_id: str
        :param service_set_name: 服务组名称
        :type service_set_name: str
        :param custom_service: 自定义服务
        :type custom_service: list[:class:`huaweicloudsdkcfw.v1.ServiceItem`]
        :param predefined_group: 预定义服务组列表
        :type predefined_group: list[str]
        :param service_group: 服务组列表
        :type service_group: list[str]
        :param service_group_names: 服务组名称列表
        :type service_group_names: list[:class:`huaweicloudsdkcfw.v1.ServiceGroupVO`]
        :param service_set_type: 服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库
        :type service_set_type: int
        """
        
        

        self._type = None
        self._protocol = None
        self._protocols = None
        self._source_port = None
        self._dest_port = None
        self._service_set_id = None
        self._service_set_name = None
        self._custom_service = None
        self._predefined_group = None
        self._service_group = None
        self._service_group_names = None
        self._service_set_type = None
        self.discriminator = None

        self.type = type
        if protocol is not None:
            self.protocol = protocol
        if protocols is not None:
            self.protocols = protocols
        if source_port is not None:
            self.source_port = source_port
        if dest_port is not None:
            self.dest_port = dest_port
        if service_set_id is not None:
            self.service_set_id = service_set_id
        if service_set_name is not None:
            self.service_set_name = service_set_name
        if custom_service is not None:
            self.custom_service = custom_service
        if predefined_group is not None:
            self.predefined_group = predefined_group
        if service_group is not None:
            self.service_group = service_group
        if service_group_names is not None:
            self.service_group_names = service_group_names
        if service_set_type is not None:
            self.service_set_type = service_set_type

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
    def protocols(self):
        """Gets the protocols of this RuleServiceDto.

        协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocols of this RuleServiceDto.
        :rtype: list[int]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this RuleServiceDto.

        协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocols: The protocols of this RuleServiceDto.
        :type protocols: list[int]
        """
        self._protocols = protocols

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

    @property
    def custom_service(self):
        """Gets the custom_service of this RuleServiceDto.

        自定义服务

        :return: The custom_service of this RuleServiceDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ServiceItem`]
        """
        return self._custom_service

    @custom_service.setter
    def custom_service(self, custom_service):
        """Sets the custom_service of this RuleServiceDto.

        自定义服务

        :param custom_service: The custom_service of this RuleServiceDto.
        :type custom_service: list[:class:`huaweicloudsdkcfw.v1.ServiceItem`]
        """
        self._custom_service = custom_service

    @property
    def predefined_group(self):
        """Gets the predefined_group of this RuleServiceDto.

        预定义服务组列表

        :return: The predefined_group of this RuleServiceDto.
        :rtype: list[str]
        """
        return self._predefined_group

    @predefined_group.setter
    def predefined_group(self, predefined_group):
        """Sets the predefined_group of this RuleServiceDto.

        预定义服务组列表

        :param predefined_group: The predefined_group of this RuleServiceDto.
        :type predefined_group: list[str]
        """
        self._predefined_group = predefined_group

    @property
    def service_group(self):
        """Gets the service_group of this RuleServiceDto.

        服务组列表

        :return: The service_group of this RuleServiceDto.
        :rtype: list[str]
        """
        return self._service_group

    @service_group.setter
    def service_group(self, service_group):
        """Sets the service_group of this RuleServiceDto.

        服务组列表

        :param service_group: The service_group of this RuleServiceDto.
        :type service_group: list[str]
        """
        self._service_group = service_group

    @property
    def service_group_names(self):
        """Gets the service_group_names of this RuleServiceDto.

        服务组名称列表

        :return: The service_group_names of this RuleServiceDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ServiceGroupVO`]
        """
        return self._service_group_names

    @service_group_names.setter
    def service_group_names(self, service_group_names):
        """Sets the service_group_names of this RuleServiceDto.

        服务组名称列表

        :param service_group_names: The service_group_names of this RuleServiceDto.
        :type service_group_names: list[:class:`huaweicloudsdkcfw.v1.ServiceGroupVO`]
        """
        self._service_group_names = service_group_names

    @property
    def service_set_type(self):
        """Gets the service_set_type of this RuleServiceDto.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :return: The service_set_type of this RuleServiceDto.
        :rtype: int
        """
        return self._service_set_type

    @service_set_type.setter
    def service_set_type(self, service_set_type):
        """Sets the service_set_type of this RuleServiceDto.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :param service_set_type: The service_set_type of this RuleServiceDto.
        :type service_set_type: int
        """
        self._service_set_type = service_set_type

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
