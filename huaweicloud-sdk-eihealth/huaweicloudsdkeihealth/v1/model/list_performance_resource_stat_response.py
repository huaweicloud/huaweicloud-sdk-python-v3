# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPerformanceResourceStatResponse(SdkResponse):

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
        'performance_resources': 'list[PerformanceResourcesRsp]'
    }

    attribute_map = {
        'count': 'count',
        'performance_resources': 'performance_resources'
    }

    def __init__(self, count=None, performance_resources=None):
        """ListPerformanceResourceStatResponse

        The model defined in huaweicloud sdk

        :param count: 性能加速资源总数
        :type count: int
        :param performance_resources: 性能加速资源信息
        :type performance_resources: list[:class:`huaweicloudsdkeihealth.v1.PerformanceResourcesRsp`]
        """
        
        super(ListPerformanceResourceStatResponse, self).__init__()

        self._count = None
        self._performance_resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if performance_resources is not None:
            self.performance_resources = performance_resources

    @property
    def count(self):
        """Gets the count of this ListPerformanceResourceStatResponse.

        性能加速资源总数

        :return: The count of this ListPerformanceResourceStatResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListPerformanceResourceStatResponse.

        性能加速资源总数

        :param count: The count of this ListPerformanceResourceStatResponse.
        :type count: int
        """
        self._count = count

    @property
    def performance_resources(self):
        """Gets the performance_resources of this ListPerformanceResourceStatResponse.

        性能加速资源信息

        :return: The performance_resources of this ListPerformanceResourceStatResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.PerformanceResourcesRsp`]
        """
        return self._performance_resources

    @performance_resources.setter
    def performance_resources(self, performance_resources):
        """Sets the performance_resources of this ListPerformanceResourceStatResponse.

        性能加速资源信息

        :param performance_resources: The performance_resources of this ListPerformanceResourceStatResponse.
        :type performance_resources: list[:class:`huaweicloudsdkeihealth.v1.PerformanceResourcesRsp`]
        """
        self._performance_resources = performance_resources

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
        if not isinstance(other, ListPerformanceResourceStatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
