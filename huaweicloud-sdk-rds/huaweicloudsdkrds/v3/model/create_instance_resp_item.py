# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRespItem:

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
        'datastore': 'Datastore',
        'ha': 'Ha',
        'configuration_id': 'str',
        'port': 'str',
        'backup_strategy': 'BackupStrategy',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'Volume',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfo',
        'collation': 'str',
        'restore_point': 'RestorePoint'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'datastore': 'datastore',
        'ha': 'ha',
        'configuration_id': 'configuration_id',
        'port': 'port',
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
        'collation': 'collation',
        'restore_point': 'restore_point'
    }

    def __init__(self, id=None, name=None, status=None, datastore=None, ha=None, configuration_id=None, port=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, collation=None, restore_point=None):
        """CreateInstanceRespItem

        The model defined in huaweicloud sdk

        :param id: 实例id
        :type id: str
        :param name: 实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名，其中，SQL Server实例名唯一。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param status: 实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。
        :type status: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.Datastore`
        :param ha: 
        :type ha: :class:`huaweicloudsdkrds.v3.Ha`
        :param configuration_id: 参数组ID。
        :type configuration_id: str
        :param port: 数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。
        :type port: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param disk_encryption_id: 用于磁盘加密的密钥ID。
        :type disk_encryption_id: str
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkrds.v3.Volume`
        :param region: 区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type region: str
        :param availability_zone: 可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。
        :type vpc_id: str
        :param subnet_id: 子网ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。
        :type subnet_id: str
        :param security_group_id: 安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。
        :type security_group_id: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        :param collation: 仅限Microsoft SQL Server实例使用。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。
        :type collation: str
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkrds.v3.RestorePoint`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._datastore = None
        self._ha = None
        self._configuration_id = None
        self._port = None
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
        self._collation = None
        self._restore_point = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if status is not None:
            self.status = status
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
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
        if collation is not None:
            self.collation = collation
        if restore_point is not None:
            self.restore_point = restore_point

    @property
    def id(self):
        """Gets the id of this CreateInstanceRespItem.

        实例id

        :return: The id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateInstanceRespItem.

        实例id

        :param id: The id of this CreateInstanceRespItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateInstanceRespItem.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名，其中，SQL Server实例名唯一。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceRespItem.

        实例名称。 用于表示实例的名称，同一租户下，同类型的实例名可重名，其中，SQL Server实例名唯一。 取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this CreateInstanceRespItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateInstanceRespItem.

        实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。

        :return: The status of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInstanceRespItem.

        实例状态。如BUILD，表示创建中。 仅创建按需实例时会返回该参数。

        :param status: The status of this CreateInstanceRespItem.
        :type status: str
        """
        self._status = status

    @property
    def datastore(self):
        """Gets the datastore of this CreateInstanceRespItem.


        :return: The datastore of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateInstanceRespItem.


        :param datastore: The datastore of this CreateInstanceRespItem.
        :type datastore: :class:`huaweicloudsdkrds.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this CreateInstanceRespItem.


        :return: The ha of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.Ha`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this CreateInstanceRespItem.


        :param ha: The ha of this CreateInstanceRespItem.
        :type ha: :class:`huaweicloudsdkrds.v3.Ha`
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this CreateInstanceRespItem.

        参数组ID。

        :return: The configuration_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this CreateInstanceRespItem.

        参数组ID。

        :param configuration_id: The configuration_id of this CreateInstanceRespItem.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this CreateInstanceRespItem.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :return: The port of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateInstanceRespItem.

        数据库端口信息。  - MySQL数据库端口设置范围为1024～65535（其中12017和33071被RDS系统占用不可设置）。 - PostgreSQL数据库端口修改范围为2100～9500。 - Microsoft SQL Server实例的端口设置范围为1433和2100~9500（其中5355和5985不可设置。对于2017 EE、2017 SE、2017 Web版，5050、5353和5986不可设置。  当不传该参数时，默认端口如下：  - MySQL默认3306。 - PostgreSQL默认5432。 - Microsoft SQL Server默认1433。

        :param port: The port of this CreateInstanceRespItem.
        :type port: str
        """
        self._port = port

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateInstanceRespItem.


        :return: The backup_strategy of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateInstanceRespItem.


        :param backup_strategy: The backup_strategy of this CreateInstanceRespItem.
        :type backup_strategy: :class:`huaweicloudsdkrds.v3.BackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceRespItem.

        企业项目ID。

        :return: The enterprise_project_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceRespItem.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRespItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this CreateInstanceRespItem.

        用于磁盘加密的密钥ID。

        :return: The disk_encryption_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this CreateInstanceRespItem.

        用于磁盘加密的密钥ID。

        :param disk_encryption_id: The disk_encryption_id of this CreateInstanceRespItem.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateInstanceRespItem.

        规格码。

        :return: The flavor_ref of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateInstanceRespItem.

        规格码。

        :param flavor_ref: The flavor_ref of this CreateInstanceRespItem.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this CreateInstanceRespItem.


        :return: The volume of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateInstanceRespItem.


        :param volume: The volume of this CreateInstanceRespItem.
        :type volume: :class:`huaweicloudsdkrds.v3.Volume`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this CreateInstanceRespItem.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The region of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRespItem.

        区域ID。创建主实例时必选，其它场景不可选。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param region: The region of this CreateInstanceRespItem.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstanceRespItem.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstanceRespItem.

        可用区ID。对于数据库实例类型不是单机的实例，需要分别为实例所有节点指定可用区，并用逗号隔开。 取值参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this CreateInstanceRespItem.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceRespItem.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The vpc_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceRespItem.

        虚拟私有云ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param vpc_id: The vpc_id of this CreateInstanceRespItem.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceRespItem.

        子网ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The subnet_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceRespItem.

        子网ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param subnet_id: The subnet_id of this CreateInstanceRespItem.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceRespItem.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :return: The security_group_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceRespItem.

        安全组ID。创建只读实例时不可选（只读实例的网络属性默认和主实例相同），其它场景必选。

        :param security_group_id: The security_group_id of this CreateInstanceRespItem.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateInstanceRespItem.


        :return: The charge_info of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateInstanceRespItem.


        :param charge_info: The charge_info of this CreateInstanceRespItem.
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def collation(self):
        """Gets the collation of this CreateInstanceRespItem.

        仅限Microsoft SQL Server实例使用。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。

        :return: The collation of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        """Sets the collation of this CreateInstanceRespItem.

        仅限Microsoft SQL Server实例使用。取值范围：根据查询SQL Server可用字符集的字符集查询列表查询可设置的字符集。

        :param collation: The collation of this CreateInstanceRespItem.
        :type collation: str
        """
        self._collation = collation

    @property
    def restore_point(self):
        """Gets the restore_point of this CreateInstanceRespItem.


        :return: The restore_point of this CreateInstanceRespItem.
        :rtype: :class:`huaweicloudsdkrds.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this CreateInstanceRespItem.


        :param restore_point: The restore_point of this CreateInstanceRespItem.
        :type restore_point: :class:`huaweicloudsdkrds.v3.RestorePoint`
        """
        self._restore_point = restore_point

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
        if not isinstance(other, CreateInstanceRespItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
