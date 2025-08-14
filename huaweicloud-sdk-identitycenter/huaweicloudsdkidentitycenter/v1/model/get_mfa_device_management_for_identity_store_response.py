# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetMfaDeviceManagementForIdentityStoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'user_permission': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'user_permission': 'user_permission'
    }

    def __init__(self, identity_store_id=None, user_permission=None):
        r"""GetMfaDeviceManagementForIdentityStoreResponse

        The model defined in huaweicloud sdk

        :param identity_store_id: 关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。
        :type identity_store_id: str
        :param user_permission: 允许用户自行操作的MFA行为
        :type user_permission: str
        """
        
        super(GetMfaDeviceManagementForIdentityStoreResponse, self).__init__()

        self._identity_store_id = None
        self._user_permission = None
        self.discriminator = None

        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if user_permission is not None:
            self.user_permission = user_permission

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this GetMfaDeviceManagementForIdentityStoreResponse.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :return: The identity_store_id of this GetMfaDeviceManagementForIdentityStoreResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this GetMfaDeviceManagementForIdentityStoreResponse.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :param identity_store_id: The identity_store_id of this GetMfaDeviceManagementForIdentityStoreResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_permission(self):
        r"""Gets the user_permission of this GetMfaDeviceManagementForIdentityStoreResponse.

        允许用户自行操作的MFA行为

        :return: The user_permission of this GetMfaDeviceManagementForIdentityStoreResponse.
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        r"""Sets the user_permission of this GetMfaDeviceManagementForIdentityStoreResponse.

        允许用户自行操作的MFA行为

        :param user_permission: The user_permission of this GetMfaDeviceManagementForIdentityStoreResponse.
        :type user_permission: str
        """
        self._user_permission = user_permission

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
        if not isinstance(other, GetMfaDeviceManagementForIdentityStoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
