# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAlgorithmResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'AlgorithmResponseMetadata',
        'job_config': 'AlgorithmResponseJobConfig',
        'resource_requirements': 'list[AlgorithmResponseResourceRequirements]',
        'advanced_config': 'AlgorithmResponseAdvancedConfig'
    }

    attribute_map = {
        'metadata': 'metadata',
        'job_config': 'job_config',
        'resource_requirements': 'resource_requirements',
        'advanced_config': 'advanced_config'
    }

    def __init__(self, metadata=None, job_config=None, resource_requirements=None, advanced_config=None):
        r"""ChangeAlgorithmResponse

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseMetadata`
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfig`
        :param resource_requirements: 算法资源约束，可不设置。设置后，在算法使用于训练作业时，控制台会过滤可用的公共资源池。
        :type resource_requirements: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseResourceRequirements`]
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseAdvancedConfig`
        """
        
        super().__init__()

        self._metadata = None
        self._job_config = None
        self._resource_requirements = None
        self._advanced_config = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if job_config is not None:
            self.job_config = job_config
        if resource_requirements is not None:
            self.resource_requirements = resource_requirements
        if advanced_config is not None:
            self.advanced_config = advanced_config

    @property
    def metadata(self):
        r"""Gets the metadata of this ChangeAlgorithmResponse.

        :return: The metadata of this ChangeAlgorithmResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ChangeAlgorithmResponse.

        :param metadata: The metadata of this ChangeAlgorithmResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseMetadata`
        """
        self._metadata = metadata

    @property
    def job_config(self):
        r"""Gets the job_config of this ChangeAlgorithmResponse.

        :return: The job_config of this ChangeAlgorithmResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this ChangeAlgorithmResponse.

        :param job_config: The job_config of this ChangeAlgorithmResponse.
        :type job_config: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfig`
        """
        self._job_config = job_config

    @property
    def resource_requirements(self):
        r"""Gets the resource_requirements of this ChangeAlgorithmResponse.

        算法资源约束，可不设置。设置后，在算法使用于训练作业时，控制台会过滤可用的公共资源池。

        :return: The resource_requirements of this ChangeAlgorithmResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseResourceRequirements`]
        """
        return self._resource_requirements

    @resource_requirements.setter
    def resource_requirements(self, resource_requirements):
        r"""Sets the resource_requirements of this ChangeAlgorithmResponse.

        算法资源约束，可不设置。设置后，在算法使用于训练作业时，控制台会过滤可用的公共资源池。

        :param resource_requirements: The resource_requirements of this ChangeAlgorithmResponse.
        :type resource_requirements: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseResourceRequirements`]
        """
        self._resource_requirements = resource_requirements

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this ChangeAlgorithmResponse.

        :return: The advanced_config of this ChangeAlgorithmResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseAdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this ChangeAlgorithmResponse.

        :param advanced_config: The advanced_config of this ChangeAlgorithmResponse.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseAdvancedConfig`
        """
        self._advanced_config = advanced_config

    def to_dict(self):
        import warnings
        warnings.warn("ChangeAlgorithmResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ChangeAlgorithmResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
