# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterReqV11:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_version': 'str',
        'cluster_name': 'str',
        'master_node_num': 'int',
        'core_node_num': 'int',
        'billing_type': 'int',
        'data_center': 'str',
        'vpc': 'str',
        'master_node_size': 'str',
        'core_node_size': 'str',
        'component_list': 'list[ComponentAmbV11]',
        'available_zone_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'security_groups_id': 'str',
        'add_jobs': 'list[AddJobsReqV11]',
        'volume_size': 'int',
        'volume_type': 'str',
        'master_data_volume_type': 'str',
        'master_data_volume_size': 'int',
        'master_data_volume_count': 'int',
        'core_data_volume_type': 'str',
        'core_data_volume_size': 'int',
        'core_data_volume_count': 'int',
        'task_node_groups': 'list[TaskNodeGroup]',
        'bootstrap_scripts': 'list[BootstrapScript]',
        'node_public_cert_name': 'str',
        'cluster_admin_secret': 'str',
        'cluster_master_secret': 'str',
        'safe_mode': 'int',
        'cluster_type': 'int',
        'log_collection': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'login_mode': 'int',
        'node_groups': 'list[NodeGroupV11]'
    }

    attribute_map = {
        'cluster_version': 'cluster_version',
        'cluster_name': 'cluster_name',
        'master_node_num': 'master_node_num',
        'core_node_num': 'core_node_num',
        'billing_type': 'billing_type',
        'data_center': 'data_center',
        'vpc': 'vpc',
        'master_node_size': 'master_node_size',
        'core_node_size': 'core_node_size',
        'component_list': 'component_list',
        'available_zone_id': 'available_zone_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'security_groups_id': 'security_groups_id',
        'add_jobs': 'add_jobs',
        'volume_size': 'volume_size',
        'volume_type': 'volume_type',
        'master_data_volume_type': 'master_data_volume_type',
        'master_data_volume_size': 'master_data_volume_size',
        'master_data_volume_count': 'master_data_volume_count',
        'core_data_volume_type': 'core_data_volume_type',
        'core_data_volume_size': 'core_data_volume_size',
        'core_data_volume_count': 'core_data_volume_count',
        'task_node_groups': 'task_node_groups',
        'bootstrap_scripts': 'bootstrap_scripts',
        'node_public_cert_name': 'node_public_cert_name',
        'cluster_admin_secret': 'cluster_admin_secret',
        'cluster_master_secret': 'cluster_master_secret',
        'safe_mode': 'safe_mode',
        'cluster_type': 'cluster_type',
        'log_collection': 'log_collection',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'login_mode': 'login_mode',
        'node_groups': 'node_groups'
    }

    def __init__(self, cluster_version=None, cluster_name=None, master_node_num=None, core_node_num=None, billing_type=None, data_center=None, vpc=None, master_node_size=None, core_node_size=None, component_list=None, available_zone_id=None, vpc_id=None, subnet_id=None, subnet_name=None, security_groups_id=None, add_jobs=None, volume_size=None, volume_type=None, master_data_volume_type=None, master_data_volume_size=None, master_data_volume_count=None, core_data_volume_type=None, core_data_volume_size=None, core_data_volume_count=None, task_node_groups=None, bootstrap_scripts=None, node_public_cert_name=None, cluster_admin_secret=None, cluster_master_secret=None, safe_mode=None, cluster_type=None, log_collection=None, enterprise_project_id=None, tags=None, login_mode=None, node_groups=None):
        r"""CreateClusterReqV11

        The model defined in huaweicloud sdk

        :param cluster_version: 集群版本。 例如：MRS 3.1.0。
        :type cluster_version: str
        :param cluster_name: 集群名称，不允许相同。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。
        :type cluster_name: str
        :param master_node_num: Master节点数量。启用集群高可用功能时配置为2，不启用集群高可用功能时配置为1。MRS 3.x版本暂时不支持该参数配置为1。
        :type master_node_num: int
        :param core_node_num: Core节点数量。  取值范围：[1～500]  Core节点默认的最大值为500，如果用户需要的Core节点数大于500，请申请扩大配额。
        :type core_node_num: int
        :param billing_type: 集群的计费模式。  12：表示按需计费。接口调用仅支持创建按需计费集群。
        :type billing_type: int
        :param data_center: 集群区域信息，请参见[终端节点及区域](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。
        :type data_center: str
        :param vpc: 子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。  在“虚拟私有云”页面的列表中即可获取VPC名称。
        :type vpc: str
        :param master_node_size: Master节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。
        :type master_node_size: str
        :param core_node_size: Core节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。
        :type core_node_size: str
        :param component_list: 服务组件安装列表信息。
        :type component_list: list[:class:`huaweicloudsdkmrs.v1.ComponentAmbV11`]
        :param available_zone_id: 可用分区ID。  - 华北-北京一可用区1（cn-north-1a）：ae04cf9d61544df3806a3feeb401b204 - 华北-北京一可用区2（cn-north-1b）：d573142f24894ef3bd3664de068b44b0 - 华东-上海二可用区1（cn-east-2a）：72d50cedc49846b9b42c21495f38d81c - 华东-上海二可用区2（cn-east-2b）：38b0f7a602344246bcb0da47b5d548e7 - 华东-上海二可用区3（cn-east-2c）：5547fd6bf8f84bb5a7f9db062ad3d015 - 华南-广州可用区1（cn-south-1a）：34f5ff4865cf4ed6b270f15382ebdec5 - 华南-广州可用区2（cn-south-2b）：043c7e39ecb347a08dc8fcb6c35a274e - 华南-广州可用区3（cn-south-1c）：af1687643e8c4ec1b34b688e4e3b8901 - 华北-北京四可用区1（cn-north-4a）：effdcbc7d4d64a02aa1fa26b42f56533 - 华北-北京四可用区2（cn-north-4b）：a0865121f83b41cbafce65930a22a6e8 - 华北-北京四可用区3（cn-north-4c）：2dcb154ac2724a6d92e9bcc859657c1e
        :type available_zone_id: str
        :param vpc_id: 子网所在VPC ID。 通过VPC管理控制台获取ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。   在“虚拟私有云”页面的列表中即可获取VPC ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。通过VPC管理控制台获取子网ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。
        :type subnet_id: str
        :param subnet_name: 子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。
        :type subnet_name: str
        :param security_groups_id: 集群安全组的ID。 - 当该ID为空时MRS后台会自己创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中包含一条全部协议，全部端口，源地址为指定的管理面节点IP的入方向规则。
        :type security_groups_id: str
        :param add_jobs: 创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。
        :type add_jobs: list[:class:`huaweicloudsdkmrs.v1.AddJobsReqV11`]
        :param volume_size: Master和Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。可以根据如下应用场景合理选择磁盘存储空间大小： - 数据存储和计算分离，数据存储在OBS系统中，集群费用相对较低，计算性能不高，并且集群随时可以删除，建议数据计算不频繁场景下使用。 - 数据存储和计算不分离，数据存储在HDFS中，集群费用相对较高，计算性能高，集群需要长期存在，建议数据计算频繁场景下使用。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。 不建议使用该参数，详情请参考volume_type参数的说明。
        :type volume_size: int
        :param volume_type: Master和Core节点的磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。磁盘参数可以使用volume_type和volume_size表示，也可以使用多磁盘相关的参数表示。volume_type和volume_size这两个参数如果与多磁盘参数同时出现，系统优先读取volume_type和volume_size参数。建议使用多磁盘参数。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD
        :type volume_type: str
        :param master_data_volume_type: 该参数为多磁盘参数，表示Master节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。
        :type master_data_volume_type: str
        :param master_data_volume_size: 该参数为多磁盘参数，表示Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。
        :type master_data_volume_size: int
        :param master_data_volume_count: 该参数为多磁盘参数，表示Master节点数据磁盘个数。取值只能是1。
        :type master_data_volume_count: int
        :param core_data_volume_type: 该参数为多磁盘参数，表示Core节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。
        :type core_data_volume_type: str
        :param core_data_volume_size: 该参数为多磁盘参数，表示Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。
        :type core_data_volume_size: int
        :param core_data_volume_count: 该参数为多磁盘参数，表示Core节点数据磁盘个数。 取值范围：1～20
        :type core_data_volume_count: int
        :param task_node_groups: Task节点列表信息。
        :type task_node_groups: list[:class:`huaweicloudsdkmrs.v1.TaskNodeGroup`]
        :param bootstrap_scripts: 配置引导操作脚本信息。
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        :param node_public_cert_name: 密钥对名称。用户可以使用密钥对方式登录集群节点。当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。
        :type node_public_cert_name: str
        :param cluster_admin_secret: 配置MRS Manager管理员用户的密码。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合     - 至少一个小写字母     - 至少一个大写字母     - 至少一个数字     - 至少一个特殊字符：!@$%^-_&#x3D;+[{}]:,./?
        :type cluster_admin_secret: str
        :param cluster_master_secret: 配置访问集群节点的root密码。当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。  密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含4种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_&#x3D;+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。
        :type cluster_master_secret: str
        :param safe_mode: MRS集群运行模式。 - 0：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - 1：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找MRS Manager的管理员分配权限。
        :type safe_mode: int
        :param cluster_type: 集群类型。  默认值为0：分析集群。  说明：暂不支持通过接口方式创建混合集群。  枚举值： - 0：分析集群 - 1：流式集群
        :type cluster_type: int
        :param log_collection: 集群创建失败时，是否收集失败日志。  默认设置为1，将创建OBS桶仅用于MRS集群创建失败时的日志收集。  枚举值： - 0：不收集 - 1：收集
        :type log_collection: int
        :param enterprise_project_id: 企业项目ID。  创建集群时，给集群绑定企业项目ID。  默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。
        :type enterprise_project_id: str
        :param tags: 集群的标签信息。  同一个集群最多能使用10个tag，tag的名称（key）不能重复 标签的键/值不能包含“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\”,“,”,“|”,“/”。
        :type tags: list[:class:`huaweicloudsdkmrs.v1.Tag`]
        :param login_mode: 集群登录方式。默认设置为1。  - 当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。 - 当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。  枚举值： - 0：密码方式 - 1：密钥对方式
        :type login_mode: int
        :param node_groups: 节点列表信息。  说明：如下参数和该参数任选一组进行配置即可。  master_node_num、master_node_size、core_node_num、core_node_size、master_data_volume_type、master_data_volume_size、master_data_volume_count、core_data_volume_type、core_data_volume_size、core_data_volume_count、volume_type、volume_size、task_node_groups。
        :type node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV11`]
        """
        
        

        self._cluster_version = None
        self._cluster_name = None
        self._master_node_num = None
        self._core_node_num = None
        self._billing_type = None
        self._data_center = None
        self._vpc = None
        self._master_node_size = None
        self._core_node_size = None
        self._component_list = None
        self._available_zone_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._subnet_name = None
        self._security_groups_id = None
        self._add_jobs = None
        self._volume_size = None
        self._volume_type = None
        self._master_data_volume_type = None
        self._master_data_volume_size = None
        self._master_data_volume_count = None
        self._core_data_volume_type = None
        self._core_data_volume_size = None
        self._core_data_volume_count = None
        self._task_node_groups = None
        self._bootstrap_scripts = None
        self._node_public_cert_name = None
        self._cluster_admin_secret = None
        self._cluster_master_secret = None
        self._safe_mode = None
        self._cluster_type = None
        self._log_collection = None
        self._enterprise_project_id = None
        self._tags = None
        self._login_mode = None
        self._node_groups = None
        self.discriminator = None

        self.cluster_version = cluster_version
        self.cluster_name = cluster_name
        if master_node_num is not None:
            self.master_node_num = master_node_num
        if core_node_num is not None:
            self.core_node_num = core_node_num
        self.billing_type = billing_type
        self.data_center = data_center
        self.vpc = vpc
        if master_node_size is not None:
            self.master_node_size = master_node_size
        if core_node_size is not None:
            self.core_node_size = core_node_size
        self.component_list = component_list
        self.available_zone_id = available_zone_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.subnet_name = subnet_name
        if security_groups_id is not None:
            self.security_groups_id = security_groups_id
        if add_jobs is not None:
            self.add_jobs = add_jobs
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_type is not None:
            self.volume_type = volume_type
        if master_data_volume_type is not None:
            self.master_data_volume_type = master_data_volume_type
        if master_data_volume_size is not None:
            self.master_data_volume_size = master_data_volume_size
        if master_data_volume_count is not None:
            self.master_data_volume_count = master_data_volume_count
        if core_data_volume_type is not None:
            self.core_data_volume_type = core_data_volume_type
        if core_data_volume_size is not None:
            self.core_data_volume_size = core_data_volume_size
        if core_data_volume_count is not None:
            self.core_data_volume_count = core_data_volume_count
        if task_node_groups is not None:
            self.task_node_groups = task_node_groups
        if bootstrap_scripts is not None:
            self.bootstrap_scripts = bootstrap_scripts
        if node_public_cert_name is not None:
            self.node_public_cert_name = node_public_cert_name
        if cluster_admin_secret is not None:
            self.cluster_admin_secret = cluster_admin_secret
        if cluster_master_secret is not None:
            self.cluster_master_secret = cluster_master_secret
        self.safe_mode = safe_mode
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if log_collection is not None:
            self.log_collection = log_collection
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if login_mode is not None:
            self.login_mode = login_mode
        if node_groups is not None:
            self.node_groups = node_groups

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this CreateClusterReqV11.

        集群版本。 例如：MRS 3.1.0。

        :return: The cluster_version of this CreateClusterReqV11.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this CreateClusterReqV11.

        集群版本。 例如：MRS 3.1.0。

        :param cluster_version: The cluster_version of this CreateClusterReqV11.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateClusterReqV11.

        集群名称，不允许相同。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。

        :return: The cluster_name of this CreateClusterReqV11.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateClusterReqV11.

        集群名称，不允许相同。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。

        :param cluster_name: The cluster_name of this CreateClusterReqV11.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def master_node_num(self):
        r"""Gets the master_node_num of this CreateClusterReqV11.

        Master节点数量。启用集群高可用功能时配置为2，不启用集群高可用功能时配置为1。MRS 3.x版本暂时不支持该参数配置为1。

        :return: The master_node_num of this CreateClusterReqV11.
        :rtype: int
        """
        return self._master_node_num

    @master_node_num.setter
    def master_node_num(self, master_node_num):
        r"""Sets the master_node_num of this CreateClusterReqV11.

        Master节点数量。启用集群高可用功能时配置为2，不启用集群高可用功能时配置为1。MRS 3.x版本暂时不支持该参数配置为1。

        :param master_node_num: The master_node_num of this CreateClusterReqV11.
        :type master_node_num: int
        """
        self._master_node_num = master_node_num

    @property
    def core_node_num(self):
        r"""Gets the core_node_num of this CreateClusterReqV11.

        Core节点数量。  取值范围：[1～500]  Core节点默认的最大值为500，如果用户需要的Core节点数大于500，请申请扩大配额。

        :return: The core_node_num of this CreateClusterReqV11.
        :rtype: int
        """
        return self._core_node_num

    @core_node_num.setter
    def core_node_num(self, core_node_num):
        r"""Sets the core_node_num of this CreateClusterReqV11.

        Core节点数量。  取值范围：[1～500]  Core节点默认的最大值为500，如果用户需要的Core节点数大于500，请申请扩大配额。

        :param core_node_num: The core_node_num of this CreateClusterReqV11.
        :type core_node_num: int
        """
        self._core_node_num = core_node_num

    @property
    def billing_type(self):
        r"""Gets the billing_type of this CreateClusterReqV11.

        集群的计费模式。  12：表示按需计费。接口调用仅支持创建按需计费集群。

        :return: The billing_type of this CreateClusterReqV11.
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        r"""Sets the billing_type of this CreateClusterReqV11.

        集群的计费模式。  12：表示按需计费。接口调用仅支持创建按需计费集群。

        :param billing_type: The billing_type of this CreateClusterReqV11.
        :type billing_type: int
        """
        self._billing_type = billing_type

    @property
    def data_center(self):
        r"""Gets the data_center of this CreateClusterReqV11.

        集群区域信息，请参见[终端节点及区域](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :return: The data_center of this CreateClusterReqV11.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this CreateClusterReqV11.

        集群区域信息，请参见[终端节点及区域](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :param data_center: The data_center of this CreateClusterReqV11.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def vpc(self):
        r"""Gets the vpc of this CreateClusterReqV11.

        子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。  在“虚拟私有云”页面的列表中即可获取VPC名称。

        :return: The vpc of this CreateClusterReqV11.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this CreateClusterReqV11.

        子网所在VPC名称。 通过VPC管理控制台获取名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。  在“虚拟私有云”页面的列表中即可获取VPC名称。

        :param vpc: The vpc of this CreateClusterReqV11.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def master_node_size(self):
        r"""Gets the master_node_size of this CreateClusterReqV11.

        Master节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :return: The master_node_size of this CreateClusterReqV11.
        :rtype: str
        """
        return self._master_node_size

    @master_node_size.setter
    def master_node_size(self, master_node_size):
        r"""Sets the master_node_size of this CreateClusterReqV11.

        Master节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :param master_node_size: The master_node_size of this CreateClusterReqV11.
        :type master_node_size: str
        """
        self._master_node_size = master_node_size

    @property
    def core_node_size(self):
        r"""Gets the core_node_size of this CreateClusterReqV11.

        Core节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :return: The core_node_size of this CreateClusterReqV11.
        :rtype: str
        """
        return self._core_node_size

    @core_node_size.setter
    def core_node_size(self, core_node_size):
        r"""Sets the core_node_size of this CreateClusterReqV11.

        Core节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :param core_node_size: The core_node_size of this CreateClusterReqV11.
        :type core_node_size: str
        """
        self._core_node_size = core_node_size

    @property
    def component_list(self):
        r"""Gets the component_list of this CreateClusterReqV11.

        服务组件安装列表信息。

        :return: The component_list of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.ComponentAmbV11`]
        """
        return self._component_list

    @component_list.setter
    def component_list(self, component_list):
        r"""Sets the component_list of this CreateClusterReqV11.

        服务组件安装列表信息。

        :param component_list: The component_list of this CreateClusterReqV11.
        :type component_list: list[:class:`huaweicloudsdkmrs.v1.ComponentAmbV11`]
        """
        self._component_list = component_list

    @property
    def available_zone_id(self):
        r"""Gets the available_zone_id of this CreateClusterReqV11.

        可用分区ID。  - 华北-北京一可用区1（cn-north-1a）：ae04cf9d61544df3806a3feeb401b204 - 华北-北京一可用区2（cn-north-1b）：d573142f24894ef3bd3664de068b44b0 - 华东-上海二可用区1（cn-east-2a）：72d50cedc49846b9b42c21495f38d81c - 华东-上海二可用区2（cn-east-2b）：38b0f7a602344246bcb0da47b5d548e7 - 华东-上海二可用区3（cn-east-2c）：5547fd6bf8f84bb5a7f9db062ad3d015 - 华南-广州可用区1（cn-south-1a）：34f5ff4865cf4ed6b270f15382ebdec5 - 华南-广州可用区2（cn-south-2b）：043c7e39ecb347a08dc8fcb6c35a274e - 华南-广州可用区3（cn-south-1c）：af1687643e8c4ec1b34b688e4e3b8901 - 华北-北京四可用区1（cn-north-4a）：effdcbc7d4d64a02aa1fa26b42f56533 - 华北-北京四可用区2（cn-north-4b）：a0865121f83b41cbafce65930a22a6e8 - 华北-北京四可用区3（cn-north-4c）：2dcb154ac2724a6d92e9bcc859657c1e

        :return: The available_zone_id of this CreateClusterReqV11.
        :rtype: str
        """
        return self._available_zone_id

    @available_zone_id.setter
    def available_zone_id(self, available_zone_id):
        r"""Sets the available_zone_id of this CreateClusterReqV11.

        可用分区ID。  - 华北-北京一可用区1（cn-north-1a）：ae04cf9d61544df3806a3feeb401b204 - 华北-北京一可用区2（cn-north-1b）：d573142f24894ef3bd3664de068b44b0 - 华东-上海二可用区1（cn-east-2a）：72d50cedc49846b9b42c21495f38d81c - 华东-上海二可用区2（cn-east-2b）：38b0f7a602344246bcb0da47b5d548e7 - 华东-上海二可用区3（cn-east-2c）：5547fd6bf8f84bb5a7f9db062ad3d015 - 华南-广州可用区1（cn-south-1a）：34f5ff4865cf4ed6b270f15382ebdec5 - 华南-广州可用区2（cn-south-2b）：043c7e39ecb347a08dc8fcb6c35a274e - 华南-广州可用区3（cn-south-1c）：af1687643e8c4ec1b34b688e4e3b8901 - 华北-北京四可用区1（cn-north-4a）：effdcbc7d4d64a02aa1fa26b42f56533 - 华北-北京四可用区2（cn-north-4b）：a0865121f83b41cbafce65930a22a6e8 - 华北-北京四可用区3（cn-north-4c）：2dcb154ac2724a6d92e9bcc859657c1e

        :param available_zone_id: The available_zone_id of this CreateClusterReqV11.
        :type available_zone_id: str
        """
        self._available_zone_id = available_zone_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateClusterReqV11.

        子网所在VPC ID。 通过VPC管理控制台获取ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。   在“虚拟私有云”页面的列表中即可获取VPC ID。

        :return: The vpc_id of this CreateClusterReqV11.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateClusterReqV11.

        子网所在VPC ID。 通过VPC管理控制台获取ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。   在“虚拟私有云”页面的列表中即可获取VPC ID。

        :param vpc_id: The vpc_id of this CreateClusterReqV11.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateClusterReqV11.

        子网ID。通过VPC管理控制台获取子网ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。

        :return: The subnet_id of this CreateClusterReqV11.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateClusterReqV11.

        子网ID。通过VPC管理控制台获取子网ID： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网。 4) 单击对应子网名称，获取“网络ID”。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。推荐使用“subnet_id”。

        :param subnet_id: The subnet_id of this CreateClusterReqV11.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this CreateClusterReqV11.

        子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。

        :return: The subnet_name of this CreateClusterReqV11.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this CreateClusterReqV11.

        子网名称。 通过VPC管理控制台获取子网名称： 1) 登录管理控制台。 2) 单击“虚拟私有云”，从左侧列表选择虚拟私有云。 3) 单击对应虚拟私有云所在行的“子网个数”查看子网，获取子网名称。  “subnet_id”和“subnet_name”必须至少填写一个，当这两个参数同时配置但是不匹配同一个子网时，集群会创建失败，请仔细填写参数。当仅填写“subnet_name”一个参数且VPC下存在同名子网时，创建集群时以VPC平台第一个名称的子网为准。推荐使用“subnet_id”。

        :param subnet_name: The subnet_name of this CreateClusterReqV11.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def security_groups_id(self):
        r"""Gets the security_groups_id of this CreateClusterReqV11.

        集群安全组的ID。 - 当该ID为空时MRS后台会自己创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中包含一条全部协议，全部端口，源地址为指定的管理面节点IP的入方向规则。

        :return: The security_groups_id of this CreateClusterReqV11.
        :rtype: str
        """
        return self._security_groups_id

    @security_groups_id.setter
    def security_groups_id(self, security_groups_id):
        r"""Sets the security_groups_id of this CreateClusterReqV11.

        集群安全组的ID。 - 当该ID为空时MRS后台会自己创建安全组，自动创建的安全组名称以mrs_{cluster_name}开头。 - 当该ID不为空时，表示使用固定安全组来创建集群，传入的ID必须是当前租户中包含的安全组ID，且该安全组中包含一条全部协议，全部端口，源地址为指定的管理面节点IP的入方向规则。

        :param security_groups_id: The security_groups_id of this CreateClusterReqV11.
        :type security_groups_id: str
        """
        self._security_groups_id = security_groups_id

    @property
    def add_jobs(self):
        r"""Gets the add_jobs of this CreateClusterReqV11.

        创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。

        :return: The add_jobs of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.AddJobsReqV11`]
        """
        return self._add_jobs

    @add_jobs.setter
    def add_jobs(self, add_jobs):
        r"""Sets the add_jobs of this CreateClusterReqV11.

        创建集群时可同时提交作业，当前版本暂时只支持新增一个作业。

        :param add_jobs: The add_jobs of this CreateClusterReqV11.
        :type add_jobs: list[:class:`huaweicloudsdkmrs.v1.AddJobsReqV11`]
        """
        self._add_jobs = add_jobs

    @property
    def volume_size(self):
        r"""Gets the volume_size of this CreateClusterReqV11.

        Master和Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。可以根据如下应用场景合理选择磁盘存储空间大小： - 数据存储和计算分离，数据存储在OBS系统中，集群费用相对较低，计算性能不高，并且集群随时可以删除，建议数据计算不频繁场景下使用。 - 数据存储和计算不分离，数据存储在HDFS中，集群费用相对较高，计算性能高，集群需要长期存在，建议数据计算频繁场景下使用。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。 不建议使用该参数，详情请参考volume_type参数的说明。

        :return: The volume_size of this CreateClusterReqV11.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this CreateClusterReqV11.

        Master和Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。可以根据如下应用场景合理选择磁盘存储空间大小： - 数据存储和计算分离，数据存储在OBS系统中，集群费用相对较低，计算性能不高，并且集群随时可以删除，建议数据计算不频繁场景下使用。 - 数据存储和计算不分离，数据存储在HDFS中，集群费用相对较高，计算性能高，集群需要长期存在，建议数据计算频繁场景下使用。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。 不建议使用该参数，详情请参考volume_type参数的说明。

        :param volume_size: The volume_size of this CreateClusterReqV11.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def volume_type(self):
        r"""Gets the volume_type of this CreateClusterReqV11.

        Master和Core节点的磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。磁盘参数可以使用volume_type和volume_size表示，也可以使用多磁盘相关的参数表示。volume_type和volume_size这两个参数如果与多磁盘参数同时出现，系统优先读取volume_type和volume_size参数。建议使用多磁盘参数。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :return: The volume_type of this CreateClusterReqV11.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this CreateClusterReqV11.

        Master和Core节点的磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。磁盘参数可以使用volume_type和volume_size表示，也可以使用多磁盘相关的参数表示。volume_type和volume_size这两个参数如果与多磁盘参数同时出现，系统优先读取volume_type和volume_size参数。建议使用多磁盘参数。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :param volume_type: The volume_type of this CreateClusterReqV11.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def master_data_volume_type(self):
        r"""Gets the master_data_volume_type of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。

        :return: The master_data_volume_type of this CreateClusterReqV11.
        :rtype: str
        """
        return self._master_data_volume_type

    @master_data_volume_type.setter
    def master_data_volume_type(self, master_data_volume_type):
        r"""Sets the master_data_volume_type of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。

        :param master_data_volume_type: The master_data_volume_type of this CreateClusterReqV11.
        :type master_data_volume_type: str
        """
        self._master_data_volume_type = master_data_volume_type

    @property
    def master_data_volume_size(self):
        r"""Gets the master_data_volume_size of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :return: The master_data_volume_size of this CreateClusterReqV11.
        :rtype: int
        """
        return self._master_data_volume_size

    @master_data_volume_size.setter
    def master_data_volume_size(self, master_data_volume_size):
        r"""Sets the master_data_volume_size of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :param master_data_volume_size: The master_data_volume_size of this CreateClusterReqV11.
        :type master_data_volume_size: int
        """
        self._master_data_volume_size = master_data_volume_size

    @property
    def master_data_volume_count(self):
        r"""Gets the master_data_volume_count of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘个数。取值只能是1。

        :return: The master_data_volume_count of this CreateClusterReqV11.
        :rtype: int
        """
        return self._master_data_volume_count

    @master_data_volume_count.setter
    def master_data_volume_count(self, master_data_volume_count):
        r"""Sets the master_data_volume_count of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Master节点数据磁盘个数。取值只能是1。

        :param master_data_volume_count: The master_data_volume_count of this CreateClusterReqV11.
        :type master_data_volume_count: int
        """
        self._master_data_volume_count = master_data_volume_count

    @property
    def core_data_volume_type(self):
        r"""Gets the core_data_volume_type of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。

        :return: The core_data_volume_type of this CreateClusterReqV11.
        :rtype: str
        """
        return self._core_data_volume_type

    @core_data_volume_type.setter
    def core_data_volume_type(self, core_data_volume_type):
        r"""Sets the core_data_volume_type of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘存储类别，目前支持SATA、SAS、SSD和GPSSD。

        :param core_data_volume_type: The core_data_volume_type of this CreateClusterReqV11.
        :type core_data_volume_type: str
        """
        self._core_data_volume_type = core_data_volume_type

    @property
    def core_data_volume_size(self):
        r"""Gets the core_data_volume_size of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :return: The core_data_volume_size of this CreateClusterReqV11.
        :rtype: int
        """
        return self._core_data_volume_size

    @core_data_volume_size.setter
    def core_data_volume_size(self, core_data_volume_size):
        r"""Sets the core_data_volume_size of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :param core_data_volume_size: The core_data_volume_size of this CreateClusterReqV11.
        :type core_data_volume_size: int
        """
        self._core_data_volume_size = core_data_volume_size

    @property
    def core_data_volume_count(self):
        r"""Gets the core_data_volume_count of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘个数。 取值范围：1～20

        :return: The core_data_volume_count of this CreateClusterReqV11.
        :rtype: int
        """
        return self._core_data_volume_count

    @core_data_volume_count.setter
    def core_data_volume_count(self, core_data_volume_count):
        r"""Sets the core_data_volume_count of this CreateClusterReqV11.

        该参数为多磁盘参数，表示Core节点数据磁盘个数。 取值范围：1～20

        :param core_data_volume_count: The core_data_volume_count of this CreateClusterReqV11.
        :type core_data_volume_count: int
        """
        self._core_data_volume_count = core_data_volume_count

    @property
    def task_node_groups(self):
        r"""Gets the task_node_groups of this CreateClusterReqV11.

        Task节点列表信息。

        :return: The task_node_groups of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TaskNodeGroup`]
        """
        return self._task_node_groups

    @task_node_groups.setter
    def task_node_groups(self, task_node_groups):
        r"""Sets the task_node_groups of this CreateClusterReqV11.

        Task节点列表信息。

        :param task_node_groups: The task_node_groups of this CreateClusterReqV11.
        :type task_node_groups: list[:class:`huaweicloudsdkmrs.v1.TaskNodeGroup`]
        """
        self._task_node_groups = task_node_groups

    @property
    def bootstrap_scripts(self):
        r"""Gets the bootstrap_scripts of this CreateClusterReqV11.

        配置引导操作脚本信息。

        :return: The bootstrap_scripts of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        """
        return self._bootstrap_scripts

    @bootstrap_scripts.setter
    def bootstrap_scripts(self, bootstrap_scripts):
        r"""Sets the bootstrap_scripts of this CreateClusterReqV11.

        配置引导操作脚本信息。

        :param bootstrap_scripts: The bootstrap_scripts of this CreateClusterReqV11.
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        """
        self._bootstrap_scripts = bootstrap_scripts

    @property
    def node_public_cert_name(self):
        r"""Gets the node_public_cert_name of this CreateClusterReqV11.

        密钥对名称。用户可以使用密钥对方式登录集群节点。当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。

        :return: The node_public_cert_name of this CreateClusterReqV11.
        :rtype: str
        """
        return self._node_public_cert_name

    @node_public_cert_name.setter
    def node_public_cert_name(self, node_public_cert_name):
        r"""Sets the node_public_cert_name of this CreateClusterReqV11.

        密钥对名称。用户可以使用密钥对方式登录集群节点。当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。

        :param node_public_cert_name: The node_public_cert_name of this CreateClusterReqV11.
        :type node_public_cert_name: str
        """
        self._node_public_cert_name = node_public_cert_name

    @property
    def cluster_admin_secret(self):
        r"""Gets the cluster_admin_secret of this CreateClusterReqV11.

        配置MRS Manager管理员用户的密码。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合     - 至少一个小写字母     - 至少一个大写字母     - 至少一个数字     - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :return: The cluster_admin_secret of this CreateClusterReqV11.
        :rtype: str
        """
        return self._cluster_admin_secret

    @cluster_admin_secret.setter
    def cluster_admin_secret(self, cluster_admin_secret):
        r"""Sets the cluster_admin_secret of this CreateClusterReqV11.

        配置MRS Manager管理员用户的密码。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合     - 至少一个小写字母     - 至少一个大写字母     - 至少一个数字     - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :param cluster_admin_secret: The cluster_admin_secret of this CreateClusterReqV11.
        :type cluster_admin_secret: str
        """
        self._cluster_admin_secret = cluster_admin_secret

    @property
    def cluster_master_secret(self):
        r"""Gets the cluster_master_secret of this CreateClusterReqV11.

        配置访问集群节点的root密码。当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。  密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含4种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :return: The cluster_master_secret of this CreateClusterReqV11.
        :rtype: str
        """
        return self._cluster_master_secret

    @cluster_master_secret.setter
    def cluster_master_secret(self, cluster_master_secret):
        r"""Sets the cluster_master_secret of this CreateClusterReqV11.

        配置访问集群节点的root密码。当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。  密码设置约束如下： - 字符串类型，可输入的字符串长度为8-26。 - 至少包含4种字符组合，如大写字母，小写字母，数字，特殊字符（!@$%^-_=+[{}]:,./?），但不能包含空格。 - 不能与用户名或者倒序用户名相同。

        :param cluster_master_secret: The cluster_master_secret of this CreateClusterReqV11.
        :type cluster_master_secret: str
        """
        self._cluster_master_secret = cluster_master_secret

    @property
    def safe_mode(self):
        r"""Gets the safe_mode of this CreateClusterReqV11.

        MRS集群运行模式。 - 0：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - 1：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找MRS Manager的管理员分配权限。

        :return: The safe_mode of this CreateClusterReqV11.
        :rtype: int
        """
        return self._safe_mode

    @safe_mode.setter
    def safe_mode(self, safe_mode):
        r"""Sets the safe_mode of this CreateClusterReqV11.

        MRS集群运行模式。 - 0：普通集群，表示Kerberos认证关闭，用户可使用集群提供的所有功能。 - 1：安全集群，表示Kerberos认证开启，普通用户无权限使用MRS集群的“文件管理”和“作业管理”功能，并且无法查看Hadoop、Spark的作业记录以及集群资源使用情况。如果需要使用集群更多功能，需要找MRS Manager的管理员分配权限。

        :param safe_mode: The safe_mode of this CreateClusterReqV11.
        :type safe_mode: int
        """
        self._safe_mode = safe_mode

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this CreateClusterReqV11.

        集群类型。  默认值为0：分析集群。  说明：暂不支持通过接口方式创建混合集群。  枚举值： - 0：分析集群 - 1：流式集群

        :return: The cluster_type of this CreateClusterReqV11.
        :rtype: int
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this CreateClusterReqV11.

        集群类型。  默认值为0：分析集群。  说明：暂不支持通过接口方式创建混合集群。  枚举值： - 0：分析集群 - 1：流式集群

        :param cluster_type: The cluster_type of this CreateClusterReqV11.
        :type cluster_type: int
        """
        self._cluster_type = cluster_type

    @property
    def log_collection(self):
        r"""Gets the log_collection of this CreateClusterReqV11.

        集群创建失败时，是否收集失败日志。  默认设置为1，将创建OBS桶仅用于MRS集群创建失败时的日志收集。  枚举值： - 0：不收集 - 1：收集

        :return: The log_collection of this CreateClusterReqV11.
        :rtype: int
        """
        return self._log_collection

    @log_collection.setter
    def log_collection(self, log_collection):
        r"""Sets the log_collection of this CreateClusterReqV11.

        集群创建失败时，是否收集失败日志。  默认设置为1，将创建OBS桶仅用于MRS集群创建失败时的日志收集。  枚举值： - 0：不收集 - 1：收集

        :param log_collection: The log_collection of this CreateClusterReqV11.
        :type log_collection: int
        """
        self._log_collection = log_collection

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateClusterReqV11.

        企业项目ID。  创建集群时，给集群绑定企业项目ID。  默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this CreateClusterReqV11.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateClusterReqV11.

        企业项目ID。  创建集群时，给集群绑定企业项目ID。  默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterReqV11.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateClusterReqV11.

        集群的标签信息。  同一个集群最多能使用10个tag，tag的名称（key）不能重复 标签的键/值不能包含“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。

        :return: The tags of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateClusterReqV11.

        集群的标签信息。  同一个集群最多能使用10个tag，tag的名称（key）不能重复 标签的键/值不能包含“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。

        :param tags: The tags of this CreateClusterReqV11.
        :type tags: list[:class:`huaweicloudsdkmrs.v1.Tag`]
        """
        self._tags = tags

    @property
    def login_mode(self):
        r"""Gets the login_mode of this CreateClusterReqV11.

        集群登录方式。默认设置为1。  - 当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。 - 当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。  枚举值： - 0：密码方式 - 1：密钥对方式

        :return: The login_mode of this CreateClusterReqV11.
        :rtype: int
        """
        return self._login_mode

    @login_mode.setter
    def login_mode(self, login_mode):
        r"""Sets the login_mode of this CreateClusterReqV11.

        集群登录方式。默认设置为1。  - 当“login_mode”配置为“0”时，请求消息体中包含cluster_master_secret字段。 - 当“login_mode”配置为“1”时，请求消息体中包含node_public_cert_name字段。  枚举值： - 0：密码方式 - 1：密钥对方式

        :param login_mode: The login_mode of this CreateClusterReqV11.
        :type login_mode: int
        """
        self._login_mode = login_mode

    @property
    def node_groups(self):
        r"""Gets the node_groups of this CreateClusterReqV11.

        节点列表信息。  说明：如下参数和该参数任选一组进行配置即可。  master_node_num、master_node_size、core_node_num、core_node_size、master_data_volume_type、master_data_volume_size、master_data_volume_count、core_data_volume_type、core_data_volume_size、core_data_volume_count、volume_type、volume_size、task_node_groups。

        :return: The node_groups of this CreateClusterReqV11.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV11`]
        """
        return self._node_groups

    @node_groups.setter
    def node_groups(self, node_groups):
        r"""Sets the node_groups of this CreateClusterReqV11.

        节点列表信息。  说明：如下参数和该参数任选一组进行配置即可。  master_node_num、master_node_size、core_node_num、core_node_size、master_data_volume_type、master_data_volume_size、master_data_volume_count、core_data_volume_type、core_data_volume_size、core_data_volume_count、volume_type、volume_size、task_node_groups。

        :param node_groups: The node_groups of this CreateClusterReqV11.
        :type node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV11`]
        """
        self._node_groups = node_groups

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
        if not isinstance(other, CreateClusterReqV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
