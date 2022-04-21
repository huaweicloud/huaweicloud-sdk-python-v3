# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProtectionGroupParams:

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
        'description': 'str',
        'status': 'str',
        'progress': 'int',
        'source_availability_zone': 'str',
        'target_availability_zone': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'priority_station': 'str',
        'protected_instance_num': 'int',
        'replication_num': 'int',
        'disaster_recovery_drill_num': 'int',
        'protected_status': 'str',
        'replication_status': 'str',
        'health_status': 'str',
        'source_vpc_id': 'str',
        'target_vpc_id': 'str',
        'test_vpc_id': 'str',
        'dr_type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'protection_type': 'str',
        'replication_model': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'progress': 'progress',
        'source_availability_zone': 'source_availability_zone',
        'target_availability_zone': 'target_availability_zone',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'priority_station': 'priority_station',
        'protected_instance_num': 'protected_instance_num',
        'replication_num': 'replication_num',
        'disaster_recovery_drill_num': 'disaster_recovery_drill_num',
        'protected_status': 'protected_status',
        'replication_status': 'replication_status',
        'health_status': 'health_status',
        'source_vpc_id': 'source_vpc_id',
        'target_vpc_id': 'target_vpc_id',
        'test_vpc_id': 'test_vpc_id',
        'dr_type': 'dr_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'protection_type': 'protection_type',
        'replication_model': 'replication_model',
        'server_type': 'server_type'
    }

    def __init__(self, id=None, name=None, description=None, status=None, progress=None, source_availability_zone=None, target_availability_zone=None, domain_id=None, domain_name=None, priority_station=None, protected_instance_num=None, replication_num=None, disaster_recovery_drill_num=None, protected_status=None, replication_status=None, health_status=None, source_vpc_id=None, target_vpc_id=None, test_vpc_id=None, dr_type=None, created_at=None, updated_at=None, protection_type=None, replication_model=None, server_type=None):
        """ShowProtectionGroupParams

        The model defined in huaweicloud sdk

        :param id: 保护组的ID。
        :type id: str
        :param name: 保护组的名称。
        :type name: str
        :param description: 保护组的描述。
        :type description: str
        :param status: 保护组的状态。
        :type status: str
        :param progress: 保护组的同步进度。单位：百分比（%）。
        :type progress: int
        :param source_availability_zone: 保护组创建时的生产站点可用区名称。注意：保护组切换、故障切换后，该值不变。
        :type source_availability_zone: str
        :param target_availability_zone: 保护组创建时的容灾站点可用区名称。注意：保护组切换、故障切换后，该值不变。
        :type target_availability_zone: str
        :param domain_id: 双活域ID。
        :type domain_id: str
        :param domain_name: 双活域名称。
        :type domain_name: str
        :param priority_station: 用于标识保护组的当前生产站点。 source：表示当前生产站点可用区为source_availability_zone的值。 target：表示当前生产站点可用区为target_availability_zone的值。
        :type priority_station: str
        :param protected_instance_num: 该保护组中保护实例的个数。
        :type protected_instance_num: int
        :param replication_num: 该保护组中复制对的个数。
        :type replication_num: int
        :param disaster_recovery_drill_num: 该保护组中容灾演练的个数。
        :type disaster_recovery_drill_num: int
        :param protected_status: 保护状态。started：表示该保护组开始保护。stopped：表示该保护组停止保护。 说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。
        :type protected_status: str
        :param replication_status: 数据同步状态。 active：表示数据已同步完成。 inactive：表示数据未同步。 copying：表示数据正在同步。 active-stopped：表示数据已停止同步。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。
        :type replication_status: str
        :param health_status: 健康状态。 normal：表示该保护组处于正常状态。 abnormal：表示该保护组处于非正常状态。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。
        :type health_status: str
        :param source_vpc_id: 生产站点虚拟私有云ID。
        :type source_vpc_id: str
        :param target_vpc_id: 容灾站点虚拟私有云ID。
        :type target_vpc_id: str
        :param test_vpc_id: 容灾演练虚拟私有云ID。（该参数暂未使用）
        :type test_vpc_id: str
        :param dr_type: 部署模式。默认值为“migration”，migration表示VPC内迁移。
        :type dr_type: str
        :param created_at: 创建时间。默认格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot;，例：\&quot;2019-04-01T12:00:00.000Z\&quot;。
        :type created_at: str
        :param updated_at: 更新时间。默认格式为：\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\&quot;，例：\&quot;2019-04-01T12:00:00.000Z\&quot;。
        :type updated_at: str
        :param protection_type: 保护模式。 replication-pair：表示以复制对为单位进行数据同步。 null：表示将保护组中的所有复制对作为一个整体进行数据同步。  说明:当保护组中的所有复制对作为一个整体进行数据同步时，如果数据同步失败，保护组中的所有复制对都会受到影响。因此，SDRS服务对系统做了优化升级： 对于升级后创建的资源，默认以复制对为单位进行数据同步，返回值为replication-pair； 对于已有资源，仍以一个整体进行数据同步，返回值为null。
        :type protection_type: str
        :param replication_model: 复制类型。 说明:预留参数，暂未启用。
        :type replication_model: str
        :param server_type: 管理的服务器类型 ECS：表示管理的服务器类型为云服务器。
        :type server_type: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._progress = None
        self._source_availability_zone = None
        self._target_availability_zone = None
        self._domain_id = None
        self._domain_name = None
        self._priority_station = None
        self._protected_instance_num = None
        self._replication_num = None
        self._disaster_recovery_drill_num = None
        self._protected_status = None
        self._replication_status = None
        self._health_status = None
        self._source_vpc_id = None
        self._target_vpc_id = None
        self._test_vpc_id = None
        self._dr_type = None
        self._created_at = None
        self._updated_at = None
        self._protection_type = None
        self._replication_model = None
        self._server_type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.progress = progress
        self.source_availability_zone = source_availability_zone
        self.target_availability_zone = target_availability_zone
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.priority_station = priority_station
        self.protected_instance_num = protected_instance_num
        self.replication_num = replication_num
        self.disaster_recovery_drill_num = disaster_recovery_drill_num
        self.protected_status = protected_status
        self.replication_status = replication_status
        self.health_status = health_status
        self.source_vpc_id = source_vpc_id
        self.target_vpc_id = target_vpc_id
        self.test_vpc_id = test_vpc_id
        self.dr_type = dr_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.protection_type = protection_type
        self.replication_model = replication_model
        self.server_type = server_type

    @property
    def id(self):
        """Gets the id of this ShowProtectionGroupParams.

        保护组的ID。

        :return: The id of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowProtectionGroupParams.

        保护组的ID。

        :param id: The id of this ShowProtectionGroupParams.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowProtectionGroupParams.

        保护组的名称。

        :return: The name of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowProtectionGroupParams.

        保护组的名称。

        :param name: The name of this ShowProtectionGroupParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowProtectionGroupParams.

        保护组的描述。

        :return: The description of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowProtectionGroupParams.

        保护组的描述。

        :param description: The description of this ShowProtectionGroupParams.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowProtectionGroupParams.

        保护组的状态。

        :return: The status of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowProtectionGroupParams.

        保护组的状态。

        :param status: The status of this ShowProtectionGroupParams.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        """Gets the progress of this ShowProtectionGroupParams.

        保护组的同步进度。单位：百分比（%）。

        :return: The progress of this ShowProtectionGroupParams.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowProtectionGroupParams.

        保护组的同步进度。单位：百分比（%）。

        :param progress: The progress of this ShowProtectionGroupParams.
        :type progress: int
        """
        self._progress = progress

    @property
    def source_availability_zone(self):
        """Gets the source_availability_zone of this ShowProtectionGroupParams.

        保护组创建时的生产站点可用区名称。注意：保护组切换、故障切换后，该值不变。

        :return: The source_availability_zone of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._source_availability_zone

    @source_availability_zone.setter
    def source_availability_zone(self, source_availability_zone):
        """Sets the source_availability_zone of this ShowProtectionGroupParams.

        保护组创建时的生产站点可用区名称。注意：保护组切换、故障切换后，该值不变。

        :param source_availability_zone: The source_availability_zone of this ShowProtectionGroupParams.
        :type source_availability_zone: str
        """
        self._source_availability_zone = source_availability_zone

    @property
    def target_availability_zone(self):
        """Gets the target_availability_zone of this ShowProtectionGroupParams.

        保护组创建时的容灾站点可用区名称。注意：保护组切换、故障切换后，该值不变。

        :return: The target_availability_zone of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._target_availability_zone

    @target_availability_zone.setter
    def target_availability_zone(self, target_availability_zone):
        """Sets the target_availability_zone of this ShowProtectionGroupParams.

        保护组创建时的容灾站点可用区名称。注意：保护组切换、故障切换后，该值不变。

        :param target_availability_zone: The target_availability_zone of this ShowProtectionGroupParams.
        :type target_availability_zone: str
        """
        self._target_availability_zone = target_availability_zone

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowProtectionGroupParams.

        双活域ID。

        :return: The domain_id of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowProtectionGroupParams.

        双活域ID。

        :param domain_id: The domain_id of this ShowProtectionGroupParams.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowProtectionGroupParams.

        双活域名称。

        :return: The domain_name of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowProtectionGroupParams.

        双活域名称。

        :param domain_name: The domain_name of this ShowProtectionGroupParams.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def priority_station(self):
        """Gets the priority_station of this ShowProtectionGroupParams.

        用于标识保护组的当前生产站点。 source：表示当前生产站点可用区为source_availability_zone的值。 target：表示当前生产站点可用区为target_availability_zone的值。

        :return: The priority_station of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._priority_station

    @priority_station.setter
    def priority_station(self, priority_station):
        """Sets the priority_station of this ShowProtectionGroupParams.

        用于标识保护组的当前生产站点。 source：表示当前生产站点可用区为source_availability_zone的值。 target：表示当前生产站点可用区为target_availability_zone的值。

        :param priority_station: The priority_station of this ShowProtectionGroupParams.
        :type priority_station: str
        """
        self._priority_station = priority_station

    @property
    def protected_instance_num(self):
        """Gets the protected_instance_num of this ShowProtectionGroupParams.

        该保护组中保护实例的个数。

        :return: The protected_instance_num of this ShowProtectionGroupParams.
        :rtype: int
        """
        return self._protected_instance_num

    @protected_instance_num.setter
    def protected_instance_num(self, protected_instance_num):
        """Sets the protected_instance_num of this ShowProtectionGroupParams.

        该保护组中保护实例的个数。

        :param protected_instance_num: The protected_instance_num of this ShowProtectionGroupParams.
        :type protected_instance_num: int
        """
        self._protected_instance_num = protected_instance_num

    @property
    def replication_num(self):
        """Gets the replication_num of this ShowProtectionGroupParams.

        该保护组中复制对的个数。

        :return: The replication_num of this ShowProtectionGroupParams.
        :rtype: int
        """
        return self._replication_num

    @replication_num.setter
    def replication_num(self, replication_num):
        """Sets the replication_num of this ShowProtectionGroupParams.

        该保护组中复制对的个数。

        :param replication_num: The replication_num of this ShowProtectionGroupParams.
        :type replication_num: int
        """
        self._replication_num = replication_num

    @property
    def disaster_recovery_drill_num(self):
        """Gets the disaster_recovery_drill_num of this ShowProtectionGroupParams.

        该保护组中容灾演练的个数。

        :return: The disaster_recovery_drill_num of this ShowProtectionGroupParams.
        :rtype: int
        """
        return self._disaster_recovery_drill_num

    @disaster_recovery_drill_num.setter
    def disaster_recovery_drill_num(self, disaster_recovery_drill_num):
        """Sets the disaster_recovery_drill_num of this ShowProtectionGroupParams.

        该保护组中容灾演练的个数。

        :param disaster_recovery_drill_num: The disaster_recovery_drill_num of this ShowProtectionGroupParams.
        :type disaster_recovery_drill_num: int
        """
        self._disaster_recovery_drill_num = disaster_recovery_drill_num

    @property
    def protected_status(self):
        """Gets the protected_status of this ShowProtectionGroupParams.

        保护状态。started：表示该保护组开始保护。stopped：表示该保护组停止保护。 说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :return: The protected_status of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        """Sets the protected_status of this ShowProtectionGroupParams.

        保护状态。started：表示该保护组开始保护。stopped：表示该保护组停止保护。 说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :param protected_status: The protected_status of this ShowProtectionGroupParams.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def replication_status(self):
        """Gets the replication_status of this ShowProtectionGroupParams.

        数据同步状态。 active：表示数据已同步完成。 inactive：表示数据未同步。 copying：表示数据正在同步。 active-stopped：表示数据已停止同步。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :return: The replication_status of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this ShowProtectionGroupParams.

        数据同步状态。 active：表示数据已同步完成。 inactive：表示数据未同步。 copying：表示数据正在同步。 active-stopped：表示数据已停止同步。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :param replication_status: The replication_status of this ShowProtectionGroupParams.
        :type replication_status: str
        """
        self._replication_status = replication_status

    @property
    def health_status(self):
        """Gets the health_status of this ShowProtectionGroupParams.

        健康状态。 normal：表示该保护组处于正常状态。 abnormal：表示该保护组处于非正常状态。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :return: The health_status of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this ShowProtectionGroupParams.

        健康状态。 normal：表示该保护组处于正常状态。 abnormal：表示该保护组处于非正常状态。  说明:系统近期进行了升级，对于升级后创建的保护组，该字段值为null，无实际意义。

        :param health_status: The health_status of this ShowProtectionGroupParams.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def source_vpc_id(self):
        """Gets the source_vpc_id of this ShowProtectionGroupParams.

        生产站点虚拟私有云ID。

        :return: The source_vpc_id of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._source_vpc_id

    @source_vpc_id.setter
    def source_vpc_id(self, source_vpc_id):
        """Sets the source_vpc_id of this ShowProtectionGroupParams.

        生产站点虚拟私有云ID。

        :param source_vpc_id: The source_vpc_id of this ShowProtectionGroupParams.
        :type source_vpc_id: str
        """
        self._source_vpc_id = source_vpc_id

    @property
    def target_vpc_id(self):
        """Gets the target_vpc_id of this ShowProtectionGroupParams.

        容灾站点虚拟私有云ID。

        :return: The target_vpc_id of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._target_vpc_id

    @target_vpc_id.setter
    def target_vpc_id(self, target_vpc_id):
        """Sets the target_vpc_id of this ShowProtectionGroupParams.

        容灾站点虚拟私有云ID。

        :param target_vpc_id: The target_vpc_id of this ShowProtectionGroupParams.
        :type target_vpc_id: str
        """
        self._target_vpc_id = target_vpc_id

    @property
    def test_vpc_id(self):
        """Gets the test_vpc_id of this ShowProtectionGroupParams.

        容灾演练虚拟私有云ID。（该参数暂未使用）

        :return: The test_vpc_id of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._test_vpc_id

    @test_vpc_id.setter
    def test_vpc_id(self, test_vpc_id):
        """Sets the test_vpc_id of this ShowProtectionGroupParams.

        容灾演练虚拟私有云ID。（该参数暂未使用）

        :param test_vpc_id: The test_vpc_id of this ShowProtectionGroupParams.
        :type test_vpc_id: str
        """
        self._test_vpc_id = test_vpc_id

    @property
    def dr_type(self):
        """Gets the dr_type of this ShowProtectionGroupParams.

        部署模式。默认值为“migration”，migration表示VPC内迁移。

        :return: The dr_type of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        """Sets the dr_type of this ShowProtectionGroupParams.

        部署模式。默认值为“migration”，migration表示VPC内迁移。

        :param dr_type: The dr_type of this ShowProtectionGroupParams.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def created_at(self):
        """Gets the created_at of this ShowProtectionGroupParams.

        创建时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :return: The created_at of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowProtectionGroupParams.

        创建时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :param created_at: The created_at of this ShowProtectionGroupParams.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowProtectionGroupParams.

        更新时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :return: The updated_at of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowProtectionGroupParams.

        更新时间。默认格式为：\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\"，例：\"2019-04-01T12:00:00.000Z\"。

        :param updated_at: The updated_at of this ShowProtectionGroupParams.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def protection_type(self):
        """Gets the protection_type of this ShowProtectionGroupParams.

        保护模式。 replication-pair：表示以复制对为单位进行数据同步。 null：表示将保护组中的所有复制对作为一个整体进行数据同步。  说明:当保护组中的所有复制对作为一个整体进行数据同步时，如果数据同步失败，保护组中的所有复制对都会受到影响。因此，SDRS服务对系统做了优化升级： 对于升级后创建的资源，默认以复制对为单位进行数据同步，返回值为replication-pair； 对于已有资源，仍以一个整体进行数据同步，返回值为null。

        :return: The protection_type of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this ShowProtectionGroupParams.

        保护模式。 replication-pair：表示以复制对为单位进行数据同步。 null：表示将保护组中的所有复制对作为一个整体进行数据同步。  说明:当保护组中的所有复制对作为一个整体进行数据同步时，如果数据同步失败，保护组中的所有复制对都会受到影响。因此，SDRS服务对系统做了优化升级： 对于升级后创建的资源，默认以复制对为单位进行数据同步，返回值为replication-pair； 对于已有资源，仍以一个整体进行数据同步，返回值为null。

        :param protection_type: The protection_type of this ShowProtectionGroupParams.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def replication_model(self):
        """Gets the replication_model of this ShowProtectionGroupParams.

        复制类型。 说明:预留参数，暂未启用。

        :return: The replication_model of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._replication_model

    @replication_model.setter
    def replication_model(self, replication_model):
        """Sets the replication_model of this ShowProtectionGroupParams.

        复制类型。 说明:预留参数，暂未启用。

        :param replication_model: The replication_model of this ShowProtectionGroupParams.
        :type replication_model: str
        """
        self._replication_model = replication_model

    @property
    def server_type(self):
        """Gets the server_type of this ShowProtectionGroupParams.

        管理的服务器类型 ECS：表示管理的服务器类型为云服务器。

        :return: The server_type of this ShowProtectionGroupParams.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this ShowProtectionGroupParams.

        管理的服务器类型 ECS：表示管理的服务器类型为云服务器。

        :param server_type: The server_type of this ShowProtectionGroupParams.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, ShowProtectionGroupParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
