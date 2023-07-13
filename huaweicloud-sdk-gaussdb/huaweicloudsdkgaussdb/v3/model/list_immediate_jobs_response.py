# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImmediateJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[TaskDetailInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'total_count': 'total_count'
    }

    def __init__(self, jobs=None, total_count=None):
        """ListImmediateJobsResponse

        The model defined in huaweicloud sdk

        :param jobs: 任务详情。
        :type jobs: list[:class:`huaweicloudsdkgaussdb.v3.TaskDetailInfo`]
        :param total_count: 任务总数。
        :type total_count: int
        """
        
        super(ListImmediateJobsResponse, self).__init__()

        self._jobs = None
        self._total_count = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if total_count is not None:
            self.total_count = total_count

    @property
    def jobs(self):
        """Gets the jobs of this ListImmediateJobsResponse.

        任务详情。

        :return: The jobs of this ListImmediateJobsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.TaskDetailInfo`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListImmediateJobsResponse.

        任务详情。

        :param jobs: The jobs of this ListImmediateJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkgaussdb.v3.TaskDetailInfo`]
        """
        self._jobs = jobs

    @property
    def total_count(self):
        """Gets the total_count of this ListImmediateJobsResponse.

        任务总数。

        :return: The total_count of this ListImmediateJobsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListImmediateJobsResponse.

        任务总数。

        :param total_count: The total_count of this ListImmediateJobsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListImmediateJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
