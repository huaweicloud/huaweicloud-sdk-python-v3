# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrRemoveServicePermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]'
    }

    attribute_map = {
        'permissions': 'permissions'
    }

    def __init__(self, permissions=None):
        """AddOrRemoveServicePermissionsResponse

        The model defined in huaweicloud sdk

        :param permissions: permission列表。 权限格式为iam:domain::6e9dfd51d1124e8d8498dce894923a0d或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。
        :type permissions: list[str]
        """
        
        super(AddOrRemoveServicePermissionsResponse, self).__init__()

        self._permissions = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions

    @property
    def permissions(self):
        """Gets the permissions of this AddOrRemoveServicePermissionsResponse.

        permission列表。 权限格式为iam:domain::6e9dfd51d1124e8d8498dce894923a0d或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。

        :return: The permissions of this AddOrRemoveServicePermissionsResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AddOrRemoveServicePermissionsResponse.

        permission列表。 权限格式为iam:domain::6e9dfd51d1124e8d8498dce894923a0d或“*”， “*”表示所有用户的终端节点可连接。 其中6e9dfd51d1124e8d8498dce894923a0d为可连接的用户domian_id。

        :param permissions: The permissions of this AddOrRemoveServicePermissionsResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

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
        if not isinstance(other, AddOrRemoveServicePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
