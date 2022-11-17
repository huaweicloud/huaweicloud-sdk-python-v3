# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRunsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'runs': 'list[Run]'
    }

    attribute_map = {
        'count': 'count',
        'runs': 'runs'
    }

    def __init__(self, count=None, runs=None):
        """ListRunsResponse

        The model defined in huaweicloud sdk

        :param count: 作业总个数。
        :type count: int
        :param runs: 作业运行列表。
        :type runs: list[:class:`huaweicloudsdkiotanalytics.v1.Run`]
        """
        
        super(ListRunsResponse, self).__init__()

        self._count = None
        self._runs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if runs is not None:
            self.runs = runs

    @property
    def count(self):
        """Gets the count of this ListRunsResponse.

        作业总个数。

        :return: The count of this ListRunsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRunsResponse.

        作业总个数。

        :param count: The count of this ListRunsResponse.
        :type count: int
        """
        self._count = count

    @property
    def runs(self):
        """Gets the runs of this ListRunsResponse.

        作业运行列表。

        :return: The runs of this ListRunsResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Run`]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this ListRunsResponse.

        作业运行列表。

        :param runs: The runs of this ListRunsResponse.
        :type runs: list[:class:`huaweicloudsdkiotanalytics.v1.Run`]
        """
        self._runs = runs

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
        if not isinstance(other, ListRunsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
