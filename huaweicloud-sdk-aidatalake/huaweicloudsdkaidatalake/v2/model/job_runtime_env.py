# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRuntimeEnv:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'working_dir': 'str',
        'dependency_dir': 'list[str]',
        'python_version': 'str',
        'env_vars': 'dict(str, str)',
        'pip': 'list[str]'
    }

    attribute_map = {
        'working_dir': 'working_dir',
        'dependency_dir': 'dependency_dir',
        'python_version': 'python_version',
        'env_vars': 'env_vars',
        'pip': 'pip'
    }

    def __init__(self, working_dir=None, dependency_dir=None, python_version=None, env_vars=None, pip=None):
        r"""JobRuntimeEnv

        The model defined in huaweicloud sdk

        :param working_dir: **参数解释**：作业运行工作目录。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。
        :type working_dir: str
        :param dependency_dir: **参数解释**：作业依赖的zip包路径。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。
        :type dependency_dir: list[str]
        :param python_version: **参数解释**：作业运行Dataframe版本号。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。
        :type python_version: str
        :param env_vars: **参数解释**：作业运行环境变量。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。
        :type env_vars: dict(str, str)
        :param pip: **参数解释**：作业运行依赖的软件包列表。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。
        :type pip: list[str]
        """
        
        

        self._working_dir = None
        self._dependency_dir = None
        self._python_version = None
        self._env_vars = None
        self._pip = None
        self.discriminator = None

        self.working_dir = working_dir
        if dependency_dir is not None:
            self.dependency_dir = dependency_dir
        if python_version is not None:
            self.python_version = python_version
        if env_vars is not None:
            self.env_vars = env_vars
        if pip is not None:
            self.pip = pip

    @property
    def working_dir(self):
        r"""Gets the working_dir of this JobRuntimeEnv.

        **参数解释**：作业运行工作目录。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :return: The working_dir of this JobRuntimeEnv.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this JobRuntimeEnv.

        **参数解释**：作业运行工作目录。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :param working_dir: The working_dir of this JobRuntimeEnv.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def dependency_dir(self):
        r"""Gets the dependency_dir of this JobRuntimeEnv.

        **参数解释**：作业依赖的zip包路径。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :return: The dependency_dir of this JobRuntimeEnv.
        :rtype: list[str]
        """
        return self._dependency_dir

    @dependency_dir.setter
    def dependency_dir(self, dependency_dir):
        r"""Sets the dependency_dir of this JobRuntimeEnv.

        **参数解释**：作业依赖的zip包路径。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :param dependency_dir: The dependency_dir of this JobRuntimeEnv.
        :type dependency_dir: list[str]
        """
        self._dependency_dir = dependency_dir

    @property
    def python_version(self):
        r"""Gets the python_version of this JobRuntimeEnv.

        **参数解释**：作业运行Dataframe版本号。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :return: The python_version of this JobRuntimeEnv.
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        r"""Sets the python_version of this JobRuntimeEnv.

        **参数解释**：作业运行Dataframe版本号。  **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :param python_version: The python_version of this JobRuntimeEnv.
        :type python_version: str
        """
        self._python_version = python_version

    @property
    def env_vars(self):
        r"""Gets the env_vars of this JobRuntimeEnv.

        **参数解释**：作业运行环境变量。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。

        :return: The env_vars of this JobRuntimeEnv.
        :rtype: dict(str, str)
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        r"""Sets the env_vars of this JobRuntimeEnv.

        **参数解释**：作业运行环境变量。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。

        :param env_vars: The env_vars of this JobRuntimeEnv.
        :type env_vars: dict(str, str)
        """
        self._env_vars = env_vars

    @property
    def pip(self):
        r"""Gets the pip of this JobRuntimeEnv.

        **参数解释**：作业运行依赖的软件包列表。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。

        :return: The pip of this JobRuntimeEnv.
        :rtype: list[str]
        """
        return self._pip

    @pip.setter
    def pip(self, pip):
        r"""Sets the pip of this JobRuntimeEnv.

        **参数解释**：作业运行依赖的软件包列表。  **约束限制**：不涉及。 **取值范围**：长度为0~1024。 **默认取值**：不涉及。

        :param pip: The pip of this JobRuntimeEnv.
        :type pip: list[str]
        """
        self._pip = pip

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
        if not isinstance(other, JobRuntimeEnv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
