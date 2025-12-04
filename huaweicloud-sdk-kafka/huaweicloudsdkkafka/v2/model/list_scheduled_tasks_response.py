# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_count': 'str',
        'jobs': 'list[ScheduledTaskEntity]'
    }

    attribute_map = {
        'job_count': 'job_count',
        'jobs': 'jobs'
    }

    def __init__(self, job_count=None, jobs=None):
        r"""ListScheduledTasksResponse

        The model defined in huaweicloud sdk

        :param job_count: **参数解释**： 任务总数。 **取值范围**： 不涉及。
        :type job_count: str
        :param jobs: **参数解释**： 任务列表。
        :type jobs: list[:class:`huaweicloudsdkkafka.v2.ScheduledTaskEntity`]
        """
        
        super().__init__()

        self._job_count = None
        self._jobs = None
        self.discriminator = None

        if job_count is not None:
            self.job_count = job_count
        if jobs is not None:
            self.jobs = jobs

    @property
    def job_count(self):
        r"""Gets the job_count of this ListScheduledTasksResponse.

        **参数解释**： 任务总数。 **取值范围**： 不涉及。

        :return: The job_count of this ListScheduledTasksResponse.
        :rtype: str
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        r"""Sets the job_count of this ListScheduledTasksResponse.

        **参数解释**： 任务总数。 **取值范围**： 不涉及。

        :param job_count: The job_count of this ListScheduledTasksResponse.
        :type job_count: str
        """
        self._job_count = job_count

    @property
    def jobs(self):
        r"""Gets the jobs of this ListScheduledTasksResponse.

        **参数解释**： 任务列表。

        :return: The jobs of this ListScheduledTasksResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ScheduledTaskEntity`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListScheduledTasksResponse.

        **参数解释**： 任务列表。

        :param jobs: The jobs of this ListScheduledTasksResponse.
        :type jobs: list[:class:`huaweicloudsdkkafka.v2.ScheduledTaskEntity`]
        """
        self._jobs = jobs

    def to_dict(self):
        import warnings
        warnings.warn("ListScheduledTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListScheduledTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
