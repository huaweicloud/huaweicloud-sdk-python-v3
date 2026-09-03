# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBinlogTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'gmt_create': 'int',
        'gmt_modified': 'int',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'connection_id': 'str',
        'binlog_type': 'str',
        'file_name': 'str',
        'backup_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modified': 'gmt_modified',
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'connection_id': 'connection_id',
        'binlog_type': 'binlog_type',
        'file_name': 'file_name',
        'backup_id': 'backup_id',
        'status': 'status'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modified=None, tenant_id=None, tenant_name=None, user_id=None, user_name=None, connection_id=None, binlog_type=None, file_name=None, backup_id=None, status=None):
        r"""CreateBinlogTaskResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: int
        :param gmt_create: 任务创建时间，单位：毫秒
        :type gmt_create: int
        :param gmt_modified: 任务修改时间，单位：毫秒
        :type gmt_modified: int
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param connection_id: 连接ID
        :type connection_id: str
        :param binlog_type: binlog类型。取值范围：latest（最近日志）、backup（归档日志）
        :type binlog_type: str
        :param file_name: binlog文件名称
        :type file_name: str
        :param backup_id: 备份文件ID
        :type backup_id: str
        :param status: 任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）
        :type status: int
        """
        
        super().__init__()

        self._id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._tenant_id = None
        self._tenant_name = None
        self._user_id = None
        self._user_name = None
        self._connection_id = None
        self._binlog_type = None
        self._file_name = None
        self._backup_id = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modified is not None:
            self.gmt_modified = gmt_modified
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if connection_id is not None:
            self.connection_id = connection_id
        if binlog_type is not None:
            self.binlog_type = binlog_type
        if file_name is not None:
            self.file_name = file_name
        if backup_id is not None:
            self.backup_id = backup_id
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this CreateBinlogTaskResponse.

        任务ID

        :return: The id of this CreateBinlogTaskResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateBinlogTaskResponse.

        任务ID

        :param id: The id of this CreateBinlogTaskResponse.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        r"""Gets the gmt_create of this CreateBinlogTaskResponse.

        任务创建时间，单位：毫秒

        :return: The gmt_create of this CreateBinlogTaskResponse.
        :rtype: int
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        r"""Sets the gmt_create of this CreateBinlogTaskResponse.

        任务创建时间，单位：毫秒

        :param gmt_create: The gmt_create of this CreateBinlogTaskResponse.
        :type gmt_create: int
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modified(self):
        r"""Gets the gmt_modified of this CreateBinlogTaskResponse.

        任务修改时间，单位：毫秒

        :return: The gmt_modified of this CreateBinlogTaskResponse.
        :rtype: int
        """
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, gmt_modified):
        r"""Sets the gmt_modified of this CreateBinlogTaskResponse.

        任务修改时间，单位：毫秒

        :param gmt_modified: The gmt_modified of this CreateBinlogTaskResponse.
        :type gmt_modified: int
        """
        self._gmt_modified = gmt_modified

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateBinlogTaskResponse.

        租户ID

        :return: The tenant_id of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateBinlogTaskResponse.

        租户ID

        :param tenant_id: The tenant_id of this CreateBinlogTaskResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CreateBinlogTaskResponse.

        租户名称

        :return: The tenant_name of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CreateBinlogTaskResponse.

        租户名称

        :param tenant_name: The tenant_name of this CreateBinlogTaskResponse.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateBinlogTaskResponse.

        用户ID

        :return: The user_id of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateBinlogTaskResponse.

        用户ID

        :param user_id: The user_id of this CreateBinlogTaskResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateBinlogTaskResponse.

        用户名称

        :return: The user_name of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateBinlogTaskResponse.

        用户名称

        :param user_name: The user_name of this CreateBinlogTaskResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def connection_id(self):
        r"""Gets the connection_id of this CreateBinlogTaskResponse.

        连接ID

        :return: The connection_id of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this CreateBinlogTaskResponse.

        连接ID

        :param connection_id: The connection_id of this CreateBinlogTaskResponse.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def binlog_type(self):
        r"""Gets the binlog_type of this CreateBinlogTaskResponse.

        binlog类型。取值范围：latest（最近日志）、backup（归档日志）

        :return: The binlog_type of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._binlog_type

    @binlog_type.setter
    def binlog_type(self, binlog_type):
        r"""Sets the binlog_type of this CreateBinlogTaskResponse.

        binlog类型。取值范围：latest（最近日志）、backup（归档日志）

        :param binlog_type: The binlog_type of this CreateBinlogTaskResponse.
        :type binlog_type: str
        """
        self._binlog_type = binlog_type

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateBinlogTaskResponse.

        binlog文件名称

        :return: The file_name of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateBinlogTaskResponse.

        binlog文件名称

        :param file_name: The file_name of this CreateBinlogTaskResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def backup_id(self):
        r"""Gets the backup_id of this CreateBinlogTaskResponse.

        备份文件ID

        :return: The backup_id of this CreateBinlogTaskResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this CreateBinlogTaskResponse.

        备份文件ID

        :param backup_id: The backup_id of this CreateBinlogTaskResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def status(self):
        r"""Gets the status of this CreateBinlogTaskResponse.

        任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）

        :return: The status of this CreateBinlogTaskResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateBinlogTaskResponse.

        任务状态。取值范围：0（初始化）、1（运行中）、2（部分成功）、3（成功）、4（失败）、-1（已删除）

        :param status: The status of this CreateBinlogTaskResponse.
        :type status: int
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("CreateBinlogTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateBinlogTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
