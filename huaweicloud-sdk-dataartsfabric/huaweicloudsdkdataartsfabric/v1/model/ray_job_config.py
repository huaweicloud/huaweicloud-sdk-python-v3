# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entrypoint': 'str',
        'metadata': 'object',
        'entrypoint_num_cpus': 'float',
        'entrypoint_num_gpus': 'float',
        'entrypoint_memory': 'int',
        'entrypoint_resources': 'object',
        'submission_id': 'str',
        'runtime_env': 'RuntimeEnv'
    }

    attribute_map = {
        'entrypoint': 'entrypoint',
        'metadata': 'metadata',
        'entrypoint_num_cpus': 'entrypoint_num_cpus',
        'entrypoint_num_gpus': 'entrypoint_num_gpus',
        'entrypoint_memory': 'entrypoint_memory',
        'entrypoint_resources': 'entrypoint_resources',
        'submission_id': 'submission_id',
        'runtime_env': 'runtime_env'
    }

    def __init__(self, entrypoint=None, metadata=None, entrypoint_num_cpus=None, entrypoint_num_gpus=None, entrypoint_memory=None, entrypoint_resources=None, submission_id=None, runtime_env=None):
        r"""RayJobConfig

        The model defined in huaweicloud sdk

        :param entrypoint: 运行作业主脚本
        :type entrypoint: str
        :param metadata: 用户提供的元数据
        :type metadata: object
        :param entrypoint_num_cpus: 执行命令的CPU数量
        :type entrypoint_num_cpus: float
        :param entrypoint_num_gpus: 执行命令的GPU数量
        :type entrypoint_num_gpus: float
        :param entrypoint_memory: 执行命令的内存大小
        :type entrypoint_memory: int
        :param entrypoint_resources: 自定义资源数量
        :type entrypoint_resources: object
        :param submission_id: 为作业指定的可选submission_id。
        :type submission_id: str
        :param runtime_env: 
        :type runtime_env: :class:`huaweicloudsdkdataartsfabric.v1.RuntimeEnv`
        """
        
        

        self._entrypoint = None
        self._metadata = None
        self._entrypoint_num_cpus = None
        self._entrypoint_num_gpus = None
        self._entrypoint_memory = None
        self._entrypoint_resources = None
        self._submission_id = None
        self._runtime_env = None
        self.discriminator = None

        self.entrypoint = entrypoint
        if metadata is not None:
            self.metadata = metadata
        if entrypoint_num_cpus is not None:
            self.entrypoint_num_cpus = entrypoint_num_cpus
        if entrypoint_num_gpus is not None:
            self.entrypoint_num_gpus = entrypoint_num_gpus
        if entrypoint_memory is not None:
            self.entrypoint_memory = entrypoint_memory
        if entrypoint_resources is not None:
            self.entrypoint_resources = entrypoint_resources
        if submission_id is not None:
            self.submission_id = submission_id
        if runtime_env is not None:
            self.runtime_env = runtime_env

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this RayJobConfig.

        运行作业主脚本

        :return: The entrypoint of this RayJobConfig.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this RayJobConfig.

        运行作业主脚本

        :param entrypoint: The entrypoint of this RayJobConfig.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def metadata(self):
        r"""Gets the metadata of this RayJobConfig.

        用户提供的元数据

        :return: The metadata of this RayJobConfig.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RayJobConfig.

        用户提供的元数据

        :param metadata: The metadata of this RayJobConfig.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def entrypoint_num_cpus(self):
        r"""Gets the entrypoint_num_cpus of this RayJobConfig.

        执行命令的CPU数量

        :return: The entrypoint_num_cpus of this RayJobConfig.
        :rtype: float
        """
        return self._entrypoint_num_cpus

    @entrypoint_num_cpus.setter
    def entrypoint_num_cpus(self, entrypoint_num_cpus):
        r"""Sets the entrypoint_num_cpus of this RayJobConfig.

        执行命令的CPU数量

        :param entrypoint_num_cpus: The entrypoint_num_cpus of this RayJobConfig.
        :type entrypoint_num_cpus: float
        """
        self._entrypoint_num_cpus = entrypoint_num_cpus

    @property
    def entrypoint_num_gpus(self):
        r"""Gets the entrypoint_num_gpus of this RayJobConfig.

        执行命令的GPU数量

        :return: The entrypoint_num_gpus of this RayJobConfig.
        :rtype: float
        """
        return self._entrypoint_num_gpus

    @entrypoint_num_gpus.setter
    def entrypoint_num_gpus(self, entrypoint_num_gpus):
        r"""Sets the entrypoint_num_gpus of this RayJobConfig.

        执行命令的GPU数量

        :param entrypoint_num_gpus: The entrypoint_num_gpus of this RayJobConfig.
        :type entrypoint_num_gpus: float
        """
        self._entrypoint_num_gpus = entrypoint_num_gpus

    @property
    def entrypoint_memory(self):
        r"""Gets the entrypoint_memory of this RayJobConfig.

        执行命令的内存大小

        :return: The entrypoint_memory of this RayJobConfig.
        :rtype: int
        """
        return self._entrypoint_memory

    @entrypoint_memory.setter
    def entrypoint_memory(self, entrypoint_memory):
        r"""Sets the entrypoint_memory of this RayJobConfig.

        执行命令的内存大小

        :param entrypoint_memory: The entrypoint_memory of this RayJobConfig.
        :type entrypoint_memory: int
        """
        self._entrypoint_memory = entrypoint_memory

    @property
    def entrypoint_resources(self):
        r"""Gets the entrypoint_resources of this RayJobConfig.

        自定义资源数量

        :return: The entrypoint_resources of this RayJobConfig.
        :rtype: object
        """
        return self._entrypoint_resources

    @entrypoint_resources.setter
    def entrypoint_resources(self, entrypoint_resources):
        r"""Sets the entrypoint_resources of this RayJobConfig.

        自定义资源数量

        :param entrypoint_resources: The entrypoint_resources of this RayJobConfig.
        :type entrypoint_resources: object
        """
        self._entrypoint_resources = entrypoint_resources

    @property
    def submission_id(self):
        r"""Gets the submission_id of this RayJobConfig.

        为作业指定的可选submission_id。

        :return: The submission_id of this RayJobConfig.
        :rtype: str
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        r"""Sets the submission_id of this RayJobConfig.

        为作业指定的可选submission_id。

        :param submission_id: The submission_id of this RayJobConfig.
        :type submission_id: str
        """
        self._submission_id = submission_id

    @property
    def runtime_env(self):
        r"""Gets the runtime_env of this RayJobConfig.

        :return: The runtime_env of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RuntimeEnv`
        """
        return self._runtime_env

    @runtime_env.setter
    def runtime_env(self, runtime_env):
        r"""Sets the runtime_env of this RayJobConfig.

        :param runtime_env: The runtime_env of this RayJobConfig.
        :type runtime_env: :class:`huaweicloudsdkdataartsfabric.v1.RuntimeEnv`
        """
        self._runtime_env = runtime_env

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
        if not isinstance(other, RayJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
