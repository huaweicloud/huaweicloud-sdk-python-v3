# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceGroupsResponse(SdkResponse):

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
        'resource_groups': 'list[OneResourceGroupResp]'
    }

    attribute_map = {
        'count': 'count',
        'resource_groups': 'resource_groups'
    }

    def __init__(self, count=None, resource_groups=None):
        """ListResourceGroupsResponse

        The model defined in huaweicloud sdk

        :param count: 资源分组总数
        :type count: int
        :param resource_groups: 资源分组列表
        :type resource_groups: list[:class:`huaweicloudsdkces.v2.OneResourceGroupResp`]
        """
        
        super(ListResourceGroupsResponse, self).__init__()

        self._count = None
        self._resource_groups = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if resource_groups is not None:
            self.resource_groups = resource_groups

    @property
    def count(self):
        """Gets the count of this ListResourceGroupsResponse.

        资源分组总数

        :return: The count of this ListResourceGroupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListResourceGroupsResponse.

        资源分组总数

        :param count: The count of this ListResourceGroupsResponse.
        :type count: int
        """
        self._count = count

    @property
    def resource_groups(self):
        """Gets the resource_groups of this ListResourceGroupsResponse.

        资源分组列表

        :return: The resource_groups of this ListResourceGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.OneResourceGroupResp`]
        """
        return self._resource_groups

    @resource_groups.setter
    def resource_groups(self, resource_groups):
        """Sets the resource_groups of this ListResourceGroupsResponse.

        资源分组列表

        :param resource_groups: The resource_groups of this ListResourceGroupsResponse.
        :type resource_groups: list[:class:`huaweicloudsdkces.v2.OneResourceGroupResp`]
        """
        self._resource_groups = resource_groups

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
        if not isinstance(other, ListResourceGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
