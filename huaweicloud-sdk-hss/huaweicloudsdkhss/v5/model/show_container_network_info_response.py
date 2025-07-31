# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowContainerNetworkInfoResponse(SdkResponse):

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
        'vpc': 'str',
        'subnet': 'str',
        'security_group': 'str',
        'ipv4_cidr': 'str',
        'cidrs': 'str',
        'kube_proxy_mode': 'str',
        'is_support_egress': 'bool'
    }

    attribute_map = {
        'mode': 'mode',
        'vpc': 'vpc',
        'subnet': 'subnet',
        'security_group': 'security_group',
        'ipv4_cidr': 'ipv4_cidr',
        'cidrs': 'cidrs',
        'kube_proxy_mode': 'kube_proxy_mode',
        'is_support_egress': 'is_support_egress'
    }

    def __init__(self, mode=None, vpc=None, subnet=None, security_group=None, ipv4_cidr=None, cidrs=None, kube_proxy_mode=None, is_support_egress=None):
        r"""ShowContainerNetworkInfoResponse

        The model defined in huaweicloud sdk

        :param mode: 网络模型
        :type mode: str
        :param vpc: VPC Id
        :type vpc: str
        :param subnet: 网络ID
        :type subnet: str
        :param security_group: 安全组
        :type security_group: str
        :param ipv4_cidr: IPv4 服务网段
        :type ipv4_cidr: str
        :param cidrs: 容器网络网段
        :type cidrs: str
        :param kube_proxy_mode: 服务转发模式:    - iptables   - ipvs
        :type kube_proxy_mode: str
        :param is_support_egress: 是否支持配置egress规则: true、false
        :type is_support_egress: bool
        """
        
        super(ShowContainerNetworkInfoResponse, self).__init__()

        self._mode = None
        self._vpc = None
        self._subnet = None
        self._security_group = None
        self._ipv4_cidr = None
        self._cidrs = None
        self._kube_proxy_mode = None
        self._is_support_egress = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if vpc is not None:
            self.vpc = vpc
        if subnet is not None:
            self.subnet = subnet
        if security_group is not None:
            self.security_group = security_group
        if ipv4_cidr is not None:
            self.ipv4_cidr = ipv4_cidr
        if cidrs is not None:
            self.cidrs = cidrs
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if is_support_egress is not None:
            self.is_support_egress = is_support_egress

    @property
    def mode(self):
        r"""Gets the mode of this ShowContainerNetworkInfoResponse.

        网络模型

        :return: The mode of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShowContainerNetworkInfoResponse.

        网络模型

        :param mode: The mode of this ShowContainerNetworkInfoResponse.
        :type mode: str
        """
        self._mode = mode

    @property
    def vpc(self):
        r"""Gets the vpc of this ShowContainerNetworkInfoResponse.

        VPC Id

        :return: The vpc of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this ShowContainerNetworkInfoResponse.

        VPC Id

        :param vpc: The vpc of this ShowContainerNetworkInfoResponse.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def subnet(self):
        r"""Gets the subnet of this ShowContainerNetworkInfoResponse.

        网络ID

        :return: The subnet of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        r"""Sets the subnet of this ShowContainerNetworkInfoResponse.

        网络ID

        :param subnet: The subnet of this ShowContainerNetworkInfoResponse.
        :type subnet: str
        """
        self._subnet = subnet

    @property
    def security_group(self):
        r"""Gets the security_group of this ShowContainerNetworkInfoResponse.

        安全组

        :return: The security_group of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this ShowContainerNetworkInfoResponse.

        安全组

        :param security_group: The security_group of this ShowContainerNetworkInfoResponse.
        :type security_group: str
        """
        self._security_group = security_group

    @property
    def ipv4_cidr(self):
        r"""Gets the ipv4_cidr of this ShowContainerNetworkInfoResponse.

        IPv4 服务网段

        :return: The ipv4_cidr of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._ipv4_cidr

    @ipv4_cidr.setter
    def ipv4_cidr(self, ipv4_cidr):
        r"""Sets the ipv4_cidr of this ShowContainerNetworkInfoResponse.

        IPv4 服务网段

        :param ipv4_cidr: The ipv4_cidr of this ShowContainerNetworkInfoResponse.
        :type ipv4_cidr: str
        """
        self._ipv4_cidr = ipv4_cidr

    @property
    def cidrs(self):
        r"""Gets the cidrs of this ShowContainerNetworkInfoResponse.

        容器网络网段

        :return: The cidrs of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        r"""Sets the cidrs of this ShowContainerNetworkInfoResponse.

        容器网络网段

        :param cidrs: The cidrs of this ShowContainerNetworkInfoResponse.
        :type cidrs: str
        """
        self._cidrs = cidrs

    @property
    def kube_proxy_mode(self):
        r"""Gets the kube_proxy_mode of this ShowContainerNetworkInfoResponse.

        服务转发模式:    - iptables   - ipvs

        :return: The kube_proxy_mode of this ShowContainerNetworkInfoResponse.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        r"""Sets the kube_proxy_mode of this ShowContainerNetworkInfoResponse.

        服务转发模式:    - iptables   - ipvs

        :param kube_proxy_mode: The kube_proxy_mode of this ShowContainerNetworkInfoResponse.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def is_support_egress(self):
        r"""Gets the is_support_egress of this ShowContainerNetworkInfoResponse.

        是否支持配置egress规则: true、false

        :return: The is_support_egress of this ShowContainerNetworkInfoResponse.
        :rtype: bool
        """
        return self._is_support_egress

    @is_support_egress.setter
    def is_support_egress(self, is_support_egress):
        r"""Sets the is_support_egress of this ShowContainerNetworkInfoResponse.

        是否支持配置egress规则: true、false

        :param is_support_egress: The is_support_egress of this ShowContainerNetworkInfoResponse.
        :type is_support_egress: bool
        """
        self._is_support_egress = is_support_egress

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
        if not isinstance(other, ShowContainerNetworkInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
