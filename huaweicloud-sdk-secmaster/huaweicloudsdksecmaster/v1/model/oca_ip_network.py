# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_public': 'bool',
        'partition': 'str',
        'plane': 'str',
        'vxlan_id': 'str'
    }

    attribute_map = {
        'is_public': 'is_public',
        'partition': 'partition',
        'plane': 'plane',
        'vxlan_id': 'vxlan_id'
    }

    def __init__(self, is_public=None, partition=None, plane=None, vxlan_id=None):
        r"""OcaIpNetwork

        The model defined in huaweicloud sdk

        :param is_public: 外网或内网 true：外网 false: 内网
        :type is_public: bool
        :param partition: 网络分区：OM/PSZ/DMZ
        :type partition: str
        :param plane: 网络平面（线下有自己的代号）
        :type plane: str
        :param vxlan_id: 虚拟网络ID
        :type vxlan_id: str
        """
        
        

        self._is_public = None
        self._partition = None
        self._plane = None
        self._vxlan_id = None
        self.discriminator = None

        self.is_public = is_public
        if partition is not None:
            self.partition = partition
        if plane is not None:
            self.plane = plane
        if vxlan_id is not None:
            self.vxlan_id = vxlan_id

    @property
    def is_public(self):
        r"""Gets the is_public of this OcaIpNetwork.

        外网或内网 true：外网 false: 内网

        :return: The is_public of this OcaIpNetwork.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this OcaIpNetwork.

        外网或内网 true：外网 false: 内网

        :param is_public: The is_public of this OcaIpNetwork.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def partition(self):
        r"""Gets the partition of this OcaIpNetwork.

        网络分区：OM/PSZ/DMZ

        :return: The partition of this OcaIpNetwork.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this OcaIpNetwork.

        网络分区：OM/PSZ/DMZ

        :param partition: The partition of this OcaIpNetwork.
        :type partition: str
        """
        self._partition = partition

    @property
    def plane(self):
        r"""Gets the plane of this OcaIpNetwork.

        网络平面（线下有自己的代号）

        :return: The plane of this OcaIpNetwork.
        :rtype: str
        """
        return self._plane

    @plane.setter
    def plane(self, plane):
        r"""Sets the plane of this OcaIpNetwork.

        网络平面（线下有自己的代号）

        :param plane: The plane of this OcaIpNetwork.
        :type plane: str
        """
        self._plane = plane

    @property
    def vxlan_id(self):
        r"""Gets the vxlan_id of this OcaIpNetwork.

        虚拟网络ID

        :return: The vxlan_id of this OcaIpNetwork.
        :rtype: str
        """
        return self._vxlan_id

    @vxlan_id.setter
    def vxlan_id(self, vxlan_id):
        r"""Sets the vxlan_id of this OcaIpNetwork.

        虚拟网络ID

        :param vxlan_id: The vxlan_id of this OcaIpNetwork.
        :type vxlan_id: str
        """
        self._vxlan_id = vxlan_id

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
        if not isinstance(other, OcaIpNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
