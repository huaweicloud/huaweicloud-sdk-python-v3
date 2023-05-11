# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerFlavor:

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
        'links': 'list[NovaLink]',
        'vcpus': 'int',
        'ram': 'int',
        'disk': 'int',
        'ephemeral': 'int',
        'swap': 'int',
        'original_name': 'str',
        'extra_specs': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'disk': 'disk',
        'ephemeral': 'ephemeral',
        'swap': 'swap',
        'original_name': 'original_name',
        'extra_specs': 'extra_specs'
    }

    def __init__(self, id=None, links=None, vcpus=None, ram=None, disk=None, ephemeral=None, swap=None, original_name=None, extra_specs=None):
        """NovaServerFlavor

        The model defined in huaweicloud sdk

        :param id: 云服务器类型ID。  微版本2.47后不支持。
        :type id: str
        :param links: 云服务器类型相关标记快捷链接信息。  微版本2.47后不支持。
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        :param vcpus: 该云服务器规格对应的CPU核数。  在微版本2.47后支持。
        :type vcpus: int
        :param ram: 该云服务器规格对应的内存大小，单位为MB。  在微版本2.47后支持。
        :type ram: int
        :param disk: 该云服务器规格对应要求系统盘大小，0为不限制。  在微版本2.47后支持。
        :type disk: int
        :param ephemeral: 未使用。  在微版本2.47后支持。
        :type ephemeral: int
        :param swap: 未使用。  在微版本2.47后支持。
        :type swap: int
        :param original_name: 云服务器规格名称。  在微版本2.47后支持。
        :type original_name: str
        :param extra_specs: flavor扩展字段。  在微版本2.47后支持。
        :type extra_specs: dict(str, str)
        """
        
        

        self._id = None
        self._links = None
        self._vcpus = None
        self._ram = None
        self._disk = None
        self._ephemeral = None
        self._swap = None
        self._original_name = None
        self._extra_specs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if disk is not None:
            self.disk = disk
        if ephemeral is not None:
            self.ephemeral = ephemeral
        if swap is not None:
            self.swap = swap
        if original_name is not None:
            self.original_name = original_name
        if extra_specs is not None:
            self.extra_specs = extra_specs

    @property
    def id(self):
        """Gets the id of this NovaServerFlavor.

        云服务器类型ID。  微版本2.47后不支持。

        :return: The id of this NovaServerFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaServerFlavor.

        云服务器类型ID。  微版本2.47后不支持。

        :param id: The id of this NovaServerFlavor.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaServerFlavor.

        云服务器类型相关标记快捷链接信息。  微版本2.47后不支持。

        :return: The links of this NovaServerFlavor.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaServerFlavor.

        云服务器类型相关标记快捷链接信息。  微版本2.47后不支持。

        :param links: The links of this NovaServerFlavor.
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        self._links = links

    @property
    def vcpus(self):
        """Gets the vcpus of this NovaServerFlavor.

        该云服务器规格对应的CPU核数。  在微版本2.47后支持。

        :return: The vcpus of this NovaServerFlavor.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this NovaServerFlavor.

        该云服务器规格对应的CPU核数。  在微版本2.47后支持。

        :param vcpus: The vcpus of this NovaServerFlavor.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this NovaServerFlavor.

        该云服务器规格对应的内存大小，单位为MB。  在微版本2.47后支持。

        :return: The ram of this NovaServerFlavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NovaServerFlavor.

        该云服务器规格对应的内存大小，单位为MB。  在微版本2.47后支持。

        :param ram: The ram of this NovaServerFlavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def disk(self):
        """Gets the disk of this NovaServerFlavor.

        该云服务器规格对应要求系统盘大小，0为不限制。  在微版本2.47后支持。

        :return: The disk of this NovaServerFlavor.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this NovaServerFlavor.

        该云服务器规格对应要求系统盘大小，0为不限制。  在微版本2.47后支持。

        :param disk: The disk of this NovaServerFlavor.
        :type disk: int
        """
        self._disk = disk

    @property
    def ephemeral(self):
        """Gets the ephemeral of this NovaServerFlavor.

        未使用。  在微版本2.47后支持。

        :return: The ephemeral of this NovaServerFlavor.
        :rtype: int
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral):
        """Sets the ephemeral of this NovaServerFlavor.

        未使用。  在微版本2.47后支持。

        :param ephemeral: The ephemeral of this NovaServerFlavor.
        :type ephemeral: int
        """
        self._ephemeral = ephemeral

    @property
    def swap(self):
        """Gets the swap of this NovaServerFlavor.

        未使用。  在微版本2.47后支持。

        :return: The swap of this NovaServerFlavor.
        :rtype: int
        """
        return self._swap

    @swap.setter
    def swap(self, swap):
        """Sets the swap of this NovaServerFlavor.

        未使用。  在微版本2.47后支持。

        :param swap: The swap of this NovaServerFlavor.
        :type swap: int
        """
        self._swap = swap

    @property
    def original_name(self):
        """Gets the original_name of this NovaServerFlavor.

        云服务器规格名称。  在微版本2.47后支持。

        :return: The original_name of this NovaServerFlavor.
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this NovaServerFlavor.

        云服务器规格名称。  在微版本2.47后支持。

        :param original_name: The original_name of this NovaServerFlavor.
        :type original_name: str
        """
        self._original_name = original_name

    @property
    def extra_specs(self):
        """Gets the extra_specs of this NovaServerFlavor.

        flavor扩展字段。  在微版本2.47后支持。

        :return: The extra_specs of this NovaServerFlavor.
        :rtype: dict(str, str)
        """
        return self._extra_specs

    @extra_specs.setter
    def extra_specs(self, extra_specs):
        """Sets the extra_specs of this NovaServerFlavor.

        flavor扩展字段。  在微版本2.47后支持。

        :param extra_specs: The extra_specs of this NovaServerFlavor.
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
        if not isinstance(other, NovaServerFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
