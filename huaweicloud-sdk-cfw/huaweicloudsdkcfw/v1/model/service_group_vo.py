# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceGroupVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'protocols': 'list[int]',
        'service_set_type': 'int',
        'set_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'protocols': 'protocols',
        'service_set_type': 'service_set_type',
        'set_id': 'set_id'
    }

    def __init__(self, name=None, protocols=None, service_set_type=None, set_id=None):
        """ServiceGroupVO

        The model defined in huaweicloud sdk

        :param name: 服务组名称
        :type name: str
        :param protocols: 协议列表
        :type protocols: list[int]
        :param service_set_type: 服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库
        :type service_set_type: int
        :param set_id: 服务组ID
        :type set_id: str
        """
        
        

        self._name = None
        self._protocols = None
        self._service_set_type = None
        self._set_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if protocols is not None:
            self.protocols = protocols
        if service_set_type is not None:
            self.service_set_type = service_set_type
        if set_id is not None:
            self.set_id = set_id

    @property
    def name(self):
        """Gets the name of this ServiceGroupVO.

        服务组名称

        :return: The name of this ServiceGroupVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceGroupVO.

        服务组名称

        :param name: The name of this ServiceGroupVO.
        :type name: str
        """
        self._name = name

    @property
    def protocols(self):
        """Gets the protocols of this ServiceGroupVO.

        协议列表

        :return: The protocols of this ServiceGroupVO.
        :rtype: list[int]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this ServiceGroupVO.

        协议列表

        :param protocols: The protocols of this ServiceGroupVO.
        :type protocols: list[int]
        """
        self._protocols = protocols

    @property
    def service_set_type(self):
        """Gets the service_set_type of this ServiceGroupVO.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :return: The service_set_type of this ServiceGroupVO.
        :rtype: int
        """
        return self._service_set_type

    @service_set_type.setter
    def service_set_type(self, service_set_type):
        """Sets the service_set_type of this ServiceGroupVO.

        服务组类型，0表示自定义服务组，1表示常用WEB服务，2表示常用远程登录和PING，3表示常用数据库

        :param service_set_type: The service_set_type of this ServiceGroupVO.
        :type service_set_type: int
        """
        self._service_set_type = service_set_type

    @property
    def set_id(self):
        """Gets the set_id of this ServiceGroupVO.

        服务组ID

        :return: The set_id of this ServiceGroupVO.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this ServiceGroupVO.

        服务组ID

        :param set_id: The set_id of this ServiceGroupVO.
        :type set_id: str
        """
        self._set_id = set_id

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
        if not isinstance(other, ServiceGroupVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
