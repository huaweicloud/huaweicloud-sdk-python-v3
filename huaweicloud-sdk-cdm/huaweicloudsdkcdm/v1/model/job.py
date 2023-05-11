# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'from_connector_name': 'str',
        'to_config_values': 'ConfigValues',
        'to_link_name': 'str',
        'driver_config_values': 'ConfigValues',
        'from_config_values': 'ConfigValues',
        'to_connector_name': 'str',
        'name': 'str',
        'from_link_name': 'str',
        'creation_user': 'str',
        'creation_date': 'int',
        'update_date': 'int',
        'is_incre_job': 'bool',
        'flag': 'int',
        'files_read': 'int',
        'update_user': 'str',
        'external_id': 'str',
        'type': 'str',
        'execute_start_date': 'int',
        'delete_rows': 'int',
        'enabled': 'bool',
        'bytes_written': 'int',
        'id': 'int',
        'is_use_sql': 'bool',
        'update_rows': 'int',
        'group_name': 'str',
        'bytes_read': 'int',
        'execute_update_date': 'int',
        'write_rows': 'int',
        'rows_written': 'int',
        'rows_read': 'int',
        'files_written': 'int',
        'is_incrementing': 'bool',
        'execute_create_date': 'int',
        'status': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'from_connector_name': 'from-connector-name',
        'to_config_values': 'to-config-values',
        'to_link_name': 'to-link-name',
        'driver_config_values': 'driver-config-values',
        'from_config_values': 'from-config-values',
        'to_connector_name': 'to-connector-name',
        'name': 'name',
        'from_link_name': 'from-link-name',
        'creation_user': 'creation-user',
        'creation_date': 'creation-date',
        'update_date': 'update-date',
        'is_incre_job': 'is_incre_job',
        'flag': 'flag',
        'files_read': 'files_read',
        'update_user': 'update-user',
        'external_id': 'external_id',
        'type': 'type',
        'execute_start_date': 'execute_start_date',
        'delete_rows': 'delete_rows',
        'enabled': 'enabled',
        'bytes_written': 'bytes_written',
        'id': 'id',
        'is_use_sql': 'is_use_sql',
        'update_rows': 'update_rows',
        'group_name': 'group_name',
        'bytes_read': 'bytes_read',
        'execute_update_date': 'execute_update_date',
        'write_rows': 'write_rows',
        'rows_written': 'rows_written',
        'rows_read': 'rows_read',
        'files_written': 'files_written',
        'is_incrementing': 'is_incrementing',
        'execute_create_date': 'execute_create_date',
        'status': 'status'
    }

    def __init__(self, job_type=None, from_connector_name=None, to_config_values=None, to_link_name=None, driver_config_values=None, from_config_values=None, to_connector_name=None, name=None, from_link_name=None, creation_user=None, creation_date=None, update_date=None, is_incre_job=None, flag=None, files_read=None, update_user=None, external_id=None, type=None, execute_start_date=None, delete_rows=None, enabled=None, bytes_written=None, id=None, is_use_sql=None, update_rows=None, group_name=None, bytes_read=None, execute_update_date=None, write_rows=None, rows_written=None, rows_read=None, files_written=None, is_incrementing=None, execute_create_date=None, status=None):
        """Job

        The model defined in huaweicloud sdk

        :param job_type: 作业类型： - NORMAL_JOB：表/文件迁移。 - BATCH_JOB：整库迁移。 - SCENARIO_JOB：场景迁移。
        :type job_type: str
        :param from_connector_name: 源端连接类型
        :type from_connector_name: str
        :param to_config_values: 
        :type to_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        :param to_link_name: 目的端连接名称
        :type to_link_name: str
        :param driver_config_values: 
        :type driver_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        :param from_config_values: 
        :type from_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        :param to_connector_name: 目的端连接类型
        :type to_connector_name: str
        :param name: 作业名称，长度在1到240个字符之间
        :type name: str
        :param from_link_name: 源连接名称
        :type from_link_name: str
        :param creation_user: 创建的用户。
        :type creation_user: str
        :param creation_date: 作业创建的时间，单位：毫秒。
        :type creation_date: int
        :param update_date: 作业最后更新的时间，单位：毫秒。
        :type update_date: int
        :param is_incre_job: 是否增量
        :type is_incre_job: bool
        :param flag: 标记
        :type flag: int
        :param files_read: 已读文件数
        :type files_read: int
        :param update_user: 作业最后更新的用户。
        :type update_user: str
        :param external_id: 外部ID。
        :type external_id: str
        :param type: 作业类型
        :type type: str
        :param execute_start_date: 执行_开始_日期。
        :type execute_start_date: int
        :param delete_rows: 删除行数
        :type delete_rows: int
        :param enabled: 是否激活连接
        :type enabled: bool
        :param bytes_written: 写入字节
        :type bytes_written: int
        :param id: 作业ID
        :type id: int
        :param is_use_sql: 用户是否使用sql
        :type is_use_sql: bool
        :param update_rows: 更新行数
        :type update_rows: int
        :param group_name: 组_名称
        :type group_name: str
        :param bytes_read: 读取字节
        :type bytes_read: int
        :param execute_update_date: 执行_更新_日期。
        :type execute_update_date: int
        :param write_rows: 写入数据行数
        :type write_rows: int
        :param rows_written: 写入行数
        :type rows_written: int
        :param rows_read: 读取的行数
        :type rows_read: int
        :param files_written: 写入文件数
        :type files_written: int
        :param is_incrementing: 是否增量
        :type is_incrementing: bool
        :param execute_create_date: 执行_创建_日期
        :type execute_create_date: int
        :param status: 作业最后的执行状态： - BOOTING：启动中。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - NEW：未被执行。
        :type status: str
        """
        
        

        self._job_type = None
        self._from_connector_name = None
        self._to_config_values = None
        self._to_link_name = None
        self._driver_config_values = None
        self._from_config_values = None
        self._to_connector_name = None
        self._name = None
        self._from_link_name = None
        self._creation_user = None
        self._creation_date = None
        self._update_date = None
        self._is_incre_job = None
        self._flag = None
        self._files_read = None
        self._update_user = None
        self._external_id = None
        self._type = None
        self._execute_start_date = None
        self._delete_rows = None
        self._enabled = None
        self._bytes_written = None
        self._id = None
        self._is_use_sql = None
        self._update_rows = None
        self._group_name = None
        self._bytes_read = None
        self._execute_update_date = None
        self._write_rows = None
        self._rows_written = None
        self._rows_read = None
        self._files_written = None
        self._is_incrementing = None
        self._execute_create_date = None
        self._status = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        self.from_connector_name = from_connector_name
        self.to_config_values = to_config_values
        self.to_link_name = to_link_name
        self.driver_config_values = driver_config_values
        self.from_config_values = from_config_values
        if to_connector_name is not None:
            self.to_connector_name = to_connector_name
        if name is not None:
            self.name = name
        if from_link_name is not None:
            self.from_link_name = from_link_name
        if creation_user is not None:
            self.creation_user = creation_user
        if creation_date is not None:
            self.creation_date = creation_date
        if update_date is not None:
            self.update_date = update_date
        if is_incre_job is not None:
            self.is_incre_job = is_incre_job
        if flag is not None:
            self.flag = flag
        if files_read is not None:
            self.files_read = files_read
        if update_user is not None:
            self.update_user = update_user
        if external_id is not None:
            self.external_id = external_id
        if type is not None:
            self.type = type
        if execute_start_date is not None:
            self.execute_start_date = execute_start_date
        if delete_rows is not None:
            self.delete_rows = delete_rows
        if enabled is not None:
            self.enabled = enabled
        if bytes_written is not None:
            self.bytes_written = bytes_written
        if id is not None:
            self.id = id
        if is_use_sql is not None:
            self.is_use_sql = is_use_sql
        if update_rows is not None:
            self.update_rows = update_rows
        if group_name is not None:
            self.group_name = group_name
        if bytes_read is not None:
            self.bytes_read = bytes_read
        if execute_update_date is not None:
            self.execute_update_date = execute_update_date
        if write_rows is not None:
            self.write_rows = write_rows
        if rows_written is not None:
            self.rows_written = rows_written
        if rows_read is not None:
            self.rows_read = rows_read
        if files_written is not None:
            self.files_written = files_written
        if is_incrementing is not None:
            self.is_incrementing = is_incrementing
        if execute_create_date is not None:
            self.execute_create_date = execute_create_date
        if status is not None:
            self.status = status

    @property
    def job_type(self):
        """Gets the job_type of this Job.

        作业类型： - NORMAL_JOB：表/文件迁移。 - BATCH_JOB：整库迁移。 - SCENARIO_JOB：场景迁移。

        :return: The job_type of this Job.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        作业类型： - NORMAL_JOB：表/文件迁移。 - BATCH_JOB：整库迁移。 - SCENARIO_JOB：场景迁移。

        :param job_type: The job_type of this Job.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def from_connector_name(self):
        """Gets the from_connector_name of this Job.

        源端连接类型

        :return: The from_connector_name of this Job.
        :rtype: str
        """
        return self._from_connector_name

    @from_connector_name.setter
    def from_connector_name(self, from_connector_name):
        """Sets the from_connector_name of this Job.

        源端连接类型

        :param from_connector_name: The from_connector_name of this Job.
        :type from_connector_name: str
        """
        self._from_connector_name = from_connector_name

    @property
    def to_config_values(self):
        """Gets the to_config_values of this Job.

        :return: The to_config_values of this Job.
        :rtype: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        return self._to_config_values

    @to_config_values.setter
    def to_config_values(self, to_config_values):
        """Sets the to_config_values of this Job.

        :param to_config_values: The to_config_values of this Job.
        :type to_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        self._to_config_values = to_config_values

    @property
    def to_link_name(self):
        """Gets the to_link_name of this Job.

        目的端连接名称

        :return: The to_link_name of this Job.
        :rtype: str
        """
        return self._to_link_name

    @to_link_name.setter
    def to_link_name(self, to_link_name):
        """Sets the to_link_name of this Job.

        目的端连接名称

        :param to_link_name: The to_link_name of this Job.
        :type to_link_name: str
        """
        self._to_link_name = to_link_name

    @property
    def driver_config_values(self):
        """Gets the driver_config_values of this Job.

        :return: The driver_config_values of this Job.
        :rtype: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        return self._driver_config_values

    @driver_config_values.setter
    def driver_config_values(self, driver_config_values):
        """Sets the driver_config_values of this Job.

        :param driver_config_values: The driver_config_values of this Job.
        :type driver_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        self._driver_config_values = driver_config_values

    @property
    def from_config_values(self):
        """Gets the from_config_values of this Job.

        :return: The from_config_values of this Job.
        :rtype: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        return self._from_config_values

    @from_config_values.setter
    def from_config_values(self, from_config_values):
        """Sets the from_config_values of this Job.

        :param from_config_values: The from_config_values of this Job.
        :type from_config_values: :class:`huaweicloudsdkcdm.v1.ConfigValues`
        """
        self._from_config_values = from_config_values

    @property
    def to_connector_name(self):
        """Gets the to_connector_name of this Job.

        目的端连接类型

        :return: The to_connector_name of this Job.
        :rtype: str
        """
        return self._to_connector_name

    @to_connector_name.setter
    def to_connector_name(self, to_connector_name):
        """Sets the to_connector_name of this Job.

        目的端连接类型

        :param to_connector_name: The to_connector_name of this Job.
        :type to_connector_name: str
        """
        self._to_connector_name = to_connector_name

    @property
    def name(self):
        """Gets the name of this Job.

        作业名称，长度在1到240个字符之间

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        作业名称，长度在1到240个字符之间

        :param name: The name of this Job.
        :type name: str
        """
        self._name = name

    @property
    def from_link_name(self):
        """Gets the from_link_name of this Job.

        源连接名称

        :return: The from_link_name of this Job.
        :rtype: str
        """
        return self._from_link_name

    @from_link_name.setter
    def from_link_name(self, from_link_name):
        """Sets the from_link_name of this Job.

        源连接名称

        :param from_link_name: The from_link_name of this Job.
        :type from_link_name: str
        """
        self._from_link_name = from_link_name

    @property
    def creation_user(self):
        """Gets the creation_user of this Job.

        创建的用户。

        :return: The creation_user of this Job.
        :rtype: str
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        """Sets the creation_user of this Job.

        创建的用户。

        :param creation_user: The creation_user of this Job.
        :type creation_user: str
        """
        self._creation_user = creation_user

    @property
    def creation_date(self):
        """Gets the creation_date of this Job.

        作业创建的时间，单位：毫秒。

        :return: The creation_date of this Job.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Job.

        作业创建的时间，单位：毫秒。

        :param creation_date: The creation_date of this Job.
        :type creation_date: int
        """
        self._creation_date = creation_date

    @property
    def update_date(self):
        """Gets the update_date of this Job.

        作业最后更新的时间，单位：毫秒。

        :return: The update_date of this Job.
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this Job.

        作业最后更新的时间，单位：毫秒。

        :param update_date: The update_date of this Job.
        :type update_date: int
        """
        self._update_date = update_date

    @property
    def is_incre_job(self):
        """Gets the is_incre_job of this Job.

        是否增量

        :return: The is_incre_job of this Job.
        :rtype: bool
        """
        return self._is_incre_job

    @is_incre_job.setter
    def is_incre_job(self, is_incre_job):
        """Sets the is_incre_job of this Job.

        是否增量

        :param is_incre_job: The is_incre_job of this Job.
        :type is_incre_job: bool
        """
        self._is_incre_job = is_incre_job

    @property
    def flag(self):
        """Gets the flag of this Job.

        标记

        :return: The flag of this Job.
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this Job.

        标记

        :param flag: The flag of this Job.
        :type flag: int
        """
        self._flag = flag

    @property
    def files_read(self):
        """Gets the files_read of this Job.

        已读文件数

        :return: The files_read of this Job.
        :rtype: int
        """
        return self._files_read

    @files_read.setter
    def files_read(self, files_read):
        """Sets the files_read of this Job.

        已读文件数

        :param files_read: The files_read of this Job.
        :type files_read: int
        """
        self._files_read = files_read

    @property
    def update_user(self):
        """Gets the update_user of this Job.

        作业最后更新的用户。

        :return: The update_user of this Job.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this Job.

        作业最后更新的用户。

        :param update_user: The update_user of this Job.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def external_id(self):
        """Gets the external_id of this Job.

        外部ID。

        :return: The external_id of this Job.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Job.

        外部ID。

        :param external_id: The external_id of this Job.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def type(self):
        """Gets the type of this Job.

        作业类型

        :return: The type of this Job.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.

        作业类型

        :param type: The type of this Job.
        :type type: str
        """
        self._type = type

    @property
    def execute_start_date(self):
        """Gets the execute_start_date of this Job.

        执行_开始_日期。

        :return: The execute_start_date of this Job.
        :rtype: int
        """
        return self._execute_start_date

    @execute_start_date.setter
    def execute_start_date(self, execute_start_date):
        """Sets the execute_start_date of this Job.

        执行_开始_日期。

        :param execute_start_date: The execute_start_date of this Job.
        :type execute_start_date: int
        """
        self._execute_start_date = execute_start_date

    @property
    def delete_rows(self):
        """Gets the delete_rows of this Job.

        删除行数

        :return: The delete_rows of this Job.
        :rtype: int
        """
        return self._delete_rows

    @delete_rows.setter
    def delete_rows(self, delete_rows):
        """Sets the delete_rows of this Job.

        删除行数

        :param delete_rows: The delete_rows of this Job.
        :type delete_rows: int
        """
        self._delete_rows = delete_rows

    @property
    def enabled(self):
        """Gets the enabled of this Job.

        是否激活连接

        :return: The enabled of this Job.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Job.

        是否激活连接

        :param enabled: The enabled of this Job.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def bytes_written(self):
        """Gets the bytes_written of this Job.

        写入字节

        :return: The bytes_written of this Job.
        :rtype: int
        """
        return self._bytes_written

    @bytes_written.setter
    def bytes_written(self, bytes_written):
        """Sets the bytes_written of this Job.

        写入字节

        :param bytes_written: The bytes_written of this Job.
        :type bytes_written: int
        """
        self._bytes_written = bytes_written

    @property
    def id(self):
        """Gets the id of this Job.

        作业ID

        :return: The id of this Job.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        作业ID

        :param id: The id of this Job.
        :type id: int
        """
        self._id = id

    @property
    def is_use_sql(self):
        """Gets the is_use_sql of this Job.

        用户是否使用sql

        :return: The is_use_sql of this Job.
        :rtype: bool
        """
        return self._is_use_sql

    @is_use_sql.setter
    def is_use_sql(self, is_use_sql):
        """Sets the is_use_sql of this Job.

        用户是否使用sql

        :param is_use_sql: The is_use_sql of this Job.
        :type is_use_sql: bool
        """
        self._is_use_sql = is_use_sql

    @property
    def update_rows(self):
        """Gets the update_rows of this Job.

        更新行数

        :return: The update_rows of this Job.
        :rtype: int
        """
        return self._update_rows

    @update_rows.setter
    def update_rows(self, update_rows):
        """Sets the update_rows of this Job.

        更新行数

        :param update_rows: The update_rows of this Job.
        :type update_rows: int
        """
        self._update_rows = update_rows

    @property
    def group_name(self):
        """Gets the group_name of this Job.

        组_名称

        :return: The group_name of this Job.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Job.

        组_名称

        :param group_name: The group_name of this Job.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def bytes_read(self):
        """Gets the bytes_read of this Job.

        读取字节

        :return: The bytes_read of this Job.
        :rtype: int
        """
        return self._bytes_read

    @bytes_read.setter
    def bytes_read(self, bytes_read):
        """Sets the bytes_read of this Job.

        读取字节

        :param bytes_read: The bytes_read of this Job.
        :type bytes_read: int
        """
        self._bytes_read = bytes_read

    @property
    def execute_update_date(self):
        """Gets the execute_update_date of this Job.

        执行_更新_日期。

        :return: The execute_update_date of this Job.
        :rtype: int
        """
        return self._execute_update_date

    @execute_update_date.setter
    def execute_update_date(self, execute_update_date):
        """Sets the execute_update_date of this Job.

        执行_更新_日期。

        :param execute_update_date: The execute_update_date of this Job.
        :type execute_update_date: int
        """
        self._execute_update_date = execute_update_date

    @property
    def write_rows(self):
        """Gets the write_rows of this Job.

        写入数据行数

        :return: The write_rows of this Job.
        :rtype: int
        """
        return self._write_rows

    @write_rows.setter
    def write_rows(self, write_rows):
        """Sets the write_rows of this Job.

        写入数据行数

        :param write_rows: The write_rows of this Job.
        :type write_rows: int
        """
        self._write_rows = write_rows

    @property
    def rows_written(self):
        """Gets the rows_written of this Job.

        写入行数

        :return: The rows_written of this Job.
        :rtype: int
        """
        return self._rows_written

    @rows_written.setter
    def rows_written(self, rows_written):
        """Sets the rows_written of this Job.

        写入行数

        :param rows_written: The rows_written of this Job.
        :type rows_written: int
        """
        self._rows_written = rows_written

    @property
    def rows_read(self):
        """Gets the rows_read of this Job.

        读取的行数

        :return: The rows_read of this Job.
        :rtype: int
        """
        return self._rows_read

    @rows_read.setter
    def rows_read(self, rows_read):
        """Sets the rows_read of this Job.

        读取的行数

        :param rows_read: The rows_read of this Job.
        :type rows_read: int
        """
        self._rows_read = rows_read

    @property
    def files_written(self):
        """Gets the files_written of this Job.

        写入文件数

        :return: The files_written of this Job.
        :rtype: int
        """
        return self._files_written

    @files_written.setter
    def files_written(self, files_written):
        """Sets the files_written of this Job.

        写入文件数

        :param files_written: The files_written of this Job.
        :type files_written: int
        """
        self._files_written = files_written

    @property
    def is_incrementing(self):
        """Gets the is_incrementing of this Job.

        是否增量

        :return: The is_incrementing of this Job.
        :rtype: bool
        """
        return self._is_incrementing

    @is_incrementing.setter
    def is_incrementing(self, is_incrementing):
        """Sets the is_incrementing of this Job.

        是否增量

        :param is_incrementing: The is_incrementing of this Job.
        :type is_incrementing: bool
        """
        self._is_incrementing = is_incrementing

    @property
    def execute_create_date(self):
        """Gets the execute_create_date of this Job.

        执行_创建_日期

        :return: The execute_create_date of this Job.
        :rtype: int
        """
        return self._execute_create_date

    @execute_create_date.setter
    def execute_create_date(self, execute_create_date):
        """Sets the execute_create_date of this Job.

        执行_创建_日期

        :param execute_create_date: The execute_create_date of this Job.
        :type execute_create_date: int
        """
        self._execute_create_date = execute_create_date

    @property
    def status(self):
        """Gets the status of this Job.

        作业最后的执行状态： - BOOTING：启动中。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - NEW：未被执行。

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        作业最后的执行状态： - BOOTING：启动中。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - NEW：未被执行。

        :param status: The status of this Job.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
