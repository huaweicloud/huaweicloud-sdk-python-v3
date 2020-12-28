# coding: utf-8

import pprint
import re

import six





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
        'tags': 'list[InstanceRequestTags]'
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
        'tags': 'tags'
    }

    def __init__(self, name=None, datastore=None, ha=None, configuration_id=None, port=None, password=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, data_vip=None, security_group_id=None, charge_info=None, time_zone=None, dsspool_id=None, replica_of_id=None, restore_point=None, collation=None, tags=None):
        """InstanceRequest - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def name(self):
        """Gets the name of this InstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名，其中，SQL Server实例名唯一。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this InstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceRequest.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名，其中，SQL Server实例名唯一。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this InstanceRequest.
        :type: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this InstanceRequest.


        :return: The datastore of this InstanceRequest.
        :rtype: Datastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this InstanceRequest.


        :param datastore: The datastore of this InstanceRequest.
        :type: Datastore
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this InstanceRequest.


        :return: The ha of this InstanceRequest.
        :rtype: Ha
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this InstanceRequest.


        :param ha: The ha of this InstanceRequest.
        :type: Ha
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this InstanceRequest.

        参数组ID。

        :return: The configuration_id of this InstanceRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this InstanceRequest.

        参数组ID。

        :param configuration_id: The configuration_id of this InstanceRequest.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this InstanceRequest.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :return: The port of this InstanceRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InstanceRequest.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :param port: The port of this InstanceRequest.
        :type: str
        """
        self._port = port

    @property
    def password(self):
        """Gets the password of this InstanceRequest.

        数据库密码。创建只读实例时不可选，其它场景必选。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this InstanceRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InstanceRequest.

        数据库密码。创建只读实例时不可选，其它场景必选。  取值范围：  非空，由大小写字母、数字和特殊符号~!@#%^*-_=+?组成，长度8~32个字符。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this InstanceRequest.
        :type: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this InstanceRequest.


        :return: The backup_strategy of this InstanceRequest.
        :rtype: BackupStrategy
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this InstanceRequest.


        :param backup_strategy: The backup_strategy of this InstanceRequest.
        :type: BackupStrategy
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceRequest.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this InstanceRequest.

        用于磁盘加密的密钥ID。

        :return: The disk_encryption_id of this InstanceRequest.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this InstanceRequest.

        用于磁盘加密的密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this InstanceRequest.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this InstanceRequest.

        规格码。

        :return: The flavor_ref of this InstanceRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this InstanceRequest.

        规格码。

        :param flavor_ref: The flavor_ref of this InstanceRequest.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this InstanceRequest.


        :return: The volume of this InstanceRequest.
        :rtype: Volume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InstanceRequest.


        :param volume: The volume of this InstanceRequest.
        :type: Volume
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this InstanceRequest.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The region of this InstanceRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstanceRequest.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param region: The region of this InstanceRequest.
        :type: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this InstanceRequest.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this InstanceRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this InstanceRequest.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this InstanceRequest.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceRequest.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The vpc_id of this InstanceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceRequest.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param vpc_id: The vpc_id of this InstanceRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceRequest.

        子网ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The subnet_id of this InstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceRequest.

        子网ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param subnet_id: The subnet_id of this InstanceRequest.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def data_vip(self):
        """Gets the data_vip of this InstanceRequest.

        指定实例的内网IP

        :return: The data_vip of this InstanceRequest.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        """Sets the data_vip of this InstanceRequest.

        指定实例的内网IP

        :param data_vip: The data_vip of this InstanceRequest.
        :type: str
        """
        self._data_vip = data_vip

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceRequest.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The security_group_id of this InstanceRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceRequest.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param security_group_id: The security_group_id of this InstanceRequest.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this InstanceRequest.


        :return: The charge_info of this InstanceRequest.
        :rtype: ChargeInfo
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this InstanceRequest.


        :param charge_info: The charge_info of this InstanceRequest.
        :type: ChargeInfo
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this InstanceRequest.

        时区。  - 不选择时，各个引擎时区如下：   - MySQL国内站、国际站默认为UTC时间。   - PostgreSQL国内站、国际站默认为UTC时间。   - Microsoft SQL Server国内站默认为UTC+08:00，国际站默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :return: The time_zone of this InstanceRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InstanceRequest.

        时区。  - 不选择时，各个引擎时区如下：   - MySQL国内站、国际站默认为UTC时间。   - PostgreSQL国内站、国际站默认为UTC时间。   - Microsoft SQL Server国内站默认为UTC+08:00，国际站默认为UTC时间。 - 选择填写时，取值范围为UTC-12:00~UTC+12:00，且只支持整段时间，如UTC+08:00，不支持UTC+08:30。

        :param time_zone: The time_zone of this InstanceRequest.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def dsspool_id(self):
        """Gets the dsspool_id of this InstanceRequest.

        专属存储池ID。

        :return: The dsspool_id of this InstanceRequest.
        :rtype: str
        """
        return self._dsspool_id

    @dsspool_id.setter
    def dsspool_id(self, dsspool_id):
        """Sets the dsspool_id of this InstanceRequest.

        专属存储池ID。

        :param dsspool_id: The dsspool_id of this InstanceRequest.
        :type: str
        """
        self._dsspool_id = dsspool_id

    @property
    def replica_of_id(self):
        """Gets the replica_of_id of this InstanceRequest.

        只读实例的主实例ID。创建只读实例时必选，其它场景不可选。

        :return: The replica_of_id of this InstanceRequest.
        :rtype: str
        """
        return self._replica_of_id

    @replica_of_id.setter
    def replica_of_id(self, replica_of_id):
        """Sets the replica_of_id of this InstanceRequest.

        只读实例的主实例ID。创建只读实例时必选，其它场景不可选。

        :param replica_of_id: The replica_of_id of this InstanceRequest.
        :type: str
        """
        self._replica_of_id = replica_of_id

    @property
    def restore_point(self):
        """Gets the restore_point of this InstanceRequest.


        :return: The restore_point of this InstanceRequest.
        :rtype: RestorePoint
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this InstanceRequest.


        :param restore_point: The restore_point of this InstanceRequest.
        :type: RestorePoint
        """
        self._restore_point = restore_point

    @property
    def collation(self):
        """Gets the collation of this InstanceRequest.

        仅限Microsoft SQL Server实例使用。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。

        :return: The collation of this InstanceRequest.
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        """Sets the collation of this InstanceRequest.

        仅限Microsoft SQL Server实例使用。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。

        :param collation: The collation of this InstanceRequest.
        :type: str
        """
        self._collation = collation

    @property
    def tags(self):
        """Gets the tags of this InstanceRequest.

        标签列表。单个实例总标签数上限10个。

        :return: The tags of this InstanceRequest.
        :rtype: list[InstanceRequestTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceRequest.

        标签列表。单个实例总标签数上限10个。

        :param tags: The tags of this InstanceRequest.
        :type: list[InstanceRequestTags]
        """
        self._tags = tags

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
