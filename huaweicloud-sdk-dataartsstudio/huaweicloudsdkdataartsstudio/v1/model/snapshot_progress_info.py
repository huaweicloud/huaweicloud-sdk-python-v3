# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotProgressInfo:

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
        'database_total': 'int',
        'database_processed': 'int',
        'schema_total': 'int',
        'schema_processed': 'int',
        'table_total': 'int',
        'table_processed': 'int',
        'table_progress': 'list[SnapshotTableProgressInfo]'
    }

    attribute_map = {
        'progress': 'progress',
        'database_total': 'database_total',
        'database_processed': 'database_processed',
        'schema_total': 'schema_total',
        'schema_processed': 'schema_processed',
        'table_total': 'table_total',
        'table_processed': 'table_processed',
        'table_progress': 'table_progress'
    }

    def __init__(self, progress=None, database_total=None, database_processed=None, schema_total=None, schema_processed=None, table_total=None, table_processed=None, table_progress=None):
        r"""SnapshotProgressInfo

        The model defined in huaweicloud sdk

        :param progress: 全量同步整体进度。
        :type progress: str
        :param database_total: 全量同步的数据库总数，如果是分库分表，则是逻辑库的数量。
        :type database_total: int
        :param database_processed: 全量同步的数据库已读取数量，如果是分库分表，则是已读取的逻辑库数量。
        :type database_processed: int
        :param schema_total: 全量同步的schema总数，如果是分库分表，则是schema的数量。
        :type schema_total: int
        :param schema_processed: 全量同步的schema已读取数量，如果是分库分表，则是已读取的schema的数量。
        :type schema_processed: int
        :param table_total: 全量同步的表总数，如果是分库分表，则是逻辑表的数量。
        :type table_total: int
        :param table_processed: 全量同步的表已读取数量，如果是分库分表，则是已读取的逻辑表的数量。
        :type table_processed: int
        :param table_progress: 表级别全量同步进度，如果是分库分表作业，则第一层为分库分表进度。
        :type table_progress: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        
        

        self._progress = None
        self._database_total = None
        self._database_processed = None
        self._schema_total = None
        self._schema_processed = None
        self._table_total = None
        self._table_processed = None
        self._table_progress = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if database_total is not None:
            self.database_total = database_total
        if database_processed is not None:
            self.database_processed = database_processed
        if schema_total is not None:
            self.schema_total = schema_total
        if schema_processed is not None:
            self.schema_processed = schema_processed
        if table_total is not None:
            self.table_total = table_total
        if table_processed is not None:
            self.table_processed = table_processed
        if table_progress is not None:
            self.table_progress = table_progress

    @property
    def progress(self):
        r"""Gets the progress of this SnapshotProgressInfo.

        全量同步整体进度。

        :return: The progress of this SnapshotProgressInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SnapshotProgressInfo.

        全量同步整体进度。

        :param progress: The progress of this SnapshotProgressInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def database_total(self):
        r"""Gets the database_total of this SnapshotProgressInfo.

        全量同步的数据库总数，如果是分库分表，则是逻辑库的数量。

        :return: The database_total of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._database_total

    @database_total.setter
    def database_total(self, database_total):
        r"""Sets the database_total of this SnapshotProgressInfo.

        全量同步的数据库总数，如果是分库分表，则是逻辑库的数量。

        :param database_total: The database_total of this SnapshotProgressInfo.
        :type database_total: int
        """
        self._database_total = database_total

    @property
    def database_processed(self):
        r"""Gets the database_processed of this SnapshotProgressInfo.

        全量同步的数据库已读取数量，如果是分库分表，则是已读取的逻辑库数量。

        :return: The database_processed of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._database_processed

    @database_processed.setter
    def database_processed(self, database_processed):
        r"""Sets the database_processed of this SnapshotProgressInfo.

        全量同步的数据库已读取数量，如果是分库分表，则是已读取的逻辑库数量。

        :param database_processed: The database_processed of this SnapshotProgressInfo.
        :type database_processed: int
        """
        self._database_processed = database_processed

    @property
    def schema_total(self):
        r"""Gets the schema_total of this SnapshotProgressInfo.

        全量同步的schema总数，如果是分库分表，则是schema的数量。

        :return: The schema_total of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._schema_total

    @schema_total.setter
    def schema_total(self, schema_total):
        r"""Sets the schema_total of this SnapshotProgressInfo.

        全量同步的schema总数，如果是分库分表，则是schema的数量。

        :param schema_total: The schema_total of this SnapshotProgressInfo.
        :type schema_total: int
        """
        self._schema_total = schema_total

    @property
    def schema_processed(self):
        r"""Gets the schema_processed of this SnapshotProgressInfo.

        全量同步的schema已读取数量，如果是分库分表，则是已读取的schema的数量。

        :return: The schema_processed of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._schema_processed

    @schema_processed.setter
    def schema_processed(self, schema_processed):
        r"""Sets the schema_processed of this SnapshotProgressInfo.

        全量同步的schema已读取数量，如果是分库分表，则是已读取的schema的数量。

        :param schema_processed: The schema_processed of this SnapshotProgressInfo.
        :type schema_processed: int
        """
        self._schema_processed = schema_processed

    @property
    def table_total(self):
        r"""Gets the table_total of this SnapshotProgressInfo.

        全量同步的表总数，如果是分库分表，则是逻辑表的数量。

        :return: The table_total of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._table_total

    @table_total.setter
    def table_total(self, table_total):
        r"""Sets the table_total of this SnapshotProgressInfo.

        全量同步的表总数，如果是分库分表，则是逻辑表的数量。

        :param table_total: The table_total of this SnapshotProgressInfo.
        :type table_total: int
        """
        self._table_total = table_total

    @property
    def table_processed(self):
        r"""Gets the table_processed of this SnapshotProgressInfo.

        全量同步的表已读取数量，如果是分库分表，则是已读取的逻辑表的数量。

        :return: The table_processed of this SnapshotProgressInfo.
        :rtype: int
        """
        return self._table_processed

    @table_processed.setter
    def table_processed(self, table_processed):
        r"""Sets the table_processed of this SnapshotProgressInfo.

        全量同步的表已读取数量，如果是分库分表，则是已读取的逻辑表的数量。

        :param table_processed: The table_processed of this SnapshotProgressInfo.
        :type table_processed: int
        """
        self._table_processed = table_processed

    @property
    def table_progress(self):
        r"""Gets the table_progress of this SnapshotProgressInfo.

        表级别全量同步进度，如果是分库分表作业，则第一层为分库分表进度。

        :return: The table_progress of this SnapshotProgressInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        return self._table_progress

    @table_progress.setter
    def table_progress(self, table_progress):
        r"""Sets the table_progress of this SnapshotProgressInfo.

        表级别全量同步进度，如果是分库分表作业，则第一层为分库分表进度。

        :param table_progress: The table_progress of this SnapshotProgressInfo.
        :type table_progress: list[:class:`huaweicloudsdkdataartsstudio.v1.SnapshotTableProgressInfo`]
        """
        self._table_progress = table_progress

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
        if not isinstance(other, SnapshotProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
