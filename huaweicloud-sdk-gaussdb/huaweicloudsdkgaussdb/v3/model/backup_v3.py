# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupV3:

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
        'description': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'name': 'str',
        'size': 'str',
        'size_unit': 'str',
        'status': 'str',
        'created': 'str',
        'updated': 'str',
        'backup_type': 'str',
        'backup_level': 'str',
        'backup_method': 'str',
        'use_detail': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'name': 'name',
        'size': 'size',
        'size_unit': 'size_unit',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'backup_type': 'backup_type',
        'backup_level': 'backup_level',
        'backup_method': 'backup_method',
        'use_detail': 'use_detail',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, description=None, instance_id=None, instance_name=None, name=None, size=None, size_unit=None, status=None, created=None, updated=None, backup_type=None, backup_level=None, backup_method=None, use_detail=None, time_zone=None):
        r"""BackupV3

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 备份ID。 **取值范围**： 不涉及。
        :type id: str
        :param description: **参数解释**： 备份描述。 **取值范围**： 不涉及。
        :type description: str
        :param instance_id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type instance_name: str
        :param name: **参数解释**： 备份名称。 **取值范围**： 不涉及。
        :type name: str
        :param size: **参数解释**： 备份大小。 **取值范围**： 不涉及。
        :type size: str
        :param size_unit: **参数解释**： 大小单位（KB）。 **取值范围**： 不涉及。
        :type size_unit: str
        :param status: **参数解释**： 备份状态。 **取值范围**： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。
        :type status: str
        :param created: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created: str
        :param updated: **参数解释**： 更新时间。 **取值范围**： 不涉及。
        :type updated: str
        :param backup_type: **参数解释**： 备份类型。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。
        :type backup_type: str
        :param backup_level: **参数解释**： 备份级别。 **取值范围**： - 1：一级备份。 - 2：二级备份。
        :type backup_level: str
        :param backup_method: **参数解释**： 备份方法。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。
        :type backup_method: str
        :param use_detail: **参数解释**： 使用详情。 **取值范围**： 不涉及。
        :type use_detail: str
        :param time_zone: **参数解释**： UTC时区。 **取值范围**： 不涉及。
        :type time_zone: str
        """
        
        

        self._id = None
        self._description = None
        self._instance_id = None
        self._instance_name = None
        self._name = None
        self._size = None
        self._size_unit = None
        self._status = None
        self._created = None
        self._updated = None
        self._backup_type = None
        self._backup_level = None
        self._backup_method = None
        self._use_detail = None
        self._time_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if size_unit is not None:
            self.size_unit = size_unit
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if backup_type is not None:
            self.backup_type = backup_type
        if backup_level is not None:
            self.backup_level = backup_level
        if backup_method is not None:
            self.backup_method = backup_method
        if use_detail is not None:
            self.use_detail = use_detail
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        r"""Gets the id of this BackupV3.

        **参数解释**： 备份ID。 **取值范围**： 不涉及。

        :return: The id of this BackupV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupV3.

        **参数解释**： 备份ID。 **取值范围**： 不涉及。

        :param id: The id of this BackupV3.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this BackupV3.

        **参数解释**： 备份描述。 **取值范围**： 不涉及。

        :return: The description of this BackupV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackupV3.

        **参数解释**： 备份描述。 **取值范围**： 不涉及。

        :param description: The description of this BackupV3.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BackupV3.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this BackupV3.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BackupV3.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this BackupV3.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BackupV3.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The instance_name of this BackupV3.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BackupV3.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param instance_name: The instance_name of this BackupV3.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def name(self):
        r"""Gets the name of this BackupV3.

        **参数解释**： 备份名称。 **取值范围**： 不涉及。

        :return: The name of this BackupV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupV3.

        **参数解释**： 备份名称。 **取值范围**： 不涉及。

        :param name: The name of this BackupV3.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this BackupV3.

        **参数解释**： 备份大小。 **取值范围**： 不涉及。

        :return: The size of this BackupV3.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackupV3.

        **参数解释**： 备份大小。 **取值范围**： 不涉及。

        :param size: The size of this BackupV3.
        :type size: str
        """
        self._size = size

    @property
    def size_unit(self):
        r"""Gets the size_unit of this BackupV3.

        **参数解释**： 大小单位（KB）。 **取值范围**： 不涉及。

        :return: The size_unit of this BackupV3.
        :rtype: str
        """
        return self._size_unit

    @size_unit.setter
    def size_unit(self, size_unit):
        r"""Sets the size_unit of this BackupV3.

        **参数解释**： 大小单位（KB）。 **取值范围**： 不涉及。

        :param size_unit: The size_unit of this BackupV3.
        :type size_unit: str
        """
        self._size_unit = size_unit

    @property
    def status(self):
        r"""Gets the status of this BackupV3.

        **参数解释**： 备份状态。 **取值范围**： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :return: The status of this BackupV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupV3.

        **参数解释**： 备份状态。 **取值范围**： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :param status: The status of this BackupV3.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        r"""Gets the created of this BackupV3.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created of this BackupV3.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this BackupV3.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created: The created of this BackupV3.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this BackupV3.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :return: The updated of this BackupV3.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this BackupV3.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :param updated: The updated of this BackupV3.
        :type updated: str
        """
        self._updated = updated

    @property
    def backup_type(self):
        r"""Gets the backup_type of this BackupV3.

        **参数解释**： 备份类型。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。

        :return: The backup_type of this BackupV3.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this BackupV3.

        **参数解释**： 备份类型。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。

        :param backup_type: The backup_type of this BackupV3.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def backup_level(self):
        r"""Gets the backup_level of this BackupV3.

        **参数解释**： 备份级别。 **取值范围**： - 1：一级备份。 - 2：二级备份。

        :return: The backup_level of this BackupV3.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this BackupV3.

        **参数解释**： 备份级别。 **取值范围**： - 1：一级备份。 - 2：二级备份。

        :param backup_level: The backup_level of this BackupV3.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def backup_method(self):
        r"""Gets the backup_method of this BackupV3.

        **参数解释**： 备份方法。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。

        :return: The backup_method of this BackupV3.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this BackupV3.

        **参数解释**： 备份方法。 **取值范围**： - Db：物理备份。 - Snapshot：快照备份。

        :param backup_method: The backup_method of this BackupV3.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def use_detail(self):
        r"""Gets the use_detail of this BackupV3.

        **参数解释**： 使用详情。 **取值范围**： 不涉及。

        :return: The use_detail of this BackupV3.
        :rtype: str
        """
        return self._use_detail

    @use_detail.setter
    def use_detail(self, use_detail):
        r"""Sets the use_detail of this BackupV3.

        **参数解释**： 使用详情。 **取值范围**： 不涉及。

        :param use_detail: The use_detail of this BackupV3.
        :type use_detail: str
        """
        self._use_detail = use_detail

    @property
    def time_zone(self):
        r"""Gets the time_zone of this BackupV3.

        **参数解释**： UTC时区。 **取值范围**： 不涉及。

        :return: The time_zone of this BackupV3.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this BackupV3.

        **参数解释**： UTC时区。 **取值范围**： 不涉及。

        :param time_zone: The time_zone of this BackupV3.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, BackupV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
