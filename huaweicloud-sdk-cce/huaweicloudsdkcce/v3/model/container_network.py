# coding: utf-8

import pprint
import re

import six





class ContainerNetwork:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cidr': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'cidr': 'cidr',
        'mode': 'mode'
    }

    def __init__(self, cidr=None, mode=None):
        """ContainerNetwork - a model defined in huaweicloud sdk"""
        
        

        self._cidr = None
        self._mode = None
        self.discriminator = None

        if cidr is not None:
            self.cidr = cidr
        self.mode = mode

    @property
    def cidr(self):
        """Gets the cidr of this ContainerNetwork.

        容器网络网段，建议使用网段10.0.0.0/12~19，172.16.0.0/16~19，192.168.0.0/16~19，如存在网段冲突，将自动重新选择。  当节点最大实例数为默认值110时，当前容器网段至少支持582个节点，此参数在集群创建后不可更改，请谨慎选择。

        :return: The cidr of this ContainerNetwork.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ContainerNetwork.

        容器网络网段，建议使用网段10.0.0.0/12~19，172.16.0.0/16~19，192.168.0.0/16~19，如存在网段冲突，将自动重新选择。  当节点最大实例数为默认值110时，当前容器网段至少支持582个节点，此参数在集群创建后不可更改，请谨慎选择。

        :param cidr: The cidr of this ContainerNetwork.
        :type: str
        """
        self._cidr = cidr

    @property
    def mode(self):
        """Gets the mode of this ContainerNetwork.

        容器网络类型（只可选择其一） - overlay_l2：通过OVS（OpenVSwitch）为容器构建的overlay _ l2网络。 - underlay_ipvlan：裸金属服务器使用ipvlan构建的Underlay的l2网络。 - vpc-router：使用ipvlan和自定义VPC路由为容器构建的Underlay的l2网络。 - eni：Yangtse网络，深度整合VPC原生ENI弹性网卡能力，采用VPC网段分配容器地址，支持ELB直通容器，享有高性能，创建CCE Turbo集群（公测中）时指定。  >   - 容器隧道网络（Overlay）：基于VXLAN技术实现的Overlay容器网络。VXLAN是将以太网报文封装成UDP报文进行隧道传输。容器网络是承载于VPC网络之上的Overlay网络平面，具有付出少量隧道封装性能损耗，获得了通用性强、互通性强、高级特性支持全面（例如Network Policy网络隔离）的优势，可以满足大多数应用需求。 >   - VPC网络：基于VPC网络的自定义路由，直接将容器网络承载于VPC网络之中。每个节点将会被分配固定大小的IP地址段。vpc-router网络由于没有隧道封装的消耗，容器网络性能相对于容器隧道网络有一定优势。vpc-router集群由于VPC路由中配置有容器网段与节点IP的路由，可以支持集群外直接访问容器实例等特殊场景。

        :return: The mode of this ContainerNetwork.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ContainerNetwork.

        容器网络类型（只可选择其一） - overlay_l2：通过OVS（OpenVSwitch）为容器构建的overlay _ l2网络。 - underlay_ipvlan：裸金属服务器使用ipvlan构建的Underlay的l2网络。 - vpc-router：使用ipvlan和自定义VPC路由为容器构建的Underlay的l2网络。 - eni：Yangtse网络，深度整合VPC原生ENI弹性网卡能力，采用VPC网段分配容器地址，支持ELB直通容器，享有高性能，创建CCE Turbo集群（公测中）时指定。  >   - 容器隧道网络（Overlay）：基于VXLAN技术实现的Overlay容器网络。VXLAN是将以太网报文封装成UDP报文进行隧道传输。容器网络是承载于VPC网络之上的Overlay网络平面，具有付出少量隧道封装性能损耗，获得了通用性强、互通性强、高级特性支持全面（例如Network Policy网络隔离）的优势，可以满足大多数应用需求。 >   - VPC网络：基于VPC网络的自定义路由，直接将容器网络承载于VPC网络之中。每个节点将会被分配固定大小的IP地址段。vpc-router网络由于没有隧道封装的消耗，容器网络性能相对于容器隧道网络有一定优势。vpc-router集群由于VPC路由中配置有容器网段与节点IP的路由，可以支持集群外直接访问容器实例等特殊场景。

        :param mode: The mode of this ContainerNetwork.
        :type: str
        """
        self._mode = mode

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContainerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
