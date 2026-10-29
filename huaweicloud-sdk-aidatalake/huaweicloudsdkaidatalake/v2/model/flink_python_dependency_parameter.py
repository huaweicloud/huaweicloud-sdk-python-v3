# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkPythonDependencyParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'python_archives': 'list[str]',
        'python_libraries': 'list[str]'
    }

    attribute_map = {
        'python_archives': 'python_archives',
        'python_libraries': 'python_libraries'
    }

    def __init__(self, python_archives=None, python_libraries=None):
        r"""FlinkPythonDependencyParameter

        The model defined in huaweicloud sdk

        :param python_archives: **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。
        :type python_archives: list[str]
        :param python_libraries: **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。
        :type python_libraries: list[str]
        """
        
        

        self._python_archives = None
        self._python_libraries = None
        self.discriminator = None

        if python_archives is not None:
            self.python_archives = python_archives
        if python_libraries is not None:
            self.python_libraries = python_libraries

    @property
    def python_archives(self):
        r"""Gets the python_archives of this FlinkPythonDependencyParameter.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。

        :return: The python_archives of this FlinkPythonDependencyParameter.
        :rtype: list[str]
        """
        return self._python_archives

    @python_archives.setter
    def python_archives(self, python_archives):
        r"""Sets the python_archives of this FlinkPythonDependencyParameter.

        **参数解释**：Python归档文件的OBS路径列表，用于指定Python运行环境或数据文件的压缩包。 **约束限制**：归档文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。

        :param python_archives: The python_archives of this FlinkPythonDependencyParameter.
        :type python_archives: list[str]
        """
        self._python_archives = python_archives

    @property
    def python_libraries(self):
        r"""Gets the python_libraries of this FlinkPythonDependencyParameter.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。

        :return: The python_libraries of this FlinkPythonDependencyParameter.
        :rtype: list[str]
        """
        return self._python_libraries

    @python_libraries.setter
    def python_libraries(self, python_libraries):
        r"""Sets the python_libraries of this FlinkPythonDependencyParameter.

        **参数解释**：第三方Python依赖的OBS路径列表，用于指定Python UDF所需的依赖。 **约束限制**：依赖文件数量不能超过100个。单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。

        :param python_libraries: The python_libraries of this FlinkPythonDependencyParameter.
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
        if not isinstance(other, FlinkPythonDependencyParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
