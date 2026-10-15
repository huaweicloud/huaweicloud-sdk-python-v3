# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSqlParameter:

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
        'dependency_jars': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'sql_script_file': 'sql_script_file',
        'dependency_jars': 'dependency_jars'
    }

    def __init__(self, type=None, sql_script_file=None, dependency_jars=None):
        r"""FlinkSqlParameter

        The model defined in huaweicloud sdk

        :param type: **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_JOB。
        :type type: str
        :param sql_script_file: **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。
        :type sql_script_file: str
        :param dependency_jars: **参数解释**：SQL作业依赖的JAR包OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。
        :type dependency_jars: list[str]
        """
        
        

        self._type = None
        self._sql_script_file = None
        self._dependency_jars = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.sql_script_file = sql_script_file
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars

    @property
    def type(self):
        r"""Gets the type of this FlinkSqlParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_JOB。

        :return: The type of this FlinkSqlParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FlinkSqlParameter.

        **参数解释**：作业类型。 **约束限制**：固定值为 FLINK_SQL_JOB。 **取值范围**：不涉及。 **默认取值**：FLINK_SQL_JOB。

        :param type: The type of this FlinkSqlParameter.
        :type type: str
        """
        self._type = type

    @property
    def sql_script_file(self):
        r"""Gets the sql_script_file of this FlinkSqlParameter.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :return: The sql_script_file of this FlinkSqlParameter.
        :rtype: str
        """
        return self._sql_script_file

    @sql_script_file.setter
    def sql_script_file(self, sql_script_file):
        r"""Sets the sql_script_file of this FlinkSqlParameter.

        **参数解释**：SQL脚本所在的OBS文件路径，用于指定SQL作业的脚本文件。 **约束限制**：不涉及。 **取值范围**：OBS URL格式，长度为1~512个字符，以obs://开头。 **默认取值**：不涉及。

        :param sql_script_file: The sql_script_file of this FlinkSqlParameter.
        :type sql_script_file: str
        """
        self._sql_script_file = sql_script_file

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this FlinkSqlParameter.

        **参数解释**：SQL作业依赖的JAR包OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :return: The dependency_jars of this FlinkSqlParameter.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this FlinkSqlParameter.

        **参数解释**：SQL作业依赖的JAR包OBS路径列表，用于指定作业运行所需的依赖JAR包，单个路径为OBS URL格式，长度为1~512个字符，以obs://开头。 **约束限制**：依赖JAR包数量不能超过100个。

        :param dependency_jars: The dependency_jars of this FlinkSqlParameter.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

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
        if not isinstance(other, FlinkSqlParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
