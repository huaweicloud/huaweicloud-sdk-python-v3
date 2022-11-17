# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComputingResourcesResponse(SdkResponse):

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
        'computing_resources': 'list[ComputingResource]'
    }

    attribute_map = {
        'count': 'count',
        'computing_resources': 'computing_resources'
    }

    def __init__(self, count=None, computing_resources=None):
        """ListComputingResourcesResponse

        The model defined in huaweicloud sdk

        :param count: 计算资源总个数。
        :type count: int
        :param computing_resources: 计算资源列表。
        :type computing_resources: list[:class:`huaweicloudsdkiotanalytics.v1.ComputingResource`]
        """
        
        super(ListComputingResourcesResponse, self).__init__()

        self._count = None
        self._computing_resources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if computing_resources is not None:
            self.computing_resources = computing_resources

    @property
    def count(self):
        """Gets the count of this ListComputingResourcesResponse.

        计算资源总个数。

        :return: The count of this ListComputingResourcesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListComputingResourcesResponse.

        计算资源总个数。

        :param count: The count of this ListComputingResourcesResponse.
        :type count: int
        """
        self._count = count

    @property
    def computing_resources(self):
        """Gets the computing_resources of this ListComputingResourcesResponse.

        计算资源列表。

        :return: The computing_resources of this ListComputingResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.ComputingResource`]
        """
        return self._computing_resources

    @computing_resources.setter
    def computing_resources(self, computing_resources):
        """Sets the computing_resources of this ListComputingResourcesResponse.

        计算资源列表。

        :param computing_resources: The computing_resources of this ListComputingResourcesResponse.
        :type computing_resources: list[:class:`huaweicloudsdkiotanalytics.v1.ComputingResource`]
        """
        self._computing_resources = computing_resources

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
        if not isinstance(other, ListComputingResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
