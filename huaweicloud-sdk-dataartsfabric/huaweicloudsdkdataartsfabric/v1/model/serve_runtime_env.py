# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServeRuntimeEnv:

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
        'env_vars': 'dict(str, str)'
    }

    attribute_map = {
        'working_dir': 'working_dir',
        'env_vars': 'env_vars'
    }

    def __init__(self, working_dir=None, env_vars=None):
        r"""ServeRuntimeEnv

        The model defined in huaweicloud sdk

        :param working_dir: **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如s3或本地路径。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type working_dir: str
        :param env_vars: **参数解释**：要设置的环境变量。 **约束限制**：不涉及。
        :type env_vars: dict(str, str)
        """
        
        

        self._working_dir = None
        self._env_vars = None
        self.discriminator = None

        if working_dir is not None:
            self.working_dir = working_dir
        if env_vars is not None:
            self.env_vars = env_vars

    @property
    def working_dir(self):
        r"""Gets the working_dir of this ServeRuntimeEnv.

        **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如s3或本地路径。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The working_dir of this ServeRuntimeEnv.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this ServeRuntimeEnv.

        **参数解释**：代码将在其中运行的工作目录。 **约束限制**：必须是远程URI，如s3或本地路径。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param working_dir: The working_dir of this ServeRuntimeEnv.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def env_vars(self):
        r"""Gets the env_vars of this ServeRuntimeEnv.

        **参数解释**：要设置的环境变量。 **约束限制**：不涉及。

        :return: The env_vars of this ServeRuntimeEnv.
        :rtype: dict(str, str)
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        r"""Sets the env_vars of this ServeRuntimeEnv.

        **参数解释**：要设置的环境变量。 **约束限制**：不涉及。

        :param env_vars: The env_vars of this ServeRuntimeEnv.
        :type env_vars: dict(str, str)
        """
        self._env_vars = env_vars

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
        if not isinstance(other, ServeRuntimeEnv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
