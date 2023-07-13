# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAsyncJobDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'jobs': 'list[JobDetailResp]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'jobs': 'jobs'
    }

    def __init__(self, total_count=None, jobs=None):
        """ListAsyncJobDetailResponse

        The model defined in huaweicloud sdk

        :param total_count: 列表中的项目总数，与分页无关。
        :type total_count: int
        :param jobs: 查询租户指定ID批量异步任务详情响应体。
        :type jobs: list[:class:`huaweicloudsdkdrs.v5.JobDetailResp`]
        """
        
        super(ListAsyncJobDetailResponse, self).__init__()

        self._total_count = None
        self._jobs = None
        self.discriminator = None

        self.total_count = total_count
        self.jobs = jobs

    @property
    def total_count(self):
        """Gets the total_count of this ListAsyncJobDetailResponse.

        列表中的项目总数，与分页无关。

        :return: The total_count of this ListAsyncJobDetailResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListAsyncJobDetailResponse.

        列表中的项目总数，与分页无关。

        :param total_count: The total_count of this ListAsyncJobDetailResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def jobs(self):
        """Gets the jobs of this ListAsyncJobDetailResponse.

        查询租户指定ID批量异步任务详情响应体。

        :return: The jobs of this ListAsyncJobDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobDetailResp`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListAsyncJobDetailResponse.

        查询租户指定ID批量异步任务详情响应体。

        :param jobs: The jobs of this ListAsyncJobDetailResponse.
        :type jobs: list[:class:`huaweicloudsdkdrs.v5.JobDetailResp`]
        """
        self._jobs = jobs

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
        if not isinstance(other, ListAsyncJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
