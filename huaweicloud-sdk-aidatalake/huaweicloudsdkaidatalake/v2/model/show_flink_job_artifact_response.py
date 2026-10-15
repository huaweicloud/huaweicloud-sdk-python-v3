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
        'main_jar': 'str',
        'main_class': 'str',
        'main_args': 'list[str]',
        'dependency_files': 'list[str]',
        'sql_gateway_config': 'ShowFlinkSqlGatewayConfigResponseBody'
    }

    attribute_map = {
        'type': 'type',
        'sql_script_file': 'sql_script_file',
        'dependency_jars': 'dependency_jars',
        'main_jar': 'main_jar',
        'main_class': 'main_class',
        'main_args': 'main_args',
        'dependency_files': 'dependency_files',
        'sql_gateway_config': 'sql_gateway_config'
    }

    def __init__(self, type=None, sql_script_file=None, dependency_jars=None, main_jar=None, main_class=None, main_args=None, dependency_files=None, sql_gateway_config=None):
        r"""ShowFlinkJobArtifactResponse

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param sql_script_file: **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。
        :type sql_script_file: str
        :param dependency_jars: **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。
        :type dependency_jars: list[str]
        :param main_jar: **参数解释**：JAR作业主类所在JAR包的OBS路径，用于指定作业的入口JAR包。 **取值范围**：长度为1~512个字符，以obs://开头。
        :type main_jar: str
        :param main_class: **参数解释**：JAR作业入口类名称，用于指定作业的入口类。 **取值范围**：长度不超过512个字符。
        :type main_class: str
        :param main_args: **参数解释**：JAR作业入口类参数，用于传递运行参数。
        :type main_args: list[str]
        :param dependency_files: **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。
        :type dependency_files: list[str]
        :param sql_gateway_config: 
        :type sql_gateway_config: :class:`huaweicloudsdkaidatalake.v2.ShowFlinkSqlGatewayConfigResponseBody`
        """
        
        

        self._type = None
        self._sql_script_file = None
        self._dependency_jars = None
        self._main_jar = None
        self._main_class = None
        self._main_args = None
        self._dependency_files = None
        self._sql_gateway_config = None
        self.discriminator = None

        self.type = type
        if sql_script_file is not None:
            self.sql_script_file = sql_script_file
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if main_jar is not None:
            self.main_jar = main_jar
        if main_class is not None:
            self.main_class = main_class
        if main_args is not None:
            self.main_args = main_args
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if sql_gateway_config is not None:
            self.sql_gateway_config = sql_gateway_config

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

        **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。

        :return: The dependency_jars of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业依赖JAR包的OBS路径，用于指定作业运行所需的依赖JAR包。

        :param dependency_jars: The dependency_jars of this ShowFlinkJobArtifactResponse.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

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

        **参数解释**：JAR作业入口类参数，用于传递运行参数。

        :return: The main_args of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._main_args

    @main_args.setter
    def main_args(self, main_args):
        r"""Sets the main_args of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业入口类参数，用于传递运行参数。

        :param main_args: The main_args of this ShowFlinkJobArtifactResponse.
        :type main_args: list[str]
        """
        self._main_args = main_args

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。

        :return: The dependency_files of this ShowFlinkJobArtifactResponse.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this ShowFlinkJobArtifactResponse.

        **参数解释**：JAR作业依赖文件的OBS路径列表，用于指定作业运行所需的依赖文件。

        :param dependency_files: The dependency_files of this ShowFlinkJobArtifactResponse.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

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
