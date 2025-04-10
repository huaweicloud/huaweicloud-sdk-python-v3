# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataLevelTableCompareJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_jobs': 'list[CompareJobInfo]',
        'count': 'int'
    }

    attribute_map = {
        'compare_jobs': 'compare_jobs',
        'count': 'count'
    }

    def __init__(self, compare_jobs=None, count=None):
        r"""ListDataLevelTableCompareJobsResponse

        The model defined in huaweicloud sdk

        :param compare_jobs: 表对比任务信息
        :type compare_jobs: list[:class:`huaweicloudsdkdrs.v3.CompareJobInfo`]
        :param count: 任务数量
        :type count: int
        """
        
        super(ListDataLevelTableCompareJobsResponse, self).__init__()

        self._compare_jobs = None
        self._count = None
        self.discriminator = None

        if compare_jobs is not None:
            self.compare_jobs = compare_jobs
        if count is not None:
            self.count = count

    @property
    def compare_jobs(self):
        r"""Gets the compare_jobs of this ListDataLevelTableCompareJobsResponse.

        表对比任务信息

        :return: The compare_jobs of this ListDataLevelTableCompareJobsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareJobInfo`]
        """
        return self._compare_jobs

    @compare_jobs.setter
    def compare_jobs(self, compare_jobs):
        r"""Sets the compare_jobs of this ListDataLevelTableCompareJobsResponse.

        表对比任务信息

        :param compare_jobs: The compare_jobs of this ListDataLevelTableCompareJobsResponse.
        :type compare_jobs: list[:class:`huaweicloudsdkdrs.v3.CompareJobInfo`]
        """
        self._compare_jobs = compare_jobs

    @property
    def count(self):
        r"""Gets the count of this ListDataLevelTableCompareJobsResponse.

        任务数量

        :return: The count of this ListDataLevelTableCompareJobsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDataLevelTableCompareJobsResponse.

        任务数量

        :param count: The count of this ListDataLevelTableCompareJobsResponse.
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
        if not isinstance(other, ListDataLevelTableCompareJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
