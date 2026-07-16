# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAlgorithm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'subscription_id': 'str',
        'item_version_id': 'str',
        'code_dir': 'str',
        'boot_file': 'str',
        'autosearch_config_path': 'str',
        'autosearch_framework_path': 'str',
        'command': 'str',
        'parameters': 'list[Parameters]',
        'policies': 'JobPolicies',
        'inputs': 'list[Input]',
        'outputs': 'list[Output]',
        'engine': 'JobEngine',
        'local_code_dir': 'str',
        'working_dir': 'str',
        'environments': 'dict(str, str)',
        'summary': 'Summary'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subscription_id': 'subscription_id',
        'item_version_id': 'item_version_id',
        'code_dir': 'code_dir',
        'boot_file': 'boot_file',
        'autosearch_config_path': 'autosearch_config_path',
        'autosearch_framework_path': 'autosearch_framework_path',
        'command': 'command',
        'parameters': 'parameters',
        'policies': 'policies',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'engine': 'engine',
        'local_code_dir': 'local_code_dir',
        'working_dir': 'working_dir',
        'environments': 'environments',
        'summary': 'summary'
    }

    def __init__(self, id=None, name=None, subscription_id=None, item_version_id=None, code_dir=None, boot_file=None, autosearch_config_path=None, autosearch_framework_path=None, command=None, parameters=None, policies=None, inputs=None, outputs=None, engine=None, local_code_dir=None, working_dir=None, environments=None, summary=None):
        r"""JobAlgorithm

        The model defined in huaweicloud sdk

        :param id: **参数解释**：算法管理的算法id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：算法名称。无需填写。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param subscription_id: **参数解释**：订阅算法的订阅ID。 **约束限制**：应与item_version_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type subscription_id: str
        :param item_version_id: **参数解释**：订阅算法的版本。 **约束限制**：应与subscription_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type item_version_id: str
        :param code_dir: **参数解释**：训练作业的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现，如果boot_file填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type code_dir: str
        :param boot_file: **参数解释**：训练作业的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现，如果code_dir填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type boot_file: str
        :param autosearch_config_path: **参数解释**：自动化搜索作业的yaml配置路径，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type autosearch_config_path: str
        :param autosearch_framework_path: **参数解释**：自动化搜索作业的框架代码目录，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type autosearch_framework_path: str
        :param command: **参数解释**：自定义镜像场景下，训练作业的自定义镜像的容器的启动命令。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type command: str
        :param parameters: **参数解释**：训练作业的运行参数。 **约束限制**：不涉及。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        :param policies: 
        :type policies: :class:`huaweicloudsdkmodelarts.v1.JobPolicies`
        :param inputs: **参数解释**：训练作业的数据输入。 **约束限制**：不涉及。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        :param outputs: **参数解释**：训练作业的结果输出。 **约束限制**：不涉及。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        :param engine: 
        :type engine: :class:`huaweicloudsdkmodelarts.v1.JobEngine`
        :param local_code_dir: **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录。 - v1兼容模式下，当前字段不生效。 - 当code_dir以file://为前缀时，当前字段不生效。 - 不支持配置成/home/ma-user/modelarts，/home/ma-user/modelarts-dev，/home/ma-user/infer以及它们底下的目录，也不支持配置成/home/ma-user  **取值范围**：不涉及。 **默认取值**：不涉及。
        :type local_code_dir: str
        :param working_dir: **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type working_dir: str
        :param environments: **参数解释**：训练作业的环境变量。格式：\&quot;key\&quot;:\&quot;value\&quot;。 **约束限制**：其中key最大允许填写8192字符，value最大允许填写4096字符，最多允许100对环境变量。变量名应该仅包含字母、数字、下划线，且以字母或下划线开头。 注：不支持使用符号 $ 引用变量。
        :type environments: dict(str, str)
        :param summary: 
        :type summary: :class:`huaweicloudsdkmodelarts.v1.Summary`
        """
        
        

        self._id = None
        self._name = None
        self._subscription_id = None
        self._item_version_id = None
        self._code_dir = None
        self._boot_file = None
        self._autosearch_config_path = None
        self._autosearch_framework_path = None
        self._command = None
        self._parameters = None
        self._policies = None
        self._inputs = None
        self._outputs = None
        self._engine = None
        self._local_code_dir = None
        self._working_dir = None
        self._environments = None
        self._summary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if item_version_id is not None:
            self.item_version_id = item_version_id
        if code_dir is not None:
            self.code_dir = code_dir
        if boot_file is not None:
            self.boot_file = boot_file
        if autosearch_config_path is not None:
            self.autosearch_config_path = autosearch_config_path
        if autosearch_framework_path is not None:
            self.autosearch_framework_path = autosearch_framework_path
        if command is not None:
            self.command = command
        if parameters is not None:
            self.parameters = parameters
        if policies is not None:
            self.policies = policies
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
        if summary is not None:
            self.summary = summary

    @property
    def id(self):
        r"""Gets the id of this JobAlgorithm.

        **参数解释**：算法管理的算法id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The id of this JobAlgorithm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobAlgorithm.

        **参数解释**：算法管理的算法id。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param id: The id of this JobAlgorithm.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobAlgorithm.

        **参数解释**：算法名称。无需填写。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this JobAlgorithm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobAlgorithm.

        **参数解释**：算法名称。无需填写。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this JobAlgorithm.
        :type name: str
        """
        self._name = name

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this JobAlgorithm.

        **参数解释**：订阅算法的订阅ID。 **约束限制**：应与item_version_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The subscription_id of this JobAlgorithm.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this JobAlgorithm.

        **参数解释**：订阅算法的订阅ID。 **约束限制**：应与item_version_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param subscription_id: The subscription_id of this JobAlgorithm.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def item_version_id(self):
        r"""Gets the item_version_id of this JobAlgorithm.

        **参数解释**：订阅算法的版本。 **约束限制**：应与subscription_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The item_version_id of this JobAlgorithm.
        :rtype: str
        """
        return self._item_version_id

    @item_version_id.setter
    def item_version_id(self, item_version_id):
        r"""Sets the item_version_id of this JobAlgorithm.

        **参数解释**：订阅算法的版本。 **约束限制**：应与subscription_id一同出现。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param item_version_id: The item_version_id of this JobAlgorithm.
        :type item_version_id: str
        """
        self._item_version_id = item_version_id

    @property
    def code_dir(self):
        r"""Gets the code_dir of this JobAlgorithm.

        **参数解释**：训练作业的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现，如果boot_file填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The code_dir of this JobAlgorithm.
        :rtype: str
        """
        return self._code_dir

    @code_dir.setter
    def code_dir(self, code_dir):
        r"""Sets the code_dir of this JobAlgorithm.

        **参数解释**：训练作业的代码目录。如：“/usr/app/”。 **约束限制**：应与boot_file一同出现，如果boot_file填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param code_dir: The code_dir of this JobAlgorithm.
        :type code_dir: str
        """
        self._code_dir = code_dir

    @property
    def boot_file(self):
        r"""Gets the boot_file of this JobAlgorithm.

        **参数解释**：训练作业的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现，如果code_dir填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The boot_file of this JobAlgorithm.
        :rtype: str
        """
        return self._boot_file

    @boot_file.setter
    def boot_file(self, boot_file):
        r"""Sets the boot_file of this JobAlgorithm.

        **参数解释**：训练作业的代码启动文件，需要在代码目录下。如：“/usr/app/boot.py”。 **约束限制**：应与code_dir一同出现，如果code_dir填入id或subscription_id+item_version_id，则此参数无需填写。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param boot_file: The boot_file of this JobAlgorithm.
        :type boot_file: str
        """
        self._boot_file = boot_file

    @property
    def autosearch_config_path(self):
        r"""Gets the autosearch_config_path of this JobAlgorithm.

        **参数解释**：自动化搜索作业的yaml配置路径，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The autosearch_config_path of this JobAlgorithm.
        :rtype: str
        """
        return self._autosearch_config_path

    @autosearch_config_path.setter
    def autosearch_config_path(self, autosearch_config_path):
        r"""Sets the autosearch_config_path of this JobAlgorithm.

        **参数解释**：自动化搜索作业的yaml配置路径，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param autosearch_config_path: The autosearch_config_path of this JobAlgorithm.
        :type autosearch_config_path: str
        """
        self._autosearch_config_path = autosearch_config_path

    @property
    def autosearch_framework_path(self):
        r"""Gets the autosearch_framework_path of this JobAlgorithm.

        **参数解释**：自动化搜索作业的框架代码目录，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The autosearch_framework_path of this JobAlgorithm.
        :rtype: str
        """
        return self._autosearch_framework_path

    @autosearch_framework_path.setter
    def autosearch_framework_path(self, autosearch_framework_path):
        r"""Sets the autosearch_framework_path of this JobAlgorithm.

        **参数解释**：自动化搜索作业的框架代码目录，需要提供一个OBS路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param autosearch_framework_path: The autosearch_framework_path of this JobAlgorithm.
        :type autosearch_framework_path: str
        """
        self._autosearch_framework_path = autosearch_framework_path

    @property
    def command(self):
        r"""Gets the command of this JobAlgorithm.

        **参数解释**：自定义镜像场景下，训练作业的自定义镜像的容器的启动命令。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The command of this JobAlgorithm.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this JobAlgorithm.

        **参数解释**：自定义镜像场景下，训练作业的自定义镜像的容器的启动命令。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param command: The command of this JobAlgorithm.
        :type command: str
        """
        self._command = command

    @property
    def parameters(self):
        r"""Gets the parameters of this JobAlgorithm.

        **参数解释**：训练作业的运行参数。 **约束限制**：不涉及。

        :return: The parameters of this JobAlgorithm.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this JobAlgorithm.

        **参数解释**：训练作业的运行参数。 **约束限制**：不涉及。

        :param parameters: The parameters of this JobAlgorithm.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.Parameters`]
        """
        self._parameters = parameters

    @property
    def policies(self):
        r"""Gets the policies of this JobAlgorithm.

        :return: The policies of this JobAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobPolicies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this JobAlgorithm.

        :param policies: The policies of this JobAlgorithm.
        :type policies: :class:`huaweicloudsdkmodelarts.v1.JobPolicies`
        """
        self._policies = policies

    @property
    def inputs(self):
        r"""Gets the inputs of this JobAlgorithm.

        **参数解释**：训练作业的数据输入。 **约束限制**：不涉及。

        :return: The inputs of this JobAlgorithm.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this JobAlgorithm.

        **参数解释**：训练作业的数据输入。 **约束限制**：不涉及。

        :param inputs: The inputs of this JobAlgorithm.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.Input`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this JobAlgorithm.

        **参数解释**：训练作业的结果输出。 **约束限制**：不涉及。

        :return: The outputs of this JobAlgorithm.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this JobAlgorithm.

        **参数解释**：训练作业的结果输出。 **约束限制**：不涉及。

        :param outputs: The outputs of this JobAlgorithm.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.Output`]
        """
        self._outputs = outputs

    @property
    def engine(self):
        r"""Gets the engine of this JobAlgorithm.

        :return: The engine of this JobAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this JobAlgorithm.

        :param engine: The engine of this JobAlgorithm.
        :type engine: :class:`huaweicloudsdkmodelarts.v1.JobEngine`
        """
        self._engine = engine

    @property
    def local_code_dir(self):
        r"""Gets the local_code_dir of this JobAlgorithm.

        **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录。 - v1兼容模式下，当前字段不生效。 - 当code_dir以file://为前缀时，当前字段不生效。 - 不支持配置成/home/ma-user/modelarts，/home/ma-user/modelarts-dev，/home/ma-user/infer以及它们底下的目录，也不支持配置成/home/ma-user  **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The local_code_dir of this JobAlgorithm.
        :rtype: str
        """
        return self._local_code_dir

    @local_code_dir.setter
    def local_code_dir(self, local_code_dir):
        r"""Sets the local_code_dir of this JobAlgorithm.

        **参数解释**：算法的代码目录下载到训练容器内的本地路径。 **约束限制**： - 必须为/home下的目录。 - v1兼容模式下，当前字段不生效。 - 当code_dir以file://为前缀时，当前字段不生效。 - 不支持配置成/home/ma-user/modelarts，/home/ma-user/modelarts-dev，/home/ma-user/infer以及它们底下的目录，也不支持配置成/home/ma-user  **取值范围**：不涉及。 **默认取值**：不涉及。

        :param local_code_dir: The local_code_dir of this JobAlgorithm.
        :type local_code_dir: str
        """
        self._local_code_dir = local_code_dir

    @property
    def working_dir(self):
        r"""Gets the working_dir of this JobAlgorithm.

        **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The working_dir of this JobAlgorithm.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this JobAlgorithm.

        **参数解释**：运行算法时所在的工作目录。 **约束限制**：v1兼容模式下，当前字段不生效。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param working_dir: The working_dir of this JobAlgorithm.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def environments(self):
        r"""Gets the environments of this JobAlgorithm.

        **参数解释**：训练作业的环境变量。格式：\"key\":\"value\"。 **约束限制**：其中key最大允许填写8192字符，value最大允许填写4096字符，最多允许100对环境变量。变量名应该仅包含字母、数字、下划线，且以字母或下划线开头。 注：不支持使用符号 $ 引用变量。

        :return: The environments of this JobAlgorithm.
        :rtype: dict(str, str)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this JobAlgorithm.

        **参数解释**：训练作业的环境变量。格式：\"key\":\"value\"。 **约束限制**：其中key最大允许填写8192字符，value最大允许填写4096字符，最多允许100对环境变量。变量名应该仅包含字母、数字、下划线，且以字母或下划线开头。 注：不支持使用符号 $ 引用变量。

        :param environments: The environments of this JobAlgorithm.
        :type environments: dict(str, str)
        """
        self._environments = environments

    @property
    def summary(self):
        r"""Gets the summary of this JobAlgorithm.

        :return: The summary of this JobAlgorithm.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Summary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this JobAlgorithm.

        :param summary: The summary of this JobAlgorithm.
        :type summary: :class:`huaweicloudsdkmodelarts.v1.Summary`
        """
        self._summary = summary

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
        if not isinstance(other, JobAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
