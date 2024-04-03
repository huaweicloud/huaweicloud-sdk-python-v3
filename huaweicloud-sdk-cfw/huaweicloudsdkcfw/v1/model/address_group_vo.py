# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroupVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'name': 'str',
        'protocols': 'list[int]',
        'service_set_type': 'int'
    }

    attribute_map = {
        'set_id': 'set_id',
        'name': 'name',
        'protocols': 'protocols',
        'service_set_type': 'service_set_type'
    }

    def __init__(self, set_id=None, name=None, protocols=None, service_set_type=None):
        """AddressGroupVO

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param name: 地址组名称
        :type name: str
        :param protocols: 协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocols: list[int]
        :param service_set_type: 服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库
        :type service_set_type: int
        """
        
        

        self._set_id = None
        self._name = None
        self._protocols = None
        self._service_set_type = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if name is not None:
            self.name = name
        if protocols is not None:
            self.protocols = protocols
        if service_set_type is not None:
            self.service_set_type = service_set_type

    @property
    def set_id(self):
        """Gets the set_id of this AddressGroupVO.

        地址组id

        :return: The set_id of this AddressGroupVO.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this AddressGroupVO.

        地址组id

        :param set_id: The set_id of this AddressGroupVO.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def name(self):
        """Gets the name of this AddressGroupVO.

        地址组名称

        :return: The name of this AddressGroupVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressGroupVO.

        地址组名称

        :param name: The name of this AddressGroupVO.
        :type name: str
        """
        self._name = name

    @property
    def protocols(self):
        """Gets the protocols of this AddressGroupVO.

        协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocols of this AddressGroupVO.
        :rtype: list[int]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this AddressGroupVO.

        协议列表，协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocols: The protocols of this AddressGroupVO.
        :type protocols: list[int]
        """
        self._protocols = protocols

    @property
    def service_set_type(self):
        """Gets the service_set_type of this AddressGroupVO.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :return: The service_set_type of this AddressGroupVO.
        :rtype: int
        """
        return self._service_set_type

    @service_set_type.setter
    def service_set_type(self, service_set_type):
        """Sets the service_set_type of this AddressGroupVO.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :param service_set_type: The service_set_type of this AddressGroupVO.
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
        if not isinstance(other, AddressGroupVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
