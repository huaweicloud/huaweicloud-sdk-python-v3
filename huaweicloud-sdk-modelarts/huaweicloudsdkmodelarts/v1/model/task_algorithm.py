# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_config': 'TaskAlgorithmJobConfig',
        'code_dir': 'str',
        'boot_file': 'str',
        'engine': 'TaskAlgorithmEngine',
        'inputs': 'list[TaskAlgorithmInputs]',
        'outputs': 'list[TaskAlgorithmOutputs]',
        'local_code_dir': 'str',
        'working_dir': 'str',
        'environments': 'dict(str, str)'
    }

    attribute_map = {
        'job_config': 'job_config',
        'code_dir': 'code_dir',
        'boot_file': 'boot_file',
        'engine': 'engine',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'local_code_dir': 'local_code_dir',
        'working_dir': 'working_dir',
        'environments': 'environments'
    }

    def __init__(self, job_config=None, code_dir=None, boot_file=None, engine=None, inputs=None, outputs=None, local_code_dir=None, working_dir=None, environments=None):
        r"""TaskAlgorithm

        The model defined in huaweicloud sdk

        :param job_config: 
        :type job_config: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfig`
        :param code_dir: **参数解释**：算法的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type code_dir: str
        :param boot_file: **参数解释**：算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type boot_file: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmEngine`
        :param inputs: **参数解释**：算法的数据输入。 **约束限制**：不涉及。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmInputs`]
        :param outputs: **参数解释**：算法的数据输出。 **约束限制**：不涉及。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmOutputs`]
        :param local_code_dir: **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。  **取值范围**：不涉及。 **默认取值**：不涉及。
        :type local_code_dir: str
        :param working_dir: **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type working_dir: str
        :param environments: **参数解释**：训练作业环境变量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type environments: dict(str, str)
        """
        
        

        self._job_config = None
        self._code_dir = None
        self._boot_file = None
        self._engine = None
        self._inputs = None
        self._outputs = None
        self._local_code_dir = None
        self._working_dir = None
        self._environments = None
        self.discriminator = None

        if job_config is not None:
            self.job_config = job_config
        if code_dir is not None:
            self.code_dir = code_dir
        if boot_file is not None:
            self.boot_file = boot_file
        if engine is not None:
            self.engine = engine
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if local_code_dir is not None:
            self.local_code_dir = local_code_dir
        if working_dir is not None:
            self.working_dir = working_dir
        if environments is not None:
            self.environments = environments

    @property
    def job_config(self):
        r"""Gets the job_config of this TaskAlgorithm.

        :return: The job_config of this TaskAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this TaskAlgorithm.

        :param job_config: The job_config of this TaskAlgorithm.
        :type job_config: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmJobConfig`
        """
        self._job_config = job_config

    @property
    def code_dir(self):
        r"""Gets the code_dir of this TaskAlgorithm.

        **参数解释**：算法的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The code_dir of this TaskAlgorithm.
        :rtype: str
        """
        return self._code_dir

    @code_dir.setter
    def code_dir(self, code_dir):
        r"""Sets the code_dir of this TaskAlgorithm.

        **参数解释**：算法的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param code_dir: The code_dir of this TaskAlgorithm.
        :type code_dir: str
        """
        self._code_dir = code_dir

    @property
    def boot_file(self):
        r"""Gets the boot_file of this TaskAlgorithm.

        **参数解释**：算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The boot_file of this TaskAlgorithm.
        :rtype: str
        """
        return self._boot_file

    @boot_file.setter
    def boot_file(self, boot_file):
        r"""Sets the boot_file of this TaskAlgorithm.

        **参数解释**：算法的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param boot_file: The boot_file of this TaskAlgorithm.
        :type boot_file: str
        """
        self._boot_file = boot_file

    @property
    def engine(self):
        r"""Gets the engine of this TaskAlgorithm.

        :return: The engine of this TaskAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this TaskAlgorithm.

        :param engine: The engine of this TaskAlgorithm.
        :type engine: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmEngine`
        """
        self._engine = engine

    @property
    def inputs(self):
        r"""Gets the inputs of this TaskAlgorithm.

        **参数解释**：算法的数据输入。 **约束限制**：不涉及。

        :return: The inputs of this TaskAlgorithm.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmInputs`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this TaskAlgorithm.

        **参数解释**：算法的数据输入。 **约束限制**：不涉及。

        :param inputs: The inputs of this TaskAlgorithm.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmInputs`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this TaskAlgorithm.

        **参数解释**：算法的数据输出。 **约束限制**：不涉及。

        :return: The outputs of this TaskAlgorithm.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmOutputs`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this TaskAlgorithm.

        **参数解释**：算法的数据输出。 **约束限制**：不涉及。

        :param outputs: The outputs of this TaskAlgorithm.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.TaskAlgorithmOutputs`]
        """
        self._outputs = outputs

    @property
    def local_code_dir(self):
        r"""Gets the local_code_dir of this TaskAlgorithm.

        **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The local_code_dir of this TaskAlgorithm.
        :rtype: str
        """
        return self._local_code_dir

    @local_code_dir.setter
    def local_code_dir(self, local_code_dir):
        r"""Sets the local_code_dir of this TaskAlgorithm.

        **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录； - v1兼容模式下，当前字段不生效； - 当code_dir以file://为前缀时，当前字段不生效。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :param local_code_dir: The local_code_dir of this TaskAlgorithm.
        :type local_code_dir: str
        """
        self._local_code_dir = local_code_dir

    @property
    def working_dir(self):
        r"""Gets the working_dir of this TaskAlgorithm.

        **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The working_dir of this TaskAlgorithm.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this TaskAlgorithm.

        **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param working_dir: The working_dir of this TaskAlgorithm.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def environments(self):
        r"""Gets the environments of this TaskAlgorithm.

        **参数解释**：训练作业环境变量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The environments of this TaskAlgorithm.
        :rtype: dict(str, str)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this TaskAlgorithm.

        **参数解释**：训练作业环境变量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param environments: The environments of this TaskAlgorithm.
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
        if not isinstance(other, TaskAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
