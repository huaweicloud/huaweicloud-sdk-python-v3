# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'mode': 'str',
        'cidr': 'str',
        'cidrs': 'list[ContainerCIDR]'
    }

    attribute_map = {
        'mode': 'mode',
        'cidr': 'cidr',
        'cidrs': 'cidrs'
    }

    def __init__(self, mode=None, cidr=None, cidrs=None):
        """ContainerNetwork

        The model defined in huaweicloud sdk

        :param mode: 容器网络类型（只可选择其一）  - overlay_l2：通过OVS（OpenVSwitch）为容器构建的overlay_l2网络。  - vpc-router：使用ipvlan和自定义VPC路由为容器构建的Underlay的l2网络。  [- eni：云原生网络2.0，深度整合VPC原生ENI弹性网卡能力，采用VPC网段分配容器地址，支持ELB直通容器，享有高性能，创建CCE Turbo集群时指定。](tag:hws,dt)
        :type mode: str
        :param cidr: 容器网络网段，建议使用网段10.0.0.0/12~19，172.16.0.0/16~19，192.168.0.0/16~19，如存在网段冲突，将会报错。   此参数在集群创建后不可更改，请谨慎选择。（已废弃，如填写cidrs将忽略该cidr）
        :type cidr: str
        :param cidrs: 容器网络网段列表。1.21及新版本集群使用cidrs字段，当集群网络类型为vpc-router类型时，支持多个容器网段；1.21之前版本若使用cidrs字段，则取值cidrs数组中的第一个cidr元素作为容器网络网段地址。  此参数在集群创建后不可更改，请谨慎选择。
        :type cidrs: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        """
        
        

        self._mode = None
        self._cidr = None
        self._cidrs = None
        self.discriminator = None

        self.mode = mode
        if cidr is not None:
            self.cidr = cidr
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def mode(self):
        """Gets the mode of this ContainerNetwork.

        容器网络类型（只可选择其一）  - overlay_l2：通过OVS（OpenVSwitch）为容器构建的overlay_l2网络。  - vpc-router：使用ipvlan和自定义VPC路由为容器构建的Underlay的l2网络。  [- eni：云原生网络2.0，深度整合VPC原生ENI弹性网卡能力，采用VPC网段分配容器地址，支持ELB直通容器，享有高性能，创建CCE Turbo集群时指定。](tag:hws,dt)

        :return: The mode of this ContainerNetwork.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ContainerNetwork.

        容器网络类型（只可选择其一）  - overlay_l2：通过OVS（OpenVSwitch）为容器构建的overlay_l2网络。  - vpc-router：使用ipvlan和自定义VPC路由为容器构建的Underlay的l2网络。  [- eni：云原生网络2.0，深度整合VPC原生ENI弹性网卡能力，采用VPC网段分配容器地址，支持ELB直通容器，享有高性能，创建CCE Turbo集群时指定。](tag:hws,dt)

        :param mode: The mode of this ContainerNetwork.
        :type mode: str
        """
        self._mode = mode

    @property
    def cidr(self):
        """Gets the cidr of this ContainerNetwork.

        容器网络网段，建议使用网段10.0.0.0/12~19，172.16.0.0/16~19，192.168.0.0/16~19，如存在网段冲突，将会报错。   此参数在集群创建后不可更改，请谨慎选择。（已废弃，如填写cidrs将忽略该cidr）

        :return: The cidr of this ContainerNetwork.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ContainerNetwork.

        容器网络网段，建议使用网段10.0.0.0/12~19，172.16.0.0/16~19，192.168.0.0/16~19，如存在网段冲突，将会报错。   此参数在集群创建后不可更改，请谨慎选择。（已废弃，如填写cidrs将忽略该cidr）

        :param cidr: The cidr of this ContainerNetwork.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def cidrs(self):
        """Gets the cidrs of this ContainerNetwork.

        容器网络网段列表。1.21及新版本集群使用cidrs字段，当集群网络类型为vpc-router类型时，支持多个容器网段；1.21之前版本若使用cidrs字段，则取值cidrs数组中的第一个cidr元素作为容器网络网段地址。  此参数在集群创建后不可更改，请谨慎选择。

        :return: The cidrs of this ContainerNetwork.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this ContainerNetwork.

        容器网络网段列表。1.21及新版本集群使用cidrs字段，当集群网络类型为vpc-router类型时，支持多个容器网段；1.21之前版本若使用cidrs字段，则取值cidrs数组中的第一个cidr元素作为容器网络网段地址。  此参数在集群创建后不可更改，请谨慎选择。

        :param cidrs: The cidrs of this ContainerNetwork.
        :type cidrs: list[:class:`huaweicloudsdkcce.v3.ContainerCIDR`]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, ContainerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
