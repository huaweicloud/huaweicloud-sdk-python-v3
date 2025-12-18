# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rate_limit': 'int',
        'prefetch_block': 'int',
        'file_split_size': 'int',
        'enable_standby_backup': 'bool',
        'close_compression': 'bool',
        'default_backup_media_type': 'str',
        'default_backup_method': 'str',
        'backup_parallel_degree': 'int',
        'backup_node_info': 'BackupNodeInfoResult'
    }

    attribute_map = {
        'rate_limit': 'rate_limit',
        'prefetch_block': 'prefetch_block',
        'file_split_size': 'file_split_size',
        'enable_standby_backup': 'enable_standby_backup',
        'close_compression': 'close_compression',
        'default_backup_media_type': 'default_backup_media_type',
        'default_backup_method': 'default_backup_method',
        'backup_parallel_degree': 'backup_parallel_degree',
        'backup_node_info': 'backup_node_info'
    }

    def __init__(self, rate_limit=None, prefetch_block=None, file_split_size=None, enable_standby_backup=None, close_compression=None, default_backup_media_type=None, default_backup_method=None, backup_parallel_degree=None, backup_node_info=None):
        r"""ShowConfigurationResponse

        The model defined in huaweicloud sdk

        :param rate_limit: **参数解释**: 备份限速。 **取值范围**: 0-1024
        :type rate_limit: int
        :param prefetch_block: **参数解释**: 增备预取页面个数。 **取值范围**: 1-8192
        :type prefetch_block: int
        :param file_split_size: **参数解释**: 分片大小。 **取值范围**: 0-1024
        :type file_split_size: int
        :param enable_standby_backup: **参数解释**: 启用备机备份标识。 **取值范围**: 不涉及。
        :type enable_standby_backup: bool
        :param close_compression: **参数解释**: 是否关闭压缩。 **取值范围**: true,false
        :type close_compression: bool
        :param default_backup_media_type: **参数解释**: 默认备份介质。 **取值范围**: - OBS 对象存储
        :type default_backup_media_type: str
        :param default_backup_method: **参数解释**: 默认备份方式。 **取值范围**: - EBACKUP 快照备份 - PHYSICAL_BACKUP 物理备份
        :type default_backup_method: str
        :param backup_parallel_degree: **参数解释**: 备份并行参数。 **取值范围**: 1, 2, 4, 8
        :type backup_parallel_degree: int
        :param backup_node_info: 
        :type backup_node_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupNodeInfoResult`
        """
        
        super().__init__()

        self._rate_limit = None
        self._prefetch_block = None
        self._file_split_size = None
        self._enable_standby_backup = None
        self._close_compression = None
        self._default_backup_media_type = None
        self._default_backup_method = None
        self._backup_parallel_degree = None
        self._backup_node_info = None
        self.discriminator = None

        if rate_limit is not None:
            self.rate_limit = rate_limit
        if prefetch_block is not None:
            self.prefetch_block = prefetch_block
        if file_split_size is not None:
            self.file_split_size = file_split_size
        if enable_standby_backup is not None:
            self.enable_standby_backup = enable_standby_backup
        if close_compression is not None:
            self.close_compression = close_compression
        if default_backup_media_type is not None:
            self.default_backup_media_type = default_backup_media_type
        if default_backup_method is not None:
            self.default_backup_method = default_backup_method
        if backup_parallel_degree is not None:
            self.backup_parallel_degree = backup_parallel_degree
        if backup_node_info is not None:
            self.backup_node_info = backup_node_info

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this ShowConfigurationResponse.

        **参数解释**: 备份限速。 **取值范围**: 0-1024

        :return: The rate_limit of this ShowConfigurationResponse.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this ShowConfigurationResponse.

        **参数解释**: 备份限速。 **取值范围**: 0-1024

        :param rate_limit: The rate_limit of this ShowConfigurationResponse.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def prefetch_block(self):
        r"""Gets the prefetch_block of this ShowConfigurationResponse.

        **参数解释**: 增备预取页面个数。 **取值范围**: 1-8192

        :return: The prefetch_block of this ShowConfigurationResponse.
        :rtype: int
        """
        return self._prefetch_block

    @prefetch_block.setter
    def prefetch_block(self, prefetch_block):
        r"""Sets the prefetch_block of this ShowConfigurationResponse.

        **参数解释**: 增备预取页面个数。 **取值范围**: 1-8192

        :param prefetch_block: The prefetch_block of this ShowConfigurationResponse.
        :type prefetch_block: int
        """
        self._prefetch_block = prefetch_block

    @property
    def file_split_size(self):
        r"""Gets the file_split_size of this ShowConfigurationResponse.

        **参数解释**: 分片大小。 **取值范围**: 0-1024

        :return: The file_split_size of this ShowConfigurationResponse.
        :rtype: int
        """
        return self._file_split_size

    @file_split_size.setter
    def file_split_size(self, file_split_size):
        r"""Sets the file_split_size of this ShowConfigurationResponse.

        **参数解释**: 分片大小。 **取值范围**: 0-1024

        :param file_split_size: The file_split_size of this ShowConfigurationResponse.
        :type file_split_size: int
        """
        self._file_split_size = file_split_size

    @property
    def enable_standby_backup(self):
        r"""Gets the enable_standby_backup of this ShowConfigurationResponse.

        **参数解释**: 启用备机备份标识。 **取值范围**: 不涉及。

        :return: The enable_standby_backup of this ShowConfigurationResponse.
        :rtype: bool
        """
        return self._enable_standby_backup

    @enable_standby_backup.setter
    def enable_standby_backup(self, enable_standby_backup):
        r"""Sets the enable_standby_backup of this ShowConfigurationResponse.

        **参数解释**: 启用备机备份标识。 **取值范围**: 不涉及。

        :param enable_standby_backup: The enable_standby_backup of this ShowConfigurationResponse.
        :type enable_standby_backup: bool
        """
        self._enable_standby_backup = enable_standby_backup

    @property
    def close_compression(self):
        r"""Gets the close_compression of this ShowConfigurationResponse.

        **参数解释**: 是否关闭压缩。 **取值范围**: true,false

        :return: The close_compression of this ShowConfigurationResponse.
        :rtype: bool
        """
        return self._close_compression

    @close_compression.setter
    def close_compression(self, close_compression):
        r"""Sets the close_compression of this ShowConfigurationResponse.

        **参数解释**: 是否关闭压缩。 **取值范围**: true,false

        :param close_compression: The close_compression of this ShowConfigurationResponse.
        :type close_compression: bool
        """
        self._close_compression = close_compression

    @property
    def default_backup_media_type(self):
        r"""Gets the default_backup_media_type of this ShowConfigurationResponse.

        **参数解释**: 默认备份介质。 **取值范围**: - OBS 对象存储

        :return: The default_backup_media_type of this ShowConfigurationResponse.
        :rtype: str
        """
        return self._default_backup_media_type

    @default_backup_media_type.setter
    def default_backup_media_type(self, default_backup_media_type):
        r"""Sets the default_backup_media_type of this ShowConfigurationResponse.

        **参数解释**: 默认备份介质。 **取值范围**: - OBS 对象存储

        :param default_backup_media_type: The default_backup_media_type of this ShowConfigurationResponse.
        :type default_backup_media_type: str
        """
        self._default_backup_media_type = default_backup_media_type

    @property
    def default_backup_method(self):
        r"""Gets the default_backup_method of this ShowConfigurationResponse.

        **参数解释**: 默认备份方式。 **取值范围**: - EBACKUP 快照备份 - PHYSICAL_BACKUP 物理备份

        :return: The default_backup_method of this ShowConfigurationResponse.
        :rtype: str
        """
        return self._default_backup_method

    @default_backup_method.setter
    def default_backup_method(self, default_backup_method):
        r"""Sets the default_backup_method of this ShowConfigurationResponse.

        **参数解释**: 默认备份方式。 **取值范围**: - EBACKUP 快照备份 - PHYSICAL_BACKUP 物理备份

        :param default_backup_method: The default_backup_method of this ShowConfigurationResponse.
        :type default_backup_method: str
        """
        self._default_backup_method = default_backup_method

    @property
    def backup_parallel_degree(self):
        r"""Gets the backup_parallel_degree of this ShowConfigurationResponse.

        **参数解释**: 备份并行参数。 **取值范围**: 1, 2, 4, 8

        :return: The backup_parallel_degree of this ShowConfigurationResponse.
        :rtype: int
        """
        return self._backup_parallel_degree

    @backup_parallel_degree.setter
    def backup_parallel_degree(self, backup_parallel_degree):
        r"""Sets the backup_parallel_degree of this ShowConfigurationResponse.

        **参数解释**: 备份并行参数。 **取值范围**: 1, 2, 4, 8

        :param backup_parallel_degree: The backup_parallel_degree of this ShowConfigurationResponse.
        :type backup_parallel_degree: int
        """
        self._backup_parallel_degree = backup_parallel_degree

    @property
    def backup_node_info(self):
        r"""Gets the backup_node_info of this ShowConfigurationResponse.

        :return: The backup_node_info of this ShowConfigurationResponse.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupNodeInfoResult`
        """
        return self._backup_node_info

    @backup_node_info.setter
    def backup_node_info(self, backup_node_info):
        r"""Sets the backup_node_info of this ShowConfigurationResponse.

        :param backup_node_info: The backup_node_info of this ShowConfigurationResponse.
        :type backup_node_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.BackupNodeInfoResult`
        """
        self._backup_node_info = backup_node_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowConfigurationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
