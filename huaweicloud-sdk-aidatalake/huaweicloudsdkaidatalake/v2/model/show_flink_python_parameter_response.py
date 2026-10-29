# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkPythonParameterResponse:

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
        r"""ShowFlinkPythonParameterResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_PYTHON_JOB：Flink Python作业。 
        :type type: str
        :param python_job_file: **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。
        :type python_job_file: str
        :param entry_module: **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。
        :type entry_module: str
        :param main_args: **参数解释**：Python作业入口参数，用于传递运行参数。
        :type main_args: list[str]
        :param dependency_jars: **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：Python作业附加依赖文件的OBS路径列表。
        :type dependency_files: list[str]
        :param python_archives: **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。
        :type python_archives: list[str]
        :param python_libraries: **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。
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
        if python_job_file is not None:
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
        r"""Gets the type of this ShowFlinkPythonParameterResponse.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_PYTHON_JOB：Flink Python作业。 

        :return: The type of this ShowFlinkPythonParameterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowFlinkPythonParameterResponse.

        **参数解释**：作业类型。 **约束限制**：不涉及。 **取值范围**：   - FLINK_PYTHON_JOB：Flink Python作业。 

        :param type: The type of this ShowFlinkPythonParameterResponse.
        :type type: str
        """
        self._type = type

    @property
    def python_job_file(self):
        r"""Gets the python_job_file of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :return: The python_job_file of this ShowFlinkPythonParameterResponse.
        :rtype: str
        """
        return self._python_job_file

    @python_job_file.setter
    def python_job_file(self, python_job_file):
        r"""Sets the python_job_file of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业文件的OBS路径，用于指定Python作业的入口脚本或作业包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :param python_job_file: The python_job_file of this ShowFlinkPythonParameterResponse.
        :type python_job_file: str
        """
        self._python_job_file = python_job_file

    @property
    def entry_module(self):
        r"""Gets the entry_module of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。

        :return: The entry_module of this ShowFlinkPythonParameterResponse.
        :rtype: str
        """
        return self._entry_module

    @entry_module.setter
    def entry_module(self, entry_module):
        r"""Sets the entry_module of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python程序入口模块名，用于指定作业包内的入口模块。 **取值范围**：长度为1~512个字符。

        :param entry_module: The entry_module of this ShowFlinkPythonParameterResponse.
        :type entry_module: str
        """
        self._entry_module = entry_module

    @property
    def main_args(self):
        r"""Gets the main_args of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业入口参数，用于传递运行参数。

        :return: The main_args of this ShowFlinkPythonParameterResponse.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业入口参数，用于传递运行参数。

        :param main_args: The main_args of this ShowFlinkPythonParameterResponse.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。

        :return: The dependency_jars of this ShowFlinkPythonParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业依赖的第三方Java JAR包OBS路径列表。

        :param dependency_jars: The dependency_jars of this ShowFlinkPythonParameterResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业附加依赖文件的OBS路径列表。

        :return: The dependency_files of this ShowFlinkPythonParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python作业附加依赖文件的OBS路径列表。

        :param dependency_files: The dependency_files of this ShowFlinkPythonParameterResponse.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def python_archives(self):
        r"""Gets the python_archives of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。

        :return: The python_archives of this ShowFlinkPythonParameterResponse.
        :rtype: list[str]
        """
        return self._python_archives

    @python_archives.setter
    def python_archives(self, python_archives):
        r"""Sets the python_archives of this ShowFlinkPythonParameterResponse.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。

        :param python_archives: The python_archives of this ShowFlinkPythonParameterResponse.
        :type python_archives: list[str]
        """
        self._python_archives = python_archives

    @property
    def python_libraries(self):
        r"""Gets the python_libraries of this ShowFlinkPythonParameterResponse.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。

        :return: The python_libraries of this ShowFlinkPythonParameterResponse.
        :rtype: list[str]
        """
        return self._python_libraries

    @python_libraries.setter
    def python_libraries(self, python_libraries):
        r"""Sets the python_libraries of this ShowFlinkPythonParameterResponse.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。

        :param python_libraries: The python_libraries of this ShowFlinkPythonParameterResponse.
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
        if not isinstance(other, ShowFlinkPythonParameterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
