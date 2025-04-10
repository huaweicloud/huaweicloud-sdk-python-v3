# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceRequest:

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
        'datastore': 'Datastore',
        'ha': 'Ha',
        'configuration_id': 'str',
        'port': 'str',
        'password': 'str',
        'backup_strategy': 'BackupStrategy',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'Volume',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'data_vip': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfo',
        'time_zone': 'str',
        'dsspool_id': 'str',
        'replica_of_id': 'str',
        'restore_point': 'RestorePoint',
        'collation': 'str',
        'tags': 'list[TagWithKeyValue]',
        'unchangeable_param': 'UnchangeableParam',
        'dry_run': 'bool',
        'count': 'int',
        'serverless_info': 'ServerlessInfo',
        'is_auto_upgrade': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'datastore': 'datastore',
        'ha': 'ha',
        'configuration_id': 'configuration_id',
        'port': 'port',
        'password': 'password',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'disk_encryption_id': 'disk_encryption_id',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'data_vip': 'data_vip',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'dsspool_id': 'dsspool_id',
        'replica_of_id': 'replica_of_id',
        'restore_point': 'restore_point',
        'collation': 'collation',
        'tags': 'tags',
        'unchangeable_param': 'unchangeable_param',
        'dry_run': 'dry_run',
        'count': 'count',
        'serverless_info': 'serverless_info',
        'is_auto_upgrade': 'is_auto_upgrade'
    }

    def __init__(self, name=None, datastore=None, ha=None, configuration_id=None, port=None, password=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, data_vip=None, security_group_id=None, charge_info=None, time_zone=None, dsspool_id=None, replica_of_id=None, restore_point=None, collation=None, tags=None, unchangeable_param=None, dry_run=None, count=None, serverless_info=None, is_auto_upgrade=None):
        r"""InstanceRequest

        The model defined in huaweicloud sdk

        :param name: 实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围如下： - MySQL数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中文字符、中划线或者下划线，不能包含其他的特殊字符。 - PostgreSQL和SQL Server数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.Datastore`
        :param ha: 
        :type ha: :class:`huaweicloudsdkrds.v3.Ha`
        :param configuration_id: 参数模板ID。可调用[获取参数模板列表](https://support.huaweicloud.com/api-rds/rds_09_0301.html)接口返回的ID获取。
        :type configuration_id: str
        :param port: 数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。
        :type port: str
        :param password: 数据库密码。创建只读实例时不可选，其它场景必选。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_&#x3D;+?组成，长度8~32个字符。  其中允许的特殊字符如下： - MySQL数据库允许输入~!@#$%^*-_&#x3D;+?,特殊字符。 - SQL Server数据库允许输入~!@#$%^*-_+?,特殊字符。 - PostgreSQL数据库允许输入~!@#%^*-_&#x3D;+?,特殊字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        :param enterprise_project_id: 企业项目ID。 使用请参考《企业管理 API参考》的[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)响应消息表“enterprise_project字段数据结构说明”的“id”。
        :type enterprise_project_id: str
        :param disk_encryption_id: 用于磁盘加密的密钥ID，默认为空。
        :type disk_encryption_id: str
        :param flavor_ref: 规格码,取值范围：非空。 使用[查询数据库规格](https://support.huaweicloud.com/api-rds/rds_06_0002.html)接口响应消息中的 flavors字段中“spec_code”获取且对应az_status为“在售”状态。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkrds.v3.Volume`
        :param region: 区域ID。创建主实例时必选，其它场景不可选。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api&#x3D;ListFlavors)响应体的az_desc字段。
        :type region: str
        :param availability_zone: 可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api&#x3D;ListFlavors)响应体的az_desc字段。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。
        :type subnet_id: str
        :param data_vip: 指定实例的内网IP,目前仅支持设置IPv4地址。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询私有IP列表](https://support.huaweicloud.com/api-vpc/vpc_privateip_0003.html),选择“device_owner”为空的私有IP。
        :type data_vip: str
        :param security_group_id: 安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。
        :type security_group_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        :param time_zone: 时区。  - 不选择时，各个引擎时区如下：   - MySQL国内站、国际站默认为UTC时间。   - PostgreSQL国内站、国际站默认为UTC时间。   - Microsoft SQL Server国内站默认为China Standard Time，国际站默认为UTC时间。 - MySQL和PostgreSQL引擎选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。 - Microsoft SQL Server引擎选择填写时，请参见“创建数据库实例”接口[表10](https://support.huaweicloud.com/api-rds/rds_01_0002.html#rds_01_0002__table613473883617) 时区与UTC偏移量对照表，填写时区列字符串，如：China Standard Time。
        :type time_zone: str
        :param dsspool_id: Dec用户专属存储ID，每个az配置的专属存储不同，Dec用户创建实例时，对于数据库实例类型不是单机或只读的实例，需要分别为实例所有节点指定dsspoolId，并用逗号隔开。 获取方法如下： - 方法1：登录专属分布式存储服务DSS的控制台界面，查看专属存储列表，选择符合条件的az下的专属dss的ID。 - 方法2：通过专属分布式存储服务DSS的API接口查询，具体操作可参考[获取专属存储详情列表](https://support.huaweicloud.com/api-dss/dss_02_1002.html)。
        :type dsspool_id: str
        :param replica_of_id: 只读实例的主实例ID。创建只读实例时必选，其它场景不可选。
        :type replica_of_id: str
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkrds.v3.RestorePoint`
        :param collation: 仅限Microsoft SQL Server实例创建使用。对于MySQL和PostgreSQL实例，该参数无意义。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。 取值范围：根据[查询SQL Server可用字符集](https://support.huaweicloud.com/api-rds/rds_05_0010.html)查询可设置的字符集。
        :type collation: str
        :param tags: 标签列表。单个实例总标签数上限20个。
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        :param unchangeable_param: 
        :type unchangeable_param: :class:`huaweicloudsdkrds.v3.UnchangeableParam`
        :param dry_run: 是否只预检此次请求，仅支持MySQL。 - true：发送参数检查请求，不会创建实例。   - 检查通过：返回202状态码。   - 检查不通过：返回对应错误码，详情请参考错误码。 - false：发送正常请求，通过检查后，并且执行创建实例的请求。
        :type dry_run: bool
        :param count: 批量创建实例的数量，取值范围为1~50。
        :type count: int
        :param serverless_info: 
        :type serverless_info: :class:`huaweicloudsdkrds.v3.ServerlessInfo`
        :param is_auto_upgrade: 是否开启自动小版本升级，默认为false，仅支持PostgreSQL。 - true：开启自动小版本升级。 - false：不开启自动小版本升级。
        :type is_auto_upgrade: bool
        """
        
        

        self._name = None
        self._datastore = None
        self._ha = None
        self._configuration_id = None
        self._port = None
        self._password = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._disk_encryption_id = None
        self._flavor_ref = None
        self._volume = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._data_vip = None
        self._security_group_id = None
        self._charge_info = None
        self._time_zone = None
        self._dsspool_id = None
        self._replica_of_id = None
        self._restore_point = None
        self._collation = None
        self._tags = None
        self._unchangeable_param = None
        self._dry_run = None
        self._count = None
        self._serverless_info = None
        self._is_auto_upgrade = None
        self.discriminator = None

        self.name = name
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
        if password is not None:
            self.password = password
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        self.flavor_ref = flavor_ref
        self.volume = volume
        self.region = region
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if data_vip is not None:
            self.data_vip = data_vip
        self.security_group_id = security_group_id
        if charge_info is not None:
            self.charge_info = charge_info
        if time_zone is not None:
            self.time_zone = time_zone
        if dsspool_id is not None:
            self.dsspool_id = dsspool_id
        if replica_of_id is not None:
            self.replica_of_id = replica_of_id
        if restore_point is not None:
            self.restore_point = restore_point
        if collation is not None:
            self.collation = collation
        if tags is not None:
            self.tags = tags
        if unchangeable_param is not None:
            self.unchangeable_param = unchangeable_param
        if dry_run is not None:
            self.dry_run = dry_run
        if count is not None:
            self.count = count
        if serverless_info is not None:
            self.serverless_info = serverless_info
        if is_auto_upgrade is not None:
            self.is_auto_upgrade = is_auto_upgrade

    @property
    def name(self):
        r"""Gets the name of this InstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围如下： - MySQL数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中文字符、中划线或者下划线，不能包含其他的特殊字符。 - PostgreSQL和SQL Server数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this InstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围如下： - MySQL数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中文字符、中划线或者下划线，不能包含其他的特殊字符。 - PostgreSQL和SQL Server数据库支持的字符长度是4~64个字符，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this InstanceRequest.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        r"""Gets the datastore of this InstanceRequest.

        :return: The datastore of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this InstanceRequest.

        :param datastore: The datastore of this InstanceRequest.
        :type datastore: :class:`huaweicloudsdkrds.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def ha(self):
        r"""Gets the ha of this InstanceRequest.

        :return: The ha of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.Ha`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        r"""Sets the ha of this InstanceRequest.

        :param ha: The ha of this InstanceRequest.
        :type ha: :class:`huaweicloudsdkrds.v3.Ha`
        """
        self._ha = ha

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this InstanceRequest.

        参数模板ID。可调用[获取参数模板列表](https://support.huaweicloud.com/api-rds/rds_09_0301.html)接口返回的ID获取。

        :return: The configuration_id of this InstanceRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this InstanceRequest.

        参数模板ID。可调用[获取参数模板列表](https://support.huaweicloud.com/api-rds/rds_09_0301.html)接口返回的ID获取。

        :param configuration_id: The configuration_id of this InstanceRequest.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        r"""Gets the port of this InstanceRequest.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :return: The port of this InstanceRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this InstanceRequest.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :param port: The port of this InstanceRequest.
        :type port: str
        """
        self._port = port

    @property
    def password(self):
        r"""Gets the password of this InstanceRequest.

        数据库密码。创建只读实例时不可选，其它场景必选。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  其中允许的特殊字符如下： - MySQL数据库允许输入~!@#$%^*-_=+?,特殊字符。 - SQL Server数据库允许输入~!@#$%^*-_+?,特殊字符。 - PostgreSQL数据库允许输入~!@#%^*-_=+?,特殊字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this InstanceRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this InstanceRequest.

        数据库密码。创建只读实例时不可选，其它场景必选。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  其中允许的特殊字符如下： - MySQL数据库允许输入~!@#$%^*-_=+?,特殊字符。 - SQL Server数据库允许输入~!@#$%^*-_+?,特殊字符。 - PostgreSQL数据库允许输入~!@#%^*-_=+?,特殊字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this InstanceRequest.
        :type password: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this InstanceRequest.

        :return: The backup_strategy of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this InstanceRequest.

        :param backup_strategy: The backup_strategy of this InstanceRequest.
        :type backup_strategy: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstanceRequest.

        企业项目ID。 使用请参考《企业管理 API参考》的[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this InstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstanceRequest.

        企业项目ID。 使用请参考《企业管理 API参考》的[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this InstanceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        r"""Gets the disk_encryption_id of this InstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :return: The disk_encryption_id of this InstanceRequest.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        r"""Sets the disk_encryption_id of this InstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :param disk_encryption_id: The disk_encryption_id of this InstanceRequest.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this InstanceRequest.

        规格码,取值范围：非空。 使用[查询数据库规格](https://support.huaweicloud.com/api-rds/rds_06_0002.html)接口响应消息中的 flavors字段中“spec_code”获取且对应az_status为“在售”状态。

        :return: The flavor_ref of this InstanceRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this InstanceRequest.

        规格码,取值范围：非空。 使用[查询数据库规格](https://support.huaweicloud.com/api-rds/rds_06_0002.html)接口响应消息中的 flavors字段中“spec_code”获取且对应az_status为“在售”状态。

        :param flavor_ref: The flavor_ref of this InstanceRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        r"""Gets the volume of this InstanceRequest.

        :return: The volume of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this InstanceRequest.

        :param volume: The volume of this InstanceRequest.
        :type volume: :class:`huaweicloudsdkrds.v3.Volume`
        """
        self._volume = volume

    @property
    def region(self):
        r"""Gets the region of this InstanceRequest.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api=ListFlavors)响应体的az_desc字段。

        :return: The region of this InstanceRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstanceRequest.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api=ListFlavors)响应体的az_desc字段。

        :param region: The region of this InstanceRequest.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this InstanceRequest.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api=ListFlavors)响应体的az_desc字段。

        :return: The availability_zone of this InstanceRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this InstanceRequest.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见OpenAPI查询数据库规格(https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc?api=ListFlavors)响应体的az_desc字段。

        :param availability_zone: The availability_zone of this InstanceRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this InstanceRequest.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :return: The vpc_id of this InstanceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this InstanceRequest.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :param vpc_id: The vpc_id of this InstanceRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this InstanceRequest.

        子网的网络ID信息。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :return: The subnet_id of this InstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this InstanceRequest.

        子网的网络ID信息。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :param subnet_id: The subnet_id of this InstanceRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def data_vip(self):
        r"""Gets the data_vip of this InstanceRequest.

        指定实例的内网IP,目前仅支持设置IPv4地址。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询私有IP列表](https://support.huaweicloud.com/api-vpc/vpc_privateip_0003.html),选择“device_owner”为空的私有IP。

        :return: The data_vip of this InstanceRequest.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this InstanceRequest.

        指定实例的内网IP,目前仅支持设置IPv4地址。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询私有IP列表](https://support.huaweicloud.com/api-vpc/vpc_privateip_0003.html),选择“device_owner”为空的私有IP。

        :param data_vip: The data_vip of this InstanceRequest.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this InstanceRequest.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :return: The security_group_id of this InstanceRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this InstanceRequest.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。 获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :param security_group_id: The security_group_id of this InstanceRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        r"""Gets the charge_info of this InstanceRequest.

        :return: The charge_info of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this InstanceRequest.

        :param charge_info: The charge_info of this InstanceRequest.
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        r"""Gets the time_zone of this InstanceRequest.

        时区。  - 不选择时，各个引擎时区如下：   - MySQL国内站、国际站默认为UTC时间。   - PostgreSQL国内站、国际站默认为UTC时间。   - Microsoft SQL Server国内站默认为China Standard Time，国际站默认为UTC时间。 - MySQL和PostgreSQL引擎选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。 - Microsoft SQL Server引擎选择填写时，请参见“创建数据库实例”接口[表10](https://support.huaweicloud.com/api-rds/rds_01_0002.html#rds_01_0002__table613473883617) 时区与UTC偏移量对照表，填写时区列字符串，如：China Standard Time。

        :return: The time_zone of this InstanceRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this InstanceRequest.

        时区。  - 不选择时，各个引擎时区如下：   - MySQL国内站、国际站默认为UTC时间。   - PostgreSQL国内站、国际站默认为UTC时间。   - Microsoft SQL Server国内站默认为China Standard Time，国际站默认为UTC时间。 - MySQL和PostgreSQL引擎选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。 - Microsoft SQL Server引擎选择填写时，请参见“创建数据库实例”接口[表10](https://support.huaweicloud.com/api-rds/rds_01_0002.html#rds_01_0002__table613473883617) 时区与UTC偏移量对照表，填写时区列字符串，如：China Standard Time。

        :param time_zone: The time_zone of this InstanceRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def dsspool_id(self):
        r"""Gets the dsspool_id of this InstanceRequest.

        Dec用户专属存储ID，每个az配置的专属存储不同，Dec用户创建实例时，对于数据库实例类型不是单机或只读的实例，需要分别为实例所有节点指定dsspoolId，并用逗号隔开。 获取方法如下： - 方法1：登录专属分布式存储服务DSS的控制台界面，查看专属存储列表，选择符合条件的az下的专属dss的ID。 - 方法2：通过专属分布式存储服务DSS的API接口查询，具体操作可参考[获取专属存储详情列表](https://support.huaweicloud.com/api-dss/dss_02_1002.html)。

        :return: The dsspool_id of this InstanceRequest.
        :rtype: str
        """
        return self._dsspool_id

    @dsspool_id.setter
    def dsspool_id(self, dsspool_id):
        r"""Sets the dsspool_id of this InstanceRequest.

        Dec用户专属存储ID，每个az配置的专属存储不同，Dec用户创建实例时，对于数据库实例类型不是单机或只读的实例，需要分别为实例所有节点指定dsspoolId，并用逗号隔开。 获取方法如下： - 方法1：登录专属分布式存储服务DSS的控制台界面，查看专属存储列表，选择符合条件的az下的专属dss的ID。 - 方法2：通过专属分布式存储服务DSS的API接口查询，具体操作可参考[获取专属存储详情列表](https://support.huaweicloud.com/api-dss/dss_02_1002.html)。

        :param dsspool_id: The dsspool_id of this InstanceRequest.
        :type dsspool_id: str
        """
        self._dsspool_id = dsspool_id

    @property
    def replica_of_id(self):
        r"""Gets the replica_of_id of this InstanceRequest.

        只读实例的主实例ID。创建只读实例时必选，其它场景不可选。

        :return: The replica_of_id of this InstanceRequest.
        :rtype: str
        """
        return self._replica_of_id

    @replica_of_id.setter
    def replica_of_id(self, replica_of_id):
        r"""Sets the replica_of_id of this InstanceRequest.

        只读实例的主实例ID。创建只读实例时必选，其它场景不可选。

        :param replica_of_id: The replica_of_id of this InstanceRequest.
        :type replica_of_id: str
        """
        self._replica_of_id = replica_of_id

    @property
    def restore_point(self):
        r"""Gets the restore_point of this InstanceRequest.

        :return: The restore_point of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        r"""Sets the restore_point of this InstanceRequest.

        :param restore_point: The restore_point of this InstanceRequest.
        :type restore_point: :class:`huaweicloudsdkrds.v3.RestorePoint`
        """
        self._restore_point = restore_point

    @property
    def collation(self):
        r"""Gets the collation of this InstanceRequest.

        仅限Microsoft SQL Server实例创建使用。对于MySQL和PostgreSQL实例，该参数无意义。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。 取值范围：根据[查询SQL Server可用字符集](https://support.huaweicloud.com/api-rds/rds_05_0010.html)查询可设置的字符集。

        :return: The collation of this InstanceRequest.
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        r"""Sets the collation of this InstanceRequest.

        仅限Microsoft SQL Server实例创建使用。对于MySQL和PostgreSQL实例，该参数无意义。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。 取值范围：根据[查询SQL Server可用字符集](https://support.huaweicloud.com/api-rds/rds_05_0010.html)查询可设置的字符集。

        :param collation: The collation of this InstanceRequest.
        :type collation: str
        """
        self._collation = collation

    @property
    def tags(self):
        r"""Gets the tags of this InstanceRequest.

        标签列表。单个实例总标签数上限20个。

        :return: The tags of this InstanceRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this InstanceRequest.

        标签列表。单个实例总标签数上限20个。

        :param tags: The tags of this InstanceRequest.
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        """
        self._tags = tags

    @property
    def unchangeable_param(self):
        r"""Gets the unchangeable_param of this InstanceRequest.

        :return: The unchangeable_param of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.UnchangeableParam`
        """
        return self._unchangeable_param

    @unchangeable_param.setter
    def unchangeable_param(self, unchangeable_param):
        r"""Sets the unchangeable_param of this InstanceRequest.

        :param unchangeable_param: The unchangeable_param of this InstanceRequest.
        :type unchangeable_param: :class:`huaweicloudsdkrds.v3.UnchangeableParam`
        """
        self._unchangeable_param = unchangeable_param

    @property
    def dry_run(self):
        r"""Gets the dry_run of this InstanceRequest.

        是否只预检此次请求，仅支持MySQL。 - true：发送参数检查请求，不会创建实例。   - 检查通过：返回202状态码。   - 检查不通过：返回对应错误码，详情请参考错误码。 - false：发送正常请求，通过检查后，并且执行创建实例的请求。

        :return: The dry_run of this InstanceRequest.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this InstanceRequest.

        是否只预检此次请求，仅支持MySQL。 - true：发送参数检查请求，不会创建实例。   - 检查通过：返回202状态码。   - 检查不通过：返回对应错误码，详情请参考错误码。 - false：发送正常请求，通过检查后，并且执行创建实例的请求。

        :param dry_run: The dry_run of this InstanceRequest.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def count(self):
        r"""Gets the count of this InstanceRequest.

        批量创建实例的数量，取值范围为1~50。

        :return: The count of this InstanceRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this InstanceRequest.

        批量创建实例的数量，取值范围为1~50。

        :param count: The count of this InstanceRequest.
        :type count: int
        """
        self._count = count

    @property
    def serverless_info(self):
        r"""Gets the serverless_info of this InstanceRequest.

        :return: The serverless_info of this InstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.ServerlessInfo`
        """
        return self._serverless_info

    @serverless_info.setter
    def serverless_info(self, serverless_info):
        r"""Sets the serverless_info of this InstanceRequest.

        :param serverless_info: The serverless_info of this InstanceRequest.
        :type serverless_info: :class:`huaweicloudsdkrds.v3.ServerlessInfo`
        """
        self._serverless_info = serverless_info

    @property
    def is_auto_upgrade(self):
        r"""Gets the is_auto_upgrade of this InstanceRequest.

        是否开启自动小版本升级，默认为false，仅支持PostgreSQL。 - true：开启自动小版本升级。 - false：不开启自动小版本升级。

        :return: The is_auto_upgrade of this InstanceRequest.
        :rtype: bool
        """
        return self._is_auto_upgrade

    @is_auto_upgrade.setter
    def is_auto_upgrade(self, is_auto_upgrade):
        r"""Sets the is_auto_upgrade of this InstanceRequest.

        是否开启自动小版本升级，默认为false，仅支持PostgreSQL。 - true：开启自动小版本升级。 - false：不开启自动小版本升级。

        :param is_auto_upgrade: The is_auto_upgrade of this InstanceRequest.
        :type is_auto_upgrade: bool
        """
        self._is_auto_upgrade = is_auto_upgrade

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
        if not isinstance(other, InstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
