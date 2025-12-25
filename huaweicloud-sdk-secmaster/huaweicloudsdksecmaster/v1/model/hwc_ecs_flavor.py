# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEcsFlavor:

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
        'vcpus': 'str',
        'ram': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disk': 'disk',
        'vcpus': 'vcpus',
        'ram': 'ram'
    }

    def __init__(self, id=None, name=None, disk=None, vcpus=None, ram=None):
        r"""HwcEcsFlavor

        The model defined in huaweicloud sdk

        :param id: 云服务器规格ID。
        :type id: str
        :param name: 云服务器规格名称。
        :type name: str
        :param disk: 该云服务器规格对应要求系统盘大小，0为不限制。
        :type disk: str
        :param vcpus: 该云服务器规格对应的CPU核数。
        :type vcpus: str
        :param ram: 该云服务器规格对应的内存大小，单位为MB。
        :type ram: str
        """
        
        

        self._id = None
        self._name = None
        self._disk = None
        self._vcpus = None
        self._ram = None
        self.discriminator = None

        self.id = id
        self.name = name
        if disk is not None:
            self.disk = disk
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram

    @property
    def id(self):
        r"""Gets the id of this HwcEcsFlavor.

        云服务器规格ID。

        :return: The id of this HwcEcsFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcEcsFlavor.

        云服务器规格ID。

        :param id: The id of this HwcEcsFlavor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this HwcEcsFlavor.

        云服务器规格名称。

        :return: The name of this HwcEcsFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HwcEcsFlavor.

        云服务器规格名称。

        :param name: The name of this HwcEcsFlavor.
        :type name: str
        """
        self._name = name

    @property
    def disk(self):
        r"""Gets the disk of this HwcEcsFlavor.

        该云服务器规格对应要求系统盘大小，0为不限制。

        :return: The disk of this HwcEcsFlavor.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this HwcEcsFlavor.

        该云服务器规格对应要求系统盘大小，0为不限制。

        :param disk: The disk of this HwcEcsFlavor.
        :type disk: str
        """
        self._disk = disk

    @property
    def vcpus(self):
        r"""Gets the vcpus of this HwcEcsFlavor.

        该云服务器规格对应的CPU核数。

        :return: The vcpus of this HwcEcsFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this HwcEcsFlavor.

        该云服务器规格对应的CPU核数。

        :param vcpus: The vcpus of this HwcEcsFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this HwcEcsFlavor.

        该云服务器规格对应的内存大小，单位为MB。

        :return: The ram of this HwcEcsFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this HwcEcsFlavor.

        该云服务器规格对应的内存大小，单位为MB。

        :param ram: The ram of this HwcEcsFlavor.
        :type ram: str
        """
        self._ram = ram

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcEcsFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
