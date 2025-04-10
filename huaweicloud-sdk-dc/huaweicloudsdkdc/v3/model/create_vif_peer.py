# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVifPeer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'address_family': 'str',
        'local_gateway_ip': 'str',
        'remote_gateway_ip': 'str',
        'route_mode': 'str',
        'bgp_asn': 'int',
        'bgp_md5': 'str',
        'remote_ep_group': 'list[str]',
        'vif_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'address_family': 'address_family',
        'local_gateway_ip': 'local_gateway_ip',
        'remote_gateway_ip': 'remote_gateway_ip',
        'route_mode': 'route_mode',
        'bgp_asn': 'bgp_asn',
        'bgp_md5': 'bgp_md5',
        'remote_ep_group': 'remote_ep_group',
        'vif_id': 'vif_id'
    }

    def __init__(self, name=None, description=None, address_family=None, local_gateway_ip=None, remote_gateway_ip=None, route_mode=None, bgp_asn=None, bgp_md5=None, remote_ep_group=None, vif_id=None):
        r"""CreateVifPeer

        The model defined in huaweicloud sdk

        :param name: VIF对等体名字
        :type name: str
        :param description: VIF对等体名字描述信息
        :type description: str
        :param address_family: 接口的地址簇类型，ipv4，ipv6
        :type address_family: str
        :param local_gateway_ip: VIF对等体云侧接口地址
        :type local_gateway_ip: str
        :param remote_gateway_ip: VIF对等体客户侧接口地址
        :type remote_gateway_ip: str
        :param route_mode: 路由模式：static/bgp
        :type route_mode: str
        :param bgp_asn: BGP邻居的AS号
        :type bgp_asn: int
        :param bgp_md5: BGP邻居的MD5密码
        :type bgp_md5: str
        :param remote_ep_group: 远端子网列表，记录租户侧的cidrs
        :type remote_ep_group: list[str]
        :param vif_id: vif对等体对应的虚拟接口ID
        :type vif_id: str
        """
        
        

        self._name = None
        self._description = None
        self._address_family = None
        self._local_gateway_ip = None
        self._remote_gateway_ip = None
        self._route_mode = None
        self._bgp_asn = None
        self._bgp_md5 = None
        self._remote_ep_group = None
        self._vif_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_family is not None:
            self.address_family = address_family
        if local_gateway_ip is not None:
            self.local_gateway_ip = local_gateway_ip
        if remote_gateway_ip is not None:
            self.remote_gateway_ip = remote_gateway_ip
        if route_mode is not None:
            self.route_mode = route_mode
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if bgp_md5 is not None:
            self.bgp_md5 = bgp_md5
        if remote_ep_group is not None:
            self.remote_ep_group = remote_ep_group
        if vif_id is not None:
            self.vif_id = vif_id

    @property
    def name(self):
        r"""Gets the name of this CreateVifPeer.

        VIF对等体名字

        :return: The name of this CreateVifPeer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVifPeer.

        VIF对等体名字

        :param name: The name of this CreateVifPeer.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateVifPeer.

        VIF对等体名字描述信息

        :return: The description of this CreateVifPeer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVifPeer.

        VIF对等体名字描述信息

        :param description: The description of this CreateVifPeer.
        :type description: str
        """
        self._description = description

    @property
    def address_family(self):
        r"""Gets the address_family of this CreateVifPeer.

        接口的地址簇类型，ipv4，ipv6

        :return: The address_family of this CreateVifPeer.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        r"""Sets the address_family of this CreateVifPeer.

        接口的地址簇类型，ipv4，ipv6

        :param address_family: The address_family of this CreateVifPeer.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def local_gateway_ip(self):
        r"""Gets the local_gateway_ip of this CreateVifPeer.

        VIF对等体云侧接口地址

        :return: The local_gateway_ip of this CreateVifPeer.
        :rtype: str
        """
        return self._local_gateway_ip

    @local_gateway_ip.setter
    def local_gateway_ip(self, local_gateway_ip):
        r"""Sets the local_gateway_ip of this CreateVifPeer.

        VIF对等体云侧接口地址

        :param local_gateway_ip: The local_gateway_ip of this CreateVifPeer.
        :type local_gateway_ip: str
        """
        self._local_gateway_ip = local_gateway_ip

    @property
    def remote_gateway_ip(self):
        r"""Gets the remote_gateway_ip of this CreateVifPeer.

        VIF对等体客户侧接口地址

        :return: The remote_gateway_ip of this CreateVifPeer.
        :rtype: str
        """
        return self._remote_gateway_ip

    @remote_gateway_ip.setter
    def remote_gateway_ip(self, remote_gateway_ip):
        r"""Sets the remote_gateway_ip of this CreateVifPeer.

        VIF对等体客户侧接口地址

        :param remote_gateway_ip: The remote_gateway_ip of this CreateVifPeer.
        :type remote_gateway_ip: str
        """
        self._remote_gateway_ip = remote_gateway_ip

    @property
    def route_mode(self):
        r"""Gets the route_mode of this CreateVifPeer.

        路由模式：static/bgp

        :return: The route_mode of this CreateVifPeer.
        :rtype: str
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        r"""Sets the route_mode of this CreateVifPeer.

        路由模式：static/bgp

        :param route_mode: The route_mode of this CreateVifPeer.
        :type route_mode: str
        """
        self._route_mode = route_mode

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this CreateVifPeer.

        BGP邻居的AS号

        :return: The bgp_asn of this CreateVifPeer.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this CreateVifPeer.

        BGP邻居的AS号

        :param bgp_asn: The bgp_asn of this CreateVifPeer.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def bgp_md5(self):
        r"""Gets the bgp_md5 of this CreateVifPeer.

        BGP邻居的MD5密码

        :return: The bgp_md5 of this CreateVifPeer.
        :rtype: str
        """
        return self._bgp_md5

    @bgp_md5.setter
    def bgp_md5(self, bgp_md5):
        r"""Sets the bgp_md5 of this CreateVifPeer.

        BGP邻居的MD5密码

        :param bgp_md5: The bgp_md5 of this CreateVifPeer.
        :type bgp_md5: str
        """
        self._bgp_md5 = bgp_md5

    @property
    def remote_ep_group(self):
        r"""Gets the remote_ep_group of this CreateVifPeer.

        远端子网列表，记录租户侧的cidrs

        :return: The remote_ep_group of this CreateVifPeer.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        r"""Sets the remote_ep_group of this CreateVifPeer.

        远端子网列表，记录租户侧的cidrs

        :param remote_ep_group: The remote_ep_group of this CreateVifPeer.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

    @property
    def vif_id(self):
        r"""Gets the vif_id of this CreateVifPeer.

        vif对等体对应的虚拟接口ID

        :return: The vif_id of this CreateVifPeer.
        :rtype: str
        """
        return self._vif_id

    @vif_id.setter
    def vif_id(self, vif_id):
        r"""Sets the vif_id of this CreateVifPeer.

        vif对等体对应的虚拟接口ID

        :param vif_id: The vif_id of this CreateVifPeer.
        :type vif_id: str
        """
        self._vif_id = vif_id

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
        if not isinstance(other, CreateVifPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
