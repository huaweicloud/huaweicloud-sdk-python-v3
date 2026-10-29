# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkPythonParameter:

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
        'python_job_file': 'str',
        'entry_module': 'str',
        'main_args': 'list[str]',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'python_archives': 'list[str]',
        'python_libraries': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'python_job_file': 'python_job_file',
        'entry_module': 'entry_module',
        'main_args': 'main_args',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'python_archives': 'python_archives',
        'python_libraries': 'python_libraries'
    }

    def __init__(self, type=None, python_job_file=None, entry_module=None, main_args=None, dependency_jars=None, dependency_files=None, python_archives=None, python_libraries=None):
        r"""FlinkPythonParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_PYTHON_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_PYTHON_JOB。
        :type type: str
        :param python_job_file: **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type python_job_file: str
        :param entry_module: **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。
        :type entry_module: str
        :param main_args: **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。
        :type main_args: list[str]
        :param dependency_jars: **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。
        :type dependency_files: list[str]
        :param python_archives: **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。
        :type python_archives: list[str]
        :param python_libraries: **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。
        :type python_libraries: list[str]
        """
        
        

        self._type = None
        self._python_job_file = None
        self._entry_module = None
        self._main_args = None
        self._dependency_jars = None
        self._dependency_files = None
        self._python_archives = None
        self._python_libraries = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.python_job_file = python_job_file
        if entry_module is not None:
            self.entry_module = entry_module
        if main_args is not None:
            self.main_args = main_args
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if python_archives is not None:
            self.python_archives = python_archives
        if python_libraries is not None:
            self.python_libraries = python_libraries

    @property
    def type(self):
        r"""Gets the type of this FlinkPythonParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_PYTHON_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_PYTHON_JOB。

        :return: The type of this FlinkPythonParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlinkPythonParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_PYTHON_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_PYTHON_JOB。

        :param type: The type of this FlinkPythonParameter.
        :type type: str
        """
        self._type = type

    @property
    def python_job_file(self):
        r"""Gets the python_job_file of this FlinkPythonParameter.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The python_job_file of this FlinkPythonParameter.
        :rtype: str
        """
        return self._python_job_file

    @python_job_file.setter
    def python_job_file(self, python_job_file):
        r"""Sets the python_job_file of this FlinkPythonParameter.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **约束限制**：以 .py 结尾时不允许配置 entry_module；非 .py 时必须配置 entry_module。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param python_job_file: The python_job_file of this FlinkPythonParameter.
        :type python_job_file: str
        """
        self._python_job_file = python_job_file

    @property
    def entry_module(self):
        r"""Gets the entry_module of this FlinkPythonParameter.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :return: The entry_module of this FlinkPythonParameter.
        :rtype: str
        """
        return self._entry_module

    @entry_module.setter
    def entry_module(self, entry_module):
        r"""Sets the entry_module of this FlinkPythonParameter.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **约束限制**：python_job_file 以 .py 结尾时必须为空；非 .py 时必填。 **取值范围**：长度为1~512个字符。 **默认取值**：不涉及。

        :param entry_module: The entry_module of this FlinkPythonParameter.
        :type entry_module: str
        """
        self._entry_module = entry_module

    @property
    def main_args(self):
        r"""Gets the main_args of this FlinkPythonParameter.

        **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。

        :return: The main_args of this FlinkPythonParameter.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this FlinkPythonParameter.

        **参数解释**：Python作业入口参数，多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。

        :param main_args: The main_args of this FlinkPythonParameter.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this FlinkPythonParameter.

        **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :return: The dependency_jars of this FlinkPythonParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this FlinkPythonParameter.

        **参数解释**：Python作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :param dependency_jars: The dependency_jars of this FlinkPythonParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this FlinkPythonParameter.

        **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :return: The dependency_files of this FlinkPythonParameter.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this FlinkPythonParameter.

        **参数解释**：Python作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :param dependency_files: The dependency_files of this FlinkPythonParameter.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def python_archives(self):
        r"""Gets the python_archives of this FlinkPythonParameter.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。

        :return: The python_archives of this FlinkPythonParameter.
        :rtype: list[str]
        """
        return self._python_archives

    @python_archives.setter
    def python_archives(self, python_archives):
        r"""Sets the python_archives of this FlinkPythonParameter.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。

        :param python_archives: The python_archives of this FlinkPythonParameter.
        :type python_archives: list[str]
        """
        self._python_archives = python_archives

    @property
    def python_libraries(self):
        r"""Gets the python_libraries of this FlinkPythonParameter.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。

        :return: The python_libraries of this FlinkPythonParameter.
        :rtype: list[str]
        """
        return self._python_libraries

    @python_libraries.setter
    def python_libraries(self, python_libraries):
        r"""Sets the python_libraries of this FlinkPythonParameter.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。

        :param python_libraries: The python_libraries of this FlinkPythonParameter.
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
        if not isinstance(other, FlinkPythonParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
