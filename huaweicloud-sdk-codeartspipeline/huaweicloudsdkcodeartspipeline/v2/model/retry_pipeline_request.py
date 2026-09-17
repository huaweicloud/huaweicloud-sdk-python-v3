# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryPipelineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_https_url': 'str',
        'job_run_ids': 'list[str]'
    }

    attribute_map = {
        'repo_https_url': 'repo_https_url',
        'job_run_ids': 'job_run_ids'
    }

    def __init__(self, repo_https_url=None, job_run_ids=None):
        r"""RetryPipelineRequest

        The model defined in huaweicloud sdk

        :param repo_https_url: **参数解释**： 仓库HTTPS地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type repo_https_url: str
        :param job_run_ids: **参数解释**： 流水线任务运行ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type job_run_ids: list[str]
        """
        
        

        self._repo_https_url = None
        self._job_run_ids = None
        self.discriminator = None

        if repo_https_url is not None:
            self.repo_https_url = repo_https_url
        if job_run_ids is not None:
            self.job_run_ids = job_run_ids

    @property
    def repo_https_url(self):
        r"""Gets the repo_https_url of this RetryPipelineRequest.

        **参数解释**： 仓库HTTPS地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The repo_https_url of this RetryPipelineRequest.
        :rtype: str
        """
        return self._repo_https_url

    @repo_https_url.setter
    def repo_https_url(self, repo_https_url):
        r"""Sets the repo_https_url of this RetryPipelineRequest.

        **参数解释**： 仓库HTTPS地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param repo_https_url: The repo_https_url of this RetryPipelineRequest.
        :type repo_https_url: str
        """
        self._repo_https_url = repo_https_url

    @property
    def job_run_ids(self):
        r"""Gets the job_run_ids of this RetryPipelineRequest.

        **参数解释**： 流水线任务运行ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The job_run_ids of this RetryPipelineRequest.
        :rtype: list[str]
        """
        return self._job_run_ids

    @job_run_ids.setter
    def job_run_ids(self, job_run_ids):
        r"""Sets the job_run_ids of this RetryPipelineRequest.

        **参数解释**： 流水线任务运行ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param job_run_ids: The job_run_ids of this RetryPipelineRequest.
        :type job_run_ids: list[str]
        """
        self._job_run_ids = job_run_ids

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
        if not isinstance(other, RetryPipelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
