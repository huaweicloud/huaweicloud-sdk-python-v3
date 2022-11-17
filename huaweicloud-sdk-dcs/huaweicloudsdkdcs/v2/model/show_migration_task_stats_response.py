# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigrationTaskStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_migration_progress': 'str',
        'offset': 'str',
        'source_dbsize': 'str',
        'target_dbsize': 'str',
        'target_input_kbps': 'str',
        'target_ops': 'str',
        'is_migrating': 'bool'
    }

    attribute_map = {
        'full_migration_progress': 'full_migration_progress',
        'offset': 'offset',
        'source_dbsize': 'source_dbsize',
        'target_dbsize': 'target_dbsize',
        'target_input_kbps': 'target_input_kbps',
        'target_ops': 'target_ops',
        'is_migrating': 'is_migrating'
    }

    def __init__(self, full_migration_progress=None, offset=None, source_dbsize=None, target_dbsize=None, target_input_kbps=None, target_ops=None, is_migrating=None):
        """ShowMigrationTaskStatsResponse

        The model defined in huaweicloud sdk

        :param full_migration_progress: 全量迁移进度百分比。
        :type full_migration_progress: str
        :param offset: 增量迁移偏移量。
        :type offset: str
        :param source_dbsize: 源redis键数量
        :type source_dbsize: str
        :param target_dbsize: 目标redis键数量
        :type target_dbsize: str
        :param target_input_kbps: 目标redis键写入流量，单位KB/s
        :type target_input_kbps: str
        :param target_ops: 目标redis每秒并发操作数
        :type target_ops: str
        :param is_migrating: 迁移任务是否在进行
        :type is_migrating: bool
        """
        
        super(ShowMigrationTaskStatsResponse, self).__init__()

        self._full_migration_progress = None
        self._offset = None
        self._source_dbsize = None
        self._target_dbsize = None
        self._target_input_kbps = None
        self._target_ops = None
        self._is_migrating = None
        self.discriminator = None

        if full_migration_progress is not None:
            self.full_migration_progress = full_migration_progress
        if offset is not None:
            self.offset = offset
        if source_dbsize is not None:
            self.source_dbsize = source_dbsize
        if target_dbsize is not None:
            self.target_dbsize = target_dbsize
        if target_input_kbps is not None:
            self.target_input_kbps = target_input_kbps
        if target_ops is not None:
            self.target_ops = target_ops
        if is_migrating is not None:
            self.is_migrating = is_migrating

    @property
    def full_migration_progress(self):
        """Gets the full_migration_progress of this ShowMigrationTaskStatsResponse.

        全量迁移进度百分比。

        :return: The full_migration_progress of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._full_migration_progress

    @full_migration_progress.setter
    def full_migration_progress(self, full_migration_progress):
        """Sets the full_migration_progress of this ShowMigrationTaskStatsResponse.

        全量迁移进度百分比。

        :param full_migration_progress: The full_migration_progress of this ShowMigrationTaskStatsResponse.
        :type full_migration_progress: str
        """
        self._full_migration_progress = full_migration_progress

    @property
    def offset(self):
        """Gets the offset of this ShowMigrationTaskStatsResponse.

        增量迁移偏移量。

        :return: The offset of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMigrationTaskStatsResponse.

        增量迁移偏移量。

        :param offset: The offset of this ShowMigrationTaskStatsResponse.
        :type offset: str
        """
        self._offset = offset

    @property
    def source_dbsize(self):
        """Gets the source_dbsize of this ShowMigrationTaskStatsResponse.

        源redis键数量

        :return: The source_dbsize of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._source_dbsize

    @source_dbsize.setter
    def source_dbsize(self, source_dbsize):
        """Sets the source_dbsize of this ShowMigrationTaskStatsResponse.

        源redis键数量

        :param source_dbsize: The source_dbsize of this ShowMigrationTaskStatsResponse.
        :type source_dbsize: str
        """
        self._source_dbsize = source_dbsize

    @property
    def target_dbsize(self):
        """Gets the target_dbsize of this ShowMigrationTaskStatsResponse.

        目标redis键数量

        :return: The target_dbsize of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._target_dbsize

    @target_dbsize.setter
    def target_dbsize(self, target_dbsize):
        """Sets the target_dbsize of this ShowMigrationTaskStatsResponse.

        目标redis键数量

        :param target_dbsize: The target_dbsize of this ShowMigrationTaskStatsResponse.
        :type target_dbsize: str
        """
        self._target_dbsize = target_dbsize

    @property
    def target_input_kbps(self):
        """Gets the target_input_kbps of this ShowMigrationTaskStatsResponse.

        目标redis键写入流量，单位KB/s

        :return: The target_input_kbps of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._target_input_kbps

    @target_input_kbps.setter
    def target_input_kbps(self, target_input_kbps):
        """Sets the target_input_kbps of this ShowMigrationTaskStatsResponse.

        目标redis键写入流量，单位KB/s

        :param target_input_kbps: The target_input_kbps of this ShowMigrationTaskStatsResponse.
        :type target_input_kbps: str
        """
        self._target_input_kbps = target_input_kbps

    @property
    def target_ops(self):
        """Gets the target_ops of this ShowMigrationTaskStatsResponse.

        目标redis每秒并发操作数

        :return: The target_ops of this ShowMigrationTaskStatsResponse.
        :rtype: str
        """
        return self._target_ops

    @target_ops.setter
    def target_ops(self, target_ops):
        """Sets the target_ops of this ShowMigrationTaskStatsResponse.

        目标redis每秒并发操作数

        :param target_ops: The target_ops of this ShowMigrationTaskStatsResponse.
        :type target_ops: str
        """
        self._target_ops = target_ops

    @property
    def is_migrating(self):
        """Gets the is_migrating of this ShowMigrationTaskStatsResponse.

        迁移任务是否在进行

        :return: The is_migrating of this ShowMigrationTaskStatsResponse.
        :rtype: bool
        """
        return self._is_migrating

    @is_migrating.setter
    def is_migrating(self, is_migrating):
        """Sets the is_migrating of this ShowMigrationTaskStatsResponse.

        迁移任务是否在进行

        :param is_migrating: The is_migrating of this ShowMigrationTaskStatsResponse.
        :type is_migrating: bool
        """
        self._is_migrating = is_migrating

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
        if not isinstance(other, ShowMigrationTaskStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
