# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotDetailV5:

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
        'created_at': 'str',
        'updated_at': 'str',
        'volume_id': 'str',
        'size': 'int',
        'status': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'encrypted': 'bool',
        'cmk_id': 'str',
        'category': 'str',
        'availability_zone': 'str',
        'tags': 'dict(str, str)',
        'instant_access': 'bool',
        'retention_at': 'str',
        'instant_access_retention_at': 'str',
        'incremental': 'bool',
        'snapshot_type': 'str',
        'progress': 'str',
        'encrypt_algorithm': 'str',
        'snapshot_chains': 'list[SnapshotChains]',
        'snapshot_group_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'volume_id': 'volume_id',
        'size': 'size',
        'status': 'status',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'encrypted': 'encrypted',
        'cmk_id': 'cmk_id',
        'category': 'category',
        'availability_zone': 'availability_zone',
        'tags': 'tags',
        'instant_access': 'instant_access',
        'retention_at': 'retention_at',
        'instant_access_retention_at': 'instant_access_retention_at',
        'incremental': 'incremental',
        'snapshot_type': 'snapshot_type',
        'progress': 'progress',
        'encrypt_algorithm': 'encrypt_algorithm',
        'snapshot_chains': 'snapshot_chains',
        'snapshot_group_id': 'snapshot_group_id'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, volume_id=None, size=None, status=None, project_id=None, enterprise_project_id=None, encrypted=None, cmk_id=None, category=None, availability_zone=None, tags=None, instant_access=None, retention_at=None, instant_access_retention_at=None, incremental=None, snapshot_type=None, progress=None, encrypt_algorithm=None, snapshot_chains=None, snapshot_group_id=None):
        r"""SnapshotDetailV5

        The model defined in huaweicloud sdk

        :param id: **参数解释** 云硬盘快照ID。 **取值范围** 不涉及。
        :type id: str
        :param name: **参数解释** 云硬盘快照名称。 名称以autobk_snapshot_为前缀的快照是创建云硬盘备份时系统自动创建的，请不要进行“删除云硬盘快照”和“回滚快照到云硬盘”操作。 **取值范围** 不涉及。
        :type name: str
        :param description: **参数解释** 云硬盘快照描述信息。 **取值范围** 不涉及。
        :type description: str
        :param created_at: **参数解释** 云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX **取值范围** 不涉及。
        :type created_at: str
        :param updated_at: **参数解释** 云硬盘快照更新时间。 **取值范围** 不涉及。
        :type updated_at: str
        :param volume_id: **参数解释** 快照所属的云硬盘ID。 **取值范围** 不涉及。
        :type volume_id: str
        :param size: **参数解释** 云硬盘快照大小，单位为GiB。 **取值范围** 不涉及。
        :type size: int
        :param status: **参数解释** 云硬盘快照的状态。 **取值范围** 具体请参见[云硬盘快照状态](evs_04_0041.xml)。
        :type status: str
        :param project_id: **参数解释** 项目ID。 **取值范围** 不涉及。
        :type project_id: str
        :param enterprise_project_id: **参数解释** 快照所属的企业项目ID。 **取值范围** 不涉及。
        :type enterprise_project_id: str
        :param encrypted: **参数解释** 是否为加密快照。 **取值范围** 不涉及。
        :type encrypted: bool
        :param cmk_id: **参数解释** 快照所属的云硬盘ID的密钥ID。 **取值范围** 不涉及。
        :type cmk_id: str
        :param category: **参数解释** 快照类型。 **取值范围** 枚举值：standard/flash。
        :type category: str
        :param availability_zone: **参数解释** 快照所属AZ。 **取值范围** 不涉及。
        :type availability_zone: str
        :param tags: **参数解释** 快照所属标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。
        :type tags: dict(str, str)
        :param instant_access: **参数解释** 是否开启了快照极速可用功能。 **取值范围** true：开启。仅SSD系列云盘支持开启该功能。 false：关闭。即快照为未开启快照极速可用功能的存量快照。
        :type instant_access: bool
        :param retention_at: **参数解释** 快照保留的时间。 **取值范围** 不涉及。
        :type retention_at: str
        :param instant_access_retention_at: **参数解释** 设置快照极速可用功能的保留时间，保留时间到期后自动关闭快照极速可用功能。 **取值范围** 默认与参数retention_at的值一致。
        :type instant_access_retention_at: str
        :param incremental: **参数解释** 是否增量快照。 **取值范围** true，false。
        :type incremental: bool
        :param snapshot_type: **参数解释** 快照创建来源。 **取值范围** auto：自动创建快照。 user：手动创建快照。 copy：复制快照。
        :type snapshot_type: str
        :param progress: **参数解释** 快照创建进度，单位为百分比。 **取值范围** 不涉及。
        :type progress: str
        :param encrypt_algorithm: **参数解释** 加密快照的加密算法。 **取值范围** 不涉及。
        :type encrypt_algorithm: str
        :param snapshot_chains: **参数解释** 快照所属的快照链信息。 **取值范围** 不涉及。
        :type snapshot_chains: list[:class:`huaweicloudsdkevs.v2.SnapshotChains`]
        :param snapshot_group_id: **参数解释** 快照所属的一致性快照组id。 **取值范围** 不涉及。
        :type snapshot_group_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._volume_id = None
        self._size = None
        self._status = None
        self._project_id = None
        self._enterprise_project_id = None
        self._encrypted = None
        self._cmk_id = None
        self._category = None
        self._availability_zone = None
        self._tags = None
        self._instant_access = None
        self._retention_at = None
        self._instant_access_retention_at = None
        self._incremental = None
        self._snapshot_type = None
        self._progress = None
        self._encrypt_algorithm = None
        self._snapshot_chains = None
        self._snapshot_group_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.volume_id = volume_id
        self.size = size
        self.status = status
        self.project_id = project_id
        self.enterprise_project_id = enterprise_project_id
        self.encrypted = encrypted
        self.cmk_id = cmk_id
        self.category = category
        self.availability_zone = availability_zone
        self.tags = tags
        self.instant_access = instant_access
        self.retention_at = retention_at
        self.instant_access_retention_at = instant_access_retention_at
        self.incremental = incremental
        self.snapshot_type = snapshot_type
        self.progress = progress
        self.encrypt_algorithm = encrypt_algorithm
        self.snapshot_chains = snapshot_chains
        if snapshot_group_id is not None:
            self.snapshot_group_id = snapshot_group_id

    @property
    def id(self):
        r"""Gets the id of this SnapshotDetailV5.

        **参数解释** 云硬盘快照ID。 **取值范围** 不涉及。

        :return: The id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SnapshotDetailV5.

        **参数解释** 云硬盘快照ID。 **取值范围** 不涉及。

        :param id: The id of this SnapshotDetailV5.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SnapshotDetailV5.

        **参数解释** 云硬盘快照名称。 名称以autobk_snapshot_为前缀的快照是创建云硬盘备份时系统自动创建的，请不要进行“删除云硬盘快照”和“回滚快照到云硬盘”操作。 **取值范围** 不涉及。

        :return: The name of this SnapshotDetailV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SnapshotDetailV5.

        **参数解释** 云硬盘快照名称。 名称以autobk_snapshot_为前缀的快照是创建云硬盘备份时系统自动创建的，请不要进行“删除云硬盘快照”和“回滚快照到云硬盘”操作。 **取值范围** 不涉及。

        :param name: The name of this SnapshotDetailV5.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SnapshotDetailV5.

        **参数解释** 云硬盘快照描述信息。 **取值范围** 不涉及。

        :return: The description of this SnapshotDetailV5.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SnapshotDetailV5.

        **参数解释** 云硬盘快照描述信息。 **取值范围** 不涉及。

        :param description: The description of this SnapshotDetailV5.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this SnapshotDetailV5.

        **参数解释** 云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX **取值范围** 不涉及。

        :return: The created_at of this SnapshotDetailV5.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SnapshotDetailV5.

        **参数解释** 云硬盘快照创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX **取值范围** 不涉及。

        :param created_at: The created_at of this SnapshotDetailV5.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SnapshotDetailV5.

        **参数解释** 云硬盘快照更新时间。 **取值范围** 不涉及。

        :return: The updated_at of this SnapshotDetailV5.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SnapshotDetailV5.

        **参数解释** 云硬盘快照更新时间。 **取值范围** 不涉及。

        :param updated_at: The updated_at of this SnapshotDetailV5.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def volume_id(self):
        r"""Gets the volume_id of this SnapshotDetailV5.

        **参数解释** 快照所属的云硬盘ID。 **取值范围** 不涉及。

        :return: The volume_id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this SnapshotDetailV5.

        **参数解释** 快照所属的云硬盘ID。 **取值范围** 不涉及。

        :param volume_id: The volume_id of this SnapshotDetailV5.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def size(self):
        r"""Gets the size of this SnapshotDetailV5.

        **参数解释** 云硬盘快照大小，单位为GiB。 **取值范围** 不涉及。

        :return: The size of this SnapshotDetailV5.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SnapshotDetailV5.

        **参数解释** 云硬盘快照大小，单位为GiB。 **取值范围** 不涉及。

        :param size: The size of this SnapshotDetailV5.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this SnapshotDetailV5.

        **参数解释** 云硬盘快照的状态。 **取值范围** 具体请参见[云硬盘快照状态](evs_04_0041.xml)。

        :return: The status of this SnapshotDetailV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SnapshotDetailV5.

        **参数解释** 云硬盘快照的状态。 **取值范围** 具体请参见[云硬盘快照状态](evs_04_0041.xml)。

        :param status: The status of this SnapshotDetailV5.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this SnapshotDetailV5.

        **参数解释** 项目ID。 **取值范围** 不涉及。

        :return: The project_id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SnapshotDetailV5.

        **参数解释** 项目ID。 **取值范围** 不涉及。

        :param project_id: The project_id of this SnapshotDetailV5.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SnapshotDetailV5.

        **参数解释** 快照所属的企业项目ID。 **取值范围** 不涉及。

        :return: The enterprise_project_id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SnapshotDetailV5.

        **参数解释** 快照所属的企业项目ID。 **取值范围** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this SnapshotDetailV5.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def encrypted(self):
        r"""Gets the encrypted of this SnapshotDetailV5.

        **参数解释** 是否为加密快照。 **取值范围** 不涉及。

        :return: The encrypted of this SnapshotDetailV5.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        r"""Sets the encrypted of this SnapshotDetailV5.

        **参数解释** 是否为加密快照。 **取值范围** 不涉及。

        :param encrypted: The encrypted of this SnapshotDetailV5.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def cmk_id(self):
        r"""Gets the cmk_id of this SnapshotDetailV5.

        **参数解释** 快照所属的云硬盘ID的密钥ID。 **取值范围** 不涉及。

        :return: The cmk_id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        r"""Sets the cmk_id of this SnapshotDetailV5.

        **参数解释** 快照所属的云硬盘ID的密钥ID。 **取值范围** 不涉及。

        :param cmk_id: The cmk_id of this SnapshotDetailV5.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def category(self):
        r"""Gets the category of this SnapshotDetailV5.

        **参数解释** 快照类型。 **取值范围** 枚举值：standard/flash。

        :return: The category of this SnapshotDetailV5.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SnapshotDetailV5.

        **参数解释** 快照类型。 **取值范围** 枚举值：standard/flash。

        :param category: The category of this SnapshotDetailV5.
        :type category: str
        """
        self._category = category

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this SnapshotDetailV5.

        **参数解释** 快照所属AZ。 **取值范围** 不涉及。

        :return: The availability_zone of this SnapshotDetailV5.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this SnapshotDetailV5.

        **参数解释** 快照所属AZ。 **取值范围** 不涉及。

        :param availability_zone: The availability_zone of this SnapshotDetailV5.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def tags(self):
        r"""Gets the tags of this SnapshotDetailV5.

        **参数解释** 快照所属标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。

        :return: The tags of this SnapshotDetailV5.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SnapshotDetailV5.

        **参数解释** 快照所属标签。 标签的key：String类型，最大长度36个字符。 由英文字母、数字、下划线、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。

        :param tags: The tags of this SnapshotDetailV5.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def instant_access(self):
        r"""Gets the instant_access of this SnapshotDetailV5.

        **参数解释** 是否开启了快照极速可用功能。 **取值范围** true：开启。仅SSD系列云盘支持开启该功能。 false：关闭。即快照为未开启快照极速可用功能的存量快照。

        :return: The instant_access of this SnapshotDetailV5.
        :rtype: bool
        """
        return self._instant_access

    @instant_access.setter
    def instant_access(self, instant_access):
        r"""Sets the instant_access of this SnapshotDetailV5.

        **参数解释** 是否开启了快照极速可用功能。 **取值范围** true：开启。仅SSD系列云盘支持开启该功能。 false：关闭。即快照为未开启快照极速可用功能的存量快照。

        :param instant_access: The instant_access of this SnapshotDetailV5.
        :type instant_access: bool
        """
        self._instant_access = instant_access

    @property
    def retention_at(self):
        r"""Gets the retention_at of this SnapshotDetailV5.

        **参数解释** 快照保留的时间。 **取值范围** 不涉及。

        :return: The retention_at of this SnapshotDetailV5.
        :rtype: str
        """
        return self._retention_at

    @retention_at.setter
    def retention_at(self, retention_at):
        r"""Sets the retention_at of this SnapshotDetailV5.

        **参数解释** 快照保留的时间。 **取值范围** 不涉及。

        :param retention_at: The retention_at of this SnapshotDetailV5.
        :type retention_at: str
        """
        self._retention_at = retention_at

    @property
    def instant_access_retention_at(self):
        r"""Gets the instant_access_retention_at of this SnapshotDetailV5.

        **参数解释** 设置快照极速可用功能的保留时间，保留时间到期后自动关闭快照极速可用功能。 **取值范围** 默认与参数retention_at的值一致。

        :return: The instant_access_retention_at of this SnapshotDetailV5.
        :rtype: str
        """
        return self._instant_access_retention_at

    @instant_access_retention_at.setter
    def instant_access_retention_at(self, instant_access_retention_at):
        r"""Sets the instant_access_retention_at of this SnapshotDetailV5.

        **参数解释** 设置快照极速可用功能的保留时间，保留时间到期后自动关闭快照极速可用功能。 **取值范围** 默认与参数retention_at的值一致。

        :param instant_access_retention_at: The instant_access_retention_at of this SnapshotDetailV5.
        :type instant_access_retention_at: str
        """
        self._instant_access_retention_at = instant_access_retention_at

    @property
    def incremental(self):
        r"""Gets the incremental of this SnapshotDetailV5.

        **参数解释** 是否增量快照。 **取值范围** true，false。

        :return: The incremental of this SnapshotDetailV5.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        r"""Sets the incremental of this SnapshotDetailV5.

        **参数解释** 是否增量快照。 **取值范围** true，false。

        :param incremental: The incremental of this SnapshotDetailV5.
        :type incremental: bool
        """
        self._incremental = incremental

    @property
    def snapshot_type(self):
        r"""Gets the snapshot_type of this SnapshotDetailV5.

        **参数解释** 快照创建来源。 **取值范围** auto：自动创建快照。 user：手动创建快照。 copy：复制快照。

        :return: The snapshot_type of this SnapshotDetailV5.
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        r"""Sets the snapshot_type of this SnapshotDetailV5.

        **参数解释** 快照创建来源。 **取值范围** auto：自动创建快照。 user：手动创建快照。 copy：复制快照。

        :param snapshot_type: The snapshot_type of this SnapshotDetailV5.
        :type snapshot_type: str
        """
        self._snapshot_type = snapshot_type

    @property
    def progress(self):
        r"""Gets the progress of this SnapshotDetailV5.

        **参数解释** 快照创建进度，单位为百分比。 **取值范围** 不涉及。

        :return: The progress of this SnapshotDetailV5.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SnapshotDetailV5.

        **参数解释** 快照创建进度，单位为百分比。 **取值范围** 不涉及。

        :param progress: The progress of this SnapshotDetailV5.
        :type progress: str
        """
        self._progress = progress

    @property
    def encrypt_algorithm(self):
        r"""Gets the encrypt_algorithm of this SnapshotDetailV5.

        **参数解释** 加密快照的加密算法。 **取值范围** 不涉及。

        :return: The encrypt_algorithm of this SnapshotDetailV5.
        :rtype: str
        """
        return self._encrypt_algorithm

    @encrypt_algorithm.setter
    def encrypt_algorithm(self, encrypt_algorithm):
        r"""Sets the encrypt_algorithm of this SnapshotDetailV5.

        **参数解释** 加密快照的加密算法。 **取值范围** 不涉及。

        :param encrypt_algorithm: The encrypt_algorithm of this SnapshotDetailV5.
        :type encrypt_algorithm: str
        """
        self._encrypt_algorithm = encrypt_algorithm

    @property
    def snapshot_chains(self):
        r"""Gets the snapshot_chains of this SnapshotDetailV5.

        **参数解释** 快照所属的快照链信息。 **取值范围** 不涉及。

        :return: The snapshot_chains of this SnapshotDetailV5.
        :rtype: list[:class:`huaweicloudsdkevs.v2.SnapshotChains`]
        """
        return self._snapshot_chains

    @snapshot_chains.setter
    def snapshot_chains(self, snapshot_chains):
        r"""Sets the snapshot_chains of this SnapshotDetailV5.

        **参数解释** 快照所属的快照链信息。 **取值范围** 不涉及。

        :param snapshot_chains: The snapshot_chains of this SnapshotDetailV5.
        :type snapshot_chains: list[:class:`huaweicloudsdkevs.v2.SnapshotChains`]
        """
        self._snapshot_chains = snapshot_chains

    @property
    def snapshot_group_id(self):
        r"""Gets the snapshot_group_id of this SnapshotDetailV5.

        **参数解释** 快照所属的一致性快照组id。 **取值范围** 不涉及。

        :return: The snapshot_group_id of this SnapshotDetailV5.
        :rtype: str
        """
        return self._snapshot_group_id

    @snapshot_group_id.setter
    def snapshot_group_id(self, snapshot_group_id):
        r"""Sets the snapshot_group_id of this SnapshotDetailV5.

        **参数解释** 快照所属的一致性快照组id。 **取值范围** 不涉及。

        :param snapshot_group_id: The snapshot_group_id of this SnapshotDetailV5.
        :type snapshot_group_id: str
        """
        self._snapshot_group_id = snapshot_group_id

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
        if not isinstance(other, SnapshotDetailV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
