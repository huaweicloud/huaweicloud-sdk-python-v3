# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVirtualGateway:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'enterprise_router_id': 'str',
        'name': 'str',
        'description': 'str',
        'local_ep_group': 'list[str]',
        'local_ep_group_ipv6': 'list[str]',
        'bgp_asn': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'enterprise_router_id': 'enterprise_router_id',
        'name': 'name',
        'description': 'description',
        'local_ep_group': 'local_ep_group',
        'local_ep_group_ipv6': 'local_ep_group_ipv6',
        'bgp_asn': 'bgp_asn',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, vpc_id=None, enterprise_router_id=None, name=None, description=None, local_ep_group=None, local_ep_group_ipv6=None, bgp_asn=None, enterprise_project_id=None, tags=None):
        r"""CreateVirtualGateway

        The model defined in huaweicloud sdk

        :param vpc_id: 虚拟网关接入的VPC的ID[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)
        :type vpc_id: str
        :param enterprise_router_id: 虚拟网关接入的ER的ID，当选择创建接入ER的虚拟网关时必选。
        :type enterprise_router_id: str
        :param name: 虚拟网关名字
        :type name: str
        :param description: 虚拟网关的描述信息
        :type description: str
        :param local_ep_group: 虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)
        :type local_ep_group: list[str]
        :param local_ep_group_ipv6: 预留字段用于虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs
        :type local_ep_group_ipv6: list[str]
        :param bgp_asn: 虚拟网关本地的BGP自治域号(asn)
        :type bgp_asn: int
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        
        

        self._vpc_id = None
        self._enterprise_router_id = None
        self._name = None
        self._description = None
        self._local_ep_group = None
        self._local_ep_group_ipv6 = None
        self._bgp_asn = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.vpc_id = vpc_id
        if enterprise_router_id is not None:
            self.enterprise_router_id = enterprise_router_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.local_ep_group = local_ep_group
        if local_ep_group_ipv6 is not None:
            self.local_ep_group_ipv6 = local_ep_group_ipv6
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateVirtualGateway.

        虚拟网关接入的VPC的ID[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)

        :return: The vpc_id of this CreateVirtualGateway.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateVirtualGateway.

        虚拟网关接入的VPC的ID[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)

        :param vpc_id: The vpc_id of this CreateVirtualGateway.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this CreateVirtualGateway.

        虚拟网关接入的ER的ID，当选择创建接入ER的虚拟网关时必选。

        :return: The enterprise_router_id of this CreateVirtualGateway.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this CreateVirtualGateway.

        虚拟网关接入的ER的ID，当选择创建接入ER的虚拟网关时必选。

        :param enterprise_router_id: The enterprise_router_id of this CreateVirtualGateway.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def name(self):
        r"""Gets the name of this CreateVirtualGateway.

        虚拟网关名字

        :return: The name of this CreateVirtualGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVirtualGateway.

        虚拟网关名字

        :param name: The name of this CreateVirtualGateway.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateVirtualGateway.

        虚拟网关的描述信息

        :return: The description of this CreateVirtualGateway.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVirtualGateway.

        虚拟网关的描述信息

        :param description: The description of this CreateVirtualGateway.
        :type description: str
        """
        self._description = description

    @property
    def local_ep_group(self):
        r"""Gets the local_ep_group of this CreateVirtualGateway.

        虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)

        :return: The local_ep_group of this CreateVirtualGateway.
        :rtype: list[str]
        """
        return self._local_ep_group

    @local_ep_group.setter
    def local_ep_group(self, local_ep_group):
        r"""Sets the local_ep_group of this CreateVirtualGateway.

        虚拟网关到访问云上服务IPv4子网列表，通常是vpc的cidrs[，当选择创建接入VPC的虚拟网关时必选。](tag:dt)

        :param local_ep_group: The local_ep_group of this CreateVirtualGateway.
        :type local_ep_group: list[str]
        """
        self._local_ep_group = local_ep_group

    @property
    def local_ep_group_ipv6(self):
        r"""Gets the local_ep_group_ipv6 of this CreateVirtualGateway.

        预留字段用于虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs

        :return: The local_ep_group_ipv6 of this CreateVirtualGateway.
        :rtype: list[str]
        """
        return self._local_ep_group_ipv6

    @local_ep_group_ipv6.setter
    def local_ep_group_ipv6(self, local_ep_group_ipv6):
        r"""Sets the local_ep_group_ipv6 of this CreateVirtualGateway.

        预留字段用于虚拟网关到访问云上服务IPv6子网列表，通常是vpc的cidrs

        :param local_ep_group_ipv6: The local_ep_group_ipv6 of this CreateVirtualGateway.
        :type local_ep_group_ipv6: list[str]
        """
        self._local_ep_group_ipv6 = local_ep_group_ipv6

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this CreateVirtualGateway.

        虚拟网关本地的BGP自治域号(asn)

        :return: The bgp_asn of this CreateVirtualGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this CreateVirtualGateway.

        虚拟网关本地的BGP自治域号(asn)

        :param bgp_asn: The bgp_asn of this CreateVirtualGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateVirtualGateway.

        实例所属企业项目ID

        :return: The enterprise_project_id of this CreateVirtualGateway.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateVirtualGateway.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateVirtualGateway.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateVirtualGateway.

        标签信息

        :return: The tags of this CreateVirtualGateway.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateVirtualGateway.

        标签信息

        :param tags: The tags of this CreateVirtualGateway.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateVirtualGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
