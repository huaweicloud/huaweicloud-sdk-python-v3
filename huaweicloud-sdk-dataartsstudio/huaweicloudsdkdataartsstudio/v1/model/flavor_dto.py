# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorDTO:

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
        'cpu': 'int',
        'mem': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disk': 'disk',
        'cpu': 'cpu',
        'mem': 'mem'
    }

    def __init__(self, id=None, name=None, disk=None, cpu=None, mem=None):
        r"""FlavorDTO

        The model defined in huaweicloud sdk

        :param id: 规格ID。
        :type id: str
        :param name: 规格名称。
        :type name: str
        :param disk: 磁盘大小。
        :type disk: int
        :param cpu: CPU大小。
        :type cpu: int
        :param mem: 内存大小。
        :type mem: int
        """
        
        

        self._id = None
        self._name = None
        self._disk = None
        self._cpu = None
        self._mem = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disk is not None:
            self.disk = disk
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem

    @property
    def id(self):
        r"""Gets the id of this FlavorDTO.

        规格ID。

        :return: The id of this FlavorDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FlavorDTO.

        规格ID。

        :param id: The id of this FlavorDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this FlavorDTO.

        规格名称。

        :return: The name of this FlavorDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlavorDTO.

        规格名称。

        :param name: The name of this FlavorDTO.
        :type name: str
        """
        self._name = name

    @property
    def disk(self):
        r"""Gets the disk of this FlavorDTO.

        磁盘大小。

        :return: The disk of this FlavorDTO.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this FlavorDTO.

        磁盘大小。

        :param disk: The disk of this FlavorDTO.
        :type disk: int
        """
        self._disk = disk

    @property
    def cpu(self):
        r"""Gets the cpu of this FlavorDTO.

        CPU大小。

        :return: The cpu of this FlavorDTO.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this FlavorDTO.

        CPU大小。

        :param cpu: The cpu of this FlavorDTO.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this FlavorDTO.

        内存大小。

        :return: The mem of this FlavorDTO.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this FlavorDTO.

        内存大小。

        :param mem: The mem of this FlavorDTO.
        :type mem: int
        """
        self._mem = mem

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
        if not isinstance(other, FlavorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
