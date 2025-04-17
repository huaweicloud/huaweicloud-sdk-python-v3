# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequestBody:

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
        'datastore': 'DatastoreOption',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'password': 'str',
        'mode': 'str',
        'product_type': 'str',
        'flavor': 'list[CreateInstanceFlavorOption]',
        'configuration_id': 'str',
        'backup_strategy': 'BackupStrategyOption',
        'enterprise_project_id': 'str',
        'dedicated_resource_id': 'str',
        'ssl_option': 'str',
        'charge_info': 'ChargeInfoOption',
        'restore_info': 'RestoreInfo',
        'port': 'str',
        'availability_zone_detail': 'AvailabilityZoneDetail'
    }

    attribute_map = {
        'name': 'name',
        'datastore': 'datastore',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'mode': 'mode',
        'product_type': 'product_type',
        'flavor': 'flavor',
        'configuration_id': 'configuration_id',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'dedicated_resource_id': 'dedicated_resource_id',
        'ssl_option': 'ssl_option',
        'charge_info': 'charge_info',
        'restore_info': 'restore_info',
        'port': 'port',
        'availability_zone_detail': 'availability_zone_detail'
    }

    def __init__(self, name=None, datastore=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, password=None, mode=None, product_type=None, flavor=None, configuration_id=None, backup_strategy=None, enterprise_project_id=None, dedicated_resource_id=None, ssl_option=None, charge_info=None, restore_info=None, port=None, availability_zone_detail=None):
        r"""CreateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 实例名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。
        :type name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreOption`
        :param region: - 区域ID - 取值：非空。
        :type region: str
        :param availability_zone: 可用区ID。 取值：请参见查询所有实例规格信息中返回的“az_status” ，支持创建3可用区实例，中间以逗号隔开。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。
        :type subnet_id: str
        :param security_group_id: 安全组ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。
        :type security_group_id: str
        :param password: 数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param mode: 实例类型。   -  GeminiDB Cassandra支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Cassandra支持云原生部署模式集群类型，取值“CloudNativeCluster”。   -  GeminiDB Mongo4.0版本支持副本集类型，取值为“ReplicaSet”。   -  GeminiDB Influx支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Influx支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Influx支持经典部署模式单节点类型，取值为“InfluxdbSingle”。   -  GeminiDB Redis支持经典部署模式Proxy集群类型，取值为“Cluster”。   -  GeminiDB redis支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Redis支持经典部署模式Cluster集群类型，取值为“RedisCluster”   -  GeminiDB Redis支持经典部署模式主备类型，取值为“Replication”。
        :type mode: str
        :param product_type: 产品类型   -  Capacity 容量型   -  Standard 标准型 当创建GeminiDB Redis云原生部署模式集群类型必传此参数。
        :type product_type: str
        :param flavor: 实例规格详情。获取方法请参见查询所有实例规格信息中响应“flavors”字段下参数的值。
        :type flavor: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorOption`]
        :param configuration_id: 参数模板ID。
        :type configuration_id: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyOption`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param dedicated_resource_id: 专属资源ID，只有开通专属资源池后才可以下发此参数。
        :type dedicated_resource_id: str
        :param ssl_option: SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认不启用SSL连接。
        :type ssl_option: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoOption`
        :param restore_info: 
        :type restore_info: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreInfo`
        :param port: 数据库访问端口号。 目前仅支持GeminiDB Redis实例支持自定义端口，取值范围为：1024~65535，禁用端口号为：2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。 不指定端口时，创建GeminiDB Redis实例的访问端口默认为6379。 如果该实例计划用于搭建双活容灾场景，请配置为8635端口。
        :type port: str
        :param availability_zone_detail: 
        :type availability_zone_detail: :class:`huaweicloudsdkgaussdbfornosql.v3.AvailabilityZoneDetail`
        """
        
        

        self._name = None
        self._datastore = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._password = None
        self._mode = None
        self._product_type = None
        self._flavor = None
        self._configuration_id = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._dedicated_resource_id = None
        self._ssl_option = None
        self._charge_info = None
        self._restore_info = None
        self._port = None
        self._availability_zone_detail = None
        self.discriminator = None

        self.name = name
        self.datastore = datastore
        self.region = region
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.password = password
        self.mode = mode
        if product_type is not None:
            self.product_type = product_type
        self.flavor = flavor
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if charge_info is not None:
            self.charge_info = charge_info
        if restore_info is not None:
            self.restore_info = restore_info
        if port is not None:
            self.port = port
        if availability_zone_detail is not None:
            self.availability_zone_detail = availability_zone_detail

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceRequestBody.

        实例名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :return: The name of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceRequestBody.

        实例名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :param name: The name of this CreateInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        r"""Gets the datastore of this CreateInstanceRequestBody.

        :return: The datastore of this CreateInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreOption`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CreateInstanceRequestBody.

        :param datastore: The datastore of this CreateInstanceRequestBody.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.DatastoreOption`
        """
        self._datastore = datastore

    @property
    def region(self):
        r"""Gets the region of this CreateInstanceRequestBody.

        - 区域ID - 取值：非空。

        :return: The region of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateInstanceRequestBody.

        - 区域ID - 取值：非空。

        :param region: The region of this CreateInstanceRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateInstanceRequestBody.

        可用区ID。 取值：请参见查询所有实例规格信息中返回的“az_status” ，支持创建3可用区实例，中间以逗号隔开。

        :return: The availability_zone of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateInstanceRequestBody.

        可用区ID。 取值：请参见查询所有实例规格信息中返回的“az_status” ，支持创建3可用区实例，中间以逗号隔开。

        :param availability_zone: The availability_zone of this CreateInstanceRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceRequestBody.

        虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。

        :return: The vpc_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceRequestBody.

        虚拟私有云ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询VPC列表。

        :param vpc_id: The vpc_id of this CreateInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateInstanceRequestBody.

        子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。

        :return: The subnet_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateInstanceRequestBody.

        子网的网络ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询子网列表。

        :param subnet_id: The subnet_id of this CreateInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateInstanceRequestBody.

        安全组ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。

        :return: The security_group_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateInstanceRequestBody.

        安全组ID，获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。

        :param security_group_id: The security_group_id of this CreateInstanceRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        r"""Gets the password of this CreateInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this CreateInstanceRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def mode(self):
        r"""Gets the mode of this CreateInstanceRequestBody.

        实例类型。   -  GeminiDB Cassandra支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Cassandra支持云原生部署模式集群类型，取值“CloudNativeCluster”。   -  GeminiDB Mongo4.0版本支持副本集类型，取值为“ReplicaSet”。   -  GeminiDB Influx支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Influx支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Influx支持经典部署模式单节点类型，取值为“InfluxdbSingle”。   -  GeminiDB Redis支持经典部署模式Proxy集群类型，取值为“Cluster”。   -  GeminiDB redis支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Redis支持经典部署模式Cluster集群类型，取值为“RedisCluster”   -  GeminiDB Redis支持经典部署模式主备类型，取值为“Replication”。

        :return: The mode of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateInstanceRequestBody.

        实例类型。   -  GeminiDB Cassandra支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Cassandra支持云原生部署模式集群类型，取值“CloudNativeCluster”。   -  GeminiDB Mongo4.0版本支持副本集类型，取值为“ReplicaSet”。   -  GeminiDB Influx支持经典部署模式集群类型，取值为“Cluster”。   -  GeminiDB Influx支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Influx支持经典部署模式单节点类型，取值为“InfluxdbSingle”。   -  GeminiDB Redis支持经典部署模式Proxy集群类型，取值为“Cluster”。   -  GeminiDB redis支持云原生部署模式集群类型，取值为“CloudNativeCluster”。   -  GeminiDB Redis支持经典部署模式Cluster集群类型，取值为“RedisCluster”   -  GeminiDB Redis支持经典部署模式主备类型，取值为“Replication”。

        :param mode: The mode of this CreateInstanceRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def product_type(self):
        r"""Gets the product_type of this CreateInstanceRequestBody.

        产品类型   -  Capacity 容量型   -  Standard 标准型 当创建GeminiDB Redis云原生部署模式集群类型必传此参数。

        :return: The product_type of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this CreateInstanceRequestBody.

        产品类型   -  Capacity 容量型   -  Standard 标准型 当创建GeminiDB Redis云原生部署模式集群类型必传此参数。

        :param product_type: The product_type of this CreateInstanceRequestBody.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateInstanceRequestBody.

        实例规格详情。获取方法请参见查询所有实例规格信息中响应“flavors”字段下参数的值。

        :return: The flavor of this CreateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorOption`]
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateInstanceRequestBody.

        实例规格详情。获取方法请参见查询所有实例规格信息中响应“flavors”字段下参数的值。

        :param flavor: The flavor of this CreateInstanceRequestBody.
        :type flavor: list[:class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceFlavorOption`]
        """
        self._flavor = flavor

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this CreateInstanceRequestBody.

        参数模板ID。

        :return: The configuration_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this CreateInstanceRequestBody.

        参数模板ID。

        :param configuration_id: The configuration_id of this CreateInstanceRequestBody.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def backup_strategy(self):
        r"""Gets the backup_strategy of this CreateInstanceRequestBody.

        :return: The backup_strategy of this CreateInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyOption`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        r"""Sets the backup_strategy of this CreateInstanceRequestBody.

        :param backup_strategy: The backup_strategy of this CreateInstanceRequestBody.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbfornosql.v3.BackupStrategyOption`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID。

        :return: The enterprise_project_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        r"""Gets the dedicated_resource_id of this CreateInstanceRequestBody.

        专属资源ID，只有开通专属资源池后才可以下发此参数。

        :return: The dedicated_resource_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        r"""Sets the dedicated_resource_id of this CreateInstanceRequestBody.

        专属资源ID，只有开通专属资源池后才可以下发此参数。

        :param dedicated_resource_id: The dedicated_resource_id of this CreateInstanceRequestBody.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def ssl_option(self):
        r"""Gets the ssl_option of this CreateInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认不启用SSL连接。

        :return: The ssl_option of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        r"""Sets the ssl_option of this CreateInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认不启用SSL连接。

        :param ssl_option: The ssl_option of this CreateInstanceRequestBody.
        :type ssl_option: str
        """
        self._ssl_option = ssl_option

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateInstanceRequestBody.

        :return: The charge_info of this CreateInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoOption`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateInstanceRequestBody.

        :param charge_info: The charge_info of this CreateInstanceRequestBody.
        :type charge_info: :class:`huaweicloudsdkgaussdbfornosql.v3.ChargeInfoOption`
        """
        self._charge_info = charge_info

    @property
    def restore_info(self):
        r"""Gets the restore_info of this CreateInstanceRequestBody.

        :return: The restore_info of this CreateInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreInfo`
        """
        return self._restore_info

    @restore_info.setter
    def restore_info(self, restore_info):
        r"""Sets the restore_info of this CreateInstanceRequestBody.

        :param restore_info: The restore_info of this CreateInstanceRequestBody.
        :type restore_info: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreInfo`
        """
        self._restore_info = restore_info

    @property
    def port(self):
        r"""Gets the port of this CreateInstanceRequestBody.

        数据库访问端口号。 目前仅支持GeminiDB Redis实例支持自定义端口，取值范围为：1024~65535，禁用端口号为：2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。 不指定端口时，创建GeminiDB Redis实例的访问端口默认为6379。 如果该实例计划用于搭建双活容灾场景，请配置为8635端口。

        :return: The port of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CreateInstanceRequestBody.

        数据库访问端口号。 目前仅支持GeminiDB Redis实例支持自定义端口，取值范围为：1024~65535，禁用端口号为：2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。 不指定端口时，创建GeminiDB Redis实例的访问端口默认为6379。 如果该实例计划用于搭建双活容灾场景，请配置为8635端口。

        :param port: The port of this CreateInstanceRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def availability_zone_detail(self):
        r"""Gets the availability_zone_detail of this CreateInstanceRequestBody.

        :return: The availability_zone_detail of this CreateInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.AvailabilityZoneDetail`
        """
        return self._availability_zone_detail

    @availability_zone_detail.setter
    def availability_zone_detail(self, availability_zone_detail):
        r"""Sets the availability_zone_detail of this CreateInstanceRequestBody.

        :param availability_zone_detail: The availability_zone_detail of this CreateInstanceRequestBody.
        :type availability_zone_detail: :class:`huaweicloudsdkgaussdbfornosql.v3.AvailabilityZoneDetail`
        """
        self._availability_zone_detail = availability_zone_detail

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
        if not isinstance(other, CreateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
