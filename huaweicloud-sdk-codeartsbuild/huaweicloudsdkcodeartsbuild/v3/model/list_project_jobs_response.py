# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[Job]',
        'total': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'total': 'total'
    }

    def __init__(self, jobs=None, total=None):
        r"""ListProjectJobsResponse

        The model defined in huaweicloud sdk

        :param jobs: 任务列表
        :type jobs: list[:class:`huaweicloudsdkcodeartsbuild.v3.Job`]
        :param total: 任务总数
        :type total: int
        """
        
        super(ListProjectJobsResponse, self).__init__()

        self._jobs = None
        self._total = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if total is not None:
            self.total = total

    @property
    def jobs(self):
        r"""Gets the jobs of this ListProjectJobsResponse.

        任务列表

        :return: The jobs of this ListProjectJobsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListProjectJobsResponse.

        任务列表

        :param jobs: The jobs of this ListProjectJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkcodeartsbuild.v3.Job`]
        """
        self._jobs = jobs

    @property
    def total(self):
        r"""Gets the total of this ListProjectJobsResponse.

        任务总数

        :return: The total of this ListProjectJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListProjectJobsResponse.

        任务总数

        :param total: The total of this ListProjectJobsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListProjectJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
