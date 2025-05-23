# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSqlJobResultRequestBody:

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
        'compress': 'str',
        'data_type': 'str',
        'queue_name': 'str',
        'export_mode': 'str',
        'with_column_header': 'bool',
        'limit_num': 'int',
        'encoding_type': 'str',
        'quote_char': 'str',
        'escape_char': 'str'
    }

    attribute_map = {
        'data_path': 'data_path',
        'compress': 'compress',
        'data_type': 'data_type',
        'queue_name': 'queue_name',
        'export_mode': 'export_mode',
        'with_column_header': 'with_column_header',
        'limit_num': 'limit_num',
        'encoding_type': 'encoding_type',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char'
    }

    def __init__(self, data_path=None, compress=None, data_type=None, queue_name=None, export_mode=None, with_column_header=None, limit_num=None, encoding_type=None, quote_char=None, escape_char=None):
        r"""ExportSqlJobResultRequestBody

        The model defined in huaweicloud sdk

        :param data_path: ExportResult
        :type data_path: str
        :param compress: 导出数据的压缩格式，目前支持gzip，bzip2和deflate压缩方式； 默认值为none，表示不压缩。
        :type compress: str
        :param data_type: 导出数据的存储格式，暂时只支持csv格式。
        :type data_type: str
        :param queue_name: 指定执行该任务的队列。若不指定队列，将采用default队列执行操作。
        :type queue_name: str
        :param export_mode: 导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。
        :type export_mode: str
        :param with_column_header: 导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。
        :type with_column_header: bool
        :param limit_num: 导出数据条数，默认为0表示全部
        :type limit_num: int
        :param encoding_type: 导出数据的编码格式。支持\&quot;utf-8\&quot;，\&quot;gb2312\&quot;，\&quot;gbk\&quot;三种，如果不填写默认为\&quot;utf-8\&quot;。
        :type encoding_type: str
        :param quote_char: 用户自定义引用字符
        :type quote_char: str
        :param escape_char: 用户自定义转义字符
        :type escape_char: str
        """
        
        

        self._data_path = None
        self._compress = None
        self._data_type = None
        self._queue_name = None
        self._export_mode = None
        self._with_column_header = None
        self._limit_num = None
        self._encoding_type = None
        self._quote_char = None
        self._escape_char = None
        self.discriminator = None

        self.data_path = data_path
        if compress is not None:
            self.compress = compress
        self.data_type = data_type
        if queue_name is not None:
            self.queue_name = queue_name
        if export_mode is not None:
            self.export_mode = export_mode
        if with_column_header is not None:
            self.with_column_header = with_column_header
        if limit_num is not None:
            self.limit_num = limit_num
        if encoding_type is not None:
            self.encoding_type = encoding_type
        if quote_char is not None:
            self.quote_char = quote_char
        if escape_char is not None:
            self.escape_char = escape_char

    @property
    def data_path(self):
        r"""Gets the data_path of this ExportSqlJobResultRequestBody.

        ExportResult

        :return: The data_path of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        r"""Sets the data_path of this ExportSqlJobResultRequestBody.

        ExportResult

        :param data_path: The data_path of this ExportSqlJobResultRequestBody.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def compress(self):
        r"""Gets the compress of this ExportSqlJobResultRequestBody.

        导出数据的压缩格式，目前支持gzip，bzip2和deflate压缩方式； 默认值为none，表示不压缩。

        :return: The compress of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        r"""Sets the compress of this ExportSqlJobResultRequestBody.

        导出数据的压缩格式，目前支持gzip，bzip2和deflate压缩方式； 默认值为none，表示不压缩。

        :param compress: The compress of this ExportSqlJobResultRequestBody.
        :type compress: str
        """
        self._compress = compress

    @property
    def data_type(self):
        r"""Gets the data_type of this ExportSqlJobResultRequestBody.

        导出数据的存储格式，暂时只支持csv格式。

        :return: The data_type of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ExportSqlJobResultRequestBody.

        导出数据的存储格式，暂时只支持csv格式。

        :param data_type: The data_type of this ExportSqlJobResultRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ExportSqlJobResultRequestBody.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :return: The queue_name of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ExportSqlJobResultRequestBody.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :param queue_name: The queue_name of this ExportSqlJobResultRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def export_mode(self):
        r"""Gets the export_mode of this ExportSqlJobResultRequestBody.

        导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。

        :return: The export_mode of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._export_mode

    @export_mode.setter
    def export_mode(self, export_mode):
        r"""Sets the export_mode of this ExportSqlJobResultRequestBody.

        导出模式，目前支持“ErrorIfExists”，“Overwrite”，不指定“export_mode”则默认为“ErrorIfExists”。  “ErrorIfExists”：存在即报错。指定的导出目录必须不存在，如果指定目录已经存在，系统将返回错误信息，无法执行导出操作。 “Overwrite”：覆盖。在指定目录下新建文件，会删除已有文件。

        :param export_mode: The export_mode of this ExportSqlJobResultRequestBody.
        :type export_mode: str
        """
        self._export_mode = export_mode

    @property
    def with_column_header(self):
        r"""Gets the with_column_header of this ExportSqlJobResultRequestBody.

        导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。

        :return: The with_column_header of this ExportSqlJobResultRequestBody.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        r"""Sets the with_column_header of this ExportSqlJobResultRequestBody.

        导出csv格式数据时，是否导出列名。  设置为“true”，表示导出列名。 设置为“false”，表示不导出列名。 若为空，默认为“false”。

        :param with_column_header: The with_column_header of this ExportSqlJobResultRequestBody.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def limit_num(self):
        r"""Gets the limit_num of this ExportSqlJobResultRequestBody.

        导出数据条数，默认为0表示全部

        :return: The limit_num of this ExportSqlJobResultRequestBody.
        :rtype: int
        """
        return self._limit_num

    @limit_num.setter
    def limit_num(self, limit_num):
        r"""Sets the limit_num of this ExportSqlJobResultRequestBody.

        导出数据条数，默认为0表示全部

        :param limit_num: The limit_num of this ExportSqlJobResultRequestBody.
        :type limit_num: int
        """
        self._limit_num = limit_num

    @property
    def encoding_type(self):
        r"""Gets the encoding_type of this ExportSqlJobResultRequestBody.

        导出数据的编码格式。支持\"utf-8\"，\"gb2312\"，\"gbk\"三种，如果不填写默认为\"utf-8\"。

        :return: The encoding_type of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        r"""Sets the encoding_type of this ExportSqlJobResultRequestBody.

        导出数据的编码格式。支持\"utf-8\"，\"gb2312\"，\"gbk\"三种，如果不填写默认为\"utf-8\"。

        :param encoding_type: The encoding_type of this ExportSqlJobResultRequestBody.
        :type encoding_type: str
        """
        self._encoding_type = encoding_type

    @property
    def quote_char(self):
        r"""Gets the quote_char of this ExportSqlJobResultRequestBody.

        用户自定义引用字符

        :return: The quote_char of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        r"""Sets the quote_char of this ExportSqlJobResultRequestBody.

        用户自定义引用字符

        :param quote_char: The quote_char of this ExportSqlJobResultRequestBody.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        r"""Gets the escape_char of this ExportSqlJobResultRequestBody.

        用户自定义转义字符

        :return: The escape_char of this ExportSqlJobResultRequestBody.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        r"""Sets the escape_char of this ExportSqlJobResultRequestBody.

        用户自定义转义字符

        :param escape_char: The escape_char of this ExportSqlJobResultRequestBody.
        :type escape_char: str
        """
        self._escape_char = escape_char

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
        if not isinstance(other, ExportSqlJobResultRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
