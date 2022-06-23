# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTableReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_path': 'str',
        'data_type': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'compress': 'str',
        'queue_name': 'str',
        'export_mode': 'str',
        'with_column_header': 'bool'
    }

    attribute_map = {
        'data_path': 'data_path',
        'data_type': 'data_type',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'compress': 'compress',
        'queue_name': 'queue_name',
        'export_mode': 'export_mode',
        'with_column_header': 'with_column_header'
    }

    def __init__(self, data_path=None, data_type=None, database_name=None, table_name=None, compress=None, queue_name=None, export_mode=None, with_column_header=None):
        """ExportTableReq

        The model defined in huaweicloud sdk

        :param data_path: 导出数据的储存路径（当前仅支持将数据存储在OBS上，且OBS路径须以s3a开头）。另外，“export_mode”配置为“errorifexists”时，该路径下的文件夹须不存在，如请求样例中的“test”文件夹。
        :type data_path: str
        :param data_type: 导出数据的类型（当前仅支持csv格式数据）。
        :type data_type: str
        :param database_name: 被导出数据的表所在的数据库名称。
        :type database_name: str
        :param table_name: 被导出数据的表名称。
        :type table_name: str
        :param compress: 导出数据的压缩方法。目前支持gzip、bzip2、deflate压缩方式；若不希望压缩，则输入none。
        :type compress: str
        :param queue_name: 指定执行该任务的队列。若不指定队列，将采用default队列执行操作。
        :type queue_name: str
        :param export_mode: 导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。
        :type export_mode: str
        :param with_column_header: 导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。
        :type with_column_header: bool
        """
        
        

        self._data_path = None
        self._data_type = None
        self._database_name = None
        self._table_name = None
        self._compress = None
        self._queue_name = None
        self._export_mode = None
        self._with_column_header = None
        self.discriminator = None

        self.data_path = data_path
        self.data_type = data_type
        self.database_name = database_name
        self.table_name = table_name
        self.compress = compress
        if queue_name is not None:
            self.queue_name = queue_name
        if export_mode is not None:
            self.export_mode = export_mode
        if with_column_header is not None:
            self.with_column_header = with_column_header

    @property
    def data_path(self):
        """Gets the data_path of this ExportTableReq.

        导出数据的储存路径（当前仅支持将数据存储在OBS上，且OBS路径须以s3a开头）。另外，“export_mode”配置为“errorifexists”时，该路径下的文件夹须不存在，如请求样例中的“test”文件夹。

        :return: The data_path of this ExportTableReq.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this ExportTableReq.

        导出数据的储存路径（当前仅支持将数据存储在OBS上，且OBS路径须以s3a开头）。另外，“export_mode”配置为“errorifexists”时，该路径下的文件夹须不存在，如请求样例中的“test”文件夹。

        :param data_path: The data_path of this ExportTableReq.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def data_type(self):
        """Gets the data_type of this ExportTableReq.

        导出数据的类型（当前仅支持csv格式数据）。

        :return: The data_type of this ExportTableReq.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ExportTableReq.

        导出数据的类型（当前仅支持csv格式数据）。

        :param data_type: The data_type of this ExportTableReq.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def database_name(self):
        """Gets the database_name of this ExportTableReq.

        被导出数据的表所在的数据库名称。

        :return: The database_name of this ExportTableReq.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ExportTableReq.

        被导出数据的表所在的数据库名称。

        :param database_name: The database_name of this ExportTableReq.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ExportTableReq.

        被导出数据的表名称。

        :return: The table_name of this ExportTableReq.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ExportTableReq.

        被导出数据的表名称。

        :param table_name: The table_name of this ExportTableReq.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def compress(self):
        """Gets the compress of this ExportTableReq.

        导出数据的压缩方法。目前支持gzip、bzip2、deflate压缩方式；若不希望压缩，则输入none。

        :return: The compress of this ExportTableReq.
        :rtype: str
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this ExportTableReq.

        导出数据的压缩方法。目前支持gzip、bzip2、deflate压缩方式；若不希望压缩，则输入none。

        :param compress: The compress of this ExportTableReq.
        :type compress: str
        """
        self._compress = compress

    @property
    def queue_name(self):
        """Gets the queue_name of this ExportTableReq.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :return: The queue_name of this ExportTableReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ExportTableReq.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :param queue_name: The queue_name of this ExportTableReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def export_mode(self):
        """Gets the export_mode of this ExportTableReq.

        导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。

        :return: The export_mode of this ExportTableReq.
        :rtype: str
        """
        return self._export_mode

    @export_mode.setter
    def export_mode(self, export_mode):
        """Sets the export_mode of this ExportTableReq.

        导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。

        :param export_mode: The export_mode of this ExportTableReq.
        :type export_mode: str
        """
        self._export_mode = export_mode

    @property
    def with_column_header(self):
        """Gets the with_column_header of this ExportTableReq.

        导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。

        :return: The with_column_header of this ExportTableReq.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this ExportTableReq.

        导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。

        :param with_column_header: The with_column_header of this ExportTableReq.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

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
        if not isinstance(other, ExportTableReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
