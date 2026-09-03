# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJarParameterResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_class': 'str',
        'main_args': 'list[str]',
        'main_jar': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'dependency_archives': 'list[str]',
        'dependency_py_files': 'list[str]'
    }

    attribute_map = {
        'main_class': 'main_class',
        'main_args': 'main_args',
        'main_jar': 'main_jar',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'dependency_archives': 'dependency_archives',
        'dependency_py_files': 'dependency_py_files'
    }

    def __init__(self, main_class=None, main_args=None, main_jar=None, dependency_jars=None, dependency_files=None, dependency_archives=None, dependency_py_files=None):
        r"""ShowSparkJarParameterResponse

        The model defined in huaweicloud sdk

        :param main_class: **参数解释**：Spark Jar作业入口类，用于指定作业的主类名称。 **取值范围**：完整的Java类路径格式，例如：com.example.SparkJob。 
        :type main_class: str
        :param main_args: **参数解释**：Spark Jar作业入口类参数列表，用于传递作业执行参数。 
        :type main_args: list[str]
        :param main_jar: **参数解释**：Spark Jar作业主类所在Jar包的OBS路径，用于指定作业的主Jar包。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/jars/spark-job.jar。 
        :type main_jar: str
        :param dependency_jars: **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 
        :type dependency_files: list[str]
        :param dependency_archives: **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 
        :type dependency_archives: list[str]
        :param dependency_py_files: **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 
        :type dependency_py_files: list[str]
        """
        
        

        self._main_class = None
        self._main_args = None
        self._main_jar = None
        self._dependency_jars = None
        self._dependency_files = None
        self._dependency_archives = None
        self._dependency_py_files = None
        self.discriminator = None

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

    @property
    def main_class(self):
        r"""Gets the main_class of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业入口类，用于指定作业的主类名称。 **取值范围**：完整的Java类路径格式，例如：com.example.SparkJob。 

        :return: The main_class of this ShowSparkJarParameterResponse.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业入口类，用于指定作业的主类名称。 **取值范围**：完整的Java类路径格式，例如：com.example.SparkJob。 

        :param main_class: The main_class of this ShowSparkJarParameterResponse.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        r"""Gets the main_args of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业入口类参数列表，用于传递作业执行参数。 

        :return: The main_args of this ShowSparkJarParameterResponse.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业入口类参数列表，用于传递作业执行参数。 

        :param main_args: The main_args of this ShowSparkJarParameterResponse.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def main_jar(self):
        r"""Gets the main_jar of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业主类所在Jar包的OBS路径，用于指定作业的主Jar包。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/jars/spark-job.jar。 

        :return: The main_jar of this ShowSparkJarParameterResponse.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        r"""Sets the main_jar of this ShowSparkJarParameterResponse.

        **参数解释**：Spark Jar作业主类所在Jar包的OBS路径，用于指定作业的主Jar包。 **取值范围**：OBS URL格式，长度为1~1024个字符，例如：obs://bucket/jars/spark-job.jar。 

        :param main_jar: The main_jar of this ShowSparkJarParameterResponse.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this ShowSparkJarParameterResponse.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 

        :return: The dependency_jars of this ShowSparkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowSparkJarParameterResponse.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 

        :param dependency_jars: The dependency_jars of this ShowSparkJarParameterResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this ShowSparkJarParameterResponse.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 

        :return: The dependency_files of this ShowSparkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this ShowSparkJarParameterResponse.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 

        :param dependency_files: The dependency_files of this ShowSparkJarParameterResponse.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def dependency_archives(self):
        r"""Gets the dependency_archives of this ShowSparkJarParameterResponse.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 

        :return: The dependency_archives of this ShowSparkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_archives

    @dependency_archives.setter
    def dependency_archives(self, dependency_archives):
        r"""Sets the dependency_archives of this ShowSparkJarParameterResponse.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 

        :param dependency_archives: The dependency_archives of this ShowSparkJarParameterResponse.
        :type dependency_archives: list[str]
        """
        self._dependency_archives = dependency_archives

    @property
    def dependency_py_files(self):
        r"""Gets the dependency_py_files of this ShowSparkJarParameterResponse.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 

        :return: The dependency_py_files of this ShowSparkJarParameterResponse.
        :rtype: list[str]
        """
        return self._dependency_py_files

    @dependency_py_files.setter
    def dependency_py_files(self, dependency_py_files):
        r"""Sets the dependency_py_files of this ShowSparkJarParameterResponse.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 

        :param dependency_py_files: The dependency_py_files of this ShowSparkJarParameterResponse.
        :type dependency_py_files: list[str]
        """
        self._dependency_py_files = dependency_py_files

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
        if not isinstance(other, ShowSparkJarParameterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
