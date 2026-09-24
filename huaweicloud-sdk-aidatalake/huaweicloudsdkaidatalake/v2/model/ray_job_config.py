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
        'job_config': 'InnerRayJobConfig',
        'runtime_env': 'RuntimeEnv',
        'image': 'V2ImageBriefInfo',
        'resource_config': 'RayResourceConfig',
        'rayjob_strategy': 'RayJobStrategy',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'entrypoint': 'entrypoint',
        'job_config': 'job_config',
        'runtime_env': 'runtime_env',
        'image': 'image',
        'resource_config': 'resource_config',
        'rayjob_strategy': 'rayjob_strategy',
        'metadata': 'metadata'
    }

    def __init__(self, entrypoint=None, job_config=None, runtime_env=None, image=None, resource_config=None, rayjob_strategy=None, metadata=None):
        r"""RayJobConfig

        The model defined in huaweicloud sdk

        :param entrypoint: **参数解释**：运行作业主脚本。 **约束限制**：不涉及。 **取值范围**：长度为1~102400个字符。 **默认取值**：不涉及。
        :type entrypoint: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.InnerRayJobConfig`
        :param runtime_env: 
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.RuntimeEnv`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfo`
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.RayResourceConfig`
        :param rayjob_strategy: 
        :type rayjob_strategy: :class:`huaweicloudsdkaidatalake.v2.RayJobStrategy`
        :param metadata: **参数解释**：用户自定义作业元数据（键值对）。 **约束限制**：键值对数量为0~255个。key和value的值不能为空，长度不超过255个字符 。
        :type metadata: dict(str, str)
        """
        
        

        self._entrypoint = None
        self._job_config = None
        self._runtime_env = None
        self._image = None
        self._resource_config = None
        self._rayjob_strategy = None
        self._metadata = None
        self.discriminator = None

        self.entrypoint = entrypoint
        if job_config is not None:
            self.job_config = job_config
        if runtime_env is not None:
            self.runtime_env = runtime_env
        if image is not None:
            self.image = image
        if resource_config is not None:
            self.resource_config = resource_config
        if rayjob_strategy is not None:
            self.rayjob_strategy = rayjob_strategy
        if metadata is not None:
            self.metadata = metadata

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this RayJobConfig.

        **参数解释**：运行作业主脚本。 **约束限制**：不涉及。 **取值范围**：长度为1~102400个字符。 **默认取值**：不涉及。

        :return: The entrypoint of this RayJobConfig.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this RayJobConfig.

        **参数解释**：运行作业主脚本。 **约束限制**：不涉及。 **取值范围**：长度为1~102400个字符。 **默认取值**：不涉及。

        :param entrypoint: The entrypoint of this RayJobConfig.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def job_config(self):
        r"""Gets the job_config of this RayJobConfig.

        :return: The job_config of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.InnerRayJobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this RayJobConfig.

        :param job_config: The job_config of this RayJobConfig.
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.InnerRayJobConfig`
        """
        self._job_config = job_config

    @property
    def runtime_env(self):
        r"""Gets the runtime_env of this RayJobConfig.

        :return: The runtime_env of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RuntimeEnv`
        """
        return self._runtime_env

    @runtime_env.setter
    def runtime_env(self, runtime_env):
        r"""Sets the runtime_env of this RayJobConfig.

        :param runtime_env: The runtime_env of this RayJobConfig.
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.RuntimeEnv`
        """
        self._runtime_env = runtime_env

    @property
    def image(self):
        r"""Gets the image of this RayJobConfig.

        :return: The image of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfo`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this RayJobConfig.

        :param image: The image of this RayJobConfig.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfo`
        """
        self._image = image

    @property
    def resource_config(self):
        r"""Gets the resource_config of this RayJobConfig.

        :return: The resource_config of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this RayJobConfig.

        :param resource_config: The resource_config of this RayJobConfig.
        :type resource_config: :class:`huaweicloudsdkaidatalake.v2.RayResourceConfig`
        """
        self._resource_config = resource_config

    @property
    def rayjob_strategy(self):
        r"""Gets the rayjob_strategy of this RayJobConfig.

        :return: The rayjob_strategy of this RayJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayJobStrategy`
        """
        return self._rayjob_strategy

    @rayjob_strategy.setter
    def rayjob_strategy(self, rayjob_strategy):
        r"""Sets the rayjob_strategy of this RayJobConfig.

        :param rayjob_strategy: The rayjob_strategy of this RayJobConfig.
        :type rayjob_strategy: :class:`huaweicloudsdkaidatalake.v2.RayJobStrategy`
        """
        self._rayjob_strategy = rayjob_strategy

    @property
    def metadata(self):
        r"""Gets the metadata of this RayJobConfig.

        **参数解释**：用户自定义作业元数据（键值对）。 **约束限制**：键值对数量为0~255个。key和value的值不能为空，长度不超过255个字符 。

        :return: The metadata of this RayJobConfig.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RayJobConfig.

        **参数解释**：用户自定义作业元数据（键值对）。 **约束限制**：键值对数量为0~255个。key和value的值不能为空，长度不超过255个字符 。

        :param metadata: The metadata of this RayJobConfig.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

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
