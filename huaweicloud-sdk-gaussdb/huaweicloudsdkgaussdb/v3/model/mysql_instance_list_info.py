# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceListInfo:

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
        'port': 'str',
        'type': 'str',
        'region': 'str',
        'datastore': 'MysqlDatastoreWithKernelVersion',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'flavor_ref': 'str',
        'flavor_info': 'MysqlFlavorInfo',
        'volume': 'MysqlVolumeInfo',
        'backup_strategy': 'MysqlBackupStrategy',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'charge_info': 'MysqlChargeInfo',
        'dedicated_resource_id': 'str',
        'tags': 'list[InstanceTagItem]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'private_ips': 'private_ips',
        'public_ips': 'public_ips',
        'port': 'port',
        'type': 'type',
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
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'charge_info': 'charge_info',
        'dedicated_resource_id': 'dedicated_resource_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, status=None, private_ips=None, public_ips=None, port=None, type=None, region=None, datastore=None, created=None, updated=None, db_user_name=None, vpc_id=None, subnet_id=None, security_group_id=None, flavor_ref=None, flavor_info=None, volume=None, backup_strategy=None, enterprise_project_id=None, time_zone=None, charge_info=None, dedicated_resource_id=None, tags=None):
        """MysqlInstanceListInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 创建的实例名称。
        :type name: str
        :param status: 实例状态。
        :type status: str
        :param private_ips: 实例写内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。
        :type private_ips: list[str]
        :param public_ips: 实例外网IP地址列表。
        :type public_ips: list[str]
        :param port: 数据库端口号。
        :type port: str
        :param type: 实例类型，取值为“Cluster”。
        :type type: str
        :param region: 实例所在区域。
        :type region: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        :param created: 创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type created: str
        :param updated: 更新时间，格式与\&quot;created\&quot;字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type updated: str
        :param db_user_name: 默认用户名。
        :type db_user_name: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param flavor_info: 
        :type flavor_info: :class:`huaweicloudsdkgaussdb.v3.MysqlFlavorInfo`
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlVolumeInfo`
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        :param dedicated_resource_id: 专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。
        :type dedicated_resource_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.InstanceTagItem`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._private_ips = None
        self._public_ips = None
        self._port = None
        self._type = None
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
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._charge_info = None
        self._dedicated_resource_id = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        if status is not None:
            self.status = status
        if private_ips is not None:
            self.private_ips = private_ips
        if public_ips is not None:
            self.public_ips = public_ips
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if region is not None:
            self.region = region
        if datastore is not None:
            self.datastore = datastore
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if db_user_name is not None:
            self.db_user_name = db_user_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if flavor_info is not None:
            self.flavor_info = flavor_info
        if volume is not None:
            self.volume = volume
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if time_zone is not None:
            self.time_zone = time_zone
        if charge_info is not None:
            self.charge_info = charge_info
        if dedicated_resource_id is not None:
            self.dedicated_resource_id = dedicated_resource_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this MysqlInstanceListInfo.

        实例ID。

        :return: The id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlInstanceListInfo.

        实例ID。

        :param id: The id of this MysqlInstanceListInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MysqlInstanceListInfo.

        创建的实例名称。

        :return: The name of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlInstanceListInfo.

        创建的实例名称。

        :param name: The name of this MysqlInstanceListInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this MysqlInstanceListInfo.

        实例状态。

        :return: The status of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlInstanceListInfo.

        实例状态。

        :param status: The status of this MysqlInstanceListInfo.
        :type status: str
        """
        self._status = status

    @property
    def private_ips(self):
        """Gets the private_ips of this MysqlInstanceListInfo.

        实例写内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :return: The private_ips of this MysqlInstanceListInfo.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        """Sets the private_ips of this MysqlInstanceListInfo.

        实例写内网IP地址列表。弹性云服务器创建成功后该值存在，其他情况下为空字符串。

        :param private_ips: The private_ips of this MysqlInstanceListInfo.
        :type private_ips: list[str]
        """
        self._private_ips = private_ips

    @property
    def public_ips(self):
        """Gets the public_ips of this MysqlInstanceListInfo.

        实例外网IP地址列表。

        :return: The public_ips of this MysqlInstanceListInfo.
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        """Sets the public_ips of this MysqlInstanceListInfo.

        实例外网IP地址列表。

        :param public_ips: The public_ips of this MysqlInstanceListInfo.
        :type public_ips: list[str]
        """
        self._public_ips = public_ips

    @property
    def port(self):
        """Gets the port of this MysqlInstanceListInfo.

        数据库端口号。

        :return: The port of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MysqlInstanceListInfo.

        数据库端口号。

        :param port: The port of this MysqlInstanceListInfo.
        :type port: str
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this MysqlInstanceListInfo.

        实例类型，取值为“Cluster”。

        :return: The type of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlInstanceListInfo.

        实例类型，取值为“Cluster”。

        :param type: The type of this MysqlInstanceListInfo.
        :type type: str
        """
        self._type = type

    @property
    def region(self):
        """Gets the region of this MysqlInstanceListInfo.

        实例所在区域。

        :return: The region of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this MysqlInstanceListInfo.

        实例所在区域。

        :param region: The region of this MysqlInstanceListInfo.
        :type region: str
        """
        self._region = region

    @property
    def datastore(self):
        """Gets the datastore of this MysqlInstanceListInfo.

        :return: The datastore of this MysqlInstanceListInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this MysqlInstanceListInfo.

        :param datastore: The datastore of this MysqlInstanceListInfo.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreWithKernelVersion`
        """
        self._datastore = datastore

    @property
    def created(self):
        """Gets the created of this MysqlInstanceListInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The created of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MysqlInstanceListInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param created: The created of this MysqlInstanceListInfo.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this MysqlInstanceListInfo.

        更新时间，格式与\"created\"字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this MysqlInstanceListInfo.

        更新时间，格式与\"created\"字段对应格式完全相同。  说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this MysqlInstanceListInfo.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        """Gets the db_user_name of this MysqlInstanceListInfo.

        默认用户名。

        :return: The db_user_name of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this MysqlInstanceListInfo.

        默认用户名。

        :param db_user_name: The db_user_name of this MysqlInstanceListInfo.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this MysqlInstanceListInfo.

        虚拟私有云ID。

        :return: The vpc_id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this MysqlInstanceListInfo.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this MysqlInstanceListInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this MysqlInstanceListInfo.

        子网的网络ID信息。

        :return: The subnet_id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this MysqlInstanceListInfo.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this MysqlInstanceListInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this MysqlInstanceListInfo.

        安全组ID。

        :return: The security_group_id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this MysqlInstanceListInfo.

        安全组ID。

        :param security_group_id: The security_group_id of this MysqlInstanceListInfo.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this MysqlInstanceListInfo.

        规格码。

        :return: The flavor_ref of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this MysqlInstanceListInfo.

        规格码。

        :param flavor_ref: The flavor_ref of this MysqlInstanceListInfo.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def flavor_info(self):
        """Gets the flavor_info of this MysqlInstanceListInfo.

        :return: The flavor_info of this MysqlInstanceListInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlFlavorInfo`
        """
        return self._flavor_info

    @flavor_info.setter
    def flavor_info(self, flavor_info):
        """Sets the flavor_info of this MysqlInstanceListInfo.

        :param flavor_info: The flavor_info of this MysqlInstanceListInfo.
        :type flavor_info: :class:`huaweicloudsdkgaussdb.v3.MysqlFlavorInfo`
        """
        self._flavor_info = flavor_info

    @property
    def volume(self):
        """Gets the volume of this MysqlInstanceListInfo.

        :return: The volume of this MysqlInstanceListInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlVolumeInfo`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MysqlInstanceListInfo.

        :param volume: The volume of this MysqlInstanceListInfo.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlVolumeInfo`
        """
        self._volume = volume

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this MysqlInstanceListInfo.

        :return: The backup_strategy of this MysqlInstanceListInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this MysqlInstanceListInfo.

        :param backup_strategy: The backup_strategy of this MysqlInstanceListInfo.
        :type backup_strategy: :class:`huaweicloudsdkgaussdb.v3.MysqlBackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MysqlInstanceListInfo.

        企业项目ID。

        :return: The enterprise_project_id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MysqlInstanceListInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this MysqlInstanceListInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        """Gets the time_zone of this MysqlInstanceListInfo.

        时区。

        :return: The time_zone of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this MysqlInstanceListInfo.

        时区。

        :param time_zone: The time_zone of this MysqlInstanceListInfo.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def charge_info(self):
        """Gets the charge_info of this MysqlInstanceListInfo.

        :return: The charge_info of this MysqlInstanceListInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this MysqlInstanceListInfo.

        :param charge_info: The charge_info of this MysqlInstanceListInfo.
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.MysqlChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def dedicated_resource_id(self):
        """Gets the dedicated_resource_id of this MysqlInstanceListInfo.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :return: The dedicated_resource_id of this MysqlInstanceListInfo.
        :rtype: str
        """
        return self._dedicated_resource_id

    @dedicated_resource_id.setter
    def dedicated_resource_id(self, dedicated_resource_id):
        """Sets the dedicated_resource_id of this MysqlInstanceListInfo.

        专属资源池ID，只有数据库实例属于专属资源池才会返回该参数。

        :param dedicated_resource_id: The dedicated_resource_id of this MysqlInstanceListInfo.
        :type dedicated_resource_id: str
        """
        self._dedicated_resource_id = dedicated_resource_id

    @property
    def tags(self):
        """Gets the tags of this MysqlInstanceListInfo.

        标签列表。

        :return: The tags of this MysqlInstanceListInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.InstanceTagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MysqlInstanceListInfo.

        标签列表。

        :param tags: The tags of this MysqlInstanceListInfo.
        :type tags: list[:class:`huaweicloudsdkgaussdb.v3.InstanceTagItem`]
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
        if not isinstance(other, MysqlInstanceListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
