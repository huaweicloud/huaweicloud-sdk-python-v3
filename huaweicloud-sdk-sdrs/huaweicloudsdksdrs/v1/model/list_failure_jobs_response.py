# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFailureJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failure_jobs': 'list[FailureJobParams]',
        'count': 'int'
    }

    attribute_map = {
        'failure_jobs': 'failure_jobs',
        'count': 'count'
    }

    def __init__(self, failure_jobs=None, count=None):
        """ListFailureJobsResponse

        The model defined in huaweicloud sdk

        :param failure_jobs: 失败任务信息列表。
        :type failure_jobs: list[:class:`huaweicloudsdksdrs.v1.FailureJobParams`]
        :param count: 列表中失败任务个数。
        :type count: int
        """
        
        super(ListFailureJobsResponse, self).__init__()

        self._failure_jobs = None
        self._count = None
        self.discriminator = None

        if failure_jobs is not None:
            self.failure_jobs = failure_jobs
        if count is not None:
            self.count = count

    @property
    def failure_jobs(self):
        """Gets the failure_jobs of this ListFailureJobsResponse.

        失败任务信息列表。

        :return: The failure_jobs of this ListFailureJobsResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.FailureJobParams`]
        """
        return self._failure_jobs

    @failure_jobs.setter
    def failure_jobs(self, failure_jobs):
        """Sets the failure_jobs of this ListFailureJobsResponse.

        失败任务信息列表。

        :param failure_jobs: The failure_jobs of this ListFailureJobsResponse.
        :type failure_jobs: list[:class:`huaweicloudsdksdrs.v1.FailureJobParams`]
        """
        self._failure_jobs = failure_jobs

    @property
    def count(self):
        """Gets the count of this ListFailureJobsResponse.

        列表中失败任务个数。

        :return: The count of this ListFailureJobsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFailureJobsResponse.

        列表中失败任务个数。

        :param count: The count of this ListFailureJobsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListFailureJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
