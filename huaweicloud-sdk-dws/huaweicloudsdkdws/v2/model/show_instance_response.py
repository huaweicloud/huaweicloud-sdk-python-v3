# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_status': 'str',
        'params_group_id': 'str',
        'type': 'str',
        'subnet_id': 'str',
        'role': 'str',
        'internal_subnet_id': 'str',
        'group': 'str',
        'secure_group': 'str',
        'vpc': 'str',
        'azcode': 'str',
        'region': 'str',
        'cluster_id': 'str',
        'created': 'str',
        'updated': 'str',
        'status': 'str',
        'name': 'str',
        'links': 'list[LinkResp]',
        'id': 'str',
        'flavor': 'ClusterFlavorResp',
        'volume': 'CompatibleInstanceVolumeResp',
        'datastore': 'CompatibleDataStoreResp',
        'fault': 'CompatibleFaultResp',
        'configuration': 'CompatibleConfigurationResp',
        'locality': 'str',
        'replicas': 'list[CompatibleReplicasResp]',
        'db_user': 'str',
        'storage_engine': 'str',
        'pay_model': 'int',
        'public_ip': 'str',
        'traffic_ip': 'str'
    }

    attribute_map = {
        'configuration_status': 'configuration_status',
        'params_group_id': 'params_group_id',
        'type': 'type',
        'subnet_id': 'subnet_id',
        'role': 'role',
        'internal_subnet_id': 'internal_subnet_id',
        'group': 'group',
        'secure_group': 'secure_group',
        'vpc': 'vpc',
        'azcode': 'azcode',
        'region': 'region',
        'cluster_id': 'cluster_id',
        'created': 'created',
        'updated': 'updated',
        'status': 'status',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'flavor': 'flavor',
        'volume': 'volume',
        'datastore': 'datastore',
        'fault': 'fault',
        'configuration': 'configuration',
        'locality': 'locality',
        'replicas': 'replicas',
        'db_user': 'db_user',
        'storage_engine': 'storage_engine',
        'pay_model': 'pay_model',
        'public_ip': 'public_ip',
        'traffic_ip': 'traffic_ip'
    }

    def __init__(self, configuration_status=None, params_group_id=None, type=None, subnet_id=None, role=None, internal_subnet_id=None, group=None, secure_group=None, vpc=None, azcode=None, region=None, cluster_id=None, created=None, updated=None, status=None, name=None, links=None, id=None, flavor=None, volume=None, datastore=None, fault=None, configuration=None, locality=None, replicas=None, db_user=None, storage_engine=None, pay_model=None, public_ip=None, traffic_ip=None):
        r"""ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param configuration_status: **参数解释**： 配置状态。 **取值范围**： 不涉及。
        :type configuration_status: str
        :param params_group_id: **参数解释**： 参数组ID。 **取值范围**： 不涉及。
        :type params_group_id: str
        :param type: **参数解释**： 类型。 **取值范围**： 不涉及。
        :type type: str
        :param subnet_id: **参数解释**： 子网ID。 **取值范围**： 不涉及。
        :type subnet_id: str
        :param role: **参数解释**： 角色。 **取值范围**： 不涉及。
        :type role: str
        :param internal_subnet_id: **参数解释**： 内部子网ID。 **取值范围**： 不涉及。
        :type internal_subnet_id: str
        :param group: **参数解释**： 分组信息。 **取值范围**： 不涉及。
        :type group: str
        :param secure_group: **参数解释**： 安全组。 **取值范围**： 不涉及。
        :type secure_group: str
        :param vpc: **参数解释**： VPC ID。 **取值范围**： 不涉及。
        :type vpc: str
        :param azcode: **参数解释**： 可用区编码。 **取值范围**： 不涉及。
        :type azcode: str
        :param region: **参数解释**： 局点编码。 **取值范围**： 不涉及。
        :type region: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        :param created: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created: str
        :param updated: **参数解释**： 更新时间。 **取值范围**： 不涉及。
        :type updated: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param name: **参数解释**： 节点名称。 **取值范围**： 不涉及。
        :type name: str
        :param links: **参数解释**： 链接信息。 **取值范围**： 不涉及。
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        :param id: **参数解释**： 节点ID。 **取值范围**： 不涉及。
        :type id: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdws.v2.ClusterFlavorResp`
        :param volume: 
        :type volume: :class:`huaweicloudsdkdws.v2.CompatibleInstanceVolumeResp`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdws.v2.CompatibleDataStoreResp`
        :param fault: 
        :type fault: :class:`huaweicloudsdkdws.v2.CompatibleFaultResp`
        :param configuration: 
        :type configuration: :class:`huaweicloudsdkdws.v2.CompatibleConfigurationResp`
        :param locality: **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。
        :type locality: str
        :param replicas: **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。
        :type replicas: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        :param db_user: **参数解释**： 数据库用户。 **取值范围**： 不涉及。
        :type db_user: str
        :param storage_engine: **参数解释**： 存储引擎。 **取值范围**： 不涉及。
        :type storage_engine: str
        :param pay_model: **参数解释**： 付款方式。 **取值范围**： 不涉及。
        :type pay_model: int
        :param public_ip: **参数解释**： 公网IP。 **取值范围**： 不涉及。
        :type public_ip: str
        :param traffic_ip: **参数解释**： 流量IP。 **取值范围**： 不涉及。
        :type traffic_ip: str
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._configuration_status = None
        self._params_group_id = None
        self._type = None
        self._subnet_id = None
        self._role = None
        self._internal_subnet_id = None
        self._group = None
        self._secure_group = None
        self._vpc = None
        self._azcode = None
        self._region = None
        self._cluster_id = None
        self._created = None
        self._updated = None
        self._status = None
        self._name = None
        self._links = None
        self._id = None
        self._flavor = None
        self._volume = None
        self._datastore = None
        self._fault = None
        self._configuration = None
        self._locality = None
        self._replicas = None
        self._db_user = None
        self._storage_engine = None
        self._pay_model = None
        self._public_ip = None
        self._traffic_ip = None
        self.discriminator = None

        if configuration_status is not None:
            self.configuration_status = configuration_status
        if params_group_id is not None:
            self.params_group_id = params_group_id
        if type is not None:
            self.type = type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if role is not None:
            self.role = role
        if internal_subnet_id is not None:
            self.internal_subnet_id = internal_subnet_id
        if group is not None:
            self.group = group
        if secure_group is not None:
            self.secure_group = secure_group
        if vpc is not None:
            self.vpc = vpc
        if azcode is not None:
            self.azcode = azcode
        if region is not None:
            self.region = region
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if flavor is not None:
            self.flavor = flavor
        if volume is not None:
            self.volume = volume
        if datastore is not None:
            self.datastore = datastore
        if fault is not None:
            self.fault = fault
        if configuration is not None:
            self.configuration = configuration
        if locality is not None:
            self.locality = locality
        if replicas is not None:
            self.replicas = replicas
        if db_user is not None:
            self.db_user = db_user
        if storage_engine is not None:
            self.storage_engine = storage_engine
        if pay_model is not None:
            self.pay_model = pay_model
        if public_ip is not None:
            self.public_ip = public_ip
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip

    @property
    def configuration_status(self):
        r"""Gets the configuration_status of this ShowInstanceResponse.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :return: The configuration_status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, configuration_status):
        r"""Sets the configuration_status of this ShowInstanceResponse.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :param configuration_status: The configuration_status of this ShowInstanceResponse.
        :type configuration_status: str
        """
        self._configuration_status = configuration_status

    @property
    def params_group_id(self):
        r"""Gets the params_group_id of this ShowInstanceResponse.

        **参数解释**： 参数组ID。 **取值范围**： 不涉及。

        :return: The params_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._params_group_id

    @params_group_id.setter
    def params_group_id(self, params_group_id):
        r"""Sets the params_group_id of this ShowInstanceResponse.

        **参数解释**： 参数组ID。 **取值范围**： 不涉及。

        :param params_group_id: The params_group_id of this ShowInstanceResponse.
        :type params_group_id: str
        """
        self._params_group_id = params_group_id

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceResponse.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :return: The type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceResponse.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :param type: The type of this ShowInstanceResponse.
        :type type: str
        """
        self._type = type

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowInstanceResponse.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowInstanceResponse.

        **参数解释**： 子网ID。 **取值范围**： 不涉及。

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def role(self):
        r"""Gets the role of this ShowInstanceResponse.

        **参数解释**： 角色。 **取值范围**： 不涉及。

        :return: The role of this ShowInstanceResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ShowInstanceResponse.

        **参数解释**： 角色。 **取值范围**： 不涉及。

        :param role: The role of this ShowInstanceResponse.
        :type role: str
        """
        self._role = role

    @property
    def internal_subnet_id(self):
        r"""Gets the internal_subnet_id of this ShowInstanceResponse.

        **参数解释**： 内部子网ID。 **取值范围**： 不涉及。

        :return: The internal_subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._internal_subnet_id

    @internal_subnet_id.setter
    def internal_subnet_id(self, internal_subnet_id):
        r"""Sets the internal_subnet_id of this ShowInstanceResponse.

        **参数解释**： 内部子网ID。 **取值范围**： 不涉及。

        :param internal_subnet_id: The internal_subnet_id of this ShowInstanceResponse.
        :type internal_subnet_id: str
        """
        self._internal_subnet_id = internal_subnet_id

    @property
    def group(self):
        r"""Gets the group of this ShowInstanceResponse.

        **参数解释**： 分组信息。 **取值范围**： 不涉及。

        :return: The group of this ShowInstanceResponse.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ShowInstanceResponse.

        **参数解释**： 分组信息。 **取值范围**： 不涉及。

        :param group: The group of this ShowInstanceResponse.
        :type group: str
        """
        self._group = group

    @property
    def secure_group(self):
        r"""Gets the secure_group of this ShowInstanceResponse.

        **参数解释**： 安全组。 **取值范围**： 不涉及。

        :return: The secure_group of this ShowInstanceResponse.
        :rtype: str
        """
        return self._secure_group

    @secure_group.setter
    def secure_group(self, secure_group):
        r"""Sets the secure_group of this ShowInstanceResponse.

        **参数解释**： 安全组。 **取值范围**： 不涉及。

        :param secure_group: The secure_group of this ShowInstanceResponse.
        :type secure_group: str
        """
        self._secure_group = secure_group

    @property
    def vpc(self):
        r"""Gets the vpc of this ShowInstanceResponse.

        **参数解释**： VPC ID。 **取值范围**： 不涉及。

        :return: The vpc of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this ShowInstanceResponse.

        **参数解释**： VPC ID。 **取值范围**： 不涉及。

        :param vpc: The vpc of this ShowInstanceResponse.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def azcode(self):
        r"""Gets the azcode of this ShowInstanceResponse.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :return: The azcode of this ShowInstanceResponse.
        :rtype: str
        """
        return self._azcode

    @azcode.setter
    def azcode(self, azcode):
        r"""Sets the azcode of this ShowInstanceResponse.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :param azcode: The azcode of this ShowInstanceResponse.
        :type azcode: str
        """
        self._azcode = azcode

    @property
    def region(self):
        r"""Gets the region of this ShowInstanceResponse.

        **参数解释**： 局点编码。 **取值范围**： 不涉及。

        :return: The region of this ShowInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowInstanceResponse.

        **参数解释**： 局点编码。 **取值范围**： 不涉及。

        :param region: The region of this ShowInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowInstanceResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowInstanceResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this ShowInstanceResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def created(self):
        r"""Gets the created of this ShowInstanceResponse.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowInstanceResponse.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created: The created of this ShowInstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowInstanceResponse.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :return: The updated of this ShowInstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowInstanceResponse.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :param updated: The updated of this ShowInstanceResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceResponse.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceResponse.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceResponse.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceResponse.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        r"""Gets the links of this ShowInstanceResponse.

        **参数解释**： 链接信息。 **取值范围**： 不涉及。

        :return: The links of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ShowInstanceResponse.

        **参数解释**： 链接信息。 **取值范围**： 不涉及。

        :param links: The links of this ShowInstanceResponse.
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        self._links = links

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :return: The id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceResponse.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :param id: The id of this ShowInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def flavor(self):
        r"""Gets the flavor of this ShowInstanceResponse.

        :return: The flavor of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.ClusterFlavorResp`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ShowInstanceResponse.

        :param flavor: The flavor of this ShowInstanceResponse.
        :type flavor: :class:`huaweicloudsdkdws.v2.ClusterFlavorResp`
        """
        self._flavor = flavor

    @property
    def volume(self):
        r"""Gets the volume of this ShowInstanceResponse.

        :return: The volume of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleInstanceVolumeResp`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this ShowInstanceResponse.

        :param volume: The volume of this ShowInstanceResponse.
        :type volume: :class:`huaweicloudsdkdws.v2.CompatibleInstanceVolumeResp`
        """
        self._volume = volume

    @property
    def datastore(self):
        r"""Gets the datastore of this ShowInstanceResponse.

        :return: The datastore of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleDataStoreResp`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ShowInstanceResponse.

        :param datastore: The datastore of this ShowInstanceResponse.
        :type datastore: :class:`huaweicloudsdkdws.v2.CompatibleDataStoreResp`
        """
        self._datastore = datastore

    @property
    def fault(self):
        r"""Gets the fault of this ShowInstanceResponse.

        :return: The fault of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleFaultResp`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        r"""Sets the fault of this ShowInstanceResponse.

        :param fault: The fault of this ShowInstanceResponse.
        :type fault: :class:`huaweicloudsdkdws.v2.CompatibleFaultResp`
        """
        self._fault = fault

    @property
    def configuration(self):
        r"""Gets the configuration of this ShowInstanceResponse.

        :return: The configuration of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleConfigurationResp`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this ShowInstanceResponse.

        :param configuration: The configuration of this ShowInstanceResponse.
        :type configuration: :class:`huaweicloudsdkdws.v2.CompatibleConfigurationResp`
        """
        self._configuration = configuration

    @property
    def locality(self):
        r"""Gets the locality of this ShowInstanceResponse.

        **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。

        :return: The locality of this ShowInstanceResponse.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        r"""Sets the locality of this ShowInstanceResponse.

        **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。

        :param locality: The locality of this ShowInstanceResponse.
        :type locality: str
        """
        self._locality = locality

    @property
    def replicas(self):
        r"""Gets the replicas of this ShowInstanceResponse.

        **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。

        :return: The replicas of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this ShowInstanceResponse.

        **参数解释**： 废弃字段，无实际含义。 **取值范围**： 不涉及。

        :param replicas: The replicas of this ShowInstanceResponse.
        :type replicas: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        """
        self._replicas = replicas

    @property
    def db_user(self):
        r"""Gets the db_user of this ShowInstanceResponse.

        **参数解释**： 数据库用户。 **取值范围**： 不涉及。

        :return: The db_user of this ShowInstanceResponse.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this ShowInstanceResponse.

        **参数解释**： 数据库用户。 **取值范围**： 不涉及。

        :param db_user: The db_user of this ShowInstanceResponse.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def storage_engine(self):
        r"""Gets the storage_engine of this ShowInstanceResponse.

        **参数解释**： 存储引擎。 **取值范围**： 不涉及。

        :return: The storage_engine of this ShowInstanceResponse.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        r"""Sets the storage_engine of this ShowInstanceResponse.

        **参数解释**： 存储引擎。 **取值范围**： 不涉及。

        :param storage_engine: The storage_engine of this ShowInstanceResponse.
        :type storage_engine: str
        """
        self._storage_engine = storage_engine

    @property
    def pay_model(self):
        r"""Gets the pay_model of this ShowInstanceResponse.

        **参数解释**： 付款方式。 **取值范围**： 不涉及。

        :return: The pay_model of this ShowInstanceResponse.
        :rtype: int
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this ShowInstanceResponse.

        **参数解释**： 付款方式。 **取值范围**： 不涉及。

        :param pay_model: The pay_model of this ShowInstanceResponse.
        :type pay_model: int
        """
        self._pay_model = pay_model

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ShowInstanceResponse.

        **参数解释**： 公网IP。 **取值范围**： 不涉及。

        :return: The public_ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ShowInstanceResponse.

        **参数解释**： 公网IP。 **取值范围**： 不涉及。

        :param public_ip: The public_ip of this ShowInstanceResponse.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def traffic_ip(self):
        r"""Gets the traffic_ip of this ShowInstanceResponse.

        **参数解释**： 流量IP。 **取值范围**： 不涉及。

        :return: The traffic_ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        r"""Sets the traffic_ip of this ShowInstanceResponse.

        **参数解释**： 流量IP。 **取值范围**： 不涉及。

        :param traffic_ip: The traffic_ip of this ShowInstanceResponse.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
