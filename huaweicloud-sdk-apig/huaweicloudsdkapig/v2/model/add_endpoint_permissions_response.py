# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddEndpointPermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'x_request_id': 'x-request-id'
    }

    def __init__(self, permissions=None, x_request_id=None):
        r"""AddEndpointPermissionsResponse

        The model defined in huaweicloud sdk

        :param permissions: 白名单记录列表。每个白名单记录的格式为iam:domain::授权账号ID。  其中，授权账号ID是长度为32的字符串，只包含英文字母（a-f）或数字；也可为*，表示允许全部用户连接。
        :type permissions: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(AddEndpointPermissionsResponse, self).__init__()

        self._permissions = None
        self._x_request_id = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def permissions(self):
        r"""Gets the permissions of this AddEndpointPermissionsResponse.

        白名单记录列表。每个白名单记录的格式为iam:domain::授权账号ID。  其中，授权账号ID是长度为32的字符串，只包含英文字母（a-f）或数字；也可为*，表示允许全部用户连接。

        :return: The permissions of this AddEndpointPermissionsResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this AddEndpointPermissionsResponse.

        白名单记录列表。每个白名单记录的格式为iam:domain::授权账号ID。  其中，授权账号ID是长度为32的字符串，只包含英文字母（a-f）或数字；也可为*，表示允许全部用户连接。

        :param permissions: The permissions of this AddEndpointPermissionsResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this AddEndpointPermissionsResponse.

        :return: The x_request_id of this AddEndpointPermissionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this AddEndpointPermissionsResponse.

        :param x_request_id: The x_request_id of this AddEndpointPermissionsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, AddEndpointPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
