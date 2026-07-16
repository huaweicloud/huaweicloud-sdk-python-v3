# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_dir': 'str',
        'boot_file': 'str',
        'command': 'str',
        'parameters': 'list[Parameters]',
        'inputs': 'list[AlgorithmCreateInput]',
        'outputs': 'list[AlgorithmCreateOutput]',
        'engine': 'AlgorithmCreateEngine',
        'parameters_customization': 'bool'
    }

    attribute_map = {
        'code_dir': 'code_dir',
        'boot_file': 'boot_file',
        'command': 'command',
        'parameters': 'parameters',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'engine': 'engine',
        'parameters_customization': 'parameters_customization'
    }

    def __init__(self, code_dir=None, boot_file=None, command=None, parameters=None, inputs=None, outputs=None, engine=None, parameters_customization=None):
        r"""AlgorithmJobConfig

        The model defined in huaweicloud sdk

        :param code_dir: 算法的代码目录。如：“/usr/app/”。应与boot_file一同出现。
        :type code_dir: str
        :param boot_file: 算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。应与code_dir一同出现。
        :type boot_file: str
        :param command: 自定义镜像算法的容器启动命令。
        :type command: str
        :param parameters: 算法的运行参数。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        :param inputs: 算法的数据输入。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateInput`]
        :param outputs: 算法的数据输出。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateOutput`]
        :param engine: 
        :type engine: :class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateEngine`
        :param parameters_customization: 算法是否允许创建训练作业时自定义超参。
        :type parameters_customization: bool
        """
        
        

        self._code_dir = None
        self._boot_file = None
        self._command = None
        self._parameters = None
        self._inputs = None
        self._outputs = None
        self._engine = None
        self._parameters_customization = None
        self.discriminator = None

        if code_dir is not None:
            self.code_dir = code_dir
        if boot_file is not None:
            self.boot_file = boot_file
        if command is not None:
            self.command = command
        if parameters is not None:
            self.parameters = parameters
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if engine is not None:
            self.engine = engine
        if parameters_customization is not None:
            self.parameters_customization = parameters_customization

    @property
    def code_dir(self):
        r"""Gets the code_dir of this AlgorithmJobConfig.

        算法的代码目录。如：“/usr/app/”。应与boot_file一同出现。

        :return: The code_dir of this AlgorithmJobConfig.
        :rtype: str
        """
        return self._code_dir

    @code_dir.setter
    def code_dir(self, code_dir):
        r"""Sets the code_dir of this AlgorithmJobConfig.

        算法的代码目录。如：“/usr/app/”。应与boot_file一同出现。

        :param code_dir: The code_dir of this AlgorithmJobConfig.
        :type code_dir: str
        """
        self._code_dir = code_dir

    @property
    def boot_file(self):
        r"""Gets the boot_file of this AlgorithmJobConfig.

        算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。应与code_dir一同出现。

        :return: The boot_file of this AlgorithmJobConfig.
        :rtype: str
        """
        return self._boot_file

    @boot_file.setter
    def boot_file(self, boot_file):
        r"""Sets the boot_file of this AlgorithmJobConfig.

        算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。应与code_dir一同出现。

        :param boot_file: The boot_file of this AlgorithmJobConfig.
        :type boot_file: str
        """
        self._boot_file = boot_file

    @property
    def command(self):
        r"""Gets the command of this AlgorithmJobConfig.

        自定义镜像算法的容器启动命令。

        :return: The command of this AlgorithmJobConfig.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this AlgorithmJobConfig.

        自定义镜像算法的容器启动命令。

        :param command: The command of this AlgorithmJobConfig.
        :type command: str
        """
        self._command = command

    @property
    def parameters(self):
        r"""Gets the parameters of this AlgorithmJobConfig.

        算法的运行参数。

        :return: The parameters of this AlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this AlgorithmJobConfig.

        算法的运行参数。

        :param parameters: The parameters of this AlgorithmJobConfig.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        """
        self._parameters = parameters

    @property
    def inputs(self):
        r"""Gets the inputs of this AlgorithmJobConfig.

        算法的数据输入。

        :return: The inputs of this AlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this AlgorithmJobConfig.

        算法的数据输入。

        :param inputs: The inputs of this AlgorithmJobConfig.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateInput`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this AlgorithmJobConfig.

        算法的数据输出。

        :return: The outputs of this AlgorithmJobConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this AlgorithmJobConfig.

        算法的数据输出。

        :param outputs: The outputs of this AlgorithmJobConfig.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateOutput`]
        """
        self._outputs = outputs

    @property
    def engine(self):
        r"""Gets the engine of this AlgorithmJobConfig.

        :return: The engine of this AlgorithmJobConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this AlgorithmJobConfig.

        :param engine: The engine of this AlgorithmJobConfig.
        :type engine: :class:`huaweicloudsdkmodelarts.v1.AlgorithmCreateEngine`
        """
        self._engine = engine

    @property
    def parameters_customization(self):
        r"""Gets the parameters_customization of this AlgorithmJobConfig.

        算法是否允许创建训练作业时自定义超参。

        :return: The parameters_customization of this AlgorithmJobConfig.
        :rtype: bool
        """
        return self._parameters_customization

    @parameters_customization.setter
    def parameters_customization(self, parameters_customization):
        r"""Sets the parameters_customization of this AlgorithmJobConfig.

        算法是否允许创建训练作业时自定义超参。

        :param parameters_customization: The parameters_customization of this AlgorithmJobConfig.
        :type parameters_customization: bool
        """
        self._parameters_customization = parameters_customization

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
        if not isinstance(other, AlgorithmJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
