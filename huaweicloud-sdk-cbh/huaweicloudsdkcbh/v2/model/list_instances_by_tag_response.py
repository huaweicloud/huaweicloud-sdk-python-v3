# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesByTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resources]',
        'total_count': 'int'
    }

    attribute_map = {
        'resources': 'resources',
        'total_count': 'total_count'
    }

    def __init__(self, resources=None, total_count=None):
        """ListInstancesByTagResponse

        The model defined in huaweicloud sdk

        :param resources: 根据查询模式获取到的资源实例详情。
        :type resources: list[:class:`huaweicloudsdkcbh.v2.Resources`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListInstancesByTagResponse, self).__init__()

        self._resources = None
        self._total_count = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if total_count is not None:
            self.total_count = total_count

    @property
    def resources(self):
        """Gets the resources of this ListInstancesByTagResponse.

        根据查询模式获取到的资源实例详情。

        :return: The resources of this ListInstancesByTagResponse.
        :rtype: list[:class:`huaweicloudsdkcbh.v2.Resources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListInstancesByTagResponse.

        根据查询模式获取到的资源实例详情。

        :param resources: The resources of this ListInstancesByTagResponse.
        :type resources: list[:class:`huaweicloudsdkcbh.v2.Resources`]
        """
        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListInstancesByTagResponse.

        总记录数。

        :return: The total_count of this ListInstancesByTagResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListInstancesByTagResponse.

        总记录数。

        :param total_count: The total_count of this ListInstancesByTagResponse.
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
        if not isinstance(other, ListInstancesByTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
