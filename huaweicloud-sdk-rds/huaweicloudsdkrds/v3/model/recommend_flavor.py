# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecommendFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'flavor_ref': 'str',
        'cpu': 'str',
        'mem': 'str',
        'group_type': 'str',
        'volume_flavors': 'list[VolumeFlavor]'
    }

    attribute_map = {
        'type': 'type',
        'flavor_ref': 'flavor_ref',
        'cpu': 'cpu',
        'mem': 'mem',
        'group_type': 'group_type',
        'volume_flavors': 'volume_flavors'
    }

    def __init__(self, type=None, flavor_ref=None, cpu=None, mem=None, group_type=None, volume_flavors=None):
        """RecommendFlavor

        The model defined in huaweicloud sdk

        :param type: 按照实例类型查询
        :type type: str
        :param flavor_ref: 规格码
        :type flavor_ref: str
        :param cpu: CPU大小
        :type cpu: str
        :param mem: 内存大小（单位：GB）
        :type mem: str
        :param group_type: 规格类型
        :type group_type: str
        :param volume_flavors: 磁盘规格信息
        :type volume_flavors: list[:class:`huaweicloudsdkrds.v3.VolumeFlavor`]
        """
        
        

        self._type = None
        self._flavor_ref = None
        self._cpu = None
        self._mem = None
        self._group_type = None
        self._volume_flavors = None
        self.discriminator = None

        self.type = type
        self.flavor_ref = flavor_ref
        self.cpu = cpu
        self.mem = mem
        self.group_type = group_type
        self.volume_flavors = volume_flavors

    @property
    def type(self):
        """Gets the type of this RecommendFlavor.

        按照实例类型查询

        :return: The type of this RecommendFlavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecommendFlavor.

        按照实例类型查询

        :param type: The type of this RecommendFlavor.
        :type type: str
        """
        self._type = type

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this RecommendFlavor.

        规格码

        :return: The flavor_ref of this RecommendFlavor.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this RecommendFlavor.

        规格码

        :param flavor_ref: The flavor_ref of this RecommendFlavor.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def cpu(self):
        """Gets the cpu of this RecommendFlavor.

        CPU大小

        :return: The cpu of this RecommendFlavor.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this RecommendFlavor.

        CPU大小

        :param cpu: The cpu of this RecommendFlavor.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this RecommendFlavor.

        内存大小（单位：GB）

        :return: The mem of this RecommendFlavor.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this RecommendFlavor.

        内存大小（单位：GB）

        :param mem: The mem of this RecommendFlavor.
        :type mem: str
        """
        self._mem = mem

    @property
    def group_type(self):
        """Gets the group_type of this RecommendFlavor.

        规格类型

        :return: The group_type of this RecommendFlavor.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this RecommendFlavor.

        规格类型

        :param group_type: The group_type of this RecommendFlavor.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def volume_flavors(self):
        """Gets the volume_flavors of this RecommendFlavor.

        磁盘规格信息

        :return: The volume_flavors of this RecommendFlavor.
        :rtype: list[:class:`huaweicloudsdkrds.v3.VolumeFlavor`]
        """
        return self._volume_flavors

    @volume_flavors.setter
    def volume_flavors(self, volume_flavors):
        """Sets the volume_flavors of this RecommendFlavor.

        磁盘规格信息

        :param volume_flavors: The volume_flavors of this RecommendFlavor.
        :type volume_flavors: list[:class:`huaweicloudsdkrds.v3.VolumeFlavor`]
        """
        self._volume_flavors = volume_flavors

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
        if not isinstance(other, RecommendFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
