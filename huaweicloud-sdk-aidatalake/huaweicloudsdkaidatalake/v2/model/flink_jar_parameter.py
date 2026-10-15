# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJarParameter:

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
        'dependency_files': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'main_jar': 'main_jar',
        'main_class': 'main_class',
        'main_args': 'main_args',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files'
    }

    def __init__(self, type=None, main_jar=None, main_class=None, main_args=None, dependency_jars=None, dependency_files=None):
        r"""FlinkJarParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_JAR_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_JAR_JOB。
        :type type: str
        :param main_jar: **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type main_jar: str
        :param main_class: **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。
        :type main_class: str
        :param main_args: **参数解释**：JAR作业入口类参数列表，按数组顺序传入。 **约束限制**：参数数量不能超过100个。
        :type main_args: list[str]
        :param dependency_jars: **参数解释**：JAR作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。
        :type dependency_files: list[str]
        """
        
        

        self._type = None
        self._main_jar = None
        self._main_class = None
        self._main_args = None
        self._dependency_jars = None
        self._dependency_files = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.main_jar = main_jar
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files

    @property
    def type(self):
        r"""Gets the type of this FlinkJarParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_JAR_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_JAR_JOB。

        :return: The type of this FlinkJarParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlinkJarParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_JAR_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_JAR_JOB。

        :param type: The type of this FlinkJarParameter.
        :type type: str
        """
        self._type = type

    @property
    def main_jar(self):
        r"""Gets the main_jar of this FlinkJarParameter.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The main_jar of this FlinkJarParameter.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this FlinkJarParameter.

        **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param main_jar: The main_jar of this FlinkJarParameter.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def main_class(self):
        r"""Gets the main_class of this FlinkJarParameter.

        **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。

        :return: The main_class of this FlinkJarParameter.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this FlinkJarParameter.

        **参数解释**：JAR作业入口类全限定名，用于指定作业的入口类。当主程序包manifest中已指定主类时可省略。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，字符组成不限制。 **默认取值**：不涉及。

        :param main_class: The main_class of this FlinkJarParameter.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this FlinkJarParameter.

        **参数解释**：JAR作业入口类参数列表，按数组顺序传入。 **约束限制**：参数数量不能超过100个。

        :return: The main_args of this FlinkJarParameter.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this FlinkJarParameter.

        **参数解释**：JAR作业入口类参数列表，按数组顺序传入。 **约束限制**：参数数量不能超过100个。

        :param main_args: The main_args of this FlinkJarParameter.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this FlinkJarParameter.

        **参数解释**：JAR作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :return: The dependency_jars of this FlinkJarParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this FlinkJarParameter.

        **参数解释**：JAR作业依赖JAR包的OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :param dependency_jars: The dependency_jars of this FlinkJarParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this FlinkJarParameter.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :return: The dependency_files of this FlinkJarParameter.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this FlinkJarParameter.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖文件数量不能超过100个。

        :param dependency_files: The dependency_files of this FlinkJarParameter.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

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
        if not isinstance(other, FlinkJarParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
