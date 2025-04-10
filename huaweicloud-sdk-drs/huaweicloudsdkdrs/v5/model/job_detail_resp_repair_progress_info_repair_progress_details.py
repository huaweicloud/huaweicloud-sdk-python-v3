# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetailRespRepairProgressInfoRepairProgressDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'total_row_count': 'int',
        'complete_row_count': 'int',
        'filter_row_count': 'int',
        'repaired_row_count': 'int',
        'failed_row_count': 'int',
        'repair_status': 'int',
        'start_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'query_id': 'query_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'total_row_count': 'total_row_count',
        'complete_row_count': 'complete_row_count',
        'filter_row_count': 'filter_row_count',
        'repaired_row_count': 'repaired_row_count',
        'failed_row_count': 'failed_row_count',
        'repair_status': 'repair_status',
        'start_time': 'start_time',
        'update_time': 'update_time'
    }

    def __init__(self, query_id=None, db_name=None, schema_name=None, table_name=None, total_row_count=None, complete_row_count=None, filter_row_count=None, repaired_row_count=None, failed_row_count=None, repair_status=None, start_time=None, update_time=None):
        r"""JobDetailRespRepairProgressInfoRepairProgressDetails

        The model defined in huaweicloud sdk

        :param query_id: 对比任务ID。
        :type query_id: str
        :param db_name: 库名。
        :type db_name: str
        :param schema_name: schema名。
        :type schema_name: str
        :param table_name: 表名。
        :type table_name: str
        :param total_row_count: 总行数。
        :type total_row_count: int
        :param complete_row_count: 完成行数。
        :type complete_row_count: int
        :param filter_row_count: 过滤行数。
        :type filter_row_count: int
        :param repaired_row_count: 已修复行数。
        :type repaired_row_count: int
        :param failed_row_count: 失败行数。
        :type failed_row_count: int
        :param repair_status: 修复状态。
        :type repair_status: int
        :param start_time: 开始时间。
        :type start_time: str
        :param update_time: 更新时间。
        :type update_time: str
        """
        
        

        self._query_id = None
        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._total_row_count = None
        self._complete_row_count = None
        self._filter_row_count = None
        self._repaired_row_count = None
        self._failed_row_count = None
        self._repair_status = None
        self._start_time = None
        self._update_time = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if complete_row_count is not None:
            self.complete_row_count = complete_row_count
        if filter_row_count is not None:
            self.filter_row_count = filter_row_count
        if repaired_row_count is not None:
            self.repaired_row_count = repaired_row_count
        if failed_row_count is not None:
            self.failed_row_count = failed_row_count
        if repair_status is not None:
            self.repair_status = repair_status
        if start_time is not None:
            self.start_time = start_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def query_id(self):
        r"""Gets the query_id of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        对比任务ID。

        :return: The query_id of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        对比任务ID。

        :param query_id: The query_id of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def db_name(self):
        r"""Gets the db_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        库名。

        :return: The db_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        库名。

        :param db_name: The db_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        schema名。

        :return: The schema_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        schema名。

        :param schema_name: The schema_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        表名。

        :return: The table_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        表名。

        :param table_name: The table_name of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def total_row_count(self):
        r"""Gets the total_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        总行数。

        :return: The total_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        r"""Sets the total_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        总行数。

        :param total_row_count: The total_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type total_row_count: int
        """
        self._total_row_count = total_row_count

    @property
    def complete_row_count(self):
        r"""Gets the complete_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        完成行数。

        :return: The complete_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._complete_row_count

    @complete_row_count.setter
    def complete_row_count(self, complete_row_count):
        r"""Sets the complete_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        完成行数。

        :param complete_row_count: The complete_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type complete_row_count: int
        """
        self._complete_row_count = complete_row_count

    @property
    def filter_row_count(self):
        r"""Gets the filter_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        过滤行数。

        :return: The filter_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._filter_row_count

    @filter_row_count.setter
    def filter_row_count(self, filter_row_count):
        r"""Sets the filter_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        过滤行数。

        :param filter_row_count: The filter_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type filter_row_count: int
        """
        self._filter_row_count = filter_row_count

    @property
    def repaired_row_count(self):
        r"""Gets the repaired_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        已修复行数。

        :return: The repaired_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._repaired_row_count

    @repaired_row_count.setter
    def repaired_row_count(self, repaired_row_count):
        r"""Sets the repaired_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        已修复行数。

        :param repaired_row_count: The repaired_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type repaired_row_count: int
        """
        self._repaired_row_count = repaired_row_count

    @property
    def failed_row_count(self):
        r"""Gets the failed_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        失败行数。

        :return: The failed_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._failed_row_count

    @failed_row_count.setter
    def failed_row_count(self, failed_row_count):
        r"""Sets the failed_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        失败行数。

        :param failed_row_count: The failed_row_count of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type failed_row_count: int
        """
        self._failed_row_count = failed_row_count

    @property
    def repair_status(self):
        r"""Gets the repair_status of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        修复状态。

        :return: The repair_status of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: int
        """
        return self._repair_status

    @repair_status.setter
    def repair_status(self, repair_status):
        r"""Sets the repair_status of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        修复状态。

        :param repair_status: The repair_status of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type repair_status: int
        """
        self._repair_status = repair_status

    @property
    def start_time(self):
        r"""Gets the start_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        开始时间。

        :return: The start_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        开始时间。

        :param start_time: The start_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def update_time(self):
        r"""Gets the update_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        更新时间。

        :return: The update_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.

        更新时间。

        :param update_time: The update_time of this JobDetailRespRepairProgressInfoRepairProgressDetails.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, JobDetailRespRepairProgressInfoRepairProgressDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
