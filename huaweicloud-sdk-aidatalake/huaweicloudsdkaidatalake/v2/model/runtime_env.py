# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeEnv:

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
        'pip': 'list[str]',
        'env_vars': 'dict(str, str)',
        'config': 'dict(str, object)'
    }

    attribute_map = {
        'working_dir': 'working_dir',
        'pip': 'pip',
        'env_vars': 'env_vars',
        'config': 'config'
    }

    def __init__(self, working_dir=None, pip=None, env_vars=None, config=None):
        r"""RuntimeEnv

        The model defined in huaweicloud sdk

        :param working_dir: **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如OBS路径。 **取值范围**：最小长度1，最大长度2048。 **默认取值**：不涉及。
        :type working_dir: str
        :param pip: **参数解释**：要安装的pip软件包列表。 **约束限制**：最小个数0，最大个数1023。
        :type pip: list[str]
        :param env_vars: **参数解释**：要设置的环境变量。key为环境变量名称，value为环境变量值，均为String类型。 **约束限制**：不涉及。
        :type env_vars: dict(str, str)
        :param config: **参数解释**：运行环境的配置。key为配置项名称，value为配置项值。 **约束限制**：不涉及。
        :type config: dict(str, object)
        """
        
        

        self._working_dir = None
        self._pip = None
        self._env_vars = None
        self._config = None
        self.discriminator = None

        if working_dir is not None:
            self.working_dir = working_dir
        if pip is not None:
            self.pip = pip
        if env_vars is not None:
            self.env_vars = env_vars
        if config is not None:
            self.config = config

    @property
    def working_dir(self):
        r"""Gets the working_dir of this RuntimeEnv.

        **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如OBS路径。 **取值范围**：最小长度1，最大长度2048。 **默认取值**：不涉及。

        :return: The working_dir of this RuntimeEnv.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this RuntimeEnv.

        **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如OBS路径。 **取值范围**：最小长度1，最大长度2048。 **默认取值**：不涉及。

        :param working_dir: The working_dir of this RuntimeEnv.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def pip(self):
        r"""Gets the pip of this RuntimeEnv.

        **参数解释**：要安装的pip软件包列表。 **约束限制**：最小个数0，最大个数1023。

        :return: The pip of this RuntimeEnv.
        :rtype: list[str]
        """
        return self._pip

    @pip.setter
    def pip(self, pip):
        r"""Sets the pip of this RuntimeEnv.

        **参数解释**：要安装的pip软件包列表。 **约束限制**：最小个数0，最大个数1023。

        :param pip: The pip of this RuntimeEnv.
        :type pip: list[str]
        """
        self._pip = pip

    @property
    def env_vars(self):
        r"""Gets the env_vars of this RuntimeEnv.

        **参数解释**：要设置的环境变量。key为环境变量名称，value为环境变量值，均为String类型。 **约束限制**：不涉及。

        :return: The env_vars of this RuntimeEnv.
        :rtype: dict(str, str)
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        r"""Sets the env_vars of this RuntimeEnv.

        **参数解释**：要设置的环境变量。key为环境变量名称，value为环境变量值，均为String类型。 **约束限制**：不涉及。

        :param env_vars: The env_vars of this RuntimeEnv.
        :type env_vars: dict(str, str)
        """
        self._env_vars = env_vars

    @property
    def config(self):
        r"""Gets the config of this RuntimeEnv.

        **参数解释**：运行环境的配置。key为配置项名称，value为配置项值。 **约束限制**：不涉及。

        :return: The config of this RuntimeEnv.
        :rtype: dict(str, object)
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this RuntimeEnv.

        **参数解释**：运行环境的配置。key为配置项名称，value为配置项值。 **约束限制**：不涉及。

        :param config: The config of this RuntimeEnv.
        :type config: dict(str, object)
        """
        self._config = config

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
        if not isinstance(other, RuntimeEnv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
