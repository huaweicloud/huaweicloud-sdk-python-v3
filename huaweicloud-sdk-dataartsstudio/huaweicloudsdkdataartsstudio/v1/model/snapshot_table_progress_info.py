# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotTableProgressInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'str',
        'database': 'str',
        'table': 'str',
        'records_read': 'int',
        'logic_table': 'bool',
        'sub_table_progress': 'list[SnapshotTableProgressInfo]'
    }

    attribute_map = {
        'progress': 'progress',
        'database': 'database',
        'table': 'table',
        'records_read': 'records_read',
        'logic_table': 'logic_table',
        'sub_table_progress': 'sub_table_progress'
    }

    def __init__(self, progress=None, database=None, table=None, records_read=None, logic_table=None, sub_table_progress=None):
        r"""SnapshotTableProgressInfo

        The model defined in huaweicloud sdk

        :param progress: 单表全量同步进度。
        :type progress: str
        :param database: 数据库名或者逻辑库名。
        :type database: str
        :param table: 表名或者逻辑表名。
        :type table: str
        :param records_read: 读取的表的数据条数。
        :type records_read: int
        :param logic_table: 是否是逻辑表。
        :type logic_table: bool
        :param sub_table_progress: 表级别全量同步进度，如果是分库分表作业，则这里为各个子表的同步进度。
        :type sub_table_progress: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        
        

        self._progress = None
        self._database = None
        self._table = None
        self._records_read = None
        self._logic_table = None
        self._sub_table_progress = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if database is not None:
            self.database = database
        if table is not None:
            self.table = table
        if records_read is not None:
            self.records_read = records_read
        if logic_table is not None:
            self.logic_table = logic_table
        if sub_table_progress is not None:
            self.sub_table_progress = sub_table_progress

    @property
    def progress(self):
        r"""Gets the progress of this SnapshotTableProgressInfo.

        单表全量同步进度。

        :return: The progress of this SnapshotTableProgressInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SnapshotTableProgressInfo.

        单表全量同步进度。

        :param progress: The progress of this SnapshotTableProgressInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def database(self):
        r"""Gets the database of this SnapshotTableProgressInfo.

        数据库名或者逻辑库名。

        :return: The database of this SnapshotTableProgressInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this SnapshotTableProgressInfo.

        数据库名或者逻辑库名。

        :param database: The database of this SnapshotTableProgressInfo.
        :type database: str
        """
        self._database = database

    @property
    def table(self):
        r"""Gets the table of this SnapshotTableProgressInfo.

        表名或者逻辑表名。

        :return: The table of this SnapshotTableProgressInfo.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this SnapshotTableProgressInfo.

        表名或者逻辑表名。

        :param table: The table of this SnapshotTableProgressInfo.
        :type table: str
        """
        self._table = table

    @property
    def records_read(self):
        r"""Gets the records_read of this SnapshotTableProgressInfo.

        读取的表的数据条数。

        :return: The records_read of this SnapshotTableProgressInfo.
        :rtype: int
        """
        return self._records_read

    @records_read.setter
    def records_read(self, records_read):
        r"""Sets the records_read of this SnapshotTableProgressInfo.

        读取的表的数据条数。

        :param records_read: The records_read of this SnapshotTableProgressInfo.
        :type records_read: int
        """
        self._records_read = records_read

    @property
    def logic_table(self):
        r"""Gets the logic_table of this SnapshotTableProgressInfo.

        是否是逻辑表。

        :return: The logic_table of this SnapshotTableProgressInfo.
        :rtype: bool
        """
        return self._logic_table

    @logic_table.setter
    def logic_table(self, logic_table):
        r"""Sets the logic_table of this SnapshotTableProgressInfo.

        是否是逻辑表。

        :param logic_table: The logic_table of this SnapshotTableProgressInfo.
        :type logic_table: bool
        """
        self._logic_table = logic_table

    @property
    def sub_table_progress(self):
        r"""Gets the sub_table_progress of this SnapshotTableProgressInfo.

        表级别全量同步进度，如果是分库分表作业，则这里为各个子表的同步进度。

        :return: The sub_table_progress of this SnapshotTableProgressInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        return self._sub_table_progress

    @sub_table_progress.setter
    def sub_table_progress(self, sub_table_progress):
        r"""Sets the sub_table_progress of this SnapshotTableProgressInfo.

        表级别全量同步进度，如果是分库分表作业，则这里为各个子表的同步进度。

        :param sub_table_progress: The sub_table_progress of this SnapshotTableProgressInfo.
        :type sub_table_progress: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        self._sub_table_progress = sub_table_progress

    def to_dict(self):
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
        if not isinstance(other, SnapshotTableProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
