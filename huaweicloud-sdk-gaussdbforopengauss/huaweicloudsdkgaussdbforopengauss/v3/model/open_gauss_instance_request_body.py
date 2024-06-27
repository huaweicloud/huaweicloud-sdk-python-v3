# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussInstanceRequestBody:

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
        'datastore': 'OpenGaussDatastoreOption',
        'ha': 'OpenGaussHaOption',
        'configuration_id': 'str',
        'port': 'str',
        'password': 'str',
        'backup_strategy': 'OpenGaussBackupStrategy',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'OpenGaussVolume',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'OpenGaussChargeInfo',
        'time_zone': 'str',
        'sharding_num': 'int',
        'coordinator_num': 'int',
        'replica_num': 'int',
        'enable_force_switch': 'bool',
        'enable_single_float_ip': 'bool'
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
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'sharding_num': 'sharding_num',
        'coordinator_num': 'coordinator_num',
        'replica_num': 'replica_num',
        'enable_force_switch': 'enable_force_switch',
        'enable_single_float_ip': 'enable_single_float_ip'
    }

    def __init__(self, name=None, datastore=None, ha=None, configuration_id=None, port=None, password=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, time_zone=None, sharding_num=None, coordinator_num=None, replica_num=None, enable_force_switch=None, enable_single_float_ip=None):
        """OpenGaussInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreOption`
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaOption`
        :param configuration_id: 参数模板ID。当不传该参数时，使用系统默认的参数模板。
        :type configuration_id: str
        :param port: 数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。
        :type port: str
        :param password: 数据库密码。必选。  取值范围：  &#39;非空； 至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为~!@#%^*-_&#x3D;+?,）四类字符中的三类字符；长度8~32个字符。&#39;  &#39;建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。&#39;
        :type password: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        :param enterprise_project_id: 企业项目ID。只有企业租户时该参数才生效。  使用请参考《企业管理 API参考》的“[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)”响应消息表“enterprise_project字段数据结构说明”的“id”。
        :type enterprise_project_id: str
        :param disk_encryption_id: 用于磁盘加密的密钥ID，默认为空。
        :type disk_encryption_id: str
        :param flavor_ref: 规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        :param region: 区域ID。  取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type region: str
        :param availability_zone: 可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\&quot;cn-north-4a,cn-north-4a,cn-north-4a\&quot;。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。
        :type security_group_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        :param time_zone: UTC时区。  - 不选择时，GaussDB国内站、默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。
        :type time_zone: str
        :param sharding_num: 仅分布式形态需要填写该参数。分片数量，取值范围1~9。
        :type sharding_num: int
        :param coordinator_num: 仅分布式形态需要填写该参数。协调节点数量，取值范围1~9。CN数量必须小于或等于两倍的分片数。
        :type coordinator_num: int
        :param replica_num: 实例副本数，支持取值3。不填默认为3。仅支持1.3.0及以上版本的实例。
        :type replica_num: int
        :param enable_force_switch: enable_force_switch表示是否开启备机强升主功能，enable_force_switch&#x3D;true表示开启备机强升主功能，enable_force_switch&#x3D;false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。
        :type enable_force_switch: bool
        :param enable_single_float_ip: 单浮动IP策略，仅主备版支持。默认值是false，表示不开启单浮动IP策略。 取值范围： true：开启单浮动IP策略，实例将只有一个浮动IP绑定主节点，如果发生主备倒换，浮动IP不会发生变化。 false：不开启单浮动IP策略，每个节点都会绑定一个浮动IP，如果发生主备倒换，浮动IP会发生变化。 说明： 仅支持3.206及以上版本的主备版实例。
        :type enable_single_float_ip: bool
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
        self._security_group_id = None
        self._charge_info = None
        self._time_zone = None
        self._sharding_num = None
        self._coordinator_num = None
        self._replica_num = None
        self._enable_force_switch = None
        self._enable_single_float_ip = None
        self.discriminator = None

        self.name = name
        self.datastore = datastore
        self.ha = ha
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
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
        self.security_group_id = security_group_id
        if charge_info is not None:
            self.charge_info = charge_info
        if time_zone is not None:
            self.time_zone = time_zone
        if sharding_num is not None:
            self.sharding_num = sharding_num
        if coordinator_num is not None:
            self.coordinator_num = coordinator_num
        if replica_num is not None:
            self.replica_num = replica_num
        if enable_force_switch is not None:
            self.enable_force_switch = enable_force_switch
        if enable_single_float_ip is not None:
            self.enable_single_float_ip = enable_single_float_ip

    @property
    def name(self):
        """Gets the name of this OpenGaussInstanceRequestBody.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenGaussInstanceRequestBody.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this OpenGaussInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this OpenGaussInstanceRequestBody.

        :return: The datastore of this OpenGaussInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreOption`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this OpenGaussInstanceRequestBody.

        :param datastore: The datastore of this OpenGaussInstanceRequestBody.
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussDatastoreOption`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this OpenGaussInstanceRequestBody.

        :return: The ha of this OpenGaussInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaOption`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this OpenGaussInstanceRequestBody.

        :param ha: The ha of this OpenGaussInstanceRequestBody.
        :type ha: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussHaOption`
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this OpenGaussInstanceRequestBody.

        参数模板ID。当不传该参数时，使用系统默认的参数模板。

        :return: The configuration_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this OpenGaussInstanceRequestBody.

        参数模板ID。当不传该参数时，使用系统默认的参数模板。

        :param configuration_id: The configuration_id of this OpenGaussInstanceRequestBody.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this OpenGaussInstanceRequestBody.

        数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。

        :return: The port of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OpenGaussInstanceRequestBody.

        数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。

        :param port: The port of this OpenGaussInstanceRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def password(self):
        """Gets the password of this OpenGaussInstanceRequestBody.

        数据库密码。必选。  取值范围：  '非空； 至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为~!@#%^*-_=+?,）四类字符中的三类字符；长度8~32个字符。'  '建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。'

        :return: The password of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OpenGaussInstanceRequestBody.

        数据库密码。必选。  取值范围：  '非空； 至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为~!@#%^*-_=+?,）四类字符中的三类字符；长度8~32个字符。'  '建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。'

        :param password: The password of this OpenGaussInstanceRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this OpenGaussInstanceRequestBody.

        :return: The backup_strategy of this OpenGaussInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this OpenGaussInstanceRequestBody.

        :param backup_strategy: The backup_strategy of this OpenGaussInstanceRequestBody.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this OpenGaussInstanceRequestBody.

        企业项目ID。只有企业租户时该参数才生效。  使用请参考《企业管理 API参考》的“[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this OpenGaussInstanceRequestBody.

        企业项目ID。只有企业租户时该参数才生效。  使用请参考《企业管理 API参考》的“[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this OpenGaussInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this OpenGaussInstanceRequestBody.

        用于磁盘加密的密钥ID，默认为空。

        :return: The disk_encryption_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this OpenGaussInstanceRequestBody.

        用于磁盘加密的密钥ID，默认为空。

        :param disk_encryption_id: The disk_encryption_id of this OpenGaussInstanceRequestBody.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenGaussInstanceRequestBody.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :return: The flavor_ref of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenGaussInstanceRequestBody.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this OpenGaussInstanceRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this OpenGaussInstanceRequestBody.

        :return: The volume of this OpenGaussInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OpenGaussInstanceRequestBody.

        :param volume: The volume of this OpenGaussInstanceRequestBody.
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this OpenGaussInstanceRequestBody.

        区域ID。  取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The region of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OpenGaussInstanceRequestBody.

        区域ID。  取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param region: The region of this OpenGaussInstanceRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OpenGaussInstanceRequestBody.

        可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OpenGaussInstanceRequestBody.

        可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this OpenGaussInstanceRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this OpenGaussInstanceRequestBody.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :return: The vpc_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this OpenGaussInstanceRequestBody.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :param vpc_id: The vpc_id of this OpenGaussInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this OpenGaussInstanceRequestBody.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :return: The subnet_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this OpenGaussInstanceRequestBody.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :param subnet_id: The subnet_id of this OpenGaussInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this OpenGaussInstanceRequestBody.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :return: The security_group_id of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this OpenGaussInstanceRequestBody.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :param security_group_id: The security_group_id of this OpenGaussInstanceRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this OpenGaussInstanceRequestBody.

        :return: The charge_info of this OpenGaussInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this OpenGaussInstanceRequestBody.

        :param charge_info: The charge_info of this OpenGaussInstanceRequestBody.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this OpenGaussInstanceRequestBody.

        UTC时区。  - 不选择时，GaussDB国内站、默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :return: The time_zone of this OpenGaussInstanceRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this OpenGaussInstanceRequestBody.

        UTC时区。  - 不选择时，GaussDB国内站、默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :param time_zone: The time_zone of this OpenGaussInstanceRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def sharding_num(self):
        """Gets the sharding_num of this OpenGaussInstanceRequestBody.

        仅分布式形态需要填写该参数。分片数量，取值范围1~9。

        :return: The sharding_num of this OpenGaussInstanceRequestBody.
        :rtype: int
        """
        return self._sharding_num

    @sharding_num.setter
    def sharding_num(self, sharding_num):
        """Sets the sharding_num of this OpenGaussInstanceRequestBody.

        仅分布式形态需要填写该参数。分片数量，取值范围1~9。

        :param sharding_num: The sharding_num of this OpenGaussInstanceRequestBody.
        :type sharding_num: int
        """
        self._sharding_num = sharding_num

    @property
    def coordinator_num(self):
        """Gets the coordinator_num of this OpenGaussInstanceRequestBody.

        仅分布式形态需要填写该参数。协调节点数量，取值范围1~9。CN数量必须小于或等于两倍的分片数。

        :return: The coordinator_num of this OpenGaussInstanceRequestBody.
        :rtype: int
        """
        return self._coordinator_num

    @coordinator_num.setter
    def coordinator_num(self, coordinator_num):
        """Sets the coordinator_num of this OpenGaussInstanceRequestBody.

        仅分布式形态需要填写该参数。协调节点数量，取值范围1~9。CN数量必须小于或等于两倍的分片数。

        :param coordinator_num: The coordinator_num of this OpenGaussInstanceRequestBody.
        :type coordinator_num: int
        """
        self._coordinator_num = coordinator_num

    @property
    def replica_num(self):
        """Gets the replica_num of this OpenGaussInstanceRequestBody.

        实例副本数，支持取值3。不填默认为3。仅支持1.3.0及以上版本的实例。

        :return: The replica_num of this OpenGaussInstanceRequestBody.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this OpenGaussInstanceRequestBody.

        实例副本数，支持取值3。不填默认为3。仅支持1.3.0及以上版本的实例。

        :param replica_num: The replica_num of this OpenGaussInstanceRequestBody.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def enable_force_switch(self):
        """Gets the enable_force_switch of this OpenGaussInstanceRequestBody.

        enable_force_switch表示是否开启备机强升主功能，enable_force_switch=true表示开启备机强升主功能，enable_force_switch=false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。

        :return: The enable_force_switch of this OpenGaussInstanceRequestBody.
        :rtype: bool
        """
        return self._enable_force_switch

    @enable_force_switch.setter
    def enable_force_switch(self, enable_force_switch):
        """Sets the enable_force_switch of this OpenGaussInstanceRequestBody.

        enable_force_switch表示是否开启备机强升主功能，enable_force_switch=true表示开启备机强升主功能，enable_force_switch=false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。

        :param enable_force_switch: The enable_force_switch of this OpenGaussInstanceRequestBody.
        :type enable_force_switch: bool
        """
        self._enable_force_switch = enable_force_switch

    @property
    def enable_single_float_ip(self):
        """Gets the enable_single_float_ip of this OpenGaussInstanceRequestBody.

        单浮动IP策略，仅主备版支持。默认值是false，表示不开启单浮动IP策略。 取值范围： true：开启单浮动IP策略，实例将只有一个浮动IP绑定主节点，如果发生主备倒换，浮动IP不会发生变化。 false：不开启单浮动IP策略，每个节点都会绑定一个浮动IP，如果发生主备倒换，浮动IP会发生变化。 说明： 仅支持3.206及以上版本的主备版实例。

        :return: The enable_single_float_ip of this OpenGaussInstanceRequestBody.
        :rtype: bool
        """
        return self._enable_single_float_ip

    @enable_single_float_ip.setter
    def enable_single_float_ip(self, enable_single_float_ip):
        """Sets the enable_single_float_ip of this OpenGaussInstanceRequestBody.

        单浮动IP策略，仅主备版支持。默认值是false，表示不开启单浮动IP策略。 取值范围： true：开启单浮动IP策略，实例将只有一个浮动IP绑定主节点，如果发生主备倒换，浮动IP不会发生变化。 false：不开启单浮动IP策略，每个节点都会绑定一个浮动IP，如果发生主备倒换，浮动IP会发生变化。 说明： 仅支持3.206及以上版本的主备版实例。

        :param enable_single_float_ip: The enable_single_float_ip of this OpenGaussInstanceRequestBody.
        :type enable_single_float_ip: bool
        """
        self._enable_single_float_ip = enable_single_float_ip

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
        if not isinstance(other, OpenGaussInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
