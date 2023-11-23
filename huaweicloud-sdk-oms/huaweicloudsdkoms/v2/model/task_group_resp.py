# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskGroupResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'status': 'int',
        'error_reason': 'ErrorReasonResp',
        'src_node': 'TaskGroupSrcNodeResp',
        'description': 'str',
        'dst_node': 'TaskGroupDstNodeResp',
        'enable_metadata_migration': 'bool',
        'enable_failed_object_recording': 'bool',
        'enable_restore': 'bool',
        'enable_kms': 'bool',
        'task_type': 'str',
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'smn_config': 'SmnInfo',
        'source_cdn': 'SourceCdnResp',
        'migrate_since': 'int',
        'migrate_speed': 'int',
        'total_time': 'int',
        'start_time': 'int',
        'total_task_num': 'int',
        'create_task_num': 'int',
        'failed_task_num': 'int',
        'complete_task_num': 'int',
        'paused_task_num': 'int',
        'executing_task_num': 'int',
        'waiting_task_num': 'int',
        'total_num': 'int',
        'create_complete_num': 'int',
        'success_num': 'int',
        'fail_num': 'int',
        'skip_num': 'int',
        'total_size': 'int',
        'create_complete_size': 'int',
        'complete_size': 'int',
        'failed_object_record': 'FailedObjectRecordDto',
        'object_overwrite_mode': 'str',
        'consistency_check': 'str',
        'enable_requester_pays': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'status': 'status',
        'error_reason': 'error_reason',
        'src_node': 'src_node',
        'description': 'description',
        'dst_node': 'dst_node',
        'enable_metadata_migration': 'enable_metadata_migration',
        'enable_failed_object_recording': 'enable_failed_object_recording',
        'enable_restore': 'enable_restore',
        'enable_kms': 'enable_kms',
        'task_type': 'task_type',
        'bandwidth_policy': 'bandwidth_policy',
        'smn_config': 'smn_config',
        'source_cdn': 'source_cdn',
        'migrate_since': 'migrate_since',
        'migrate_speed': 'migrate_speed',
        'total_time': 'total_time',
        'start_time': 'start_time',
        'total_task_num': 'total_task_num',
        'create_task_num': 'create_task_num',
        'failed_task_num': 'failed_task_num',
        'complete_task_num': 'complete_task_num',
        'paused_task_num': 'paused_task_num',
        'executing_task_num': 'executing_task_num',
        'waiting_task_num': 'waiting_task_num',
        'total_num': 'total_num',
        'create_complete_num': 'create_complete_num',
        'success_num': 'success_num',
        'fail_num': 'fail_num',
        'skip_num': 'skip_num',
        'total_size': 'total_size',
        'create_complete_size': 'create_complete_size',
        'complete_size': 'complete_size',
        'failed_object_record': 'failed_object_record',
        'object_overwrite_mode': 'object_overwrite_mode',
        'consistency_check': 'consistency_check',
        'enable_requester_pays': 'enable_requester_pays'
    }

    def __init__(self, group_id=None, status=None, error_reason=None, src_node=None, description=None, dst_node=None, enable_metadata_migration=None, enable_failed_object_recording=None, enable_restore=None, enable_kms=None, task_type=None, bandwidth_policy=None, smn_config=None, source_cdn=None, migrate_since=None, migrate_speed=None, total_time=None, start_time=None, total_task_num=None, create_task_num=None, failed_task_num=None, complete_task_num=None, paused_task_num=None, executing_task_num=None, waiting_task_num=None, total_num=None, create_complete_num=None, success_num=None, fail_num=None, skip_num=None, total_size=None, create_complete_size=None, complete_size=None, failed_object_record=None, object_overwrite_mode=None, consistency_check=None, enable_requester_pays=None):
        """TaskGroupResp

        The model defined in huaweicloud sdk

        :param group_id: 任务组id
        :type group_id: str
        :param status: 迁移组任务状态。 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除
        :type status: int
        :param error_reason: 
        :type error_reason: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        :param src_node: 
        :type src_node: :class:`huaweicloudsdkoms.v2.TaskGroupSrcNodeResp`
        :param description: 任务描述，不能超过255个字符，且不能包含^&lt;&gt;&amp;\&quot;&#39;等特殊字符。
        :type description: str
        :param dst_node: 
        :type dst_node: :class:`huaweicloudsdkoms.v2.TaskGroupDstNodeResp`
        :param enable_metadata_migration: 是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。
        :type enable_metadata_migration: bool
        :param enable_failed_object_recording: 是否开启记录失败对象
        :type enable_failed_object_recording: bool
        :param enable_restore: 是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。
        :type enable_restore: bool
        :param enable_kms: 存储入OBS时是否使用KMS加密。
        :type enable_kms: bool
        :param task_type: 任务类型，默认为PREFIX。 LIST：对象列表迁移 URL_LIST：URL列表迁移， PREFIX：对象前缀迁移
        :type task_type: str
        :param bandwidth_policy: 配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        :param smn_config: 
        :type smn_config: :class:`huaweicloudsdkoms.v2.SmnInfo`
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        :param migrate_since: 迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。
        :type migrate_since: int
        :param migrate_speed: 任务组迁移速度（Byte/s）
        :type migrate_speed: int
        :param total_time: 迁移任务组总耗时(毫秒)
        :type total_time: int
        :param start_time: 迁移任务组的启动时间(Unix时间戳，毫秒)
        :type start_time: int
        :param total_task_num: 任务组包含的迁移任务总数
        :type total_task_num: int
        :param create_task_num: 已创建的迁移任务数
        :type create_task_num: int
        :param failed_task_num: 失败的迁移任务数
        :type failed_task_num: int
        :param complete_task_num: 已完成的迁移任务数
        :type complete_task_num: int
        :param paused_task_num: 暂停的迁移任务数
        :type paused_task_num: int
        :param executing_task_num: 正在运行的迁移任务数
        :type executing_task_num: int
        :param waiting_task_num: 等待中的迁移任务数
        :type waiting_task_num: int
        :param total_num: 迁移任务组包含的对象总数量
        :type total_num: int
        :param create_complete_num: 已完成任务创建的对象总数量
        :type create_complete_num: int
        :param success_num: 成功的对象数量
        :type success_num: int
        :param fail_num: 失败的对象数量
        :type fail_num: int
        :param skip_num: 忽略的对象数量
        :type skip_num: int
        :param total_size: 任务迁移总大小(Byte)
        :type total_size: int
        :param create_complete_size: 已创建迁移任务包含的对象总大小(Byte)
        :type create_complete_size: int
        :param complete_size: 已迁移成功的对象总大小(Byte)
        :type complete_size: int
        :param failed_object_record: 
        :type failed_object_record: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        :param object_overwrite_mode: 迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。
        :type object_overwrite_mode: str
        :param consistency_check: 一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。
        :type consistency_check: str
        :param enable_requester_pays: 是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。
        :type enable_requester_pays: bool
        """
        
        

        self._group_id = None
        self._status = None
        self._error_reason = None
        self._src_node = None
        self._description = None
        self._dst_node = None
        self._enable_metadata_migration = None
        self._enable_failed_object_recording = None
        self._enable_restore = None
        self._enable_kms = None
        self._task_type = None
        self._bandwidth_policy = None
        self._smn_config = None
        self._source_cdn = None
        self._migrate_since = None
        self._migrate_speed = None
        self._total_time = None
        self._start_time = None
        self._total_task_num = None
        self._create_task_num = None
        self._failed_task_num = None
        self._complete_task_num = None
        self._paused_task_num = None
        self._executing_task_num = None
        self._waiting_task_num = None
        self._total_num = None
        self._create_complete_num = None
        self._success_num = None
        self._fail_num = None
        self._skip_num = None
        self._total_size = None
        self._create_complete_size = None
        self._complete_size = None
        self._failed_object_record = None
        self._object_overwrite_mode = None
        self._consistency_check = None
        self._enable_requester_pays = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if status is not None:
            self.status = status
        if error_reason is not None:
            self.error_reason = error_reason
        if src_node is not None:
            self.src_node = src_node
        if description is not None:
            self.description = description
        if dst_node is not None:
            self.dst_node = dst_node
        if enable_metadata_migration is not None:
            self.enable_metadata_migration = enable_metadata_migration
        if enable_failed_object_recording is not None:
            self.enable_failed_object_recording = enable_failed_object_recording
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if task_type is not None:
            self.task_type = task_type
        if bandwidth_policy is not None:
            self.bandwidth_policy = bandwidth_policy
        if smn_config is not None:
            self.smn_config = smn_config
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if migrate_since is not None:
            self.migrate_since = migrate_since
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if total_time is not None:
            self.total_time = total_time
        if start_time is not None:
            self.start_time = start_time
        if total_task_num is not None:
            self.total_task_num = total_task_num
        if create_task_num is not None:
            self.create_task_num = create_task_num
        if failed_task_num is not None:
            self.failed_task_num = failed_task_num
        if complete_task_num is not None:
            self.complete_task_num = complete_task_num
        if paused_task_num is not None:
            self.paused_task_num = paused_task_num
        if executing_task_num is not None:
            self.executing_task_num = executing_task_num
        if waiting_task_num is not None:
            self.waiting_task_num = waiting_task_num
        if total_num is not None:
            self.total_num = total_num
        if create_complete_num is not None:
            self.create_complete_num = create_complete_num
        if success_num is not None:
            self.success_num = success_num
        if fail_num is not None:
            self.fail_num = fail_num
        if skip_num is not None:
            self.skip_num = skip_num
        if total_size is not None:
            self.total_size = total_size
        if create_complete_size is not None:
            self.create_complete_size = create_complete_size
        if complete_size is not None:
            self.complete_size = complete_size
        if failed_object_record is not None:
            self.failed_object_record = failed_object_record
        if object_overwrite_mode is not None:
            self.object_overwrite_mode = object_overwrite_mode
        if consistency_check is not None:
            self.consistency_check = consistency_check
        if enable_requester_pays is not None:
            self.enable_requester_pays = enable_requester_pays

    @property
    def group_id(self):
        """Gets the group_id of this TaskGroupResp.

        任务组id

        :return: The group_id of this TaskGroupResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TaskGroupResp.

        任务组id

        :param group_id: The group_id of this TaskGroupResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def status(self):
        """Gets the status of this TaskGroupResp.

        迁移组任务状态。 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除

        :return: The status of this TaskGroupResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskGroupResp.

        迁移组任务状态。 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除

        :param status: The status of this TaskGroupResp.
        :type status: int
        """
        self._status = status

    @property
    def error_reason(self):
        """Gets the error_reason of this TaskGroupResp.

        :return: The error_reason of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this TaskGroupResp.

        :param error_reason: The error_reason of this TaskGroupResp.
        :type error_reason: :class:`huaweicloudsdkoms.v2.ErrorReasonResp`
        """
        self._error_reason = error_reason

    @property
    def src_node(self):
        """Gets the src_node of this TaskGroupResp.

        :return: The src_node of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.TaskGroupSrcNodeResp`
        """
        return self._src_node

    @src_node.setter
    def src_node(self, src_node):
        """Sets the src_node of this TaskGroupResp.

        :param src_node: The src_node of this TaskGroupResp.
        :type src_node: :class:`huaweicloudsdkoms.v2.TaskGroupSrcNodeResp`
        """
        self._src_node = src_node

    @property
    def description(self):
        """Gets the description of this TaskGroupResp.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :return: The description of this TaskGroupResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskGroupResp.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :param description: The description of this TaskGroupResp.
        :type description: str
        """
        self._description = description

    @property
    def dst_node(self):
        """Gets the dst_node of this TaskGroupResp.

        :return: The dst_node of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.TaskGroupDstNodeResp`
        """
        return self._dst_node

    @dst_node.setter
    def dst_node(self, dst_node):
        """Sets the dst_node of this TaskGroupResp.

        :param dst_node: The dst_node of this TaskGroupResp.
        :type dst_node: :class:`huaweicloudsdkoms.v2.TaskGroupDstNodeResp`
        """
        self._dst_node = dst_node

    @property
    def enable_metadata_migration(self):
        """Gets the enable_metadata_migration of this TaskGroupResp.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :return: The enable_metadata_migration of this TaskGroupResp.
        :rtype: bool
        """
        return self._enable_metadata_migration

    @enable_metadata_migration.setter
    def enable_metadata_migration(self, enable_metadata_migration):
        """Sets the enable_metadata_migration of this TaskGroupResp.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :param enable_metadata_migration: The enable_metadata_migration of this TaskGroupResp.
        :type enable_metadata_migration: bool
        """
        self._enable_metadata_migration = enable_metadata_migration

    @property
    def enable_failed_object_recording(self):
        """Gets the enable_failed_object_recording of this TaskGroupResp.

        是否开启记录失败对象

        :return: The enable_failed_object_recording of this TaskGroupResp.
        :rtype: bool
        """
        return self._enable_failed_object_recording

    @enable_failed_object_recording.setter
    def enable_failed_object_recording(self, enable_failed_object_recording):
        """Sets the enable_failed_object_recording of this TaskGroupResp.

        是否开启记录失败对象

        :param enable_failed_object_recording: The enable_failed_object_recording of this TaskGroupResp.
        :type enable_failed_object_recording: bool
        """
        self._enable_failed_object_recording = enable_failed_object_recording

    @property
    def enable_restore(self):
        """Gets the enable_restore of this TaskGroupResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :return: The enable_restore of this TaskGroupResp.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        """Sets the enable_restore of this TaskGroupResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :param enable_restore: The enable_restore of this TaskGroupResp.
        :type enable_restore: bool
        """
        self._enable_restore = enable_restore

    @property
    def enable_kms(self):
        """Gets the enable_kms of this TaskGroupResp.

        存储入OBS时是否使用KMS加密。

        :return: The enable_kms of this TaskGroupResp.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        """Sets the enable_kms of this TaskGroupResp.

        存储入OBS时是否使用KMS加密。

        :param enable_kms: The enable_kms of this TaskGroupResp.
        :type enable_kms: bool
        """
        self._enable_kms = enable_kms

    @property
    def task_type(self):
        """Gets the task_type of this TaskGroupResp.

        任务类型，默认为PREFIX。 LIST：对象列表迁移 URL_LIST：URL列表迁移， PREFIX：对象前缀迁移

        :return: The task_type of this TaskGroupResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskGroupResp.

        任务类型，默认为PREFIX。 LIST：对象列表迁移 URL_LIST：URL列表迁移， PREFIX：对象前缀迁移

        :param task_type: The task_type of this TaskGroupResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def bandwidth_policy(self):
        """Gets the bandwidth_policy of this TaskGroupResp.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :return: The bandwidth_policy of this TaskGroupResp.
        :rtype: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        """Sets the bandwidth_policy of this TaskGroupResp.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :param bandwidth_policy: The bandwidth_policy of this TaskGroupResp.
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def smn_config(self):
        """Gets the smn_config of this TaskGroupResp.

        :return: The smn_config of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.SmnInfo`
        """
        return self._smn_config

    @smn_config.setter
    def smn_config(self, smn_config):
        """Sets the smn_config of this TaskGroupResp.

        :param smn_config: The smn_config of this TaskGroupResp.
        :type smn_config: :class:`huaweicloudsdkoms.v2.SmnInfo`
        """
        self._smn_config = smn_config

    @property
    def source_cdn(self):
        """Gets the source_cdn of this TaskGroupResp.

        :return: The source_cdn of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        """Sets the source_cdn of this TaskGroupResp.

        :param source_cdn: The source_cdn of this TaskGroupResp.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnResp`
        """
        self._source_cdn = source_cdn

    @property
    def migrate_since(self):
        """Gets the migrate_since of this TaskGroupResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :return: The migrate_since of this TaskGroupResp.
        :rtype: int
        """
        return self._migrate_since

    @migrate_since.setter
    def migrate_since(self, migrate_since):
        """Sets the migrate_since of this TaskGroupResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :param migrate_since: The migrate_since of this TaskGroupResp.
        :type migrate_since: int
        """
        self._migrate_since = migrate_since

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this TaskGroupResp.

        任务组迁移速度（Byte/s）

        :return: The migrate_speed of this TaskGroupResp.
        :rtype: int
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this TaskGroupResp.

        任务组迁移速度（Byte/s）

        :param migrate_speed: The migrate_speed of this TaskGroupResp.
        :type migrate_speed: int
        """
        self._migrate_speed = migrate_speed

    @property
    def total_time(self):
        """Gets the total_time of this TaskGroupResp.

        迁移任务组总耗时(毫秒)

        :return: The total_time of this TaskGroupResp.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this TaskGroupResp.

        迁移任务组总耗时(毫秒)

        :param total_time: The total_time of this TaskGroupResp.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def start_time(self):
        """Gets the start_time of this TaskGroupResp.

        迁移任务组的启动时间(Unix时间戳，毫秒)

        :return: The start_time of this TaskGroupResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskGroupResp.

        迁移任务组的启动时间(Unix时间戳，毫秒)

        :param start_time: The start_time of this TaskGroupResp.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def total_task_num(self):
        """Gets the total_task_num of this TaskGroupResp.

        任务组包含的迁移任务总数

        :return: The total_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._total_task_num

    @total_task_num.setter
    def total_task_num(self, total_task_num):
        """Sets the total_task_num of this TaskGroupResp.

        任务组包含的迁移任务总数

        :param total_task_num: The total_task_num of this TaskGroupResp.
        :type total_task_num: int
        """
        self._total_task_num = total_task_num

    @property
    def create_task_num(self):
        """Gets the create_task_num of this TaskGroupResp.

        已创建的迁移任务数

        :return: The create_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._create_task_num

    @create_task_num.setter
    def create_task_num(self, create_task_num):
        """Sets the create_task_num of this TaskGroupResp.

        已创建的迁移任务数

        :param create_task_num: The create_task_num of this TaskGroupResp.
        :type create_task_num: int
        """
        self._create_task_num = create_task_num

    @property
    def failed_task_num(self):
        """Gets the failed_task_num of this TaskGroupResp.

        失败的迁移任务数

        :return: The failed_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._failed_task_num

    @failed_task_num.setter
    def failed_task_num(self, failed_task_num):
        """Sets the failed_task_num of this TaskGroupResp.

        失败的迁移任务数

        :param failed_task_num: The failed_task_num of this TaskGroupResp.
        :type failed_task_num: int
        """
        self._failed_task_num = failed_task_num

    @property
    def complete_task_num(self):
        """Gets the complete_task_num of this TaskGroupResp.

        已完成的迁移任务数

        :return: The complete_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._complete_task_num

    @complete_task_num.setter
    def complete_task_num(self, complete_task_num):
        """Sets the complete_task_num of this TaskGroupResp.

        已完成的迁移任务数

        :param complete_task_num: The complete_task_num of this TaskGroupResp.
        :type complete_task_num: int
        """
        self._complete_task_num = complete_task_num

    @property
    def paused_task_num(self):
        """Gets the paused_task_num of this TaskGroupResp.

        暂停的迁移任务数

        :return: The paused_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._paused_task_num

    @paused_task_num.setter
    def paused_task_num(self, paused_task_num):
        """Sets the paused_task_num of this TaskGroupResp.

        暂停的迁移任务数

        :param paused_task_num: The paused_task_num of this TaskGroupResp.
        :type paused_task_num: int
        """
        self._paused_task_num = paused_task_num

    @property
    def executing_task_num(self):
        """Gets the executing_task_num of this TaskGroupResp.

        正在运行的迁移任务数

        :return: The executing_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._executing_task_num

    @executing_task_num.setter
    def executing_task_num(self, executing_task_num):
        """Sets the executing_task_num of this TaskGroupResp.

        正在运行的迁移任务数

        :param executing_task_num: The executing_task_num of this TaskGroupResp.
        :type executing_task_num: int
        """
        self._executing_task_num = executing_task_num

    @property
    def waiting_task_num(self):
        """Gets the waiting_task_num of this TaskGroupResp.

        等待中的迁移任务数

        :return: The waiting_task_num of this TaskGroupResp.
        :rtype: int
        """
        return self._waiting_task_num

    @waiting_task_num.setter
    def waiting_task_num(self, waiting_task_num):
        """Sets the waiting_task_num of this TaskGroupResp.

        等待中的迁移任务数

        :param waiting_task_num: The waiting_task_num of this TaskGroupResp.
        :type waiting_task_num: int
        """
        self._waiting_task_num = waiting_task_num

    @property
    def total_num(self):
        """Gets the total_num of this TaskGroupResp.

        迁移任务组包含的对象总数量

        :return: The total_num of this TaskGroupResp.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this TaskGroupResp.

        迁移任务组包含的对象总数量

        :param total_num: The total_num of this TaskGroupResp.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def create_complete_num(self):
        """Gets the create_complete_num of this TaskGroupResp.

        已完成任务创建的对象总数量

        :return: The create_complete_num of this TaskGroupResp.
        :rtype: int
        """
        return self._create_complete_num

    @create_complete_num.setter
    def create_complete_num(self, create_complete_num):
        """Sets the create_complete_num of this TaskGroupResp.

        已完成任务创建的对象总数量

        :param create_complete_num: The create_complete_num of this TaskGroupResp.
        :type create_complete_num: int
        """
        self._create_complete_num = create_complete_num

    @property
    def success_num(self):
        """Gets the success_num of this TaskGroupResp.

        成功的对象数量

        :return: The success_num of this TaskGroupResp.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this TaskGroupResp.

        成功的对象数量

        :param success_num: The success_num of this TaskGroupResp.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        """Gets the fail_num of this TaskGroupResp.

        失败的对象数量

        :return: The fail_num of this TaskGroupResp.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        """Sets the fail_num of this TaskGroupResp.

        失败的对象数量

        :param fail_num: The fail_num of this TaskGroupResp.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def skip_num(self):
        """Gets the skip_num of this TaskGroupResp.

        忽略的对象数量

        :return: The skip_num of this TaskGroupResp.
        :rtype: int
        """
        return self._skip_num

    @skip_num.setter
    def skip_num(self, skip_num):
        """Sets the skip_num of this TaskGroupResp.

        忽略的对象数量

        :param skip_num: The skip_num of this TaskGroupResp.
        :type skip_num: int
        """
        self._skip_num = skip_num

    @property
    def total_size(self):
        """Gets the total_size of this TaskGroupResp.

        任务迁移总大小(Byte)

        :return: The total_size of this TaskGroupResp.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this TaskGroupResp.

        任务迁移总大小(Byte)

        :param total_size: The total_size of this TaskGroupResp.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def create_complete_size(self):
        """Gets the create_complete_size of this TaskGroupResp.

        已创建迁移任务包含的对象总大小(Byte)

        :return: The create_complete_size of this TaskGroupResp.
        :rtype: int
        """
        return self._create_complete_size

    @create_complete_size.setter
    def create_complete_size(self, create_complete_size):
        """Sets the create_complete_size of this TaskGroupResp.

        已创建迁移任务包含的对象总大小(Byte)

        :param create_complete_size: The create_complete_size of this TaskGroupResp.
        :type create_complete_size: int
        """
        self._create_complete_size = create_complete_size

    @property
    def complete_size(self):
        """Gets the complete_size of this TaskGroupResp.

        已迁移成功的对象总大小(Byte)

        :return: The complete_size of this TaskGroupResp.
        :rtype: int
        """
        return self._complete_size

    @complete_size.setter
    def complete_size(self, complete_size):
        """Sets the complete_size of this TaskGroupResp.

        已迁移成功的对象总大小(Byte)

        :param complete_size: The complete_size of this TaskGroupResp.
        :type complete_size: int
        """
        self._complete_size = complete_size

    @property
    def failed_object_record(self):
        """Gets the failed_object_record of this TaskGroupResp.

        :return: The failed_object_record of this TaskGroupResp.
        :rtype: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        """
        return self._failed_object_record

    @failed_object_record.setter
    def failed_object_record(self, failed_object_record):
        """Sets the failed_object_record of this TaskGroupResp.

        :param failed_object_record: The failed_object_record of this TaskGroupResp.
        :type failed_object_record: :class:`huaweicloudsdkoms.v2.FailedObjectRecordDto`
        """
        self._failed_object_record = failed_object_record

    @property
    def object_overwrite_mode(self):
        """Gets the object_overwrite_mode of this TaskGroupResp.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :return: The object_overwrite_mode of this TaskGroupResp.
        :rtype: str
        """
        return self._object_overwrite_mode

    @object_overwrite_mode.setter
    def object_overwrite_mode(self, object_overwrite_mode):
        """Sets the object_overwrite_mode of this TaskGroupResp.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :param object_overwrite_mode: The object_overwrite_mode of this TaskGroupResp.
        :type object_overwrite_mode: str
        """
        self._object_overwrite_mode = object_overwrite_mode

    @property
    def consistency_check(self):
        """Gets the consistency_check of this TaskGroupResp.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :return: The consistency_check of this TaskGroupResp.
        :rtype: str
        """
        return self._consistency_check

    @consistency_check.setter
    def consistency_check(self, consistency_check):
        """Sets the consistency_check of this TaskGroupResp.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :param consistency_check: The consistency_check of this TaskGroupResp.
        :type consistency_check: str
        """
        self._consistency_check = consistency_check

    @property
    def enable_requester_pays(self):
        """Gets the enable_requester_pays of this TaskGroupResp.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :return: The enable_requester_pays of this TaskGroupResp.
        :rtype: bool
        """
        return self._enable_requester_pays

    @enable_requester_pays.setter
    def enable_requester_pays(self, enable_requester_pays):
        """Sets the enable_requester_pays of this TaskGroupResp.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :param enable_requester_pays: The enable_requester_pays of this TaskGroupResp.
        :type enable_requester_pays: bool
        """
        self._enable_requester_pays = enable_requester_pays

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
        if not isinstance(other, TaskGroupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
