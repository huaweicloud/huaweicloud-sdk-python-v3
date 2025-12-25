# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupForList:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'datastore': 'BackupDatabase',
        'type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'size': 'int',
        'description': 'str',
        'instance_status': 'str',
        'instance_mode': 'str',
        'is_instance_restoring': 'bool',
        'backup_method': 'str',
        'kms_enable': 'bool',
        'deletable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'datastore': 'datastore',
        'type': 'type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'size': 'size',
        'description': 'description',
        'instance_status': 'instance_status',
        'instance_mode': 'instance_mode',
        'is_instance_restoring': 'is_instance_restoring',
        'backup_method': 'backup_method',
        'kms_enable': 'kms_enable',
        'deletable': 'deletable'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, datastore=None, type=None, begin_time=None, end_time=None, status=None, size=None, description=None, instance_status=None, instance_mode=None, is_instance_restoring=None, backup_method=None, kms_enable=None, deletable=None):
        r"""BackupForList

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 备份ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 备份名称。 **取值范围：** 不涉及。
        :type name: str
        :param instance_id: **参数解释：** 备份所属的实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。
        :type instance_id: str
        :param instance_name: **参数解释：** 备份所属的实例名称。 **取值范围：** 不涉及。
        :type instance_name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        :param type: **参数解释：** 备份类型。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。
        :type type: str
        :param begin_time: **参数解释：** 备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。
        :type begin_time: str
        :param end_time: **参数解释：** 备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。
        :type end_time: str
        :param status: **参数解释：** 备份状态。 **取值范围：** - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。
        :type status: str
        :param size: **参数解释：** 备份大小，单位：KB。 **取值范围：** 不涉及。
        :type size: int
        :param description: **参数解释：** 备份描述。 **取值范围：** 不涉及。
        :type description: str
        :param instance_status: **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示存储空间满。 - enlargefail，表示实例扩容节点个数失败。
        :type instance_status: str
        :param instance_mode: **参数解释：** 实例模式。 **取值范围：** - Sharding - ReplicaSet - Single
        :type instance_mode: str
        :param is_instance_restoring: **参数解释：** 当前实例是否处于恢复中或者恢复检查中。 **取值范围：** - true，表示实例处于恢复中或者恢复检查中，不允许删除该实例备份。 - false，当前实例未处于恢复中或者恢复检查中，允许删除该实例备份。
        :type is_instance_restoring: bool
        :param backup_method: **参数解释：** 备份方式。 **取值范围：** - Snapshot，快照备份。 - Physical，物理备份。 - Logical，逻辑备份。 - Incremental，增量备份。
        :type backup_method: str
        :param kms_enable: **参数解释：** 是否开启kms加密。 **取值范围：** - true，已开启kms加密。 - false，未开启kms加密。
        :type kms_enable: bool
        :param deletable: **参数解释：** 是否支持删除该备份。当全备策略存在时，不允许删除自动备份。手动备份允许删除。 **取值范围：** - true，允许删除该备份。 - false，不允许删除该备份。
        :type deletable: bool
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._datastore = None
        self._type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._size = None
        self._description = None
        self._instance_status = None
        self._instance_mode = None
        self._is_instance_restoring = None
        self._backup_method = None
        self._kms_enable = None
        self._deletable = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.datastore = datastore
        self.type = type
        self.begin_time = begin_time
        self.end_time = end_time
        self.status = status
        self.size = size
        self.description = description
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if is_instance_restoring is not None:
            self.is_instance_restoring = is_instance_restoring
        if backup_method is not None:
            self.backup_method = backup_method
        if kms_enable is not None:
            self.kms_enable = kms_enable
        if deletable is not None:
            self.deletable = deletable

    @property
    def id(self):
        r"""Gets the id of this BackupForList.

        **参数解释：** 备份ID。 **取值范围：** 不涉及。

        :return: The id of this BackupForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupForList.

        **参数解释：** 备份ID。 **取值范围：** 不涉及。

        :param id: The id of this BackupForList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupForList.

        **参数解释：** 备份名称。 **取值范围：** 不涉及。

        :return: The name of this BackupForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupForList.

        **参数解释：** 备份名称。 **取值范围：** 不涉及。

        :param name: The name of this BackupForList.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BackupForList.

        **参数解释：** 备份所属的实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。

        :return: The instance_id of this BackupForList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BackupForList.

        **参数解释：** 备份所属的实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 **取值范围：** 不涉及。

        :param instance_id: The instance_id of this BackupForList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BackupForList.

        **参数解释：** 备份所属的实例名称。 **取值范围：** 不涉及。

        :return: The instance_name of this BackupForList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BackupForList.

        **参数解释：** 备份所属的实例名称。 **取值范围：** 不涉及。

        :param instance_name: The instance_name of this BackupForList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def datastore(self):
        r"""Gets the datastore of this BackupForList.

        :return: The datastore of this BackupForList.
        :rtype: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this BackupForList.

        :param datastore: The datastore of this BackupForList.
        :type datastore: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        """
        self._datastore = datastore

    @property
    def type(self):
        r"""Gets the type of this BackupForList.

        **参数解释：** 备份类型。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。

        :return: The type of this BackupForList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BackupForList.

        **参数解释：** 备份类型。 **取值范围：** - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。

        :param type: The type of this BackupForList.
        :type type: str
        """
        self._type = type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BackupForList.

        **参数解释：** 备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。

        :return: The begin_time of this BackupForList.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BackupForList.

        **参数解释：** 备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。

        :param begin_time: The begin_time of this BackupForList.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BackupForList.

        **参数解释：** 备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。

        :return: The end_time of this BackupForList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BackupForList.

        **参数解释：** 备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。 **取值范围：** 不涉及。

        :param end_time: The end_time of this BackupForList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this BackupForList.

        **参数解释：** 备份状态。 **取值范围：** - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :return: The status of this BackupForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupForList.

        **参数解释：** 备份状态。 **取值范围：** - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :param status: The status of this BackupForList.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        r"""Gets the size of this BackupForList.

        **参数解释：** 备份大小，单位：KB。 **取值范围：** 不涉及。

        :return: The size of this BackupForList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackupForList.

        **参数解释：** 备份大小，单位：KB。 **取值范围：** 不涉及。

        :param size: The size of this BackupForList.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this BackupForList.

        **参数解释：** 备份描述。 **取值范围：** 不涉及。

        :return: The description of this BackupForList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackupForList.

        **参数解释：** 备份描述。 **取值范围：** 不涉及。

        :param description: The description of this BackupForList.
        :type description: str
        """
        self._description = description

    @property
    def instance_status(self):
        r"""Gets the instance_status of this BackupForList.

        **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示存储空间满。 - enlargefail，表示实例扩容节点个数失败。

        :return: The instance_status of this BackupForList.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this BackupForList.

        **参数解释：** 实例状态。 **取值范围：** - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示存储空间满。 - enlargefail，表示实例扩容节点个数失败。

        :param instance_status: The instance_status of this BackupForList.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this BackupForList.

        **参数解释：** 实例模式。 **取值范围：** - Sharding - ReplicaSet - Single

        :return: The instance_mode of this BackupForList.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this BackupForList.

        **参数解释：** 实例模式。 **取值范围：** - Sharding - ReplicaSet - Single

        :param instance_mode: The instance_mode of this BackupForList.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def is_instance_restoring(self):
        r"""Gets the is_instance_restoring of this BackupForList.

        **参数解释：** 当前实例是否处于恢复中或者恢复检查中。 **取值范围：** - true，表示实例处于恢复中或者恢复检查中，不允许删除该实例备份。 - false，当前实例未处于恢复中或者恢复检查中，允许删除该实例备份。

        :return: The is_instance_restoring of this BackupForList.
        :rtype: bool
        """
        return self._is_instance_restoring

    @is_instance_restoring.setter
    def is_instance_restoring(self, is_instance_restoring):
        r"""Sets the is_instance_restoring of this BackupForList.

        **参数解释：** 当前实例是否处于恢复中或者恢复检查中。 **取值范围：** - true，表示实例处于恢复中或者恢复检查中，不允许删除该实例备份。 - false，当前实例未处于恢复中或者恢复检查中，允许删除该实例备份。

        :param is_instance_restoring: The is_instance_restoring of this BackupForList.
        :type is_instance_restoring: bool
        """
        self._is_instance_restoring = is_instance_restoring

    @property
    def backup_method(self):
        r"""Gets the backup_method of this BackupForList.

        **参数解释：** 备份方式。 **取值范围：** - Snapshot，快照备份。 - Physical，物理备份。 - Logical，逻辑备份。 - Incremental，增量备份。

        :return: The backup_method of this BackupForList.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this BackupForList.

        **参数解释：** 备份方式。 **取值范围：** - Snapshot，快照备份。 - Physical，物理备份。 - Logical，逻辑备份。 - Incremental，增量备份。

        :param backup_method: The backup_method of this BackupForList.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def kms_enable(self):
        r"""Gets the kms_enable of this BackupForList.

        **参数解释：** 是否开启kms加密。 **取值范围：** - true，已开启kms加密。 - false，未开启kms加密。

        :return: The kms_enable of this BackupForList.
        :rtype: bool
        """
        return self._kms_enable

    @kms_enable.setter
    def kms_enable(self, kms_enable):
        r"""Sets the kms_enable of this BackupForList.

        **参数解释：** 是否开启kms加密。 **取值范围：** - true，已开启kms加密。 - false，未开启kms加密。

        :param kms_enable: The kms_enable of this BackupForList.
        :type kms_enable: bool
        """
        self._kms_enable = kms_enable

    @property
    def deletable(self):
        r"""Gets the deletable of this BackupForList.

        **参数解释：** 是否支持删除该备份。当全备策略存在时，不允许删除自动备份。手动备份允许删除。 **取值范围：** - true，允许删除该备份。 - false，不允许删除该备份。

        :return: The deletable of this BackupForList.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this BackupForList.

        **参数解释：** 是否支持删除该备份。当全备策略存在时，不允许删除自动备份。手动备份允许删除。 **取值范围：** - true，允许删除该备份。 - false，不允许删除该备份。

        :param deletable: The deletable of this BackupForList.
        :type deletable: bool
        """
        self._deletable = deletable

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackupForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
