# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataProfileRO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'db_type': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'table_id': 'str',
        'column_names': 'list[TableColumnDTO]',
        'fields_name': 'list[str]',
        'queue': 'str',
        'unique': 'bool',
        'time_profile': 'bool',
        'sample': 'str',
        'job_id': 'str',
        'cancel': 'bool',
        'auto_stop': 'bool',
        'obsconfig': 'OBSCommonConfig'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'db_type': 'db_type',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'table_id': 'table_id',
        'column_names': 'column_names',
        'fields_name': 'fields_name',
        'queue': 'queue',
        'unique': 'unique',
        'time_profile': 'time_profile',
        'sample': 'sample',
        'job_id': 'job_id',
        'cancel': 'cancel',
        'auto_stop': 'auto_stop',
        'obsconfig': 'obsconfig'
    }

    def __init__(self, dw_id=None, db_type=None, database_name=None, table_name=None, table_id=None, column_names=None, fields_name=None, queue=None, unique=None, time_profile=None, sample=None, job_id=None, cancel=None, auto_stop=None, obsconfig=None):
        """DataProfileRO

        The model defined in huaweicloud sdk

        :param dw_id: 连接id
        :type dw_id: str
        :param db_type: 数据源类型
        :type db_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param table_id: 表ID
        :type table_id: str
        :param column_names: 待更新概要字段列表
        :type column_names: list[:class:`huaweicloudsdkdataartsstudio.v1.TableColumnDTO`]
        :param fields_name: 字段名称列表
        :type fields_name: list[str]
        :param queue: 执行更新语句队列
        :type queue: str
        :param unique: 是否采集唯一值
        :type unique: bool
        :param time_profile: 时间档案
        :type time_profile: bool
        :param sample: 数据采样方式
        :type sample: str
        :param job_id: 作业id
        :type job_id: str
        :param cancel: 是否取消
        :type cancel: bool
        :param auto_stop: 是否自动停止
        :type auto_stop: bool
        :param obsconfig: 
        :type obsconfig: :class:`huaweicloudsdkdataartsstudio.v1.OBSCommonConfig`
        """
        
        

        self._dw_id = None
        self._db_type = None
        self._database_name = None
        self._table_name = None
        self._table_id = None
        self._column_names = None
        self._fields_name = None
        self._queue = None
        self._unique = None
        self._time_profile = None
        self._sample = None
        self._job_id = None
        self._cancel = None
        self._auto_stop = None
        self._obsconfig = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if db_type is not None:
            self.db_type = db_type
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        if column_names is not None:
            self.column_names = column_names
        if fields_name is not None:
            self.fields_name = fields_name
        if queue is not None:
            self.queue = queue
        if unique is not None:
            self.unique = unique
        if time_profile is not None:
            self.time_profile = time_profile
        if sample is not None:
            self.sample = sample
        if job_id is not None:
            self.job_id = job_id
        if cancel is not None:
            self.cancel = cancel
        if auto_stop is not None:
            self.auto_stop = auto_stop
        if obsconfig is not None:
            self.obsconfig = obsconfig

    @property
    def dw_id(self):
        """Gets the dw_id of this DataProfileRO.

        连接id

        :return: The dw_id of this DataProfileRO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this DataProfileRO.

        连接id

        :param dw_id: The dw_id of this DataProfileRO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def db_type(self):
        """Gets the db_type of this DataProfileRO.

        数据源类型

        :return: The db_type of this DataProfileRO.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this DataProfileRO.

        数据源类型

        :param db_type: The db_type of this DataProfileRO.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def database_name(self):
        """Gets the database_name of this DataProfileRO.

        数据库名称

        :return: The database_name of this DataProfileRO.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DataProfileRO.

        数据库名称

        :param database_name: The database_name of this DataProfileRO.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this DataProfileRO.

        表名称

        :return: The table_name of this DataProfileRO.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DataProfileRO.

        表名称

        :param table_name: The table_name of this DataProfileRO.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_id(self):
        """Gets the table_id of this DataProfileRO.

        表ID

        :return: The table_id of this DataProfileRO.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this DataProfileRO.

        表ID

        :param table_id: The table_id of this DataProfileRO.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def column_names(self):
        """Gets the column_names of this DataProfileRO.

        待更新概要字段列表

        :return: The column_names of this DataProfileRO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableColumnDTO`]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this DataProfileRO.

        待更新概要字段列表

        :param column_names: The column_names of this DataProfileRO.
        :type column_names: list[:class:`huaweicloudsdkdataartsstudio.v1.TableColumnDTO`]
        """
        self._column_names = column_names

    @property
    def fields_name(self):
        """Gets the fields_name of this DataProfileRO.

        字段名称列表

        :return: The fields_name of this DataProfileRO.
        :rtype: list[str]
        """
        return self._fields_name

    @fields_name.setter
    def fields_name(self, fields_name):
        """Sets the fields_name of this DataProfileRO.

        字段名称列表

        :param fields_name: The fields_name of this DataProfileRO.
        :type fields_name: list[str]
        """
        self._fields_name = fields_name

    @property
    def queue(self):
        """Gets the queue of this DataProfileRO.

        执行更新语句队列

        :return: The queue of this DataProfileRO.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this DataProfileRO.

        执行更新语句队列

        :param queue: The queue of this DataProfileRO.
        :type queue: str
        """
        self._queue = queue

    @property
    def unique(self):
        """Gets the unique of this DataProfileRO.

        是否采集唯一值

        :return: The unique of this DataProfileRO.
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this DataProfileRO.

        是否采集唯一值

        :param unique: The unique of this DataProfileRO.
        :type unique: bool
        """
        self._unique = unique

    @property
    def time_profile(self):
        """Gets the time_profile of this DataProfileRO.

        时间档案

        :return: The time_profile of this DataProfileRO.
        :rtype: bool
        """
        return self._time_profile

    @time_profile.setter
    def time_profile(self, time_profile):
        """Sets the time_profile of this DataProfileRO.

        时间档案

        :param time_profile: The time_profile of this DataProfileRO.
        :type time_profile: bool
        """
        self._time_profile = time_profile

    @property
    def sample(self):
        """Gets the sample of this DataProfileRO.

        数据采样方式

        :return: The sample of this DataProfileRO.
        :rtype: str
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this DataProfileRO.

        数据采样方式

        :param sample: The sample of this DataProfileRO.
        :type sample: str
        """
        self._sample = sample

    @property
    def job_id(self):
        """Gets the job_id of this DataProfileRO.

        作业id

        :return: The job_id of this DataProfileRO.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DataProfileRO.

        作业id

        :param job_id: The job_id of this DataProfileRO.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def cancel(self):
        """Gets the cancel of this DataProfileRO.

        是否取消

        :return: The cancel of this DataProfileRO.
        :rtype: bool
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this DataProfileRO.

        是否取消

        :param cancel: The cancel of this DataProfileRO.
        :type cancel: bool
        """
        self._cancel = cancel

    @property
    def auto_stop(self):
        """Gets the auto_stop of this DataProfileRO.

        是否自动停止

        :return: The auto_stop of this DataProfileRO.
        :rtype: bool
        """
        return self._auto_stop

    @auto_stop.setter
    def auto_stop(self, auto_stop):
        """Sets the auto_stop of this DataProfileRO.

        是否自动停止

        :param auto_stop: The auto_stop of this DataProfileRO.
        :type auto_stop: bool
        """
        self._auto_stop = auto_stop

    @property
    def obsconfig(self):
        """Gets the obsconfig of this DataProfileRO.

        :return: The obsconfig of this DataProfileRO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.OBSCommonConfig`
        """
        return self._obsconfig

    @obsconfig.setter
    def obsconfig(self, obsconfig):
        """Sets the obsconfig of this DataProfileRO.

        :param obsconfig: The obsconfig of this DataProfileRO.
        :type obsconfig: :class:`huaweicloudsdkdataartsstudio.v1.OBSCommonConfig`
        """
        self._obsconfig = obsconfig

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
        if not isinstance(other, DataProfileRO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
