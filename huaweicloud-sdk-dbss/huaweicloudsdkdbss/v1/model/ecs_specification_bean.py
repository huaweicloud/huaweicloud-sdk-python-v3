# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EcsSpecificationBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'azs': 'list[str]',
        'id': 'str',
        'level': 'str',
        'name': 'str',
        'proxy': 'int',
        'ram': 'int',
        'vcpus': 'int'
    }

    attribute_map = {
        'azs': 'azs',
        'id': 'id',
        'level': 'level',
        'name': 'name',
        'proxy': 'proxy',
        'ram': 'ram',
        'vcpus': 'vcpus'
    }

    def __init__(self, azs=None, id=None, level=None, name=None, proxy=None, ram=None, vcpus=None):
        """EcsSpecificationBean

        The model defined in huaweicloud sdk

        :param azs: 可用区集合
        :type azs: list[str]
        :param id: ID
        :type id: str
        :param level: 等级
        :type level: str
        :param name: 名称
        :type name: str
        :param proxy: 代理
        :type proxy: int
        :param ram: 内存
        :type ram: int
        :param vcpus: CPU
        :type vcpus: int
        """
        
        

        self._azs = None
        self._id = None
        self._level = None
        self._name = None
        self._proxy = None
        self._ram = None
        self._vcpus = None
        self.discriminator = None

        self.azs = azs
        self.id = id
        self.level = level
        self.name = name
        self.proxy = proxy
        self.ram = ram
        self.vcpus = vcpus

    @property
    def azs(self):
        """Gets the azs of this EcsSpecificationBean.

        可用区集合

        :return: The azs of this EcsSpecificationBean.
        :rtype: list[str]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        """Sets the azs of this EcsSpecificationBean.

        可用区集合

        :param azs: The azs of this EcsSpecificationBean.
        :type azs: list[str]
        """
        self._azs = azs

    @property
    def id(self):
        """Gets the id of this EcsSpecificationBean.

        ID

        :return: The id of this EcsSpecificationBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcsSpecificationBean.

        ID

        :param id: The id of this EcsSpecificationBean.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        """Gets the level of this EcsSpecificationBean.

        等级

        :return: The level of this EcsSpecificationBean.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this EcsSpecificationBean.

        等级

        :param level: The level of this EcsSpecificationBean.
        :type level: str
        """
        self._level = level

    @property
    def name(self):
        """Gets the name of this EcsSpecificationBean.

        名称

        :return: The name of this EcsSpecificationBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcsSpecificationBean.

        名称

        :param name: The name of this EcsSpecificationBean.
        :type name: str
        """
        self._name = name

    @property
    def proxy(self):
        """Gets the proxy of this EcsSpecificationBean.

        代理

        :return: The proxy of this EcsSpecificationBean.
        :rtype: int
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this EcsSpecificationBean.

        代理

        :param proxy: The proxy of this EcsSpecificationBean.
        :type proxy: int
        """
        self._proxy = proxy

    @property
    def ram(self):
        """Gets the ram of this EcsSpecificationBean.

        内存

        :return: The ram of this EcsSpecificationBean.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this EcsSpecificationBean.

        内存

        :param ram: The ram of this EcsSpecificationBean.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        """Gets the vcpus of this EcsSpecificationBean.

        CPU

        :return: The vcpus of this EcsSpecificationBean.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this EcsSpecificationBean.

        CPU

        :param vcpus: The vcpus of this EcsSpecificationBean.
        :type vcpus: int
        """
        self._vcpus = vcpus

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
        if not isinstance(other, EcsSpecificationBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
