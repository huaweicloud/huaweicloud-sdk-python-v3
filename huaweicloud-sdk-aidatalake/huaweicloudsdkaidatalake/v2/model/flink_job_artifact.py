# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobArtifact:

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
        'python_parameter': 'FlinkPythonDependencyParameter',
        'main_jar': 'str',
        'main_class': 'str',
        'main_args': 'list[str]',
        'sql_gateway_token': 'str',
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
        'sql_gateway_token': 'sql_gateway_token',
        'idle_enabled': 'idle_enabled',
        'idle_timeout': 'idle_timeout',
        'python_job_file': 'python_job_file',
        'entry_module': 'entry_module',
        'python_archives': 'python_archives',
        'python_libraries': 'python_libraries'
    }

    def __init__(self, type=None, sql_script_file=None, dependency_jars=None, dependency_files=None, python_parameter=None, main_jar=None, main_class=None, main_args=None, sql_gateway_token=None, idle_enabled=None, idle_timeout=None, python_job_file=None, entry_module=None, python_archives=None, python_libraries=None):
        r"""FlinkJobArtifact

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param sql_script_file: **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type sql_script_file: str
        :param dependency_jars: **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。
        :type dependency_files: list[str]
        :param python_parameter: 
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.FlinkPythonDependencyParameter`
        :param main_jar: **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type main_jar: str
        :param main_class: **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。
        :type main_class: str
        :param main_args: **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。
        :type main_args: list[str]
        :param sql_gateway_token: **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。
        :type sql_gateway_token: str
        :param idle_enabled: **参数解释**：是否开启空闲自动释放。 **约束限制**：不涉及。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。 **默认取值**：false。
        :type idle_enabled: bool
        :param idle_timeout: **参数解释**：最大空闲时长，单位为分钟，用于指定SQL Gateway空闲多长时间后自动停止。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **约束限制**：不涉及。 **取值范围**：10~1440。 **默认取值**：30。
        :type idle_timeout: int
        :param python_job_file: **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type python_job_file: str
        :param entry_module: **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。
        :type entry_module: str
        :param python_archives: **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。
        :type python_archives: list[str]
        :param python_libraries: **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。
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
        self._sql_gateway_token = None
        self._idle_enabled = None
        self._idle_timeout = None
        self._python_job_file = None
        self._entry_module = None
        self._python_archives = None
        self._python_libraries = None
        self.discriminator = None

        self.type = type
        self.sql_script_file = sql_script_file
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if python_parameter is not None:
            self.python_parameter = python_parameter
        self.main_jar = main_jar
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if sql_gateway_token is not None:
            self.sql_gateway_token = sql_gateway_token
        if idle_enabled is not None:
            self.idle_enabled = idle_enabled
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        self.python_job_file = python_job_file
        if entry_module is not None:
            self.entry_module = entry_module
        if python_archives is not None:
            self.python_archives = python_archives
        if python_libraries is not None:
            self.python_libraries = python_libraries

    @property
    def type(self):
        r"""Gets the type of this FlinkJobArtifact.

        :return: The type of this FlinkJobArtifact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlinkJobArtifact.

        :param type: The type of this FlinkJobArtifact.
        :type type: str
        """
        self._type = type

    @property
    def sql_script_file(self):
        r"""Gets the sql_script_file of this FlinkJobArtifact.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The sql_script_file of this FlinkJobArtifact.
        :rtype: str
        """
        return self._sql_script_file

    @sql_script_file.setter
    def sql_script_file(self, sql_script_file):
        r"""Sets the sql_script_file of this FlinkJobArtifact.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param sql_script_file: The sql_script_file of this FlinkJobArtifact.
        :type sql_script_file: str
        """
        self._sql_script_file = sql_script_file

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this FlinkJobArtifact.

        **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :return: The dependency_jars of this FlinkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this FlinkJobArtifact.

        **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :param dependency_jars: The dependency_jars of this FlinkJobArtifact.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this FlinkJobArtifact.

        **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :return: The dependency_files of this FlinkJobArtifact.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this FlinkJobArtifact.

        **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :param dependency_files: The dependency_files of this FlinkJobArtifact.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def python_parameter(self):
        r"""Gets the python_parameter of this FlinkJobArtifact.

        :return: The python_parameter of this FlinkJobArtifact.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkPythonDependencyParameter`
        """
        return self._python_parameter

    @python_parameter.setter
    def python_parameter(self, python_parameter):
        r"""Sets the python_parameter of this FlinkJobArtifact.

        :param python_parameter: The python_parameter of this FlinkJobArtifact.
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.FlinkPythonDependencyParameter`
        """
        self._python_parameter = python_parameter

    @property
    def main_jar(self):
        r"""Gets the main_jar of this FlinkJobArtifact.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The main_jar of this FlinkJobArtifact.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this FlinkJobArtifact.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param main_jar: The main_jar of this FlinkJobArtifact.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def main_class(self):
        r"""Gets the main_class of this FlinkJobArtifact.

        **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。

        :return: The main_class of this FlinkJobArtifact.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this FlinkJobArtifact.

        **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。

        :param main_class: The main_class of this FlinkJobArtifact.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this FlinkJobArtifact.

        **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。

        :return: The main_args of this FlinkJobArtifact.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this FlinkJobArtifact.

        **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。

        :param main_args: The main_args of this FlinkJobArtifact.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def sql_gateway_token(self):
        r"""Gets the sql_gateway_token of this FlinkJobArtifact.

        **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :return: The sql_gateway_token of this FlinkJobArtifact.
        :rtype: str
        """
        return self._sql_gateway_token

    @sql_gateway_token.setter
    def sql_gateway_token(self, sql_gateway_token):
        r"""Sets the sql_gateway_token of this FlinkJobArtifact.

        **参数解释**：用户自定义的SQL Gateway访问鉴权Token，调用方通过HTTP请求头 Authorization: Bearer {token} 携带。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :param sql_gateway_token: The sql_gateway_token of this FlinkJobArtifact.
        :type sql_gateway_token: str
        """
        self._sql_gateway_token = sql_gateway_token

    @property
    def idle_enabled(self):
        r"""Gets the idle_enabled of this FlinkJobArtifact.

        **参数解释**：是否开启空闲自动释放。 **约束限制**：不涉及。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。 **默认取值**：false。

        :return: The idle_enabled of this FlinkJobArtifact.
        :rtype: bool
        """
        return self._idle_enabled

    @idle_enabled.setter
    def idle_enabled(self, idle_enabled):
        r"""Sets the idle_enabled of this FlinkJobArtifact.

        **参数解释**：是否开启空闲自动释放。 **约束限制**：不涉及。 **取值范围**：   - true：开启空闲自动释放。   - false：关闭空闲自动释放。 **默认取值**：false。

        :param idle_enabled: The idle_enabled of this FlinkJobArtifact.
        :type idle_enabled: bool
        """
        self._idle_enabled = idle_enabled

    @property
    def idle_timeout(self):
        r"""Gets the idle_timeout of this FlinkJobArtifact.

        **参数解释**：最大空闲时长，单位为分钟，用于指定SQL Gateway空闲多长时间后自动停止。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **约束限制**：不涉及。 **取值范围**：10~1440。 **默认取值**：30。

        :return: The idle_timeout of this FlinkJobArtifact.
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        r"""Sets the idle_timeout of this FlinkJobArtifact.

        **参数解释**：最大空闲时长，单位为分钟，用于指定SQL Gateway空闲多长时间后自动停止。空闲指会话内没有正在运行的作业，创建会话等其他操作不计为非空闲。 **约束限制**：不涉及。 **取值范围**：10~1440。 **默认取值**：30。

        :param idle_timeout: The idle_timeout of this FlinkJobArtifact.
        :type idle_timeout: int
        """
        self._idle_timeout = idle_timeout

    @property
    def python_job_file(self):
        r"""Gets the python_job_file of this FlinkJobArtifact.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The python_job_file of this FlinkJobArtifact.
        :rtype: str
        """
        return self._python_job_file

    @python_job_file.setter
    def python_job_file(self, python_job_file):
        r"""Sets the python_job_file of this FlinkJobArtifact.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param python_job_file: The python_job_file of this FlinkJobArtifact.
        :type python_job_file: str
        """
        self._python_job_file = python_job_file

    @property
    def entry_module(self):
        r"""Gets the entry_module of this FlinkJobArtifact.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :return: The entry_module of this FlinkJobArtifact.
        :rtype: str
        """
        return self._entry_module

    @entry_module.setter
    def entry_module(self, entry_module):
        r"""Sets the entry_module of this FlinkJobArtifact.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :param entry_module: The entry_module of this FlinkJobArtifact.
        :type entry_module: str
        """
        self._entry_module = entry_module

    @property
    def python_archives(self):
        r"""Gets the python_archives of this FlinkJobArtifact.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。

        :return: The python_archives of this FlinkJobArtifact.
        :rtype: list[str]
        """
        return self._python_archives

    @python_archives.setter
    def python_archives(self, python_archives):
        r"""Sets the python_archives of this FlinkJobArtifact.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。

        :param python_archives: The python_archives of this FlinkJobArtifact.
        :type python_archives: list[str]
        """
        self._python_archives = python_archives

    @property
    def python_libraries(self):
        r"""Gets the python_libraries of this FlinkJobArtifact.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。

        :return: The python_libraries of this FlinkJobArtifact.
        :rtype: list[str]
        """
        return self._python_libraries

    @python_libraries.setter
    def python_libraries(self, python_libraries):
        r"""Sets the python_libraries of this FlinkJobArtifact.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。

        :param python_libraries: The python_libraries of this FlinkJobArtifact.
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
        if not isinstance(other, FlinkJobArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
