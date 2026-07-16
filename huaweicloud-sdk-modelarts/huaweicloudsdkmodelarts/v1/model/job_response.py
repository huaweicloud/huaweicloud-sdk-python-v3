# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResponse:

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
        'metadata': 'JobMetadataResponse',
        'status': 'Status',
        'algorithm': 'JobAlgorithmResponse',
        'tasks': 'list[TaskResponse]',
        'spec': 'SpecResponse',
        'endpoints': 'JobEndpointsResp',
        'ftjob_config': 'MasJobConfig'
    }

    attribute_map = {
        'kind': 'kind',
        'metadata': 'metadata',
        'status': 'status',
        'algorithm': 'algorithm',
        'tasks': 'tasks',
        'spec': 'spec',
        'endpoints': 'endpoints',
        'ftjob_config': 'ftjob_config'
    }

    def __init__(self, kind=None, metadata=None, status=None, algorithm=None, tasks=None, spec=None, endpoints=None, ftjob_config=None):
        r"""JobResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释**：训练作业类型。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.Status`
        :param algorithm: 
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponse`
        :param tasks: **参数解释**：异构训练作业的任务列表。
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.TaskResponse`]
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        :param endpoints: 
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsResp`
        :param ftjob_config: 
        :type ftjob_config: :class:`huaweicloudsdkmodelarts.v1.MasJobConfig`
        """
        
        

        self._kind = None
        self._metadata = None
        self._status = None
        self._algorithm = None
        self._tasks = None
        self._spec = None
        self._endpoints = None
        self._ftjob_config = None
        self.discriminator = None

        self.kind = kind
        self.metadata = metadata
        if status is not None:
            self.status = status
        if algorithm is not None:
            self.algorithm = algorithm
        if tasks is not None:
            self.tasks = tasks
        if spec is not None:
            self.spec = spec
        if endpoints is not None:
            self.endpoints = endpoints
        if ftjob_config is not None:
            self.ftjob_config = ftjob_config

    @property
    def kind(self):
        r"""Gets the kind of this JobResponse.

        **参数解释**：训练作业类型。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业

        :return: The kind of this JobResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this JobResponse.

        **参数解释**：训练作业类型。 **取值范围**： - job：普通作业 - federated_pool_job：资源池联邦作业 - edge_job：边缘作业 - hetero_job：异构作业 - mrs_job：MRS作业 - autosearch_job：自动化搜索作业 - diag_job：诊断作业 - visualization_job：可视化作业

        :param kind: The kind of this JobResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this JobResponse.

        :return: The metadata of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this JobResponse.

        :param metadata: The metadata of this JobResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobMetadataResponse`
        """
        self._metadata = metadata

    @property
    def status(self):
        r"""Gets the status of this JobResponse.

        :return: The status of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobResponse.

        :param status: The status of this JobResponse.
        :type status: :class:`huaweicloudsdkmodelarts.v1.Status`
        """
        self._status = status

    @property
    def algorithm(self):
        r"""Gets the algorithm of this JobResponse.

        :return: The algorithm of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponse`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this JobResponse.

        :param algorithm: The algorithm of this JobResponse.
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponse`
        """
        self._algorithm = algorithm

    @property
    def tasks(self):
        r"""Gets the tasks of this JobResponse.

        **参数解释**：异构训练作业的任务列表。

        :return: The tasks of this JobResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TaskResponse`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this JobResponse.

        **参数解释**：异构训练作业的任务列表。

        :param tasks: The tasks of this JobResponse.
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.TaskResponse`]
        """
        self._tasks = tasks

    @property
    def spec(self):
        r"""Gets the spec of this JobResponse.

        :return: The spec of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this JobResponse.

        :param spec: The spec of this JobResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.SpecResponse`
        """
        self._spec = spec

    @property
    def endpoints(self):
        r"""Gets the endpoints of this JobResponse.

        :return: The endpoints of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsResp`
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this JobResponse.

        :param endpoints: The endpoints of this JobResponse.
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsResp`
        """
        self._endpoints = endpoints

    @property
    def ftjob_config(self):
        r"""Gets the ftjob_config of this JobResponse.

        :return: The ftjob_config of this JobResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MasJobConfig`
        """
        return self._ftjob_config

    @ftjob_config.setter
    def ftjob_config(self, ftjob_config):
        r"""Sets the ftjob_config of this JobResponse.

        :param ftjob_config: The ftjob_config of this JobResponse.
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
        if not isinstance(other, JobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
