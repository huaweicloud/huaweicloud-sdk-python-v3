# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'src_node': 'SrcNodeReq',
        'dst_node': 'DstNodeReq',
        'enable_kms': 'bool',
        'description': 'str',
        'migrate_since': 'int',
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'source_cdn': 'SourceCdnReq',
        'smn_config': 'SmnConfig',
        'enable_metadata_migration': 'bool',
        'enable_restore': 'bool',
        'enable_failed_object_recording': 'bool',
        'object_overwrite_mode': 'str',
        'consistency_check': 'str',
        'enable_requester_pays': 'bool'
    }

    attribute_map = {
        'task_type': 'task_type',
        'src_node': 'src_node',
        'dst_node': 'dst_node',
        'enable_kms': 'enable_kms',
        'description': 'description',
        'migrate_since': 'migrate_since',
        'bandwidth_policy': 'bandwidth_policy',
        'source_cdn': 'source_cdn',
        'smn_config': 'smn_config',
        'enable_metadata_migration': 'enable_metadata_migration',
        'enable_restore': 'enable_restore',
        'enable_failed_object_recording': 'enable_failed_object_recording',
        'object_overwrite_mode': 'object_overwrite_mode',
        'consistency_check': 'consistency_check',
        'enable_requester_pays': 'enable_requester_pays'
    }

    def __init__(self, task_type=None, src_node=None, dst_node=None, enable_kms=None, description=None, migrate_since=None, bandwidth_policy=None, source_cdn=None, smn_config=None, enable_metadata_migration=None, enable_restore=None, enable_failed_object_recording=None, object_overwrite_mode=None, consistency_check=None, enable_requester_pays=None):
        """CreateTaskReq

        The model defined in huaweicloud sdk

        :param task_type: 任务类型，默认为object。  list：对象列表迁移 url_list：URL列表迁移 object：文件/文件夹迁移，默认 prefix：对象前缀迁移
        :type task_type: str
        :param src_node: 
        :type src_node: :class:`huaweicloudsdkoms.v2.SrcNodeReq`
        :param dst_node: 
        :type dst_node: :class:`huaweicloudsdkoms.v2.DstNodeReq`
        :param enable_kms: 是否开启KMS加密，默认不开启。
        :type enable_kms: bool
        :param description: 任务描述，不能超过255个字符，且不能包含^&lt;&gt;&amp;\&quot;&#39;等特殊字符。
        :type description: str
        :param migrate_since: 以时间戳方式表示的迁移指定时间（单位：秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认不设置迁移指定时间。
        :type migrate_since: int
        :param bandwidth_policy: 配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        :param smn_config: 
        :type smn_config: :class:`huaweicloudsdkoms.v2.SmnConfig`
        :param enable_metadata_migration: 是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。
        :type enable_metadata_migration: bool
        :param enable_restore: 是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。
        :type enable_restore: bool
        :param enable_failed_object_recording: 是否记录失败对象，默认开启。  开启后，如果有迁移失败对象，会在目的端存储失败对象信息。
        :type enable_failed_object_recording: bool
        :param object_overwrite_mode: 迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。
        :type object_overwrite_mode: str
        :param consistency_check: 一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。
        :type consistency_check: str
        :param enable_requester_pays: 是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。
        :type enable_requester_pays: bool
        """
        
        

        self._task_type = None
        self._src_node = None
        self._dst_node = None
        self._enable_kms = None
        self._description = None
        self._migrate_since = None
        self._bandwidth_policy = None
        self._source_cdn = None
        self._smn_config = None
        self._enable_metadata_migration = None
        self._enable_restore = None
        self._enable_failed_object_recording = None
        self._object_overwrite_mode = None
        self._consistency_check = None
        self._enable_requester_pays = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type
        self.src_node = src_node
        self.dst_node = dst_node
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if description is not None:
            self.description = description
        if migrate_since is not None:
            self.migrate_since = migrate_since
        if bandwidth_policy is not None:
            self.bandwidth_policy = bandwidth_policy
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if smn_config is not None:
            self.smn_config = smn_config
        if enable_metadata_migration is not None:
            self.enable_metadata_migration = enable_metadata_migration
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if enable_failed_object_recording is not None:
            self.enable_failed_object_recording = enable_failed_object_recording
        if object_overwrite_mode is not None:
            self.object_overwrite_mode = object_overwrite_mode
        if consistency_check is not None:
            self.consistency_check = consistency_check
        if enable_requester_pays is not None:
            self.enable_requester_pays = enable_requester_pays

    @property
    def task_type(self):
        """Gets the task_type of this CreateTaskReq.

        任务类型，默认为object。  list：对象列表迁移 url_list：URL列表迁移 object：文件/文件夹迁移，默认 prefix：对象前缀迁移

        :return: The task_type of this CreateTaskReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateTaskReq.

        任务类型，默认为object。  list：对象列表迁移 url_list：URL列表迁移 object：文件/文件夹迁移，默认 prefix：对象前缀迁移

        :param task_type: The task_type of this CreateTaskReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def src_node(self):
        """Gets the src_node of this CreateTaskReq.

        :return: The src_node of this CreateTaskReq.
        :rtype: :class:`huaweicloudsdkoms.v2.SrcNodeReq`
        """
        return self._src_node

    @src_node.setter
    def src_node(self, src_node):
        """Sets the src_node of this CreateTaskReq.

        :param src_node: The src_node of this CreateTaskReq.
        :type src_node: :class:`huaweicloudsdkoms.v2.SrcNodeReq`
        """
        self._src_node = src_node

    @property
    def dst_node(self):
        """Gets the dst_node of this CreateTaskReq.

        :return: The dst_node of this CreateTaskReq.
        :rtype: :class:`huaweicloudsdkoms.v2.DstNodeReq`
        """
        return self._dst_node

    @dst_node.setter
    def dst_node(self, dst_node):
        """Sets the dst_node of this CreateTaskReq.

        :param dst_node: The dst_node of this CreateTaskReq.
        :type dst_node: :class:`huaweicloudsdkoms.v2.DstNodeReq`
        """
        self._dst_node = dst_node

    @property
    def enable_kms(self):
        """Gets the enable_kms of this CreateTaskReq.

        是否开启KMS加密，默认不开启。

        :return: The enable_kms of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        """Sets the enable_kms of this CreateTaskReq.

        是否开启KMS加密，默认不开启。

        :param enable_kms: The enable_kms of this CreateTaskReq.
        :type enable_kms: bool
        """
        self._enable_kms = enable_kms

    @property
    def description(self):
        """Gets the description of this CreateTaskReq.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :return: The description of this CreateTaskReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTaskReq.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :param description: The description of this CreateTaskReq.
        :type description: str
        """
        self._description = description

    @property
    def migrate_since(self):
        """Gets the migrate_since of this CreateTaskReq.

        以时间戳方式表示的迁移指定时间（单位：秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认不设置迁移指定时间。

        :return: The migrate_since of this CreateTaskReq.
        :rtype: int
        """
        return self._migrate_since

    @migrate_since.setter
    def migrate_since(self, migrate_since):
        """Sets the migrate_since of this CreateTaskReq.

        以时间戳方式表示的迁移指定时间（单位：秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认不设置迁移指定时间。

        :param migrate_since: The migrate_since of this CreateTaskReq.
        :type migrate_since: int
        """
        self._migrate_since = migrate_since

    @property
    def bandwidth_policy(self):
        """Gets the bandwidth_policy of this CreateTaskReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :return: The bandwidth_policy of this CreateTaskReq.
        :rtype: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        """Sets the bandwidth_policy of this CreateTaskReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :param bandwidth_policy: The bandwidth_policy of this CreateTaskReq.
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def source_cdn(self):
        """Gets the source_cdn of this CreateTaskReq.

        :return: The source_cdn of this CreateTaskReq.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        """Sets the source_cdn of this CreateTaskReq.

        :param source_cdn: The source_cdn of this CreateTaskReq.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        self._source_cdn = source_cdn

    @property
    def smn_config(self):
        """Gets the smn_config of this CreateTaskReq.

        :return: The smn_config of this CreateTaskReq.
        :rtype: :class:`huaweicloudsdkoms.v2.SmnConfig`
        """
        return self._smn_config

    @smn_config.setter
    def smn_config(self, smn_config):
        """Sets the smn_config of this CreateTaskReq.

        :param smn_config: The smn_config of this CreateTaskReq.
        :type smn_config: :class:`huaweicloudsdkoms.v2.SmnConfig`
        """
        self._smn_config = smn_config

    @property
    def enable_metadata_migration(self):
        """Gets the enable_metadata_migration of this CreateTaskReq.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :return: The enable_metadata_migration of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_metadata_migration

    @enable_metadata_migration.setter
    def enable_metadata_migration(self, enable_metadata_migration):
        """Sets the enable_metadata_migration of this CreateTaskReq.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :param enable_metadata_migration: The enable_metadata_migration of this CreateTaskReq.
        :type enable_metadata_migration: bool
        """
        self._enable_metadata_migration = enable_metadata_migration

    @property
    def enable_restore(self):
        """Gets the enable_restore of this CreateTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :return: The enable_restore of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        """Sets the enable_restore of this CreateTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :param enable_restore: The enable_restore of this CreateTaskReq.
        :type enable_restore: bool
        """
        self._enable_restore = enable_restore

    @property
    def enable_failed_object_recording(self):
        """Gets the enable_failed_object_recording of this CreateTaskReq.

        是否记录失败对象，默认开启。  开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :return: The enable_failed_object_recording of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_failed_object_recording

    @enable_failed_object_recording.setter
    def enable_failed_object_recording(self, enable_failed_object_recording):
        """Sets the enable_failed_object_recording of this CreateTaskReq.

        是否记录失败对象，默认开启。  开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :param enable_failed_object_recording: The enable_failed_object_recording of this CreateTaskReq.
        :type enable_failed_object_recording: bool
        """
        self._enable_failed_object_recording = enable_failed_object_recording

    @property
    def object_overwrite_mode(self):
        """Gets the object_overwrite_mode of this CreateTaskReq.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :return: The object_overwrite_mode of this CreateTaskReq.
        :rtype: str
        """
        return self._object_overwrite_mode

    @object_overwrite_mode.setter
    def object_overwrite_mode(self, object_overwrite_mode):
        """Sets the object_overwrite_mode of this CreateTaskReq.

        迁移前同名对象覆盖方式，用于迁移前判断源端与目的端有同名对象时，覆盖目的端或跳过迁移。默认SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE。 NO_OVERWRITE：不覆盖。迁移前源端对象与目的端对象同名时，不做对比直接跳过迁移。 SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE：大小/最后修改时间对比覆盖。默认配置。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象大小和最后修改时间，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。源端与目的端同名对象大小不相同，或目的端对象的最后修改时间晚于源端对象的最后修改时间(源端较新)，覆盖目的端。 CRC64_COMPARISON_OVERWRITE：CRC64对比覆盖。目前仅支持华为/阿里/腾讯。迁移前源端对象与目的端对象同名时，通过对比源端和目的端对象元数据中CRC64值是否相同，判断是否覆盖目的端，需满足源端/目的端对象的加密状态一致。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用SIZE_LAST_MODIFIED_COMPARISON_OVERWRITE(大小/最后修改时间对比覆盖)来对比进行覆盖判断。 FULL_OVERWRITE：全覆盖。迁移前源端对象与目的端对象同名时，不做对比覆盖目的端。

        :param object_overwrite_mode: The object_overwrite_mode of this CreateTaskReq.
        :type object_overwrite_mode: str
        """
        self._object_overwrite_mode = object_overwrite_mode

    @property
    def consistency_check(self):
        """Gets the consistency_check of this CreateTaskReq.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :return: The consistency_check of this CreateTaskReq.
        :rtype: str
        """
        return self._consistency_check

    @consistency_check.setter
    def consistency_check(self, consistency_check):
        """Sets the consistency_check of this CreateTaskReq.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象的最后修改时间不早于源端对象的最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 no_check：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :param consistency_check: The consistency_check of this CreateTaskReq.
        :type consistency_check: str
        """
        self._consistency_check = consistency_check

    @property
    def enable_requester_pays(self):
        """Gets the enable_requester_pays of this CreateTaskReq.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :return: The enable_requester_pays of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_requester_pays

    @enable_requester_pays.setter
    def enable_requester_pays(self, enable_requester_pays):
        """Sets the enable_requester_pays of this CreateTaskReq.

        是否开启请求者付款，在启用后，请求者支付请求和数据传输费用。

        :param enable_requester_pays: The enable_requester_pays of this CreateTaskReq.
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
        if not isinstance(other, CreateTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
