# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterReqV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_dec_project': 'bool',
        'cluster_version': 'str',
        'cluster_name': 'str',
        'cluster_type': 'str',
        'charge_info': 'ChargeInfo',
        'region': 'str',
        'vpc_name': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'components': 'str',
        'availability_zone': 'str',
        'security_groups_id': 'str',
        'auto_create_default_security_group': 'bool',
        'safe_mode': 'str',
        'manager_admin_password': 'str',
        'login_mode': 'str',
        'node_root_password': 'str',
        'node_keypair_name': 'str',
        'enterprise_project_id': 'str',
        'eip_address': 'str',
        'eip_id': 'str',
        'mrs_ecs_default_agency': 'str',
        'template_id': 'str',
        'tags': 'list[Tag]',
        'log_collection': 'int',
        'node_groups': 'list[NodeGroupV2]',
        'bootstrap_scripts': 'list[BootstrapScript]',
        'add_jobs': 'list[AddJobsReqV11]'
    }

    attribute_map = {
        'is_dec_project': 'is_dec_project',
        'cluster_version': 'cluster_version',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type',
        'charge_info': 'charge_info',
        'region': 'region',
        'vpc_name': 'vpc_name',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'components': 'components',
        'availability_zone': 'availability_zone',
        'security_groups_id': 'security_groups_id',
        'auto_create_default_security_group': 'auto_create_default_security_group',
        'safe_mode': 'safe_mode',
        'manager_admin_password': 'manager_admin_password',
        'login_mode': 'login_mode',
        'node_root_password': 'node_root_password',
        'node_keypair_name': 'node_keypair_name',
        'enterprise_project_id': 'enterprise_project_id',
        'eip_address': 'eip_address',
        'eip_id': 'eip_id',
        'mrs_ecs_default_agency': 'mrs_ecs_default_agency',
        'template_id': 'template_id',
        'tags': 'tags',
        'log_collection': 'log_collection',
        'node_groups': 'node_groups',
        'bootstrap_scripts': 'bootstrap_scripts',
        'add_jobs': 'add_jobs'
    }

    def __init__(self, is_dec_project=None, cluster_version=None, cluster_name=None, cluster_type=None, charge_info=None, region=None, vpc_name=None, subnet_id=None, subnet_name=None, components=None, availability_zone=None, security_groups_id=None, auto_create_default_security_group=None, safe_mode=None, manager_admin_password=None, login_mode=None, node_root_password=None, node_keypair_name=None, enterprise_project_id=None, eip_address=None, eip_id=None, mrs_ecs_default_agency=None, template_id=None, tags=None, log_collection=None, node_groups=None, bootstrap_scripts=None, add_jobs=None):
        """CreateClusterReqV2

        The model defined in huaweicloud sdk

        :param is_dec_project: 说明是否为专属云的资源，默认为false。
        :type is_dec_project: bool
        :param cluster_version: 集群版本。例如：MRS 3.1.0。
        :type cluster_version: str
        :param cluster_name: 集群名称，不允许相同。  只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。
        :type cluster_name: str
        :param cluster_type: 集群类型，取值范围： - ANALYSIS：分析集群 - STREAMING：流式集群 - MIXED：混合集群 - CUSTOM：自定义集群，仅MRS 3.x版本支持。
        :type cluster_type: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        :param region: 集群所在区域信息，请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。
        :type region: str
        :param vpc_name: 子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 在“虚拟私有云”页面的列表中即可获取VPC名称。
        :type vpc_name: str
        :param subnet_id: 子网ID。通过VPC管理控制台获取子网ID： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。
        :type subnet_id: str
        :param subnet_name: 子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。
        :type subnet_name: str
        :param components: 组件名称列表，用逗号分隔。支持的组件请参见[获取MRS集群信息](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)页面的“MRS服务支持的组件”内容。
        :type components: str
        :param availability_zone: 可用分区名称，不支持多AZ集群。 可用分区信息请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。
        :type availability_zone: str
        :param security_groups_id: 集群安全组的ID。 - 当该ID为空时MRS后台会自动创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中需要包含一条支持全部协议、全部端口、源地址为指定的管理面节点IP的入方向规则。
        :type security_groups_id: str
        :param auto_create_default_security_group: 是否要创建MRS集群默认安全组，默认为false。 当指定该参数为true，则无论“security_groups_id”参数是否指定，都会为集群创建默认安全组。
        :type auto_create_default_security_group: bool
        :param safe_mode: MRS集群运行模式。 - SIMPLE：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - KERBEROS：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找Manager的管理员分配权限。
        :type safe_mode: str
        :param manager_admin_password: 配置Manager管理员用户的密码。 - 密码长度应在8～26个字符之间。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_&#x3D;+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。
        :type manager_admin_password: str
        :param login_mode: 节点登录方式。 - PASSWORD：密码登录，选择此项时，node_root_password不能为空。 - KEYPAIR：密钥对登录，选择此项时，node_keypair_name不能为空。
        :type login_mode: str
        :param node_root_password: 配置访问集群节点的root密码。 密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_&#x3D;+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。
        :type node_root_password: str
        :param node_keypair_name: 密钥对名称。用户可以使用密钥对方式登录集群节点。
        :type node_keypair_name: str
        :param enterprise_project_id: 企业项目ID。 创建集群时，给集群绑定企业项目ID。 默认设置为0，表示为default企业项目。 获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。
        :type enterprise_project_id: str
        :param eip_address: 与MRS集群绑定的弹性公网IP，可实现使用弹性公网IP访问Manager的目的。该弹性公网IP必须已经创建且与集群在同一区域。
        :type eip_address: str
        :param eip_id: 当“eip_address”配置时，该参数必须配置，用于表示绑定的弹性公网IP的ID。可通过在VPC服务的“网络控制台 &gt; 弹性公网IP和带宽 &gt; 弹性公网IP”页面单击待绑定的弹性公网IP，在基本信息中获取“ID”。
        :type eip_id: str
        :param mrs_ecs_default_agency: 集群节点默认绑定的委托名称，固定为MRS_ECS_DEFAULT_AGENCY。 通过绑定委托，您可以将部分资源共享给ECS或BMS云服务来管理，例如通过配置ECS委托可自动获取AK/SK访问OBS。 MRS_ECS_DEFAULT_AGENCY委托拥有对象存储服务的OBS OperateAccess权限和在集群所在区域拥有CES FullAccess（对开启细粒度策略的用户）、CES Administrator和KMS Administrator权限。
        :type mrs_ecs_default_agency: str
        :param template_id: 当集群类型为CUSTOM时，用于指定节点部署所使用的模板。 - mgmt_control_combined_v2：管控合设模板，管理角色和控制角色共同部署在Master节点中，数据实例合设在同一节点组。该部署方式适用于100个以下的节点，可以减少成本。 - mgmt_control_separated_v2：管控分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例合设在同一节点组。该部署方式适用于100-500个节点，在高并发负载情况下表现更好。 - mgmt_control_data_separated_v2：数据分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例分设在不同节点组。该部署方式适用于500个以上的节点，可以将各组件进一步分开部署，适用于更大的集群规模。
        :type template_id: str
        :param tags: 集群的标签信息。 同一个集群最多能使用10个tag，tag的名称（key）不能重复。
        :type tags: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        :param log_collection: 集群创建失败时，是否收集失败日志。 默认设置为1，此时将创建OBS桶仅用于MRS集群创建失败时的日志收集。 枚举值： - 0：不收集 - 1：收集
        :type log_collection: int
        :param node_groups: 组成集群的节点组信息。
        :type node_groups: list[:class:`huaweicloudsdkmrs.v2.NodeGroupV2`]
        :param bootstrap_scripts: 配置引导操作脚本信息。
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v2.BootstrapScript`]
        :param add_jobs: 创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。
        :type add_jobs: list[:class:`huaweicloudsdkmrs.v2.AddJobsReqV11`]
        """
        
        

        self._is_dec_project = None
        self._cluster_version = None
        self._cluster_name = None
        self._cluster_type = None
        self._charge_info = None
        self._region = None
        self._vpc_name = None
        self._subnet_id = None
        self._subnet_name = None
        self._components = None
        self._availability_zone = None
        self._security_groups_id = None
        self._auto_create_default_security_group = None
        self._safe_mode = None
        self._manager_admin_password = None
        self._login_mode = None
        self._node_root_password = None
        self._node_keypair_name = None
        self._enterprise_project_id = None
        self._eip_address = None
        self._eip_id = None
        self._mrs_ecs_default_agency = None
        self._template_id = None
        self._tags = None
        self._log_collection = None
        self._node_groups = None
        self._bootstrap_scripts = None
        self._add_jobs = None
        self.discriminator = None

        if is_dec_project is not None:
            self.is_dec_project = is_dec_project
        self.cluster_version = cluster_version
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        if charge_info is not None:
            self.charge_info = charge_info
        self.region = region
        self.vpc_name = vpc_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        self.subnet_name = subnet_name
        self.components = components
        self.availability_zone = availability_zone
        if security_groups_id is not None:
            self.security_groups_id = security_groups_id
        if auto_create_default_security_group is not None:
            self.auto_create_default_security_group = auto_create_default_security_group
        self.safe_mode = safe_mode
        self.manager_admin_password = manager_admin_password
        self.login_mode = login_mode
        if node_root_password is not None:
            self.node_root_password = node_root_password
        if node_keypair_name is not None:
            self.node_keypair_name = node_keypair_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if eip_address is not None:
            self.eip_address = eip_address
        if eip_id is not None:
            self.eip_id = eip_id
        if mrs_ecs_default_agency is not None:
            self.mrs_ecs_default_agency = mrs_ecs_default_agency
        if template_id is not None:
            self.template_id = template_id
        if tags is not None:
            self.tags = tags
        if log_collection is not None:
            self.log_collection = log_collection
        self.node_groups = node_groups
        if bootstrap_scripts is not None:
            self.bootstrap_scripts = bootstrap_scripts
        if add_jobs is not None:
            self.add_jobs = add_jobs

    @property
    def is_dec_project(self):
        """Gets the is_dec_project of this CreateClusterReqV2.

        说明是否为专属云的资源，默认为false。

        :return: The is_dec_project of this CreateClusterReqV2.
        :rtype: bool
        """
        return self._is_dec_project

    @is_dec_project.setter
    def is_dec_project(self, is_dec_project):
        """Sets the is_dec_project of this CreateClusterReqV2.

        说明是否为专属云的资源，默认为false。

        :param is_dec_project: The is_dec_project of this CreateClusterReqV2.
        :type is_dec_project: bool
        """
        self._is_dec_project = is_dec_project

    @property
    def cluster_version(self):
        """Gets the cluster_version of this CreateClusterReqV2.

        集群版本。例如：MRS 3.1.0。

        :return: The cluster_version of this CreateClusterReqV2.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """Sets the cluster_version of this CreateClusterReqV2.

        集群版本。例如：MRS 3.1.0。

        :param cluster_version: The cluster_version of this CreateClusterReqV2.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateClusterReqV2.

        集群名称，不允许相同。  只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。

        :return: The cluster_name of this CreateClusterReqV2.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateClusterReqV2.

        集群名称，不允许相同。  只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。

        :param cluster_name: The cluster_name of this CreateClusterReqV2.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """Gets the cluster_type of this CreateClusterReqV2.

        集群类型，取值范围： - ANALYSIS：分析集群 - STREAMING：流式集群 - MIXED：混合集群 - CUSTOM：自定义集群，仅MRS 3.x版本支持。

        :return: The cluster_type of this CreateClusterReqV2.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this CreateClusterReqV2.

        集群类型，取值范围： - ANALYSIS：分析集群 - STREAMING：流式集群 - MIXED：混合集群 - CUSTOM：自定义集群，仅MRS 3.x版本支持。

        :param cluster_type: The cluster_type of this CreateClusterReqV2.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateClusterReqV2.

        :return: The charge_info of this CreateClusterReqV2.
        :rtype: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateClusterReqV2.

        :param charge_info: The charge_info of this CreateClusterReqV2.
        :type charge_info: :class:`huaweicloudsdkmrs.v2.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def region(self):
        """Gets the region of this CreateClusterReqV2.

        集群所在区域信息，请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :return: The region of this CreateClusterReqV2.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateClusterReqV2.

        集群所在区域信息，请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :param region: The region of this CreateClusterReqV2.
        :type region: str
        """
        self._region = region

    @property
    def vpc_name(self):
        """Gets the vpc_name of this CreateClusterReqV2.

        子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 在“虚拟私有云”页面的列表中即可获取VPC名称。

        :return: The vpc_name of this CreateClusterReqV2.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this CreateClusterReqV2.

        子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 在“虚拟私有云”页面的列表中即可获取VPC名称。

        :param vpc_name: The vpc_name of this CreateClusterReqV2.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateClusterReqV2.

        子网ID。通过VPC管理控制台获取子网ID： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。

        :return: The subnet_id of this CreateClusterReqV2.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateClusterReqV2.

        子网ID。通过VPC管理控制台获取子网ID： 1) 登录VPC管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。

        :param subnet_id: The subnet_id of this CreateClusterReqV2.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this CreateClusterReqV2.

        子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。

        :return: The subnet_name of this CreateClusterReqV2.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this CreateClusterReqV2.

        子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。 “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。

        :param subnet_name: The subnet_name of this CreateClusterReqV2.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def components(self):
        """Gets the components of this CreateClusterReqV2.

        组件名称列表，用逗号分隔。支持的组件请参见[获取MRS集群信息](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)页面的“MRS服务支持的组件”内容。

        :return: The components of this CreateClusterReqV2.
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this CreateClusterReqV2.

        组件名称列表，用逗号分隔。支持的组件请参见[获取MRS集群信息](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)页面的“MRS服务支持的组件”内容。

        :param components: The components of this CreateClusterReqV2.
        :type components: str
        """
        self._components = components

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClusterReqV2.

        可用分区名称，不支持多AZ集群。 可用分区信息请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :return: The availability_zone of this CreateClusterReqV2.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClusterReqV2.

        可用分区名称，不支持多AZ集群。 可用分区信息请参见[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :param availability_zone: The availability_zone of this CreateClusterReqV2.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def security_groups_id(self):
        """Gets the security_groups_id of this CreateClusterReqV2.

        集群安全组的ID。 - 当该ID为空时MRS后台会自动创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中需要包含一条支持全部协议、全部端口、源地址为指定的管理面节点IP的入方向规则。

        :return: The security_groups_id of this CreateClusterReqV2.
        :rtype: str
        """
        return self._security_groups_id

    @security_groups_id.setter
    def security_groups_id(self, security_groups_id):
        """Sets the security_groups_id of this CreateClusterReqV2.

        集群安全组的ID。 - 当该ID为空时MRS后台会自动创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中需要包含一条支持全部协议、全部端口、源地址为指定的管理面节点IP的入方向规则。

        :param security_groups_id: The security_groups_id of this CreateClusterReqV2.
        :type security_groups_id: str
        """
        self._security_groups_id = security_groups_id

    @property
    def auto_create_default_security_group(self):
        """Gets the auto_create_default_security_group of this CreateClusterReqV2.

        是否要创建MRS集群默认安全组，默认为false。 当指定该参数为true，则无论“security_groups_id”参数是否指定，都会为集群创建默认安全组。

        :return: The auto_create_default_security_group of this CreateClusterReqV2.
        :rtype: bool
        """
        return self._auto_create_default_security_group

    @auto_create_default_security_group.setter
    def auto_create_default_security_group(self, auto_create_default_security_group):
        """Sets the auto_create_default_security_group of this CreateClusterReqV2.

        是否要创建MRS集群默认安全组，默认为false。 当指定该参数为true，则无论“security_groups_id”参数是否指定，都会为集群创建默认安全组。

        :param auto_create_default_security_group: The auto_create_default_security_group of this CreateClusterReqV2.
        :type auto_create_default_security_group: bool
        """
        self._auto_create_default_security_group = auto_create_default_security_group

    @property
    def safe_mode(self):
        """Gets the safe_mode of this CreateClusterReqV2.

        MRS集群运行模式。 - SIMPLE：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - KERBEROS：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找Manager的管理员分配权限。

        :return: The safe_mode of this CreateClusterReqV2.
        :rtype: str
        """
        return self._safe_mode

    @safe_mode.setter
    def safe_mode(self, safe_mode):
        """Sets the safe_mode of this CreateClusterReqV2.

        MRS集群运行模式。 - SIMPLE：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - KERBEROS：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找Manager的管理员分配权限。

        :param safe_mode: The safe_mode of this CreateClusterReqV2.
        :type safe_mode: str
        """
        self._safe_mode = safe_mode

    @property
    def manager_admin_password(self):
        """Gets the manager_admin_password of this CreateClusterReqV2.

        配置Manager管理员用户的密码。 - 密码长度应在8～26个字符之间。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :return: The manager_admin_password of this CreateClusterReqV2.
        :rtype: str
        """
        return self._manager_admin_password

    @manager_admin_password.setter
    def manager_admin_password(self, manager_admin_password):
        """Sets the manager_admin_password of this CreateClusterReqV2.

        配置Manager管理员用户的密码。 - 密码长度应在8～26个字符之间。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :param manager_admin_password: The manager_admin_password of this CreateClusterReqV2.
        :type manager_admin_password: str
        """
        self._manager_admin_password = manager_admin_password

    @property
    def login_mode(self):
        """Gets the login_mode of this CreateClusterReqV2.

        节点登录方式。 - PASSWORD：密码登录，选择此项时，node_root_password不能为空。 - KEYPAIR：密钥对登录，选择此项时，node_keypair_name不能为空。

        :return: The login_mode of this CreateClusterReqV2.
        :rtype: str
        """
        return self._login_mode

    @login_mode.setter
    def login_mode(self, login_mode):
        """Sets the login_mode of this CreateClusterReqV2.

        节点登录方式。 - PASSWORD：密码登录，选择此项时，node_root_password不能为空。 - KEYPAIR：密钥对登录，选择此项时，node_keypair_name不能为空。

        :param login_mode: The login_mode of this CreateClusterReqV2.
        :type login_mode: str
        """
        self._login_mode = login_mode

    @property
    def node_root_password(self):
        """Gets the node_root_password of this CreateClusterReqV2.

        配置访问集群节点的root密码。 密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :return: The node_root_password of this CreateClusterReqV2.
        :rtype: str
        """
        return self._node_root_password

    @node_root_password.setter
    def node_root_password(self, node_root_password):
        """Sets the node_root_password of this CreateClusterReqV2.

        配置访问集群节点的root密码。 密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含四种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :param node_root_password: The node_root_password of this CreateClusterReqV2.
        :type node_root_password: str
        """
        self._node_root_password = node_root_password

    @property
    def node_keypair_name(self):
        """Gets the node_keypair_name of this CreateClusterReqV2.

        密钥对名称。用户可以使用密钥对方式登录集群节点。

        :return: The node_keypair_name of this CreateClusterReqV2.
        :rtype: str
        """
        return self._node_keypair_name

    @node_keypair_name.setter
    def node_keypair_name(self, node_keypair_name):
        """Sets the node_keypair_name of this CreateClusterReqV2.

        密钥对名称。用户可以使用密钥对方式登录集群节点。

        :param node_keypair_name: The node_keypair_name of this CreateClusterReqV2.
        :type node_keypair_name: str
        """
        self._node_keypair_name = node_keypair_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterReqV2.

        企业项目ID。 创建集群时，给集群绑定企业项目ID。 默认设置为0，表示为default企业项目。 获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this CreateClusterReqV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterReqV2.

        企业项目ID。 创建集群时，给集群绑定企业项目ID。 默认设置为0，表示为default企业项目。 获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterReqV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def eip_address(self):
        """Gets the eip_address of this CreateClusterReqV2.

        与MRS集群绑定的弹性公网IP，可实现使用弹性公网IP访问Manager的目的。该弹性公网IP必须已经创建且与集群在同一区域。

        :return: The eip_address of this CreateClusterReqV2.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this CreateClusterReqV2.

        与MRS集群绑定的弹性公网IP，可实现使用弹性公网IP访问Manager的目的。该弹性公网IP必须已经创建且与集群在同一区域。

        :param eip_address: The eip_address of this CreateClusterReqV2.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def eip_id(self):
        """Gets the eip_id of this CreateClusterReqV2.

        当“eip_address”配置时，该参数必须配置，用于表示绑定的弹性公网IP的ID。可通过在VPC服务的“网络控制台 > 弹性公网IP和带宽 > 弹性公网IP”页面单击待绑定的弹性公网IP，在基本信息中获取“ID”。

        :return: The eip_id of this CreateClusterReqV2.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this CreateClusterReqV2.

        当“eip_address”配置时，该参数必须配置，用于表示绑定的弹性公网IP的ID。可通过在VPC服务的“网络控制台 > 弹性公网IP和带宽 > 弹性公网IP”页面单击待绑定的弹性公网IP，在基本信息中获取“ID”。

        :param eip_id: The eip_id of this CreateClusterReqV2.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def mrs_ecs_default_agency(self):
        """Gets the mrs_ecs_default_agency of this CreateClusterReqV2.

        集群节点默认绑定的委托名称，固定为MRS_ECS_DEFAULT_AGENCY。 通过绑定委托，您可以将部分资源共享给ECS或BMS云服务来管理，例如通过配置ECS委托可自动获取AK/SK访问OBS。 MRS_ECS_DEFAULT_AGENCY委托拥有对象存储服务的OBS OperateAccess权限和在集群所在区域拥有CES FullAccess（对开启细粒度策略的用户）、CES Administrator和KMS Administrator权限。

        :return: The mrs_ecs_default_agency of this CreateClusterReqV2.
        :rtype: str
        """
        return self._mrs_ecs_default_agency

    @mrs_ecs_default_agency.setter
    def mrs_ecs_default_agency(self, mrs_ecs_default_agency):
        """Sets the mrs_ecs_default_agency of this CreateClusterReqV2.

        集群节点默认绑定的委托名称，固定为MRS_ECS_DEFAULT_AGENCY。 通过绑定委托，您可以将部分资源共享给ECS或BMS云服务来管理，例如通过配置ECS委托可自动获取AK/SK访问OBS。 MRS_ECS_DEFAULT_AGENCY委托拥有对象存储服务的OBS OperateAccess权限和在集群所在区域拥有CES FullAccess（对开启细粒度策略的用户）、CES Administrator和KMS Administrator权限。

        :param mrs_ecs_default_agency: The mrs_ecs_default_agency of this CreateClusterReqV2.
        :type mrs_ecs_default_agency: str
        """
        self._mrs_ecs_default_agency = mrs_ecs_default_agency

    @property
    def template_id(self):
        """Gets the template_id of this CreateClusterReqV2.

        当集群类型为CUSTOM时，用于指定节点部署所使用的模板。 - mgmt_control_combined_v2：管控合设模板，管理角色和控制角色共同部署在Master节点中，数据实例合设在同一节点组。该部署方式适用于100个以下的节点，可以减少成本。 - mgmt_control_separated_v2：管控分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例合设在同一节点组。该部署方式适用于100-500个节点，在高并发负载情况下表现更好。 - mgmt_control_data_separated_v2：数据分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例分设在不同节点组。该部署方式适用于500个以上的节点，可以将各组件进一步分开部署，适用于更大的集群规模。

        :return: The template_id of this CreateClusterReqV2.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateClusterReqV2.

        当集群类型为CUSTOM时，用于指定节点部署所使用的模板。 - mgmt_control_combined_v2：管控合设模板，管理角色和控制角色共同部署在Master节点中，数据实例合设在同一节点组。该部署方式适用于100个以下的节点，可以减少成本。 - mgmt_control_separated_v2：管控分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例合设在同一节点组。该部署方式适用于100-500个节点，在高并发负载情况下表现更好。 - mgmt_control_data_separated_v2：数据分设模板，管理角色和控制角色分别部署在不同的Master节点中，数据实例分设在不同节点组。该部署方式适用于500个以上的节点，可以将各组件进一步分开部署，适用于更大的集群规模。

        :param template_id: The template_id of this CreateClusterReqV2.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def tags(self):
        """Gets the tags of this CreateClusterReqV2.

        集群的标签信息。 同一个集群最多能使用10个tag，tag的名称（key）不能重复。

        :return: The tags of this CreateClusterReqV2.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClusterReqV2.

        集群的标签信息。 同一个集群最多能使用10个tag，tag的名称（key）不能重复。

        :param tags: The tags of this CreateClusterReqV2.
        :type tags: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        """
        self._tags = tags

    @property
    def log_collection(self):
        """Gets the log_collection of this CreateClusterReqV2.

        集群创建失败时，是否收集失败日志。 默认设置为1，此时将创建OBS桶仅用于MRS集群创建失败时的日志收集。 枚举值： - 0：不收集 - 1：收集

        :return: The log_collection of this CreateClusterReqV2.
        :rtype: int
        """
        return self._log_collection

    @log_collection.setter
    def log_collection(self, log_collection):
        """Sets the log_collection of this CreateClusterReqV2.

        集群创建失败时，是否收集失败日志。 默认设置为1，此时将创建OBS桶仅用于MRS集群创建失败时的日志收集。 枚举值： - 0：不收集 - 1：收集

        :param log_collection: The log_collection of this CreateClusterReqV2.
        :type log_collection: int
        """
        self._log_collection = log_collection

    @property
    def node_groups(self):
        """Gets the node_groups of this CreateClusterReqV2.

        组成集群的节点组信息。

        :return: The node_groups of this CreateClusterReqV2.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.NodeGroupV2`]
        """
        return self._node_groups

    @node_groups.setter
    def node_groups(self, node_groups):
        """Sets the node_groups of this CreateClusterReqV2.

        组成集群的节点组信息。

        :param node_groups: The node_groups of this CreateClusterReqV2.
        :type node_groups: list[:class:`huaweicloudsdkmrs.v2.NodeGroupV2`]
        """
        self._node_groups = node_groups

    @property
    def bootstrap_scripts(self):
        """Gets the bootstrap_scripts of this CreateClusterReqV2.

        配置引导操作脚本信息。

        :return: The bootstrap_scripts of this CreateClusterReqV2.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.BootstrapScript`]
        """
        return self._bootstrap_scripts

    @bootstrap_scripts.setter
    def bootstrap_scripts(self, bootstrap_scripts):
        """Sets the bootstrap_scripts of this CreateClusterReqV2.

        配置引导操作脚本信息。

        :param bootstrap_scripts: The bootstrap_scripts of this CreateClusterReqV2.
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v2.BootstrapScript`]
        """
        self._bootstrap_scripts = bootstrap_scripts

    @property
    def add_jobs(self):
        """Gets the add_jobs of this CreateClusterReqV2.

        创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。

        :return: The add_jobs of this CreateClusterReqV2.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.AddJobsReqV11`]
        """
        return self._add_jobs

    @add_jobs.setter
    def add_jobs(self, add_jobs):
        """Sets the add_jobs of this CreateClusterReqV2.

        创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。

        :param add_jobs: The add_jobs of this CreateClusterReqV2.
        :type add_jobs: list[:class:`huaweicloudsdkmrs.v2.AddJobsReqV11`]
        """
        self._add_jobs = add_jobs

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
        if not isinstance(other, CreateClusterReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
