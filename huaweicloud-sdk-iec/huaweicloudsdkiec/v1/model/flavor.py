# coding: utf-8

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
        'disk': 'str',
        'ram': 'int',
        'vcpus': 'str',
        'os_extra_specs': 'OsExtraSpecs',
        'os_flavor_access_is_public': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disk': 'disk',
        'ram': 'ram',
        'vcpus': 'vcpus',
        'os_extra_specs': 'os_extra_specs',
        'os_flavor_access_is_public': 'os_flavor_access_is_public'
    }

    def __init__(self, id=None, name=None, disk=None, ram=None, vcpus=None, os_extra_specs=None, os_flavor_access_is_public=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param id: 边缘实例规格的ID。
        :type id: str
        :param name: 边缘实例规格的名称。
        :type name: str
        :param disk: 边缘实例规格对应要求系统盘大小。  当前未使用该参数，缺省值为0。
        :type disk: str
        :param ram: 边缘实例规格对应的内存大小，单位为MB。
        :type ram: int
        :param vcpus: 边缘实例规格对应的CPU核数。
        :type vcpus: str
        :param os_extra_specs: 
        :type os_extra_specs: :class:`huaweicloudsdkiec.v1.OsExtraSpecs`
        :param os_flavor_access_is_public: 扩展属性，flavor是否给所有租户使用。
        :type os_flavor_access_is_public: bool
        """
        
        

        self._id = None
        self._name = None
        self._disk = None
        self._ram = None
        self._vcpus = None
        self._os_extra_specs = None
        self._os_flavor_access_is_public = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disk is not None:
            self.disk = disk
        if ram is not None:
            self.ram = ram
        if vcpus is not None:
            self.vcpus = vcpus
        if os_extra_specs is not None:
            self.os_extra_specs = os_extra_specs
        if os_flavor_access_is_public is not None:
            self.os_flavor_access_is_public = os_flavor_access_is_public

    @property
    def id(self):
        """Gets the id of this Flavor.

        边缘实例规格的ID。

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        边缘实例规格的ID。

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Flavor.

        边缘实例规格的名称。

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flavor.

        边缘实例规格的名称。

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def disk(self):
        """Gets the disk of this Flavor.

        边缘实例规格对应要求系统盘大小。  当前未使用该参数，缺省值为0。

        :return: The disk of this Flavor.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this Flavor.

        边缘实例规格对应要求系统盘大小。  当前未使用该参数，缺省值为0。

        :param disk: The disk of this Flavor.
        :type disk: str
        """
        self._disk = disk

    @property
    def ram(self):
        """Gets the ram of this Flavor.

        边缘实例规格对应的内存大小，单位为MB。

        :return: The ram of this Flavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Flavor.

        边缘实例规格对应的内存大小，单位为MB。

        :param ram: The ram of this Flavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        """Gets the vcpus of this Flavor.

        边缘实例规格对应的CPU核数。

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Flavor.

        边缘实例规格对应的CPU核数。

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def os_extra_specs(self):
        """Gets the os_extra_specs of this Flavor.

        :return: The os_extra_specs of this Flavor.
        :rtype: :class:`huaweicloudsdkiec.v1.OsExtraSpecs`
        """
        return self._os_extra_specs

    @os_extra_specs.setter
    def os_extra_specs(self, os_extra_specs):
        """Sets the os_extra_specs of this Flavor.

        :param os_extra_specs: The os_extra_specs of this Flavor.
        :type os_extra_specs: :class:`huaweicloudsdkiec.v1.OsExtraSpecs`
        """
        self._os_extra_specs = os_extra_specs

    @property
    def os_flavor_access_is_public(self):
        """Gets the os_flavor_access_is_public of this Flavor.

        扩展属性，flavor是否给所有租户使用。

        :return: The os_flavor_access_is_public of this Flavor.
        :rtype: bool
        """
        return self._os_flavor_access_is_public

    @os_flavor_access_is_public.setter
    def os_flavor_access_is_public(self, os_flavor_access_is_public):
        """Sets the os_flavor_access_is_public of this Flavor.

        扩展属性，flavor是否给所有租户使用。

        :param os_flavor_access_is_public: The os_flavor_access_is_public of this Flavor.
        :type os_flavor_access_is_public: bool
        """
        self._os_flavor_access_is_public = os_flavor_access_is_public

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
