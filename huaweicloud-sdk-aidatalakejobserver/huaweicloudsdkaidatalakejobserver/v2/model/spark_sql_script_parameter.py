# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkSqlScriptParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'sql_scripting_file': 'str',
        'sql_scripting_parameters': 'list[SparkJobSqlScriptParameter]',
        'dependency_jars': 'list[str]',
        'sql_scripting_result_to_obs': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'sql_scripting_file': 'sql_scripting_file',
        'sql_scripting_parameters': 'sql_scripting_parameters',
        'dependency_jars': 'dependency_jars',
        'sql_scripting_result_to_obs': 'sql_scripting_result_to_obs'
    }

    def __init__(self, type=None, sql_scripting_file=None, sql_scripting_parameters=None, dependency_jars=None, sql_scripting_result_to_obs=None):
        r"""SparkSqlScriptParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 spark_sql_scripting_job。 **取值范围**：不涉及。 **默认取值**：spark_sql_scripting_job。 
        :type type: str
        :param sql_scripting_file: **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 
        :type sql_scripting_file: str
        :param sql_scripting_parameters: **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        :param dependency_jars: **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 
        :type dependency_jars: list[str]
        :param sql_scripting_result_to_obs: **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 
        :type sql_scripting_result_to_obs: bool
        """
        
        

        self._type = None
        self._sql_scripting_file = None
        self._sql_scripting_parameters = None
        self._dependency_jars = None
        self._sql_scripting_result_to_obs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.sql_scripting_file = sql_scripting_file
        if sql_scripting_parameters is not None:
            self.sql_scripting_parameters = sql_scripting_parameters
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if sql_scripting_result_to_obs is not None:
            self.sql_scripting_result_to_obs = sql_scripting_result_to_obs

    @property
    def type(self):
        r"""Gets the type of this SparkSqlScriptParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 spark_sql_scripting_job。 **取值范围**：不涉及。 **默认取值**：spark_sql_scripting_job。 

        :return: The type of this SparkSqlScriptParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SparkSqlScriptParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 spark_sql_scripting_job。 **取值范围**：不涉及。 **默认取值**：spark_sql_scripting_job。 

        :param type: The type of this SparkSqlScriptParameter.
        :type type: str
        """
        self._type = type

    @property
    def sql_scripting_file(self):
        r"""Gets the sql_scripting_file of this SparkSqlScriptParameter.

        **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 

        :return: The sql_scripting_file of this SparkSqlScriptParameter.
        :rtype: str
        """
        return self._sql_scripting_file

    @sql_scripting_file.setter
    def sql_scripting_file(self, sql_scripting_file):
        r"""Sets the sql_scripting_file of this SparkSqlScriptParameter.

        **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 

        :param sql_scripting_file: The sql_scripting_file of this SparkSqlScriptParameter.
        :type sql_scripting_file: str
        """
        self._sql_scripting_file = sql_scripting_file

    @property
    def sql_scripting_parameters(self):
        r"""Gets the sql_scripting_parameters of this SparkSqlScriptParameter.

        **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :return: The sql_scripting_parameters of this SparkSqlScriptParameter.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        """
        return self._sql_scripting_parameters

    @sql_scripting_parameters.setter
    def sql_scripting_parameters(self, sql_scripting_parameters):
        r"""Sets the sql_scripting_parameters of this SparkSqlScriptParameter.

        **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :param sql_scripting_parameters: The sql_scripting_parameters of this SparkSqlScriptParameter.
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        """
        self._sql_scripting_parameters = sql_scripting_parameters

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this SparkSqlScriptParameter.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :return: The dependency_jars of this SparkSqlScriptParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this SparkSqlScriptParameter.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :param dependency_jars: The dependency_jars of this SparkSqlScriptParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def sql_scripting_result_to_obs(self):
        r"""Gets the sql_scripting_result_to_obs of this SparkSqlScriptParameter.

        **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 

        :return: The sql_scripting_result_to_obs of this SparkSqlScriptParameter.
        :rtype: bool
        """
        return self._sql_scripting_result_to_obs

    @sql_scripting_result_to_obs.setter
    def sql_scripting_result_to_obs(self, sql_scripting_result_to_obs):
        r"""Sets the sql_scripting_result_to_obs of this SparkSqlScriptParameter.

        **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 

        :param sql_scripting_result_to_obs: The sql_scripting_result_to_obs of this SparkSqlScriptParameter.
        :type sql_scripting_result_to_obs: bool
        """
        self._sql_scripting_result_to_obs = sql_scripting_result_to_obs

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
        if not isinstance(other, SparkSqlScriptParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
