# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_task_id': 'str',
        'src_cloud_type': 'str',
        'src_region': 'str',
        'src_bucket': 'str',
        'create_time': 'int',
        'last_start_time': 'int',
        'dst_bucket': 'str',
        'dst_region': 'str',
        'description': 'str',
        'status': 'str',
        'enable_kms': 'bool',
        'enable_metadata_migration': 'bool',
        'enable_restore': 'bool',
        'object_overwrite_mode': 'str',
        'dst_storage_policy': 'str',
        'app_id': 'str',
        'source_cdn': 'SourceCdnResp',
        'consistency_check': 'str'
    }

    attribute_map = {
        'sync_task_id': 'sync_task_id',
        'src_cloud_type': 'src_cloud_type',
        'src_region': 'src_region',
        'src_bucket': 'src_bucket',
        'create_time': 'create_time',
        'last_start_time': 'last_start_time',
        'dst_bucket': 'dst_bucket',
        'dst_region': 'dst_region',
        'description': 'description',
        'status': 'status',
        'enable_kms': 'enable_kms',
        'enable_metadata_migration': 'enable_metadata_migration',
        'enable_restore': 'enable_restore',
        'object_overwrite_mode': 'object_overwrite_mode',
        'dst_storage_policy': 'dst_storage_policy',
        'app_id': 'app_id',
        'source_cdn': 'source_cdn',
        'consistency_check': 'consistency_check'
    }

    def __init__(self, sync_task_id=None, src_cloud_type=None, src_region=None, src_bucket=None, create_time=None, last_start_time=None, dst_bucket=None, dst_region=None, description=None, status=None, enable_kms=None, enable_metadata_migration=None, enable_restore=None, object_overwrite_mode=None, dst_storage_policy=None, app_id=None, source_cdn=None, consistency_check=None):
        r"""SyncTaskInfo

        The model defined in huaweicloud sdk

        :param sync_task_id: 同步任务ID
        :type sync_task_id: str
        :param src_cloud_type: 源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、UCloud、Google。默认值为Aliyun。
        :type src_cloud_type: str
        :param src_region: 源端桶所处的区域
        :type src_region: str
        :param src_bucket: 源端桶
        :type src_bucket: str
        :param create_time: 同步任务创建时间（Unix时间戳，毫秒）
        :type create_time: int
        :param last_start_time: 最近启动同步任务时间（Unix时间戳，毫秒）
        :type last_start_time: int
        :param dst_bucket: 目的端桶。
        :type dst_bucket: str
        :param dst_region: 目的端region
        :type dst_region: str
        :param description: 任务描述，不能超过255个字符，且不能包含&lt;&gt;()\&quot;&#39;&amp;等特殊字符。
        :type description: str
        :param status: 同步任务状态 SYNCHRONIZING：同步中 STOPPED：已停止
        :type status: str
        :param enable_kms: 是否开启KMS加密，默认不开启。
        :type enable_kms: bool
        :param enable_metadata_migration: 是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。
        :type enable_metadata_migration: bool
        :param enable_restore: 是否自动解冻归档数据，默认否。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移。
        :type enable_restore: bool
        :param object_overwrite_mode: 迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。
        :type object_overwrite_mode: str
        :param dst_storage_policy: 目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型
        :type dst_storage_policy: str
        :param app_id: 当源端为腾讯云时，需要填写此参数。
        :type app_id: str
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        :param consistency_check: 迁移后对象一致性校验方式，用于迁移后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移后，通过对比源端和目的端对象大小和最后修改时间，判断对象迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。
        :type consistency_check: str
        """
        
        

        self._sync_task_id = None
        self._src_cloud_type = None
        self._src_region = None
        self._src_bucket = None
        self._create_time = None
        self._last_start_time = None
        self._dst_bucket = None
        self._dst_region = None
        self._description = None
        self._status = None
        self._enable_kms = None
        self._enable_metadata_migration = None
        self._enable_restore = None
        self._object_overwrite_mode = None
        self._dst_storage_policy = None
        self._app_id = None
        self._source_cdn = None
        self._consistency_check = None
        self.discriminator = None

        if sync_task_id is not None:
            self.sync_task_id = sync_task_id
        if src_cloud_type is not None:
            self.src_cloud_type = src_cloud_type
        if src_region is not None:
            self.src_region = src_region
        if src_bucket is not None:
            self.src_bucket = src_bucket
        if create_time is not None:
            self.create_time = create_time
        if last_start_time is not None:
            self.last_start_time = last_start_time
        if dst_bucket is not None:
            self.dst_bucket = dst_bucket
        if dst_region is not None:
            self.dst_region = dst_region
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if enable_metadata_migration is not None:
            self.enable_metadata_migration = enable_metadata_migration
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if object_overwrite_mode is not None:
            self.object_overwrite_mode = object_overwrite_mode
        if dst_storage_policy is not None:
            self.dst_storage_policy = dst_storage_policy
        if app_id is not None:
            self.app_id = app_id
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if consistency_check is not None:
            self.consistency_check = consistency_check

    @property
    def sync_task_id(self):
        r"""Gets the sync_task_id of this SyncTaskInfo.

        同步任务ID

        :return: The sync_task_id of this SyncTaskInfo.
        :rtype: str
        """
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, sync_task_id):
        r"""Sets the sync_task_id of this SyncTaskInfo.

        同步任务ID

        :param sync_task_id: The sync_task_id of this SyncTaskInfo.
        :type sync_task_id: str
        """
        self._sync_task_id = sync_task_id

    @property
    def src_cloud_type(self):
        r"""Gets the src_cloud_type of this SyncTaskInfo.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、UCloud、Google。默认值为Aliyun。

        :return: The src_cloud_type of this SyncTaskInfo.
        :rtype: str
        """
        return self._src_cloud_type

    @src_cloud_type.setter
    def src_cloud_type(self, src_cloud_type):
        r"""Sets the src_cloud_type of this SyncTaskInfo.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、UCloud、Google。默认值为Aliyun。

        :param src_cloud_type: The src_cloud_type of this SyncTaskInfo.
        :type src_cloud_type: str
        """
        self._src_cloud_type = src_cloud_type

    @property
    def src_region(self):
        r"""Gets the src_region of this SyncTaskInfo.

        源端桶所处的区域

        :return: The src_region of this SyncTaskInfo.
        :rtype: str
        """
        return self._src_region

    @src_region.setter
    def src_region(self, src_region):
        r"""Sets the src_region of this SyncTaskInfo.

        源端桶所处的区域

        :param src_region: The src_region of this SyncTaskInfo.
        :type src_region: str
        """
        self._src_region = src_region

    @property
    def src_bucket(self):
        r"""Gets the src_bucket of this SyncTaskInfo.

        源端桶

        :return: The src_bucket of this SyncTaskInfo.
        :rtype: str
        """
        return self._src_bucket

    @src_bucket.setter
    def src_bucket(self, src_bucket):
        r"""Sets the src_bucket of this SyncTaskInfo.

        源端桶

        :param src_bucket: The src_bucket of this SyncTaskInfo.
        :type src_bucket: str
        """
        self._src_bucket = src_bucket

    @property
    def create_time(self):
        r"""Gets the create_time of this SyncTaskInfo.

        同步任务创建时间（Unix时间戳，毫秒）

        :return: The create_time of this SyncTaskInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SyncTaskInfo.

        同步任务创建时间（Unix时间戳，毫秒）

        :param create_time: The create_time of this SyncTaskInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_start_time(self):
        r"""Gets the last_start_time of this SyncTaskInfo.

        最近启动同步任务时间（Unix时间戳，毫秒）

        :return: The last_start_time of this SyncTaskInfo.
        :rtype: int
        """
        return self._last_start_time

    @last_start_time.setter
    def last_start_time(self, last_start_time):
        r"""Sets the last_start_time of this SyncTaskInfo.

        最近启动同步任务时间（Unix时间戳，毫秒）

        :param last_start_time: The last_start_time of this SyncTaskInfo.
        :type last_start_time: int
        """
        self._last_start_time = last_start_time

    @property
    def dst_bucket(self):
        r"""Gets the dst_bucket of this SyncTaskInfo.

        目的端桶。

        :return: The dst_bucket of this SyncTaskInfo.
        :rtype: str
        """
        return self._dst_bucket

    @dst_bucket.setter
    def dst_bucket(self, dst_bucket):
        r"""Sets the dst_bucket of this SyncTaskInfo.

        目的端桶。

        :param dst_bucket: The dst_bucket of this SyncTaskInfo.
        :type dst_bucket: str
        """
        self._dst_bucket = dst_bucket

    @property
    def dst_region(self):
        r"""Gets the dst_region of this SyncTaskInfo.

        目的端region

        :return: The dst_region of this SyncTaskInfo.
        :rtype: str
        """
        return self._dst_region

    @dst_region.setter
    def dst_region(self, dst_region):
        r"""Sets the dst_region of this SyncTaskInfo.

        目的端region

        :param dst_region: The dst_region of this SyncTaskInfo.
        :type dst_region: str
        """
        self._dst_region = dst_region

    @property
    def description(self):
        r"""Gets the description of this SyncTaskInfo.

        任务描述，不能超过255个字符，且不能包含<>()\"'&等特殊字符。

        :return: The description of this SyncTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SyncTaskInfo.

        任务描述，不能超过255个字符，且不能包含<>()\"'&等特殊字符。

        :param description: The description of this SyncTaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this SyncTaskInfo.

        同步任务状态 SYNCHRONIZING：同步中 STOPPED：已停止

        :return: The status of this SyncTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SyncTaskInfo.

        同步任务状态 SYNCHRONIZING：同步中 STOPPED：已停止

        :param status: The status of this SyncTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def enable_kms(self):
        r"""Gets the enable_kms of this SyncTaskInfo.

        是否开启KMS加密，默认不开启。

        :return: The enable_kms of this SyncTaskInfo.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        r"""Sets the enable_kms of this SyncTaskInfo.

        是否开启KMS加密，默认不开启。

        :param enable_kms: The enable_kms of this SyncTaskInfo.
        :type enable_kms: bool
        """
        self._enable_kms = enable_kms

    @property
    def enable_metadata_migration(self):
        r"""Gets the enable_metadata_migration of this SyncTaskInfo.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :return: The enable_metadata_migration of this SyncTaskInfo.
        :rtype: bool
        """
        return self._enable_metadata_migration

    @enable_metadata_migration.setter
    def enable_metadata_migration(self, enable_metadata_migration):
        r"""Sets the enable_metadata_migration of this SyncTaskInfo.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :param enable_metadata_migration: The enable_metadata_migration of this SyncTaskInfo.
        :type enable_metadata_migration: bool
        """
        self._enable_metadata_migration = enable_metadata_migration

    @property
    def enable_restore(self):
        r"""Gets the enable_restore of this SyncTaskInfo.

        是否自动解冻归档数据，默认否。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :return: The enable_restore of this SyncTaskInfo.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        r"""Sets the enable_restore of this SyncTaskInfo.

        是否自动解冻归档数据，默认否。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :param enable_restore: The enable_restore of this SyncTaskInfo.
        :type enable_restore: bool
        """
        self._enable_restore = enable_restore

    @property
    def object_overwrite_mode(self):
        r"""Gets the object_overwrite_mode of this SyncTaskInfo.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :return: The object_overwrite_mode of this SyncTaskInfo.
        :rtype: str
        """
        return self._object_overwrite_mode

    @object_overwrite_mode.setter
    def object_overwrite_mode(self, object_overwrite_mode):
        r"""Sets the object_overwrite_mode of this SyncTaskInfo.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :param object_overwrite_mode: The object_overwrite_mode of this SyncTaskInfo.
        :type object_overwrite_mode: str
        """
        self._object_overwrite_mode = object_overwrite_mode

    @property
    def dst_storage_policy(self):
        r"""Gets the dst_storage_policy of this SyncTaskInfo.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :return: The dst_storage_policy of this SyncTaskInfo.
        :rtype: str
        """
        return self._dst_storage_policy

    @dst_storage_policy.setter
    def dst_storage_policy(self, dst_storage_policy):
        r"""Sets the dst_storage_policy of this SyncTaskInfo.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :param dst_storage_policy: The dst_storage_policy of this SyncTaskInfo.
        :type dst_storage_policy: str
        """
        self._dst_storage_policy = dst_storage_policy

    @property
    def app_id(self):
        r"""Gets the app_id of this SyncTaskInfo.

        当源端为腾讯云时，需要填写此参数。

        :return: The app_id of this SyncTaskInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this SyncTaskInfo.

        当源端为腾讯云时，需要填写此参数。

        :param app_id: The app_id of this SyncTaskInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def source_cdn(self):
        r"""Gets the source_cdn of this SyncTaskInfo.

        :return: The source_cdn of this SyncTaskInfo.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        r"""Sets the source_cdn of this SyncTaskInfo.

        :param source_cdn: The source_cdn of this SyncTaskInfo.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        self._source_cdn = source_cdn

    @property
    def consistency_check(self):
        r"""Gets the consistency_check of this SyncTaskInfo.

        迁移后对象一致性校验方式，用于迁移后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移后，通过对比源端和目的端对象大小和最后修改时间，判断对象迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :return: The consistency_check of this SyncTaskInfo.
        :rtype: str
        """
        return self._consistency_check

    @consistency_check.setter
    def consistency_check(self, consistency_check):
        r"""Sets the consistency_check of this SyncTaskInfo.

        迁移后对象一致性校验方式，用于迁移后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移后，通过对比源端和目的端对象大小和最后修改时间，判断对象迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :param consistency_check: The consistency_check of this SyncTaskInfo.
        :type consistency_check: str
        """
        self._consistency_check = consistency_check

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
        if not isinstance(other, SyncTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
