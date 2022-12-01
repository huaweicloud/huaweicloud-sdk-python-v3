# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLinksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_links': 'list[JobLinkResp]',
        'total_count': 'int'
    }

    attribute_map = {
        'job_links': 'job_links',
        'total_count': 'total_count'
    }

    def __init__(self, job_links=None, total_count=None):
        """ListLinksResponse

        The model defined in huaweicloud sdk

        :param job_links: 可用链路信息。
        :type job_links: list[:class:`huaweicloudsdkdrs.v5.JobLinkResp`]
        :param total_count: 可用链路总条数。
        :type total_count: int
        """
        
        super(ListLinksResponse, self).__init__()

        self._job_links = None
        self._total_count = None
        self.discriminator = None

        if job_links is not None:
            self.job_links = job_links
        if total_count is not None:
            self.total_count = total_count

    @property
    def job_links(self):
        """Gets the job_links of this ListLinksResponse.

        可用链路信息。

        :return: The job_links of this ListLinksResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobLinkResp`]
        """
        return self._job_links

    @job_links.setter
    def job_links(self, job_links):
        """Sets the job_links of this ListLinksResponse.

        可用链路信息。

        :param job_links: The job_links of this ListLinksResponse.
        :type job_links: list[:class:`huaweicloudsdkdrs.v5.JobLinkResp`]
        """
        self._job_links = job_links

    @property
    def total_count(self):
        """Gets the total_count of this ListLinksResponse.

        可用链路总条数。

        :return: The total_count of this ListLinksResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListLinksResponse.

        可用链路总条数。

        :param total_count: The total_count of this ListLinksResponse.
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
        if not isinstance(other, ListLinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
