# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorDetailInfos:

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
        'disk': 'int',
        'vcpus': 'int',
        'ram': 'int',
        'gpus': 'list[GpuInfo]',
        'asic_accelerators': 'list[ASICAcceleratorInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disk': 'disk',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'gpus': 'gpus',
        'asic_accelerators': 'asic_accelerators'
    }

    def __init__(self, id=None, name=None, disk=None, vcpus=None, ram=None, gpus=None, asic_accelerators=None):
        r"""FlavorDetailInfos

        The model defined in huaweicloud sdk

        :param id: 裸金属服务器规格ID
        :type id: str
        :param name: 裸金属服务器规格名称
        :type name: str
        :param disk: 该裸金属服务器规格对应要求系统盘大小，0为不限制。
        :type disk: int
        :param vcpus: 该裸金属服务器规格对应的CPU核数
        :type vcpus: int
        :param ram: 该裸金属服务器规格对应的内存大小，单位为MB
        :type ram: int
        :param gpus: 该裸金属服务器规格对应的GPU设备。
        :type gpus: list[:class:`huaweicloudsdkbms.v1.GpuInfo`]
        :param asic_accelerators: 该裸金属服务器规格对应的ASIC设备。
        :type asic_accelerators: list[:class:`huaweicloudsdkbms.v1.ASICAcceleratorInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._disk = None
        self._vcpus = None
        self._ram = None
        self._gpus = None
        self._asic_accelerators = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disk is not None:
            self.disk = disk
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if gpus is not None:
            self.gpus = gpus
        if asic_accelerators is not None:
            self.asic_accelerators = asic_accelerators

    @property
    def id(self):
        r"""Gets the id of this FlavorDetailInfos.

        裸金属服务器规格ID

        :return: The id of this FlavorDetailInfos.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FlavorDetailInfos.

        裸金属服务器规格ID

        :param id: The id of this FlavorDetailInfos.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this FlavorDetailInfos.

        裸金属服务器规格名称

        :return: The name of this FlavorDetailInfos.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlavorDetailInfos.

        裸金属服务器规格名称

        :param name: The name of this FlavorDetailInfos.
        :type name: str
        """
        self._name = name

    @property
    def disk(self):
        r"""Gets the disk of this FlavorDetailInfos.

        该裸金属服务器规格对应要求系统盘大小，0为不限制。

        :return: The disk of this FlavorDetailInfos.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this FlavorDetailInfos.

        该裸金属服务器规格对应要求系统盘大小，0为不限制。

        :param disk: The disk of this FlavorDetailInfos.
        :type disk: int
        """
        self._disk = disk

    @property
    def vcpus(self):
        r"""Gets the vcpus of this FlavorDetailInfos.

        该裸金属服务器规格对应的CPU核数

        :return: The vcpus of this FlavorDetailInfos.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this FlavorDetailInfos.

        该裸金属服务器规格对应的CPU核数

        :param vcpus: The vcpus of this FlavorDetailInfos.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this FlavorDetailInfos.

        该裸金属服务器规格对应的内存大小，单位为MB

        :return: The ram of this FlavorDetailInfos.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this FlavorDetailInfos.

        该裸金属服务器规格对应的内存大小，单位为MB

        :param ram: The ram of this FlavorDetailInfos.
        :type ram: int
        """
        self._ram = ram

    @property
    def gpus(self):
        r"""Gets the gpus of this FlavorDetailInfos.

        该裸金属服务器规格对应的GPU设备。

        :return: The gpus of this FlavorDetailInfos.
        :rtype: list[:class:`huaweicloudsdkbms.v1.GpuInfo`]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        r"""Sets the gpus of this FlavorDetailInfos.

        该裸金属服务器规格对应的GPU设备。

        :param gpus: The gpus of this FlavorDetailInfos.
        :type gpus: list[:class:`huaweicloudsdkbms.v1.GpuInfo`]
        """
        self._gpus = gpus

    @property
    def asic_accelerators(self):
        r"""Gets the asic_accelerators of this FlavorDetailInfos.

        该裸金属服务器规格对应的ASIC设备。

        :return: The asic_accelerators of this FlavorDetailInfos.
        :rtype: list[:class:`huaweicloudsdkbms.v1.ASICAcceleratorInfo`]
        """
        return self._asic_accelerators

    @asic_accelerators.setter
    def asic_accelerators(self, asic_accelerators):
        r"""Sets the asic_accelerators of this FlavorDetailInfos.

        该裸金属服务器规格对应的ASIC设备。

        :param asic_accelerators: The asic_accelerators of this FlavorDetailInfos.
        :type asic_accelerators: list[:class:`huaweicloudsdkbms.v1.ASICAcceleratorInfo`]
        """
        self._asic_accelerators = asic_accelerators

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
        if not isinstance(other, FlavorDetailInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
