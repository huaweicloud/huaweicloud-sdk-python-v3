# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRemoveEndpointServicePermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[EpsPermission]'
    }

    attribute_map = {
        'permissions': 'permissions'
    }

    def __init__(self, permissions=None):
        r"""BatchRemoveEndpointServicePermissionsResponse

        The model defined in huaweicloud sdk

        :param permissions: 终端节点服务白名单
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.EpsPermission`]
        """
        
        super(BatchRemoveEndpointServicePermissionsResponse, self).__init__()

        self._permissions = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions

    @property
    def permissions(self):
        r"""Gets the permissions of this BatchRemoveEndpointServicePermissionsResponse.

        终端节点服务白名单

        :return: The permissions of this BatchRemoveEndpointServicePermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.EpsPermission`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this BatchRemoveEndpointServicePermissionsResponse.

        终端节点服务白名单

        :param permissions: The permissions of this BatchRemoveEndpointServicePermissionsResponse.
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.EpsPermission`]
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
        if not isinstance(other, BatchRemoveEndpointServicePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
