# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJarParameterResponse:

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
        'main_jar': 'str',
        'main_class': 'str',
        'main_args': 'list[str]',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'python_parameter': 'ShowFlinkPythonDependencyParameterResponse'
    }

    attribute_map = {
        'type': 'type',
        'main_jar': 'main_jar',
        'main_class': 'main_class',
        'main_args': 'main_args',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'python_parameter': 'python_parameter'
    }

    def __init__(self, type=None, main_jar=None, main_class=None, main_args=None, dependency_jars=None, dependency_files=None, python_parameter=None):
        r"""ShowFlinkJarParameterResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型，用于区分SQL作业、Jar作业和SQL Gateway作业。 **约束限制**：不涉及。 **取值范围**：   - FLINK_JAR_JOB：Jar作业。 
        :type type: str
        :param main_jar: **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。
        :type main_jar: str
        :param main_class: **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。
        :type main_class: str
        :param main_args: **参数解释**：JAR作业入口类参数，用于传递运行参数。
        :type main_args: list[str]
        :param dependency_jars: **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。
        :type dependency_files: list[str]
        :param python_parameter: 
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        """
        
        

        self._type = None
        self._main_jar = None
        self._main_class = None
        self._main_args = None
        self._dependency_jars = None
        self._dependency_files = None
        self._python_parameter = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if main_jar is not None:
            self.main_jar = main_jar
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if python_parameter is not None:
            self.python_parameter = python_parameter

    @property
    def type(self):
        r"""Gets the type of this ShowFlinkJarParameterResponse.

        **参数解释**：作业类型，用于区分SQL作业、Jar作业和SQL Gateway作业。 **约束限制**：不涉及。 **取值范围**：   - FLINK_JAR_JOB：Jar作业。 

        :return: The type of this ShowFlinkJarParameterResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowFlinkJarParameterResponse.

        **参数解释**：作业类型，用于区分SQL作业、Jar作业和SQL Gateway作业。 **约束限制**：不涉及。 **取值范围**：   - FLINK_JAR_JOB：Jar作业。 

        :param type: The type of this ShowFlinkJarParameterResponse.
        :type type: str
        """
        self._type = type

    @property
    def main_jar(self):
        r"""Gets the main_jar of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :return: The main_jar of this ShowFlinkJarParameterResponse.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。

        :param main_jar: The main_jar of this ShowFlinkJarParameterResponse.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def main_class(self):
        r"""Gets the main_class of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。

        :return: The main_class of this ShowFlinkJarParameterResponse.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。

        :param main_class: The main_class of this ShowFlinkJarParameterResponse.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业入口类参数，用于传递运行参数。

        :return: The main_args of this ShowFlinkJarParameterResponse.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业入口类参数，用于传递运行参数。

        :param main_args: The main_args of this ShowFlinkJarParameterResponse.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。

        :return: The dependency_jars of this ShowFlinkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。

        :param dependency_jars: The dependency_jars of this ShowFlinkJarParameterResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。

        :return: The dependency_files of this ShowFlinkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this ShowFlinkJarParameterResponse.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。

        :param dependency_files: The dependency_files of this ShowFlinkJarParameterResponse.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def python_parameter(self):
        r"""Gets the python_parameter of this ShowFlinkJarParameterResponse.

        :return: The python_parameter of this ShowFlinkJarParameterResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        """
        return self._python_parameter

    @python_parameter.setter
    def python_parameter(self, python_parameter):
        r"""Sets the python_parameter of this ShowFlinkJarParameterResponse.

        :param python_parameter: The python_parameter of this ShowFlinkJarParameterResponse.
        :type python_parameter: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkPythonDependencyParameterResponse`
        """
        self._python_parameter = python_parameter

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
        if not isinstance(other, ShowFlinkJarParameterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
