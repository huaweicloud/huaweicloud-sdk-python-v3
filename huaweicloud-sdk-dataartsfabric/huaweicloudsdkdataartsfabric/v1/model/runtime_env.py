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
        'py_modules': 'list[str]',
        'pip': 'list[str]',
        'conda': 'object',
        'env_vars': 'dict(str, str)',
        'container': 'object',
        'worker_process_setup_hook': 'str',
        'nsight': 'str',
        'config': 'str'
    }

    attribute_map = {
        'working_dir': 'working_dir',
        'py_modules': 'py_modules',
        'pip': 'pip',
        'conda': 'conda',
        'env_vars': 'env_vars',
        'container': 'container',
        'worker_process_setup_hook': 'worker_process_setup_hook',
        'nsight': 'nsight',
        'config': 'config'
    }

    def __init__(self, working_dir=None, py_modules=None, pip=None, conda=None, env_vars=None, container=None, worker_process_setup_hook=None, nsight=None, config=None):
        r"""RuntimeEnv

        The model defined in huaweicloud sdk

        :param working_dir: 代码将在其中运行的工作目录。必须是远程URI，如s3或git路径。
        :type working_dir: str
        :param py_modules: 将与运行时环境一起安装的Python模块。这些必须是远程URI。
        :type py_modules: list[str]
        :param pip: 要安装的pip软件包列表。
        :type pip: list[str]
        :param conda: 【联合【指令【str，任何】，str】：conda YAML配置或本地conda env的名称（例如，“pytorch_p36”），
        :type conda: object
        :param env_vars: 要设置的环境变量。
        :type env_vars: dict(str, str)
        :param container: 容器配置
        :type container: object
        :param worker_process_setup_hook: hook配置信息
        :type worker_process_setup_hook: str
        :param nsight: nsight配置
        :type nsight: str
        :param config: 运行环境的配置
        :type config: str
        """
        
        

        self._working_dir = None
        self._py_modules = None
        self._pip = None
        self._conda = None
        self._env_vars = None
        self._container = None
        self._worker_process_setup_hook = None
        self._nsight = None
        self._config = None
        self.discriminator = None

        if working_dir is not None:
            self.working_dir = working_dir
        if py_modules is not None:
            self.py_modules = py_modules
        if pip is not None:
            self.pip = pip
        if conda is not None:
            self.conda = conda
        if env_vars is not None:
            self.env_vars = env_vars
        if container is not None:
            self.container = container
        if worker_process_setup_hook is not None:
            self.worker_process_setup_hook = worker_process_setup_hook
        if nsight is not None:
            self.nsight = nsight
        if config is not None:
            self.config = config

    @property
    def working_dir(self):
        r"""Gets the working_dir of this RuntimeEnv.

        代码将在其中运行的工作目录。必须是远程URI，如s3或git路径。

        :return: The working_dir of this RuntimeEnv.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this RuntimeEnv.

        代码将在其中运行的工作目录。必须是远程URI，如s3或git路径。

        :param working_dir: The working_dir of this RuntimeEnv.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def py_modules(self):
        r"""Gets the py_modules of this RuntimeEnv.

        将与运行时环境一起安装的Python模块。这些必须是远程URI。

        :return: The py_modules of this RuntimeEnv.
        :rtype: list[str]
        """
        return self._py_modules

    @py_modules.setter
    def py_modules(self, py_modules):
        r"""Sets the py_modules of this RuntimeEnv.

        将与运行时环境一起安装的Python模块。这些必须是远程URI。

        :param py_modules: The py_modules of this RuntimeEnv.
        :type py_modules: list[str]
        """
        self._py_modules = py_modules

    @property
    def pip(self):
        r"""Gets the pip of this RuntimeEnv.

        要安装的pip软件包列表。

        :return: The pip of this RuntimeEnv.
        :rtype: list[str]
        """
        return self._pip

    @pip.setter
    def pip(self, pip):
        r"""Sets the pip of this RuntimeEnv.

        要安装的pip软件包列表。

        :param pip: The pip of this RuntimeEnv.
        :type pip: list[str]
        """
        self._pip = pip

    @property
    def conda(self):
        r"""Gets the conda of this RuntimeEnv.

        【联合【指令【str，任何】，str】：conda YAML配置或本地conda env的名称（例如，“pytorch_p36”），

        :return: The conda of this RuntimeEnv.
        :rtype: object
        """
        return self._conda

    @conda.setter
    def conda(self, conda):
        r"""Sets the conda of this RuntimeEnv.

        【联合【指令【str，任何】，str】：conda YAML配置或本地conda env的名称（例如，“pytorch_p36”），

        :param conda: The conda of this RuntimeEnv.
        :type conda: object
        """
        self._conda = conda

    @property
    def env_vars(self):
        r"""Gets the env_vars of this RuntimeEnv.

        要设置的环境变量。

        :return: The env_vars of this RuntimeEnv.
        :rtype: dict(str, str)
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        r"""Sets the env_vars of this RuntimeEnv.

        要设置的环境变量。

        :param env_vars: The env_vars of this RuntimeEnv.
        :type env_vars: dict(str, str)
        """
        self._env_vars = env_vars

    @property
    def container(self):
        r"""Gets the container of this RuntimeEnv.

        容器配置

        :return: The container of this RuntimeEnv.
        :rtype: object
        """
        return self._container

    @container.setter
    def container(self, container):
        r"""Sets the container of this RuntimeEnv.

        容器配置

        :param container: The container of this RuntimeEnv.
        :type container: object
        """
        self._container = container

    @property
    def worker_process_setup_hook(self):
        r"""Gets the worker_process_setup_hook of this RuntimeEnv.

        hook配置信息

        :return: The worker_process_setup_hook of this RuntimeEnv.
        :rtype: str
        """
        return self._worker_process_setup_hook

    @worker_process_setup_hook.setter
    def worker_process_setup_hook(self, worker_process_setup_hook):
        r"""Sets the worker_process_setup_hook of this RuntimeEnv.

        hook配置信息

        :param worker_process_setup_hook: The worker_process_setup_hook of this RuntimeEnv.
        :type worker_process_setup_hook: str
        """
        self._worker_process_setup_hook = worker_process_setup_hook

    @property
    def nsight(self):
        r"""Gets the nsight of this RuntimeEnv.

        nsight配置

        :return: The nsight of this RuntimeEnv.
        :rtype: str
        """
        return self._nsight

    @nsight.setter
    def nsight(self, nsight):
        r"""Sets the nsight of this RuntimeEnv.

        nsight配置

        :param nsight: The nsight of this RuntimeEnv.
        :type nsight: str
        """
        self._nsight = nsight

    @property
    def config(self):
        r"""Gets the config of this RuntimeEnv.

        运行环境的配置

        :return: The config of this RuntimeEnv.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this RuntimeEnv.

        运行环境的配置

        :param config: The config of this RuntimeEnv.
        :type config: str
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
