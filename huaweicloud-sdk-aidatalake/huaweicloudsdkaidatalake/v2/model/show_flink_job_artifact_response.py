# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJobArtifactResponse:

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
        'sql_script_file': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'python_parameter': 'ShowFlinkPythonDependencyParameterResponse',
        'main_jar': 'str',
        'main_class': 'str',
        'main_args': 'list[str]',
        'sql_gateway_config': 'ShowFlinkSqlGatewayConfigResponseBody',
        'idle_enabled': 'bool',
        'idle_timeout': 'int',
        'python_job_file': 'str',
        'entry_module': 'str',
        'python_archives': 'list[str]',
        'python_libraries': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'sql_script_file': 'sql_script_file',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'python_parameter': 'python_parameter',
        'main_jar': 'main_jar',
        'main_class': 'main_class',
        'main_args': 'main_args',
        'sql_gateway_config': 'sql_gateway_config',
        'idle_enabled': 'idle_enabled',
        'idle_timeout': 'idle_timeout',
        'python_job_file': 'python_job_file',
        'entry_module': 'entry_module',
        'python_archives': 'python_archives',
        'python_libraries': 'python_libraries'
    }

    def __init__(self, type=None, sql_script_file=None, dependency_jars=None, dependency_files=None, python_parameter=None, main_jar=None, main_class=None, main_args=None, sql_gateway_config=None, idle_enabled=None, idle_timeout=None, python_job_file=None, entry_module=None, python_archives=None, python_libraries=None):
        r"""ShowFlinkJobArtifactResponse

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param sql_script_file: **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。
        :type sql_script_file: str
        :param dependency_jars: **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：Python作业附加依赖文件的OBS路径列表。
        :type dependency_files: list[str]
        :param python_parameter: 
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        :param main_jar: **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。
        :type main_jar: str
        :param main_class: **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。
        :type main_class: str
        :param main_args: **参数解释**：Python作业入口参数，用于传递运行参数。
        :type main_args: list[str]
        :param sql_gateway_config: 
        :type sql_gateway_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        :param idle_enabled: **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。
        :type idle_enabled: bool
        :param idle_timeout: **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。
        :type idle_timeout: int
        :param python_job_file: **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。
        :type python_job_file: str
        :param entry_module: **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。
        :type entry_module: str
        :param python_archives: **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。
        :type python_archives: list[str]
        :param python_libraries: **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。
        :type python_libraries: list[str]
        """
        
        

        self._type = None
        self._sql_script_file = None
        self._dependency_jars = None
        self._dependency_files = None
        self._python_parameter = None
        self._main_jar = None
        self._main_class = None
        self._main_args = None
        self._sql_gateway_config = None
        self._idle_enabled = None
        self._idle_timeout = None
        self._python_job_file = None
        self._entry_module = None
        self._python_archives = None
        self._python_libraries = None
        self.discriminator = None

        self.type = type
        if sql_script_file is not None:
            self.sql_script_file = sql_script_file
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if python_parameter is not None:
            self.python_parameter = python_parameter
        if main_jar is not None:
            self.main_jar = main_jar
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if sql_gateway_config is not None:
            self.sql_gateway_config = sql_gateway_config
        if idle_enabled is not None:
            self.idle_enabled = idle_enabled
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if python_job_file is not None:
            self.python_job_file = python_job_file
        if entry_module is not None:
            self.entry_module = entry_module
        if python_archives is not None:
            self.python_archives = python_archives
        if python_libraries is not None:
            self.python_libraries = python_libraries

    @property
    def type(self):
        r"""Gets the type of this ShowFlinkJobArtifactResponse.

        :return: The type of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowFlinkJobArtifactResponse.

        :param type: The type of this ShowFlinkJobArtifactResponse.
        :type type: str
        """
        self._type = type

    @property
    def sql_script_file(self):
        r"""Gets the sql_script_file of this ShowFlinkJobArtifactResponse.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。

        :return: The sql_script_file of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._sql_script_file

    @sql_script_file.setter
    def sql_script_file(self, sql_script_file):
        r"""Sets the sql_script_file of this ShowFlinkJobArtifactResponse.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。

        :param sql_script_file: The sql_script_file of this ShowFlinkJobArtifactResponse.
        :type sql_script_file: str
        """
        self._sql_script_file = sql_script_file

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。

        :return: The dependency_jars of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。

        :param dependency_jars: The dependency_jars of this ShowFlinkJobArtifactResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业附加依赖文件的OBS路径列表。

        :return: The dependency_files of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业附加依赖文件的OBS路径列表。

        :param dependency_files: The dependency_files of this ShowFlinkJobArtifactResponse.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def python_parameter(self):
        r"""Gets the python_parameter of this ShowFlinkJobArtifactResponse.

        :return: The python_parameter of this ShowFlinkJobArtifactResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        """
        return self._python_parameter

    @python_parameter.setter
    def python_parameter(self, python_parameter):
        r"""Sets the python_parameter of this ShowFlinkJobArtifactResponse.

        :param python_parameter: The python_parameter of this ShowFlinkJobArtifactResponse.
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        """
        self._python_parameter = python_parameter

    @property
    def main_jar(self):
        r"""Gets the main_jar of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :return: The main_jar of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :param main_jar: The main_jar of this ShowFlinkJobArtifactResponse.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def main_class(self):
        r"""Gets the main_class of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。

        :return: The main_class of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。

        :param main_class: The main_class of this ShowFlinkJobArtifactResponse.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业入口参数，用于传递运行参数。

        :return: The main_args of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业入口参数，用于传递运行参数。

        :param main_args: The main_args of this ShowFlinkJobArtifactResponse.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def sql_gateway_config(self):
        r"""Gets the sql_gateway_config of this ShowFlinkJobArtifactResponse.

        :return: The sql_gateway_config of this ShowFlinkJobArtifactResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        """
        return self._sql_gateway_config

    @sql_gateway_config.setter
    def sql_gateway_config(self, sql_gateway_config):
        r"""Sets the sql_gateway_config of this ShowFlinkJobArtifactResponse.

        :param sql_gateway_config: The sql_gateway_config of this ShowFlinkJobArtifactResponse.
        :type sql_gateway_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        """
        self._sql_gateway_config = sql_gateway_config

    @property
    def idle_enabled(self):
        r"""Gets the idle_enabled of this ShowFlinkJobArtifactResponse.

        **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。

        :return: The idle_enabled of this ShowFlinkJobArtifactResponse.
        :rtype: bool
        """
        return self._idle_enabled

    @idle_enabled.setter
    def idle_enabled(self, idle_enabled):
        r"""Sets the idle_enabled of this ShowFlinkJobArtifactResponse.

        **参数解释**：是否开启空闲自动释放。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。

        :param idle_enabled: The idle_enabled of this ShowFlinkJobArtifactResponse.
        :type idle_enabled: bool
        """
        self._idle_enabled = idle_enabled

    @property
    def idle_timeout(self):
        r"""Gets the idle_timeout of this ShowFlinkJobArtifactResponse.

        **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。

        :return: The idle_timeout of this ShowFlinkJobArtifactResponse.
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        r"""Sets the idle_timeout of this ShowFlinkJobArtifactResponse.

        **参数解释**：最大空闲时长，单位为分钟。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **取值范围**：10~1440。

        :param idle_timeout: The idle_timeout of this ShowFlinkJobArtifactResponse.
        :type idle_timeout: int
        """
        self._idle_timeout = idle_timeout

    @property
    def python_job_file(self):
        r"""Gets the python_job_file of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :return: The python_job_file of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._python_job_file

    @python_job_file.setter
    def python_job_file(self, python_job_file):
        r"""Sets the python_job_file of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :param python_job_file: The python_job_file of this ShowFlinkJobArtifactResponse.
        :type python_job_file: str
        """
        self._python_job_file = python_job_file

    @property
    def entry_module(self):
        r"""Gets the entry_module of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。

        :return: The entry_module of this ShowFlinkJobArtifactResponse.
        :rtype: str
        """
        return self._entry_module

    @entry_module.setter
    def entry_module(self, entry_module):
        r"""Sets the entry_module of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。

        :param entry_module: The entry_module of this ShowFlinkJobArtifactResponse.
        :type entry_module: str
        """
        self._entry_module = entry_module

    @property
    def python_archives(self):
        r"""Gets the python_archives of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。

        :return: The python_archives of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._python_archives

    @python_archives.setter
    def python_archives(self, python_archives):
        r"""Sets the python_archives of this ShowFlinkJobArtifactResponse.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。

        :param python_archives: The python_archives of this ShowFlinkJobArtifactResponse.
        :type python_archives: list[str]
        """
        self._python_archives = python_archives

    @property
    def python_libraries(self):
        r"""Gets the python_libraries of this ShowFlinkJobArtifactResponse.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。

        :return: The python_libraries of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._python_libraries

    @python_libraries.setter
    def python_libraries(self, python_libraries):
        r"""Sets the python_libraries of this ShowFlinkJobArtifactResponse.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。

        :param python_libraries: The python_libraries of this ShowFlinkJobArtifactResponse.
        :type python_libraries: list[str]
        """
        self._python_libraries = python_libraries

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
        if not isinstance(other, ShowFlinkJobArtifactResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
