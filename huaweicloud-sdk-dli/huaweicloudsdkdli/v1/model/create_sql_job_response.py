# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlJobResponse(SdkResponse):

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
        'schema': 'list[object]',
        'rows': 'list[list[object]]',
        'job_mode': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'schema': 'schema',
        'rows': 'rows',
        'job_mode': 'job_mode'
    }

    def __init__(self, is_success=None, message=None, job_id=None, job_type=None, schema=None, rows=None, job_mode=None):
        r"""CreateSqlJobResponse

        The model defined in huaweicloud sdk

        :param is_success: 参数解释: 当“job_type”为“DCL”时，为请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: true,false 默认取值: 无
        :type is_success: bool
        :param message: 参数解释: 系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无
        :type message: str
        :param job_id: 参数解释: 此SQL语句将生成并提交一个新作业，返回此作业的ID，可用于获取作业状态和作业结果 示例: 8ecb0777-9c70-4529-9935-29ea0946039c 约束限制:  无 取值范围: 无 默认取值: 无
        :type job_id: str
        :param job_type: 参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无
        :type job_type: str
        :param schema: 参数解释:  当语句类型为DDL时，返回其结果的列名称及类型 示例: [{\&quot;col_name\&quot;: \&quot;string\&quot;},{\&quot;data_type\&quot;: \&quot;string\&quot;},{\&quot;comment\&quot;: \&quot;string\&quot;}] 约束限制:  无 取值范围: 无 默认取值: 无
        :type schema: list[object]
        :param rows: 参数解释:  当语句类型为DDL时，直接返回其执行结果 示例: [[\&quot;c1\&quot;,\&quot;int\&quot;,null],[\&quot;c2\&quot;,\&quot;string\&quot;,null]] 约束限制:  无 取值范围: 无 默认取值: 无
        :type rows: list[list[object]]
        :param job_mode: 参数解释:  表示作业执行方式，是同步还是异步的 示例: async 约束限制:  无 取值范围: async（异步） sync（同步） 默认取值: 无
        :type job_mode: str
        """
        
        super(CreateSqlJobResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._job_type = None
        self._schema = None
        self._rows = None
        self._job_mode = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows
        if job_mode is not None:
            self.job_mode = job_mode

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateSqlJobResponse.

        参数解释: 当“job_type”为“DCL”时，为请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: true,false 默认取值: 无

        :return: The is_success of this CreateSqlJobResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateSqlJobResponse.

        参数解释: 当“job_type”为“DCL”时，为请求执行是否成功。“true”表示请求执行成功 示例: true 约束限制:  无 取值范围: true,false 默认取值: 无

        :param is_success: The is_success of this CreateSqlJobResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateSqlJobResponse.

        参数解释: 系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The message of this CreateSqlJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateSqlJobResponse.

        参数解释: 系统提示信息，执行成功时，信息可能为空 示例: success 约束限制:  无 取值范围: 无 默认取值: 无

        :param message: The message of this CreateSqlJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateSqlJobResponse.

        参数解释: 此SQL语句将生成并提交一个新作业，返回此作业的ID，可用于获取作业状态和作业结果 示例: 8ecb0777-9c70-4529-9935-29ea0946039c 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The job_id of this CreateSqlJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateSqlJobResponse.

        参数解释: 此SQL语句将生成并提交一个新作业，返回此作业的ID，可用于获取作业状态和作业结果 示例: 8ecb0777-9c70-4529-9935-29ea0946039c 约束限制:  无 取值范围: 无 默认取值: 无

        :param job_id: The job_id of this CreateSqlJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateSqlJobResponse.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :return: The job_type of this CreateSqlJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateSqlJobResponse.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :param job_type: The job_type of this CreateSqlJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def schema(self):
        r"""Gets the schema of this CreateSqlJobResponse.

        参数解释:  当语句类型为DDL时，返回其结果的列名称及类型 示例: [{\"col_name\": \"string\"},{\"data_type\": \"string\"},{\"comment\": \"string\"}] 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The schema of this CreateSqlJobResponse.
        :rtype: list[object]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this CreateSqlJobResponse.

        参数解释:  当语句类型为DDL时，返回其结果的列名称及类型 示例: [{\"col_name\": \"string\"},{\"data_type\": \"string\"},{\"comment\": \"string\"}] 约束限制:  无 取值范围: 无 默认取值: 无

        :param schema: The schema of this CreateSqlJobResponse.
        :type schema: list[object]
        """
        self._schema = schema

    @property
    def rows(self):
        r"""Gets the rows of this CreateSqlJobResponse.

        参数解释:  当语句类型为DDL时，直接返回其执行结果 示例: [[\"c1\",\"int\",null],[\"c2\",\"string\",null]] 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The rows of this CreateSqlJobResponse.
        :rtype: list[list[object]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this CreateSqlJobResponse.

        参数解释:  当语句类型为DDL时，直接返回其执行结果 示例: [[\"c1\",\"int\",null],[\"c2\",\"string\",null]] 约束限制:  无 取值范围: 无 默认取值: 无

        :param rows: The rows of this CreateSqlJobResponse.
        :type rows: list[list[object]]
        """
        self._rows = rows

    @property
    def job_mode(self):
        r"""Gets the job_mode of this CreateSqlJobResponse.

        参数解释:  表示作业执行方式，是同步还是异步的 示例: async 约束限制:  无 取值范围: async（异步） sync（同步） 默认取值: 无

        :return: The job_mode of this CreateSqlJobResponse.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this CreateSqlJobResponse.

        参数解释:  表示作业执行方式，是同步还是异步的 示例: async 约束限制:  无 取值范围: async（异步） sync（同步） 默认取值: 无

        :param job_mode: The job_mode of this CreateSqlJobResponse.
        :type job_mode: str
        """
        self._job_mode = job_mode

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
        if not isinstance(other, CreateSqlJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
