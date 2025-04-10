# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSyncTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_cloud_type': 'str',
        'src_region': 'str',
        'src_bucket': 'str',
        'src_ak': 'str',
        'src_sk': 'str',
        'dst_ak': 'str',
        'dst_sk': 'str',
        'dst_region': 'str',
        'dst_bucket': 'str',
        'description': 'str',
        'enable_metadata_migration': 'bool',
        'enable_kms': 'bool',
        'enable_restore': 'bool',
        'dst_storage_policy': 'str',
        'app_id': 'str',
        'source_cdn': 'SourceCdnReq',
        'consistency_check': 'str'
    }

    attribute_map = {
        'src_cloud_type': 'src_cloud_type',
        'src_region': 'src_region',
        'src_bucket': 'src_bucket',
        'src_ak': 'src_ak',
        'src_sk': 'src_sk',
        'dst_ak': 'dst_ak',
        'dst_sk': 'dst_sk',
        'dst_region': 'dst_region',
        'dst_bucket': 'dst_bucket',
        'description': 'description',
        'enable_metadata_migration': 'enable_metadata_migration',
        'enable_kms': 'enable_kms',
        'enable_restore': 'enable_restore',
        'dst_storage_policy': 'dst_storage_policy',
        'app_id': 'app_id',
        'source_cdn': 'source_cdn',
        'consistency_check': 'consistency_check'
    }

    def __init__(self, src_cloud_type=None, src_region=None, src_bucket=None, src_ak=None, src_sk=None, dst_ak=None, dst_sk=None, dst_region=None, dst_bucket=None, description=None, enable_metadata_migration=None, enable_kms=None, enable_restore=None, dst_storage_policy=None, app_id=None, source_cdn=None, consistency_check=None):
        r"""CreateSyncTaskReq

        The model defined in huaweicloud sdk

        :param src_cloud_type: 源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、Cloud。默认值为Aliyun。
        :type src_cloud_type: str
        :param src_region: 源端桶所处的区域
        :type src_region: str
        :param src_bucket: 源端桶名
        :type src_bucket: str
        :param src_ak: 源端桶的AK（最大长度100个字符）。
        :type src_ak: str
        :param src_sk: 源端桶的SK（最大长度100个字符）。
        :type src_sk: str
        :param dst_ak: 目的端桶的AK（最大长度100个字符）。
        :type dst_ak: str
        :param dst_sk: 目的端桶的SK（最大长度100个字符）。
        :type dst_sk: str
        :param dst_region: 目的端region
        :type dst_region: str
        :param dst_bucket: 目的端桶名
        :type dst_bucket: str
        :param description: 任务描述，不能超过255个字符，且不能包含&lt;&gt;()\&quot;&#39;&amp;等特殊字符。
        :type description: str
        :param enable_metadata_migration: 是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。
        :type enable_metadata_migration: bool
        :param enable_kms: 是否开启KMS加密，默认不开启。
        :type enable_kms: bool
        :param enable_restore: 是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。
        :type enable_restore: bool
        :param dst_storage_policy: 目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型
        :type dst_storage_policy: str
        :param app_id: 当源端为腾讯云时，需要填写此参数。
        :type app_id: str
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        :param consistency_check: 一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象最后修改时间晚于源端对象最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 transmission：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。
        :type consistency_check: str
        """
        
        

        self._src_cloud_type = None
        self._src_region = None
        self._src_bucket = None
        self._src_ak = None
        self._src_sk = None
        self._dst_ak = None
        self._dst_sk = None
        self._dst_region = None
        self._dst_bucket = None
        self._description = None
        self._enable_metadata_migration = None
        self._enable_kms = None
        self._enable_restore = None
        self._dst_storage_policy = None
        self._app_id = None
        self._source_cdn = None
        self._consistency_check = None
        self.discriminator = None

        if src_cloud_type is not None:
            self.src_cloud_type = src_cloud_type
        self.src_region = src_region
        self.src_bucket = src_bucket
        self.src_ak = src_ak
        self.src_sk = src_sk
        self.dst_ak = dst_ak
        self.dst_sk = dst_sk
        self.dst_region = dst_region
        self.dst_bucket = dst_bucket
        if description is not None:
            self.description = description
        if enable_metadata_migration is not None:
            self.enable_metadata_migration = enable_metadata_migration
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if dst_storage_policy is not None:
            self.dst_storage_policy = dst_storage_policy
        if app_id is not None:
            self.app_id = app_id
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if consistency_check is not None:
            self.consistency_check = consistency_check

    @property
    def src_cloud_type(self):
        r"""Gets the src_cloud_type of this CreateSyncTaskReq.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、Cloud。默认值为Aliyun。

        :return: The src_cloud_type of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._src_cloud_type

    @src_cloud_type.setter
    def src_cloud_type(self, src_cloud_type):
        r"""Sets the src_cloud_type of this CreateSyncTaskReq.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、Cloud。默认值为Aliyun。

        :param src_cloud_type: The src_cloud_type of this CreateSyncTaskReq.
        :type src_cloud_type: str
        """
        self._src_cloud_type = src_cloud_type

    @property
    def src_region(self):
        r"""Gets the src_region of this CreateSyncTaskReq.

        源端桶所处的区域

        :return: The src_region of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._src_region

    @src_region.setter
    def src_region(self, src_region):
        r"""Sets the src_region of this CreateSyncTaskReq.

        源端桶所处的区域

        :param src_region: The src_region of this CreateSyncTaskReq.
        :type src_region: str
        """
        self._src_region = src_region

    @property
    def src_bucket(self):
        r"""Gets the src_bucket of this CreateSyncTaskReq.

        源端桶名

        :return: The src_bucket of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._src_bucket

    @src_bucket.setter
    def src_bucket(self, src_bucket):
        r"""Sets the src_bucket of this CreateSyncTaskReq.

        源端桶名

        :param src_bucket: The src_bucket of this CreateSyncTaskReq.
        :type src_bucket: str
        """
        self._src_bucket = src_bucket

    @property
    def src_ak(self):
        r"""Gets the src_ak of this CreateSyncTaskReq.

        源端桶的AK（最大长度100个字符）。

        :return: The src_ak of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._src_ak

    @src_ak.setter
    def src_ak(self, src_ak):
        r"""Sets the src_ak of this CreateSyncTaskReq.

        源端桶的AK（最大长度100个字符）。

        :param src_ak: The src_ak of this CreateSyncTaskReq.
        :type src_ak: str
        """
        self._src_ak = src_ak

    @property
    def src_sk(self):
        r"""Gets the src_sk of this CreateSyncTaskReq.

        源端桶的SK（最大长度100个字符）。

        :return: The src_sk of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._src_sk

    @src_sk.setter
    def src_sk(self, src_sk):
        r"""Sets the src_sk of this CreateSyncTaskReq.

        源端桶的SK（最大长度100个字符）。

        :param src_sk: The src_sk of this CreateSyncTaskReq.
        :type src_sk: str
        """
        self._src_sk = src_sk

    @property
    def dst_ak(self):
        r"""Gets the dst_ak of this CreateSyncTaskReq.

        目的端桶的AK（最大长度100个字符）。

        :return: The dst_ak of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._dst_ak

    @dst_ak.setter
    def dst_ak(self, dst_ak):
        r"""Sets the dst_ak of this CreateSyncTaskReq.

        目的端桶的AK（最大长度100个字符）。

        :param dst_ak: The dst_ak of this CreateSyncTaskReq.
        :type dst_ak: str
        """
        self._dst_ak = dst_ak

    @property
    def dst_sk(self):
        r"""Gets the dst_sk of this CreateSyncTaskReq.

        目的端桶的SK（最大长度100个字符）。

        :return: The dst_sk of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._dst_sk

    @dst_sk.setter
    def dst_sk(self, dst_sk):
        r"""Sets the dst_sk of this CreateSyncTaskReq.

        目的端桶的SK（最大长度100个字符）。

        :param dst_sk: The dst_sk of this CreateSyncTaskReq.
        :type dst_sk: str
        """
        self._dst_sk = dst_sk

    @property
    def dst_region(self):
        r"""Gets the dst_region of this CreateSyncTaskReq.

        目的端region

        :return: The dst_region of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._dst_region

    @dst_region.setter
    def dst_region(self, dst_region):
        r"""Sets the dst_region of this CreateSyncTaskReq.

        目的端region

        :param dst_region: The dst_region of this CreateSyncTaskReq.
        :type dst_region: str
        """
        self._dst_region = dst_region

    @property
    def dst_bucket(self):
        r"""Gets the dst_bucket of this CreateSyncTaskReq.

        目的端桶名

        :return: The dst_bucket of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._dst_bucket

    @dst_bucket.setter
    def dst_bucket(self, dst_bucket):
        r"""Sets the dst_bucket of this CreateSyncTaskReq.

        目的端桶名

        :param dst_bucket: The dst_bucket of this CreateSyncTaskReq.
        :type dst_bucket: str
        """
        self._dst_bucket = dst_bucket

    @property
    def description(self):
        r"""Gets the description of this CreateSyncTaskReq.

        任务描述，不能超过255个字符，且不能包含<>()\"'&等特殊字符。

        :return: The description of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSyncTaskReq.

        任务描述，不能超过255个字符，且不能包含<>()\"'&等特殊字符。

        :param description: The description of this CreateSyncTaskReq.
        :type description: str
        """
        self._description = description

    @property
    def enable_metadata_migration(self):
        r"""Gets the enable_metadata_migration of this CreateSyncTaskReq.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :return: The enable_metadata_migration of this CreateSyncTaskReq.
        :rtype: bool
        """
        return self._enable_metadata_migration

    @enable_metadata_migration.setter
    def enable_metadata_migration(self, enable_metadata_migration):
        r"""Sets the enable_metadata_migration of this CreateSyncTaskReq.

        是否启用元数据迁移，默认否。不启用时，为保证迁移任务正常运行，仍将为您迁移ContentType元数据。

        :param enable_metadata_migration: The enable_metadata_migration of this CreateSyncTaskReq.
        :type enable_metadata_migration: bool
        """
        self._enable_metadata_migration = enable_metadata_migration

    @property
    def enable_kms(self):
        r"""Gets the enable_kms of this CreateSyncTaskReq.

        是否开启KMS加密，默认不开启。

        :return: The enable_kms of this CreateSyncTaskReq.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        r"""Sets the enable_kms of this CreateSyncTaskReq.

        是否开启KMS加密，默认不开启。

        :param enable_kms: The enable_kms of this CreateSyncTaskReq.
        :type enable_kms: bool
        """
        self._enable_kms = enable_kms

    @property
    def enable_restore(self):
        r"""Gets the enable_restore of this CreateSyncTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :return: The enable_restore of this CreateSyncTaskReq.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        r"""Sets the enable_restore of this CreateSyncTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :param enable_restore: The enable_restore of this CreateSyncTaskReq.
        :type enable_restore: bool
        """
        self._enable_restore = enable_restore

    @property
    def dst_storage_policy(self):
        r"""Gets the dst_storage_policy of this CreateSyncTaskReq.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :return: The dst_storage_policy of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._dst_storage_policy

    @dst_storage_policy.setter
    def dst_storage_policy(self, dst_storage_policy):
        r"""Sets the dst_storage_policy of this CreateSyncTaskReq.

        目的端存储类型设置，当且仅当目的端为华为云OBS时需要，默认为标准存储 STANDARD：华为云OBS标准存储 IA：华为云OBS低频存储 ARCHIVE：华为云OBS归档存储 DEEP_ARCHIVE：华为云OBS深度归档存储 SRC_STORAGE_MAPPING：保留源端存储类型，将源端存储类型映射为华为云OBS存储类型

        :param dst_storage_policy: The dst_storage_policy of this CreateSyncTaskReq.
        :type dst_storage_policy: str
        """
        self._dst_storage_policy = dst_storage_policy

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateSyncTaskReq.

        当源端为腾讯云时，需要填写此参数。

        :return: The app_id of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateSyncTaskReq.

        当源端为腾讯云时，需要填写此参数。

        :param app_id: The app_id of this CreateSyncTaskReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def source_cdn(self):
        r"""Gets the source_cdn of this CreateSyncTaskReq.

        :return: The source_cdn of this CreateSyncTaskReq.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        r"""Sets the source_cdn of this CreateSyncTaskReq.

        :param source_cdn: The source_cdn of this CreateSyncTaskReq.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        self._source_cdn = source_cdn

    @property
    def consistency_check(self):
        r"""Gets the consistency_check of this CreateSyncTaskReq.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象最后修改时间晚于源端对象最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 transmission：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :return: The consistency_check of this CreateSyncTaskReq.
        :rtype: str
        """
        return self._consistency_check

    @consistency_check.setter
    def consistency_check(self, consistency_check):
        r"""Sets the consistency_check of this CreateSyncTaskReq.

        一致性校验方式，用于迁移前/后校验对象是否一致，所有校验方式需满足源端/目的端对象的加密状态一致，具体校验方式和校验结果可通过对象列表查看。默认size_last_modified。 size_last_modified：默认配置。迁移前后，通过对比源端和目的端对象大小+最后修改时间，判断对象是否已存在或迁移后数据是否完整。源端与目的端同名对象大小相同，且目的端对象最后修改时间晚于源端对象最后修改时间，则代表该对象已存在/迁移成功。 crc64：目前仅支持华为/阿里/腾讯。迁移前后，通过对比源端和目的端对象元数据中CRC64值是否相同，判断对象是否已存在/迁移完成。如果源端与目的端对象元数据中不存在CRC64值，则系统会默认使用大小/最后修改时间校验方式来校验。 transmission：目前仅支持HTTP/HTTPS数据源。当源端对象无法通过标准http协议中content-length字段获取数据大小时，默认数据下载成功即迁移成功，不对数据做额外校验，且迁移时源端对象默认覆盖目的端同名对象。当源端对象能正常通过标准http协议中content-length字段获取数据大小时，则采用大小/最后修改时间校验方式来校验。

        :param consistency_check: The consistency_check of this CreateSyncTaskReq.
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
        if not isinstance(other, CreateSyncTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
