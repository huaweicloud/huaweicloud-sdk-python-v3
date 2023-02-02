# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpengaussRestoreInstanceRequest:

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
        'availability_zone': 'str',
        'flavor_ref': 'str',
        'volume': 'OpenGaussVolume',
        'disk_encryption_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'password': 'str',
        'charge_info': 'OpenGaussChargeInfo',
        'restore_point': 'RestorePoint',
        'backup_strategy': 'OpenGaussBackupStrategy',
        'enable_parallel_restore': 'bool',
        'configuration_id': 'str',
        'enterprise_project_id': 'str',
        'port': 'str',
        'time_zone': 'str',
        'enable_force_switch': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'disk_encryption_id': 'disk_encryption_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'charge_info': 'charge_info',
        'restore_point': 'restore_point',
        'backup_strategy': 'backup_strategy',
        'enable_parallel_restore': 'enable_parallel_restore',
        'configuration_id': 'configuration_id',
        'enterprise_project_id': 'enterprise_project_id',
        'port': 'port',
        'time_zone': 'time_zone',
        'enable_force_switch': 'enable_force_switch'
    }

    def __init__(self, name=None, availability_zone=None, flavor_ref=None, volume=None, disk_encryption_id=None, vpc_id=None, subnet_id=None, security_group_id=None, password=None, charge_info=None, restore_point=None, backup_strategy=None, enable_parallel_restore=None, configuration_id=None, enterprise_project_id=None, port=None, time_zone=None, enable_force_switch=None):
        """OpengaussRestoreInstanceRequest

        The model defined in huaweicloud sdk

        :param name: 实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param availability_zone: 可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\&quot;cn-north-4a,cn-north-4a,cn-north-4a\&quot;。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type availability_zone: str
        :param flavor_ref: 规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB 的“规格编码”列内容获取。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        :param disk_encryption_id: 用于磁盘加密的密钥ID，默认为空。
        :type disk_encryption_id: str
        :param vpc_id: 虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。
        :type security_group_id: str
        :param password: 数据库密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_&#x3D;+?组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestorePoint`
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        :param enable_parallel_restore: 是否支持备份并行恢复。当不传该参数时，企业版默认为不支持，主备版默认支持。
        :type enable_parallel_restore: bool
        :param configuration_id: 参数组ID，当不传该参数时，使用系统默认的参数模板。
        :type configuration_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param port: 数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。
        :type port: str
        :param time_zone: 时区。  - 不选择时，国内站默认为UTC+08:00，国际站默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。
        :type time_zone: str
        :param enable_force_switch: enable_force_switch表示是否开启备机强升主功能，仅支持取值true，false。 enable_force_switch&#x3D;true表示开启备机强升主功能，enable_force_switch&#x3D;false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。
        :type enable_force_switch: bool
        """
        
        

        self._name = None
        self._availability_zone = None
        self._flavor_ref = None
        self._volume = None
        self._disk_encryption_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._password = None
        self._charge_info = None
        self._restore_point = None
        self._backup_strategy = None
        self._enable_parallel_restore = None
        self._configuration_id = None
        self._enterprise_project_id = None
        self._port = None
        self._time_zone = None
        self._enable_force_switch = None
        self.discriminator = None

        self.name = name
        self.availability_zone = availability_zone
        self.flavor_ref = flavor_ref
        self.volume = volume
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.password = password
        if charge_info is not None:
            self.charge_info = charge_info
        self.restore_point = restore_point
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enable_parallel_restore is not None:
            self.enable_parallel_restore = enable_parallel_restore
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if port is not None:
            self.port = port
        if time_zone is not None:
            self.time_zone = time_zone
        if enable_force_switch is not None:
            self.enable_force_switch = enable_force_switch

    @property
    def name(self):
        """Gets the name of this OpengaussRestoreInstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpengaussRestoreInstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this OpengaussRestoreInstanceRequest.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OpengaussRestoreInstanceRequest.

        可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OpengaussRestoreInstanceRequest.

        可用区ID。  GaussDB取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this OpengaussRestoreInstanceRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpengaussRestoreInstanceRequest.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB 的“规格编码”列内容获取。

        :return: The flavor_ref of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpengaussRestoreInstanceRequest.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB 的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this OpengaussRestoreInstanceRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this OpengaussRestoreInstanceRequest.

        :return: The volume of this OpengaussRestoreInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OpengaussRestoreInstanceRequest.

        :param volume: The volume of this OpengaussRestoreInstanceRequest.
        :type volume: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussVolume`
        """
        self._volume = volume

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this OpengaussRestoreInstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :return: The disk_encryption_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this OpengaussRestoreInstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :param disk_encryption_id: The disk_encryption_id of this OpengaussRestoreInstanceRequest.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this OpengaussRestoreInstanceRequest.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :return: The vpc_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this OpengaussRestoreInstanceRequest.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :param vpc_id: The vpc_id of this OpengaussRestoreInstanceRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this OpengaussRestoreInstanceRequest.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :return: The subnet_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this OpengaussRestoreInstanceRequest.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :param subnet_id: The subnet_id of this OpengaussRestoreInstanceRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this OpengaussRestoreInstanceRequest.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :return: The security_group_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this OpengaussRestoreInstanceRequest.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :param security_group_id: The security_group_id of this OpengaussRestoreInstanceRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        """Gets the password of this OpengaussRestoreInstanceRequest.

        数据库密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OpengaussRestoreInstanceRequest.

        数据库密码。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this OpengaussRestoreInstanceRequest.
        :type password: str
        """
        self._password = password

    @property
    def charge_info(self):
        """Gets the charge_info of this OpengaussRestoreInstanceRequest.

        :return: The charge_info of this OpengaussRestoreInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this OpengaussRestoreInstanceRequest.

        :param charge_info: The charge_info of this OpengaussRestoreInstanceRequest.
        :type charge_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def restore_point(self):
        """Gets the restore_point of this OpengaussRestoreInstanceRequest.

        :return: The restore_point of this OpengaussRestoreInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this OpengaussRestoreInstanceRequest.

        :param restore_point: The restore_point of this OpengaussRestoreInstanceRequest.
        :type restore_point: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestorePoint`
        """
        self._restore_point = restore_point

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this OpengaussRestoreInstanceRequest.

        :return: The backup_strategy of this OpengaussRestoreInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this OpengaussRestoreInstanceRequest.

        :param backup_strategy: The backup_strategy of this OpengaussRestoreInstanceRequest.
        :type backup_strategy: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enable_parallel_restore(self):
        """Gets the enable_parallel_restore of this OpengaussRestoreInstanceRequest.

        是否支持备份并行恢复。当不传该参数时，企业版默认为不支持，主备版默认支持。

        :return: The enable_parallel_restore of this OpengaussRestoreInstanceRequest.
        :rtype: bool
        """
        return self._enable_parallel_restore

    @enable_parallel_restore.setter
    def enable_parallel_restore(self, enable_parallel_restore):
        """Sets the enable_parallel_restore of this OpengaussRestoreInstanceRequest.

        是否支持备份并行恢复。当不传该参数时，企业版默认为不支持，主备版默认支持。

        :param enable_parallel_restore: The enable_parallel_restore of this OpengaussRestoreInstanceRequest.
        :type enable_parallel_restore: bool
        """
        self._enable_parallel_restore = enable_parallel_restore

    @property
    def configuration_id(self):
        """Gets the configuration_id of this OpengaussRestoreInstanceRequest.

        参数组ID，当不传该参数时，使用系统默认的参数模板。

        :return: The configuration_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this OpengaussRestoreInstanceRequest.

        参数组ID，当不传该参数时，使用系统默认的参数模板。

        :param configuration_id: The configuration_id of this OpengaussRestoreInstanceRequest.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this OpengaussRestoreInstanceRequest.

        企业项目ID。

        :return: The enterprise_project_id of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this OpengaussRestoreInstanceRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this OpengaussRestoreInstanceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def port(self):
        """Gets the port of this OpengaussRestoreInstanceRequest.

        数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。

        :return: The port of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OpengaussRestoreInstanceRequest.

        数据库对外开放的端口，不填默认为8000，可选范围为：1024-39998。限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。  - GaussDB数据库端口当前只支持设置为8000，当不传该参数时，默认端口为8000。

        :param port: The port of this OpengaussRestoreInstanceRequest.
        :type port: str
        """
        self._port = port

    @property
    def time_zone(self):
        """Gets the time_zone of this OpengaussRestoreInstanceRequest.

        时区。  - 不选择时，国内站默认为UTC+08:00，国际站默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :return: The time_zone of this OpengaussRestoreInstanceRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this OpengaussRestoreInstanceRequest.

        时区。  - 不选择时，国内站默认为UTC+08:00，国际站默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :param time_zone: The time_zone of this OpengaussRestoreInstanceRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def enable_force_switch(self):
        """Gets the enable_force_switch of this OpengaussRestoreInstanceRequest.

        enable_force_switch表示是否开启备机强升主功能，仅支持取值true，false。 enable_force_switch=true表示开启备机强升主功能，enable_force_switch=false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。

        :return: The enable_force_switch of this OpengaussRestoreInstanceRequest.
        :rtype: bool
        """
        return self._enable_force_switch

    @enable_force_switch.setter
    def enable_force_switch(self, enable_force_switch):
        """Sets the enable_force_switch of this OpengaussRestoreInstanceRequest.

        enable_force_switch表示是否开启备机强升主功能，仅支持取值true，false。 enable_force_switch=true表示开启备机强升主功能，enable_force_switch=false表示关闭，默认关闭。仅支持1.2.2及以上版本。  说明：  备机强升主功能适用场景：在主机发生故障后，为了保障集群的可用性，强制拉起备机作为新主机对外提供服务的场景。 本功能在集群故障状态下，以丢失部分数据为代价换取集群尽可能快的恢复服务。本功能是集群状态为不可用时的一个逃生方法，如果操作者不清楚备机强升后丢失数据对业务的影响，请勿使用本功能。 备机强升主相关介绍请参考《故障处理》备机强升主章节。

        :param enable_force_switch: The enable_force_switch of this OpengaussRestoreInstanceRequest.
        :type enable_force_switch: bool
        """
        self._enable_force_switch = enable_force_switch

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
        if not isinstance(other, OpengaussRestoreInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
