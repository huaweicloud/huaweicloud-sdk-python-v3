# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCheckJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[PostPreCheckResp]',
        'count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'count': 'count'
    }

    def __init__(self, results=None, count=None):
        """BatchCheckJobsResponse

        The model defined in huaweicloud sdk

        :param results: 预检查响应体
        :type results: list[:class:`huaweicloudsdkdrs.v3.PostPreCheckResp`]
        :param count: 总数
        :type count: int
        """
        
        super(BatchCheckJobsResponse, self).__init__()

        self._results = None
        self._count = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if count is not None:
            self.count = count

    @property
    def results(self):
        """Gets the results of this BatchCheckJobsResponse.

        预检查响应体

        :return: The results of this BatchCheckJobsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.PostPreCheckResp`]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchCheckJobsResponse.

        预检查响应体

        :param results: The results of this BatchCheckJobsResponse.
        :type results: list[:class:`huaweicloudsdkdrs.v3.PostPreCheckResp`]
        """
        self._results = results

    @property
    def count(self):
        """Gets the count of this BatchCheckJobsResponse.

        总数

        :return: The count of this BatchCheckJobsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchCheckJobsResponse.

        总数

        :param count: The count of this BatchCheckJobsResponse.
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
        if not isinstance(other, BatchCheckJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
