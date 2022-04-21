# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

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
        'vcpus': 'str',
        'ram': 'int',
        'disk': 'str',
        'swap': 'str',
        'os_flv_ext_dat_aephemeral': 'int',
        'os_flv_disable_ddisabled': 'bool',
        'rxtx_factor': 'float',
        'rxtx_quota': 'str',
        'rxtx_cap': 'str',
        'os_flavor_accessis_public': 'bool',
        'links': 'list[FlavorLink]',
        'os_extra_specs': 'FlavorExtraSpec',
        'attachable_quantity': 'ServerAttachableQuantity'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'disk': 'disk',
        'swap': 'swap',
        'os_flv_ext_dat_aephemeral': 'OS-FLV-EXT-DATA:ephemeral',
        'os_flv_disable_ddisabled': 'OS-FLV-DISABLED:disabled',
        'rxtx_factor': 'rxtx_factor',
        'rxtx_quota': 'rxtx_quota',
        'rxtx_cap': 'rxtx_cap',
        'os_flavor_accessis_public': 'os-flavor-access:is_public',
        'links': 'links',
        'os_extra_specs': 'os_extra_specs',
        'attachable_quantity': 'attachableQuantity'
    }

    def __init__(self, id=None, name=None, vcpus=None, ram=None, disk=None, swap=None, os_flv_ext_dat_aephemeral=None, os_flv_disable_ddisabled=None, rxtx_factor=None, rxtx_quota=None, rxtx_cap=None, os_flavor_accessis_public=None, links=None, os_extra_specs=None, attachable_quantity=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param id: 云服务器规格的ID。
        :type id: str
        :param name: 云服务器规格的名称。
        :type name: str
        :param vcpus: 云服务器规格对应的CPU核数。
        :type vcpus: str
        :param ram: 云服务器规格对应的内存大小，单位为MB。
        :type ram: int
        :param disk: 云服务器规格对应要求的系统盘大小。  当前未使用该参数，缺省值为0。
        :type disk: str
        :param swap: 云服务器规格对应要求的交换分区大小。  当前未使用该参数，缺省值为\&quot;\&quot;。
        :type swap: str
        :param os_flv_ext_dat_aephemeral: 扩展属性，临时盘大小。  当前未使用该参数，缺省值为0
        :type os_flv_ext_dat_aephemeral: int
        :param os_flv_disable_ddisabled: 扩展属性，该云服务器规格是否禁用。  当前未使用该参数，缺省值为false。
        :type os_flv_disable_ddisabled: bool
        :param rxtx_factor: 云服务器可使用网络带宽与网络硬件带宽的比例。  当前未使用该参数，缺省值为1.0。
        :type rxtx_factor: float
        :param rxtx_quota: 云服务器可使用网络带宽的软限制。  当前未使用该参数，缺省值为null。
        :type rxtx_quota: str
        :param rxtx_cap:   云服务器可使用网络带宽的硬限制。  当前未使用该参数，缺省值为null。
        :type rxtx_cap: str
        :param os_flavor_accessis_public: 扩展属性，flavor是否给所有租户使用。  - true：表示给所有租户使用。 - false：表示给指定租户使用。  缺省值为true。
        :type os_flavor_accessis_public: bool
        :param links: 规格相关快捷链接地址。
        :type links: list[:class:`huaweicloudsdkecs.v2.FlavorLink`]
        :param os_extra_specs: 
        :type os_extra_specs: :class:`huaweicloudsdkecs.v2.FlavorExtraSpec`
        :param attachable_quantity: 
        :type attachable_quantity: :class:`huaweicloudsdkecs.v2.ServerAttachableQuantity`
        """
        
        

        self._id = None
        self._name = None
        self._vcpus = None
        self._ram = None
        self._disk = None
        self._swap = None
        self._os_flv_ext_dat_aephemeral = None
        self._os_flv_disable_ddisabled = None
        self._rxtx_factor = None
        self._rxtx_quota = None
        self._rxtx_cap = None
        self._os_flavor_accessis_public = None
        self._links = None
        self._os_extra_specs = None
        self._attachable_quantity = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.vcpus = vcpus
        self.ram = ram
        self.disk = disk
        self.swap = swap
        self.os_flv_ext_dat_aephemeral = os_flv_ext_dat_aephemeral
        self.os_flv_disable_ddisabled = os_flv_disable_ddisabled
        self.rxtx_factor = rxtx_factor
        self.rxtx_quota = rxtx_quota
        self.rxtx_cap = rxtx_cap
        self.os_flavor_accessis_public = os_flavor_accessis_public
        self.links = links
        self.os_extra_specs = os_extra_specs
        if attachable_quantity is not None:
            self.attachable_quantity = attachable_quantity

    @property
    def id(self):
        """Gets the id of this Flavor.

        云服务器规格的ID。

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        云服务器规格的ID。

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Flavor.

        云服务器规格的名称。

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flavor.

        云服务器规格的名称。

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def vcpus(self):
        """Gets the vcpus of this Flavor.

        云服务器规格对应的CPU核数。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Flavor.

        云服务器规格对应的CPU核数。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this Flavor.

        云服务器规格对应的内存大小，单位为MB。

        :return: The ram of this Flavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Flavor.

        云服务器规格对应的内存大小，单位为MB。

        :param ram: The ram of this Flavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def disk(self):
        """Gets the disk of this Flavor.

        云服务器规格对应要求的系统盘大小。  当前未使用该参数，缺省值为0。

        :return: The disk of this Flavor.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this Flavor.

        云服务器规格对应要求的系统盘大小。  当前未使用该参数，缺省值为0。

        :param disk: The disk of this Flavor.
        :type disk: str
        """
        self._disk = disk

    @property
    def swap(self):
        """Gets the swap of this Flavor.

        云服务器规格对应要求的交换分区大小。  当前未使用该参数，缺省值为\"\"。

        :return: The swap of this Flavor.
        :rtype: str
        """
        return self._swap

    @swap.setter
    def swap(self, swap):
        """Sets the swap of this Flavor.

        云服务器规格对应要求的交换分区大小。  当前未使用该参数，缺省值为\"\"。

        :param swap: The swap of this Flavor.
        :type swap: str
        """
        self._swap = swap

    @property
    def os_flv_ext_dat_aephemeral(self):
        """Gets the os_flv_ext_dat_aephemeral of this Flavor.

        扩展属性，临时盘大小。  当前未使用该参数，缺省值为0

        :return: The os_flv_ext_dat_aephemeral of this Flavor.
        :rtype: int
        """
        return self._os_flv_ext_dat_aephemeral

    @os_flv_ext_dat_aephemeral.setter
    def os_flv_ext_dat_aephemeral(self, os_flv_ext_dat_aephemeral):
        """Sets the os_flv_ext_dat_aephemeral of this Flavor.

        扩展属性，临时盘大小。  当前未使用该参数，缺省值为0

        :param os_flv_ext_dat_aephemeral: The os_flv_ext_dat_aephemeral of this Flavor.
        :type os_flv_ext_dat_aephemeral: int
        """
        self._os_flv_ext_dat_aephemeral = os_flv_ext_dat_aephemeral

    @property
    def os_flv_disable_ddisabled(self):
        """Gets the os_flv_disable_ddisabled of this Flavor.

        扩展属性，该云服务器规格是否禁用。  当前未使用该参数，缺省值为false。

        :return: The os_flv_disable_ddisabled of this Flavor.
        :rtype: bool
        """
        return self._os_flv_disable_ddisabled

    @os_flv_disable_ddisabled.setter
    def os_flv_disable_ddisabled(self, os_flv_disable_ddisabled):
        """Sets the os_flv_disable_ddisabled of this Flavor.

        扩展属性，该云服务器规格是否禁用。  当前未使用该参数，缺省值为false。

        :param os_flv_disable_ddisabled: The os_flv_disable_ddisabled of this Flavor.
        :type os_flv_disable_ddisabled: bool
        """
        self._os_flv_disable_ddisabled = os_flv_disable_ddisabled

    @property
    def rxtx_factor(self):
        """Gets the rxtx_factor of this Flavor.

        云服务器可使用网络带宽与网络硬件带宽的比例。  当前未使用该参数，缺省值为1.0。

        :return: The rxtx_factor of this Flavor.
        :rtype: float
        """
        return self._rxtx_factor

    @rxtx_factor.setter
    def rxtx_factor(self, rxtx_factor):
        """Sets the rxtx_factor of this Flavor.

        云服务器可使用网络带宽与网络硬件带宽的比例。  当前未使用该参数，缺省值为1.0。

        :param rxtx_factor: The rxtx_factor of this Flavor.
        :type rxtx_factor: float
        """
        self._rxtx_factor = rxtx_factor

    @property
    def rxtx_quota(self):
        """Gets the rxtx_quota of this Flavor.

        云服务器可使用网络带宽的软限制。  当前未使用该参数，缺省值为null。

        :return: The rxtx_quota of this Flavor.
        :rtype: str
        """
        return self._rxtx_quota

    @rxtx_quota.setter
    def rxtx_quota(self, rxtx_quota):
        """Sets the rxtx_quota of this Flavor.

        云服务器可使用网络带宽的软限制。  当前未使用该参数，缺省值为null。

        :param rxtx_quota: The rxtx_quota of this Flavor.
        :type rxtx_quota: str
        """
        self._rxtx_quota = rxtx_quota

    @property
    def rxtx_cap(self):
        """Gets the rxtx_cap of this Flavor.

          云服务器可使用网络带宽的硬限制。  当前未使用该参数，缺省值为null。

        :return: The rxtx_cap of this Flavor.
        :rtype: str
        """
        return self._rxtx_cap

    @rxtx_cap.setter
    def rxtx_cap(self, rxtx_cap):
        """Sets the rxtx_cap of this Flavor.

          云服务器可使用网络带宽的硬限制。  当前未使用该参数，缺省值为null。

        :param rxtx_cap: The rxtx_cap of this Flavor.
        :type rxtx_cap: str
        """
        self._rxtx_cap = rxtx_cap

    @property
    def os_flavor_accessis_public(self):
        """Gets the os_flavor_accessis_public of this Flavor.

        扩展属性，flavor是否给所有租户使用。  - true：表示给所有租户使用。 - false：表示给指定租户使用。  缺省值为true。

        :return: The os_flavor_accessis_public of this Flavor.
        :rtype: bool
        """
        return self._os_flavor_accessis_public

    @os_flavor_accessis_public.setter
    def os_flavor_accessis_public(self, os_flavor_accessis_public):
        """Sets the os_flavor_accessis_public of this Flavor.

        扩展属性，flavor是否给所有租户使用。  - true：表示给所有租户使用。 - false：表示给指定租户使用。  缺省值为true。

        :param os_flavor_accessis_public: The os_flavor_accessis_public of this Flavor.
        :type os_flavor_accessis_public: bool
        """
        self._os_flavor_accessis_public = os_flavor_accessis_public

    @property
    def links(self):
        """Gets the links of this Flavor.

        规格相关快捷链接地址。

        :return: The links of this Flavor.
        :rtype: list[:class:`huaweicloudsdkecs.v2.FlavorLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Flavor.

        规格相关快捷链接地址。

        :param links: The links of this Flavor.
        :type links: list[:class:`huaweicloudsdkecs.v2.FlavorLink`]
        """
        self._links = links

    @property
    def os_extra_specs(self):
        """Gets the os_extra_specs of this Flavor.


        :return: The os_extra_specs of this Flavor.
        :rtype: :class:`huaweicloudsdkecs.v2.FlavorExtraSpec`
        """
        return self._os_extra_specs

    @os_extra_specs.setter
    def os_extra_specs(self, os_extra_specs):
        """Sets the os_extra_specs of this Flavor.


        :param os_extra_specs: The os_extra_specs of this Flavor.
        :type os_extra_specs: :class:`huaweicloudsdkecs.v2.FlavorExtraSpec`
        """
        self._os_extra_specs = os_extra_specs

    @property
    def attachable_quantity(self):
        """Gets the attachable_quantity of this Flavor.


        :return: The attachable_quantity of this Flavor.
        :rtype: :class:`huaweicloudsdkecs.v2.ServerAttachableQuantity`
        """
        return self._attachable_quantity

    @attachable_quantity.setter
    def attachable_quantity(self, attachable_quantity):
        """Sets the attachable_quantity of this Flavor.


        :param attachable_quantity: The attachable_quantity of this Flavor.
        :type attachable_quantity: :class:`huaweicloudsdkecs.v2.ServerAttachableQuantity`
        """
        self._attachable_quantity = attachable_quantity

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
