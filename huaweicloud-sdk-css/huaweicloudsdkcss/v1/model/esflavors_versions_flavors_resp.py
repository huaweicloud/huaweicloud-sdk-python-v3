# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsflavorsVersionsFlavorsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'ram': 'int',
        'name': 'str',
        'region': 'str',
        'diskrange': 'str',
        'available_az': 'str',
        'flavor_id': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'ram': 'ram',
        'name': 'name',
        'region': 'region',
        'diskrange': 'diskrange',
        'available_az': 'availableAZ',
        'flavor_id': 'flavor_id'
    }

    def __init__(self, cpu=None, ram=None, name=None, region=None, diskrange=None, available_az=None, flavor_id=None):
        """EsflavorsVersionsFlavorsResp

        The model defined in huaweicloud sdk

        :param cpu: 实例的CPU核数。
        :type cpu: int
        :param ram: 实例的内存大小。单位GB。
        :type ram: int
        :param name: 规格名称。
        :type name: str
        :param region: 可用region。
        :type region: str
        :param diskrange: 实例的硬盘容量范围。
        :type diskrange: str
        :param available_az: 可用区。
        :type available_az: str
        :param flavor_id: 规格对应的ID。
        :type flavor_id: str
        """
        
        

        self._cpu = None
        self._ram = None
        self._name = None
        self._region = None
        self._diskrange = None
        self._available_az = None
        self._flavor_id = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if diskrange is not None:
            self.diskrange = diskrange
        if available_az is not None:
            self.available_az = available_az
        if flavor_id is not None:
            self.flavor_id = flavor_id

    @property
    def cpu(self):
        """Gets the cpu of this EsflavorsVersionsFlavorsResp.

        实例的CPU核数。

        :return: The cpu of this EsflavorsVersionsFlavorsResp.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this EsflavorsVersionsFlavorsResp.

        实例的CPU核数。

        :param cpu: The cpu of this EsflavorsVersionsFlavorsResp.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def ram(self):
        """Gets the ram of this EsflavorsVersionsFlavorsResp.

        实例的内存大小。单位GB。

        :return: The ram of this EsflavorsVersionsFlavorsResp.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this EsflavorsVersionsFlavorsResp.

        实例的内存大小。单位GB。

        :param ram: The ram of this EsflavorsVersionsFlavorsResp.
        :type ram: int
        """
        self._ram = ram

    @property
    def name(self):
        """Gets the name of this EsflavorsVersionsFlavorsResp.

        规格名称。

        :return: The name of this EsflavorsVersionsFlavorsResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EsflavorsVersionsFlavorsResp.

        规格名称。

        :param name: The name of this EsflavorsVersionsFlavorsResp.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        """Gets the region of this EsflavorsVersionsFlavorsResp.

        可用region。

        :return: The region of this EsflavorsVersionsFlavorsResp.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this EsflavorsVersionsFlavorsResp.

        可用region。

        :param region: The region of this EsflavorsVersionsFlavorsResp.
        :type region: str
        """
        self._region = region

    @property
    def diskrange(self):
        """Gets the diskrange of this EsflavorsVersionsFlavorsResp.

        实例的硬盘容量范围。

        :return: The diskrange of this EsflavorsVersionsFlavorsResp.
        :rtype: str
        """
        return self._diskrange

    @diskrange.setter
    def diskrange(self, diskrange):
        """Sets the diskrange of this EsflavorsVersionsFlavorsResp.

        实例的硬盘容量范围。

        :param diskrange: The diskrange of this EsflavorsVersionsFlavorsResp.
        :type diskrange: str
        """
        self._diskrange = diskrange

    @property
    def available_az(self):
        """Gets the available_az of this EsflavorsVersionsFlavorsResp.

        可用区。

        :return: The available_az of this EsflavorsVersionsFlavorsResp.
        :rtype: str
        """
        return self._available_az

    @available_az.setter
    def available_az(self, available_az):
        """Sets the available_az of this EsflavorsVersionsFlavorsResp.

        可用区。

        :param available_az: The available_az of this EsflavorsVersionsFlavorsResp.
        :type available_az: str
        """
        self._available_az = available_az

    @property
    def flavor_id(self):
        """Gets the flavor_id of this EsflavorsVersionsFlavorsResp.

        规格对应的ID。

        :return: The flavor_id of this EsflavorsVersionsFlavorsResp.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this EsflavorsVersionsFlavorsResp.

        规格对应的ID。

        :param flavor_id: The flavor_id of this EsflavorsVersionsFlavorsResp.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

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
        if not isinstance(other, EsflavorsVersionsFlavorsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
