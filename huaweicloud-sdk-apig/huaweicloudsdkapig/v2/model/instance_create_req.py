# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'spec_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'eip_id': 'str',
        'enterprise_project_id': 'str',
        'available_zone_ids': 'list[str]',
        'bandwidth_size': 'int',
        'bandwidth_charging_mode': 'str',
        'ipv6_enable': 'bool',
        'loadbalancer_provider': 'str',
        'tags': 'list[TmsKeyValue]',
        'vpcep_service_name': 'str',
        'ingress_bandwidth_size': 'int',
        'ingress_bandwidth_charging_mode': 'str'
    }

    attribute_map = {
        'description': 'description',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'spec_id': 'spec_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'eip_id': 'eip_id',
        'enterprise_project_id': 'enterprise_project_id',
        'available_zone_ids': 'available_zone_ids',
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_charging_mode': 'bandwidth_charging_mode',
        'ipv6_enable': 'ipv6_enable',
        'loadbalancer_provider': 'loadbalancer_provider',
        'tags': 'tags',
        'vpcep_service_name': 'vpcep_service_name',
        'ingress_bandwidth_size': 'ingress_bandwidth_size',
        'ingress_bandwidth_charging_mode': 'ingress_bandwidth_charging_mode'
    }

    def __init__(self, description=None, maintain_begin=None, maintain_end=None, instance_name=None, instance_id=None, spec_id=None, vpc_id=None, subnet_id=None, security_group_id=None, eip_id=None, enterprise_project_id=None, available_zone_ids=None, bandwidth_size=None, bandwidth_charging_mode=None, ipv6_enable=None, loadbalancer_provider=None, tags=None, vpcep_service_name=None, ingress_bandwidth_size=None, ingress_bandwidth_charging_mode=None):
        """InstanceCreateReq

        The model defined in huaweicloud sdk

        :param description: 实例描述
        :type description: str
        :param maintain_begin: 维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。
        :type maintain_begin: str
        :param maintain_end: 维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。
        :type maintain_end: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param instance_id: 实例编号，不填写自动生成
        :type instance_id: str
        :param spec_id: 实例规格： - BASIC：基础版实例 - PROFESSIONAL：专业版实例 - ENTERPRISE：企业版实例 - PLATINUM：铂金版实例 - BASIC_IPV6：基础版IPV6实例 - PROFESSIONAL_IPV6：专业版IPV6实例 - ENTERPRISE_IPV6：企业版IPV6实例 - PLATINUM_IPV6：铂金版IPV6实例
        :type spec_id: str
        :param vpc_id: 虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询VPC列表”章节。 
        :type vpc_id: str
        :param subnet_id: 子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询子网列表”章节。 
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 
        :type security_group_id: str
        :param eip_id: 弹性公网IP ID。  实例需要开启公网访问，且loadbalancer_provider为lvs时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源  获取方法：登录虚拟私有云服务的控制台界面，在弹性公网IP的详情页面查找弹性公网IP ID。
        :type eip_id: str
        :param enterprise_project_id: 企业项目ID，企业帐号必填。  获取方法如下： - 方法1：登录企业项目管理界面，在项目管理详情页面查找项目ID。 - 方法2：通过企业项目管理的API接口查询，具体方法请参见《企业管理API参考》的“查询企业项目列表”章节。
        :type enterprise_project_id: str
        :param available_zone_ids: 可用区列表。  可用区指在同一地域下，电力、网络隔离的物理区域，可用区之内内网互通，不同可用区之间物理隔离。选择多个AZ部署可以有效提升可靠性。  获取方法：通过文档中实例管理的可用区列表接口查询。
        :type available_zone_ids: list[str]
        :param bandwidth_size: 出公网带宽  实例需要开启出公网功能时需要填写，绑定后使用者可以利用该出口访问公网上的互联网资源
        :type bandwidth_size: int
        :param bandwidth_charging_mode: 出公网带宽计费类型，实例需要开启出公网功能时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费
        :type bandwidth_charging_mode: str
        :param ipv6_enable: 公网访问是否支持IPv6。  当前仅部分region部分可用区支持IPv6
        :type ipv6_enable: bool
        :param loadbalancer_provider: 实例使用的负载均衡器类型 - lvs Linux虚拟服务器 - elb 弹性负载均衡，elb仅部分region支持
        :type loadbalancer_provider: str
        :param tags: 标签列表。  一个实例默认最多支持创建20个标签
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        :param vpcep_service_name: 终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 实例创建完成后，可以在实例管理-&gt;终端节点管理页面修改该名称。 
        :type vpcep_service_name: str
        :param ingress_bandwidth_size: 入公网带宽  实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源
        :type ingress_bandwidth_size: int
        :param ingress_bandwidth_charging_mode: 入公网带宽计费类型，实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费
        :type ingress_bandwidth_charging_mode: str
        """
        
        

        self._description = None
        self._maintain_begin = None
        self._maintain_end = None
        self._instance_name = None
        self._instance_id = None
        self._spec_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._eip_id = None
        self._enterprise_project_id = None
        self._available_zone_ids = None
        self._bandwidth_size = None
        self._bandwidth_charging_mode = None
        self._ipv6_enable = None
        self._loadbalancer_provider = None
        self._tags = None
        self._vpcep_service_name = None
        self._ingress_bandwidth_size = None
        self._ingress_bandwidth_charging_mode = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if spec_id is not None:
            self.spec_id = spec_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if eip_id is not None:
            self.eip_id = eip_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if available_zone_ids is not None:
            self.available_zone_ids = available_zone_ids
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_charging_mode is not None:
            self.bandwidth_charging_mode = bandwidth_charging_mode
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if loadbalancer_provider is not None:
            self.loadbalancer_provider = loadbalancer_provider
        if tags is not None:
            self.tags = tags
        if vpcep_service_name is not None:
            self.vpcep_service_name = vpcep_service_name
        if ingress_bandwidth_size is not None:
            self.ingress_bandwidth_size = ingress_bandwidth_size
        if ingress_bandwidth_charging_mode is not None:
            self.ingress_bandwidth_charging_mode = ingress_bandwidth_charging_mode

    @property
    def description(self):
        """Gets the description of this InstanceCreateReq.

        实例描述

        :return: The description of this InstanceCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceCreateReq.

        实例描述

        :param description: The description of this InstanceCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this InstanceCreateReq.

        维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :return: The maintain_begin of this InstanceCreateReq.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this InstanceCreateReq.

        维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :param maintain_begin: The maintain_begin of this InstanceCreateReq.
        :type maintain_begin: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this InstanceCreateReq.

        维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :return: The maintain_end of this InstanceCreateReq.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this InstanceCreateReq.

        维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。  在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。

        :param maintain_end: The maintain_end of this InstanceCreateReq.
        :type maintain_end: str
        """
        self._maintain_end = maintain_end

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceCreateReq.

        实例名称

        :return: The instance_name of this InstanceCreateReq.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceCreateReq.

        实例名称

        :param instance_name: The instance_name of this InstanceCreateReq.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceCreateReq.

        实例编号，不填写自动生成

        :return: The instance_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceCreateReq.

        实例编号，不填写自动生成

        :param instance_id: The instance_id of this InstanceCreateReq.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def spec_id(self):
        """Gets the spec_id of this InstanceCreateReq.

        实例规格： - BASIC：基础版实例 - PROFESSIONAL：专业版实例 - ENTERPRISE：企业版实例 - PLATINUM：铂金版实例 - BASIC_IPV6：基础版IPV6实例 - PROFESSIONAL_IPV6：专业版IPV6实例 - ENTERPRISE_IPV6：企业版IPV6实例 - PLATINUM_IPV6：铂金版IPV6实例

        :return: The spec_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        """Sets the spec_id of this InstanceCreateReq.

        实例规格： - BASIC：基础版实例 - PROFESSIONAL：专业版实例 - ENTERPRISE：企业版实例 - PLATINUM：铂金版实例 - BASIC_IPV6：基础版IPV6实例 - PROFESSIONAL_IPV6：专业版IPV6实例 - ENTERPRISE_IPV6：企业版IPV6实例 - PLATINUM_IPV6：铂金版IPV6实例

        :param spec_id: The spec_id of this InstanceCreateReq.
        :type spec_id: str
        """
        self._spec_id = spec_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceCreateReq.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询VPC列表”章节。 

        :return: The vpc_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceCreateReq.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询VPC列表”章节。 

        :param vpc_id: The vpc_id of this InstanceCreateReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceCreateReq.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询子网列表”章节。 

        :return: The subnet_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceCreateReq.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询子网列表”章节。 

        :param subnet_id: The subnet_id of this InstanceCreateReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceCreateReq.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :return: The security_group_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceCreateReq.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :param security_group_id: The security_group_id of this InstanceCreateReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def eip_id(self):
        """Gets the eip_id of this InstanceCreateReq.

        弹性公网IP ID。  实例需要开启公网访问，且loadbalancer_provider为lvs时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源  获取方法：登录虚拟私有云服务的控制台界面，在弹性公网IP的详情页面查找弹性公网IP ID。

        :return: The eip_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this InstanceCreateReq.

        弹性公网IP ID。  实例需要开启公网访问，且loadbalancer_provider为lvs时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源  获取方法：登录虚拟私有云服务的控制台界面，在弹性公网IP的详情页面查找弹性公网IP ID。

        :param eip_id: The eip_id of this InstanceCreateReq.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceCreateReq.

        企业项目ID，企业帐号必填。  获取方法如下： - 方法1：登录企业项目管理界面，在项目管理详情页面查找项目ID。 - 方法2：通过企业项目管理的API接口查询，具体方法请参见《企业管理API参考》的“查询企业项目列表”章节。

        :return: The enterprise_project_id of this InstanceCreateReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceCreateReq.

        企业项目ID，企业帐号必填。  获取方法如下： - 方法1：登录企业项目管理界面，在项目管理详情页面查找项目ID。 - 方法2：通过企业项目管理的API接口查询，具体方法请参见《企业管理API参考》的“查询企业项目列表”章节。

        :param enterprise_project_id: The enterprise_project_id of this InstanceCreateReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def available_zone_ids(self):
        """Gets the available_zone_ids of this InstanceCreateReq.

        可用区列表。  可用区指在同一地域下，电力、网络隔离的物理区域，可用区之内内网互通，不同可用区之间物理隔离。选择多个AZ部署可以有效提升可靠性。  获取方法：通过文档中实例管理的可用区列表接口查询。

        :return: The available_zone_ids of this InstanceCreateReq.
        :rtype: list[str]
        """
        return self._available_zone_ids

    @available_zone_ids.setter
    def available_zone_ids(self, available_zone_ids):
        """Sets the available_zone_ids of this InstanceCreateReq.

        可用区列表。  可用区指在同一地域下，电力、网络隔离的物理区域，可用区之内内网互通，不同可用区之间物理隔离。选择多个AZ部署可以有效提升可靠性。  获取方法：通过文档中实例管理的可用区列表接口查询。

        :param available_zone_ids: The available_zone_ids of this InstanceCreateReq.
        :type available_zone_ids: list[str]
        """
        self._available_zone_ids = available_zone_ids

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this InstanceCreateReq.

        出公网带宽  实例需要开启出公网功能时需要填写，绑定后使用者可以利用该出口访问公网上的互联网资源

        :return: The bandwidth_size of this InstanceCreateReq.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this InstanceCreateReq.

        出公网带宽  实例需要开启出公网功能时需要填写，绑定后使用者可以利用该出口访问公网上的互联网资源

        :param bandwidth_size: The bandwidth_size of this InstanceCreateReq.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_charging_mode(self):
        """Gets the bandwidth_charging_mode of this InstanceCreateReq.

        出公网带宽计费类型，实例需要开启出公网功能时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费

        :return: The bandwidth_charging_mode of this InstanceCreateReq.
        :rtype: str
        """
        return self._bandwidth_charging_mode

    @bandwidth_charging_mode.setter
    def bandwidth_charging_mode(self, bandwidth_charging_mode):
        """Sets the bandwidth_charging_mode of this InstanceCreateReq.

        出公网带宽计费类型，实例需要开启出公网功能时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费

        :param bandwidth_charging_mode: The bandwidth_charging_mode of this InstanceCreateReq.
        :type bandwidth_charging_mode: str
        """
        self._bandwidth_charging_mode = bandwidth_charging_mode

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this InstanceCreateReq.

        公网访问是否支持IPv6。  当前仅部分region部分可用区支持IPv6

        :return: The ipv6_enable of this InstanceCreateReq.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this InstanceCreateReq.

        公网访问是否支持IPv6。  当前仅部分region部分可用区支持IPv6

        :param ipv6_enable: The ipv6_enable of this InstanceCreateReq.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def loadbalancer_provider(self):
        """Gets the loadbalancer_provider of this InstanceCreateReq.

        实例使用的负载均衡器类型 - lvs Linux虚拟服务器 - elb 弹性负载均衡，elb仅部分region支持

        :return: The loadbalancer_provider of this InstanceCreateReq.
        :rtype: str
        """
        return self._loadbalancer_provider

    @loadbalancer_provider.setter
    def loadbalancer_provider(self, loadbalancer_provider):
        """Sets the loadbalancer_provider of this InstanceCreateReq.

        实例使用的负载均衡器类型 - lvs Linux虚拟服务器 - elb 弹性负载均衡，elb仅部分region支持

        :param loadbalancer_provider: The loadbalancer_provider of this InstanceCreateReq.
        :type loadbalancer_provider: str
        """
        self._loadbalancer_provider = loadbalancer_provider

    @property
    def tags(self):
        """Gets the tags of this InstanceCreateReq.

        标签列表。  一个实例默认最多支持创建20个标签

        :return: The tags of this InstanceCreateReq.
        :rtype: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceCreateReq.

        标签列表。  一个实例默认最多支持创建20个标签

        :param tags: The tags of this InstanceCreateReq.
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        """
        self._tags = tags

    @property
    def vpcep_service_name(self):
        """Gets the vpcep_service_name of this InstanceCreateReq.

        终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 实例创建完成后，可以在实例管理->终端节点管理页面修改该名称。 

        :return: The vpcep_service_name of this InstanceCreateReq.
        :rtype: str
        """
        return self._vpcep_service_name

    @vpcep_service_name.setter
    def vpcep_service_name(self, vpcep_service_name):
        """Sets the vpcep_service_name of this InstanceCreateReq.

        终端节点服务的名称。  长度不超过16个字符，允许输入大小写字母、数字、下划线、中划线。  如果您不填写该参数，系统生成的终端节点服务的名称为{region}.apig.{service_id}。 如果您填写该参数，系统生成的终端节点服务的名称为{region}.{vpcep_service_name}.{service_id}。 实例创建完成后，可以在实例管理->终端节点管理页面修改该名称。 

        :param vpcep_service_name: The vpcep_service_name of this InstanceCreateReq.
        :type vpcep_service_name: str
        """
        self._vpcep_service_name = vpcep_service_name

    @property
    def ingress_bandwidth_size(self):
        """Gets the ingress_bandwidth_size of this InstanceCreateReq.

        入公网带宽  实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源

        :return: The ingress_bandwidth_size of this InstanceCreateReq.
        :rtype: int
        """
        return self._ingress_bandwidth_size

    @ingress_bandwidth_size.setter
    def ingress_bandwidth_size(self, ingress_bandwidth_size):
        """Sets the ingress_bandwidth_size of this InstanceCreateReq.

        入公网带宽  实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写，绑定后使用者可以通过该入口从公网访问APIG实例中的API等资源

        :param ingress_bandwidth_size: The ingress_bandwidth_size of this InstanceCreateReq.
        :type ingress_bandwidth_size: int
        """
        self._ingress_bandwidth_size = ingress_bandwidth_size

    @property
    def ingress_bandwidth_charging_mode(self):
        """Gets the ingress_bandwidth_charging_mode of this InstanceCreateReq.

        入公网带宽计费类型，实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费

        :return: The ingress_bandwidth_charging_mode of this InstanceCreateReq.
        :rtype: str
        """
        return self._ingress_bandwidth_charging_mode

    @ingress_bandwidth_charging_mode.setter
    def ingress_bandwidth_charging_mode(self, ingress_bandwidth_charging_mode):
        """Sets the ingress_bandwidth_charging_mode of this InstanceCreateReq.

        入公网带宽计费类型，实例需要开启入公网功能，且loadbalancer_provider为elb时需要填写： - bandwidth：按带宽计费 - traffic：按流量计费

        :param ingress_bandwidth_charging_mode: The ingress_bandwidth_charging_mode of this InstanceCreateReq.
        :type ingress_bandwidth_charging_mode: str
        """
        self._ingress_bandwidth_charging_mode = ingress_bandwidth_charging_mode

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
        if not isinstance(other, InstanceCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
