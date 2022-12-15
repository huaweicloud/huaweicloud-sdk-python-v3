# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'version': 'str',
        'service_type': 'str',
        'purchase_type': 'str',
        'sign_algorithm': 'str',
        'consensus': 'str',
        'charging_mode': 'int',
        'version_type': 'int',
        'database_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_type': 'str',
        'cluster_az': 'str',
        'created_time': 'str',
        'deploy_type': 'str',
        'order_fade_enabled': 'bool',
        'is_cross_region': 'bool',
        'is_support_rollback': 'bool',
        'is_support_restful': 'bool',
        'is_support_tc3': 'bool',
        'is_old_service': 'bool',
        'old_service_version': 'str',
        'agent_portal_addrs': 'list[str]',
        'status': 'str',
        'process_status': 'str',
        'order_status': 'int',
        'order_fade_cache': 'int',
        'deploy_status': 'int',
        'block_info': 'CreateRequestBodyBlockInfo',
        'cluster_platform_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'service_type': 'service_type',
        'purchase_type': 'purchase_type',
        'sign_algorithm': 'sign_algorithm',
        'consensus': 'consensus',
        'charging_mode': 'charging_mode',
        'version_type': 'version_type',
        'database_type': 'database_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type',
        'cluster_az': 'cluster_az',
        'created_time': 'created_time',
        'deploy_type': 'deploy_type',
        'order_fade_enabled': 'order_fade_enabled',
        'is_cross_region': 'is_cross_region',
        'is_support_rollback': 'is_support_rollback',
        'is_support_restful': 'is_support_restful',
        'is_support_tc3': 'is_support_tc3',
        'is_old_service': 'is_old_service',
        'old_service_version': 'old_service_version',
        'agent_portal_addrs': 'agent_portal_addrs',
        'status': 'status',
        'process_status': 'process_status',
        'order_status': 'order_status',
        'order_fade_cache': 'order_fade_cache',
        'deploy_status': 'deploy_status',
        'block_info': 'block_info',
        'cluster_platform_type': 'cluster_platform_type'
    }

    def __init__(self, id=None, name=None, version=None, service_type=None, purchase_type=None, sign_algorithm=None, consensus=None, charging_mode=None, version_type=None, database_type=None, cluster_id=None, cluster_name=None, cluster_type=None, cluster_az=None, created_time=None, deploy_type=None, order_fade_enabled=None, is_cross_region=None, is_support_rollback=None, is_support_restful=None, is_support_tc3=None, is_old_service=None, old_service_version=None, agent_portal_addrs=None, status=None, process_status=None, order_status=None, order_fade_cache=None, deploy_status=None, block_info=None, cluster_platform_type=None):
        """BasicInfo

        The model defined in huaweicloud sdk

        :param id: BCS服务ID
        :type id: str
        :param name: 区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。
        :type name: str
        :param version: BCS服务版本信息
        :type version: str
        :param service_type: BCS服务的类型，分为：联盟链（union），私有链（private）
        :type service_type: str
        :param purchase_type: BCS服务部署类型，一键部署（onestep），普通部署（normal）
        :type purchase_type: str
        :param sign_algorithm: BCS服务安全机制，分为ECDSA（ECDSA），国密算法（sm2）
        :type sign_algorithm: str
        :param consensus: BCS服务的共识策略，分为测试策略（solo），快速拜占庭容错算法（sflic）,Kafka(kafka)，raft共识算法（etcdraft）
        :type consensus: str
        :param charging_mode: BCS服务付费模式，分为按需（1）[包周期（0）](tag:onorder)
        :type charging_mode: int
        :param version_type: BCS服务版本类型
        :type version_type: int
        :param database_type: BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb）
        :type database_type: str
        :param cluster_id: BCS服务所在集群ID
        :type cluster_id: str
        :param cluster_name: BCS服务所在集群名称
        :type cluster_name: str
        :param cluster_type: BCS服务的集群类型，分为CCE集群（CCE），IEF集群（ief）
        :type cluster_type: str
        :param cluster_az: BCS多可用区标示，分为：多可用区（yes），非多可用区（no）
        :type cluster_az: str
        :param created_time: BCS服务创建时间
        :type created_time: str
        :param deploy_type: BCS服务联盟链下生效，分为邀请方（create），被邀请方（invite）
        :type deploy_type: str
        :param order_fade_enabled: 是否允许order老化
        :type order_fade_enabled: bool
        :param is_cross_region: BCS服务是否跨region
        :type is_cross_region: bool
        :param is_support_rollback: BCS服务升级失败，是否支持回滚
        :type is_support_rollback: bool
        :param is_support_restful: BCS服务是否添加RESTful APIs支持，分为支持（true），不支持（false）
        :type is_support_restful: bool
        :param is_support_tc3: BCS服务是否支持可信计算平台，分为支持（true），不支持（false）
        :type is_support_tc3: bool
        :param is_old_service: 区分BCS是否新服务，分为老服务（true），新服务（false）
        :type is_old_service: bool
        :param old_service_version: BCS服务为老服务时，此字段为老服务版本号
        :type old_service_version: str
        :param agent_portal_addrs: BCS服务用户数据面agent地址端口列表
        :type agent_portal_addrs: list[str]
        :param status: BCS服务状态，分为正常（Normal），异常（Abnormal），弹性IP异常（EipAbnormal），已冻结（Freeze），休眠中（Hibernation），未知（其余值）
        :type status: str
        :param process_status: BCS服务处理状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（IsScaling），删除中（IsDeleting），添加中（IsAdding）
        :type process_status: str
        :param order_status: BCS服务为包周期模式时，返回值为0（订单未成功）,1（订单异常）,2（订单正常）
        :type order_status: int
        :param order_fade_cache: 共识节点的老化阈值
        :type order_fade_cache: int
        :param deploy_status: BCS服务部署状态，分为进行中（0），成功（1），失败（2），结束（3）
        :type deploy_status: int
        :param block_info: 
        :type block_info: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        :param cluster_platform_type: 集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）
        :type cluster_platform_type: str
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self._service_type = None
        self._purchase_type = None
        self._sign_algorithm = None
        self._consensus = None
        self._charging_mode = None
        self._version_type = None
        self._database_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_type = None
        self._cluster_az = None
        self._created_time = None
        self._deploy_type = None
        self._order_fade_enabled = None
        self._is_cross_region = None
        self._is_support_rollback = None
        self._is_support_restful = None
        self._is_support_tc3 = None
        self._is_old_service = None
        self._old_service_version = None
        self._agent_portal_addrs = None
        self._status = None
        self._process_status = None
        self._order_status = None
        self._order_fade_cache = None
        self._deploy_status = None
        self._block_info = None
        self._cluster_platform_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if service_type is not None:
            self.service_type = service_type
        if purchase_type is not None:
            self.purchase_type = purchase_type
        if sign_algorithm is not None:
            self.sign_algorithm = sign_algorithm
        if consensus is not None:
            self.consensus = consensus
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if version_type is not None:
            self.version_type = version_type
        if database_type is not None:
            self.database_type = database_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_az is not None:
            self.cluster_az = cluster_az
        if created_time is not None:
            self.created_time = created_time
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if order_fade_enabled is not None:
            self.order_fade_enabled = order_fade_enabled
        if is_cross_region is not None:
            self.is_cross_region = is_cross_region
        if is_support_rollback is not None:
            self.is_support_rollback = is_support_rollback
        if is_support_restful is not None:
            self.is_support_restful = is_support_restful
        if is_support_tc3 is not None:
            self.is_support_tc3 = is_support_tc3
        if is_old_service is not None:
            self.is_old_service = is_old_service
        if old_service_version is not None:
            self.old_service_version = old_service_version
        if agent_portal_addrs is not None:
            self.agent_portal_addrs = agent_portal_addrs
        if status is not None:
            self.status = status
        if process_status is not None:
            self.process_status = process_status
        if order_status is not None:
            self.order_status = order_status
        if order_fade_cache is not None:
            self.order_fade_cache = order_fade_cache
        if deploy_status is not None:
            self.deploy_status = deploy_status
        if block_info is not None:
            self.block_info = block_info
        if cluster_platform_type is not None:
            self.cluster_platform_type = cluster_platform_type

    @property
    def id(self):
        """Gets the id of this BasicInfo.

        BCS服务ID

        :return: The id of this BasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicInfo.

        BCS服务ID

        :param id: The id of this BasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BasicInfo.

        区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。

        :return: The name of this BasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicInfo.

        区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。

        :param name: The name of this BasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this BasicInfo.

        BCS服务版本信息

        :return: The version of this BasicInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BasicInfo.

        BCS服务版本信息

        :param version: The version of this BasicInfo.
        :type version: str
        """
        self._version = version

    @property
    def service_type(self):
        """Gets the service_type of this BasicInfo.

        BCS服务的类型，分为：联盟链（union），私有链（private）

        :return: The service_type of this BasicInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this BasicInfo.

        BCS服务的类型，分为：联盟链（union），私有链（private）

        :param service_type: The service_type of this BasicInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def purchase_type(self):
        """Gets the purchase_type of this BasicInfo.

        BCS服务部署类型，一键部署（onestep），普通部署（normal）

        :return: The purchase_type of this BasicInfo.
        :rtype: str
        """
        return self._purchase_type

    @purchase_type.setter
    def purchase_type(self, purchase_type):
        """Sets the purchase_type of this BasicInfo.

        BCS服务部署类型，一键部署（onestep），普通部署（normal）

        :param purchase_type: The purchase_type of this BasicInfo.
        :type purchase_type: str
        """
        self._purchase_type = purchase_type

    @property
    def sign_algorithm(self):
        """Gets the sign_algorithm of this BasicInfo.

        BCS服务安全机制，分为ECDSA（ECDSA），国密算法（sm2）

        :return: The sign_algorithm of this BasicInfo.
        :rtype: str
        """
        return self._sign_algorithm

    @sign_algorithm.setter
    def sign_algorithm(self, sign_algorithm):
        """Sets the sign_algorithm of this BasicInfo.

        BCS服务安全机制，分为ECDSA（ECDSA），国密算法（sm2）

        :param sign_algorithm: The sign_algorithm of this BasicInfo.
        :type sign_algorithm: str
        """
        self._sign_algorithm = sign_algorithm

    @property
    def consensus(self):
        """Gets the consensus of this BasicInfo.

        BCS服务的共识策略，分为测试策略（solo），快速拜占庭容错算法（sflic）,Kafka(kafka)，raft共识算法（etcdraft）

        :return: The consensus of this BasicInfo.
        :rtype: str
        """
        return self._consensus

    @consensus.setter
    def consensus(self, consensus):
        """Sets the consensus of this BasicInfo.

        BCS服务的共识策略，分为测试策略（solo），快速拜占庭容错算法（sflic）,Kafka(kafka)，raft共识算法（etcdraft）

        :param consensus: The consensus of this BasicInfo.
        :type consensus: str
        """
        self._consensus = consensus

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BasicInfo.

        BCS服务付费模式，分为按需（1）[包周期（0）](tag:onorder)

        :return: The charging_mode of this BasicInfo.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BasicInfo.

        BCS服务付费模式，分为按需（1）[包周期（0）](tag:onorder)

        :param charging_mode: The charging_mode of this BasicInfo.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def version_type(self):
        """Gets the version_type of this BasicInfo.

        BCS服务版本类型

        :return: The version_type of this BasicInfo.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this BasicInfo.

        BCS服务版本类型

        :param version_type: The version_type of this BasicInfo.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def database_type(self):
        """Gets the database_type of this BasicInfo.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb）

        :return: The database_type of this BasicInfo.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """Sets the database_type of this BasicInfo.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb）

        :param database_type: The database_type of this BasicInfo.
        :type database_type: str
        """
        self._database_type = database_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BasicInfo.

        BCS服务所在集群ID

        :return: The cluster_id of this BasicInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BasicInfo.

        BCS服务所在集群ID

        :param cluster_id: The cluster_id of this BasicInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this BasicInfo.

        BCS服务所在集群名称

        :return: The cluster_name of this BasicInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this BasicInfo.

        BCS服务所在集群名称

        :param cluster_name: The cluster_name of this BasicInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """Gets the cluster_type of this BasicInfo.

        BCS服务的集群类型，分为CCE集群（CCE），IEF集群（ief）

        :return: The cluster_type of this BasicInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this BasicInfo.

        BCS服务的集群类型，分为CCE集群（CCE），IEF集群（ief）

        :param cluster_type: The cluster_type of this BasicInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_az(self):
        """Gets the cluster_az of this BasicInfo.

        BCS多可用区标示，分为：多可用区（yes），非多可用区（no）

        :return: The cluster_az of this BasicInfo.
        :rtype: str
        """
        return self._cluster_az

    @cluster_az.setter
    def cluster_az(self, cluster_az):
        """Sets the cluster_az of this BasicInfo.

        BCS多可用区标示，分为：多可用区（yes），非多可用区（no）

        :param cluster_az: The cluster_az of this BasicInfo.
        :type cluster_az: str
        """
        self._cluster_az = cluster_az

    @property
    def created_time(self):
        """Gets the created_time of this BasicInfo.

        BCS服务创建时间

        :return: The created_time of this BasicInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this BasicInfo.

        BCS服务创建时间

        :param created_time: The created_time of this BasicInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def deploy_type(self):
        """Gets the deploy_type of this BasicInfo.

        BCS服务联盟链下生效，分为邀请方（create），被邀请方（invite）

        :return: The deploy_type of this BasicInfo.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this BasicInfo.

        BCS服务联盟链下生效，分为邀请方（create），被邀请方（invite）

        :param deploy_type: The deploy_type of this BasicInfo.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def order_fade_enabled(self):
        """Gets the order_fade_enabled of this BasicInfo.

        是否允许order老化

        :return: The order_fade_enabled of this BasicInfo.
        :rtype: bool
        """
        return self._order_fade_enabled

    @order_fade_enabled.setter
    def order_fade_enabled(self, order_fade_enabled):
        """Sets the order_fade_enabled of this BasicInfo.

        是否允许order老化

        :param order_fade_enabled: The order_fade_enabled of this BasicInfo.
        :type order_fade_enabled: bool
        """
        self._order_fade_enabled = order_fade_enabled

    @property
    def is_cross_region(self):
        """Gets the is_cross_region of this BasicInfo.

        BCS服务是否跨region

        :return: The is_cross_region of this BasicInfo.
        :rtype: bool
        """
        return self._is_cross_region

    @is_cross_region.setter
    def is_cross_region(self, is_cross_region):
        """Sets the is_cross_region of this BasicInfo.

        BCS服务是否跨region

        :param is_cross_region: The is_cross_region of this BasicInfo.
        :type is_cross_region: bool
        """
        self._is_cross_region = is_cross_region

    @property
    def is_support_rollback(self):
        """Gets the is_support_rollback of this BasicInfo.

        BCS服务升级失败，是否支持回滚

        :return: The is_support_rollback of this BasicInfo.
        :rtype: bool
        """
        return self._is_support_rollback

    @is_support_rollback.setter
    def is_support_rollback(self, is_support_rollback):
        """Sets the is_support_rollback of this BasicInfo.

        BCS服务升级失败，是否支持回滚

        :param is_support_rollback: The is_support_rollback of this BasicInfo.
        :type is_support_rollback: bool
        """
        self._is_support_rollback = is_support_rollback

    @property
    def is_support_restful(self):
        """Gets the is_support_restful of this BasicInfo.

        BCS服务是否添加RESTful APIs支持，分为支持（true），不支持（false）

        :return: The is_support_restful of this BasicInfo.
        :rtype: bool
        """
        return self._is_support_restful

    @is_support_restful.setter
    def is_support_restful(self, is_support_restful):
        """Sets the is_support_restful of this BasicInfo.

        BCS服务是否添加RESTful APIs支持，分为支持（true），不支持（false）

        :param is_support_restful: The is_support_restful of this BasicInfo.
        :type is_support_restful: bool
        """
        self._is_support_restful = is_support_restful

    @property
    def is_support_tc3(self):
        """Gets the is_support_tc3 of this BasicInfo.

        BCS服务是否支持可信计算平台，分为支持（true），不支持（false）

        :return: The is_support_tc3 of this BasicInfo.
        :rtype: bool
        """
        return self._is_support_tc3

    @is_support_tc3.setter
    def is_support_tc3(self, is_support_tc3):
        """Sets the is_support_tc3 of this BasicInfo.

        BCS服务是否支持可信计算平台，分为支持（true），不支持（false）

        :param is_support_tc3: The is_support_tc3 of this BasicInfo.
        :type is_support_tc3: bool
        """
        self._is_support_tc3 = is_support_tc3

    @property
    def is_old_service(self):
        """Gets the is_old_service of this BasicInfo.

        区分BCS是否新服务，分为老服务（true），新服务（false）

        :return: The is_old_service of this BasicInfo.
        :rtype: bool
        """
        return self._is_old_service

    @is_old_service.setter
    def is_old_service(self, is_old_service):
        """Sets the is_old_service of this BasicInfo.

        区分BCS是否新服务，分为老服务（true），新服务（false）

        :param is_old_service: The is_old_service of this BasicInfo.
        :type is_old_service: bool
        """
        self._is_old_service = is_old_service

    @property
    def old_service_version(self):
        """Gets the old_service_version of this BasicInfo.

        BCS服务为老服务时，此字段为老服务版本号

        :return: The old_service_version of this BasicInfo.
        :rtype: str
        """
        return self._old_service_version

    @old_service_version.setter
    def old_service_version(self, old_service_version):
        """Sets the old_service_version of this BasicInfo.

        BCS服务为老服务时，此字段为老服务版本号

        :param old_service_version: The old_service_version of this BasicInfo.
        :type old_service_version: str
        """
        self._old_service_version = old_service_version

    @property
    def agent_portal_addrs(self):
        """Gets the agent_portal_addrs of this BasicInfo.

        BCS服务用户数据面agent地址端口列表

        :return: The agent_portal_addrs of this BasicInfo.
        :rtype: list[str]
        """
        return self._agent_portal_addrs

    @agent_portal_addrs.setter
    def agent_portal_addrs(self, agent_portal_addrs):
        """Sets the agent_portal_addrs of this BasicInfo.

        BCS服务用户数据面agent地址端口列表

        :param agent_portal_addrs: The agent_portal_addrs of this BasicInfo.
        :type agent_portal_addrs: list[str]
        """
        self._agent_portal_addrs = agent_portal_addrs

    @property
    def status(self):
        """Gets the status of this BasicInfo.

        BCS服务状态，分为正常（Normal），异常（Abnormal），弹性IP异常（EipAbnormal），已冻结（Freeze），休眠中（Hibernation），未知（其余值）

        :return: The status of this BasicInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BasicInfo.

        BCS服务状态，分为正常（Normal），异常（Abnormal），弹性IP异常（EipAbnormal），已冻结（Freeze），休眠中（Hibernation），未知（其余值）

        :param status: The status of this BasicInfo.
        :type status: str
        """
        self._status = status

    @property
    def process_status(self):
        """Gets the process_status of this BasicInfo.

        BCS服务处理状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（IsScaling），删除中（IsDeleting），添加中（IsAdding）

        :return: The process_status of this BasicInfo.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this BasicInfo.

        BCS服务处理状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（IsScaling），删除中（IsDeleting），添加中（IsAdding）

        :param process_status: The process_status of this BasicInfo.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def order_status(self):
        """Gets the order_status of this BasicInfo.

        BCS服务为包周期模式时，返回值为0（订单未成功）,1（订单异常）,2（订单正常）

        :return: The order_status of this BasicInfo.
        :rtype: int
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this BasicInfo.

        BCS服务为包周期模式时，返回值为0（订单未成功）,1（订单异常）,2（订单正常）

        :param order_status: The order_status of this BasicInfo.
        :type order_status: int
        """
        self._order_status = order_status

    @property
    def order_fade_cache(self):
        """Gets the order_fade_cache of this BasicInfo.

        共识节点的老化阈值

        :return: The order_fade_cache of this BasicInfo.
        :rtype: int
        """
        return self._order_fade_cache

    @order_fade_cache.setter
    def order_fade_cache(self, order_fade_cache):
        """Sets the order_fade_cache of this BasicInfo.

        共识节点的老化阈值

        :param order_fade_cache: The order_fade_cache of this BasicInfo.
        :type order_fade_cache: int
        """
        self._order_fade_cache = order_fade_cache

    @property
    def deploy_status(self):
        """Gets the deploy_status of this BasicInfo.

        BCS服务部署状态，分为进行中（0），成功（1），失败（2），结束（3）

        :return: The deploy_status of this BasicInfo.
        :rtype: int
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this BasicInfo.

        BCS服务部署状态，分为进行中（0），成功（1），失败（2），结束（3）

        :param deploy_status: The deploy_status of this BasicInfo.
        :type deploy_status: int
        """
        self._deploy_status = deploy_status

    @property
    def block_info(self):
        """Gets the block_info of this BasicInfo.

        :return: The block_info of this BasicInfo.
        :rtype: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        """
        return self._block_info

    @block_info.setter
    def block_info(self, block_info):
        """Sets the block_info of this BasicInfo.

        :param block_info: The block_info of this BasicInfo.
        :type block_info: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        """
        self._block_info = block_info

    @property
    def cluster_platform_type(self):
        """Gets the cluster_platform_type of this BasicInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :return: The cluster_platform_type of this BasicInfo.
        :rtype: str
        """
        return self._cluster_platform_type

    @cluster_platform_type.setter
    def cluster_platform_type(self, cluster_platform_type):
        """Sets the cluster_platform_type of this BasicInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :param cluster_platform_type: The cluster_platform_type of this BasicInfo.
        :type cluster_platform_type: str
        """
        self._cluster_platform_type = cluster_platform_type

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
        if not isinstance(other, BasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
