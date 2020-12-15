# coding: utf-8

import pprint
import re

import six





class HostNetwork:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_group': 'str',
        'highway_subnet': 'str',
        'subnet': 'str',
        'vpc': 'str'
    }

    attribute_map = {
        'security_group': 'SecurityGroup',
        'highway_subnet': 'highwaySubnet',
        'subnet': 'subnet',
        'vpc': 'vpc'
    }

    def __init__(self, security_group=None, highway_subnet=None, subnet=None, vpc=None):
        """HostNetwork - a model defined in huaweicloud sdk"""
        
        

        self._security_group = None
        self._highway_subnet = None
        self._subnet = None
        self._vpc = None
        self.discriminator = None

        if security_group is not None:
            self.security_group = security_group
        if highway_subnet is not None:
            self.highway_subnet = highway_subnet
        self.subnet = subnet
        self.vpc = vpc

    @property
    def security_group(self):
        """Gets the security_group of this HostNetwork.

        节点安全组ID，创建时指定无效 

        :return: The security_group of this HostNetwork.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this HostNetwork.

        节点安全组ID，创建时指定无效 

        :param security_group: The security_group of this HostNetwork.
        :type: str
        """
        self._security_group = security_group

    @property
    def highway_subnet(self):
        """Gets the highway_subnet of this HostNetwork.

        用于创建裸金属节点的高速网络的子网ID。该值在[创建高速网络（可选）](https://support.huaweicloud.com/api-cce/cce_02_0270.html)中获取。创建裸金属集群时该参数为必选参数。

        :return: The highway_subnet of this HostNetwork.
        :rtype: str
        """
        return self._highway_subnet

    @highway_subnet.setter
    def highway_subnet(self, highway_subnet):
        """Sets the highway_subnet of this HostNetwork.

        用于创建裸金属节点的高速网络的子网ID。该值在[创建高速网络（可选）](https://support.huaweicloud.com/api-cce/cce_02_0270.html)中获取。创建裸金属集群时该参数为必选参数。

        :param highway_subnet: The highway_subnet of this HostNetwork.
        :type: str
        """
        self._highway_subnet = highway_subnet

    @property
    def subnet(self):
        """Gets the subnet of this HostNetwork.

        用于创建控制节点的subnet的网络ID。获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)  

        :return: The subnet of this HostNetwork.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this HostNetwork.

        用于创建控制节点的subnet的网络ID。获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)  

        :param subnet: The subnet of this HostNetwork.
        :type: str
        """
        self._subnet = subnet

    @property
    def vpc(self):
        """Gets the vpc of this HostNetwork.

        用于创建控制节点的VPC的ID。该值在[创建VPC和子网](https://support.huaweicloud.com/api-cce/cce_02_0100.html)中获取。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)   >当前vpc-router容器网络模型不支持对接含拓展网段的VPC。 >若您的用户类型为企业用户，则需要保证vpc所属的企业项目ID和集群创建时选择的企业项目ID一致。集群所属的企业项目ID通过extendParam字段下的enterpriseProjectId体现，该值默认为\"0\"，表示默认的企业项目。

        :return: The vpc of this HostNetwork.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this HostNetwork.

        用于创建控制节点的VPC的ID。该值在[创建VPC和子网](https://support.huaweicloud.com/api-cce/cce_02_0100.html)中获取。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)   >当前vpc-router容器网络模型不支持对接含拓展网段的VPC。 >若您的用户类型为企业用户，则需要保证vpc所属的企业项目ID和集群创建时选择的企业项目ID一致。集群所属的企业项目ID通过extendParam字段下的enterpriseProjectId体现，该值默认为\"0\"，表示默认的企业项目。

        :param vpc: The vpc of this HostNetwork.
        :type: str
        """
        self._vpc = vpc

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
        if not isinstance(other, HostNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
