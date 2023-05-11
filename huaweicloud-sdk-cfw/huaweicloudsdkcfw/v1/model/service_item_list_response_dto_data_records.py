# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceItemListResponseDtoDataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'protocol': 'int',
        'source_port': 'str',
        'dest_port': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'protocol': 'protocol',
        'source_port': 'source_port',
        'dest_port': 'dest_port',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, item_id=None, protocol=None, source_port=None, dest_port=None, name=None, description=None):
        """ServiceItemListResponseDtoDataRecords

        The model defined in huaweicloud sdk

        :param item_id: 服务成员id
        :type item_id: str
        :param protocol: 协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: int
        :param source_port: 源端口
        :type source_port: str
        :param dest_port: 目的端口
        :type dest_port: str
        :param name: 服务成员名称
        :type name: str
        :param description: 服务成员描述
        :type description: str
        """
        
        

        self._item_id = None
        self._protocol = None
        self._source_port = None
        self._dest_port = None
        self._name = None
        self._description = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if protocol is not None:
            self.protocol = protocol
        if source_port is not None:
            self.source_port = source_port
        if dest_port is not None:
            self.dest_port = dest_port
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def item_id(self):
        """Gets the item_id of this ServiceItemListResponseDtoDataRecords.

        服务成员id

        :return: The item_id of this ServiceItemListResponseDtoDataRecords.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ServiceItemListResponseDtoDataRecords.

        服务成员id

        :param item_id: The item_id of this ServiceItemListResponseDtoDataRecords.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def protocol(self):
        """Gets the protocol of this ServiceItemListResponseDtoDataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this ServiceItemListResponseDtoDataRecords.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ServiceItemListResponseDtoDataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this ServiceItemListResponseDtoDataRecords.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def source_port(self):
        """Gets the source_port of this ServiceItemListResponseDtoDataRecords.

        源端口

        :return: The source_port of this ServiceItemListResponseDtoDataRecords.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this ServiceItemListResponseDtoDataRecords.

        源端口

        :param source_port: The source_port of this ServiceItemListResponseDtoDataRecords.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def dest_port(self):
        """Gets the dest_port of this ServiceItemListResponseDtoDataRecords.

        目的端口

        :return: The dest_port of this ServiceItemListResponseDtoDataRecords.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this ServiceItemListResponseDtoDataRecords.

        目的端口

        :param dest_port: The dest_port of this ServiceItemListResponseDtoDataRecords.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def name(self):
        """Gets the name of this ServiceItemListResponseDtoDataRecords.

        服务成员名称

        :return: The name of this ServiceItemListResponseDtoDataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceItemListResponseDtoDataRecords.

        服务成员名称

        :param name: The name of this ServiceItemListResponseDtoDataRecords.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ServiceItemListResponseDtoDataRecords.

        服务成员描述

        :return: The description of this ServiceItemListResponseDtoDataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceItemListResponseDtoDataRecords.

        服务成员描述

        :param description: The description of this ServiceItemListResponseDtoDataRecords.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ServiceItemListResponseDtoDataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
