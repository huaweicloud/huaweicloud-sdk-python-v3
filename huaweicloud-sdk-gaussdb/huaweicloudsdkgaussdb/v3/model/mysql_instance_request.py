# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_info': 'MysqlChargeInfo',
        'region': 'str',
        'name': 'str',
        'datastore': 'MysqlDatastoreInReq',
        'mode': 'str',
        'flavor_ref': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'configuration_id': 'str',
        'password': 'str',
        'backup_strategy': 'MysqlBackupStrategy',
        'time_zone': 'str',
        'availability_zone_mode': 'str',
        'master_availability_zone': 'str',
        'slave_count': 'int',
        'volume': 'MysqlVolume',
        'tags': 'list[MysqlTags]',
        'lower_case_table_names': 'int',
        'enterprise_project_id': 'str',
        'dedicated_resource_id': 'str',
        'restore_point': 'MysqlRestorePoint'
    }

    attribute_map = {
        'charge_info': 'charge_info',
        'region': 'region',
        'name': 'name',
        'datastore': 'datastore',
        'mode': 'mode',
        'flavor_ref': 'flavor_ref',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'configuration_id': 'configuration_id',
        'password': 'password',
        'backup_strategy': 'backup_strategy',
        'time_zone': 'time_zone',
        'availability_zone_mode': 'availability_zone_mode',
        'master_availability_zone': 'master_availability_zone',
        'slave_count': 'slave_count',
        'volume': 'volume',
        'tags': 'tags',
        'lower_case_table_names': 'lower_case_table_names',
        'enterprise_project_id': 'enterprise_project_id',
        'dedicated_resource_id': 'dedicated_resource_id',
        'restore_point': 'restore_point'
    }

    def __init__(self, charge_info=None, region=None, name=None, datastore=None, mode=None, flavor_ref=None, vpc_id=None, subnet_id=None, security_group_id=None, configuration_id=None, password=None, backup_strategy=None, time_zone=None, availability_zone_mode=None, master_availability_zone=None, slave_count=None, volume=None, tags=None, lower_case_table_names=None, enterprise_project_id=None, dedicated_resource_id=None, restore_point=None):
        """MysqlInstanceRequest

        The model defined in huaweicloud sdk

        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        :param region: 区域ID。
        :type region: str
        :param name: 实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。
        :type name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInReq`
        :param mode: 实例类型，目前仅支持Cluster。
        :type mode: str
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。
        :type security_group_id: str
        :param configuration_id: 参数模板ID。
        :type configuration_id: str
        :param password: 数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_&#x3D;+?,()&amp;，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。
        :type password: str
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        :param time_zone: 时区。默认时区为UTC。
        :type time_zone: str
        :param availability_zone_mode: 可用区类型,单可用区single或多可用区multi。
        :type availability_zone_mode: str
        :param master_availability_zone: 主可用区。
        :type master_availability_zone: str
        :param slave_count: 只读节点个数。单次接口调用最多支持创建9个只读节点。
        :type slave_count: int
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlVolume`
        :param tags: 
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        :param lower_case_table_names: 表名大小写是否敏感，默认值是“1”。  取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。
        :type lower_case_table_names: int
        :param enterprise_project_id: 企业项目ID。如果账户开通企业项目服务则该参数必选，未开启该参数不可选。
        :type enterprise_project_id: str
        :param dedicated_resource_id: 专属资源池ID，只有开通专属资源池后才可以下发此参数。
        :type dedicated_resource_id: str
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkgaussdb.v3.MysqlRestorePoint`
        """
        
        

        self._charge_info = None
        self._region = None
        self._name = None
        self._datastore = None
        self._mode = None
        self._flavor_ref = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._configuration_id = None
        self._password = None
        self._backup_strategy = None
        self._time_zone = None
        self._availability_zone_mode = None
        self._master_availability_zone = None
        self._slave_count = None
        self._volume = None
        self._tags = None
        self._lower_case_table_names = None
        self._enterprise_project_id = None
        self._dedicated_resource_id = None
        self._restore_point = None
        self.discriminator = None

        if charge_info is not None:
            self.charge_info = charge_info
        self.region = region
        self.name = name
        self.datastore = datastore
        self.mode = mode
        self.flavor_ref = flavor_ref
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if configuration_id is not None:
            self.configuration_id = configuration_id
        self.password = password
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if time_zone is not None:
            self.time_zone = time_zone
        self.availability_zone_mode = availability_zone_mode
        if master_availability_zone is not None:
            self.master_availability_zone = master_availability_zone
        self.slave_count = slave_count
        if volume is not None:
            self.volume = volume
        if tags is not None:
            self.tags = tags
        if lower_case_table_names is not None:
            self.lower_case_table_names = lower_case_table_names
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if restore_point is not None:
            self.restore_point = restore_point

    @property
    def charge_info(self):
        """Gets the charge_info of this MysqlInstanceRequest.

        :return: The charge_info of this MysqlInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this MysqlInstanceRequest.

        :param charge_info: The charge_info of this MysqlInstanceRequest.
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def region(self):
        """Gets the region of this MysqlInstanceRequest.

        区域ID。

        :return: The region of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MysqlInstanceRequest.

        区域ID。

        :param region: The region of this MysqlInstanceRequest.
        :type region: str
        """
        self._region = region

    @property
    def name(self):
        """Gets the name of this MysqlInstanceRequest.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :return: The name of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlInstanceRequest.

        实例名称。用于表示实例的名称，同一租户下，同类型的实例名可重名。  取值范围：4~64个字符之间，必须以字母开头，区分大小写，可以包含字母、数字、中划线或者下划线，不能包含其他的特殊字符。

        :param name: The name of this MysqlInstanceRequest.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this MysqlInstanceRequest.

        :return: The datastore of this MysqlInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInReq`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this MysqlInstanceRequest.

        :param datastore: The datastore of this MysqlInstanceRequest.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInReq`
        """
        self._datastore = datastore

    @property
    def mode(self):
        """Gets the mode of this MysqlInstanceRequest.

        实例类型，目前仅支持Cluster。

        :return: The mode of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MysqlInstanceRequest.

        实例类型，目前仅支持Cluster。

        :param mode: The mode of this MysqlInstanceRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this MysqlInstanceRequest.

        规格码。

        :return: The flavor_ref of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this MysqlInstanceRequest.

        规格码。

        :param flavor_ref: The flavor_ref of this MysqlInstanceRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def vpc_id(self):
        """Gets the vpc_id of this MysqlInstanceRequest.

        虚拟私有云ID。

        :return: The vpc_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this MysqlInstanceRequest.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this MysqlInstanceRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this MysqlInstanceRequest.

        子网的网络ID。

        :return: The subnet_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this MysqlInstanceRequest.

        子网的网络ID。

        :param subnet_id: The subnet_id of this MysqlInstanceRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this MysqlInstanceRequest.

        安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。

        :return: The security_group_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this MysqlInstanceRequest.

        安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。

        :param security_group_id: The security_group_id of this MysqlInstanceRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def configuration_id(self):
        """Gets the configuration_id of this MysqlInstanceRequest.

        参数模板ID。

        :return: The configuration_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this MysqlInstanceRequest.

        参数模板ID。

        :param configuration_id: The configuration_id of this MysqlInstanceRequest.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def password(self):
        """Gets the password of this MysqlInstanceRequest.

        数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。

        :return: The password of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this MysqlInstanceRequest.

        数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。

        :param password: The password of this MysqlInstanceRequest.
        :type password: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this MysqlInstanceRequest.

        :return: The backup_strategy of this MysqlInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this MysqlInstanceRequest.

        :param backup_strategy: The backup_strategy of this MysqlInstanceRequest.
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def time_zone(self):
        """Gets the time_zone of this MysqlInstanceRequest.

        时区。默认时区为UTC。

        :return: The time_zone of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this MysqlInstanceRequest.

        时区。默认时区为UTC。

        :param time_zone: The time_zone of this MysqlInstanceRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def availability_zone_mode(self):
        """Gets the availability_zone_mode of this MysqlInstanceRequest.

        可用区类型,单可用区single或多可用区multi。

        :return: The availability_zone_mode of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._availability_zone_mode

    @availability_zone_mode.setter
    def availability_zone_mode(self, availability_zone_mode):
        """Sets the availability_zone_mode of this MysqlInstanceRequest.

        可用区类型,单可用区single或多可用区multi。

        :param availability_zone_mode: The availability_zone_mode of this MysqlInstanceRequest.
        :type availability_zone_mode: str
        """
        self._availability_zone_mode = availability_zone_mode

    @property
    def master_availability_zone(self):
        """Gets the master_availability_zone of this MysqlInstanceRequest.

        主可用区。

        :return: The master_availability_zone of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._master_availability_zone

    @master_availability_zone.setter
    def master_availability_zone(self, master_availability_zone):
        """Sets the master_availability_zone of this MysqlInstanceRequest.

        主可用区。

        :param master_availability_zone: The master_availability_zone of this MysqlInstanceRequest.
        :type master_availability_zone: str
        """
        self._master_availability_zone = master_availability_zone

    @property
    def slave_count(self):
        """Gets the slave_count of this MysqlInstanceRequest.

        只读节点个数。单次接口调用最多支持创建9个只读节点。

        :return: The slave_count of this MysqlInstanceRequest.
        :rtype: int
        """
        return self._slave_count

    @slave_count.setter
    def slave_count(self, slave_count):
        """Sets the slave_count of this MysqlInstanceRequest.

        只读节点个数。单次接口调用最多支持创建9个只读节点。

        :param slave_count: The slave_count of this MysqlInstanceRequest.
        :type slave_count: int
        """
        self._slave_count = slave_count

    @property
    def volume(self):
        """Gets the volume of this MysqlInstanceRequest.

        :return: The volume of this MysqlInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MysqlInstanceRequest.

        :param volume: The volume of this MysqlInstanceRequest.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlVolume`
        """
        self._volume = volume

    @property
    def tags(self):
        """Gets the tags of this MysqlInstanceRequest.

        :return: The tags of this MysqlInstanceRequest.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MysqlInstanceRequest.

        :param tags: The tags of this MysqlInstanceRequest.
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.MysqlTags`]
        """
        self._tags = tags

    @property
    def lower_case_table_names(self):
        """Gets the lower_case_table_names of this MysqlInstanceRequest.

        表名大小写是否敏感，默认值是“1”。  取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。

        :return: The lower_case_table_names of this MysqlInstanceRequest.
        :rtype: int
        """
        return self._lower_case_table_names

    @lower_case_table_names.setter
    def lower_case_table_names(self, lower_case_table_names):
        """Sets the lower_case_table_names of this MysqlInstanceRequest.

        表名大小写是否敏感，默认值是“1”。  取值范围： - 0：表名被存储成固定且表名称大小写敏感。 - 1：表名将被存储成小写且表名称大小写不敏感。

        :param lower_case_table_names: The lower_case_table_names of this MysqlInstanceRequest.
        :type lower_case_table_names: int
        """
        self._lower_case_table_names = lower_case_table_names

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MysqlInstanceRequest.

        企业项目ID。如果账户开通企业项目服务则该参数必选，未开启该参数不可选。

        :return: The enterprise_project_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MysqlInstanceRequest.

        企业项目ID。如果账户开通企业项目服务则该参数必选，未开启该参数不可选。

        :param enterprise_project_id: The enterprise_project_id of this MysqlInstanceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this MysqlInstanceRequest.

        专属资源池ID，只有开通专属资源池后才可以下发此参数。

        :return: The dedicated_resource_id of this MysqlInstanceRequest.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this MysqlInstanceRequest.

        专属资源池ID，只有开通专属资源池后才可以下发此参数。

        :param dedicated_resource_id: The dedicated_resource_id of this MysqlInstanceRequest.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def restore_point(self):
        """Gets the restore_point of this MysqlInstanceRequest.

        :return: The restore_point of this MysqlInstanceRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlRestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this MysqlInstanceRequest.

        :param restore_point: The restore_point of this MysqlInstanceRequest.
        :type restore_point: :class:`huaweicloudsdkgaussdb.v3.MysqlRestorePoint`
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
        if not isinstance(other, MysqlInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
