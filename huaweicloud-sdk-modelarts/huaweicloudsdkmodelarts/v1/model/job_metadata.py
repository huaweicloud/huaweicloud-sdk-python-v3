# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'workspace_id': 'str',
        'description': 'str',
        'annotations': 'dict(str, str)',
        'training_experiment_reference': 'TrainingExperimentRequest'
    }

    attribute_map = {
        'name': 'name',
        'workspace_id': 'workspace_id',
        'description': 'description',
        'annotations': 'annotations',
        'training_experiment_reference': 'training_experiment_reference'
    }

    def __init__(self, name=None, workspace_id=None, description=None, annotations=None, training_experiment_reference=None):
        r"""JobMetadata

        The model defined in huaweicloud sdk

        :param name: 训练作业名称。限制为1-64位只含数字、字母、下划线和中划线的名称。
        :type name: str
        :param workspace_id: 指定作业所处的工作空间，默认值为“0”。
        :type workspace_id: str
        :param description: 对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。
        :type description: str
        :param annotations: 训练作业高级功能配置，可选取值如下： - \&quot;job_template\&quot;: \&quot;Template RL\&quot;（异构作业）。 - \&quot;fault-tolerance/job-retry-num\&quot;: \&quot;3\&quot;（故障自动重启次数）。 - \&quot;jupyter-lab/enable\&quot;: \&quot;true\&quot;（JupyterLab训练应用程序）
        :type annotations: dict(str, str)
        :param training_experiment_reference: 
        :type training_experiment_reference: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentRequest`
        """
        
        

        self._name = None
        self._workspace_id = None
        self._description = None
        self._annotations = None
        self._training_experiment_reference = None
        self.discriminator = None

        self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if description is not None:
            self.description = description
        if annotations is not None:
            self.annotations = annotations
        if training_experiment_reference is not None:
            self.training_experiment_reference = training_experiment_reference

    @property
    def name(self):
        r"""Gets the name of this JobMetadata.

        训练作业名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :return: The name of this JobMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobMetadata.

        训练作业名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :param name: The name of this JobMetadata.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this JobMetadata.

        指定作业所处的工作空间，默认值为“0”。

        :return: The workspace_id of this JobMetadata.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this JobMetadata.

        指定作业所处的工作空间，默认值为“0”。

        :param workspace_id: The workspace_id of this JobMetadata.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def description(self):
        r"""Gets the description of this JobMetadata.

        对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :return: The description of this JobMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobMetadata.

        对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :param description: The description of this JobMetadata.
        :type description: str
        """
        self._description = description

    @property
    def annotations(self):
        r"""Gets the annotations of this JobMetadata.

        训练作业高级功能配置，可选取值如下： - \"job_template\": \"Template RL\"（异构作业）。 - \"fault-tolerance/job-retry-num\": \"3\"（故障自动重启次数）。 - \"jupyter-lab/enable\": \"true\"（JupyterLab训练应用程序）

        :return: The annotations of this JobMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this JobMetadata.

        训练作业高级功能配置，可选取值如下： - \"job_template\": \"Template RL\"（异构作业）。 - \"fault-tolerance/job-retry-num\": \"3\"（故障自动重启次数）。 - \"jupyter-lab/enable\": \"true\"（JupyterLab训练应用程序）

        :param annotations: The annotations of this JobMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def training_experiment_reference(self):
        r"""Gets the training_experiment_reference of this JobMetadata.

        :return: The training_experiment_reference of this JobMetadata.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentRequest`
        """
        return self._training_experiment_reference

    @training_experiment_reference.setter
    def training_experiment_reference(self, training_experiment_reference):
        r"""Sets the training_experiment_reference of this JobMetadata.

        :param training_experiment_reference: The training_experiment_reference of this JobMetadata.
        :type training_experiment_reference: :class:`huaweicloudsdkmodelarts.v1.TrainingExperimentRequest`
        """
        self._training_experiment_reference = training_experiment_reference

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
        if not isinstance(other, JobMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
