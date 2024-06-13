# coding: utf-8

import six

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
        'main_class': 'str',
        'main_args': 'str',
        'main_jar': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]'
    }

    attribute_map = {
        'main_class': 'main_class',
        'main_args': 'main_args',
        'main_jar': 'main_jar',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files'
    }

    def __init__(self, main_class=None, main_args=None, main_jar=None, dependency_jars=None, dependency_files=None):
        """FlinkJarParameter

        The model defined in huaweicloud sdk

        :param main_class: Flink Jar 作业入口类。
        :type main_class: str
        :param main_args: Flink Jar 作业入口类参数，多个参数之间空格分隔。
        :type main_args: str
        :param main_jar: Flink Jar 作业主类所在 Jar 包的 OBS 路径。
        :type main_jar: str
        :param dependency_jars: Flink Jar 作业依赖 Jar 包的 OBS 路径数组。示例：[obs://bucket/demo/test1.jar,obs://bucket/demo/test2.jar]
        :type dependency_jars: list[str]
        :param dependency_files: Flink Jar 作业依赖文件的 OBS 路径数组。示例：[obs://bucket/demo/test1.csv,obs://bucket/demo/test2.csv]
        :type dependency_files: list[str]
        """
        
        

        self._main_class = None
        self._main_args = None
        self._main_jar = None
        self._dependency_jars = None
        self._dependency_files = None
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

    @property
    def main_class(self):
        """Gets the main_class of this FlinkJarParameter.

        Flink Jar 作业入口类。

        :return: The main_class of this FlinkJarParameter.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        """Sets the main_class of this FlinkJarParameter.

        Flink Jar 作业入口类。

        :param main_class: The main_class of this FlinkJarParameter.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_args(self):
        """Gets the main_args of this FlinkJarParameter.

        Flink Jar 作业入口类参数，多个参数之间空格分隔。

        :return: The main_args of this FlinkJarParameter.
        :rtype: str
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        """Sets the main_args of this FlinkJarParameter.

        Flink Jar 作业入口类参数，多个参数之间空格分隔。

        :param main_args: The main_args of this FlinkJarParameter.
        :type main_args: str
        """
        self._main_args = main_args

    @property
    def main_jar(self):
        """Gets the main_jar of this FlinkJarParameter.

        Flink Jar 作业主类所在 Jar 包的 OBS 路径。

        :return: The main_jar of this FlinkJarParameter.
        :rtype: str
        """
        return self._main_jar

    @main_jar.setter
    def main_jar(self, main_jar):
        """Sets the main_jar of this FlinkJarParameter.

        Flink Jar 作业主类所在 Jar 包的 OBS 路径。

        :param main_jar: The main_jar of this FlinkJarParameter.
        :type main_jar: str
        """
        self._main_jar = main_jar

    @property
    def dependency_jars(self):
        """Gets the dependency_jars of this FlinkJarParameter.

        Flink Jar 作业依赖 Jar 包的 OBS 路径数组。示例：[obs://bucket/demo/test1.jar,obs://bucket/demo/test2.jar]

        :return: The dependency_jars of this FlinkJarParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        """Sets the dependency_jars of this FlinkJarParameter.

        Flink Jar 作业依赖 Jar 包的 OBS 路径数组。示例：[obs://bucket/demo/test1.jar,obs://bucket/demo/test2.jar]

        :param dependency_jars: The dependency_jars of this FlinkJarParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        """Gets the dependency_files of this FlinkJarParameter.

        Flink Jar 作业依赖文件的 OBS 路径数组。示例：[obs://bucket/demo/test1.csv,obs://bucket/demo/test2.csv]

        :return: The dependency_files of this FlinkJarParameter.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        """Sets the dependency_files of this FlinkJarParameter.

        Flink Jar 作业依赖文件的 OBS 路径数组。示例：[obs://bucket/demo/test1.csv,obs://bucket/demo/test2.csv]

        :param dependency_files: The dependency_files of this FlinkJarParameter.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
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
