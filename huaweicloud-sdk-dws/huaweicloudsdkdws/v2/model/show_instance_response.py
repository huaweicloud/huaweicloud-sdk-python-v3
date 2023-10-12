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
        """ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param configuration_status: 配置状态
        :type configuration_status: str
        :param params_group_id: 参数组ID
        :type params_group_id: str
        :param type: 类型
        :type type: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param role: 角色
        :type role: str
        :param internal_subnet_id: 内部子网ID
        :type internal_subnet_id: str
        :param group: 组
        :type group: str
        :param secure_group: 安全组
        :type secure_group: str
        :param vpc: VPC
        :type vpc: str
        :param azcode: 编码
        :type azcode: str
        :param region: 区域
        :type region: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param created: 被创建的
        :type created: str
        :param updated: 被更新的
        :type updated: str
        :param status: 状态
        :type status: str
        :param name: 名称
        :type name: str
        :param links: 连接
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        :param id: ID
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
        :param locality: 地点
        :type locality: str
        :param replicas: 备份
        :type replicas: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        :param db_user: 数据库用户
        :type db_user: str
        :param storage_engine: 存储引擎
        :type storage_engine: str
        :param pay_model: 付款方式
        :type pay_model: int
        :param public_ip: 公网IP
        :type public_ip: str
        :param traffic_ip: 流量IP
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
        """Gets the configuration_status of this ShowInstanceResponse.

        配置状态

        :return: The configuration_status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, configuration_status):
        """Sets the configuration_status of this ShowInstanceResponse.

        配置状态

        :param configuration_status: The configuration_status of this ShowInstanceResponse.
        :type configuration_status: str
        """
        self._configuration_status = configuration_status

    @property
    def params_group_id(self):
        """Gets the params_group_id of this ShowInstanceResponse.

        参数组ID

        :return: The params_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._params_group_id

    @params_group_id.setter
    def params_group_id(self, params_group_id):
        """Sets the params_group_id of this ShowInstanceResponse.

        参数组ID

        :param params_group_id: The params_group_id of this ShowInstanceResponse.
        :type params_group_id: str
        """
        self._params_group_id = params_group_id

    @property
    def type(self):
        """Gets the type of this ShowInstanceResponse.

        类型

        :return: The type of this ShowInstanceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowInstanceResponse.

        类型

        :param type: The type of this ShowInstanceResponse.
        :type type: str
        """
        self._type = type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowInstanceResponse.

        子网ID

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowInstanceResponse.

        子网ID

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def role(self):
        """Gets the role of this ShowInstanceResponse.

        角色

        :return: The role of this ShowInstanceResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ShowInstanceResponse.

        角色

        :param role: The role of this ShowInstanceResponse.
        :type role: str
        """
        self._role = role

    @property
    def internal_subnet_id(self):
        """Gets the internal_subnet_id of this ShowInstanceResponse.

        内部子网ID

        :return: The internal_subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._internal_subnet_id

    @internal_subnet_id.setter
    def internal_subnet_id(self, internal_subnet_id):
        """Sets the internal_subnet_id of this ShowInstanceResponse.

        内部子网ID

        :param internal_subnet_id: The internal_subnet_id of this ShowInstanceResponse.
        :type internal_subnet_id: str
        """
        self._internal_subnet_id = internal_subnet_id

    @property
    def group(self):
        """Gets the group of this ShowInstanceResponse.

        组

        :return: The group of this ShowInstanceResponse.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ShowInstanceResponse.

        组

        :param group: The group of this ShowInstanceResponse.
        :type group: str
        """
        self._group = group

    @property
    def secure_group(self):
        """Gets the secure_group of this ShowInstanceResponse.

        安全组

        :return: The secure_group of this ShowInstanceResponse.
        :rtype: str
        """
        return self._secure_group

    @secure_group.setter
    def secure_group(self, secure_group):
        """Sets the secure_group of this ShowInstanceResponse.

        安全组

        :param secure_group: The secure_group of this ShowInstanceResponse.
        :type secure_group: str
        """
        self._secure_group = secure_group

    @property
    def vpc(self):
        """Gets the vpc of this ShowInstanceResponse.

        VPC

        :return: The vpc of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this ShowInstanceResponse.

        VPC

        :param vpc: The vpc of this ShowInstanceResponse.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def azcode(self):
        """Gets the azcode of this ShowInstanceResponse.

        编码

        :return: The azcode of this ShowInstanceResponse.
        :rtype: str
        """
        return self._azcode

    @azcode.setter
    def azcode(self, azcode):
        """Sets the azcode of this ShowInstanceResponse.

        编码

        :param azcode: The azcode of this ShowInstanceResponse.
        :type azcode: str
        """
        self._azcode = azcode

    @property
    def region(self):
        """Gets the region of this ShowInstanceResponse.

        区域

        :return: The region of this ShowInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowInstanceResponse.

        区域

        :param region: The region of this ShowInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowInstanceResponse.

        集群ID

        :return: The cluster_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowInstanceResponse.

        集群ID

        :param cluster_id: The cluster_id of this ShowInstanceResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def created(self):
        """Gets the created of this ShowInstanceResponse.

        被创建的

        :return: The created of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowInstanceResponse.

        被创建的

        :param created: The created of this ShowInstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ShowInstanceResponse.

        被更新的

        :return: The updated of this ShowInstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowInstanceResponse.

        被更新的

        :param updated: The updated of this ShowInstanceResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def status(self):
        """Gets the status of this ShowInstanceResponse.

        状态

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResponse.

        状态

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ShowInstanceResponse.

        名称

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceResponse.

        名称

        :param name: The name of this ShowInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        """Gets the links of this ShowInstanceResponse.

        连接

        :return: The links of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowInstanceResponse.

        连接

        :param links: The links of this ShowInstanceResponse.
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this ShowInstanceResponse.

        ID

        :return: The id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowInstanceResponse.

        ID

        :param id: The id of this ShowInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def flavor(self):
        """Gets the flavor of this ShowInstanceResponse.

        :return: The flavor of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.ClusterFlavorResp`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ShowInstanceResponse.

        :param flavor: The flavor of this ShowInstanceResponse.
        :type flavor: :class:`huaweicloudsdkdws.v2.ClusterFlavorResp`
        """
        self._flavor = flavor

    @property
    def volume(self):
        """Gets the volume of this ShowInstanceResponse.

        :return: The volume of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleInstanceVolumeResp`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ShowInstanceResponse.

        :param volume: The volume of this ShowInstanceResponse.
        :type volume: :class:`huaweicloudsdkdws.v2.CompatibleInstanceVolumeResp`
        """
        self._volume = volume

    @property
    def datastore(self):
        """Gets the datastore of this ShowInstanceResponse.

        :return: The datastore of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleDataStoreResp`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ShowInstanceResponse.

        :param datastore: The datastore of this ShowInstanceResponse.
        :type datastore: :class:`huaweicloudsdkdws.v2.CompatibleDataStoreResp`
        """
        self._datastore = datastore

    @property
    def fault(self):
        """Gets the fault of this ShowInstanceResponse.

        :return: The fault of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleFaultResp`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this ShowInstanceResponse.

        :param fault: The fault of this ShowInstanceResponse.
        :type fault: :class:`huaweicloudsdkdws.v2.CompatibleFaultResp`
        """
        self._fault = fault

    @property
    def configuration(self):
        """Gets the configuration of this ShowInstanceResponse.

        :return: The configuration of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.CompatibleConfigurationResp`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ShowInstanceResponse.

        :param configuration: The configuration of this ShowInstanceResponse.
        :type configuration: :class:`huaweicloudsdkdws.v2.CompatibleConfigurationResp`
        """
        self._configuration = configuration

    @property
    def locality(self):
        """Gets the locality of this ShowInstanceResponse.

        地点

        :return: The locality of this ShowInstanceResponse.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this ShowInstanceResponse.

        地点

        :param locality: The locality of this ShowInstanceResponse.
        :type locality: str
        """
        self._locality = locality

    @property
    def replicas(self):
        """Gets the replicas of this ShowInstanceResponse.

        备份

        :return: The replicas of this ShowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ShowInstanceResponse.

        备份

        :param replicas: The replicas of this ShowInstanceResponse.
        :type replicas: list[:class:`huaweicloudsdkdws.v2.CompatibleReplicasResp`]
        """
        self._replicas = replicas

    @property
    def db_user(self):
        """Gets the db_user of this ShowInstanceResponse.

        数据库用户

        :return: The db_user of this ShowInstanceResponse.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this ShowInstanceResponse.

        数据库用户

        :param db_user: The db_user of this ShowInstanceResponse.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def storage_engine(self):
        """Gets the storage_engine of this ShowInstanceResponse.

        存储引擎

        :return: The storage_engine of this ShowInstanceResponse.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        """Sets the storage_engine of this ShowInstanceResponse.

        存储引擎

        :param storage_engine: The storage_engine of this ShowInstanceResponse.
        :type storage_engine: str
        """
        self._storage_engine = storage_engine

    @property
    def pay_model(self):
        """Gets the pay_model of this ShowInstanceResponse.

        付款方式

        :return: The pay_model of this ShowInstanceResponse.
        :rtype: int
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        """Sets the pay_model of this ShowInstanceResponse.

        付款方式

        :param pay_model: The pay_model of this ShowInstanceResponse.
        :type pay_model: int
        """
        self._pay_model = pay_model

    @property
    def public_ip(self):
        """Gets the public_ip of this ShowInstanceResponse.

        公网IP

        :return: The public_ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ShowInstanceResponse.

        公网IP

        :param public_ip: The public_ip of this ShowInstanceResponse.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def traffic_ip(self):
        """Gets the traffic_ip of this ShowInstanceResponse.

        流量IP

        :return: The traffic_ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        """Sets the traffic_ip of this ShowInstanceResponse.

        流量IP

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
