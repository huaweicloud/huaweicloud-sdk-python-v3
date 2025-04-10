# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'complete_size': 'int',
        'description': 'str',
        'dst_node': 'DstNodeResp',
        'enable_failed_object_recording': 'bool',
        'enable_kms': 'bool',
        'enable_metadata_migration': 'bool',
        'enable_restore': 'bool',
        'error_reason': 'ErrorReasonResp',
        'failed_num': 'int',
        'failed_object_record': 'FailedObjectRecordDto',
        'group_id': 'str',
        'id': 'int',
        'is_query_over': 'bool',
        'left_time': 'int',
        'migrate_since': 'int',
        'migrate_speed': 'int',
        'name': 'str',
        'progress': 'float',
        'real_size': 'int',
        'skipped_num': 'int',
        'src_node': 'SrcNodeResp',
        'start_time': 'int',
        'status': 'int',
        'successful_num': 'int',
        'task_type': 'str',
        'group_type': 'str',
        'total_num': 'int',
        'total_size': 'int',
        'total_time': 'int',
        'smn_info': 'SmnInfo',
        'source_cdn': 'SourceCdnResp',
        'success_record_error_reason': 'str',
        'skip_record_error_reason': 'str',
        'object_overwrite_mode': 'str',
        'dst_storage_policy': 'str',
        'consistency_check': 'str',
        'enable_requester_pays': 'bool',
        'task_priority': 'str'
    }

    attribute_map = {
        'bandwidth_policy': 'bandwidth_policy',
        'complete_size': 'complete_size',
        'description': 'description',
        'dst_node': 'dst_node',
        'enable_failed_object_recording': 'enable_failed_object_recording',
        'enable_kms': 'enable_kms',
        'enable_metadata_migration': 'enable_metadata_migration',
        'enable_restore': 'enable_restore',
        'error_reason': 'error_reason',
        'failed_num': 'failed_num',
        'failed_object_record': 'failed_object_record',
        'group_id': 'group_id',
        'id': 'id',
        'is_query_over': 'is_query_over',
        'left_time': 'left_time',
        'migrate_since': 'migrate_since',
        'migrate_speed': 'migrate_speed',
        'name': 'name',
        'progress': 'progress',
        'real_size': 'real_size',
        'skipped_num': 'skipped_num',
        'src_node': 'src_node',
        'start_time': 'start_time',
        'status': 'status',
        'successful_num': 'successful_num',
        'task_type': 'task_type',
        'group_type': 'group_type',
        'total_num': 'total_num',
        'total_size': 'total_size',
        'total_time': 'total_time',
        'smn_info': 'smn_info',
        'source_cdn': 'source_cdn',
        'success_record_error_reason': 'success_record_error_reason',
        'skip_record_error_reason': 'skip_record_error_reason',
        'object_overwrite_mode': 'object_overwrite_mode',
        'dst_storage_policy': 'dst_storage_policy',
        'consistency_check': 'consistency_check',
        'enable_requester_pays': 'enable_requester_pays',
        'task_priority': 'task_priority'
    }

    def __init__(self, bandwidth_policy=None, complete_size=None, description=None, dst_node=None, enable_failed_object_recording=None, enable_kms=None, enable_metadata_migration=None, enable_restore=None, error_reason=None, failed_num=None, failed_object_record=None, group_id=None, id=None, is_query_over=None, left_time=None, migrate_since=None, migrate_speed=None, name=None, progress=None, real_size=None, skipped_num=None, src_node=None, start_time=None, status=None, successful_num=None, task_type=None, group_type=None, total_num=None, total_size=None, total_time=None, smn_info=None, source_cdn=None, success_record_error_reason=None, skip_record_error_reason=None, object_overwrite_mode=None, dst_storage_policy=None, consistency_check=None, enable_requester_pays=None, task_priority=None):
        r"""TaskResp

        The model defined in huaweicloud sdk

        :param bandwidth_policy: 流量控制策略，每个任务最多可设置5条限速策略。
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        :param complete_size: 任务迁移完成大小（Byte）。
        :type complete_size: int
        :param description: 任务描述，没有设置时为空字符串。
        :type description: str
        :param dst_node: 
        :type dst_node: :class:`huaweicloudsdkoms.v2.DstNodeResp`
        :param enable_failed_object_recording: 是否记录失败对象。开启后，如果有迁移失败对象，会在目的端存储失败对象信息。
        :type enable_failed_object_recording: bool
        :param enable_kms: 存储入OBS时是否使用KMS加密。
        :type enable_kms: bool
        :param enable_metadata_migration: 是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。
        :type enable_metadata_migration: bool
        :param enable_restore: 是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。
        :type enable_restore: bool
        :param error_reason: 
        :type error_reason: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        :param failed_num: 迁移失败对象数量。
        :type failed_num: int
        :param failed_object_record: 
        :type failed_object_record: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        :param group_id: 迁移任务组ID，当任务由迁移任务组创建时会包含迁移任务组的id信息。
        :type group_id: str
        :param id: 任务ID。
        :type id: int
        :param is_query_over: 迁移任务是否完成源端对象统计数据扫描。
        :type is_query_over: bool
        :param left_time: 任务剩余时间（毫秒）。
        :type left_time: int
        :param migrate_since: 迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。
        :type migrate_since: int
        :param migrate_speed: 任务迁移速度（Byte/s）。
        :type migrate_speed: int
        :param name: 任务名称。
        :type name: str
        :param progress: 任务进度，例如：0.522代表任务进度为52.2%，1代表任务进度为100%。
        :type progress: float
        :param real_size: 实际迁移对象总大小（Byte），忽略对象的大小不会统计在内。
        :type real_size: int
        :param skipped_num: 迁移忽略对象数（存在以下两种情况会自动跳过：1.源端对象最后修改时间在迁移指定时间前；2.目的端已有该对象。）
        :type skipped_num: int
        :param src_node: 
        :type src_node: :class:`huaweicloudsdkoms.v2.SrcNodeResp`
        :param start_time: 任务启动时间（Unix时间戳，毫秒）。
        :type start_time: int
        :param status: 任务状态。 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7：等待中
        :type status: int
        :param successful_num: 迁移成功对象数量。
        :type successful_num: int
        :param task_type: 任务类型，为空默认设置为object。 list：对象列表迁移 object：文件/文件夹迁移 prefix：对象前缀迁移 url_list: url对象列表
        :type task_type: str
        :param group_type: 分组类型 NORMAL_TASK：一般迁移任务 SYNC_TASK：同步任务所属迁移任务 GROUP_TASK：任务组所属迁移任务
        :type group_type: str
        :param total_num: 迁移任务对象总数量。
        :type total_num: int
        :param total_size: 任务迁移总大小（Byte）。
        :type total_size: int
        :param total_time: 任务总耗时（毫秒）。
        :type total_time: int
        :param smn_info: 
        :type smn_info: :class:`huaweicloudsdkoms.v2.SmnInfo`
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        :param success_record_error_reason: 迁移成功对象列表记录失败错误码，记录成功时为空
        :type success_record_error_reason: str
        :param skip_record_error_reason: 迁移忽略对象列表记录失败错误码,记录记录成功时为空。
        :type skip_record_error_reason: str
        :param object_overwrite_mode: 迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。
        :type object_overwrite_mode: str
        :param dst_storage_policy: 目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型
        :type dst_storage_policy: str
        :param consistency_check: 一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。
        :type consistency_check: str
        :param enable_requester_pays: 是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。
        :type enable_requester_pays: bool
        :param task_priority: HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级
        :type task_priority: str
        """
        
        

        self._bandwidth_policy = None
        self._complete_size = None
        self._description = None
        self._dst_node = None
        self._enable_failed_object_recording = None
        self._enable_kms = None
        self._enable_metadata_migration = None
        self._enable_restore = None
        self._error_reason = None
        self._failed_num = None
        self._failed_object_record = None
        self._group_id = None
        self._id = None
        self._is_query_over = None
        self._left_time = None
        self._migrate_since = None
        self._migrate_speed = None
        self._name = None
        self._progress = None
        self._real_size = None
        self._skipped_num = None
        self._src_node = None
        self._start_time = None
        self._status = None
        self._successful_num = None
        self._task_type = None
        self._group_type = None
        self._total_num = None
        self._total_size = None
        self._total_time = None
        self._smn_info = None
        self._source_cdn = None
        self._success_record_error_reason = None
        self._skip_record_error_reason = None
        self._object_overwrite_mode = None
        self._dst_storage_policy = None
        self._consistency_check = None
        self._enable_requester_pays = None
        self._task_priority = None
        self.discriminator = None

        if bandwidth_policy is not None:
            self.bandwidth_policy = bandwidth_policy
        if complete_size is not None:
            self.complete_size = complete_size
        if description is not None:
            self.description = description
        if dst_node is not None:
            self.dst_node = dst_node
        if enable_failed_object_recording is not None:
            self.enable_failed_object_recording = enable_failed_object_recording
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if enable_metadata_migration is not None:
            self.enable_metadata_migration = enable_metadata_migration
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if error_reason is not None:
            self.error_reason = error_reason
        if failed_num is not None:
            self.failed_num = failed_num
        if failed_object_record is not None:
            self.failed_object_record = failed_object_record
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if is_query_over is not None:
            self.is_query_over = is_query_over
        if left_time is not None:
            self.left_time = left_time
        if migrate_since is not None:
            self.migrate_since = migrate_since
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if name is not None:
            self.name = name
        if progress is not None:
            self.progress = progress
        if real_size is not None:
            self.real_size = real_size
        if skipped_num is not None:
            self.skipped_num = skipped_num
        if src_node is not None:
            self.src_node = src_node
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if successful_num is not None:
            self.successful_num = successful_num
        if task_type is not None:
            self.task_type = task_type
        if group_type is not None:
            self.group_type = group_type
        if total_num is not None:
            self.total_num = total_num
        if total_size is not None:
            self.total_size = total_size
        if total_time is not None:
            self.total_time = total_time
        if smn_info is not None:
            self.smn_info = smn_info
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if success_record_error_reason is not None:
            self.success_record_error_reason = success_record_error_reason
        if skip_record_error_reason is not None:
            self.skip_record_error_reason = skip_record_error_reason
        if object_overwrite_mode is not None:
            self.object_overwrite_mode = object_overwrite_mode
        if dst_storage_policy is not None:
            self.dst_storage_policy = dst_storage_policy
        if consistency_check is not None:
            self.consistency_check = consistency_check
        if enable_requester_pays is not None:
            self.enable_requester_pays = enable_requester_pays
        if task_priority is not None:
            self.task_priority = task_priority

    @property
    def bandwidth_policy(self):
        r"""Gets the bandwidth_policy of this TaskResp.

        流量控制策略，每个任务最多可设置5条限速策略。

        :return: The bandwidth_policy of this TaskResp.
        :rtype: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        r"""Sets the bandwidth_policy of this TaskResp.

        流量控制策略，每个任务最多可设置5条限速策略。

        :param bandwidth_policy: The bandwidth_policy of this TaskResp.
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def complete_size(self):
        r"""Gets the complete_size of this TaskResp.

        任务迁移完成大小（Byte）。

        :return: The complete_size of this TaskResp.
        :rtype: int
        """
        return self._complete_size

    @complete_size.setter
    def complete_size(self, complete_size):
        r"""Sets the complete_size of this TaskResp.

        任务迁移完成大小（Byte）。

        :param complete_size: The complete_size of this TaskResp.
        :type complete_size: int
        """
        self._complete_size = complete_size

    @property
    def description(self):
        r"""Gets the description of this TaskResp.

        任务描述，没有设置时为空字符串。

        :return: The description of this TaskResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskResp.

        任务描述，没有设置时为空字符串。

        :param description: The description of this TaskResp.
        :type description: str
        """
        self._description = description

    @property
    def dst_node(self):
        r"""Gets the dst_node of this TaskResp.

        :return: The dst_node of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.DstNodeResp`
        """
        return self._dst_node

    @dst_node.setter
    def dst_node(self, dst_node):
        r"""Sets the dst_node of this TaskResp.

        :param dst_node: The dst_node of this TaskResp.
        :type dst_node: :class:`huaweicloudsdkoms.v2.DstNodeResp`
        """
        self._dst_node = dst_node

    @property
    def enable_failed_object_recording(self):
        r"""Gets the enable_failed_object_recording of this TaskResp.

        是否记录失败对象。开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :return: The enable_failed_object_recording of this TaskResp.
        :rtype: bool
        """
        return self._enable_failed_object_recording

    @enable_failed_object_recording.setter
    def enable_failed_object_recording(self, enable_failed_object_recording):
        r"""Sets the enable_failed_object_recording of this TaskResp.

        是否记录失败对象。开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :param enable_failed_object_recording: The enable_failed_object_recording of this TaskResp.
        :type enable_failed_object_recording: bool
        """
        self._enable_failed_object_recording = enable_failed_object_recording

    @property
    def enable_kms(self):
        r"""Gets the enable_kms of this TaskResp.

        存储入OBS时是否使用KMS加密。

        :return: The enable_kms of this TaskResp.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        r"""Sets the enable_kms of this TaskResp.

        存储入OBS时是否使用KMS加密。

        :param enable_kms: The enable_kms of this TaskResp.
        :type enable_kms: bool
        """
        self._enable_kms = enable_kms

    @property
    def enable_metadata_migration(self):
        r"""Gets the enable_metadata_migration of this TaskResp.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :return: The enable_metadata_migration of this TaskResp.
        :rtype: bool
        """
        return self._enable_metadata_migration

    @enable_metadata_migration.setter
    def enable_metadata_migration(self, enable_metadata_migration):
        r"""Sets the enable_metadata_migration of this TaskResp.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :param enable_metadata_migration: The enable_metadata_migration of this TaskResp.
        :type enable_metadata_migration: bool
        """
        self._enable_metadata_migration = enable_metadata_migration

    @property
    def enable_restore(self):
        r"""Gets the enable_restore of this TaskResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :return: The enable_restore of this TaskResp.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        r"""Sets the enable_restore of this TaskResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :param enable_restore: The enable_restore of this TaskResp.
        :type enable_restore: bool
        """
        self._enable_restore = enable_restore

    @property
    def error_reason(self):
        r"""Gets the error_reason of this TaskResp.

        :return: The error_reason of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this TaskResp.

        :param error_reason: The error_reason of this TaskResp.
        :type error_reason: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        """
        self._error_reason = error_reason

    @property
    def failed_num(self):
        r"""Gets the failed_num of this TaskResp.

        迁移失败对象数量。

        :return: The failed_num of this TaskResp.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this TaskResp.

        迁移失败对象数量。

        :param failed_num: The failed_num of this TaskResp.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def failed_object_record(self):
        r"""Gets the failed_object_record of this TaskResp.

        :return: The failed_object_record of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        """
        return self._failed_object_record

    @failed_object_record.setter
    def failed_object_record(self, failed_object_record):
        r"""Sets the failed_object_record of this TaskResp.

        :param failed_object_record: The failed_object_record of this TaskResp.
        :type failed_object_record: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        """
        self._failed_object_record = failed_object_record

    @property
    def group_id(self):
        r"""Gets the group_id of this TaskResp.

        迁移任务组ID，当任务由迁移任务组创建时会包含迁移任务组的id信息。

        :return: The group_id of this TaskResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this TaskResp.

        迁移任务组ID，当任务由迁移任务组创建时会包含迁移任务组的id信息。

        :param group_id: The group_id of this TaskResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this TaskResp.

        任务ID。

        :return: The id of this TaskResp.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskResp.

        任务ID。

        :param id: The id of this TaskResp.
        :type id: int
        """
        self._id = id

    @property
    def is_query_over(self):
        r"""Gets the is_query_over of this TaskResp.

        迁移任务是否完成源端对象统计数据扫描。

        :return: The is_query_over of this TaskResp.
        :rtype: bool
        """
        return self._is_query_over

    @is_query_over.setter
    def is_query_over(self, is_query_over):
        r"""Sets the is_query_over of this TaskResp.

        迁移任务是否完成源端对象统计数据扫描。

        :param is_query_over: The is_query_over of this TaskResp.
        :type is_query_over: bool
        """
        self._is_query_over = is_query_over

    @property
    def left_time(self):
        r"""Gets the left_time of this TaskResp.

        任务剩余时间（毫秒）。

        :return: The left_time of this TaskResp.
        :rtype: int
        """
        return self._left_time

    @left_time.setter
    def left_time(self, left_time):
        r"""Sets the left_time of this TaskResp.

        任务剩余时间（毫秒）。

        :param left_time: The left_time of this TaskResp.
        :type left_time: int
        """
        self._left_time = left_time

    @property
    def migrate_since(self):
        r"""Gets the migrate_since of this TaskResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :return: The migrate_since of this TaskResp.
        :rtype: int
        """
        return self._migrate_since

    @migrate_since.setter
    def migrate_since(self, migrate_since):
        r"""Sets the migrate_since of this TaskResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :param migrate_since: The migrate_since of this TaskResp.
        :type migrate_since: int
        """
        self._migrate_since = migrate_since

    @property
    def migrate_speed(self):
        r"""Gets the migrate_speed of this TaskResp.

        任务迁移速度（Byte/s）。

        :return: The migrate_speed of this TaskResp.
        :rtype: int
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        r"""Sets the migrate_speed of this TaskResp.

        任务迁移速度（Byte/s）。

        :param migrate_speed: The migrate_speed of this TaskResp.
        :type migrate_speed: int
        """
        self._migrate_speed = migrate_speed

    @property
    def name(self):
        r"""Gets the name of this TaskResp.

        任务名称。

        :return: The name of this TaskResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskResp.

        任务名称。

        :param name: The name of this TaskResp.
        :type name: str
        """
        self._name = name

    @property
    def progress(self):
        r"""Gets the progress of this TaskResp.

        任务进度，例如：0.522代表任务进度为52.2%，1代表任务进度为100%。

        :return: The progress of this TaskResp.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this TaskResp.

        任务进度，例如：0.522代表任务进度为52.2%，1代表任务进度为100%。

        :param progress: The progress of this TaskResp.
        :type progress: float
        """
        self._progress = progress

    @property
    def real_size(self):
        r"""Gets the real_size of this TaskResp.

        实际迁移对象总大小（Byte），忽略对象的大小不会统计在内。

        :return: The real_size of this TaskResp.
        :rtype: int
        """
        return self._real_size

    @real_size.setter
    def real_size(self, real_size):
        r"""Sets the real_size of this TaskResp.

        实际迁移对象总大小（Byte），忽略对象的大小不会统计在内。

        :param real_size: The real_size of this TaskResp.
        :type real_size: int
        """
        self._real_size = real_size

    @property
    def skipped_num(self):
        r"""Gets the skipped_num of this TaskResp.

        迁移忽略对象数（存在以下两种情况会自动跳过：1.源端对象最后修改时间在迁移指定时间前；2.目的端已有该对象。）

        :return: The skipped_num of this TaskResp.
        :rtype: int
        """
        return self._skipped_num

    @skipped_num.setter
    def skipped_num(self, skipped_num):
        r"""Sets the skipped_num of this TaskResp.

        迁移忽略对象数（存在以下两种情况会自动跳过：1.源端对象最后修改时间在迁移指定时间前；2.目的端已有该对象。）

        :param skipped_num: The skipped_num of this TaskResp.
        :type skipped_num: int
        """
        self._skipped_num = skipped_num

    @property
    def src_node(self):
        r"""Gets the src_node of this TaskResp.

        :return: The src_node of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.SrcNodeResp`
        """
        return self._src_node

    @src_node.setter
    def src_node(self, src_node):
        r"""Sets the src_node of this TaskResp.

        :param src_node: The src_node of this TaskResp.
        :type src_node: :class:`huaweicloudsdkoms.v2.SrcNodeResp`
        """
        self._src_node = src_node

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskResp.

        任务启动时间（Unix时间戳，毫秒）。

        :return: The start_time of this TaskResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskResp.

        任务启动时间（Unix时间戳，毫秒）。

        :param start_time: The start_time of this TaskResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this TaskResp.

        任务状态。 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7：等待中

        :return: The status of this TaskResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskResp.

        任务状态。 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7：等待中

        :param status: The status of this TaskResp.
        :type status: int
        """
        self._status = status

    @property
    def successful_num(self):
        r"""Gets the successful_num of this TaskResp.

        迁移成功对象数量。

        :return: The successful_num of this TaskResp.
        :rtype: int
        """
        return self._successful_num

    @successful_num.setter
    def successful_num(self, successful_num):
        r"""Sets the successful_num of this TaskResp.

        迁移成功对象数量。

        :param successful_num: The successful_num of this TaskResp.
        :type successful_num: int
        """
        self._successful_num = successful_num

    @property
    def task_type(self):
        r"""Gets the task_type of this TaskResp.

        任务类型，为空默认设置为object。 list：对象列表迁移 object：文件/文件夹迁移 prefix：对象前缀迁移 url_list: url对象列表

        :return: The task_type of this TaskResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this TaskResp.

        任务类型，为空默认设置为object。 list：对象列表迁移 object：文件/文件夹迁移 prefix：对象前缀迁移 url_list: url对象列表

        :param task_type: The task_type of this TaskResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def group_type(self):
        r"""Gets the group_type of this TaskResp.

        分组类型 NORMAL_TASK：一般迁移任务 SYNC_TASK：同步任务所属迁移任务 GROUP_TASK：任务组所属迁移任务

        :return: The group_type of this TaskResp.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this TaskResp.

        分组类型 NORMAL_TASK：一般迁移任务 SYNC_TASK：同步任务所属迁移任务 GROUP_TASK：任务组所属迁移任务

        :param group_type: The group_type of this TaskResp.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def total_num(self):
        r"""Gets the total_num of this TaskResp.

        迁移任务对象总数量。

        :return: The total_num of this TaskResp.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this TaskResp.

        迁移任务对象总数量。

        :param total_num: The total_num of this TaskResp.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def total_size(self):
        r"""Gets the total_size of this TaskResp.

        任务迁移总大小（Byte）。

        :return: The total_size of this TaskResp.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this TaskResp.

        任务迁移总大小（Byte）。

        :param total_size: The total_size of this TaskResp.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def total_time(self):
        r"""Gets the total_time of this TaskResp.

        任务总耗时（毫秒）。

        :return: The total_time of this TaskResp.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this TaskResp.

        任务总耗时（毫秒）。

        :param total_time: The total_time of this TaskResp.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def smn_info(self):
        r"""Gets the smn_info of this TaskResp.

        :return: The smn_info of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.SmnInfo`
        """
        return self._smn_info

    @smn_info.setter
    def smn_info(self, smn_info):
        r"""Sets the smn_info of this TaskResp.

        :param smn_info: The smn_info of this TaskResp.
        :type smn_info: :class:`huaweicloudsdkoms.v2.SmnInfo`
        """
        self._smn_info = smn_info

    @property
    def source_cdn(self):
        r"""Gets the source_cdn of this TaskResp.

        :return: The source_cdn of this TaskResp.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        r"""Sets the source_cdn of this TaskResp.

        :param source_cdn: The source_cdn of this TaskResp.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        self._source_cdn = source_cdn

    @property
    def success_record_error_reason(self):
        r"""Gets the success_record_error_reason of this TaskResp.

        迁移成功对象列表记录失败错误码，记录成功时为空

        :return: The success_record_error_reason of this TaskResp.
        :rtype: str
        """
        return self._success_record_error_reason

    @success_record_error_reason.setter
    def success_record_error_reason(self, success_record_error_reason):
        r"""Sets the success_record_error_reason of this TaskResp.

        迁移成功对象列表记录失败错误码，记录成功时为空

        :param success_record_error_reason: The success_record_error_reason of this TaskResp.
        :type success_record_error_reason: str
        """
        self._success_record_error_reason = success_record_error_reason

    @property
    def skip_record_error_reason(self):
        r"""Gets the skip_record_error_reason of this TaskResp.

        迁移忽略对象列表记录失败错误码,记录记录成功时为空。

        :return: The skip_record_error_reason of this TaskResp.
        :rtype: str
        """
        return self._skip_record_error_reason

    @skip_record_error_reason.setter
    def skip_record_error_reason(self, skip_record_error_reason):
        r"""Sets the skip_record_error_reason of this TaskResp.

        迁移忽略对象列表记录失败错误码,记录记录成功时为空。

        :param skip_record_error_reason: The skip_record_error_reason of this TaskResp.
        :type skip_record_error_reason: str
        """
        self._skip_record_error_reason = skip_record_error_reason

    @property
    def object_overwrite_mode(self):
        r"""Gets the object_overwrite_mode of this TaskResp.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :return: The object_overwrite_mode of this TaskResp.
        :rtype: str
        """
        return self._object_overwrite_mode

    @object_overwrite_mode.setter
    def object_overwrite_mode(self, object_overwrite_mode):
        r"""Sets the object_overwrite_mode of this TaskResp.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :param object_overwrite_mode: The object_overwrite_mode of this TaskResp.
        :type object_overwrite_mode: str
        """
        self._object_overwrite_mode = object_overwrite_mode

    @property
    def dst_storage_policy(self):
        r"""Gets the dst_storage_policy of this TaskResp.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :return: The dst_storage_policy of this TaskResp.
        :rtype: str
        """
        return self._dst_storage_policy

    @dst_storage_policy.setter
    def dst_storage_policy(self, dst_storage_policy):
        r"""Sets the dst_storage_policy of this TaskResp.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :param dst_storage_policy: The dst_storage_policy of this TaskResp.
        :type dst_storage_policy: str
        """
        self._dst_storage_policy = dst_storage_policy

    @property
    def consistency_check(self):
        r"""Gets the consistency_check of this TaskResp.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :return: The consistency_check of this TaskResp.
        :rtype: str
        """
        return self._consistency_check

    @consistency_check.setter
    def consistency_check(self, consistency_check):
        r"""Sets the consistency_check of this TaskResp.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :param consistency_check: The consistency_check of this TaskResp.
        :type consistency_check: str
        """
        self._consistency_check = consistency_check

    @property
    def enable_requester_pays(self):
        r"""Gets the enable_requester_pays of this TaskResp.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :return: The enable_requester_pays of this TaskResp.
        :rtype: bool
        """
        return self._enable_requester_pays

    @enable_requester_pays.setter
    def enable_requester_pays(self, enable_requester_pays):
        r"""Sets the enable_requester_pays of this TaskResp.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :param enable_requester_pays: The enable_requester_pays of this TaskResp.
        :type enable_requester_pays: bool
        """
        self._enable_requester_pays = enable_requester_pays

    @property
    def task_priority(self):
        r"""Gets the task_priority of this TaskResp.

        HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级

        :return: The task_priority of this TaskResp.
        :rtype: str
        """
        return self._task_priority

    @task_priority.setter
    def task_priority(self, task_priority):
        r"""Sets the task_priority of this TaskResp.

        HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级

        :param task_priority: The task_priority of this TaskResp.
        :type task_priority: str
        """
        self._task_priority = task_priority

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
        if not isinstance(other, TaskResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
