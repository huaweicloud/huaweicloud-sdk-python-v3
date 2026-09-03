# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkScriptSQLParameterResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_scripting_file': 'str',
        'sql_scripting_parameters': 'list[SparkJobSqlScriptParameter]',
        'dependency_jars': 'list[str]',
        'sql_scripting_result_to_obs': 'bool',
        'result': 'SparkSqlScriptingResultResponse'
    }

    attribute_map = {
        'sql_scripting_file': 'sql_scripting_file',
        'sql_scripting_parameters': 'sql_scripting_parameters',
        'dependency_jars': 'dependency_jars',
        'sql_scripting_result_to_obs': 'sql_scripting_result_to_obs',
        'result': 'result'
    }

    def __init__(self, sql_scripting_file=None, sql_scripting_parameters=None, dependency_jars=None, sql_scripting_result_to_obs=None, result=None):
        r"""ShowSparkScriptSQLParameterResponse

        The model defined in huaweicloud sdk

        :param sql_scripting_file: **参数解释**：Spark Script SQL类型作业的SQL脚本文件OBS路径，用于指定作业执行的SQL脚本。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/sparksql/script.sql。 
        :type sql_scripting_file: str
        :param sql_scripting_parameters: **参数解释**：SQL脚本占位符参数列表，用于为SQL脚本中的占位符传递参数值。 
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalake.v2.SparkJobSqlScriptParameter`]
        :param dependency_jars: **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 
        :type dependency_jars: list[str]
        :param sql_scripting_result_to_obs: **参数解释**：SQL脚本结果是否写入OBS，用于控制查询结果的输出方式。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 
        :type sql_scripting_result_to_obs: bool
        :param result: 
        :type result: :class:`huaweicloudsdkaidatalake.v2.SparkSqlScriptingResultResponse`
        """
        
        

        self._sql_scripting_file = None
        self._sql_scripting_parameters = None
        self._dependency_jars = None
        self._sql_scripting_result_to_obs = None
        self._result = None
        self.discriminator = None

        self.sql_scripting_file = sql_scripting_file
        if sql_scripting_parameters is not None:
            self.sql_scripting_parameters = sql_scripting_parameters
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if sql_scripting_result_to_obs is not None:
            self.sql_scripting_result_to_obs = sql_scripting_result_to_obs
        if result is not None:
            self.result = result

    @property
    def sql_scripting_file(self):
        r"""Gets the sql_scripting_file of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：Spark Script SQL类型作业的SQL脚本文件OBS路径，用于指定作业执行的SQL脚本。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/sparksql/script.sql。 

        :return: The sql_scripting_file of this ShowSparkScriptSQLParameterResponse.
        :rtype: str
        """
        return self._sql_scripting_file

    @sql_scripting_file.setter
    def sql_scripting_file(self, sql_scripting_file):
        r"""Sets the sql_scripting_file of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：Spark Script SQL类型作业的SQL脚本文件OBS路径，用于指定作业执行的SQL脚本。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/sparksql/script.sql。 

        :param sql_scripting_file: The sql_scripting_file of this ShowSparkScriptSQLParameterResponse.
        :type sql_scripting_file: str
        """
        self._sql_scripting_file = sql_scripting_file

    @property
    def sql_scripting_parameters(self):
        r"""Gets the sql_scripting_parameters of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：SQL脚本占位符参数列表，用于为SQL脚本中的占位符传递参数值。 

        :return: The sql_scripting_parameters of this ShowSparkScriptSQLParameterResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SparkJobSqlScriptParameter`]
        """
        return self._sql_scripting_parameters

    @sql_scripting_parameters.setter
    def sql_scripting_parameters(self, sql_scripting_parameters):
        r"""Sets the sql_scripting_parameters of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：SQL脚本占位符参数列表，用于为SQL脚本中的占位符传递参数值。 

        :param sql_scripting_parameters: The sql_scripting_parameters of this ShowSparkScriptSQLParameterResponse.
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalake.v2.SparkJobSqlScriptParameter`]
        """
        self._sql_scripting_parameters = sql_scripting_parameters

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 

        :return: The dependency_jars of this ShowSparkScriptSQLParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 

        :param dependency_jars: The dependency_jars of this ShowSparkScriptSQLParameterResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def sql_scripting_result_to_obs(self):
        r"""Gets the sql_scripting_result_to_obs of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：SQL脚本结果是否写入OBS，用于控制查询结果的输出方式。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 

        :return: The sql_scripting_result_to_obs of this ShowSparkScriptSQLParameterResponse.
        :rtype: bool
        """
        return self._sql_scripting_result_to_obs

    @sql_scripting_result_to_obs.setter
    def sql_scripting_result_to_obs(self, sql_scripting_result_to_obs):
        r"""Sets the sql_scripting_result_to_obs of this ShowSparkScriptSQLParameterResponse.

        **参数解释**：SQL脚本结果是否写入OBS，用于控制查询结果的输出方式。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 

        :param sql_scripting_result_to_obs: The sql_scripting_result_to_obs of this ShowSparkScriptSQLParameterResponse.
        :type sql_scripting_result_to_obs: bool
        """
        self._sql_scripting_result_to_obs = sql_scripting_result_to_obs

    @property
    def result(self):
        r"""Gets the result of this ShowSparkScriptSQLParameterResponse.

        :return: The result of this ShowSparkScriptSQLParameterResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSqlScriptingResultResponse`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowSparkScriptSQLParameterResponse.

        :param result: The result of this ShowSparkScriptSQLParameterResponse.
        :type result: :class:`huaweicloudsdkaidatalake.v2.SparkSqlScriptingResultResponse`
        """
        self._result = result

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
        if not isinstance(other, ShowSparkScriptSQLParameterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
