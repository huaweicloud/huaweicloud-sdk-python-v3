# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceResult:

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
        'status': 'str',
        'private_ips': 'list[str]',
        'public_ips': 'list[str]',
        'port': 'int',
        'type': 'str',
        'ha': 'ListHaResult',
        'replica_num': 'int',
        'region': 'str',
        'datastore': 'ListDatastore',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'flavor_ref': 'str',
        'flavor_info': 'ListFlavorInfo',
        'volume': 'ListVolume',
        'switch_strategy': 'str',
        'backup_strategy': 'OpenGaussBackupStrategyForListResponse',
        'maintenance_window': 'str',
        'nodes': 'list[NodeResult]',
        'enterprise_project_id': 'str',
        'instance_mode': 'str',
        'disk_encryption_id': 'str',
        'charge_info': 'OpenGaussChargeInfoListResponse',
        'time_zone': 'str',
        'tags': 'list[TagResult]',
        'disk_usage': 'str',
        'backup_used_space': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'private_ips': 'private_ips',
        'public_ips': 'public_ips',
        'port': 'port',
        'type': 'type',
        'ha': 'ha',
        'replica_num': 'replica_num',
        'region': 'region',
        'datastore': 'datastore',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'flavor_ref': 'flavor_ref',
        'flavor_info': 'flavor_info',
        'volume': 'volume',
        'switch_strategy': 'switch_strategy',
        'backup_strategy': 'backup_strategy',
        'maintenance_window': 'maintenance_window',
        'nodes': 'nodes',
        'enterprise_project_id': 'enterprise_project_id',
        'instance_mode': 'instance_mode',
        'disk_encryption_id': 'disk_encryption_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'tags': 'tags',
        'disk_usage': 'disk_usage',
        'backup_used_space': 'backup_used_space'
    }

    def __init__(self, id=None, name=None, status=None, private_ips=None, public_ips=None, port=None, type=None, ha=None, replica_num=None, region=None, datastore=None, created=None, updated=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, flavor_ref=None, flavor_info=None, volume=None, switch_strategy=None, backup_strategy=None, maintenance_window=None, nodes=None, enterprise_project_id=None, instance_mode=None, disk_encryption_id=None, charge_info=None, time_zone=None, tags=None, disk_usage=None, backup_used_space=None):
        r"""ListInstanceResult

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param status: 实例状态。  取值：  值为“BUILD”，表示实例正在创建。  值为“ACTIVE”，表示实例正常。  值为“FAILED”，表示实例异常。  值为“FROZEN”，表示实例冻结。  值为“EXPANDING”，表示实例正在扩容CN或DN。  值为“REBOOTING”，表示实例正在重启。  值为“UPGRADING”，表示实例正在升级。  值为“RESTORING”，表示实例正在恢复。  值为“BACKING UP”，表示实例正在进行备份。  值为“REDUCING REPLICATION”，表示实例正在降副本。  值为“STORAGE FULL”，表示实例磁盘空间满。
        :type status: str
        :param private_ips: 实例内网IP地址列表。分布式CN所在的弹性云服务器创建成功后该值存在，主备版DN所在的弹性云服务器创建成功后该值存在，其他情况下为空字符串。
        :type private_ips: list[str]
        :param public_ips: 实例外网IP地址列表。绑定弹性公网IP后，该值不为空。
        :type public_ips: list[str]
        :param port: 数据库端口号。GaussDB数据库端口设置范围为1024~39998（其中2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,20049,20050,21731,21732被系统占用不可设置）。  当不传该参数时，默认端口如下：8000。
        :type port: int
        :param type: 实例类型，取值为 \&quot;Enterprise\&quot;，对应于分布式实例（企业版）。取值为\&quot;Ha\&quot;，对应于主备版实例。
        :type type: str
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListHaResult`
        :param replica_num: 实例副本数。
        :type replica_num: int
        :param region: 实例所在区域。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatastore`
        :param created: 创建时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。  说明：创建时该值为实例下发创建的时间，创建完成后，该值为创建完成时间。
        :type created: str
        :param updated: 更新时间，格式与“created”字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type updated: str
        :param db_user_name: 默认用户名。
        :type db_user_name: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param flavor_ref: 规格码。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。
        :type flavor_ref: str
        :param flavor_info: 
        :type flavor_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListFlavorInfo`
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListVolume`
        :param switch_strategy: 数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。 若创建时没有选择切换策略，则不予显示。
        :type switch_strategy: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForListResponse`
        :param maintenance_window: 可维护时间窗，为UTC时间。
        :type maintenance_window: str
        :param nodes: 实例节点信息列表。
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeResult`]
        :param enterprise_project_id: 企业项目标签ID。非企业项目账号的实例，企业项目默认0。
        :type enterprise_project_id: str
        :param instance_mode: basic为基础版 ，enterprise为企业版。
        :type instance_mode: str
        :param disk_encryption_id: 磁盘加密密钥ID。只有创建磁盘加密实例才会显示该参数。
        :type disk_encryption_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoListResponse`
        :param time_zone: 时区。
        :type time_zone: str
        :param tags: 标签列表，没有标签不返回该参数。
        :type tags: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TagResult`]
        :param disk_usage: 实例磁盘的可使用率，值范围[0-1]，值保留四位小数。
        :type disk_usage: str
        :param backup_used_space: 备份空间使用量，单位KB。
        :type backup_used_space: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._private_ips = None
        self._public_ips = None
        self._port = None
        self._type = None
        self._ha = None
        self._replica_num = None
        self._region = None
        self._datastore = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._flavor_ref = None
        self._flavor_info = None
        self._volume = None
        self._switch_strategy = None
        self._backup_strategy = None
        self._maintenance_window = None
        self._nodes = None
        self._enterprise_project_id = None
        self._instance_mode = None
        self._disk_encryption_id = None
        self._charge_info = None
        self._time_zone = None
        self._tags = None
        self._disk_usage = None
        self._backup_used_space = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.private_ips = private_ips
        self.public_ips = public_ips
        self.port = port
        self.type = type
        self.ha = ha
        if replica_num is not None:
            self.replica_num = replica_num
        self.region = region
        self.datastore = datastore
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.flavor_ref = flavor_ref
        self.flavor_info = flavor_info
        self.volume = volume
        self.switch_strategy = switch_strategy
        self.backup_strategy = backup_strategy
        self.maintenance_window = maintenance_window
        self.nodes = nodes
        self.enterprise_project_id = enterprise_project_id
        self.instance_mode = instance_mode
        self.disk_encryption_id = disk_encryption_id
        self.charge_info = charge_info
        self.time_zone = time_zone
        self.tags = tags
        if disk_usage is not None:
            self.disk_usage = disk_usage
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space

    @property
    def id(self):
        r"""Gets the id of this ListInstanceResult.

        实例ID。

        :return: The id of this ListInstanceResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInstanceResult.

        实例ID。

        :param id: The id of this ListInstanceResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListInstanceResult.

        创建的实例名称。

        :return: The name of this ListInstanceResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceResult.

        创建的实例名称。

        :param name: The name of this ListInstanceResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListInstanceResult.

        实例状态。  取值：  值为“BUILD”，表示实例正在创建。  值为“ACTIVE”，表示实例正常。  值为“FAILED”，表示实例异常。  值为“FROZEN”，表示实例冻结。  值为“EXPANDING”，表示实例正在扩容CN或DN。  值为“REBOOTING”，表示实例正在重启。  值为“UPGRADING”，表示实例正在升级。  值为“RESTORING”，表示实例正在恢复。  值为“BACKING UP”，表示实例正在进行备份。  值为“REDUCING REPLICATION”，表示实例正在降副本。  值为“STORAGE FULL”，表示实例磁盘空间满。

        :return: The status of this ListInstanceResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInstanceResult.

        实例状态。  取值：  值为“BUILD”，表示实例正在创建。  值为“ACTIVE”，表示实例正常。  值为“FAILED”，表示实例异常。  值为“FROZEN”，表示实例冻结。  值为“EXPANDING”，表示实例正在扩容CN或DN。  值为“REBOOTING”，表示实例正在重启。  值为“UPGRADING”，表示实例正在升级。  值为“RESTORING”，表示实例正在恢复。  值为“BACKING UP”，表示实例正在进行备份。  值为“REDUCING REPLICATION”，表示实例正在降副本。  值为“STORAGE FULL”，表示实例磁盘空间满。

        :param status: The status of this ListInstanceResult.
        :type status: str
        """
        self._status = status

    @property
    def private_ips(self):
        r"""Gets the private_ips of this ListInstanceResult.

        实例内网IP地址列表。分布式CN所在的弹性云服务器创建成功后该值存在，主备版DN所在的弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :return: The private_ips of this ListInstanceResult.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        r"""Sets the private_ips of this ListInstanceResult.

        实例内网IP地址列表。分布式CN所在的弹性云服务器创建成功后该值存在，主备版DN所在的弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :param private_ips: The private_ips of this ListInstanceResult.
        :type private_ips: list[str]
        """
        self._private_ips = private_ips

    @property
    def public_ips(self):
        r"""Gets the public_ips of this ListInstanceResult.

        实例外网IP地址列表。绑定弹性公网IP后，该值不为空。

        :return: The public_ips of this ListInstanceResult.
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        r"""Sets the public_ips of this ListInstanceResult.

        实例外网IP地址列表。绑定弹性公网IP后，该值不为空。

        :param public_ips: The public_ips of this ListInstanceResult.
        :type public_ips: list[str]
        """
        self._public_ips = public_ips

    @property
    def port(self):
        r"""Gets the port of this ListInstanceResult.

        数据库端口号。GaussDB数据库端口设置范围为1024~39998（其中2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,20049,20050,21731,21732被系统占用不可设置）。  当不传该参数时，默认端口如下：8000。

        :return: The port of this ListInstanceResult.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListInstanceResult.

        数据库端口号。GaussDB数据库端口设置范围为1024~39998（其中2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,20049,20050,21731,21732被系统占用不可设置）。  当不传该参数时，默认端口如下：8000。

        :param port: The port of this ListInstanceResult.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this ListInstanceResult.

        实例类型，取值为 \"Enterprise\"，对应于分布式实例（企业版）。取值为\"Ha\"，对应于主备版实例。

        :return: The type of this ListInstanceResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInstanceResult.

        实例类型，取值为 \"Enterprise\"，对应于分布式实例（企业版）。取值为\"Ha\"，对应于主备版实例。

        :param type: The type of this ListInstanceResult.
        :type type: str
        """
        self._type = type

    @property
    def ha(self):
        r"""Gets the ha of this ListInstanceResult.

        :return: The ha of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListHaResult`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        r"""Sets the ha of this ListInstanceResult.

        :param ha: The ha of this ListInstanceResult.
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListHaResult`
        """
        self._ha = ha

    @property
    def replica_num(self):
        r"""Gets the replica_num of this ListInstanceResult.

        实例副本数。

        :return: The replica_num of this ListInstanceResult.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        r"""Sets the replica_num of this ListInstanceResult.

        实例副本数。

        :param replica_num: The replica_num of this ListInstanceResult.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def region(self):
        r"""Gets the region of this ListInstanceResult.

        实例所在区域。

        :return: The region of this ListInstanceResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListInstanceResult.

        实例所在区域。

        :param region: The region of this ListInstanceResult.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        r"""Gets the datastore of this ListInstanceResult.

        :return: The datastore of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ListInstanceResult.

        :param datastore: The datastore of this ListInstanceResult.
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatastore`
        """
        self._datastore = datastore

    @property
    def created(self):
        r"""Gets the created of this ListInstanceResult.

        创建时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。  说明：创建时该值为实例下发创建的时间，创建完成后，该值为创建完成时间。

        :return: The created of this ListInstanceResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ListInstanceResult.

        创建时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。  说明：创建时该值为实例下发创建的时间，创建完成后，该值为创建完成时间。

        :param created: The created of this ListInstanceResult.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ListInstanceResult.

        更新时间，格式与“created”字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this ListInstanceResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ListInstanceResult.

        更新时间，格式与“created”字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this ListInstanceResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        r"""Gets the db_user_name of this ListInstanceResult.

        默认用户名。

        :return: The db_user_name of this ListInstanceResult.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        r"""Sets the db_user_name of this ListInstanceResult.

        默认用户名。

        :param db_user_name: The db_user_name of this ListInstanceResult.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInstanceResult.

        虚拟私有云ID。

        :return: The vpc_id of this ListInstanceResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInstanceResult.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListInstanceResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListInstanceResult.

        子网的网络ID信息。

        :return: The subnet_id of this ListInstanceResult.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListInstanceResult.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this ListInstanceResult.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ListInstanceResult.

        安全组ID。

        :return: The security_group_id of this ListInstanceResult.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ListInstanceResult.

        安全组ID。

        :param security_group_id: The security_group_id of this ListInstanceResult.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this ListInstanceResult.

        规格码。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :return: The flavor_ref of this ListInstanceResult.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this ListInstanceResult.

        规格码。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this ListInstanceResult.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def flavor_info(self):
        r"""Gets the flavor_info of this ListInstanceResult.

        :return: The flavor_info of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListFlavorInfo`
        """
        return self._flavor_info

    @flavor_info.setter
    def flavor_info(self, flavor_info):
        r"""Sets the flavor_info of this ListInstanceResult.

        :param flavor_info: The flavor_info of this ListInstanceResult.
        :type flavor_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListFlavorInfo`
        """
        self._flavor_info = flavor_info

    @property
    def volume(self):
        r"""Gets the volume of this ListInstanceResult.

        :return: The volume of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this ListInstanceResult.

        :param volume: The volume of this ListInstanceResult.
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListVolume`
        """
        self._volume = volume

    @property
    def switch_strategy(self):
        r"""Gets the switch_strategy of this ListInstanceResult.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。 若创建时没有选择切换策略，则不予显示。

        :return: The switch_strategy of this ListInstanceResult.
        :rtype: str
        """
        return self._switch_strategy

    @switch_strategy.setter
    def switch_strategy(self, switch_strategy):
        r"""Sets the switch_strategy of this ListInstanceResult.

        数据库切换策略。取值为“reliability”或“availability”，分别对应于可靠性优先和可用性优先。 若创建时没有选择切换策略，则不予显示。

        :param switch_strategy: The switch_strategy of this ListInstanceResult.
        :type switch_strategy: str
        """
        self._switch_strategy = switch_strategy

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this ListInstanceResult.

        :return: The backup_strategy of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForListResponse`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this ListInstanceResult.

        :param backup_strategy: The backup_strategy of this ListInstanceResult.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategyForListResponse`
        """
        self._backup_strategy = backup_strategy

    @property
    def maintenance_window(self):
        r"""Gets the maintenance_window of this ListInstanceResult.

        可维护时间窗，为UTC时间。

        :return: The maintenance_window of this ListInstanceResult.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        r"""Sets the maintenance_window of this ListInstanceResult.

        可维护时间窗，为UTC时间。

        :param maintenance_window: The maintenance_window of this ListInstanceResult.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def nodes(self):
        r"""Gets the nodes of this ListInstanceResult.

        实例节点信息列表。

        :return: The nodes of this ListInstanceResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeResult`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ListInstanceResult.

        实例节点信息列表。

        :param nodes: The nodes of this ListInstanceResult.
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeResult`]
        """
        self._nodes = nodes

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstanceResult.

        企业项目标签ID。非企业项目账号的实例，企业项目默认0。

        :return: The enterprise_project_id of this ListInstanceResult.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstanceResult.

        企业项目标签ID。非企业项目账号的实例，企业项目默认0。

        :param enterprise_project_id: The enterprise_project_id of this ListInstanceResult.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this ListInstanceResult.

        basic为基础版 ，enterprise为企业版。

        :return: The instance_mode of this ListInstanceResult.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this ListInstanceResult.

        basic为基础版 ，enterprise为企业版。

        :param instance_mode: The instance_mode of this ListInstanceResult.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def disk_encryption_id(self):
        r"""Gets the disk_encryption_id of this ListInstanceResult.

        磁盘加密密钥ID。只有创建磁盘加密实例才会显示该参数。

        :return: The disk_encryption_id of this ListInstanceResult.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        r"""Sets the disk_encryption_id of this ListInstanceResult.

        磁盘加密密钥ID。只有创建磁盘加密实例才会显示该参数。

        :param disk_encryption_id: The disk_encryption_id of this ListInstanceResult.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def charge_info(self):
        r"""Gets the charge_info of this ListInstanceResult.

        :return: The charge_info of this ListInstanceResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoListResponse`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this ListInstanceResult.

        :param charge_info: The charge_info of this ListInstanceResult.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfoListResponse`
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ListInstanceResult.

        时区。

        :return: The time_zone of this ListInstanceResult.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ListInstanceResult.

        时区。

        :param time_zone: The time_zone of this ListInstanceResult.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def tags(self):
        r"""Gets the tags of this ListInstanceResult.

        标签列表，没有标签不返回该参数。

        :return: The tags of this ListInstanceResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TagResult`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstanceResult.

        标签列表，没有标签不返回该参数。

        :param tags: The tags of this ListInstanceResult.
        :type tags: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TagResult`]
        """
        self._tags = tags

    @property
    def disk_usage(self):
        r"""Gets the disk_usage of this ListInstanceResult.

        实例磁盘的可使用率，值范围[0-1]，值保留四位小数。

        :return: The disk_usage of this ListInstanceResult.
        :rtype: str
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        r"""Sets the disk_usage of this ListInstanceResult.

        实例磁盘的可使用率，值范围[0-1]，值保留四位小数。

        :param disk_usage: The disk_usage of this ListInstanceResult.
        :type disk_usage: str
        """
        self._disk_usage = disk_usage

    @property
    def backup_used_space(self):
        r"""Gets the backup_used_space of this ListInstanceResult.

        备份空间使用量，单位KB。

        :return: The backup_used_space of this ListInstanceResult.
        :rtype: str
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        r"""Sets the backup_used_space of this ListInstanceResult.

        备份空间使用量，单位KB。

        :param backup_used_space: The backup_used_space of this ListInstanceResult.
        :type backup_used_space: str
        """
        self._backup_used_space = backup_used_space

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
        if not isinstance(other, ListInstanceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
