# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewSparkSqlResultResponse(SdkResponse):

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
        'schema': 'list[SparkSqlSchemaItem]',
        'rows': 'list[list[str]]'
    }

    attribute_map = {
        'result_format': 'result_format',
        'result_path': 'result_path',
        'schema': 'schema',
        'rows': 'rows'
    }

    def __init__(self, result_format=None, result_path=None, schema=None, rows=None):
        r"""PreviewSparkSqlResultResponse

        The model defined in huaweicloud sdk

        :param result_format: **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv，arrow。
        :type result_format: str
        :param result_path: **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。
        :type result_path: str
        :param schema: **参数解释**：结果数据的列结构定义，包含列名和列类型信息。数组中的每个元素为SparkSqlSchemaItem对象。
        :type schema: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlSchemaItem`]
        :param rows: **参数解释**：作业结果集，包含查询返回的实际数据行。每行为一个数组，对应schema中定义的列顺序。
        :type rows: list[list[str]]
        """
        
        super().__init__()

        self._result_format = None
        self._result_path = None
        self._schema = None
        self._rows = None
        self.discriminator = None

        if result_format is not None:
            self.result_format = result_format
        if result_path is not None:
            self.result_path = result_path
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows

    @property
    def result_format(self):
        r"""Gets the result_format of this PreviewSparkSqlResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv，arrow。

        :return: The result_format of this PreviewSparkSqlResultResponse.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        r"""Sets the result_format of this PreviewSparkSqlResultResponse.

        **参数解释**：查询类SQL结果格式，用于指定结果的存储格式。 **取值范围**：csv，arrow。

        :param result_format: The result_format of this PreviewSparkSqlResultResponse.
        :type result_format: str
        """
        self._result_format = result_format

    @property
    def result_path(self):
        r"""Gets the result_path of this PreviewSparkSqlResultResponse.

        **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。

        :return: The result_path of this PreviewSparkSqlResultResponse.
        :rtype: str
        """
        return self._result_path

    @result_path.setter
    def result_path(self, result_path):
        r"""Sets the result_path of this PreviewSparkSqlResultResponse.

        **参数解释**：查询类SQL结果的OBS路径，用于存储SQL查询的结果数据。 **取值范围**：采用OBS路径格式，例如：obs://bucket/aidatalake/workspace_xxx/spark/endpoint_xxx/jobs/sql_result/{statement_id}/result.csv。

        :param result_path: The result_path of this PreviewSparkSqlResultResponse.
        :type result_path: str
        """
        self._result_path = result_path

    @property
    def schema(self):
        r"""Gets the schema of this PreviewSparkSqlResultResponse.

        **参数解释**：结果数据的列结构定义，包含列名和列类型信息。数组中的每个元素为SparkSqlSchemaItem对象。

        :return: The schema of this PreviewSparkSqlResultResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlSchemaItem`]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this PreviewSparkSqlResultResponse.

        **参数解释**：结果数据的列结构定义，包含列名和列类型信息。数组中的每个元素为SparkSqlSchemaItem对象。

        :param schema: The schema of this PreviewSparkSqlResultResponse.
        :type schema: list[:class:`huaweicloudsdkaidatalake.v2.SparkSqlSchemaItem`]
        """
        self._schema = schema

    @property
    def rows(self):
        r"""Gets the rows of this PreviewSparkSqlResultResponse.

        **参数解释**：作业结果集，包含查询返回的实际数据行。每行为一个数组，对应schema中定义的列顺序。

        :return: The rows of this PreviewSparkSqlResultResponse.
        :rtype: list[list[str]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this PreviewSparkSqlResultResponse.

        **参数解释**：作业结果集，包含查询返回的实际数据行。每行为一个数组，对应schema中定义的列顺序。

        :param rows: The rows of this PreviewSparkSqlResultResponse.
        :type rows: list[list[str]]
        """
        self._rows = rows

    def to_dict(self):
        import warnings
        warnings.warn("PreviewSparkSqlResultResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, PreviewSparkSqlResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
