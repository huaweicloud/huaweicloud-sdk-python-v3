# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupJobEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'ms_file_stream_status': 'str',
        'file_id': 'str'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'ms_file_stream_status': 'ms_file_stream_status',
        'file_id': 'file_id'
    }

    def __init__(self, target_instance_id=None, ms_file_stream_status=None, file_id=None):
        r"""BackupJobEndpointInfo

        The model defined in huaweicloud sdk

        :param target_instance_id: 备份迁移任务恢复目标RDS for SQL Server实例ID。
        :type target_instance_id: str
        :param ms_file_stream_status: 目标实例是否开启FileStream模式。可通过RDS for SQL Server详情接口获取。
        :type ms_file_stream_status: str
        :param file_id: RDS for SQL Server备份文件的文件ID，通过RDS全量恢复时必填。可通过云数据库RDS备份管理页面获取。
        :type file_id: str
        """
        
        

        self._target_instance_id = None
        self._ms_file_stream_status = None
        self._file_id = None
        self.discriminator = None

        self.target_instance_id = target_instance_id
        if ms_file_stream_status is not None:
            self.ms_file_stream_status = ms_file_stream_status
        if file_id is not None:
            self.file_id = file_id

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this BackupJobEndpointInfo.

        备份迁移任务恢复目标RDS for SQL Server实例ID。

        :return: The target_instance_id of this BackupJobEndpointInfo.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this BackupJobEndpointInfo.

        备份迁移任务恢复目标RDS for SQL Server实例ID。

        :param target_instance_id: The target_instance_id of this BackupJobEndpointInfo.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def ms_file_stream_status(self):
        r"""Gets the ms_file_stream_status of this BackupJobEndpointInfo.

        目标实例是否开启FileStream模式。可通过RDS for SQL Server详情接口获取。

        :return: The ms_file_stream_status of this BackupJobEndpointInfo.
        :rtype: str
        """
        return self._ms_file_stream_status

    @ms_file_stream_status.setter
    def ms_file_stream_status(self, ms_file_stream_status):
        r"""Sets the ms_file_stream_status of this BackupJobEndpointInfo.

        目标实例是否开启FileStream模式。可通过RDS for SQL Server详情接口获取。

        :param ms_file_stream_status: The ms_file_stream_status of this BackupJobEndpointInfo.
        :type ms_file_stream_status: str
        """
        self._ms_file_stream_status = ms_file_stream_status

    @property
    def file_id(self):
        r"""Gets the file_id of this BackupJobEndpointInfo.

        RDS for SQL Server备份文件的文件ID，通过RDS全量恢复时必填。可通过云数据库RDS备份管理页面获取。

        :return: The file_id of this BackupJobEndpointInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this BackupJobEndpointInfo.

        RDS for SQL Server备份文件的文件ID，通过RDS全量恢复时必填。可通过云数据库RDS备份管理页面获取。

        :param file_id: The file_id of this BackupJobEndpointInfo.
        :type file_id: str
        """
        self._file_id = file_id

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
        if not isinstance(other, BackupJobEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
