# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set': 'PermissionSetDto'
    }

    attribute_map = {
        'permission_set': 'permission_set'
    }

    def __init__(self, permission_set=None):
        r"""CreatePermissionSetResponse

        The model defined in huaweicloud sdk

        :param permission_set: 
        :type permission_set: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetDto`
        """
        
        super(CreatePermissionSetResponse, self).__init__()

        self._permission_set = None
        self.discriminator = None

        if permission_set is not None:
            self.permission_set = permission_set

    @property
    def permission_set(self):
        r"""Gets the permission_set of this CreatePermissionSetResponse.

        :return: The permission_set of this CreatePermissionSetResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetDto`
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        r"""Sets the permission_set of this CreatePermissionSetResponse.

        :param permission_set: The permission_set of this CreatePermissionSetResponse.
        :type permission_set: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetDto`
        """
        self._permission_set = permission_set

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
        if not isinstance(other, CreatePermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
