# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataframeJobConfig:

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
        'job_config': 'ResourceConfig',
        'runtime_env': 'JobRuntimeEnv'
    }

    attribute_map = {
        'entrypoint': 'entrypoint',
        'job_config': 'job_config',
        'runtime_env': 'runtime_env'
    }

    def __init__(self, entrypoint=None, job_config=None, runtime_env=None):
        r"""DataframeJobConfig

        The model defined in huaweicloud sdk

        :param entrypoint: **参数解释**：运行作业主脚本。  **约束限制**：不涉及。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。
        :type entrypoint: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.ResourceConfig`
        :param runtime_env: 
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.JobRuntimeEnv`
        """
        
        

        self._entrypoint = None
        self._job_config = None
        self._runtime_env = None
        self.discriminator = None

        self.entrypoint = entrypoint
        if job_config is not None:
            self.job_config = job_config
        if runtime_env is not None:
            self.runtime_env = runtime_env

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this DataframeJobConfig.

        **参数解释**：运行作业主脚本。  **约束限制**：不涉及。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。

        :return: The entrypoint of this DataframeJobConfig.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this DataframeJobConfig.

        **参数解释**：运行作业主脚本。  **约束限制**：不涉及。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。

        :param entrypoint: The entrypoint of this DataframeJobConfig.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def job_config(self):
        r"""Gets the job_config of this DataframeJobConfig.

        :return: The job_config of this DataframeJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ResourceConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this DataframeJobConfig.

        :param job_config: The job_config of this DataframeJobConfig.
        :type job_config: :class:`huaweicloudsdkaidatalake.v2.ResourceConfig`
        """
        self._job_config = job_config

    @property
    def runtime_env(self):
        r"""Gets the runtime_env of this DataframeJobConfig.

        :return: The runtime_env of this DataframeJobConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.JobRuntimeEnv`
        """
        return self._runtime_env

    @runtime_env.setter
    def runtime_env(self, runtime_env):
        r"""Sets the runtime_env of this DataframeJobConfig.

        :param runtime_env: The runtime_env of this DataframeJobConfig.
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.JobRuntimeEnv`
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
        if not isinstance(other, DataframeJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
