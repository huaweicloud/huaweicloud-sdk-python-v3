# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'version_type': 'int',
        'fabric_version': 'str',
        'blockchain_type': 'str',
        'consensus': 'str',
        'sign_algorithm': 'str',
        'enterprise_project_id': 'str',
        'volume_type': 'str',
        'evs_disk_type': 'str',
        'org_disk_size': 'int',
        'database_type': 'str',
        'resource_password': 'str',
        'orderer_node_number': 'int',
        'use_eip': 'bool',
        'bandwidth_size': 'int',
        'cluster_type': 'str',
        'create_new_cluster': 'bool',
        'cce_cluster_info': 'CCEClusterInfo',
        'cce_create_info': 'CCECreateInfo',
        'ief_deploy_mode': 'int',
        'ief_nodes_info': 'list[IEFNode]',
        'peer_orgs': 'list[OrgPeer]',
        'channels': 'list[ChannelInfoV2]',
        'couchdb_info': 'CouchDb',
        'turbo_info': 'TurboInfo',
        'block_info': 'CreateRequestBodyBlockInfo',
        'kafka_create_info': 'KafkaCreateInfo',
        'tc3_need': 'bool',
        'restful_api_support': 'bool',
        'is_invitee': 'bool',
        'invitor_infos': 'InvitorInfos'
    }

    attribute_map = {
        'name': 'name',
        'version_type': 'version_type',
        'fabric_version': 'fabric_version',
        'blockchain_type': 'blockchain_type',
        'consensus': 'consensus',
        'sign_algorithm': 'sign_algorithm',
        'enterprise_project_id': 'enterprise_project_id',
        'volume_type': 'volume_type',
        'evs_disk_type': 'evs_disk_type',
        'org_disk_size': 'org_disk_size',
        'database_type': 'database_type',
        'resource_password': 'resource_password',
        'orderer_node_number': 'orderer_node_number',
        'use_eip': 'use_eip',
        'bandwidth_size': 'bandwidth_size',
        'cluster_type': 'cluster_type',
        'create_new_cluster': 'create_new_cluster',
        'cce_cluster_info': 'cce_cluster_info',
        'cce_create_info': 'cce_create_info',
        'ief_deploy_mode': 'ief_deploy_mode',
        'ief_nodes_info': 'ief_nodes_info',
        'peer_orgs': 'peer_orgs',
        'channels': 'channels',
        'couchdb_info': 'couchdb_info',
        'turbo_info': 'turbo_info',
        'block_info': 'block_info',
        'kafka_create_info': 'kafka_create_info',
        'tc3_need': 'tc3_need',
        'restful_api_support': 'restful_api_support',
        'is_invitee': 'is_invitee',
        'invitor_infos': 'invitor_infos'
    }

    def __init__(self, name=None, version_type=None, fabric_version=None, blockchain_type=None, consensus=None, sign_algorithm=None, enterprise_project_id=None, volume_type=None, evs_disk_type=None, org_disk_size=None, database_type=None, resource_password=None, orderer_node_number=None, use_eip=None, bandwidth_size=None, cluster_type=None, create_new_cluster=None, cce_cluster_info=None, cce_create_info=None, ief_deploy_mode=None, ief_nodes_info=None, peer_orgs=None, channels=None, couchdb_info=None, turbo_info=None, block_info=None, kafka_create_info=None, tc3_need=None, restful_api_support=None, is_invitee=None, invitor_infos=None):
        """CreateRequestBody

        The model defined in huaweicloud sdk

        :param name: 区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。
        :type name: str
        :param version_type: BCS服务版本类型，可选：[基础版（4），专业版（2），企业版（3）](tag: hws)[基础版（4），专业版（2）](tag: hws_hk)。被邀请方创建时，和邀请方保持一致。
        :type version_type: int
        :param fabric_version: Fabric版本，当前邀请方以及私有链的创建仅可选：2.2 ;被邀请方创建时，和邀请方保持一致，1.4版本服务仅支持1.15及以下版本集群. 默认值为2.2.
        :type fabric_version: str
        :param blockchain_type: 区块链类型，默认私有链，可选：联盟链（union），私有链（private）。被邀请方创建时，和邀请方保持一致。
        :type blockchain_type: str
        :param consensus: BCS服务的共识策略，Fabric1.4版本可选：测试策略（solo）、快速拜占庭容错算法（SFLIC）；Fabric2.2版本可选：raft共识算法（etcdraft）、快速拜占庭容错算法（SFLIC）。被邀请方创建时，和邀请方保持一致。
        :type consensus: str
        :param sign_algorithm: BCS服务安全机制，可选：ECDSA（ECDSA），国密算法（sm2）
        :type sign_algorithm: str
        :param enterprise_project_id: BCS服务所属企业项目ID
        :type enterprise_project_id: str
        :param volume_type: CCE集群存储卷类型，根据实际环境可选：云硬盘存储卷（evs），文件存储卷（nfs）, 极速文件存储卷（efs）
        :type volume_type: str
        :param evs_disk_type: 云硬盘存储卷类型，volume_type选择evs时必填，可选：普通I/O（SATA），高I/O（SAS），超高I/O（SSD）
        :type evs_disk_type: str
        :param org_disk_size: 节点组织存储容量，[基础版和专业版至少100GB，企业版至少500GB](tag: hws)[基础版和专业版至少100GB](tag: hws_hk)
        :type org_disk_size: int
        :param database_type: BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb），选择couchdb需要填写couchdb_info字段中的信息
        :type database_type: str
        :param resource_password: BCS服务资源、区块链管理密码
        :type resource_password: str
        :param orderer_node_number: 共识组织节点数，被邀请方创实例时可不填。购买fabric2.2服务时必填，若共识策略为Raft（CFT），节点数为3；若共识策略为快速拜占庭容错共识算法（FBFT），节点数为4。
        :type orderer_node_number: int
        :param use_eip: 是否使用集群节点弹性IP
        :type use_eip: bool
        :param bandwidth_size: 弹性IP带宽
        :type bandwidth_size: int
        :param cluster_type: 集群类型，可选：CCE集群 [,边缘集群ief](tag:hasief)。
        :type cluster_type: str
        :param create_new_cluster: 是否创建新集群，使用已有集群需要填写cce_cluster_info字段中的信息，创建新集群需要填写cce_create_info字段中的信息
        :type create_new_cluster: bool
        :param cce_cluster_info: 
        :type cce_cluster_info: :class:`huaweicloudsdkbcs.v2.CCEClusterInfo`
        :param cce_create_info: 
        :type cce_create_info: :class:`huaweicloudsdkbcs.v2.CCECreateInfo`
        :param ief_deploy_mode: IEF集群部署方式，随机部署（0），组织节点绑定（1）。组织节点绑定模式时，peer_orgs 参数必填。组织名和IEF节点名必须一致。
        :type ief_deploy_mode: int
        :param ief_nodes_info: IEF集群节点列表，使用边缘集群模式部署时必填。
        :type ief_nodes_info: list[:class:`huaweicloudsdkbcs.v2.IEFNode`]
        :param peer_orgs: 节点组织列表。节点绑定模式中，组织名和IEF节点名必须一致。边缘集群模式时此字段必填。
        :type peer_orgs: list[:class:`huaweicloudsdkbcs.v2.OrgPeer`]
        :param channels: 通道列表
        :type channels: list[:class:`huaweicloudsdkbcs.v2.ChannelInfoV2`]
        :param couchdb_info: 
        :type couchdb_info: :class:`huaweicloudsdkbcs.v2.CouchDb`
        :param turbo_info: 
        :type turbo_info: :class:`huaweicloudsdkbcs.v2.TurboInfo`
        :param block_info: 
        :type block_info: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        :param kafka_create_info: 
        :type kafka_create_info: :class:`huaweicloudsdkbcs.v2.KafkaCreateInfo`
        :param tc3_need: 是否添加可信计算平台
        :type tc3_need: bool
        :param restful_api_support: 是否添加restful API支持
        :type restful_api_support: bool
        :param is_invitee: 是否是创建被邀请方BCS服务实例，创建被邀请方实例需要同时填写invitor_infos字段中的信息
        :type is_invitee: bool
        :param invitor_infos: 
        :type invitor_infos: :class:`huaweicloudsdkbcs.v2.InvitorInfos`
        """
        
        

        self._name = None
        self._version_type = None
        self._fabric_version = None
        self._blockchain_type = None
        self._consensus = None
        self._sign_algorithm = None
        self._enterprise_project_id = None
        self._volume_type = None
        self._evs_disk_type = None
        self._org_disk_size = None
        self._database_type = None
        self._resource_password = None
        self._orderer_node_number = None
        self._use_eip = None
        self._bandwidth_size = None
        self._cluster_type = None
        self._create_new_cluster = None
        self._cce_cluster_info = None
        self._cce_create_info = None
        self._ief_deploy_mode = None
        self._ief_nodes_info = None
        self._peer_orgs = None
        self._channels = None
        self._couchdb_info = None
        self._turbo_info = None
        self._block_info = None
        self._kafka_create_info = None
        self._tc3_need = None
        self._restful_api_support = None
        self._is_invitee = None
        self._invitor_infos = None
        self.discriminator = None

        self.name = name
        self.version_type = version_type
        if fabric_version is not None:
            self.fabric_version = fabric_version
        if blockchain_type is not None:
            self.blockchain_type = blockchain_type
        if consensus is not None:
            self.consensus = consensus
        if sign_algorithm is not None:
            self.sign_algorithm = sign_algorithm
        self.enterprise_project_id = enterprise_project_id
        if volume_type is not None:
            self.volume_type = volume_type
        if evs_disk_type is not None:
            self.evs_disk_type = evs_disk_type
        if org_disk_size is not None:
            self.org_disk_size = org_disk_size
        if database_type is not None:
            self.database_type = database_type
        self.resource_password = resource_password
        if orderer_node_number is not None:
            self.orderer_node_number = orderer_node_number
        if use_eip is not None:
            self.use_eip = use_eip
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.cluster_type = cluster_type
        self.create_new_cluster = create_new_cluster
        if cce_cluster_info is not None:
            self.cce_cluster_info = cce_cluster_info
        if cce_create_info is not None:
            self.cce_create_info = cce_create_info
        if ief_deploy_mode is not None:
            self.ief_deploy_mode = ief_deploy_mode
        if ief_nodes_info is not None:
            self.ief_nodes_info = ief_nodes_info
        if peer_orgs is not None:
            self.peer_orgs = peer_orgs
        if channels is not None:
            self.channels = channels
        if couchdb_info is not None:
            self.couchdb_info = couchdb_info
        if turbo_info is not None:
            self.turbo_info = turbo_info
        if block_info is not None:
            self.block_info = block_info
        if kafka_create_info is not None:
            self.kafka_create_info = kafka_create_info
        if tc3_need is not None:
            self.tc3_need = tc3_need
        if restful_api_support is not None:
            self.restful_api_support = restful_api_support
        if is_invitee is not None:
            self.is_invitee = is_invitee
        if invitor_infos is not None:
            self.invitor_infos = invitor_infos

    @property
    def name(self):
        """Gets the name of this CreateRequestBody.

        区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。

        :return: The name of this CreateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRequestBody.

        区块链服务名称，支持英文，数字，中文字符和中划线(-)，不能以中划线(-)开头，长度4-24个字符。

        :param name: The name of this CreateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def version_type(self):
        """Gets the version_type of this CreateRequestBody.

        BCS服务版本类型，可选：[基础版（4），专业版（2），企业版（3）](tag: hws)[基础版（4），专业版（2）](tag: hws_hk)。被邀请方创建时，和邀请方保持一致。

        :return: The version_type of this CreateRequestBody.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this CreateRequestBody.

        BCS服务版本类型，可选：[基础版（4），专业版（2），企业版（3）](tag: hws)[基础版（4），专业版（2）](tag: hws_hk)。被邀请方创建时，和邀请方保持一致。

        :param version_type: The version_type of this CreateRequestBody.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def fabric_version(self):
        """Gets the fabric_version of this CreateRequestBody.

        Fabric版本，当前邀请方以及私有链的创建仅可选：2.2 ;被邀请方创建时，和邀请方保持一致，1.4版本服务仅支持1.15及以下版本集群. 默认值为2.2.

        :return: The fabric_version of this CreateRequestBody.
        :rtype: str
        """
        return self._fabric_version

    @fabric_version.setter
    def fabric_version(self, fabric_version):
        """Sets the fabric_version of this CreateRequestBody.

        Fabric版本，当前邀请方以及私有链的创建仅可选：2.2 ;被邀请方创建时，和邀请方保持一致，1.4版本服务仅支持1.15及以下版本集群. 默认值为2.2.

        :param fabric_version: The fabric_version of this CreateRequestBody.
        :type fabric_version: str
        """
        self._fabric_version = fabric_version

    @property
    def blockchain_type(self):
        """Gets the blockchain_type of this CreateRequestBody.

        区块链类型，默认私有链，可选：联盟链（union），私有链（private）。被邀请方创建时，和邀请方保持一致。

        :return: The blockchain_type of this CreateRequestBody.
        :rtype: str
        """
        return self._blockchain_type

    @blockchain_type.setter
    def blockchain_type(self, blockchain_type):
        """Sets the blockchain_type of this CreateRequestBody.

        区块链类型，默认私有链，可选：联盟链（union），私有链（private）。被邀请方创建时，和邀请方保持一致。

        :param blockchain_type: The blockchain_type of this CreateRequestBody.
        :type blockchain_type: str
        """
        self._blockchain_type = blockchain_type

    @property
    def consensus(self):
        """Gets the consensus of this CreateRequestBody.

        BCS服务的共识策略，Fabric1.4版本可选：测试策略（solo）、快速拜占庭容错算法（SFLIC）；Fabric2.2版本可选：raft共识算法（etcdraft）、快速拜占庭容错算法（SFLIC）。被邀请方创建时，和邀请方保持一致。

        :return: The consensus of this CreateRequestBody.
        :rtype: str
        """
        return self._consensus

    @consensus.setter
    def consensus(self, consensus):
        """Sets the consensus of this CreateRequestBody.

        BCS服务的共识策略，Fabric1.4版本可选：测试策略（solo）、快速拜占庭容错算法（SFLIC）；Fabric2.2版本可选：raft共识算法（etcdraft）、快速拜占庭容错算法（SFLIC）。被邀请方创建时，和邀请方保持一致。

        :param consensus: The consensus of this CreateRequestBody.
        :type consensus: str
        """
        self._consensus = consensus

    @property
    def sign_algorithm(self):
        """Gets the sign_algorithm of this CreateRequestBody.

        BCS服务安全机制，可选：ECDSA（ECDSA），国密算法（sm2）

        :return: The sign_algorithm of this CreateRequestBody.
        :rtype: str
        """
        return self._sign_algorithm

    @sign_algorithm.setter
    def sign_algorithm(self, sign_algorithm):
        """Sets the sign_algorithm of this CreateRequestBody.

        BCS服务安全机制，可选：ECDSA（ECDSA），国密算法（sm2）

        :param sign_algorithm: The sign_algorithm of this CreateRequestBody.
        :type sign_algorithm: str
        """
        self._sign_algorithm = sign_algorithm

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateRequestBody.

        BCS服务所属企业项目ID

        :return: The enterprise_project_id of this CreateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateRequestBody.

        BCS服务所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def volume_type(self):
        """Gets the volume_type of this CreateRequestBody.

        CCE集群存储卷类型，根据实际环境可选：云硬盘存储卷（evs），文件存储卷（nfs）, 极速文件存储卷（efs）

        :return: The volume_type of this CreateRequestBody.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this CreateRequestBody.

        CCE集群存储卷类型，根据实际环境可选：云硬盘存储卷（evs），文件存储卷（nfs）, 极速文件存储卷（efs）

        :param volume_type: The volume_type of this CreateRequestBody.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def evs_disk_type(self):
        """Gets the evs_disk_type of this CreateRequestBody.

        云硬盘存储卷类型，volume_type选择evs时必填，可选：普通I/O（SATA），高I/O（SAS），超高I/O（SSD）

        :return: The evs_disk_type of this CreateRequestBody.
        :rtype: str
        """
        return self._evs_disk_type

    @evs_disk_type.setter
    def evs_disk_type(self, evs_disk_type):
        """Sets the evs_disk_type of this CreateRequestBody.

        云硬盘存储卷类型，volume_type选择evs时必填，可选：普通I/O（SATA），高I/O（SAS），超高I/O（SSD）

        :param evs_disk_type: The evs_disk_type of this CreateRequestBody.
        :type evs_disk_type: str
        """
        self._evs_disk_type = evs_disk_type

    @property
    def org_disk_size(self):
        """Gets the org_disk_size of this CreateRequestBody.

        节点组织存储容量，[基础版和专业版至少100GB，企业版至少500GB](tag: hws)[基础版和专业版至少100GB](tag: hws_hk)

        :return: The org_disk_size of this CreateRequestBody.
        :rtype: int
        """
        return self._org_disk_size

    @org_disk_size.setter
    def org_disk_size(self, org_disk_size):
        """Sets the org_disk_size of this CreateRequestBody.

        节点组织存储容量，[基础版和专业版至少100GB，企业版至少500GB](tag: hws)[基础版和专业版至少100GB](tag: hws_hk)

        :param org_disk_size: The org_disk_size of this CreateRequestBody.
        :type org_disk_size: int
        """
        self._org_disk_size = org_disk_size

    @property
    def database_type(self):
        """Gets the database_type of this CreateRequestBody.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb），选择couchdb需要填写couchdb_info字段中的信息

        :return: The database_type of this CreateRequestBody.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """Sets the database_type of this CreateRequestBody.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb），选择couchdb需要填写couchdb_info字段中的信息

        :param database_type: The database_type of this CreateRequestBody.
        :type database_type: str
        """
        self._database_type = database_type

    @property
    def resource_password(self):
        """Gets the resource_password of this CreateRequestBody.

        BCS服务资源、区块链管理密码

        :return: The resource_password of this CreateRequestBody.
        :rtype: str
        """
        return self._resource_password

    @resource_password.setter
    def resource_password(self, resource_password):
        """Sets the resource_password of this CreateRequestBody.

        BCS服务资源、区块链管理密码

        :param resource_password: The resource_password of this CreateRequestBody.
        :type resource_password: str
        """
        self._resource_password = resource_password

    @property
    def orderer_node_number(self):
        """Gets the orderer_node_number of this CreateRequestBody.

        共识组织节点数，被邀请方创实例时可不填。购买fabric2.2服务时必填，若共识策略为Raft（CFT），节点数为3；若共识策略为快速拜占庭容错共识算法（FBFT），节点数为4。

        :return: The orderer_node_number of this CreateRequestBody.
        :rtype: int
        """
        return self._orderer_node_number

    @orderer_node_number.setter
    def orderer_node_number(self, orderer_node_number):
        """Sets the orderer_node_number of this CreateRequestBody.

        共识组织节点数，被邀请方创实例时可不填。购买fabric2.2服务时必填，若共识策略为Raft（CFT），节点数为3；若共识策略为快速拜占庭容错共识算法（FBFT），节点数为4。

        :param orderer_node_number: The orderer_node_number of this CreateRequestBody.
        :type orderer_node_number: int
        """
        self._orderer_node_number = orderer_node_number

    @property
    def use_eip(self):
        """Gets the use_eip of this CreateRequestBody.

        是否使用集群节点弹性IP

        :return: The use_eip of this CreateRequestBody.
        :rtype: bool
        """
        return self._use_eip

    @use_eip.setter
    def use_eip(self, use_eip):
        """Sets the use_eip of this CreateRequestBody.

        是否使用集群节点弹性IP

        :param use_eip: The use_eip of this CreateRequestBody.
        :type use_eip: bool
        """
        self._use_eip = use_eip

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CreateRequestBody.

        弹性IP带宽

        :return: The bandwidth_size of this CreateRequestBody.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CreateRequestBody.

        弹性IP带宽

        :param bandwidth_size: The bandwidth_size of this CreateRequestBody.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def cluster_type(self):
        """Gets the cluster_type of this CreateRequestBody.

        集群类型，可选：CCE集群 [,边缘集群ief](tag:hasief)。

        :return: The cluster_type of this CreateRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this CreateRequestBody.

        集群类型，可选：CCE集群 [,边缘集群ief](tag:hasief)。

        :param cluster_type: The cluster_type of this CreateRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def create_new_cluster(self):
        """Gets the create_new_cluster of this CreateRequestBody.

        是否创建新集群，使用已有集群需要填写cce_cluster_info字段中的信息，创建新集群需要填写cce_create_info字段中的信息

        :return: The create_new_cluster of this CreateRequestBody.
        :rtype: bool
        """
        return self._create_new_cluster

    @create_new_cluster.setter
    def create_new_cluster(self, create_new_cluster):
        """Sets the create_new_cluster of this CreateRequestBody.

        是否创建新集群，使用已有集群需要填写cce_cluster_info字段中的信息，创建新集群需要填写cce_create_info字段中的信息

        :param create_new_cluster: The create_new_cluster of this CreateRequestBody.
        :type create_new_cluster: bool
        """
        self._create_new_cluster = create_new_cluster

    @property
    def cce_cluster_info(self):
        """Gets the cce_cluster_info of this CreateRequestBody.

        :return: The cce_cluster_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.CCEClusterInfo`
        """
        return self._cce_cluster_info

    @cce_cluster_info.setter
    def cce_cluster_info(self, cce_cluster_info):
        """Sets the cce_cluster_info of this CreateRequestBody.

        :param cce_cluster_info: The cce_cluster_info of this CreateRequestBody.
        :type cce_cluster_info: :class:`huaweicloudsdkbcs.v2.CCEClusterInfo`
        """
        self._cce_cluster_info = cce_cluster_info

    @property
    def cce_create_info(self):
        """Gets the cce_create_info of this CreateRequestBody.

        :return: The cce_create_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.CCECreateInfo`
        """
        return self._cce_create_info

    @cce_create_info.setter
    def cce_create_info(self, cce_create_info):
        """Sets the cce_create_info of this CreateRequestBody.

        :param cce_create_info: The cce_create_info of this CreateRequestBody.
        :type cce_create_info: :class:`huaweicloudsdkbcs.v2.CCECreateInfo`
        """
        self._cce_create_info = cce_create_info

    @property
    def ief_deploy_mode(self):
        """Gets the ief_deploy_mode of this CreateRequestBody.

        IEF集群部署方式，随机部署（0），组织节点绑定（1）。组织节点绑定模式时，peer_orgs 参数必填。组织名和IEF节点名必须一致。

        :return: The ief_deploy_mode of this CreateRequestBody.
        :rtype: int
        """
        return self._ief_deploy_mode

    @ief_deploy_mode.setter
    def ief_deploy_mode(self, ief_deploy_mode):
        """Sets the ief_deploy_mode of this CreateRequestBody.

        IEF集群部署方式，随机部署（0），组织节点绑定（1）。组织节点绑定模式时，peer_orgs 参数必填。组织名和IEF节点名必须一致。

        :param ief_deploy_mode: The ief_deploy_mode of this CreateRequestBody.
        :type ief_deploy_mode: int
        """
        self._ief_deploy_mode = ief_deploy_mode

    @property
    def ief_nodes_info(self):
        """Gets the ief_nodes_info of this CreateRequestBody.

        IEF集群节点列表，使用边缘集群模式部署时必填。

        :return: The ief_nodes_info of this CreateRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.IEFNode`]
        """
        return self._ief_nodes_info

    @ief_nodes_info.setter
    def ief_nodes_info(self, ief_nodes_info):
        """Sets the ief_nodes_info of this CreateRequestBody.

        IEF集群节点列表，使用边缘集群模式部署时必填。

        :param ief_nodes_info: The ief_nodes_info of this CreateRequestBody.
        :type ief_nodes_info: list[:class:`huaweicloudsdkbcs.v2.IEFNode`]
        """
        self._ief_nodes_info = ief_nodes_info

    @property
    def peer_orgs(self):
        """Gets the peer_orgs of this CreateRequestBody.

        节点组织列表。节点绑定模式中，组织名和IEF节点名必须一致。边缘集群模式时此字段必填。

        :return: The peer_orgs of this CreateRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.OrgPeer`]
        """
        return self._peer_orgs

    @peer_orgs.setter
    def peer_orgs(self, peer_orgs):
        """Sets the peer_orgs of this CreateRequestBody.

        节点组织列表。节点绑定模式中，组织名和IEF节点名必须一致。边缘集群模式时此字段必填。

        :param peer_orgs: The peer_orgs of this CreateRequestBody.
        :type peer_orgs: list[:class:`huaweicloudsdkbcs.v2.OrgPeer`]
        """
        self._peer_orgs = peer_orgs

    @property
    def channels(self):
        """Gets the channels of this CreateRequestBody.

        通道列表

        :return: The channels of this CreateRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.ChannelInfoV2`]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this CreateRequestBody.

        通道列表

        :param channels: The channels of this CreateRequestBody.
        :type channels: list[:class:`huaweicloudsdkbcs.v2.ChannelInfoV2`]
        """
        self._channels = channels

    @property
    def couchdb_info(self):
        """Gets the couchdb_info of this CreateRequestBody.

        :return: The couchdb_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.CouchDb`
        """
        return self._couchdb_info

    @couchdb_info.setter
    def couchdb_info(self, couchdb_info):
        """Sets the couchdb_info of this CreateRequestBody.

        :param couchdb_info: The couchdb_info of this CreateRequestBody.
        :type couchdb_info: :class:`huaweicloudsdkbcs.v2.CouchDb`
        """
        self._couchdb_info = couchdb_info

    @property
    def turbo_info(self):
        """Gets the turbo_info of this CreateRequestBody.

        :return: The turbo_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.TurboInfo`
        """
        return self._turbo_info

    @turbo_info.setter
    def turbo_info(self, turbo_info):
        """Sets the turbo_info of this CreateRequestBody.

        :param turbo_info: The turbo_info of this CreateRequestBody.
        :type turbo_info: :class:`huaweicloudsdkbcs.v2.TurboInfo`
        """
        self._turbo_info = turbo_info

    @property
    def block_info(self):
        """Gets the block_info of this CreateRequestBody.

        :return: The block_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        """
        return self._block_info

    @block_info.setter
    def block_info(self, block_info):
        """Sets the block_info of this CreateRequestBody.

        :param block_info: The block_info of this CreateRequestBody.
        :type block_info: :class:`huaweicloudsdkbcs.v2.CreateRequestBodyBlockInfo`
        """
        self._block_info = block_info

    @property
    def kafka_create_info(self):
        """Gets the kafka_create_info of this CreateRequestBody.

        :return: The kafka_create_info of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.KafkaCreateInfo`
        """
        return self._kafka_create_info

    @kafka_create_info.setter
    def kafka_create_info(self, kafka_create_info):
        """Sets the kafka_create_info of this CreateRequestBody.

        :param kafka_create_info: The kafka_create_info of this CreateRequestBody.
        :type kafka_create_info: :class:`huaweicloudsdkbcs.v2.KafkaCreateInfo`
        """
        self._kafka_create_info = kafka_create_info

    @property
    def tc3_need(self):
        """Gets the tc3_need of this CreateRequestBody.

        是否添加可信计算平台

        :return: The tc3_need of this CreateRequestBody.
        :rtype: bool
        """
        return self._tc3_need

    @tc3_need.setter
    def tc3_need(self, tc3_need):
        """Sets the tc3_need of this CreateRequestBody.

        是否添加可信计算平台

        :param tc3_need: The tc3_need of this CreateRequestBody.
        :type tc3_need: bool
        """
        self._tc3_need = tc3_need

    @property
    def restful_api_support(self):
        """Gets the restful_api_support of this CreateRequestBody.

        是否添加restful API支持

        :return: The restful_api_support of this CreateRequestBody.
        :rtype: bool
        """
        return self._restful_api_support

    @restful_api_support.setter
    def restful_api_support(self, restful_api_support):
        """Sets the restful_api_support of this CreateRequestBody.

        是否添加restful API支持

        :param restful_api_support: The restful_api_support of this CreateRequestBody.
        :type restful_api_support: bool
        """
        self._restful_api_support = restful_api_support

    @property
    def is_invitee(self):
        """Gets the is_invitee of this CreateRequestBody.

        是否是创建被邀请方BCS服务实例，创建被邀请方实例需要同时填写invitor_infos字段中的信息

        :return: The is_invitee of this CreateRequestBody.
        :rtype: bool
        """
        return self._is_invitee

    @is_invitee.setter
    def is_invitee(self, is_invitee):
        """Sets the is_invitee of this CreateRequestBody.

        是否是创建被邀请方BCS服务实例，创建被邀请方实例需要同时填写invitor_infos字段中的信息

        :param is_invitee: The is_invitee of this CreateRequestBody.
        :type is_invitee: bool
        """
        self._is_invitee = is_invitee

    @property
    def invitor_infos(self):
        """Gets the invitor_infos of this CreateRequestBody.

        :return: The invitor_infos of this CreateRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.InvitorInfos`
        """
        return self._invitor_infos

    @invitor_infos.setter
    def invitor_infos(self, invitor_infos):
        """Sets the invitor_infos of this CreateRequestBody.

        :param invitor_infos: The invitor_infos of this CreateRequestBody.
        :type invitor_infos: :class:`huaweicloudsdkbcs.v2.InvitorInfos`
        """
        self._invitor_infos = invitor_infos

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
        if not isinstance(other, CreateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
