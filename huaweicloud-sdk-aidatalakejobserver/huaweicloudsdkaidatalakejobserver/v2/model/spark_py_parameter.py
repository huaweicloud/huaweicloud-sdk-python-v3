# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkPyParameter:

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
        'main_python_file': 'str',
        'main_args': 'list[str]',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'dependency_archives': 'list[str]',
        'dependency_py_files': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'main_python_file': 'main_python_file',
        'main_args': 'main_args',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'dependency_archives': 'dependency_archives',
        'dependency_py_files': 'dependency_py_files'
    }

    def __init__(self, type=None, main_python_file=None, main_args=None, dependency_jars=None, dependency_files=None, dependency_archives=None, dependency_py_files=None):
        r"""SparkPyParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 spark_python_job。 **取值范围**：不涉及。 **默认取值**：spark_python_job。 
        :type type: str
        :param main_python_file: **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 
        :type main_python_file: str
        :param main_args: **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 
        :type main_args: list[str]
        :param dependency_jars: **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 
        :type dependency_jars: list[str]
        :param dependency_files: **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 
        :type dependency_files: list[str]
        :param dependency_archives: **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 
        :type dependency_archives: list[str]
        :param dependency_py_files: **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 
        :type dependency_py_files: list[str]
        """
        
        

        self._type = None
        self._main_python_file = None
        self._main_args = None
        self._dependency_jars = None
        self._dependency_files = None
        self._dependency_archives = None
        self._dependency_py_files = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.main_python_file = main_python_file
        if main_args is not None:
            self.main_args = main_args
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if dependency_archives is not None:
            self.dependency_archives = dependency_archives
        if dependency_py_files is not None:
            self.dependency_py_files = dependency_py_files

    @property
    def type(self):
        r"""Gets the type of this SparkPyParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 spark_python_job。 **取值范围**：不涉及。 **默认取值**：spark_python_job。 

        :return: The type of this SparkPyParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SparkPyParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 spark_python_job。 **取值范围**：不涉及。 **默认取值**：spark_python_job。 

        :param type: The type of this SparkPyParameter.
        :type type: str
        """
        self._type = type

    @property
    def main_python_file(self):
        r"""Gets the main_python_file of this SparkPyParameter.

        **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 

        :return: The main_python_file of this SparkPyParameter.
        :rtype: str
        """
        return self._main_python_file

    @main_python_file.setter
    def main_python_file(self, main_python_file):
        r"""Sets the main_python_file of this SparkPyParameter.

        **参数解释**：主Python文件路径，用于指定Python Spark作业的主文件OBS路径。 **约束限制**：不涉及。 **取值范围**：长度为1~512个字符，格式为OBS路径，例如：“obs://bucket/pyspark/pySpark_udf_python.py”。 **默认取值**：不涉及。 

        :param main_python_file: The main_python_file of this SparkPyParameter.
        :type main_python_file: str
        """
        self._main_python_file = main_python_file

    @property
    def main_args(self):
        r"""Gets the main_args of this SparkPyParameter.

        **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 

        :return: The main_args of this SparkPyParameter.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this SparkPyParameter.

        **参数解释**：主类参数列表，用于传递给Python Spark作业的参数。多个参数之间空格分隔。 **约束限制**：参数数量不能超过100个。 

        :param main_args: The main_args of this SparkPyParameter.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this SparkPyParameter.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :return: The dependency_jars of this SparkPyParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this SparkPyParameter.

        **参数解释**：依赖Jar包列表，用于指定Spark作业依赖的Jar包OBS路径。 **约束限制**：依赖Jar包数量不能超过100个。 

        :param dependency_jars: The dependency_jars of this SparkPyParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this SparkPyParameter.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 

        :return: The dependency_files of this SparkPyParameter.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this SparkPyParameter.

        **参数解释**：依赖文件列表，用于指定Spark作业依赖的文件OBS路径。 **约束限制**：依赖文件数量不能超过100个。 

        :param dependency_files: The dependency_files of this SparkPyParameter.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def dependency_archives(self):
        r"""Gets the dependency_archives of this SparkPyParameter.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 

        :return: The dependency_archives of this SparkPyParameter.
        :rtype: list[str]
        """
        return self._dependency_archives

    @dependency_archives.setter
    def dependency_archives(self, dependency_archives):
        r"""Sets the dependency_archives of this SparkPyParameter.

        **参数解释**：依赖归档包列表，用于指定Spark作业依赖的归档包OBS路径。 **约束限制**：依赖归档包数量不能超过100个。 

        :param dependency_archives: The dependency_archives of this SparkPyParameter.
        :type dependency_archives: list[str]
        """
        self._dependency_archives = dependency_archives

    @property
    def dependency_py_files(self):
        r"""Gets the dependency_py_files of this SparkPyParameter.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 

        :return: The dependency_py_files of this SparkPyParameter.
        :rtype: list[str]
        """
        return self._dependency_py_files

    @dependency_py_files.setter
    def dependency_py_files(self, dependency_py_files):
        r"""Sets the dependency_py_files of this SparkPyParameter.

        **参数解释**：依赖Python文件列表，用于指定Spark作业依赖的Python包OBS路径。 **约束限制**：依赖Python文件数量不能超过100个。 

        :param dependency_py_files: The dependency_py_files of this SparkPyParameter.
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
        if not isinstance(other, SparkPyParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
