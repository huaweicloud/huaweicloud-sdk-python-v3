# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlResultResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_format': 'str',
        'result_path': 'str',
        'result_records': 'int',
        'result_bytes': 'int',
        'execution_profile_path': 'str'
    }

    attribute_map = {
        'result_format': 'result_format',
        'result_path': 'result_path',
        'result_records': 'result_records',
        'result_bytes': 'result_bytes',
        'execution_profile_path': 'execution_profile_path'
    }

    def __init__(self, result_format=None, result_path=None, result_records=None, result_bytes=None, execution_profile_path=None):
        r"""SparkSqlResultResponse

        The model defined in huaweicloud sdk

        :param result_format: **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv、arrow。
        :type result_format: str
        :param result_path: **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。
        :type result_path: str
        :param result_records: **参数解释**：查询结果行数，表示SQL查询返回的数据行数。
        :type result_records: int
        :param result_bytes: **参数解释**：查询结果字节数，表示SQL查询返回的数据大小。
        :type result_bytes: int
        :param execution_profile_path: **参数解释**：作业执行计划的存储路径，用于存储作业的执行计划信息。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_profile/{statement_id}/。
        :type execution_profile_path: str
        """
        
        

        self._result_format = None
        self._result_path = None
        self._result_records = None
        self._result_bytes = None
        self._execution_profile_path = None
        self.discriminator = None

        if result_format is not None:
            self.result_format = result_format
        if result_path is not None:
            self.result_path = result_path
        if result_records is not None:
            self.result_records = result_records
        if result_bytes is not None:
            self.result_bytes = result_bytes
        if execution_profile_path is not None:
            self.execution_profile_path = execution_profile_path

    @property
    def result_format(self):
        r"""Gets the result_format of this SparkSqlResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv、arrow。

        :return: The result_format of this SparkSqlResultResponse.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        r"""Sets the result_format of this SparkSqlResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv、arrow。

        :param result_format: The result_format of this SparkSqlResultResponse.
        :type result_format: str
        """
        self._result_format = result_format

    @property
    def result_path(self):
        r"""Gets the result_path of this SparkSqlResultResponse.

        **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。

        :return: The result_path of this SparkSqlResultResponse.
        :rtype: str
        """
        return self._result_path

    @result_path.setter
    def result_path(self, result_path):
        r"""Sets the result_path of this SparkSqlResultResponse.

        **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。

        :param result_path: The result_path of this SparkSqlResultResponse.
        :type result_path: str
        """
        self._result_path = result_path

    @property
    def result_records(self):
        r"""Gets the result_records of this SparkSqlResultResponse.

        **参数解释**：查询结果行数，表示SQL查询返回的数据行数。

        :return: The result_records of this SparkSqlResultResponse.
        :rtype: int
        """
        return self._result_records

    @result_records.setter
    def result_records(self, result_records):
        r"""Sets the result_records of this SparkSqlResultResponse.

        **参数解释**：查询结果行数，表示SQL查询返回的数据行数。

        :param result_records: The result_records of this SparkSqlResultResponse.
        :type result_records: int
        """
        self._result_records = result_records

    @property
    def result_bytes(self):
        r"""Gets the result_bytes of this SparkSqlResultResponse.

        **参数解释**：查询结果字节数，表示SQL查询返回的数据大小。

        :return: The result_bytes of this SparkSqlResultResponse.
        :rtype: int
        """
        return self._result_bytes

    @result_bytes.setter
    def result_bytes(self, result_bytes):
        r"""Sets the result_bytes of this SparkSqlResultResponse.

        **参数解释**：查询结果字节数，表示SQL查询返回的数据大小。

        :param result_bytes: The result_bytes of this SparkSqlResultResponse.
        :type result_bytes: int
        """
        self._result_bytes = result_bytes

    @property
    def execution_profile_path(self):
        r"""Gets the execution_profile_path of this SparkSqlResultResponse.

        **参数解释**：作业执行计划的存储路径，用于存储作业的执行计划信息。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_profile/{statement_id}/。

        :return: The execution_profile_path of this SparkSqlResultResponse.
        :rtype: str
        """
        return self._execution_profile_path

    @execution_profile_path.setter
    def execution_profile_path(self, execution_profile_path):
        r"""Sets the execution_profile_path of this SparkSqlResultResponse.

        **参数解释**：作业执行计划的存储路径，用于存储作业的执行计划信息。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_profile/{statement_id}/。

        :param execution_profile_path: The execution_profile_path of this SparkSqlResultResponse.
        :type execution_profile_path: str
        """
        self._execution_profile_path = execution_profile_path

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
        if not isinstance(other, SparkSqlResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
