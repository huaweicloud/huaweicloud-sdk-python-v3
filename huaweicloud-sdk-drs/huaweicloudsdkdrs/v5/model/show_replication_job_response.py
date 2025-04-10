# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplicationJobResponse(SdkResponse):

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
        'status': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'backup_info': 'BackupInfoResp',
        'base_info': 'BackupJobBaseInfo',
        'target_db_info': 'BackupJobEndpointInfo',
        'options': 'BackupRestoreOptionInfo',
        'new_db_names': 'str',
        'instance_name': 'str',
        'error_log': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'backup_info': 'backup_info',
        'base_info': 'base_info',
        'target_db_info': 'target_db_info',
        'options': 'options',
        'new_db_names': 'new_db_names',
        'instance_name': 'instance_name',
        'error_log': 'error_log'
    }

    def __init__(self, id=None, status=None, create_time=None, finish_time=None, backup_info=None, base_info=None, target_db_info=None, options=None, new_db_names=None, instance_name=None, error_log=None):
        r"""ShowReplicationJobResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param finish_time: 任务完成时间。
        :type finish_time: str
        :param backup_info: 
        :type backup_info: :class:`huaweicloudsdkdrs.v5.BackupInfoResp`
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        :param target_db_info: 
        :type target_db_info: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        :param options: 
        :type options: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        :param new_db_names: 备份恢复数据库映射新名称。
        :type new_db_names: str
        :param instance_name: RDS实例名称。
        :type instance_name: str
        :param error_log: 迁移过程中失败原因。
        :type error_log: str
        """
        
        super(ShowReplicationJobResponse, self).__init__()

        self._id = None
        self._status = None
        self._create_time = None
        self._finish_time = None
        self._backup_info = None
        self._base_info = None
        self._target_db_info = None
        self._options = None
        self._new_db_names = None
        self._instance_name = None
        self._error_log = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if backup_info is not None:
            self.backup_info = backup_info
        if base_info is not None:
            self.base_info = base_info
        if target_db_info is not None:
            self.target_db_info = target_db_info
        if options is not None:
            self.options = options
        if new_db_names is not None:
            self.new_db_names = new_db_names
        if instance_name is not None:
            self.instance_name = instance_name
        if error_log is not None:
            self.error_log = error_log

    @property
    def id(self):
        r"""Gets the id of this ShowReplicationJobResponse.

        任务ID。

        :return: The id of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowReplicationJobResponse.

        任务ID。

        :param id: The id of this ShowReplicationJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowReplicationJobResponse.

        任务状态。

        :return: The status of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowReplicationJobResponse.

        任务状态。

        :param status: The status of this ShowReplicationJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowReplicationJobResponse.

        任务创建时间。

        :return: The create_time of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowReplicationJobResponse.

        任务创建时间。

        :param create_time: The create_time of this ShowReplicationJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this ShowReplicationJobResponse.

        任务完成时间。

        :return: The finish_time of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this ShowReplicationJobResponse.

        任务完成时间。

        :param finish_time: The finish_time of this ShowReplicationJobResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def backup_info(self):
        r"""Gets the backup_info of this ShowReplicationJobResponse.

        :return: The backup_info of this ShowReplicationJobResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupInfoResp`
        """
        return self._backup_info

    @backup_info.setter
    def backup_info(self, backup_info):
        r"""Sets the backup_info of this ShowReplicationJobResponse.

        :param backup_info: The backup_info of this ShowReplicationJobResponse.
        :type backup_info: :class:`huaweicloudsdkdrs.v5.BackupInfoResp`
        """
        self._backup_info = backup_info

    @property
    def base_info(self):
        r"""Gets the base_info of this ShowReplicationJobResponse.

        :return: The base_info of this ShowReplicationJobResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ShowReplicationJobResponse.

        :param base_info: The base_info of this ShowReplicationJobResponse.
        :type base_info: :class:`huaweicloudsdkdrs.v5.BackupJobBaseInfo`
        """
        self._base_info = base_info

    @property
    def target_db_info(self):
        r"""Gets the target_db_info of this ShowReplicationJobResponse.

        :return: The target_db_info of this ShowReplicationJobResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        """
        return self._target_db_info

    @target_db_info.setter
    def target_db_info(self, target_db_info):
        r"""Sets the target_db_info of this ShowReplicationJobResponse.

        :param target_db_info: The target_db_info of this ShowReplicationJobResponse.
        :type target_db_info: :class:`huaweicloudsdkdrs.v5.BackupJobEndpointInfo`
        """
        self._target_db_info = target_db_info

    @property
    def options(self):
        r"""Gets the options of this ShowReplicationJobResponse.

        :return: The options of this ShowReplicationJobResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ShowReplicationJobResponse.

        :param options: The options of this ShowReplicationJobResponse.
        :type options: :class:`huaweicloudsdkdrs.v5.BackupRestoreOptionInfo`
        """
        self._options = options

    @property
    def new_db_names(self):
        r"""Gets the new_db_names of this ShowReplicationJobResponse.

        备份恢复数据库映射新名称。

        :return: The new_db_names of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._new_db_names

    @new_db_names.setter
    def new_db_names(self, new_db_names):
        r"""Sets the new_db_names of this ShowReplicationJobResponse.

        备份恢复数据库映射新名称。

        :param new_db_names: The new_db_names of this ShowReplicationJobResponse.
        :type new_db_names: str
        """
        self._new_db_names = new_db_names

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowReplicationJobResponse.

        RDS实例名称。

        :return: The instance_name of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowReplicationJobResponse.

        RDS实例名称。

        :param instance_name: The instance_name of this ShowReplicationJobResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def error_log(self):
        r"""Gets the error_log of this ShowReplicationJobResponse.

        迁移过程中失败原因。

        :return: The error_log of this ShowReplicationJobResponse.
        :rtype: str
        """
        return self._error_log

    @error_log.setter
    def error_log(self, error_log):
        r"""Sets the error_log of this ShowReplicationJobResponse.

        迁移过程中失败原因。

        :param error_log: The error_log of this ShowReplicationJobResponse.
        :type error_log: str
        """
        self._error_log = error_log

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
        if not isinstance(other, ShowReplicationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
