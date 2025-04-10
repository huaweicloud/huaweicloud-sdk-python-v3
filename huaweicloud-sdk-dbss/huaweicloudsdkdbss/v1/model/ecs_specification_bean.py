# coding: utf-8

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
        'vcpus': 'int',
        'az_type': 'str'
    }

    attribute_map = {
        'azs': 'azs',
        'id': 'id',
        'level': 'level',
        'name': 'name',
        'proxy': 'proxy',
        'ram': 'ram',
        'vcpus': 'vcpus',
        'az_type': 'az_type'
    }

    def __init__(self, azs=None, id=None, level=None, name=None, proxy=None, ram=None, vcpus=None, az_type=None):
        r"""EcsSpecificationBean

        The model defined in huaweicloud sdk

        :param azs: ECS规格所在的可用区集合
        :type azs: list[str]
        :param id: 规格ID
        :type id: str
        :param level: 规格等级，支持的等级以局点配置为准。 - entry:入门版 - low:基础版 - medium:专业版 - high:高级版
        :type level: str
        :param name: 规格名称
        :type name: str
        :param proxy: 规格可添加的数据库数量
        :type proxy: int
        :param ram: 内存
        :type ram: int
        :param vcpus: CPU
        :type vcpus: int
        :param az_type: 可用区类型 - DEDICATED - DEC - EDGE
        :type az_type: str
        """
        
        

        self._azs = None
        self._id = None
        self._level = None
        self._name = None
        self._proxy = None
        self._ram = None
        self._vcpus = None
        self._az_type = None
        self.discriminator = None

        self.azs = azs
        self.id = id
        self.level = level
        self.name = name
        self.proxy = proxy
        self.ram = ram
        self.vcpus = vcpus
        if az_type is not None:
            self.az_type = az_type

    @property
    def azs(self):
        r"""Gets the azs of this EcsSpecificationBean.

        ECS规格所在的可用区集合

        :return: The azs of this EcsSpecificationBean.
        :rtype: list[str]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this EcsSpecificationBean.

        ECS规格所在的可用区集合

        :param azs: The azs of this EcsSpecificationBean.
        :type azs: list[str]
        """
        self._azs = azs

    @property
    def id(self):
        r"""Gets the id of this EcsSpecificationBean.

        规格ID

        :return: The id of this EcsSpecificationBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EcsSpecificationBean.

        规格ID

        :param id: The id of this EcsSpecificationBean.
        :type id: str
        """
        self._id = id

    @property
    def level(self):
        r"""Gets the level of this EcsSpecificationBean.

        规格等级，支持的等级以局点配置为准。 - entry:入门版 - low:基础版 - medium:专业版 - high:高级版

        :return: The level of this EcsSpecificationBean.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this EcsSpecificationBean.

        规格等级，支持的等级以局点配置为准。 - entry:入门版 - low:基础版 - medium:专业版 - high:高级版

        :param level: The level of this EcsSpecificationBean.
        :type level: str
        """
        self._level = level

    @property
    def name(self):
        r"""Gets the name of this EcsSpecificationBean.

        规格名称

        :return: The name of this EcsSpecificationBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EcsSpecificationBean.

        规格名称

        :param name: The name of this EcsSpecificationBean.
        :type name: str
        """
        self._name = name

    @property
    def proxy(self):
        r"""Gets the proxy of this EcsSpecificationBean.

        规格可添加的数据库数量

        :return: The proxy of this EcsSpecificationBean.
        :rtype: int
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this EcsSpecificationBean.

        规格可添加的数据库数量

        :param proxy: The proxy of this EcsSpecificationBean.
        :type proxy: int
        """
        self._proxy = proxy

    @property
    def ram(self):
        r"""Gets the ram of this EcsSpecificationBean.

        内存

        :return: The ram of this EcsSpecificationBean.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this EcsSpecificationBean.

        内存

        :param ram: The ram of this EcsSpecificationBean.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        r"""Gets the vcpus of this EcsSpecificationBean.

        CPU

        :return: The vcpus of this EcsSpecificationBean.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this EcsSpecificationBean.

        CPU

        :param vcpus: The vcpus of this EcsSpecificationBean.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def az_type(self):
        r"""Gets the az_type of this EcsSpecificationBean.

        可用区类型 - DEDICATED - DEC - EDGE

        :return: The az_type of this EcsSpecificationBean.
        :rtype: str
        """
        return self._az_type

    @az_type.setter
    def az_type(self, az_type):
        r"""Sets the az_type of this EcsSpecificationBean.

        可用区类型 - DEDICATED - DEC - EDGE

        :param az_type: The az_type of this EcsSpecificationBean.
        :type az_type: str
        """
        self._az_type = az_type

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
