# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[JobListDto]',
        'count': 'int',
        'running_count': 'int',
        'waiting_count': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'count': 'count',
        'running_count': 'running_count',
        'waiting_count': 'waiting_count'
    }

    def __init__(self, jobs=None, count=None, running_count=None, waiting_count=None):
        r"""ListUserJobResponse

        The model defined in huaweicloud sdk

        :param jobs: 作业列表。
        :type jobs: list[:class:`huaweicloudsdkeihealth.v1.JobListDto`]
        :param count: 作业总数。
        :type count: int
        :param running_count: 运行中作业总数。
        :type running_count: int
        :param waiting_count: 等待中作业总数。
        :type waiting_count: int
        """
        
        super(ListUserJobResponse, self).__init__()

        self._jobs = None
        self._count = None
        self._running_count = None
        self._waiting_count = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if count is not None:
            self.count = count
        if running_count is not None:
            self.running_count = running_count
        if waiting_count is not None:
            self.waiting_count = waiting_count

    @property
    def jobs(self):
        r"""Gets the jobs of this ListUserJobResponse.

        作业列表。

        :return: The jobs of this ListUserJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.JobListDto`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListUserJobResponse.

        作业列表。

        :param jobs: The jobs of this ListUserJobResponse.
        :type jobs: list[:class:`huaweicloudsdkeihealth.v1.JobListDto`]
        """
        self._jobs = jobs

    @property
    def count(self):
        r"""Gets the count of this ListUserJobResponse.

        作业总数。

        :return: The count of this ListUserJobResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListUserJobResponse.

        作业总数。

        :param count: The count of this ListUserJobResponse.
        :type count: int
        """
        self._count = count

    @property
    def running_count(self):
        r"""Gets the running_count of this ListUserJobResponse.

        运行中作业总数。

        :return: The running_count of this ListUserJobResponse.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        r"""Sets the running_count of this ListUserJobResponse.

        运行中作业总数。

        :param running_count: The running_count of this ListUserJobResponse.
        :type running_count: int
        """
        self._running_count = running_count

    @property
    def waiting_count(self):
        r"""Gets the waiting_count of this ListUserJobResponse.

        等待中作业总数。

        :return: The waiting_count of this ListUserJobResponse.
        :rtype: int
        """
        return self._waiting_count

    @waiting_count.setter
    def waiting_count(self, waiting_count):
        r"""Sets the waiting_count of this ListUserJobResponse.

        等待中作业总数。

        :param waiting_count: The waiting_count of this ListUserJobResponse.
        :type waiting_count: int
        """
        self._waiting_count = waiting_count

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
        if not isinstance(other, ListUserJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
