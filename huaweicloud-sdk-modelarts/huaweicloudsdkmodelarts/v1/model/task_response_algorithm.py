# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskResponseAlgorithm:

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
        'inputs': 'AlgorithmInput',
        'outputs': 'AlgorithmOutput',
        'engine': 'AlgorithmEngine',
        'local_code_dir': 'str',
        'working_dir': 'str',
        'environments': 'dict(str, str)'
    }

    attribute_map = {
        'code_dir': 'code_dir',
        'boot_file': 'boot_file',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'engine': 'engine',
        'local_code_dir': 'local_code_dir',
        'working_dir': 'working_dir',
        'environments': 'environments'
    }

    def __init__(self, code_dir=None, boot_file=None, inputs=None, outputs=None, engine=None, local_code_dir=None, working_dir=None, environments=None):
        r"""TaskResponseAlgorithm

        The model defined in huaweicloud sdk

        :param code_dir: 算法启动文件所在目录绝对路径。
        :type code_dir: str
        :param boot_file: 算法启动文件绝对路径。
        :type boot_file: str
        :param inputs: 
        :type inputs: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInput`
        :param outputs: 
        :type outputs: :class:`huaweicloudsdkmodelarts.v1.AlgorithmOutput`
        :param engine: 
        :type engine: :class:`huaweicloudsdkmodelarts.v1.AlgorithmEngine`
        :param local_code_dir: 算法的代码目录下载到训练容器内的本地路径。规则如下： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。
        :type local_code_dir: str
        :param working_dir: 运行算法时所在的工作目录。规则：v1兼容模式下，当前字段不生效。
        :type working_dir: str
        :param environments: **参数解释**：训练作业相关的环境变量。 **取值范围**：不涉及。
        :type environments: dict(str, str)
        """
        
        

        self._code_dir = None
        self._boot_file = None
        self._inputs = None
        self._outputs = None
        self._engine = None
        self._local_code_dir = None
        self._working_dir = None
        self._environments = None
        self.discriminator = None

        if code_dir is not None:
            self.code_dir = code_dir
        if boot_file is not None:
            self.boot_file = boot_file
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if engine is not None:
            self.engine = engine
        if local_code_dir is not None:
            self.local_code_dir = local_code_dir
        if working_dir is not None:
            self.working_dir = working_dir
        if environments is not None:
            self.environments = environments

    @property
    def code_dir(self):
        r"""Gets the code_dir of this TaskResponseAlgorithm.

        算法启动文件所在目录绝对路径。

        :return: The code_dir of this TaskResponseAlgorithm.
        :rtype: str
        """
        return self._code_dir

    @code_dir.setter
    def code_dir(self, code_dir):
        r"""Sets the code_dir of this TaskResponseAlgorithm.

        算法启动文件所在目录绝对路径。

        :param code_dir: The code_dir of this TaskResponseAlgorithm.
        :type code_dir: str
        """
        self._code_dir = code_dir

    @property
    def boot_file(self):
        r"""Gets the boot_file of this TaskResponseAlgorithm.

        算法启动文件绝对路径。

        :return: The boot_file of this TaskResponseAlgorithm.
        :rtype: str
        """
        return self._boot_file

    @boot_file.setter
    def boot_file(self, boot_file):
        r"""Sets the boot_file of this TaskResponseAlgorithm.

        算法启动文件绝对路径。

        :param boot_file: The boot_file of this TaskResponseAlgorithm.
        :type boot_file: str
        """
        self._boot_file = boot_file

    @property
    def inputs(self):
        r"""Gets the inputs of this TaskResponseAlgorithm.

        :return: The inputs of this TaskResponseAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInput`
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this TaskResponseAlgorithm.

        :param inputs: The inputs of this TaskResponseAlgorithm.
        :type inputs: :class:`huaweicloudsdkmodelarts.v1.AlgorithmInput`
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this TaskResponseAlgorithm.

        :return: The outputs of this TaskResponseAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmOutput`
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this TaskResponseAlgorithm.

        :param outputs: The outputs of this TaskResponseAlgorithm.
        :type outputs: :class:`huaweicloudsdkmodelarts.v1.AlgorithmOutput`
        """
        self._outputs = outputs

    @property
    def engine(self):
        r"""Gets the engine of this TaskResponseAlgorithm.

        :return: The engine of this TaskResponseAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this TaskResponseAlgorithm.

        :param engine: The engine of this TaskResponseAlgorithm.
        :type engine: :class:`huaweicloudsdkmodelarts.v1.AlgorithmEngine`
        """
        self._engine = engine

    @property
    def local_code_dir(self):
        r"""Gets the local_code_dir of this TaskResponseAlgorithm.

        算法的代码目录下载到训练容器内的本地路径。规则如下： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。

        :return: The local_code_dir of this TaskResponseAlgorithm.
        :rtype: str
        """
        return self._local_code_dir

    @local_code_dir.setter
    def local_code_dir(self, local_code_dir):
        r"""Sets the local_code_dir of this TaskResponseAlgorithm.

        算法的代码目录下载到训练容器内的本地路径。规则如下： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。

        :param local_code_dir: The local_code_dir of this TaskResponseAlgorithm.
        :type local_code_dir: str
        """
        self._local_code_dir = local_code_dir

    @property
    def working_dir(self):
        r"""Gets the working_dir of this TaskResponseAlgorithm.

        运行算法时所在的工作目录。规则：v1兼容模式下，当前字段不生效。

        :return: The working_dir of this TaskResponseAlgorithm.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this TaskResponseAlgorithm.

        运行算法时所在的工作目录。规则：v1兼容模式下，当前字段不生效。

        :param working_dir: The working_dir of this TaskResponseAlgorithm.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def environments(self):
        r"""Gets the environments of this TaskResponseAlgorithm.

        **参数解释**：训练作业相关的环境变量。 **取值范围**：不涉及。

        :return: The environments of this TaskResponseAlgorithm.
        :rtype: dict(str, str)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this TaskResponseAlgorithm.

        **参数解释**：训练作业相关的环境变量。 **取值范围**：不涉及。

        :param environments: The environments of this TaskResponseAlgorithm.
        :type environments: dict(str, str)
        """
        self._environments = environments

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
        if not isinstance(other, TaskResponseAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
