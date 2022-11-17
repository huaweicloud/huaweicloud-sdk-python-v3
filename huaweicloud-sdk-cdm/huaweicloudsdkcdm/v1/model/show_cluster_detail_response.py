# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_endpoint': 'str',
        'instances': 'list[ClusterDetailInstance]',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'customer_config': 'CustomerConfig',
        'datastore': 'Datastore',
        'is_auto_off': 'bool',
        'public_endpoint_domain_name': 'str',
        'bak_expected_start_time': 'str',
        'bak_keep_day': 'int',
        'maintain_window': 'CdmQueryClusterDetailsRepsonseMaintainWindow',
        'recent_event': 'int',
        'flavor_name': 'str',
        'az_name': 'str',
        'endpoint_domain_name': 'str',
        'public_endpoint_status': 'CdmQueryClusterDetailsRepsonsePublicEndpointStatus',
        'is_schedule_boot_off': 'bool',
        'namespace': 'str',
        'eip_id': 'str',
        'failed_reasons': 'FailedReasons',
        'dbuser': 'str',
        'links': 'list[ClusterLinks]',
        'cluster_mode': 'str',
        'task': 'ClusterTask',
        'created': 'str',
        'status_detail': 'str',
        'config_status': 'str',
        'action_progress': 'ActionProgress',
        'name': 'str',
        'id': 'str',
        'is_frozen': 'str',
        'actions': 'list[str]',
        'updated': 'str',
        'status': 'str'
    }

    attribute_map = {
        'public_endpoint': 'publicEndpoint',
        'instances': 'instances',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'customer_config': 'customerConfig',
        'datastore': 'datastore',
        'is_auto_off': 'isAutoOff',
        'public_endpoint_domain_name': 'publicEndpointDomainName',
        'bak_expected_start_time': 'bakExpectedStartTime',
        'bak_keep_day': 'bakKeepDay',
        'maintain_window': 'maintainWindow',
        'recent_event': 'recentEvent',
        'flavor_name': 'flavorName',
        'az_name': 'azName',
        'endpoint_domain_name': 'endpointDomainName',
        'public_endpoint_status': 'publicEndpointStatus',
        'is_schedule_boot_off': 'isScheduleBootOff',
        'namespace': 'namespace',
        'eip_id': 'eipId',
        'failed_reasons': 'failedReasons',
        'dbuser': 'dbuser',
        'links': 'links',
        'cluster_mode': 'clusterMode',
        'task': 'task',
        'created': 'created',
        'status_detail': 'statusDetail',
        'config_status': 'config_status',
        'action_progress': 'actionProgress',
        'name': 'name',
        'id': 'id',
        'is_frozen': 'isFrozen',
        'actions': 'actions',
        'updated': 'updated',
        'status': 'status'
    }

    def __init__(self, public_endpoint=None, instances=None, security_group_id=None, subnet_id=None, vpc_id=None, customer_config=None, datastore=None, is_auto_off=None, public_endpoint_domain_name=None, bak_expected_start_time=None, bak_keep_day=None, maintain_window=None, recent_event=None, flavor_name=None, az_name=None, endpoint_domain_name=None, public_endpoint_status=None, is_schedule_boot_off=None, namespace=None, eip_id=None, failed_reasons=None, dbuser=None, links=None, cluster_mode=None, task=None, created=None, status_detail=None, config_status=None, action_progress=None, name=None, id=None, is_frozen=None, actions=None, updated=None, status=None):
        """ShowClusterDetailResponse

        The model defined in huaweicloud sdk

        :param public_endpoint: 集群绑定的EIP
        :type public_endpoint: str
        :param instances: 集群的节点信息，请参见instances参数说明
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        :param security_group_id: 安全组id
        :type security_group_id: str
        :param subnet_id: 子网id
        :type subnet_id: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param customer_config: 
        :type customer_config: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        :param is_auto_off: 自动关机
        :type is_auto_off: bool
        :param public_endpoint_domain_name: 集群绑定的EIP域名
        :type public_endpoint_domain_name: str
        :param bak_expected_start_time: 开始时间
        :type bak_expected_start_time: str
        :param bak_keep_day: 保留时间
        :type bak_keep_day: int
        :param maintain_window: 
        :type maintain_window: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonseMaintainWindow`
        :param recent_event: 事件数
        :type recent_event: int
        :param flavor_name: 规格名称
        :type flavor_name: str
        :param az_name: az名称
        :type az_name: str
        :param endpoint_domain_name: 对端域名
        :type endpoint_domain_name: str
        :param public_endpoint_status: 
        :type public_endpoint_status: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonsePublicEndpointStatus`
        :param is_schedule_boot_off: 选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启
        :type is_schedule_boot_off: bool
        :param namespace: 命名空间
        :type namespace: str
        :param eip_id: 弹性ip id
        :type eip_id: str
        :param failed_reasons: 
        :type failed_reasons: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        :param dbuser: 数据库用户
        :type dbuser: str
        :param links: 
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        :param cluster_mode: 集群模式：sharding(分片集群)
        :type cluster_mode: str
        :param task: 
        :type task: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        :param created: 集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type created: str
        :param status_detail: 集群状态描述：Normal（正常）
        :type status_detail: str
        :param config_status: 集群配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败
        :type config_status: str
        :param action_progress: 
        :type action_progress: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        :param name: 集群名称
        :type name: str
        :param id: 集群ID
        :type id: str
        :param is_frozen: 集群是否冻结：0：否1：是
        :type is_frozen: str
        :param actions: 集群配置状态：In-Sync：配置已同步。Applying：配置中。Sync-Failure：配置失败
        :type actions: list[str]
        :param updated: 集群更新时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type updated: str
        :param status: 集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机
        :type status: str
        """
        
        super(ShowClusterDetailResponse, self).__init__()

        self._public_endpoint = None
        self._instances = None
        self._security_group_id = None
        self._subnet_id = None
        self._vpc_id = None
        self._customer_config = None
        self._datastore = None
        self._is_auto_off = None
        self._public_endpoint_domain_name = None
        self._bak_expected_start_time = None
        self._bak_keep_day = None
        self._maintain_window = None
        self._recent_event = None
        self._flavor_name = None
        self._az_name = None
        self._endpoint_domain_name = None
        self._public_endpoint_status = None
        self._is_schedule_boot_off = None
        self._namespace = None
        self._eip_id = None
        self._failed_reasons = None
        self._dbuser = None
        self._links = None
        self._cluster_mode = None
        self._task = None
        self._created = None
        self._status_detail = None
        self._config_status = None
        self._action_progress = None
        self._name = None
        self._id = None
        self._is_frozen = None
        self._actions = None
        self._updated = None
        self._status = None
        self.discriminator = None

        if public_endpoint is not None:
            self.public_endpoint = public_endpoint
        if instances is not None:
            self.instances = instances
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if customer_config is not None:
            self.customer_config = customer_config
        if datastore is not None:
            self.datastore = datastore
        if is_auto_off is not None:
            self.is_auto_off = is_auto_off
        if public_endpoint_domain_name is not None:
            self.public_endpoint_domain_name = public_endpoint_domain_name
        if bak_expected_start_time is not None:
            self.bak_expected_start_time = bak_expected_start_time
        if bak_keep_day is not None:
            self.bak_keep_day = bak_keep_day
        if maintain_window is not None:
            self.maintain_window = maintain_window
        if recent_event is not None:
            self.recent_event = recent_event
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if az_name is not None:
            self.az_name = az_name
        if endpoint_domain_name is not None:
            self.endpoint_domain_name = endpoint_domain_name
        if public_endpoint_status is not None:
            self.public_endpoint_status = public_endpoint_status
        if is_schedule_boot_off is not None:
            self.is_schedule_boot_off = is_schedule_boot_off
        if namespace is not None:
            self.namespace = namespace
        if eip_id is not None:
            self.eip_id = eip_id
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons
        if dbuser is not None:
            self.dbuser = dbuser
        if links is not None:
            self.links = links
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if task is not None:
            self.task = task
        if created is not None:
            self.created = created
        if status_detail is not None:
            self.status_detail = status_detail
        if config_status is not None:
            self.config_status = config_status
        if action_progress is not None:
            self.action_progress = action_progress
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if actions is not None:
            self.actions = actions
        if updated is not None:
            self.updated = updated
        if status is not None:
            self.status = status

    @property
    def public_endpoint(self):
        """Gets the public_endpoint of this ShowClusterDetailResponse.

        集群绑定的EIP

        :return: The public_endpoint of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._public_endpoint

    @public_endpoint.setter
    def public_endpoint(self, public_endpoint):
        """Sets the public_endpoint of this ShowClusterDetailResponse.

        集群绑定的EIP

        :param public_endpoint: The public_endpoint of this ShowClusterDetailResponse.
        :type public_endpoint: str
        """
        self._public_endpoint = public_endpoint

    @property
    def instances(self):
        """Gets the instances of this ShowClusterDetailResponse.

        集群的节点信息，请参见instances参数说明

        :return: The instances of this ShowClusterDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ShowClusterDetailResponse.

        集群的节点信息，请参见instances参数说明

        :param instances: The instances of this ShowClusterDetailResponse.
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterDetailInstance`]
        """
        self._instances = instances

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowClusterDetailResponse.

        安全组id

        :return: The security_group_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowClusterDetailResponse.

        安全组id

        :param security_group_id: The security_group_id of this ShowClusterDetailResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowClusterDetailResponse.

        子网id

        :return: The subnet_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowClusterDetailResponse.

        子网id

        :param subnet_id: The subnet_id of this ShowClusterDetailResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowClusterDetailResponse.

        虚拟私有云ID

        :return: The vpc_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowClusterDetailResponse.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this ShowClusterDetailResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def customer_config(self):
        """Gets the customer_config of this ShowClusterDetailResponse.

        :return: The customer_config of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        """
        return self._customer_config

    @customer_config.setter
    def customer_config(self, customer_config):
        """Sets the customer_config of this ShowClusterDetailResponse.

        :param customer_config: The customer_config of this ShowClusterDetailResponse.
        :type customer_config: :class:`huaweicloudsdkcdm.v1.CustomerConfig`
        """
        self._customer_config = customer_config

    @property
    def datastore(self):
        """Gets the datastore of this ShowClusterDetailResponse.

        :return: The datastore of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ShowClusterDetailResponse.

        :param datastore: The datastore of this ShowClusterDetailResponse.
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        self._datastore = datastore

    @property
    def is_auto_off(self):
        """Gets the is_auto_off of this ShowClusterDetailResponse.

        自动关机

        :return: The is_auto_off of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._is_auto_off

    @is_auto_off.setter
    def is_auto_off(self, is_auto_off):
        """Sets the is_auto_off of this ShowClusterDetailResponse.

        自动关机

        :param is_auto_off: The is_auto_off of this ShowClusterDetailResponse.
        :type is_auto_off: bool
        """
        self._is_auto_off = is_auto_off

    @property
    def public_endpoint_domain_name(self):
        """Gets the public_endpoint_domain_name of this ShowClusterDetailResponse.

        集群绑定的EIP域名

        :return: The public_endpoint_domain_name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._public_endpoint_domain_name

    @public_endpoint_domain_name.setter
    def public_endpoint_domain_name(self, public_endpoint_domain_name):
        """Sets the public_endpoint_domain_name of this ShowClusterDetailResponse.

        集群绑定的EIP域名

        :param public_endpoint_domain_name: The public_endpoint_domain_name of this ShowClusterDetailResponse.
        :type public_endpoint_domain_name: str
        """
        self._public_endpoint_domain_name = public_endpoint_domain_name

    @property
    def bak_expected_start_time(self):
        """Gets the bak_expected_start_time of this ShowClusterDetailResponse.

        开始时间

        :return: The bak_expected_start_time of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._bak_expected_start_time

    @bak_expected_start_time.setter
    def bak_expected_start_time(self, bak_expected_start_time):
        """Sets the bak_expected_start_time of this ShowClusterDetailResponse.

        开始时间

        :param bak_expected_start_time: The bak_expected_start_time of this ShowClusterDetailResponse.
        :type bak_expected_start_time: str
        """
        self._bak_expected_start_time = bak_expected_start_time

    @property
    def bak_keep_day(self):
        """Gets the bak_keep_day of this ShowClusterDetailResponse.

        保留时间

        :return: The bak_keep_day of this ShowClusterDetailResponse.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        """Sets the bak_keep_day of this ShowClusterDetailResponse.

        保留时间

        :param bak_keep_day: The bak_keep_day of this ShowClusterDetailResponse.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

    @property
    def maintain_window(self):
        """Gets the maintain_window of this ShowClusterDetailResponse.

        :return: The maintain_window of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonseMaintainWindow`
        """
        return self._maintain_window

    @maintain_window.setter
    def maintain_window(self, maintain_window):
        """Sets the maintain_window of this ShowClusterDetailResponse.

        :param maintain_window: The maintain_window of this ShowClusterDetailResponse.
        :type maintain_window: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonseMaintainWindow`
        """
        self._maintain_window = maintain_window

    @property
    def recent_event(self):
        """Gets the recent_event of this ShowClusterDetailResponse.

        事件数

        :return: The recent_event of this ShowClusterDetailResponse.
        :rtype: int
        """
        return self._recent_event

    @recent_event.setter
    def recent_event(self, recent_event):
        """Sets the recent_event of this ShowClusterDetailResponse.

        事件数

        :param recent_event: The recent_event of this ShowClusterDetailResponse.
        :type recent_event: int
        """
        self._recent_event = recent_event

    @property
    def flavor_name(self):
        """Gets the flavor_name of this ShowClusterDetailResponse.

        规格名称

        :return: The flavor_name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        """Sets the flavor_name of this ShowClusterDetailResponse.

        规格名称

        :param flavor_name: The flavor_name of this ShowClusterDetailResponse.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def az_name(self):
        """Gets the az_name of this ShowClusterDetailResponse.

        az名称

        :return: The az_name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this ShowClusterDetailResponse.

        az名称

        :param az_name: The az_name of this ShowClusterDetailResponse.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def endpoint_domain_name(self):
        """Gets the endpoint_domain_name of this ShowClusterDetailResponse.

        对端域名

        :return: The endpoint_domain_name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._endpoint_domain_name

    @endpoint_domain_name.setter
    def endpoint_domain_name(self, endpoint_domain_name):
        """Sets the endpoint_domain_name of this ShowClusterDetailResponse.

        对端域名

        :param endpoint_domain_name: The endpoint_domain_name of this ShowClusterDetailResponse.
        :type endpoint_domain_name: str
        """
        self._endpoint_domain_name = endpoint_domain_name

    @property
    def public_endpoint_status(self):
        """Gets the public_endpoint_status of this ShowClusterDetailResponse.

        :return: The public_endpoint_status of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonsePublicEndpointStatus`
        """
        return self._public_endpoint_status

    @public_endpoint_status.setter
    def public_endpoint_status(self, public_endpoint_status):
        """Sets the public_endpoint_status of this ShowClusterDetailResponse.

        :param public_endpoint_status: The public_endpoint_status of this ShowClusterDetailResponse.
        :type public_endpoint_status: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterDetailsRepsonsePublicEndpointStatus`
        """
        self._public_endpoint_status = public_endpoint_status

    @property
    def is_schedule_boot_off(self):
        """Gets the is_schedule_boot_off of this ShowClusterDetailResponse.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :return: The is_schedule_boot_off of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._is_schedule_boot_off

    @is_schedule_boot_off.setter
    def is_schedule_boot_off(self, is_schedule_boot_off):
        """Sets the is_schedule_boot_off of this ShowClusterDetailResponse.

        选择是否启用定时开关机功能。定时开关机功能和自动关机功能不可同时开启

        :param is_schedule_boot_off: The is_schedule_boot_off of this ShowClusterDetailResponse.
        :type is_schedule_boot_off: bool
        """
        self._is_schedule_boot_off = is_schedule_boot_off

    @property
    def namespace(self):
        """Gets the namespace of this ShowClusterDetailResponse.

        命名空间

        :return: The namespace of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowClusterDetailResponse.

        命名空间

        :param namespace: The namespace of this ShowClusterDetailResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def eip_id(self):
        """Gets the eip_id of this ShowClusterDetailResponse.

        弹性ip id

        :return: The eip_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this ShowClusterDetailResponse.

        弹性ip id

        :param eip_id: The eip_id of this ShowClusterDetailResponse.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this ShowClusterDetailResponse.

        :return: The failed_reasons of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this ShowClusterDetailResponse.

        :param failed_reasons: The failed_reasons of this ShowClusterDetailResponse.
        :type failed_reasons: :class:`huaweicloudsdkcdm.v1.FailedReasons`
        """
        self._failed_reasons = failed_reasons

    @property
    def dbuser(self):
        """Gets the dbuser of this ShowClusterDetailResponse.

        数据库用户

        :return: The dbuser of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._dbuser

    @dbuser.setter
    def dbuser(self, dbuser):
        """Sets the dbuser of this ShowClusterDetailResponse.

        数据库用户

        :param dbuser: The dbuser of this ShowClusterDetailResponse.
        :type dbuser: str
        """
        self._dbuser = dbuser

    @property
    def links(self):
        """Gets the links of this ShowClusterDetailResponse.

        :return: The links of this ShowClusterDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowClusterDetailResponse.

        :param links: The links of this ShowClusterDetailResponse.
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        self._links = links

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this ShowClusterDetailResponse.

        集群模式：sharding(分片集群)

        :return: The cluster_mode of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this ShowClusterDetailResponse.

        集群模式：sharding(分片集群)

        :param cluster_mode: The cluster_mode of this ShowClusterDetailResponse.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def task(self):
        """Gets the task of this ShowClusterDetailResponse.

        :return: The task of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ShowClusterDetailResponse.

        :param task: The task of this ShowClusterDetailResponse.
        :type task: :class:`huaweicloudsdkcdm.v1.ClusterTask`
        """
        self._task = task

    @property
    def created(self):
        """Gets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The created of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param created: The created of this ShowClusterDetailResponse.
        :type created: str
        """
        self._created = created

    @property
    def status_detail(self):
        """Gets the status_detail of this ShowClusterDetailResponse.

        集群状态描述：Normal（正常）

        :return: The status_detail of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this ShowClusterDetailResponse.

        集群状态描述：Normal（正常）

        :param status_detail: The status_detail of this ShowClusterDetailResponse.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def config_status(self):
        """Gets the config_status of this ShowClusterDetailResponse.

        集群配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败

        :return: The config_status of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this ShowClusterDetailResponse.

        集群配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败

        :param config_status: The config_status of this ShowClusterDetailResponse.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def action_progress(self):
        """Gets the action_progress of this ShowClusterDetailResponse.

        :return: The action_progress of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ShowClusterDetailResponse.

        :param action_progress: The action_progress of this ShowClusterDetailResponse.
        :type action_progress: :class:`huaweicloudsdkcdm.v1.ActionProgress`
        """
        self._action_progress = action_progress

    @property
    def name(self):
        """Gets the name of this ShowClusterDetailResponse.

        集群名称

        :return: The name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowClusterDetailResponse.

        集群名称

        :param name: The name of this ShowClusterDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ShowClusterDetailResponse.

        集群ID

        :return: The id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowClusterDetailResponse.

        集群ID

        :param id: The id of this ShowClusterDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def is_frozen(self):
        """Gets the is_frozen of this ShowClusterDetailResponse.

        集群是否冻结：0：否1：是

        :return: The is_frozen of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this ShowClusterDetailResponse.

        集群是否冻结：0：否1：是

        :param is_frozen: The is_frozen of this ShowClusterDetailResponse.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

    @property
    def actions(self):
        """Gets the actions of this ShowClusterDetailResponse.

        集群配置状态：In-Sync：配置已同步。Applying：配置中。Sync-Failure：配置失败

        :return: The actions of this ShowClusterDetailResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ShowClusterDetailResponse.

        集群配置状态：In-Sync：配置已同步。Applying：配置中。Sync-Failure：配置失败

        :param actions: The actions of this ShowClusterDetailResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def updated(self):
        """Gets the updated of this ShowClusterDetailResponse.

        集群更新时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The updated of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowClusterDetailResponse.

        集群更新时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param updated: The updated of this ShowClusterDetailResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        """Gets the status of this ShowClusterDetailResponse.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :return: The status of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClusterDetailResponse.

        集群状态： - 100：创建中 - 200：正常 - 300：失败 - 303：创建失败 - 800：冻结 - 900：已关机 - 910：正在关机 - 920：正在开机

        :param status: The status of this ShowClusterDetailResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowClusterDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
