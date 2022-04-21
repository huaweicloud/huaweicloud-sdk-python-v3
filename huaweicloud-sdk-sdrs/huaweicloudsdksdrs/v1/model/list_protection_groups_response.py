# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_groups': 'list[ShowProtectionGroupParams]',
        'count': 'int'
    }

    attribute_map = {
        'server_groups': 'server_groups',
        'count': 'count'
    }

    def __init__(self, server_groups=None, count=None):
        """ListProtectionGroupsResponse

        The model defined in huaweicloud sdk

        :param server_groups: 保护组的信息列表。
        :type server_groups: list[:class:`huaweicloudsdksdrs.v1.ShowProtectionGroupParams`]
        :param count: 此参数为满足过滤条件的列表中包含的保护组个数。
        :type count: int
        """
        
        super(ListProtectionGroupsResponse, self).__init__()

        self._server_groups = None
        self._count = None
        self.discriminator = None

        if server_groups is not None:
            self.server_groups = server_groups
        if count is not None:
            self.count = count

    @property
    def server_groups(self):
        """Gets the server_groups of this ListProtectionGroupsResponse.

        保护组的信息列表。

        :return: The server_groups of this ListProtectionGroupsResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ShowProtectionGroupParams`]
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this ListProtectionGroupsResponse.

        保护组的信息列表。

        :param server_groups: The server_groups of this ListProtectionGroupsResponse.
        :type server_groups: list[:class:`huaweicloudsdksdrs.v1.ShowProtectionGroupParams`]
        """
        self._server_groups = server_groups

    @property
    def count(self):
        """Gets the count of this ListProtectionGroupsResponse.

        此参数为满足过滤条件的列表中包含的保护组个数。

        :return: The count of this ListProtectionGroupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProtectionGroupsResponse.

        此参数为满足过滤条件的列表中包含的保护组个数。

        :param count: The count of this ListProtectionGroupsResponse.
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
        if not isinstance(other, ListProtectionGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
