# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewSqlJobResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'row_count': 'int',
        'input_size': 'int',
        'schema': 'list[dict(str, str)]',
        'rows': 'list[list[object]]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'row_count': 'row_count',
        'input_size': 'input_size',
        'schema': 'schema',
        'rows': 'rows'
    }

    def __init__(self, is_success=None, message=None, job_id=None, job_type=None, row_count=None, input_size=None, schema=None, rows=None):
        r"""PreviewSqlJobResultResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_id: 系统提示信息，执行成功时，信息可能为空。
        :type job_id: str
        :param job_type: 作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT。  目前仅支持查看“QUERY”类型作业的执行结果。
        :type job_type: str
        :param row_count: 作业结果总条数。
        :type row_count: int
        :param input_size: 作业执行过程中扫描的数据量。
        :type input_size: int
        :param schema: 作业结果列名称和类型。
        :type schema: list[dict(str, str)]
        :param rows: 作业结果集。
        :type rows: list[list[object]]
        """
        
        super(PreviewSqlJobResultResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._job_type = None
        self._row_count = None
        self._input_size = None
        self._schema = None
        self._rows = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if row_count is not None:
            self.row_count = row_count
        if input_size is not None:
            self.input_size = input_size
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows

    @property
    def is_success(self):
        r"""Gets the is_success of this PreviewSqlJobResultResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this PreviewSqlJobResultResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this PreviewSqlJobResultResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this PreviewSqlJobResultResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this PreviewSqlJobResultResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this PreviewSqlJobResultResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this PreviewSqlJobResultResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this PreviewSqlJobResultResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        r"""Gets the job_id of this PreviewSqlJobResultResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The job_id of this PreviewSqlJobResultResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this PreviewSqlJobResultResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param job_id: The job_id of this PreviewSqlJobResultResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this PreviewSqlJobResultResponse.

        作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT。  目前仅支持查看“QUERY”类型作业的执行结果。

        :return: The job_type of this PreviewSqlJobResultResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this PreviewSqlJobResultResponse.

        作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT。  目前仅支持查看“QUERY”类型作业的执行结果。

        :param job_type: The job_type of this PreviewSqlJobResultResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def row_count(self):
        r"""Gets the row_count of this PreviewSqlJobResultResponse.

        作业结果总条数。

        :return: The row_count of this PreviewSqlJobResultResponse.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        r"""Sets the row_count of this PreviewSqlJobResultResponse.

        作业结果总条数。

        :param row_count: The row_count of this PreviewSqlJobResultResponse.
        :type row_count: int
        """
        self._row_count = row_count

    @property
    def input_size(self):
        r"""Gets the input_size of this PreviewSqlJobResultResponse.

        作业执行过程中扫描的数据量。

        :return: The input_size of this PreviewSqlJobResultResponse.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        r"""Sets the input_size of this PreviewSqlJobResultResponse.

        作业执行过程中扫描的数据量。

        :param input_size: The input_size of this PreviewSqlJobResultResponse.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def schema(self):
        r"""Gets the schema of this PreviewSqlJobResultResponse.

        作业结果列名称和类型。

        :return: The schema of this PreviewSqlJobResultResponse.
        :rtype: list[dict(str, str)]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this PreviewSqlJobResultResponse.

        作业结果列名称和类型。

        :param schema: The schema of this PreviewSqlJobResultResponse.
        :type schema: list[dict(str, str)]
        """
        self._schema = schema

    @property
    def rows(self):
        r"""Gets the rows of this PreviewSqlJobResultResponse.

        作业结果集。

        :return: The rows of this PreviewSqlJobResultResponse.
        :rtype: list[list[object]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this PreviewSqlJobResultResponse.

        作业结果集。

        :param rows: The rows of this PreviewSqlJobResultResponse.
        :type rows: list[list[object]]
        """
        self._rows = rows

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
        if not isinstance(other, PreviewSqlJobResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
