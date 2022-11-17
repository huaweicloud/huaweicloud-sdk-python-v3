# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseFlavorRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'cpu': 'int',
        'ram': 'int',
        'max_connections': 'int',
        'disk_space': 'int',
        'sold_out': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'cpu': 'cpu',
        'ram': 'ram',
        'max_connections': 'max_connections',
        'disk_space': 'disk_space',
        'sold_out': 'sold_out'
    }

    def __init__(self, code=None, name=None, cpu=None, ram=None, max_connections=None, disk_space=None, sold_out=None):
        """DatabaseFlavorRsp

        The model defined in huaweicloud sdk

        :param code: 规格编号
        :type code: str
        :param name: 规格名称
        :type name: str
        :param cpu: 核数
        :type cpu: int
        :param ram: 内存
        :type ram: int
        :param max_connections: 最大连接数
        :type max_connections: int
        :param disk_space: 存储空间
        :type disk_space: int
        :param sold_out: 是否售罄
        :type sold_out: bool
        """
        
        

        self._code = None
        self._name = None
        self._cpu = None
        self._ram = None
        self._max_connections = None
        self._disk_space = None
        self._sold_out = None
        self.discriminator = None

        self.code = code
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.max_connections = max_connections
        self.disk_space = disk_space
        self.sold_out = sold_out

    @property
    def code(self):
        """Gets the code of this DatabaseFlavorRsp.

        规格编号

        :return: The code of this DatabaseFlavorRsp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DatabaseFlavorRsp.

        规格编号

        :param code: The code of this DatabaseFlavorRsp.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this DatabaseFlavorRsp.

        规格名称

        :return: The name of this DatabaseFlavorRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseFlavorRsp.

        规格名称

        :param name: The name of this DatabaseFlavorRsp.
        :type name: str
        """
        self._name = name

    @property
    def cpu(self):
        """Gets the cpu of this DatabaseFlavorRsp.

        核数

        :return: The cpu of this DatabaseFlavorRsp.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this DatabaseFlavorRsp.

        核数

        :param cpu: The cpu of this DatabaseFlavorRsp.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this DatabaseFlavorRsp.

        内存

        :return: The ram of this DatabaseFlavorRsp.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this DatabaseFlavorRsp.

        内存

        :param ram: The ram of this DatabaseFlavorRsp.
        :type ram: int
        """
        self._ram = ram

    @property
    def max_connections(self):
        """Gets the max_connections of this DatabaseFlavorRsp.

        最大连接数

        :return: The max_connections of this DatabaseFlavorRsp.
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this DatabaseFlavorRsp.

        最大连接数

        :param max_connections: The max_connections of this DatabaseFlavorRsp.
        :type max_connections: int
        """
        self._max_connections = max_connections

    @property
    def disk_space(self):
        """Gets the disk_space of this DatabaseFlavorRsp.

        存储空间

        :return: The disk_space of this DatabaseFlavorRsp.
        :rtype: int
        """
        return self._disk_space

    @disk_space.setter
    def disk_space(self, disk_space):
        """Sets the disk_space of this DatabaseFlavorRsp.

        存储空间

        :param disk_space: The disk_space of this DatabaseFlavorRsp.
        :type disk_space: int
        """
        self._disk_space = disk_space

    @property
    def sold_out(self):
        """Gets the sold_out of this DatabaseFlavorRsp.

        是否售罄

        :return: The sold_out of this DatabaseFlavorRsp.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        """Sets the sold_out of this DatabaseFlavorRsp.

        是否售罄

        :param sold_out: The sold_out of this DatabaseFlavorRsp.
        :type sold_out: bool
        """
        self._sold_out = sold_out

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
        if not isinstance(other, DatabaseFlavorRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
