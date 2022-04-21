# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'all_counts': 'int',
        'results': 'list[DatabaseObjectResp]'
    }

    attribute_map = {
        'all_counts': 'all_counts',
        'results': 'results'
    }

    def __init__(self, all_counts=None, results=None):
        """BatchSetObjectsResponse

        The model defined in huaweicloud sdk

        :param all_counts: 总数
        :type all_counts: int
        :param results: 批量对象选择响应列表
        :type results: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectResp`]
        """
        
        super(BatchSetObjectsResponse, self).__init__()

        self._all_counts = None
        self._results = None
        self.discriminator = None

        if all_counts is not None:
            self.all_counts = all_counts
        if results is not None:
            self.results = results

    @property
    def all_counts(self):
        """Gets the all_counts of this BatchSetObjectsResponse.

        总数

        :return: The all_counts of this BatchSetObjectsResponse.
        :rtype: int
        """
        return self._all_counts

    @all_counts.setter
    def all_counts(self, all_counts):
        """Sets the all_counts of this BatchSetObjectsResponse.

        总数

        :param all_counts: The all_counts of this BatchSetObjectsResponse.
        :type all_counts: int
        """
        self._all_counts = all_counts

    @property
    def results(self):
        """Gets the results of this BatchSetObjectsResponse.

        批量对象选择响应列表

        :return: The results of this BatchSetObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectResp`]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchSetObjectsResponse.

        批量对象选择响应列表

        :param results: The results of this BatchSetObjectsResponse.
        :type results: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectResp`]
        """
        self._results = results

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
        if not isinstance(other, BatchSetObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
