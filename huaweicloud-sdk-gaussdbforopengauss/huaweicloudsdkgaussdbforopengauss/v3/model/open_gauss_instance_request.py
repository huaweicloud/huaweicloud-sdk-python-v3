# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussInstanceRequest:


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
        'datastore': 'OpenGaussDatastore',
        'ha': 'OpenGaussHa',
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
        'replica_num': 'int'
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
        'replica_num': 'replica_num'
    }

    def __init__(self, name=None, datastore=None, ha=None, configuration_id=None, port=None, password=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, time_zone=None, sharding_num=None, coordinator_num=None, replica_num=None):
        """OpenGaussInstanceRequest - a model defined in huaweicloud sdk"""
        
        

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
        self.sharding_num = sharding_num
        self.coordinator_num = coordinator_num
        if replica_num is not None:
            self.replica_num = replica_num

    @property
    def name(self):
        """Gets the name of this OpenGaussInstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenGaussInstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this OpenGaussInstanceRequest.
        :type: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this OpenGaussInstanceRequest.


        :return: The datastore of this OpenGaussInstanceRequest.
        :rtype: OpenGaussDatastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this OpenGaussInstanceRequest.


        :param datastore: The datastore of this OpenGaussInstanceRequest.
        :type: OpenGaussDatastore
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this OpenGaussInstanceRequest.


        :return: The ha of this OpenGaussInstanceRequest.
        :rtype: OpenGaussHa
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this OpenGaussInstanceRequest.


        :param ha: The ha of this OpenGaussInstanceRequest.
        :type: OpenGaussHa
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this OpenGaussInstanceRequest.

        参数模板ID。当不传该参数时，使用系统默认的参数模板。

        :return: The configuration_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this OpenGaussInstanceRequest.

        参数模板ID。当不传该参数时，使用系统默认的参数模板。

        :param configuration_id: The configuration_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this OpenGaussInstanceRequest.

        数据库端口信息。 - GaussDB(openGauss)   数据库端口设置范围为1024~39998（其中2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124被系统占用不可设置）  当不传该参数时，默认端口如下：  - GaussDB(openGauss)默认8000

        :return: The port of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OpenGaussInstanceRequest.

        数据库端口信息。 - GaussDB(openGauss)   数据库端口设置范围为1024~39998（其中2378,2379,2380,4999,5000,5999,6000,6001,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124被系统占用不可设置）  当不传该参数时，默认端口如下：  - GaussDB(openGauss)默认8000

        :param port: The port of this OpenGaussInstanceRequest.
        :type: str
        """
        self._port = port

    @property
    def password(self):
        """Gets the password of this OpenGaussInstanceRequest.

        数据库密码。必选。  取值范围：  '非空； 至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为~!@#%^*-_=+?,）四类字符中的三类字符；长度8~32个字符。'  '建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。'

        :return: The password of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OpenGaussInstanceRequest.

        数据库密码。必选。  取值范围：  '非空； 至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为~!@#%^*-_=+?,）四类字符中的三类字符；长度8~32个字符。'  '建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。'

        :param password: The password of this OpenGaussInstanceRequest.
        :type: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this OpenGaussInstanceRequest.


        :return: The backup_strategy of this OpenGaussInstanceRequest.
        :rtype: OpenGaussBackupStrategy
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this OpenGaussInstanceRequest.


        :param backup_strategy: The backup_strategy of this OpenGaussInstanceRequest.
        :type: OpenGaussBackupStrategy
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this OpenGaussInstanceRequest.

        企业项目ID。只有企业租户时该参数才生效。  使用请参考《企业管理 API参考》的“[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this OpenGaussInstanceRequest.

        企业项目ID。只有企业租户时该参数才生效。  使用请参考《企业管理 API参考》的“[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this OpenGaussInstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :return: The disk_encryption_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this OpenGaussInstanceRequest.

        用于磁盘加密的密钥ID，默认为空。

        :param disk_encryption_id: The disk_encryption_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this OpenGaussInstanceRequest.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB(for openGauss)的“规格编码”列内容获取。

        :return: The flavor_ref of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this OpenGaussInstanceRequest.

        规格码，取值范围：非空。参考[表1](https://support.huaweicloud.com/api-opengauss/opengauss_api_0037.html#opengauss_api_0037__ted9b9d433c8a4c52884e199e17f94479)中GaussDB(for openGauss)的“规格编码”列内容获取。

        :param flavor_ref: The flavor_ref of this OpenGaussInstanceRequest.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this OpenGaussInstanceRequest.


        :return: The volume of this OpenGaussInstanceRequest.
        :rtype: OpenGaussVolume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OpenGaussInstanceRequest.


        :param volume: The volume of this OpenGaussInstanceRequest.
        :type: OpenGaussVolume
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this OpenGaussInstanceRequest.

        区域ID。  取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The region of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OpenGaussInstanceRequest.

        区域ID。  取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param region: The region of this OpenGaussInstanceRequest.
        :type: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OpenGaussInstanceRequest.

        可用区ID。  GaussDB(for openGauss)取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OpenGaussInstanceRequest.

        可用区ID。  GaussDB(for openGauss)取值范围：非空，可选部署在同一可用区或三个不同可用区，可用区之间用逗号隔开。详见示例。  - 部署在同一可用区：需要输入三个相同的可用区。例如：部署在“cn-north-4a”可用区，则需要在此处输入\"cn-north-4a,cn-north-4a,cn-north-4a\"。 - 部署在三个不同可用区：需要分别输入三个不同的可用区。 取值范围：非空，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this OpenGaussInstanceRequest.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this OpenGaussInstanceRequest.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :return: The vpc_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this OpenGaussInstanceRequest.

        虚拟私有云ID，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。

        :param vpc_id: The vpc_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this OpenGaussInstanceRequest.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :return: The subnet_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this OpenGaussInstanceRequest.

        子网的网络ID信息，获取方法如下：  - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。

        :param subnet_id: The subnet_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this OpenGaussInstanceRequest.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :return: The security_group_id of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this OpenGaussInstanceRequest.

        指定实例所属的安全组。如果不需要指定安全组，请联系客服申请白名单。  - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_sg01_0003.html)。

        :param security_group_id: The security_group_id of this OpenGaussInstanceRequest.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this OpenGaussInstanceRequest.


        :return: The charge_info of this OpenGaussInstanceRequest.
        :rtype: OpenGaussChargeInfo
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this OpenGaussInstanceRequest.


        :param charge_info: The charge_info of this OpenGaussInstanceRequest.
        :type: OpenGaussChargeInfo
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this OpenGaussInstanceRequest.

        UTC时区。  - 不选择时，GaussDB(for openGauss)国内站、默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :return: The time_zone of this OpenGaussInstanceRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this OpenGaussInstanceRequest.

        UTC时区。  - 不选择时，GaussDB(for openGauss)国内站、默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :param time_zone: The time_zone of this OpenGaussInstanceRequest.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def sharding_num(self):
        """Gets the sharding_num of this OpenGaussInstanceRequest.

        分片数量，取值范围1~9。

        :return: The sharding_num of this OpenGaussInstanceRequest.
        :rtype: int
        """
        return self._sharding_num

    @sharding_num.setter
    def sharding_num(self, sharding_num):
        """Sets the sharding_num of this OpenGaussInstanceRequest.

        分片数量，取值范围1~9。

        :param sharding_num: The sharding_num of this OpenGaussInstanceRequest.
        :type: int
        """
        self._sharding_num = sharding_num

    @property
    def coordinator_num(self):
        """Gets the coordinator_num of this OpenGaussInstanceRequest.

        协调节点数量，取值范围1~9。CN数量必须小于或等于两倍的分片数。

        :return: The coordinator_num of this OpenGaussInstanceRequest.
        :rtype: int
        """
        return self._coordinator_num

    @coordinator_num.setter
    def coordinator_num(self, coordinator_num):
        """Sets the coordinator_num of this OpenGaussInstanceRequest.

        协调节点数量，取值范围1~9。CN数量必须小于或等于两倍的分片数。

        :param coordinator_num: The coordinator_num of this OpenGaussInstanceRequest.
        :type: int
        """
        self._coordinator_num = coordinator_num

    @property
    def replica_num(self):
        """Gets the replica_num of this OpenGaussInstanceRequest.

        实例副本数，支持取值2，3。不填默认为3。  说明： 2副本选项仅针对特定用户开放，如需配置白名单权限，您可以在管理控制台右上角，选择“[工单 > 新建工单](https://auth.huaweicloud.com/authui/login.html?service=https%3A%2F%2Fconsole.huaweicloud.com%2Fticket%2F%3Fregion%3Dcn-north-1%26locale%3Dzh-cn%26cloud_route_state%3D%2Fticketindex%2FcreateIndex#/login)”，提交开通白名单的申请。

        :return: The replica_num of this OpenGaussInstanceRequest.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this OpenGaussInstanceRequest.

        实例副本数，支持取值2，3。不填默认为3。  说明： 2副本选项仅针对特定用户开放，如需配置白名单权限，您可以在管理控制台右上角，选择“[工单 > 新建工单](https://auth.huaweicloud.com/authui/login.html?service=https%3A%2F%2Fconsole.huaweicloud.com%2Fticket%2F%3Fregion%3Dcn-north-1%26locale%3Dzh-cn%26cloud_route_state%3D%2Fticketindex%2FcreateIndex#/login)”，提交开通白名单的申请。

        :param replica_num: The replica_num of this OpenGaussInstanceRequest.
        :type: int
        """
        self._replica_num = replica_num

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
        if not isinstance(other, OpenGaussInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
