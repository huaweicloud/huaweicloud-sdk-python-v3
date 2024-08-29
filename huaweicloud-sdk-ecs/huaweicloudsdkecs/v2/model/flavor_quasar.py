# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorQuasar:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'vcpus': 'int',
        'ram': 'int',
        'disk': 'int',
        'root_gb': 'int',
        'ephemeral_gb': 'int',
        'extra_specs': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'disk': 'disk',
        'root_gb': 'root_gb',
        'ephemeral_gb': 'ephemeral_gb',
        'extra_specs': 'extra_specs'
    }

    def __init__(self, id=None, name=None, vcpus=None, ram=None, disk=None, root_gb=None, ephemeral_gb=None, extra_specs=None):
        """FlavorQuasar

        The model defined in huaweicloud sdk

        :param id: 云服务器类型ID。
        :type id: str
        :param name: 云服务器规格名称。
        :type name: str
        :param vcpus: 该云服务器规格对应的CPU核数。
        :type vcpus: int
        :param ram: 该云服务器规格对应的内存大小，单位为MB.
        :type ram: int
        :param disk: 该云服务器规格对应要求系统盘大小，0为不限制。
        :type disk: int
        :param root_gb: 
        :type root_gb: int
        :param ephemeral_gb: 
        :type ephemeral_gb: int
        :param extra_specs: flavor扩展字段。
        :type extra_specs: dict(str, str)
        """
        
        

        self._id = None
        self._name = None
        self._vcpus = None
        self._ram = None
        self._disk = None
        self._root_gb = None
        self._ephemeral_gb = None
        self._extra_specs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if disk is not None:
            self.disk = disk
        if root_gb is not None:
            self.root_gb = root_gb
        if ephemeral_gb is not None:
            self.ephemeral_gb = ephemeral_gb
        if extra_specs is not None:
            self.extra_specs = extra_specs

    @property
    def id(self):
        """Gets the id of this FlavorQuasar.

        云服务器类型ID。

        :return: The id of this FlavorQuasar.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlavorQuasar.

        云服务器类型ID。

        :param id: The id of this FlavorQuasar.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FlavorQuasar.

        云服务器规格名称。

        :return: The name of this FlavorQuasar.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlavorQuasar.

        云服务器规格名称。

        :param name: The name of this FlavorQuasar.
        :type name: str
        """
        self._name = name

    @property
    def vcpus(self):
        """Gets the vcpus of this FlavorQuasar.

        该云服务器规格对应的CPU核数。

        :return: The vcpus of this FlavorQuasar.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this FlavorQuasar.

        该云服务器规格对应的CPU核数。

        :param vcpus: The vcpus of this FlavorQuasar.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this FlavorQuasar.

        该云服务器规格对应的内存大小，单位为MB.

        :return: The ram of this FlavorQuasar.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this FlavorQuasar.

        该云服务器规格对应的内存大小，单位为MB.

        :param ram: The ram of this FlavorQuasar.
        :type ram: int
        """
        self._ram = ram

    @property
    def disk(self):
        """Gets the disk of this FlavorQuasar.

        该云服务器规格对应要求系统盘大小，0为不限制。

        :return: The disk of this FlavorQuasar.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this FlavorQuasar.

        该云服务器规格对应要求系统盘大小，0为不限制。

        :param disk: The disk of this FlavorQuasar.
        :type disk: int
        """
        self._disk = disk

    @property
    def root_gb(self):
        """Gets the root_gb of this FlavorQuasar.

        :return: The root_gb of this FlavorQuasar.
        :rtype: int
        """
        return self._root_gb

    @root_gb.setter
    def root_gb(self, root_gb):
        """Sets the root_gb of this FlavorQuasar.

        :param root_gb: The root_gb of this FlavorQuasar.
        :type root_gb: int
        """
        self._root_gb = root_gb

    @property
    def ephemeral_gb(self):
        """Gets the ephemeral_gb of this FlavorQuasar.

        :return: The ephemeral_gb of this FlavorQuasar.
        :rtype: int
        """
        return self._ephemeral_gb

    @ephemeral_gb.setter
    def ephemeral_gb(self, ephemeral_gb):
        """Sets the ephemeral_gb of this FlavorQuasar.

        :param ephemeral_gb: The ephemeral_gb of this FlavorQuasar.
        :type ephemeral_gb: int
        """
        self._ephemeral_gb = ephemeral_gb

    @property
    def extra_specs(self):
        """Gets the extra_specs of this FlavorQuasar.

        flavor扩展字段。

        :return: The extra_specs of this FlavorQuasar.
        :rtype: dict(str, str)
        """
        return self._extra_specs

    @extra_specs.setter
    def extra_specs(self, extra_specs):
        """Sets the extra_specs of this FlavorQuasar.

        flavor扩展字段。

        :param extra_specs: The extra_specs of this FlavorQuasar.
        :type extra_specs: dict(str, str)
        """
        self._extra_specs = extra_specs

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
        if not isinstance(other, FlavorQuasar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
