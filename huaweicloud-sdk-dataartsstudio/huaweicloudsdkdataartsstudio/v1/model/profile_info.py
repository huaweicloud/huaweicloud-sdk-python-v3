# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProfileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_type': 'str',
        'cancel': 'bool',
        'table_size': 'float',
        'database_name': 'str',
        'obs_common_config': 'str',
        'total_row_count': 'str',
        'fields_name': 'list[str]',
        'table_name': 'str',
        'sample': 'str',
        'update_date': 'str',
        'row_count': 'float',
        'column_count': 'float',
        'unique': 'bool',
        'auto_stop': 'bool',
        'time_profile': 'bool',
        'queue': 'str',
        'dw_id': 'str',
        'colunms_metric': 'object',
        'columns_list': 'list[ColumnInfo]'
    }

    attribute_map = {
        'db_type': 'db_type',
        'cancel': 'cancel',
        'table_size': 'table_size',
        'database_name': 'database_name',
        'obs_common_config': 'obs_common_config',
        'total_row_count': 'total_row_count',
        'fields_name': 'fields_name',
        'table_name': 'table_name',
        'sample': 'sample',
        'update_date': 'update_date',
        'row_count': 'row_count',
        'column_count': 'column_count',
        'unique': 'unique',
        'auto_stop': 'auto_stop',
        'time_profile': 'time_profile',
        'queue': 'queue',
        'dw_id': 'dw_id',
        'colunms_metric': 'colunms_metric',
        'columns_list': 'columns_list'
    }

    def __init__(self, db_type=None, cancel=None, table_size=None, database_name=None, obs_common_config=None, total_row_count=None, fields_name=None, table_name=None, sample=None, update_date=None, row_count=None, column_count=None, unique=None, auto_stop=None, time_profile=None, queue=None, dw_id=None, colunms_metric=None, columns_list=None):
        """ProfileInfo

        The model defined in huaweicloud sdk

        :param db_type: 数据库类型
        :type db_type: str
        :param cancel: 是否取消
        :type cancel: bool
        :param table_size: 表大小
        :type table_size: float
        :param database_name: 数据库名
        :type database_name: str
        :param obs_common_config: obs公共配置
        :type obs_common_config: str
        :param total_row_count: 总行数
        :type total_row_count: str
        :param fields_name: 文件列表
        :type fields_name: list[str]
        :param table_name: 表名
        :type table_name: str
        :param sample: 样本
        :type sample: str
        :param update_date: 修改时间
        :type update_date: str
        :param row_count: 采样行数
        :type row_count: float
        :param column_count: 列数
        :type column_count: float
        :param unique: 是否唯一
        :type unique: bool
        :param auto_stop: 自动停止
        :type auto_stop: bool
        :param time_profile: 时间档案
        :type time_profile: bool
        :param queue: duilie
        :type queue: str
        :param dw_id: 连接id
        :type dw_id: str
        :param colunms_metric: 列概要信息
        :type colunms_metric: object
        :param columns_list: 列信息
        :type columns_list: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnInfo`]
        """
        
        

        self._db_type = None
        self._cancel = None
        self._table_size = None
        self._database_name = None
        self._obs_common_config = None
        self._total_row_count = None
        self._fields_name = None
        self._table_name = None
        self._sample = None
        self._update_date = None
        self._row_count = None
        self._column_count = None
        self._unique = None
        self._auto_stop = None
        self._time_profile = None
        self._queue = None
        self._dw_id = None
        self._colunms_metric = None
        self._columns_list = None
        self.discriminator = None

        if db_type is not None:
            self.db_type = db_type
        if cancel is not None:
            self.cancel = cancel
        if table_size is not None:
            self.table_size = table_size
        if database_name is not None:
            self.database_name = database_name
        if obs_common_config is not None:
            self.obs_common_config = obs_common_config
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if fields_name is not None:
            self.fields_name = fields_name
        if table_name is not None:
            self.table_name = table_name
        if sample is not None:
            self.sample = sample
        if update_date is not None:
            self.update_date = update_date
        if row_count is not None:
            self.row_count = row_count
        if column_count is not None:
            self.column_count = column_count
        if unique is not None:
            self.unique = unique
        if auto_stop is not None:
            self.auto_stop = auto_stop
        if time_profile is not None:
            self.time_profile = time_profile
        if queue is not None:
            self.queue = queue
        if dw_id is not None:
            self.dw_id = dw_id
        if colunms_metric is not None:
            self.colunms_metric = colunms_metric
        if columns_list is not None:
            self.columns_list = columns_list

    @property
    def db_type(self):
        """Gets the db_type of this ProfileInfo.

        数据库类型

        :return: The db_type of this ProfileInfo.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this ProfileInfo.

        数据库类型

        :param db_type: The db_type of this ProfileInfo.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def cancel(self):
        """Gets the cancel of this ProfileInfo.

        是否取消

        :return: The cancel of this ProfileInfo.
        :rtype: bool
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this ProfileInfo.

        是否取消

        :param cancel: The cancel of this ProfileInfo.
        :type cancel: bool
        """
        self._cancel = cancel

    @property
    def table_size(self):
        """Gets the table_size of this ProfileInfo.

        表大小

        :return: The table_size of this ProfileInfo.
        :rtype: float
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        """Sets the table_size of this ProfileInfo.

        表大小

        :param table_size: The table_size of this ProfileInfo.
        :type table_size: float
        """
        self._table_size = table_size

    @property
    def database_name(self):
        """Gets the database_name of this ProfileInfo.

        数据库名

        :return: The database_name of this ProfileInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ProfileInfo.

        数据库名

        :param database_name: The database_name of this ProfileInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def obs_common_config(self):
        """Gets the obs_common_config of this ProfileInfo.

        obs公共配置

        :return: The obs_common_config of this ProfileInfo.
        :rtype: str
        """
        return self._obs_common_config

    @obs_common_config.setter
    def obs_common_config(self, obs_common_config):
        """Sets the obs_common_config of this ProfileInfo.

        obs公共配置

        :param obs_common_config: The obs_common_config of this ProfileInfo.
        :type obs_common_config: str
        """
        self._obs_common_config = obs_common_config

    @property
    def total_row_count(self):
        """Gets the total_row_count of this ProfileInfo.

        总行数

        :return: The total_row_count of this ProfileInfo.
        :rtype: str
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this ProfileInfo.

        总行数

        :param total_row_count: The total_row_count of this ProfileInfo.
        :type total_row_count: str
        """
        self._total_row_count = total_row_count

    @property
    def fields_name(self):
        """Gets the fields_name of this ProfileInfo.

        文件列表

        :return: The fields_name of this ProfileInfo.
        :rtype: list[str]
        """
        return self._fields_name

    @fields_name.setter
    def fields_name(self, fields_name):
        """Sets the fields_name of this ProfileInfo.

        文件列表

        :param fields_name: The fields_name of this ProfileInfo.
        :type fields_name: list[str]
        """
        self._fields_name = fields_name

    @property
    def table_name(self):
        """Gets the table_name of this ProfileInfo.

        表名

        :return: The table_name of this ProfileInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ProfileInfo.

        表名

        :param table_name: The table_name of this ProfileInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def sample(self):
        """Gets the sample of this ProfileInfo.

        样本

        :return: The sample of this ProfileInfo.
        :rtype: str
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this ProfileInfo.

        样本

        :param sample: The sample of this ProfileInfo.
        :type sample: str
        """
        self._sample = sample

    @property
    def update_date(self):
        """Gets the update_date of this ProfileInfo.

        修改时间

        :return: The update_date of this ProfileInfo.
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this ProfileInfo.

        修改时间

        :param update_date: The update_date of this ProfileInfo.
        :type update_date: str
        """
        self._update_date = update_date

    @property
    def row_count(self):
        """Gets the row_count of this ProfileInfo.

        采样行数

        :return: The row_count of this ProfileInfo.
        :rtype: float
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this ProfileInfo.

        采样行数

        :param row_count: The row_count of this ProfileInfo.
        :type row_count: float
        """
        self._row_count = row_count

    @property
    def column_count(self):
        """Gets the column_count of this ProfileInfo.

        列数

        :return: The column_count of this ProfileInfo.
        :rtype: float
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """Sets the column_count of this ProfileInfo.

        列数

        :param column_count: The column_count of this ProfileInfo.
        :type column_count: float
        """
        self._column_count = column_count

    @property
    def unique(self):
        """Gets the unique of this ProfileInfo.

        是否唯一

        :return: The unique of this ProfileInfo.
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this ProfileInfo.

        是否唯一

        :param unique: The unique of this ProfileInfo.
        :type unique: bool
        """
        self._unique = unique

    @property
    def auto_stop(self):
        """Gets the auto_stop of this ProfileInfo.

        自动停止

        :return: The auto_stop of this ProfileInfo.
        :rtype: bool
        """
        return self._auto_stop

    @auto_stop.setter
    def auto_stop(self, auto_stop):
        """Sets the auto_stop of this ProfileInfo.

        自动停止

        :param auto_stop: The auto_stop of this ProfileInfo.
        :type auto_stop: bool
        """
        self._auto_stop = auto_stop

    @property
    def time_profile(self):
        """Gets the time_profile of this ProfileInfo.

        时间档案

        :return: The time_profile of this ProfileInfo.
        :rtype: bool
        """
        return self._time_profile

    @time_profile.setter
    def time_profile(self, time_profile):
        """Sets the time_profile of this ProfileInfo.

        时间档案

        :param time_profile: The time_profile of this ProfileInfo.
        :type time_profile: bool
        """
        self._time_profile = time_profile

    @property
    def queue(self):
        """Gets the queue of this ProfileInfo.

        duilie

        :return: The queue of this ProfileInfo.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this ProfileInfo.

        duilie

        :param queue: The queue of this ProfileInfo.
        :type queue: str
        """
        self._queue = queue

    @property
    def dw_id(self):
        """Gets the dw_id of this ProfileInfo.

        连接id

        :return: The dw_id of this ProfileInfo.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this ProfileInfo.

        连接id

        :param dw_id: The dw_id of this ProfileInfo.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def colunms_metric(self):
        """Gets the colunms_metric of this ProfileInfo.

        列概要信息

        :return: The colunms_metric of this ProfileInfo.
        :rtype: object
        """
        return self._colunms_metric

    @colunms_metric.setter
    def colunms_metric(self, colunms_metric):
        """Sets the colunms_metric of this ProfileInfo.

        列概要信息

        :param colunms_metric: The colunms_metric of this ProfileInfo.
        :type colunms_metric: object
        """
        self._colunms_metric = colunms_metric

    @property
    def columns_list(self):
        """Gets the columns_list of this ProfileInfo.

        列信息

        :return: The columns_list of this ProfileInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnInfo`]
        """
        return self._columns_list

    @columns_list.setter
    def columns_list(self, columns_list):
        """Sets the columns_list of this ProfileInfo.

        列信息

        :param columns_list: The columns_list of this ProfileInfo.
        :type columns_list: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnInfo`]
        """
        self._columns_list = columns_list

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
        if not isinstance(other, ProfileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
