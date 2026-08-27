# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJobArtifact:

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
        'main_class': 'str',
        'main_args': 'list[str]',
        'main_jar': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'dependency_archives': 'list[str]',
        'dependency_py_files': 'list[str]',
        'main_python_file': 'str',
        'sql_scripting_file': 'str',
        'sql_scripting_parameters': 'list[SparkJobSqlScriptParameter]',
        'sql_scripting_result_to_obs': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'main_class': 'main_class',
        'main_args': 'main_args',
        'main_jar': 'main_jar',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'dependency_archives': 'dependency_archives',
        'dependency_py_files': 'dependency_py_files',
        'main_python_file': 'main_python_file',
        'sql_scripting_file': 'sql_scripting_file',
        'sql_scripting_parameters': 'sql_scripting_parameters',
        'sql_scripting_result_to_obs': 'sql_scripting_result_to_obs'
    }

    def __init__(self, type=None, main_class=None, main_args=None, main_jar=None, dependency_jars=None, dependency_files=None, dependency_archives=None, dependency_py_files=None, main_python_file=None, sql_scripting_file=None, sql_scripting_parameters=None, sql_scripting_result_to_obs=None):
        r"""SparkJobArtifact

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param main_class: **参数解释**：主类名称，用于指定Spark Jar作业的入口类。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。 
        :type main_class: str
        :param main_args: **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 
        :type main_args: list[str]
        :param main_jar: **参数解释**：主Jar包路径，用于指定Spark Jar作业主类所在Jar包的OBS路径。当作业类型为“spark_jar_job”时，此参数必填。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket_name/path/to/jar.jar”。 **默认取值**：不涉及。 
        :type main_jar: str
        :param dependency_jars: **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 
        :type dependency_files: list[str]
        :param dependency_archives: **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 
        :type dependency_archives: list[str]
        :param dependency_py_files: **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 
        :type dependency_py_files: list[str]
        :param main_python_file: **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 
        :type main_python_file: str
        :param sql_scripting_file: **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 
        :type sql_scripting_file: str
        :param sql_scripting_parameters: **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        :param sql_scripting_result_to_obs: **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 
        :type sql_scripting_result_to_obs: bool
        """
        
        

        self._type = None
        self._main_class = None
        self._main_args = None
        self._main_jar = None
        self._dependency_jars = None
        self._dependency_files = None
        self._dependency_archives = None
        self._dependency_py_files = None
        self._main_python_file = None
        self._sql_scripting_file = None
        self._sql_scripting_parameters = None
        self._sql_scripting_result_to_obs = None
        self.discriminator = None

        self.type = type
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if main_jar is not None:
            self.main_jar = main_jar
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if dependency_archives is not None:
            self.dependency_archives = dependency_archives
        if dependency_py_files is not None:
            self.dependency_py_files = dependency_py_files
        self.main_python_file = main_python_file
        self.sql_scripting_file = sql_scripting_file
        if sql_scripting_parameters is not None:
            self.sql_scripting_parameters = sql_scripting_parameters
        if sql_scripting_result_to_obs is not None:
            self.sql_scripting_result_to_obs = sql_scripting_result_to_obs

    @property
    def type(self):
        r"""Gets the type of this SparkJobArtifact.

        :return: The type of this SparkJobArtifact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SparkJobArtifact.

        :param type: The type of this SparkJobArtifact.
        :type type: str
        """
        self._type = type

    @property
    def main_class(self):
        r"""Gets the main_class of this SparkJobArtifact.

        **参数解释**：主类名称，用于指定Spark Jar作业的入口类。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。 

        :return: The main_class of this SparkJobArtifact.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this SparkJobArtifact.

        **参数解释**：主类名称，用于指定Spark Jar作业的入口类。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。 

        :param main_class: The main_class of this SparkJobArtifact.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this SparkJobArtifact.

        **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 

        :return: The main_args of this SparkJobArtifact.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this SparkJobArtifact.

        **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 

        :param main_args: The main_args of this SparkJobArtifact.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def main_jar(self):
        r"""Gets the main_jar of this SparkJobArtifact.

        **参数解释**：主Jar包路径，用于指定Spark Jar作业主类所在Jar包的OBS路径。当作业类型为“spark_jar_job”时，此参数必填。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket_name/path/to/jar.jar”。 **默认取值**：不涉及。 

        :return: The main_jar of this SparkJobArtifact.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this SparkJobArtifact.

        **参数解释**：主Jar包路径，用于指定Spark Jar作业主类所在Jar包的OBS路径。当作业类型为“spark_jar_job”时，此参数必填。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket_name/path/to/jar.jar”。 **默认取值**：不涉及。 

        :param main_jar: The main_jar of this SparkJobArtifact.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this SparkJobArtifact.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :return: The dependency_jars of this SparkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this SparkJobArtifact.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :param dependency_jars: The dependency_jars of this SparkJobArtifact.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this SparkJobArtifact.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 

        :return: The dependency_files of this SparkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this SparkJobArtifact.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 

        :param dependency_files: The dependency_files of this SparkJobArtifact.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def dependency_archives(self):
        r"""Gets the dependency_archives of this SparkJobArtifact.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 

        :return: The dependency_archives of this SparkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_archives

    @dependency_archives.setter
    def dependency_archives(self, dependency_archives):
        r"""Sets the dependency_archives of this SparkJobArtifact.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 

        :param dependency_archives: The dependency_archives of this SparkJobArtifact.
        :type dependency_archives: list[str]
        """
        self._dependency_archives = dependency_archives

    @property
    def dependency_py_files(self):
        r"""Gets the dependency_py_files of this SparkJobArtifact.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 

        :return: The dependency_py_files of this SparkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_py_files

    @dependency_py_files.setter
    def dependency_py_files(self, dependency_py_files):
        r"""Sets the dependency_py_files of this SparkJobArtifact.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 

        :param dependency_py_files: The dependency_py_files of this SparkJobArtifact.
        :type dependency_py_files: list[str]
        """
        self._dependency_py_files = dependency_py_files

    @property
    def main_python_file(self):
        r"""Gets the main_python_file of this SparkJobArtifact.

        **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 

        :return: The main_python_file of this SparkJobArtifact.
        :rtype: str
        """
        return self._main_python_file

    @main_python_file.setter
    def main_python_file(self, main_python_file):
        r"""Sets the main_python_file of this SparkJobArtifact.

        **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 

        :param main_python_file: The main_python_file of this SparkJobArtifact.
        :type main_python_file: str
        """
        self._main_python_file = main_python_file

    @property
    def sql_scripting_file(self):
        r"""Gets the sql_scripting_file of this SparkJobArtifact.

        **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 

        :return: The sql_scripting_file of this SparkJobArtifact.
        :rtype: str
        """
        return self._sql_scripting_file

    @sql_scripting_file.setter
    def sql_scripting_file(self, sql_scripting_file):
        r"""Sets the sql_scripting_file of this SparkJobArtifact.

        **参数解释**：SQL脚本文件路径，用于指定Spark Script SQL作业的脚本文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/sparksqlscript/script.sql”。 **默认取值**：不涉及。 

        :param sql_scripting_file: The sql_scripting_file of this SparkJobArtifact.
        :type sql_scripting_file: str
        """
        self._sql_scripting_file = sql_scripting_file

    @property
    def sql_scripting_parameters(self):
        r"""Gets the sql_scripting_parameters of this SparkJobArtifact.

        **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :return: The sql_scripting_parameters of this SparkJobArtifact.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        """
        return self._sql_scripting_parameters

    @sql_scripting_parameters.setter
    def sql_scripting_parameters(self, sql_scripting_parameters):
        r"""Sets the sql_scripting_parameters of this SparkJobArtifact.

        **参数解释**：SQL脚本占位符参数列表，用于配置SQL脚本中的参数化变量。数组中的每个元素为SparkJobSqlScriptParameter对象，包含占位符的键、值和类型信息。 **约束限制**：占位符参数数量不能超过16条。 

        :param sql_scripting_parameters: The sql_scripting_parameters of this SparkJobArtifact.
        :type sql_scripting_parameters: list[:class:`huaweicloudsdkaidatalakejobserver.v2.SparkJobSqlScriptParameter`]
        """
        self._sql_scripting_parameters = sql_scripting_parameters

    @property
    def sql_scripting_result_to_obs(self):
        r"""Gets the sql_scripting_result_to_obs of this SparkJobArtifact.

        **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 

        :return: The sql_scripting_result_to_obs of this SparkJobArtifact.
        :rtype: bool
        """
        return self._sql_scripting_result_to_obs

    @sql_scripting_result_to_obs.setter
    def sql_scripting_result_to_obs(self, sql_scripting_result_to_obs):
        r"""Sets the sql_scripting_result_to_obs of this SparkJobArtifact.

        **参数解释**：结果写入OBS标识，用于控制SQL脚本作业的执行结果是否写入OBS。 **约束限制**：不涉及。 **取值范围**： - true：结果写入OBS。 - false：结果不写入OBS。 **默认取值**：不涉及。 

        :param sql_scripting_result_to_obs: The sql_scripting_result_to_obs of this SparkJobArtifact.
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
        if not isinstance(other, SparkJobArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
