# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteAuraSqlStatementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'str'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        r"""ExecuteAuraSqlStatementResponse

        The model defined in huaweicloud sdk

        :param body: **参数解释**：执行SQL的响应信息。 **取值范围**： 异步或同步执行超时执行结果： ## StatementResponse - **status**（Integer）：请求整体执行状态。   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 同步执行正常返回结果： ## StatementResponse - **status**（Integer）：请求整体执行状态   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 - **results**（Array of StatementResult objects）：每条SQL执行结果。 --- ## StatementResult - **status**（String）：SQL执行状态。   - PGRES_TUPLES_OK：查询成功并含结果集。   - PGRES_COMMAND_OK：执行成功无结果。   - PGRES_FATAL_ERROR：执行失败。 - **statement_id**（String）：语句ID。 - **num_rows**（Integer）：查询结果总行数。 - **row_count**（Integer）：当前页实际返回行数。 - **page_no**（Integer）：当前页码。 - **page_count**（Integer）： 总页数。 - **err_code**（String）：错误码，0表示无错误，其他数值参见错误信息。 - **sql_state**（String）：SQL状态码。 - **message**（String）：执行信息或错误详情。 - **result_set**（Object，type: StatementResultSet）：仅查询成功时含有效数据，否则为空结构。 --- ## StatementResultSet - **columns**（Array of RowType objects）：列元数据列表。 - **rows**（Array of String arrays）：实际数据行，每行顺序与columns对应。 --- ## RowType - **name**（String）：列名。 - **table_id**（Integer）：表的ID。 - **column_id**（Integer）：列的ID。 - **format**（Integer）：格式。 - **type**（Integer）：PG类型OID。 - **size**（Integer）：大小。 - **type_mod**（Integer）：typemod。
        :type body: str
        """
        
        super().__init__()

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        r"""Gets the body of this ExecuteAuraSqlStatementResponse.

        **参数解释**：执行SQL的响应信息。 **取值范围**： 异步或同步执行超时执行结果： ## StatementResponse - **status**（Integer）：请求整体执行状态。   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 同步执行正常返回结果： ## StatementResponse - **status**（Integer）：请求整体执行状态   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 - **results**（Array of StatementResult objects）：每条SQL执行结果。 --- ## StatementResult - **status**（String）：SQL执行状态。   - PGRES_TUPLES_OK：查询成功并含结果集。   - PGRES_COMMAND_OK：执行成功无结果。   - PGRES_FATAL_ERROR：执行失败。 - **statement_id**（String）：语句ID。 - **num_rows**（Integer）：查询结果总行数。 - **row_count**（Integer）：当前页实际返回行数。 - **page_no**（Integer）：当前页码。 - **page_count**（Integer）： 总页数。 - **err_code**（String）：错误码，0表示无错误，其他数值参见错误信息。 - **sql_state**（String）：SQL状态码。 - **message**（String）：执行信息或错误详情。 - **result_set**（Object，type: StatementResultSet）：仅查询成功时含有效数据，否则为空结构。 --- ## StatementResultSet - **columns**（Array of RowType objects）：列元数据列表。 - **rows**（Array of String arrays）：实际数据行，每行顺序与columns对应。 --- ## RowType - **name**（String）：列名。 - **table_id**（Integer）：表的ID。 - **column_id**（Integer）：列的ID。 - **format**（Integer）：格式。 - **type**（Integer）：PG类型OID。 - **size**（Integer）：大小。 - **type_mod**（Integer）：typemod。

        :return: The body of this ExecuteAuraSqlStatementResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExecuteAuraSqlStatementResponse.

        **参数解释**：执行SQL的响应信息。 **取值范围**： 异步或同步执行超时执行结果： ## StatementResponse - **status**（Integer）：请求整体执行状态。   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 同步执行正常返回结果： ## StatementResponse - **status**（Integer）：请求整体执行状态   - 0：成功。   - -1：失败。   - 1： 执行中。   - 2：执行完成但无结果集。   - 3：排队等待中。   - 4：语句未正常执行。 - **session_id**（String，UUID）：当前执行会话唯一标识。 - **statement_id**（String，UUID）：本次语句执行唯一标识。 - **results**（Array of StatementResult objects）：每条SQL执行结果。 --- ## StatementResult - **status**（String）：SQL执行状态。   - PGRES_TUPLES_OK：查询成功并含结果集。   - PGRES_COMMAND_OK：执行成功无结果。   - PGRES_FATAL_ERROR：执行失败。 - **statement_id**（String）：语句ID。 - **num_rows**（Integer）：查询结果总行数。 - **row_count**（Integer）：当前页实际返回行数。 - **page_no**（Integer）：当前页码。 - **page_count**（Integer）： 总页数。 - **err_code**（String）：错误码，0表示无错误，其他数值参见错误信息。 - **sql_state**（String）：SQL状态码。 - **message**（String）：执行信息或错误详情。 - **result_set**（Object，type: StatementResultSet）：仅查询成功时含有效数据，否则为空结构。 --- ## StatementResultSet - **columns**（Array of RowType objects）：列元数据列表。 - **rows**（Array of String arrays）：实际数据行，每行顺序与columns对应。 --- ## RowType - **name**（String）：列名。 - **table_id**（Integer）：表的ID。 - **column_id**（Integer）：列的ID。 - **format**（Integer）：格式。 - **type**（Integer）：PG类型OID。 - **size**（Integer）：大小。 - **type_mod**（Integer）：typemod。

        :param body: The body of this ExecuteAuraSqlStatementResponse.
        :type body: str
        """
        self._body = body

    def to_dict(self):
        import warnings
        warnings.warn("ExecuteAuraSqlStatementResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ExecuteAuraSqlStatementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
