# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'metadata': 'JobMetadata',
        'algorithm': 'JobAlgorithm',
        'tasks': 'list[Task]',
        'spec': 'Spec',
        'endpoints': 'JobEndpointsReq',
        'train_type': 'str',
        'ftjob_config': 'MasJobConfig'
    }

    attribute_map = {
        'kind': 'kind',
        'metadata': 'metadata',
        'algorithm': 'algorithm',
        'tasks': 'tasks',
        'spec': 'spec',
        'endpoints': 'endpoints',
        'train_type': 'train_type',
        'ftjob_config': 'ftjob_config'
    }

    def __init__(self, kind=None, metadata=None, algorithm=None, tasks=None, spec=None, endpoints=None, train_type=None, ftjob_config=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param kind: **参数解释**：训练作业类型。 **约束限制**：不涉及。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业  **默认取值**：job。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadata`
        :param algorithm: 
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithm`
        :param tasks: **参数解释**：任务列表。该功能暂未实现。 **约束限制**：不涉及。
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.Task`]
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.Spec`
        :param endpoints: 
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        :param train_type: **参数解释**：类型。 **约束限制**：不涉及。 **取值范围**：SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）
        :type train_type: str
        :param ftjob_config: 
        :type ftjob_config: :class:`huaweicloudsdkmodelarts.v1.MasJobConfig`
        """
        
        

        self._kind = None
        self._metadata = None
        self._algorithm = None
        self._tasks = None
        self._spec = None
        self._endpoints = None
        self._train_type = None
        self._ftjob_config = None
        self.discriminator = None

        self.kind = kind
        self.metadata = metadata
        if algorithm is not None:
            self.algorithm = algorithm
        if tasks is not None:
            self.tasks = tasks
        if spec is not None:
            self.spec = spec
        if endpoints is not None:
            self.endpoints = endpoints
        if train_type is not None:
            self.train_type = train_type
        if ftjob_config is not None:
            self.ftjob_config = ftjob_config

    @property
    def kind(self):
        r"""Gets the kind of this Job.

        **参数解释**：训练作业类型。 **约束限制**：不涉及。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业  **默认取值**：job。

        :return: The kind of this Job.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this Job.

        **参数解释**：训练作业类型。 **约束限制**：不涉及。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业  **默认取值**：job。

        :param kind: The kind of this Job.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this Job.

        :return: The metadata of this Job.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Job.

        :param metadata: The metadata of this Job.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadata`
        """
        self._metadata = metadata

    @property
    def algorithm(self):
        r"""Gets the algorithm of this Job.

        :return: The algorithm of this Job.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithm`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this Job.

        :param algorithm: The algorithm of this Job.
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithm`
        """
        self._algorithm = algorithm

    @property
    def tasks(self):
        r"""Gets the tasks of this Job.

        **参数解释**：任务列表。该功能暂未实现。 **约束限制**：不涉及。

        :return: The tasks of this Job.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this Job.

        **参数解释**：任务列表。该功能暂未实现。 **约束限制**：不涉及。

        :param tasks: The tasks of this Job.
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.Task`]
        """
        self._tasks = tasks

    @property
    def spec(self):
        r"""Gets the spec of this Job.

        :return: The spec of this Job.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Spec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this Job.

        :param spec: The spec of this Job.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.Spec`
        """
        self._spec = spec

    @property
    def endpoints(self):
        r"""Gets the endpoints of this Job.

        :return: The endpoints of this Job.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this Job.

        :param endpoints: The endpoints of this Job.
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        """
        self._endpoints = endpoints

    @property
    def train_type(self):
        r"""Gets the train_type of this Job.

        **参数解释**：类型。 **约束限制**：不涉及。 **取值范围**：SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）

        :return: The train_type of this Job.
        :rtype: str
        """
        return self._train_type

    @train_type.setter
    def train_type(self, train_type):
        r"""Sets the train_type of this Job.

        **参数解释**：类型。 **约束限制**：不涉及。 **取值范围**：SFT（全量微调）、PRETRAIN（预训练）、LORA（lora微调）、DPO（dpo强化学习）、RFT（rft强化学习）

        :param train_type: The train_type of this Job.
        :type train_type: str
        """
        self._train_type = train_type

    @property
    def ftjob_config(self):
        r"""Gets the ftjob_config of this Job.

        :return: The ftjob_config of this Job.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MasJobConfig`
        """
        return self._ftjob_config

    @ftjob_config.setter
    def ftjob_config(self, ftjob_config):
        r"""Sets the ftjob_config of this Job.

        :param ftjob_config: The ftjob_config of this Job.
        :type ftjob_config: :class:`huaweicloudsdkmodelarts.v1.MasJobConfig`
        """
        self._ftjob_config = ftjob_config

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
